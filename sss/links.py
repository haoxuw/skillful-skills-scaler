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
"""Make skills visible to every agent runtime.

Claude Code reads .claude/skills, Codex and Gemini read .agents/skills. All three
follow symlinks. SSS writes generated skills to skills_dir and links each one into
every mirror_dir. SSS's own command skills are linked the same way."""
from __future__ import annotations

import os
import shutil
from pathlib import Path

from .manifest import Manifest

HERE = Path(__file__).resolve().parent.parent
OWN_SKILLS = HERE / "skills"


def _link(target: Path, link: Path, copy: bool) -> str:
    link.parent.mkdir(parents=True, exist_ok=True)
    if link.is_symlink() or link.exists():
        if link.is_symlink():
            if not copy and os.path.realpath(link) == os.path.realpath(target):
                return "unchanged"
            link.unlink()          # wrong target, or copy mode wants a real copy
        elif link.is_dir():
            if copy:
                shutil.rmtree(link)  # refresh the copy
            else:
                return f"skipped: {link} is a real directory"
        else:
            link.unlink()
    if copy:
        shutil.copytree(target, link)
        return "copied"
    rel = os.path.relpath(target, link.parent)
    link.symlink_to(rel, target_is_directory=True)
    return "linked"


def sync_links(m: Manifest, copy: bool | None = None) -> list[dict]:
    """Ensure every generated skill and every SSS command skill is reachable from
    skills_dir and all mirror_dirs. Symlinks by default; real copies when the
    manifest says link_mode: copy."""
    if copy is None:
        copy = m.link_mode == "copy"
    results = []
    out = m.root / m.skills_dir
    out.mkdir(parents=True, exist_ok=True)
    # SSS's own command skills go into skills_dir as links.
    own = []
    if OWN_SKILLS.is_dir():
        for d in sorted(OWN_SKILLS.iterdir()):
            if (d / "SKILL.md").is_file():
                own.append(d.name)
                results.append({"skill": d.name, "into": m.skills_dir, "result": _link(d, out / d.name, copy)})
    names = own + [k.name for k in m.skills if (out / k.name / "SKILL.md").is_file()]
    for mirror in m.mirror_dirs:
        if mirror.rstrip("/") == m.skills_dir.rstrip("/"):
            continue
        for name in names:
            results.append({"skill": name, "into": mirror, "result": _link(out / name, m.root / mirror / name, copy)})
    return results


def unlink_skill(m: Manifest, name: str) -> list[str]:
    removed = []
    for d in [m.skills_dir, *m.mirror_dirs]:
        p = m.root / d / name
        if p.is_symlink():
            p.unlink(); removed.append(str(p.relative_to(m.root)))
        elif p.is_dir():
            shutil.rmtree(p); removed.append(str(p.relative_to(m.root)))
    return removed
