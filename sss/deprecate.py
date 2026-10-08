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

from . import links
from .inventory import SKIP_DIRS
from .manifest import Manifest, ManifestError, SOURCES_DIR, TOOL_DIR


def run(m: Manifest, name: str, keep_patches: bool = False) -> dict:
    removed: list[str] = []
    skill = None
    if m.has_skill(name):
        skill = m.skill(name)
        m.skills = [k for k in m.skills if k.name != name]
        if not keep_patches:
            for p in skill.patches:
                fp = m.root / p
                if fp.exists():
                    fp.unlink(); removed.append(p)
        m.save()
    removed += links.unlink_skill(m, name)
    if skill is None and not removed:
        raise ManifestError(f"{name} is not in the manifest and has no generated output")
    return {"skill": name, "removed": removed, "references": find_references(m.root, name, m)}


def find_references(root: Path, name: str, m: Manifest | None) -> list[dict]:
    pat = re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])")
    exclude = {os.path.realpath(root / e) for e in [SOURCES_DIR, TOOL_DIR, ".git"]}
    if m:
        exclude |= {os.path.realpath(root / d) for d in m.mirror_dirs}
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
