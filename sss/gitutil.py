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
"""Thin wrappers around git. Every call is explicit about its working directory."""
from __future__ import annotations

import subprocess
from pathlib import Path


class GitError(RuntimeError):
    pass


def run(args: list[str], cwd: Path, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=str(cwd), capture_output=True, text=True
    )
    if check and proc.returncode != 0:
        raise GitError(f"git {' '.join(args)} failed in {cwd}:\n{proc.stderr.strip()}")
    return proc.stdout


def repo_root(start: Path) -> Path:
    out = run(["rev-parse", "--show-toplevel"], cwd=start).strip()
    return Path(out)


def head(cwd: Path) -> str | None:
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=str(cwd), capture_output=True, text=True
    )
    return proc.stdout.strip() if proc.returncode == 0 else None


def last_commit_touching(root: Path, rel_paths: list[str]) -> str | None:
    """Most recent commit that touched any of rel_paths, or None if never committed."""
    if not rel_paths:
        return None
    out = run(["log", "-1", "--format=%H", "--", *rel_paths], cwd=root).strip()
    return out or None


def commits_touching_since(root: Path, since: str, rel_paths: list[str]) -> list[str]:
    if not rel_paths:
        return []
    out = run(["log", "--format=%H", f"{since}..HEAD", "--", *rel_paths], cwd=root)
    return [line for line in out.splitlines() if line]


def is_tracked(root: Path, rel_path: str) -> bool:
    out = run(["ls-files", "--error-unmatch", rel_path], cwd=root, check=False)
    return bool(out.strip())


def dirty_paths(root: Path, rel_paths: list[str]) -> list[str]:
    """Paths with uncommitted or untracked changes among rel_paths."""
    if not rel_paths:
        return []
    out = run(["status", "--porcelain", "--", *rel_paths], cwd=root)
    return [line[3:].strip() for line in out.splitlines() if line.strip()]


def path_changed_between(repo: Path, old: str, new: str, rel_path: str) -> bool:
    proc = subprocess.run(
        ["git", "diff", "--quiet", old, new, "--", rel_path],
        cwd=str(repo), capture_output=True, text=True,
    )
    return proc.returncode == 1


def export_tree(repo: Path, commit: str, rel_path: str, dest: Path) -> None:
    """Write the contents of rel_path at commit into dest using git archive."""
    dest.mkdir(parents=True, exist_ok=True)
    archive = subprocess.run(
        ["git", "archive", "--format=tar", commit, "--", rel_path],
        cwd=str(repo), capture_output=True,
    )
    if archive.returncode != 0:
        raise GitError(archive.stderr.decode(errors="replace"))
    strip = rel_path.count("/") + 1
    subprocess.run(
        ["tar", "-x", f"--strip-components={strip}", "-C", str(dest)],
        input=archive.stdout, check=True,
    )
