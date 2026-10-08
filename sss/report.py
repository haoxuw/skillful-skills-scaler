"""Render reorganize-report.md from reorganize-report.json, per docs/report-schema.md.

The report answers, in order: are any skills out of date, duplicated, conflicting,
missing pieces, or unuseful and out of place."""
from __future__ import annotations

import hashlib
import json
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
QUESTIONS = [
    ("out_of_date", "Are any skills out of date?"),
    ("duplicate", "Are any skills duplicated?"),
    ("conflict", "Do any skills give conflicting information?"),
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


def render(data: dict) -> str:
    data = normalize(data)
    s = data["summary"]
    L: list[str] = ["# Skills reorganize report", ""]

    # 1. Summary: answer each question in one line
    L += ["## 1. Summary", ""]
    L += [data.get("summary_text") or f"We looked at {s['skills_found']} skills from {s['sources']} sources. "
          + ("Nothing needs your attention." if s["decisions_needed"] == 0 else f"{s['decisions_needed']} items need a decision from you."), ""]
    L += ["| Question | Answer |", "| --- | --- |"]
    for types, q in QUESTIONS:
        n = len(_by(data, types))
        L.append(f"| {q} | {'No' if n == 0 else f'Yes, {n}'} |")
    safe = len({_action_key(f) for f in data["findings"] if f["proposed_action"].get("verb", "none") != "none" and not f["decision_needed"]})
    L += [f"| Actions we can take without asking | {safe} |",
          f"| Decisions needed from you | {s['decisions_needed']} |", ""]

    # 2. Inventory
    L += ["## 2. What we looked at", ""]
    if data["inventory"]:
        L += ["| Skill | Source | Status | Location | Files | Words | Last changed |", "| --- | --- | --- | --- | --- | --- | --- |"]
        for i in data["inventory"]:
            L.append(f"| {i.get('id','')} | {i.get('source','local')} | {i.get('status','')} | `{i.get('path','')}` | {i.get('files','')} | {i.get('words','')} | {i.get('last_changed') or ''} |")
        L.append("")
    else:
        _nothing(L)

    # 3..7: one section per question
    sections = [
        ("3. Out of date", "out_of_date", "These skills are behind their source, or describe things that have since changed."),
        ("4. Duplicates", "duplicate", "These skills cover the same ground. Keeping both wastes the agent's attention and lets them drift apart."),
        ("5. Conflicts", "conflict", "These skills disagree. An agent that loads both will get two answers."),
        ("6. Missing pieces", ("missing_dependency", "broken_reference"), "These skills point at files or other skills that are not here."),
        ("7. Unuseful or out of place", ("out_of_place", "low_value"), "These skills do not belong in this repo, or do not help an agent do anything."),
    ]
    for title, types, intro in sections:
        L += [f"## {title}", ""]
        items = _by(data, types)
        if not items:
            _nothing(L)
            continue
        L += [intro, ""]
        for f in items:
            L += _finding_block(f, show_options=(f.get("type") == "conflict"))

    # 8. Proposed changes
    L += ["## 8. Proposed changes", ""]
    ready = [f for f in data["findings"] if f["proposed_action"].get("verb", "none") != "none" and not f["decision_needed"]]
    waiting = [f for f in data["findings"] if f["proposed_action"].get("verb", "none") != "none" and f["decision_needed"]]
    if not ready and not waiting:
        _nothing(L)
    if ready:
        L += ["These are safe and the pull request applies them:", ""]
        L += [f"- {line}" for line in _grouped_actions(ready)] + [""]
    if waiting:
        L += ["### Waiting on your decision", ""]
        L += ["One line per action. Several findings can point at the same action; all their IDs are listed.", ""]
        L += [f"- {line}" for line in _grouped_actions(waiting)] + [""]

    # 9. Left alone
    L += ["## 9. What we left alone", ""]
    if data.get("left_alone"):
        L += [f"- **{x.get('skill','')}**: {x.get('reason','')}" for x in data["left_alone"]] + [""]
    else:
        _nothing(L)

    # 10. How to respond
    L += ["## 10. How to respond", ""]
    L += ["Each item marked \"needs decision\" has an ID like `conf-81be44`. Reply with the ID and your choice,",
          "either as a comment on the pull request or by adding a line to `.sss/decisions.yaml`:", "",
          "```yaml", "dup-3f9a2c: accept", "conf-81be44:", "  choice: 3", "  note: \"Both are right in different regions.\"", "```", "",
          "The next run reads those answers and applies them. Items you have answered are not asked again.", ""]
    return "\n".join(L)


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


def render_file(json_path: Path, md_path: Path) -> None:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    md_path.write_text(render(data), encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
