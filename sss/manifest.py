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
"""The manifest: .sss/manifest.yaml in the target repo.

People own: skills_dir, mirror_dirs, each source's name/url/ref/mode/path/skills_root,
each skill's name/from/patches.  SSS owns: synced_commit, synced_at, generated_at,
status, conflict.
"""
from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from pathlib import Path

import yaml

SSS_DIR = ".sss"
MANIFEST = f"{SSS_DIR}/manifest.yaml"
PATCHES_DIR = f"{SSS_DIR}/patches"
SOURCES_DIR = f"{SSS_DIR}/sources"
LOCAL_DIR = f"{SSS_DIR}/local"
TOOL_DIR = f"{SSS_DIR}/tool"
DECISIONS = f"{SSS_DIR}/decisions.yaml"
REPORTS_DIR = f"{SSS_DIR}/reports"

STATUSES = ("pending", "ok", "stale", "conflict", "failed")


class ManifestError(RuntimeError):
    pass


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat()


@dataclass
class Source:
    name: str
    url: str | None = None
    ref: str = "main"
    mode: str = "copy"           # copy | submodule | local
    path: str = ""
    skills_root: str = "skills"
    synced_commit: str | None = None
    synced_at: str | None = None

    def __post_init__(self) -> None:
        if not self.path:
            self.path = LOCAL_DIR if self.mode == "local" else f"{SOURCES_DIR}/{self.name}"
        if self.mode not in ("copy", "submodule", "local"):
            raise ManifestError(f"source {self.name}: mode must be copy, submodule or local")

    def skill_rel(self, skill_dir: str) -> str:
        root = self.skills_root.strip("/")
        return f"{self.path}/{root}/{skill_dir}" if root and root != "." else f"{self.path}/{skill_dir}"

    def to_dict(self) -> dict:
        d = {"name": self.name}
        if self.mode != "local":
            d["url"] = self.url
            d["ref"] = self.ref
        d["mode"] = self.mode
        d["path"] = self.path
        d["skills_root"] = self.skills_root
        if self.synced_commit:
            d["synced_commit"] = self.synced_commit
        if self.synced_at:
            d["synced_at"] = self.synced_at
        return d


@dataclass
class Skill:
    name: str
    source: str                   # source name
    skill_dir: str                # directory name under the source's skills_root
    patches: list[str] = field(default_factory=list)
    status: str = "pending"
    generated_at: str | None = None
    conflict: dict | None = None

    @property
    def from_ref(self) -> str:
        return f"{self.source}/{self.skill_dir}"

    def to_dict(self) -> dict:
        d: dict = {"name": self.name, "from": self.from_ref, "patches": list(self.patches), "status": self.status}
        if self.generated_at:
            d["generated_at"] = self.generated_at
        if self.conflict:
            d["conflict"] = self.conflict
        return d


@dataclass
class Manifest:
    root: Path
    skills_dir: str = ".agents/skills"   # where generated skills land; often shared with hand-written ones
    mirror_dirs: list[str] = field(default_factory=lambda: [".claude/skills"])
    link_mode: str = "symlink"    # symlink | copy  (copy for file systems without symlinks)
    sources: list[Source] = field(default_factory=list)
    skills: list[Skill] = field(default_factory=list)
    schema_version: int = 1

    # ---- persistence -------------------------------------------------
    @property
    def path(self) -> Path:
        return self.root / MANIFEST

    @classmethod
    def load(cls, root: Path) -> "Manifest":
        p = root / MANIFEST
        if not p.exists():
            raise ManifestError(f"no manifest at {p}. Run: sss init")
        raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        m = cls(root=root)
        m.schema_version = int(raw.get("schema_version", 1))
        m.skills_dir = raw.get("skills_dir", raw.get("output_dir", m.skills_dir))  # output_dir: old name
        m.mirror_dirs = list(raw.get("mirror_dirs", m.mirror_dirs) or [])
        m.link_mode = raw.get("link_mode", "symlink")
        for s in raw.get("sources", []) or []:
            m.sources.append(Source(
                name=s["name"], url=s.get("url"), ref=s.get("ref", "main"),
                mode=s.get("mode", "copy"), path=s.get("path", ""),
                skills_root=s.get("skills_root", "skills"),
                synced_commit=s.get("synced_commit"), synced_at=s.get("synced_at"),
            ))
        for k in raw.get("skills", []) or []:
            src, _, sdir = str(k["from"]).partition("/")
            m.skills.append(Skill(
                name=k["name"], source=src, skill_dir=sdir or k["name"],
                patches=list(k.get("patches", []) or []),
                status=k.get("status", "pending"),
                generated_at=k.get("generated_at"), conflict=k.get("conflict"),
            ))
        return m

    def save(self) -> None:
        data = {
            "schema_version": self.schema_version,
            "skills_dir": self.skills_dir,
            "mirror_dirs": list(self.mirror_dirs),
            "link_mode": self.link_mode,
            "sources": [s.to_dict() for s in self.sources],
            "skills": [k.to_dict() for k in self.skills],
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        header = "# Managed by SSS. People edit skills_dir, mirror_dirs, link_mode, sources (not synced_*),\n# and skills name/from/patches. SSS writes the rest.\n"
        self.path.write_text(header + yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")

    # ---- lookups -----------------------------------------------------
    def source(self, name: str) -> Source:
        for s in self.sources:
            if s.name == name:
                return s
        raise ManifestError(f"unknown source: {name}")

    def skill(self, name: str) -> Skill:
        for k in self.skills:
            if k.name == name:
                return k
        raise ManifestError(f"unknown skill: {name}")

    def has_skill(self, name: str) -> bool:
        return any(k.name == name for k in self.skills)

    def output_rel(self, skill: Skill) -> str:
        return f"{self.skills_dir.rstrip('/')}/{skill.name}"

    def source_skill_rel(self, skill: Skill) -> str:
        return self.source(skill.source).skill_rel(skill.skill_dir)
