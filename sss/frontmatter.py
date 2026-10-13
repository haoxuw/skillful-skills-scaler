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
    """Last-resort read for front matter that is still not YAML after repair. Flat
    `key: value` lines only; nested blocks are kept as raw text. Read-only: the
    result is never written back (see write())."""
    data: dict = {}
    key = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
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


def _repair(raw: str, err: yaml.YAMLError) -> str | None:
    """Quote the value on the line PyYAML complains about (almost always an
    unquoted colon in a long description) and let the real parser handle the
    rest, so nested maps, lists and types survive."""
    mark = getattr(err, "problem_mark", None)
    if mark is None:
        return None
    lines = raw.splitlines()
    i = mark.line
    if i >= len(lines) or ": " not in lines[i]:
        return None
    key, _, value = lines[i].partition(": ")
    value = value.strip()
    if value.startswith(("'", '"', "|", ">", "[", "{", "-")):
        return None
    lines[i] = f'{key}: "{value.replace(chr(92), chr(92) * 2).replace(chr(34), chr(92) + chr(34))}"'
    return "\n".join(lines)


def split(text: str) -> tuple[dict, str]:
    m = _FM.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError as e:
        data = None
        fixed = raw
        for _ in range(3):  # a description may hold more than one bad colon
            fixed = _repair(fixed, e)
            if fixed is None:
                break
            try:
                data = yaml.safe_load(fixed) or {}
                if isinstance(data, dict):
                    data["_frontmatter_error"] = f"repaired: {str(e).splitlines()[0]}"
                break
            except yaml.YAMLError as e2:
                e = e2
        if data is None:
            data = _lenient(raw)
            data["_frontmatter_error"] = str(e).splitlines()[0] if str(e) else "invalid YAML"
    if not isinstance(data, dict):
        data = {}
    return data, text[m.end():]


def is_valid(meta: dict) -> bool:
    return "_frontmatter_error" not in meta


def join(meta: dict, body: str) -> str:
    meta = {k: v for k, v in meta.items() if not str(k).startswith("_")}  # internal flags never reach disk
    dumped = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).rstrip("\n")
    body = body.lstrip("\n")
    return f"---\n{dumped}\n---\n\n{body}"


def read(path: Path) -> tuple[dict, str]:
    return split(path.read_text(encoding="utf-8"))


def write(path: Path, meta: dict, body: str) -> None:
    path.write_text(join(meta, body), encoding="utf-8")
