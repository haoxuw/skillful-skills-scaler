"""Staleness, decided from inputs only, using git history. Never by regenerating.

A generated skill is stale when any commit after the last commit that touched its
output folder also touched its inputs (replica path or patch files), or when any
input has uncommitted changes. In submodule mode the replica path is diffed inside
the submodule between the provenance commit and the current pointer."""
from __future__ import annotations

from pathlib import Path

from . import frontmatter, gitutil
from .manifest import Manifest, Skill


def provenance(m: Manifest, skill: Skill) -> dict:
    p = m.root / m.output_rel(skill) / "SKILL.md"
    if not p.is_file():
        return {}
    meta, _ = frontmatter.read(p)
    return ((meta.get("metadata") or {}).get("sss") or {}) if isinstance(meta.get("metadata"), dict) else {}


def check(m: Manifest, skill: Skill) -> dict:
    out_rel = m.output_rel(skill)
    out_dir = m.root / out_rel
    src = m.source(skill.source)
    src_rel = m.source_skill_rel(skill)
    reasons: list[str] = []

    if skill.status == "conflict":
        return _result(skill, "conflict", [f"conflict recorded: {(skill.conflict or {}).get('reason', '')}"])
    if not (out_dir / "SKILL.md").is_file():
        return _result(skill, "pending", ["no generated output yet"])
    if not (m.root / src_rel / "SKILL.md").is_file():
        return _result(skill, "conflict", [f"source skill missing: {src_rel}"])

    last_gen = gitutil.last_commit_touching(m.root, [out_rel])
    if last_gen is None:
        reasons.append("output not committed yet")
    inputs = list(skill.patches)
    if src.mode == "submodule":
        prov = provenance(m, skill)
        pointer = gitutil.head(m.root / src.path)
        if prov.get("source_commit") and pointer and prov["source_commit"] != pointer:
            if gitutil.path_changed_between(m.root / src.path, prov["source_commit"], pointer, _inside_sub(src, skill)):
                reasons.append(f"source changed in submodule {prov['source_commit'][:7]}..{pointer[:7]}")
    else:
        inputs.append(src_rel)

    if last_gen is not None:
        for c in gitutil.commits_touching_since(m.root, last_gen, inputs):
            reasons.append(f"input changed in commit {c[:7]}")
    for d in gitutil.dirty_paths(m.root, inputs):
        reasons.append(f"uncommitted change in {d}")
    hand = gitutil.dirty_paths(m.root, [out_rel]) if last_gen is not None else []

    state = "stale" if any(r.startswith(("input changed", "uncommitted", "source changed")) for r in reasons) else "ok"
    res = _result(skill, state, reasons)
    if hand:
        res["warnings"] = [f"generated output has uncommitted edits: {p}" for p in hand]
    return res


def _inside_sub(src, skill: Skill) -> str:
    root = src.skills_root.strip("/")
    return f"{root}/{skill.skill_dir}" if root and root != "." else skill.skill_dir


def _result(skill: Skill, state: str, reasons: list[str]) -> dict:
    return {"skill": skill.name, "from": skill.from_ref, "status": state,
            "patched": bool(skill.patches), "reasons": reasons}


def check_all(m: Manifest) -> list[dict]:
    return [check(m, k) for k in m.skills]
