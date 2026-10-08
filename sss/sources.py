"""Part 1: the source replica. Copy mode vendors the skills_root subtree letter for
letter; submodule mode pins a git submodule; local mode is the repo's own skills."""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from . import gitutil
from .manifest import Manifest, ManifestError, Source, now_iso

LICENSE_NAMES = ("LICENSE", "LICENSE.md", "LICENSE.txt", "NOTICE", "NOTICE.md", "NOTICE.txt")


def add(m: Manifest, name: str, url: str | None, ref: str, mode: str, skills_root: str) -> Source:
    if any(s.name == name for s in m.sources):
        raise ManifestError(f"source already exists: {name}")
    if mode != "local" and not url:
        raise ManifestError("url is required unless mode is local")
    if mode == "local" and skills_root == "skills":
        skills_root = "."   # local skills live directly under .sss/local/<skill>/
    src = Source(name=name, url=url, ref=ref, mode=mode, skills_root=skills_root)
    m.sources.append(src)
    if mode == "local":
        (m.root / src.path).mkdir(parents=True, exist_ok=True)
    m.save()
    return src


def sync(m: Manifest, src: Source) -> dict:
    """Refresh the replica. Returns {"changed": bool, "old": sha, "new": sha}."""
    old = src.synced_commit
    if src.mode == "local":
        return {"source": src.name, "changed": False, "old": old, "new": old}
    if src.mode == "submodule":
        new = _sync_submodule(m, src)
    else:
        new = _sync_copy(m, src)
    src.synced_commit = new
    src.synced_at = now_iso()
    m.save()
    return {"source": src.name, "changed": new != old, "old": old, "new": new}


def _sync_copy(m: Manifest, src: Source) -> str:
    dest = m.root / src.path
    with tempfile.TemporaryDirectory(prefix="sss-src-") as tmp:
        clone = Path(tmp) / "clone"
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", "--branch", src.ref, src.url, str(clone)],
            check=True, capture_output=True, text=True,
        )
        sha = gitutil.head(clone) or ""
        root = src.skills_root.strip("/")
        subtree = clone / root if root and root != "." else clone
        if not subtree.is_dir():
            raise ManifestError(f"source {src.name}: skills_root {src.skills_root!r} not found at {src.url}")
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)
        target = dest / root if root and root != "." else dest
        shutil.copytree(subtree, target, symlinks=False, ignore=shutil.ignore_patterns(".git"))
        for lic in LICENSE_NAMES:
            if (clone / lic).is_file():
                shutil.copy2(clone / lic, dest / lic)
        (dest / ".sss-replica").write_text(
            f"Letter-for-letter replica of {src.url} @ {sha} ({src.skills_root}). Do not edit.\n",
            encoding="utf-8",
        )
    return sha


def _sync_submodule(m: Manifest, src: Source) -> str:
    sub = m.root / src.path
    if not (sub / ".git").exists():
        subprocess.run(
            ["git", "submodule", "add", "-b", src.ref, src.url, src.path],
            cwd=str(m.root), check=True, capture_output=True, text=True,
        )
    else:
        subprocess.run(
            ["git", "submodule", "update", "--remote", "--", src.path],
            cwd=str(m.root), check=True, capture_output=True, text=True,
        )
    return gitutil.head(sub) or ""


def list_skill_dirs(m: Manifest, src: Source) -> list[str]:
    root = m.root / src.path
    base = root / src.skills_root.strip("/") if src.skills_root.strip("/") not in ("", ".") else root
    if not base.is_dir():
        return []
    out = []
    for d in sorted(base.iterdir()):
        if d.is_dir() and (d / "SKILL.md").is_file():
            out.append(d.name)
    return out
