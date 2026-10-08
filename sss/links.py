"""Make skills visible to every agent runtime.

Claude Code reads .claude/skills, Codex and Gemini read .agents/skills. All three
follow symlinks. SSS writes generated skills to output_dir and links each one into
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
            if os.path.realpath(link) == os.path.realpath(target):
                return "unchanged"
            link.unlink()
        elif link.is_dir():
            if copy:
                shutil.rmtree(link)
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


def sync_links(m: Manifest, copy: bool = False) -> list[dict]:
    """Ensure every generated skill and every SSS command skill is reachable from
    output_dir and all mirror_dirs."""
    results = []
    out = m.root / m.output_dir
    out.mkdir(parents=True, exist_ok=True)
    # SSS's own command skills go into output_dir as links.
    own = []
    if OWN_SKILLS.is_dir():
        for d in sorted(OWN_SKILLS.iterdir()):
            if (d / "SKILL.md").is_file():
                own.append(d.name)
                results.append({"skill": d.name, "into": m.output_dir, "result": _link(d, out / d.name, copy)})
    names = own + [k.name for k in m.skills if (out / k.name / "SKILL.md").is_file()]
    for mirror in m.mirror_dirs:
        if mirror.rstrip("/") == m.output_dir.rstrip("/"):
            continue
        for name in names:
            results.append({"skill": name, "into": mirror, "result": _link(out / name, m.root / mirror / name, copy)})
    return results


def unlink_skill(m: Manifest, name: str) -> list[str]:
    removed = []
    for d in [m.output_dir, *m.mirror_dirs]:
        p = m.root / d / name
        if p.is_symlink():
            p.unlink(); removed.append(str(p.relative_to(m.root)))
        elif p.is_dir():
            shutil.rmtree(p); removed.append(str(p.relative_to(m.root)))
    return removed
