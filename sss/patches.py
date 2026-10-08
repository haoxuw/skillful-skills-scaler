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
"""Semantic patch files: .sss/patches/<name>.md with front matter and a prose body.

Front matter:
  target: <skill name>
  intent: <one line>
  checks:
    - A plain sentence (judged by the model after generation)
    - contains: "literal text"          # deterministic
    - not_contains: "literal text"      # deterministic
    - regex: "pattern"                  # deterministic, searched in SKILL.md
    - file_exists: "scripts/x.sh"       # deterministic, relative to the skill dir
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from . import frontmatter

DETERMINISTIC = ("contains", "not_contains", "regex", "file_exists")


@dataclass
class Patch:
    path: str
    target: str
    intent: str
    body: str
    checks: list = field(default_factory=list)

    @property
    def sentence_checks(self) -> list[str]:
        return [c for c in self.checks if isinstance(c, str)]

    @property
    def deterministic_checks(self) -> list[dict]:
        return [c for c in self.checks if isinstance(c, dict)]

    def to_dict(self) -> dict:
        return {
            "path": self.path, "target": self.target, "intent": self.intent,
            "body": self.body.strip(), "checks": self.checks,
        }


def load(root: Path, rel: str) -> Patch:
    p = root / rel
    if not p.exists():
        raise FileNotFoundError(f"patch not found: {rel}")
    meta, body = frontmatter.read(p)
    return Patch(
        path=rel, target=str(meta.get("target", "")), intent=str(meta.get("intent", "")),
        body=body, checks=list(meta.get("checks", []) or []),
    )


def template(target: str, intent: str) -> str:
    return frontmatter.join(
        {"target": target, "intent": intent, "checks": ["Describe what must be true in the final skill."]},
        "Describe the change in plain language. Say what to add, remove or reword,\n"
        "and tell the model to keep everything else exactly as the source has it.\n",
    )


def run_deterministic(skill_dir: Path, checks: list[dict]) -> list[str]:
    """Return a list of failure messages. Empty means all passed."""
    failures: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8") if skill_md.exists() else ""
    for c in checks:
        (kind, value), = c.items()
        if kind == "contains" and str(value) not in text:
            failures.append(f"contains: {value!r} not found in SKILL.md")
        elif kind == "not_contains" and str(value) in text:
            failures.append(f"not_contains: {value!r} is present in SKILL.md")
        elif kind == "regex" and not re.search(str(value), text, re.M):
            failures.append(f"regex: {value!r} did not match SKILL.md")
        elif kind == "file_exists" and not (skill_dir / str(value)).exists():
            failures.append(f"file_exists: {value!r} missing under {skill_dir.name}/")
        elif kind not in DETERMINISTIC:
            failures.append(f"unknown check type: {kind}")
    return failures
