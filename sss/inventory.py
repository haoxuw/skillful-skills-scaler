"""Reorganize step 0: find every skill in the repo and the cheap facts about it.
The model only judges candidates this module surfaces."""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
from itertools import combinations
from pathlib import Path

from . import frontmatter, sources as srcmod, status as statusmod
from .manifest import Manifest, SOURCES_DIR, TOOL_DIR

SKIP_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build"}
_LINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+)[^)]*\)|`((?:\./|\.\./|/)?[\w./-]+\.(?:md|sh|py|yaml|yml|json|txt))`")
_TICK = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")
_HEAD = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
_WORD = re.compile(r"[a-z0-9]+")
STOP = {"the", "a", "an", "and", "or", "for", "to", "of", "in", "on", "with", "this", "that", "skill", "skills", "use", "when",
        "how", "is", "are", "it", "you", "your", "using", "don", "not", "do", "from", "by", "as", "be", "into", "guide", "fork", "old", "new", "v2", "copy"}


def _tokens(*texts: str) -> set[str]:
    toks = set()
    for t in texts:
        toks.update(w for w in _WORD.findall((t or "").lower()) if w not in STOP and len(w) > 1)
    return toks


def _jaccard(a: set[str], b: set[str]) -> float:
    return len(a & b) / len(a | b) if a or b else 0.0


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
        refs, broken = _references(d, body)
        rel = os.path.relpath(d, root)
        sid = str(meta.get("name") or d.name)
        st = managed_status.get(sid, {})
        skills.append({
            "id": sid,
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
        })
    present = {s["id"] for s in skills} | {s["dir_name"] for s in skills}
    for s in skills:
        missing = []
        for name in s["mentions_skills"]:
            if name in present or name == s["id"]:
                continue
            if name in available:
                missing.append({"skill": name, "available_from": available[name]})
        for b in s["broken_references"]:
            head = b.split("/")[0]
            if head in available and head not in present:
                entry = {"skill": head, "available_from": available[head]}
                if entry not in missing:
                    missing.append(entry)
        s["missing_dependencies"] = missing
    return {"root": str(root), "skills": skills, "candidates": candidates(skills)}


def _references(d: Path, body: str) -> tuple[list[str], list[str]]:
    refs, broken = [], []
    for mm in _LINK.finditer(body):
        target = mm.group(1) or mm.group(2)
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        refs.append(target)
        p = (d / target) if not target.startswith("/") else (d.parents[len(d.parents) - 1] / target.lstrip("/"))
        if not p.exists():
            broken.append(target)
    return refs, broken


def candidates(skills: list[dict]) -> list[dict]:
    """Cheap duplicate candidates. Identical body is certain. Otherwise a pair is a
    candidate when names overlap, descriptions overlap, or headings overlap."""
    out = []
    by_sha: dict[str, list[str]] = {}
    for s in skills:
        by_sha.setdefault(s["body_sha"], []).append(s["id"])
    for ids in by_sha.values():
        if len(ids) > 1:
            out.append({"kind": "identical_body", "skills": sorted(ids), "score": 1.0, "why": "same text"})
    name_t = {s["id"]: _tokens(s["id"].replace("-", " "), s["dir_name"].replace("-", " ")) for s in skills}
    desc_t = {s["id"]: _tokens(s["description"]) for s in skills}
    head_t = {s["id"]: _tokens(*s.get("headings", [])) for s in skills}
    for a, b in combinations(skills, 2):
        if a["body_sha"] == b["body_sha"]:
            continue
        n = _jaccard(name_t[a["id"]], name_t[b["id"]])
        d = _jaccard(desc_t[a["id"]], desc_t[b["id"]])
        h = _jaccard(head_t[a["id"]], head_t[b["id"]])
        why = []
        if n >= 0.5:
            why.append(f"names overlap {n:.2f}")
        if d >= 0.3:
            why.append(f"descriptions overlap {d:.2f}")
        if h >= 0.4 and len(head_t[a["id"]] | head_t[b["id"]]) >= 4:
            why.append(f"headings overlap {h:.2f}")
        if why:
            out.append({"kind": "similar", "skills": sorted([a["id"], b["id"]]), "score": round(max(n, d, h), 2), "why": "; ".join(why)})
    return sorted(out, key=lambda c: -c["score"])
