"""Reorganize step 0: find every skill in the repo and the cheap facts about it.
The model only judges candidates this module surfaces."""
from __future__ import annotations

import hashlib
import math
import os
import re
import subprocess
from collections import Counter
from itertools import combinations
from pathlib import Path

from . import frontmatter, sources as srcmod, status as statusmod
from .manifest import Manifest, SOURCES_DIR, TOOL_DIR

SKIP_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build"}
_MDLINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+)[^)]*\)")
_TICKPATH = re.compile(r"`((?:\./|\.\./)?[\w.-]+(?:/[\w.-]+)+\.(?:md|sh|py|yaml|yml|json|txt|toml|tf))`")
_TICK = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")
_HEAD = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
_WORD = re.compile(r"[a-z0-9]+")
STOP = {"the", "a", "an", "and", "or", "for", "to", "of", "in", "on", "with", "this", "that", "skill", "skills", "use", "when",
        "how", "is", "are", "it", "you", "your", "using", "don", "not", "do", "from", "by", "as", "be", "into", "guide", "fork",
        "old", "new", "v2", "copy", "t", "s"}


def _tokens(*texts: str) -> set[str]:
    toks = set()
    for t in texts:
        toks.update(w for w in _WORD.findall((t or "").lower()) if w not in STOP and len(w) > 1)
    return toks


def _weighted_jaccard(a: set[str], b: set[str], w: dict[str, float]) -> float:
    inter = sum(w.get(t, 1.0) for t in a & b)
    union = sum(w.get(t, 1.0) for t in a | b)
    return inter / union if union else 0.0


def _idf(sets: list[set[str]]) -> dict[str, float]:
    """Tokens shared by many skills (a family prefix like 'google cloud waf', or a
    heading like 'Usage') say little about any one pair."""
    n = max(len(sets), 1)
    df = Counter(t for s in sets for t in s)
    return {t: math.log((n + 1) / (c + 1)) + 0.1 for t, c in df.items()}


def find_skill_dirs(root: Path, exclude: list[str]) -> list[Path]:
    ex = {os.path.realpath(root / e) for e in exclude}
    found: dict[str, Path] = {}
    for dirpath, dirnames, filenames in os.walk(root, followlinks=True):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and os.path.realpath(os.path.join(dirpath, d)) not in ex]
        if "SKILL.md" in filenames:
            real = os.path.realpath(dirpath)
            if real in ex or any(real.startswith(e + os.sep) for e in ex):
                continue
            found.setdefault(real, Path(dirpath))   # dedupe symlinked mirrors
            dirnames[:] = []                         # skills do not nest
    return sorted(found.values(), key=lambda p: str(p))


def _last_changed(root: Path, rel: str) -> str | None:
    proc = subprocess.run(["git", "log", "-1", "--format=%cs", "--", rel], cwd=str(root), capture_output=True, text=True)
    return proc.stdout.strip() or None


def scan(m: Manifest | None, root: Path) -> dict:
    exclude = [SOURCES_DIR, TOOL_DIR, ".sss/local"]
    exclude += (m.mirror_dirs if m else [])  # real dirs live in output_dir; mirrors are links
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
            "body_sha": hashlib.sha256(body.strip().encode()).hexdigest()[:12],
            "headings": _HEAD.findall(body)[:40],
            "references": refs,
            "broken_references": broken,
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
    return {"root": str(root), "skills": skills, "candidates": candidates(skills), "same_name": [n for n, c in counts.items() if c > 1]}


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


def candidates(skills: list[dict]) -> list[dict]:
    """Cheap duplicate candidates. Identical body is certain. Otherwise a pair is a
    candidate when the distinguishing parts of their names, descriptions or
    headings overlap, after down-weighting tokens common to many skills."""
    out = []
    by_sha: dict[str, list[str]] = {}
    for s in skills:
        by_sha.setdefault(s["body_sha"], []).append(s["id"])
    for ids in by_sha.values():
        if len(ids) > 1:
            out.append({"kind": "identical_body", "skills": sorted(ids), "score": 1.0, "why": "same text"})
    name_t = {s["id"]: _tokens(s["name"].replace("-", " "), s["dir_name"].replace("-", " ")) for s in skills}
    desc_t = {s["id"]: _tokens(s["description"]) for s in skills}
    head_t = {s["id"]: _tokens(*s.get("headings", [])) for s in skills}
    wn, wd, wh = _idf(list(name_t.values())), _idf(list(desc_t.values())), _idf(list(head_t.values()))
    for a, b in combinations(skills, 2):
        if a["body_sha"] == b["body_sha"]:
            continue
        n = _weighted_jaccard(name_t[a["id"]], name_t[b["id"]], wn)
        d = _weighted_jaccard(desc_t[a["id"]], desc_t[b["id"]], wd)
        h = _weighted_jaccard(head_t[a["id"]], head_t[b["id"]], wh)
        why = []
        if n >= 0.5:
            why.append(f"names overlap {n:.2f}")
        if d >= 0.35:
            why.append(f"descriptions overlap {d:.2f}")
        # Shared headings alone only mean a shared template; they count when the
        # names or descriptions also lean the same way.
        if h >= 0.5 and len(head_t[a["id"]] | head_t[b["id"]]) >= 6 and (n >= 0.35 or d >= 0.25):
            why.append(f"headings overlap {h:.2f}")
        if why:
            out.append({"kind": "similar", "skills": sorted([a["id"], b["id"]]), "score": round(max(n, d, h), 2), "why": "; ".join(why)})
    return sorted(out, key=lambda c: -c["score"])
