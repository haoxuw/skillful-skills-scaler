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
"""Render reorganize-report.md from reorganize-report.json, per docs/report-schema.md.

The report answers, in order: are any skills out of date, duplicated, conflicting,
missing pieces, or unuseful and out of place."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import re
from pathlib import Path

TYPES = ("out_of_date", "duplicate", "conflict", "missing_dependency", "broken_reference", "out_of_place", "low_value")
PREFIX = {"out_of_date": "old", "duplicate": "dup", "conflict": "conf", "missing_dependency": "dep",
          "broken_reference": "ref", "out_of_place": "place", "low_value": "low"}
VERBS = {"move": "Move", "merge": "Merge", "remove": "Remove", "patch": "Patch", "rename": "Rename",
         "fix_link": "Fix link", "update": "Update", "import": "Import", "none": "No change"}
CONFLICT_OPTIONS = [
    "Keep A, retire B.",
    "Keep B, retire A.",
    "Keep both, and write a local patch that reconciles them.",
    "Open an issue upstream, and patch locally meanwhile.",
]
QUESTIONS = [  # same order as the report sections
    ("conflict", "Do any skills give conflicting information?"),
    ("out_of_date", "Are any skills out of date?"),
    ("duplicate", "Are any skills duplicated?"),
    (("missing_dependency", "broken_reference"), "Are any skills missing pieces they refer to?"),
    (("out_of_place", "low_value"), "Are any skills unuseful or out of place?"),
]


def finding_id(kind: str, skills: list[str], subject: str = "") -> str:
    """Stable across runs: type + sorted skills + subject (the thing missing, the
    broken path, ...) so two findings about the same skill do not collide."""
    h = hashlib.sha256((kind + "|" + "|".join(sorted(skills)) + "|" + subject).encode()).hexdigest()[:6]
    return f"{PREFIX.get(kind, 'f')}-{h}"


def _subject(f: dict) -> str:
    if f.get("subject"):
        return str(f["subject"])
    a = f.get("proposed_action") or {}
    if f.get("type") in ("missing_dependency", "broken_reference"):
        frm = a.get("from")
        if frm:
            return ",".join(frm) if isinstance(frm, list) else str(frm)
        ev = f.get("evidence") or []
        return str(ev[0].get("quote", "")) if ev else ""
    return ""


def _action_key(f: dict) -> tuple:
    a = f["proposed_action"]
    frm = a.get("from")
    frm = tuple(frm) if isinstance(frm, list) else (str(frm),) if frm else ()
    return (a.get("verb", "none"), frm, a.get("into", ""))


def normalize(data: dict) -> dict:
    data.setdefault("schema_version", 2)
    findings = data.setdefault("findings", [])
    for f in findings:
        f.setdefault("skills", [])
        f.setdefault("evidence", [])
        f["id"] = f.get("id") or finding_id(f.get("type", "f"), f["skills"], _subject(f))
        f.setdefault("confidence", "unsure")
        f.setdefault("options", CONFLICT_OPTIONS if f.get("type") == "conflict" else [])
        action = f.setdefault("proposed_action", {"verb": "none"})
        needs = f.get("type") == "conflict" or f["confidence"] == "unsure" or action.get("verb") == "remove"
        f["decision_needed"] = bool(f.get("decision_needed", False) or needs)
        if not f["evidence"]:
            f.setdefault("_warnings", []).append("finding has no evidence")
    inv = data.setdefault("inventory", [])
    counts = {t: sum(1 for f in findings if f.get("type") == t) for t in TYPES}
    data["summary"] = {
        "skills_found": len(inv),
        "sources": len({s.get("source", "local") for s in inv}),
        **counts,
        "actions_proposed": len({_action_key(f) for f in findings if f["proposed_action"].get("verb", "none") != "none"}),
        "decisions_needed": len({_action_key(f) if f["proposed_action"].get("verb", "none") != "none" else ("none", (f["id"],), "")
                                 for f in findings if f["decision_needed"]}),
        "findings_total": len(findings),
    }
    return data


def _nothing(L: list[str]) -> None:
    L += ["Nothing found.", ""]


def _by(data: dict, types) -> list[dict]:
    types = (types,) if isinstance(types, str) else types
    return [f for f in data["findings"] if f.get("type") in types]


def warnings_for(data: dict) -> list[str]:
    out = []
    for i in data.get("inventory", []):
        if not i.get("goal"):
            out.append(f"{i.get('id')}: no goal written; using its description")
        elif i.get("goal", "").strip() == i.get("description", "").strip():
            out.append(f"{i.get('id')}: goal is the description copied verbatim")
    for f in data.get("findings", []):
        if not f.get("evidence"):
            out.append(f"{f.get('id')}: finding has no evidence")
    return out


TEMPLATE = Path(__file__).resolve().parent.parent / "skills" / "reorganize-skills" / "templates" / "reorganize-report.md"


def _block(lines: list[str]) -> str:
    text = "\n".join(lines).strip("\n")
    return text if text else "Nothing found."


def blocks(data: dict, matrix=None) -> dict:
    """Every placeholder the template can use, as finished markdown."""
    data = normalize(data)
    s = data["summary"]
    B: dict[str, str] = {}
    B["repo"] = str(data.get("repo") or "this repo")
    B["generated_at"] = str(data.get("generated_at") or _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    B["summary_text"] = data.get("summary_text") or (
        f"We looked at {s['skills_found']} skills from {s['sources']} sources. "
        + ("Nothing needs your attention." if s["decisions_needed"] == 0 else f"{s['decisions_needed']} items need a decision from you."))

    L = ["| Question | Answer |", "| --- | --- |"]
    for types, q in QUESTIONS:
        n = len(_by(data, types))
        L.append(f"| {q} | {'No' if n == 0 else f'Yes, {n}'} |")
    safe = len({_action_key(f) for f in data["findings"] if f["proposed_action"].get("verb", "none") != "none" and not f["decision_needed"]})
    L += [f"| Actions we can take without asking | {safe} |", f"| Decisions needed from you | {s['decisions_needed']} |"]
    B["question_table"] = _block(L)

    L = []
    if data["inventory"]:
        L += ["| Skill | Source | Status | Location | Files | Words | Last changed |", "| --- | --- | --- | --- | --- | --- | --- |"]
        for i in data["inventory"]:
            L.append(f"| {i.get('id','')} | {i.get('source','local')} | {i.get('status','')} | `{i.get('path','')}` | {i.get('files','')} | {i.get('words','')} | {i.get('last_changed') or ''} |")
    B["inventory_table"] = _block(L)

    for key_, types in (("out_of_date", "out_of_date"), ("duplicates", "duplicate"), ("conflicts", "conflict"),
                        ("missing_pieces", ("missing_dependency", "broken_reference")), ("out_of_place", ("out_of_place", "low_value"))):
        L = []
        for f in _by(data, types):
            L += _finding_block(f, show_options=(f.get("type") == "conflict"))
        B[key_] = _block(L)

    ready = [f for f in data["findings"] if f["proposed_action"].get("verb", "none") != "none" and not f["decision_needed"]]
    waiting = [f for f in data["findings"] if f["proposed_action"].get("verb", "none") != "none" and f["decision_needed"]]
    L = []
    if ready:
        L += ["These are safe and the pull request applies them:", ""] + [f"- {x}" for x in _grouped_actions(ready)] + [""]
    if waiting:
        L += ["### Waiting on your decision", "", "One line per action. Several findings can point at the same action; all their IDs are listed.", ""]
        L += [f"- {x}" for x in _grouped_actions(waiting)]
    B["proposed_changes"] = _block(L)

    L = []
    for i in data["inventory"]:
        L += _appendix_entry(i, data["findings"])
    B["appendix_skills"] = _block(L) if data["inventory"] else "No skills found."

    if matrix:
        from . import matrix as matrixmod
        inv, mdata = matrix
        B["appendix_matrix"] = matrixmod.render_table(inv, mdata).rstrip("\n")
    else:
        B["appendix_matrix"] = "No coverage matrix was produced for this run."
    return B


_PLACEHOLDER = re.compile(r"\{\{(\w+)\}\}")


def render(data: dict, matrix=None, template: str | None = None) -> str:
    """Fill the report template. The template is a resource of the reorganize
    skill, so the agent and the renderer share one definition of the shape."""
    tpl = template if template is not None else TEMPLATE.read_text(encoding="utf-8")
    B = blocks(data, matrix)
    missing = []

    def sub(m):
        k = m.group(1)
        if k in B:
            return B[k]
        missing.append(k)
        return m.group(0)
    out = _PLACEHOLDER.sub(sub, tpl)
    if missing:
        out += "\n\n<!-- unfilled placeholders: " + ", ".join(sorted(set(missing))) + " -->\n"
    return out.rstrip("\n") + "\n"


_SHORT = {"out_of_date": "out of date", "duplicate": "duplicate", "conflict": "conflicts", "missing_dependency": "missing dependency",
          "broken_reference": "broken link", "out_of_place": "out of place", "low_value": "low value"}


def _one_line(text: str, limit: int = 160) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def _appendix_entry(i: dict, findings: list[dict]) -> list[str]:
    sid = i.get("id", "")
    L = [f"### {sid}", ""]
    L.append(f"- **Source:** {i.get('source', 'local')}  **Status:** {i.get('status', '')}  **Location:** `{i.get('path', '')}`")
    goal = i.get("goal") or _one_line(i.get("description", "")) or "No description given."
    L.append(f"- **Goal:** {goal}")
    mine = [f for f in findings if sid in f.get("skills", [])]
    if not mine:
        L.append("- **Concerns:** none")
    else:
        L.append("- **Concerns:**")
        for f in mine:
            others = [s for s in f.get("skills", []) if s != sid]
            with_ = f" with {', '.join(others)}" if others else ""
            tail = f" Decision needed." if f.get("decision_needed") else ""
            L.append(f"  - {_SHORT.get(f.get('type'), f.get('type'))}{with_} [{f['id']}]: {_one_line(f.get('recommendation') or f.get('why_it_matters', ''), 140)}{tail}")
    L.append("")
    return L


def _finding_block(f: dict, show_options: bool) -> list[str]:
    L = [f"### {f['id']}: {', '.join(f['skills'])}", ""]
    if f.get("why_it_matters"):
        L += [f["why_it_matters"], ""]
    if f["evidence"]:
        L.append("Evidence:")
        for e in f["evidence"]:
            loc = f"{e.get('skill','')}/{e.get('file','SKILL.md')}" + (f":{e['line']}" if e.get("line") else "")
            L.append(f"- `{loc}`: \"{e.get('quote','')}\"")
        L.append("")
    if show_options and f.get("options"):
        L += ["Options:"] + [f"{i}. {o}" for i, o in enumerate(f["options"], 1)] + [""]
    if f.get("recommendation"):
        L += [f"**Recommendation** ({f['confidence']}): {f['recommendation']}", ""]
    L += [f"Decision needed: {'yes' if f['decision_needed'] else 'no'}", ""]
    return L


def _grouped_actions(findings: list[dict]) -> list[str]:
    groups: dict[tuple, list[dict]] = {}
    for f in findings:
        groups.setdefault(_action_key(f), []).append(f)
    lines = []
    for key, fs in groups.items():
        a = fs[0]["proposed_action"]
        parts = [VERBS.get(a.get("verb", "none"), a.get("verb"))]
        if a.get("from"):
            parts.append(", ".join(a["from"]) if isinstance(a["from"], list) else str(a["from"]))
        if a.get("into"):
            parts.append(f"into {a['into']}")
        details = sorted({x["proposed_action"].get("detail") for x in fs if x["proposed_action"].get("detail")})
        if details:
            parts.append("(" + "; ".join(details) + ")")
        ids = ", ".join(x["id"] for x in fs)
        lines.append(" ".join(parts) + f" [{ids}]")
    return lines


def render_file(json_path: Path, md_path: Path, matrix=None) -> list[str]:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    md_path.write_text(render(data, matrix=matrix), encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return warnings_for(data)
