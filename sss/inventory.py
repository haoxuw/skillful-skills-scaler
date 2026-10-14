# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Reorganize step 0: find every skill in the repo and the cheap facts about it.
The model only judges candidates this module surfaces."""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
from collections import Counter
from pathlib import Path

from . import frontmatter, sources as srcmod, status as statusmod
from .manifest import Manifest, SOURCES_DIR, TOOL_DIR

SKIP_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build"}
_MDLINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+)[^)]*\)")
_TICKPATH = re.compile(r"`((?:\./|\.\./)?[\w.-]+(?:/[\w.-]+)+\.(?:md|sh|py|yaml|yml|json|txt|toml|tf))`")
_TICK = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")
_HEAD = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)


def find_skill_dirs(root: Path, exclude: list[str]) -> list[Path]:
    from .links import OWN_SKILLS  # SSS's own command skills are never inventory
    ex = {os.path.realpath(root / e) for e in exclude} | {os.path.realpath(OWN_SKILLS)}
    found: dict[str, Path] = {}
    for dirpath, dirnames, filenames in os.walk(root, followlinks=True):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and os.path.realpath(os.path.join(dirpath, d)) not in ex]
        if "SKILL.md" in filenames:
            real = os.path.realpath(dirpath)
            if real in ex or any(real.startswith(e + os.sep) for e in ex):
                continue
            # Dedupe symlinked mirrors, and always record the real location so the
            # path and git history do not depend on which link os.walk met first.
            root_real = os.path.realpath(root)
            where = Path(real) if real.startswith(root_real + os.sep) else Path(dirpath)
            found.setdefault(real, where)
            dirnames[:] = []                         # skills do not nest
    return sorted(found.values(), key=lambda p: str(p))


def _content_hash(d: Path, files: list[Path]) -> str:
    """Identity of a skill for caching and identical-content detection: every file
    in the folder by relative path and bytes, full SHA-256. SKILL.md is hashed
    without its `name` and without SSS's own provenance block, so a rename or a
    regeneration with the same content keeps the same identity. A change to a
    reference file, a script, the description or the body changes it."""
    import json as _json
    h = hashlib.sha256()
    for p in sorted(files, key=lambda x: str(x.relative_to(d))):
        rel = str(p.relative_to(d))
        h.update(rel.encode()); h.update(b"\0")
        if rel == "SKILL.md":
            meta, body = frontmatter.read(p)
            meta = {k: v for k, v in meta.items() if k != "name" and not str(k).startswith("_")}
            if isinstance(meta.get("metadata"), dict):
                meta["metadata"] = {k: v for k, v in meta["metadata"].items() if k != "sss"}
            h.update(_json.dumps(meta, sort_keys=True, default=str).encode()); h.update(b"\0")
            h.update(body.strip().encode())
        else:
            h.update(p.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def _last_changed(root: Path, rel: str) -> str | None:
    proc = subprocess.run(["git", "log", "-1", "--format=%cs", "--", rel], cwd=str(root), capture_output=True, text=True)
    return proc.stdout.strip() or None


def scan(m: Manifest | None, root: Path) -> dict:
    exclude = [SOURCES_DIR, TOOL_DIR, ".sss/local"]
    # Mirror dirs normally hold symlinks into skills_dir, which the realpath dedupe
    # below already collapses. Only exclude a mirror when it holds real copies
    # (link_mode: copy) and is not the output dir itself under another name.
    if m and m.link_mode == "copy":
        out_real = os.path.realpath(root / m.skills_dir)
        exclude += [d for d in m.mirror_dirs if os.path.realpath(root / d) != out_real]
    managed_status = {s["skill"]: s for s in statusmod.check_all(m)} if m else {}
    available: dict[str, list[str]] = {}
    if m:
        for src in m.sources:
            for d in srcmod.list_skill_dirs(m, src):
                available.setdefault(d.rsplit("/", 1)[-1], []).append(f"{src.name}/{d}")

    skills = []
    for d in find_skill_dirs(root, exclude):
        meta, body = frontmatter.read(d / "SKILL.md")
        files = [p for p in d.rglob("*") if p.is_file()]
        words = sum(len(p.read_text(encoding="utf-8", errors="replace").split()) for p in files if p.suffix.lower() in (".md", ".txt"))
        prov = (meta.get("metadata") or {}).get("sss") if isinstance(meta.get("metadata"), dict) else None
        refs, broken = _references(d, body, files)
        rel = os.path.relpath(d, root)
        name = str(meta.get("name") or d.name)
        st = managed_status.get(name, {})
        skills.append({
            "id": name,
            "name": name,
            "dir_name": d.name,
            "path": rel,
            "source": (prov or {}).get("source", "local"),
            "managed": bool(prov),
            "status": st.get("status", "unmanaged"),
            "status_reasons": st.get("reasons", []),
            "description": str(meta.get("description", "")).strip(),
            "version": str((meta.get("metadata") or {}).get("version", "")) if isinstance(meta.get("metadata"), dict) else "",
            "files": len(files),
            "words": words,
            "last_changed": _last_changed(root, rel),
            "body_sha": _content_hash(d, files),
            "headings": _HEAD.findall(body)[:40],
            "references": refs,
            "broken_references": broken,
            "frontmatter_error": meta.get("_frontmatter_error"),
            "mentions_skills": sorted(set(_TICK.findall(body))),
            "_body": body,
        })
    # Two skills with the same name must still be told apart in findings.
    counts = Counter(s["name"] for s in skills)
    for s in skills:
        if counts[s["name"]] > 1:
            s["id"] = f"{s['name']} ({s['path']})"
    present = {s["name"] for s in skills} | {s["dir_name"] for s in skills}
    # Mentions of known skill names anywhere in the text, backticked or not, with or
    # without a .md / /SKILL.md tail, in prose, comments or the description.
    known = sorted(set(available) | present, key=len, reverse=True)
    known_re = re.compile(r"(?<![\w-])(" + "|".join(re.escape(k) for k in known) + r")(?:\.md|/SKILL\.md)?(?![\w-])") if known else None
    for s in skills:
        if known_re:
            text = s["description"] + "\n" + s["_body"]
            s["mentions_skills"] = sorted(set(s["mentions_skills"]) | {mm.group(1) for mm in known_re.finditer(text)})
        del s["_body"]
        missing = []
        for nm in s["mentions_skills"]:
            if nm in present or nm == s["name"]:
                continue
            if nm in available:
                missing.append({"skill": nm, "available_from": available[nm]})
        for b in s["broken_references"]:
            head = b.split("/")[0]
            if head in available and head not in present:
                entry = {"skill": head, "available_from": available[head]}
                if entry not in missing:
                    missing.append(entry)
        s["missing_dependencies"] = missing
    return {"root": str(root), "skills": skills, "identical": identical(skills), "same_name": [n for n, c in counts.items() if c > 1]}


def _references(d: Path, body: str, files: list[Path]) -> tuple[list[str], list[str]]:
    """Markdown links and backticked relative paths count as references. A bare
    backticked filename is only a reference if such a file exists in the skill
    folder; otherwise it is just a name being mentioned."""
    refs, broken = [], []
    basenames = {p.name for p in files}
    seen = set()
    for mm in list(_MDLINK.finditer(body)) + list(_TICKPATH.finditer(body)):
        target = mm.group(1)
        if not target or target in seen or target.startswith(("http://", "https://", "mailto:", "/")):
            continue
        seen.add(target)
        refs.append(target)
        p = d / target
        if not p.exists() and os.path.basename(target) not in basenames:
            broken.append(target)
    return refs, broken


def identical(skills: list[dict]) -> list[dict]:
    """Groups of skills whose bodies are byte-for-byte the same. This is a fact,
    not a similarity guess; everything softer is scored by the model in the
    coverage matrix (see matrix.py)."""
    by_sha: dict[str, list[str]] = {}
    for s in skills:
        by_sha.setdefault(s["body_sha"], []).append(s["id"])
    return [{"skills": sorted(ids)} for ids in by_sha.values() if len(ids) > 1]
