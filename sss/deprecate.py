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
"""Deprecate: remove a skill from the manifest, its patches, its generated output and
links, then report every remaining reference so the agent can deal with them."""
from __future__ import annotations

import os
import re
from pathlib import Path

from . import frontmatter, links
from .inventory import SKIP_DIRS
from .manifest import Manifest, ManifestError, SOURCES_DIR, TOOL_DIR


def _generated_by_sss(path: Path) -> bool:
    md = path / "SKILL.md"
    if not md.is_file():
        return False
    meta, _ = frontmatter.read(md)
    return bool(frontmatter.provenance(meta))


def run(m: Manifest, name: str, keep_patches: bool = False) -> dict:
    """Remove a skill SSS manages. Output SSS generated earlier but whose manifest
    entry is already gone is also removed (its SKILL.md carries SSS provenance).
    A skill with no provenance is the repo's own; SSS never deletes those."""
    if not m.has_skill(name):
        dirs = [m.skills_dir, *m.real_mirror_dirs()]
        places = [d for d in dirs if os.path.lexists(m.root / d / name)]
        dangling = [d for d in places if (m.root / d / name).is_symlink() and not (m.root / d / name).exists()]
        generated = [d for d in places if (m.root / d / name).exists() and _generated_by_sss(m.root / d / name)]
        if places and (generated or len(dangling) == len(places)):
            # Orphaned SSS output (manifest entry removed by hand) or links left behind.
            removed = links.unlink_skill(m, name)
            return {"skill": name, "removed": removed, "note": "orphaned SSS output removed; it had no manifest entry",
                    "references": find_references(m.root, name, m)}
        hint = (f" It exists at {', '.join(f'{d}/{name}' for d in places)} without SSS provenance; remove it by hand if that is wanted."
                if places else "")
        raise ManifestError(f"{name} is not managed by SSS (not in the manifest).{hint}")
    skill = m.skill(name)
    removed: list[str] = []
    m.skills = [k for k in m.skills if k.name != name]
    if not keep_patches:
        for p in skill.patches:
            fp = m.root / p
            if fp.exists():
                fp.unlink(); removed.append(p)
    m.save()
    removed += links.unlink_skill(m, name)
    return {"skill": name, "removed": removed, "references": find_references(m.root, name, m)}


def find_references(root: Path, name: str, m: Manifest | None) -> list[dict]:
    pat = re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])")
    exclude = {os.path.realpath(root / e) for e in [SOURCES_DIR, TOOL_DIR, ".git"]}
    if m:
        exclude |= {os.path.realpath(root / d) for d in m.real_mirror_dirs()}
    hits = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and os.path.realpath(os.path.join(dirpath, d)) not in exclude]
        for fn in filenames:
            if not fn.lower().endswith((".md", ".yaml", ".yml", ".json", ".toml", ".txt")):
                continue
            p = Path(dirpath) / fn
            try:
                for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if pat.search(line):
                        hits.append({"file": os.path.relpath(p, root), "line": i, "text": line.strip()[:200]})
            except OSError:
                continue
    return hits
