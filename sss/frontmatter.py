"""Read and write YAML front matter on SKILL.md files without touching the body."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

_FM = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.S)


def split(text: str) -> tuple[dict, str]:
    m = _FM.match(text)
    if not m:
        return {}, text
    data = yaml.safe_load(m.group(1)) or {}
    if not isinstance(data, dict):
        data = {}
    return data, text[m.end():]


def join(meta: dict, body: str) -> str:
    dumped = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).rstrip("\n")
    body = body.lstrip("\n")
    return f"---\n{dumped}\n---\n\n{body}"


def read(path: Path) -> tuple[dict, str]:
    return split(path.read_text(encoding="utf-8"))


def write(path: Path, meta: dict, body: str) -> None:
    path.write_text(join(meta, body), encoding="utf-8")
