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
"""Read and write YAML front matter on SKILL.md files without touching the body."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

_FM = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.S)


def _lenient(raw: str) -> dict:
    """Best-effort parse for front matter PyYAML rejects, most often an unquoted
    colon inside a long description. Top-level `key: value` lines only; indented
    continuation lines are folded into the previous value; nested blocks are
    kept as raw text under their key."""
    data: dict = {}
    key = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line[:1] not in (" ", "\t") and ":" in line:
            k, _, v = line.partition(":")
            key = k.strip()
            v = v.strip()
            if v.startswith(("|", ">")):
                v = ""
            data[key] = v.strip("'\"")
        elif key is not None:
            data[key] = (data[key] + " " + line.strip()).strip()
    return data


def split(text: str) -> tuple[dict, str]:
    m = _FM.match(text)
    if not m:
        return {}, text
    try:
        data = yaml.safe_load(m.group(1)) or {}
        if not isinstance(data, dict):
            data = {}
    except yaml.YAMLError as e:
        data = _lenient(m.group(1))
        data["_frontmatter_error"] = str(e).splitlines()[0] if str(e) else "invalid YAML"
    return data, text[m.end():]


def join(meta: dict, body: str) -> str:
    dumped = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).rstrip("\n")
    body = body.lstrip("\n")
    return f"---\n{dumped}\n---\n\n{body}"


def read(path: Path) -> tuple[dict, str]:
    return split(path.read_text(encoding="utf-8"))


def write(path: Path, meta: dict, body: str) -> None:
    path.write_text(join(meta, body), encoding="utf-8")
