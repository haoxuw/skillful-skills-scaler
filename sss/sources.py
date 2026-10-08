"""Part 1: the source replica. Copy mode vendors the skills_root subtree letter for
letter; submodule mode pins a git submodule; local mode is the repo's own skills."""
from __future__ import annotations

import os
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


def remove(m: Manifest, name: str, force: bool = False) -> dict:
    src = m.source(name)
    users = [k.name for k in m.skills if k.source == name]
    if users and not force:
        raise ManifestError(f"source {name} is used by: {', '.join(users)}. Deprecate them first, or pass --force.")
    m.sources = [s for s in m.sources if s.name != name]
    m.skills = [k for k in m.skills if k.source != name]
    m.save()
    removed = []
    if src.mode == "submodule":
        subprocess.run(["git", "submodule", "deinit", "-f", "--", src.path], cwd=str(m.root), capture_output=True, text=True)
        subprocess.run(["git", "rm", "-q", "-f", "--", src.path], cwd=str(m.root), capture_output=True, text=True)
        shutil.rmtree(m.root / ".git" / "modules" / src.path, ignore_errors=True)
        removed.append(src.path)
    elif src.mode == "copy" and (m.root / src.path).exists():
        shutil.rmtree(m.root / src.path)
        removed.append(src.path)
    return {"source": name, "removed": removed, "skills_dropped": users if force else []}


def sync(m: Manifest, src: Source) -> dict:
    """Refresh the replica. Returns {"changed": bool, "old": sha, "new": sha}."""
    old = src.synced_commit
    if src.mode == "local":
        return {"source": src.name, "changed": False, "old": old, "new": old}
    if src.mode == "submodule":
        new = _sync_submodule(m, src)
    else:
        new = _sync_copy(m, src)
    if new != old:
        src.synced_commit = new
        src.synced_at = now_iso()
        m.save()
    return {"source": src.name, "changed": new != old, "old": old, "new": new}


def _ignore_for_copy(dirpath: str, names: list[str]) -> set[str]:
    """Skip VCS and dependency folders, and symlinks whose target does not exist.
    (shutil's ignore_dangling_symlinks resolves relative targets against the cwd, so
    it misses links like `.agent/skills -> ../skills`.)"""
    skip = {".git", "node_modules"}
    out = {n for n in names if n in skip}
    for n in names:
        full = Path(dirpath) / n
        if full.is_symlink() and not full.exists():
            out.add(n)
    return out


def _sync_copy(m: Manifest, src: Source) -> str:
    dest = m.root / src.path
    with tempfile.TemporaryDirectory(prefix="sss-src-") as tmp:
        clone = Path(tmp) / "clone"
        proc = subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", "--branch", src.ref, src.url, str(clone)],
            capture_output=True, text=True,
        )
        if proc.returncode != 0:
            raise ManifestError(f"source {src.name}: clone failed: {proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else 'unknown error'}")
        sha = gitutil.head(clone) or ""
        root = src.skills_root.strip("/")
        subtree = clone / root if root and root != "." else clone
        if not subtree.is_dir():
            raise ManifestError(f"source {src.name}: skills_root {src.skills_root!r} not found at {src.url}")
        if dest.exists():
            shutil.rmtree(dest)
        target = dest / root if root and root != "." else dest
        shutil.copytree(subtree, target, symlinks=False, ignore=_ignore_for_copy)
        for lic in LICENSE_NAMES:
            if (clone / lic).is_file():
                shutil.copy2(clone / lic, dest / lic)
        (dest / ".sss-replica").write_text(
            f"Letter-for-letter replica of {src.url} @ {sha} ({src.skills_root}). Do not edit.\n",
            encoding="utf-8",
        )
    return sha


def _git_opts(url: str | None) -> list[str]:
    # Local sources (tests, monorepos) need the file transport, which git disables
    # for submodules by default.
    local = bool(url) and (url.startswith("file://") or url.startswith("/") or url.startswith("."))
    return ["-c", "protocol.file.allow=always"] if local else []


def _sync_submodule(m: Manifest, src: Source) -> str:
    sub = m.root / src.path
    if not (sub / ".git").exists():
        proc = subprocess.run(
            ["git", *_git_opts(src.url), "submodule", "add", "-b", src.ref, src.url, src.path],
            cwd=str(m.root), capture_output=True, text=True,
        )
    else:
        proc = subprocess.run(
            ["git", *_git_opts(src.url), "submodule", "update", "--remote", "--init", "--", src.path],
            cwd=str(m.root), capture_output=True, text=True,
        )
    if proc.returncode != 0:
        raise ManifestError(f"source {src.name}: {proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else 'git submodule failed'}")
    return gitutil.head(sub) or ""


def list_skill_dirs(m: Manifest, src: Source) -> list[str]:
    """Every directory under skills_root that holds a SKILL.md, as a path relative to
    skills_root. Skills may be nested in category folders; skills do not nest in skills."""
    root = m.root / src.path
    sr = src.skills_root.strip("/")
    base = root / sr if sr not in ("", ".") else root
    if not base.is_dir():
        return []
    skip = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build", ".sss"}
    out = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d not in skip)
        if "SKILL.md" in filenames and Path(dirpath) != base:
            out.append(os.path.relpath(dirpath, base))
            dirnames[:] = []
    return sorted(out)
