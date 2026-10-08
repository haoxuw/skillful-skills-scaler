"""Reorganize step 0: find every skill in the repo and the cheap facts about it.
The model only judges candidates this module surfaces."""
from __future__ import annotations

import hashlib
import os
import re
from itertools import combinations
from pathlib import Path

from . import frontmatter
from .manifest import Manifest, SOURCES_DIR, TOOL_DIR

SKIP_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build"}
_LINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+)[^)]*\)|`((?:\./|\.\./|/)?[\w./-]+\.(?:md|sh|py|yaml|yml|json|txt))`")
_WORD = re.compile(r"[a-z0-9]+")
STOP = {"the", "a", "an", "and", "or", "for", "to", "of", "in", "on", "with", "this", "that", "skill", "use", "when", "how", "is", "are", "it", "you", "your"}


def _tokens(*texts: str) -> set[str]:
    toks = set()
    for t in texts:
        toks.update(w for w in _WORD.findall((t or "").lower()) if w not in STOP and len(w) > 2)
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


def scan(m: Manifest | None, root: Path) -> dict:
    exclude = [SOURCES_DIR, TOOL_DIR, ".sss/local"]
    mirrors = m.mirror_dirs if m else []
    exclude += mirrors  # real dirs live in output_dir; mirrors are links
    skills = []
    for d in find_skill_dirs(root, exclude):
        meta, body = frontmatter.read(d / "SKILL.md")
        files = [p for p in d.rglob("*") if p.is_file()]
        words = sum(len(p.read_text(encoding="utf-8", errors="replace").split()) for p in files if p.suffix.lower() in (".md", ".txt"))
        prov = (meta.get("metadata") or {}).get("sss") if isinstance(meta.get("metadata"), dict) else None
        refs, broken = _references(d, body)
        skills.append({
            "id": str(meta.get("name") or d.name),
            "dir_name": d.name,
            "path": os.path.relpath(d, root),
            "source": (prov or {}).get("source", "local"),
            "managed": bool(prov),
            "description": str(meta.get("description", "")).strip(),
            "files": len(files),
            "words": words,
            "body_sha": hashlib.sha256(body.strip().encode()).hexdigest()[:12],
            "references": refs,
            "broken_references": broken,
        })
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


def candidates(skills: list[dict], threshold: float = 0.35) -> list[dict]:
    """Cheap duplicate candidates. Exact body match is certain; token overlap is a hint."""
    out = []
    by_sha: dict[str, list[str]] = {}
    for s in skills:
        by_sha.setdefault(s["body_sha"], []).append(s["id"])
    for sha, ids in by_sha.items():
        if len(ids) > 1:
            out.append({"kind": "identical_body", "skills": sorted(ids), "score": 1.0})
    toks = {s["id"]: _tokens(s["id"].replace("-", " "), s["description"]) for s in skills}
    for a, b in combinations(skills, 2):
        if a["body_sha"] == b["body_sha"]:
            continue
        score = _jaccard(toks[a["id"]], toks[b["id"]])
        if score >= threshold:
            out.append({"kind": "similar_name_or_description", "skills": sorted([a["id"], b["id"]]), "score": round(score, 2)})
    return sorted(out, key=lambda c: -c["score"])
