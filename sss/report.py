"""Render reorganize-report.md from reorganize-report.json, per docs/report-schema.md."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

VERBS = {"move": "Move", "merge": "Merge", "remove": "Remove", "patch": "Patch", "rename": "Rename", "fix_link": "Fix link", "none": "No change"}
CONFLICT_OPTIONS = [
    "Keep A, retire B.",
    "Keep B, retire A.",
    "Keep both, and write a local patch that reconciles them.",
    "Open an issue upstream, and patch locally meanwhile.",
]


def finding_id(kind: str, skills: list[str]) -> str:
    prefix = {"duplicate": "dup", "conflict": "conf", "broken_reference": "ref", "orphan": "orph", "oversize": "big"}.get(kind, "f")
    h = hashlib.sha256((kind + "|" + "|".join(sorted(skills))).encode()).hexdigest()[:6]
    return f"{prefix}-{h}"


def normalize(data: dict) -> dict:
    """Fill ids, enforce the schema's rules, and compute the summary."""
    data.setdefault("schema_version", 1)
    findings = data.setdefault("findings", [])
    for f in findings:
        f.setdefault("skills", [])
        f["id"] = f.get("id") or finding_id(f.get("type", "f"), f["skills"])
        f.setdefault("evidence", [])
        f.setdefault("confidence", "unsure")
        f.setdefault("options", CONFLICT_OPTIONS if f.get("type") == "conflict" else [])
        action = f.setdefault("proposed_action", {"verb": "none"})
        needs = f.get("type") == "conflict" or f["confidence"] == "unsure" or action.get("verb") == "remove"
        f["decision_needed"] = bool(f.get("decision_needed", False) or needs)
        if not f["evidence"]:
            f.setdefault("_warnings", []).append("finding has no evidence")
    inv = data.setdefault("inventory", [])
    data["summary"] = {
        "skills_found": len(inv),
        "sources": len({s.get("source", "local") for s in inv}),
        "duplicate_groups": sum(1 for f in findings if f.get("type") == "duplicate"),
        "conflicts": sum(1 for f in findings if f.get("type") == "conflict"),
        "broken_references": sum(1 for f in findings if f.get("type") == "broken_reference"),
        "actions_proposed": sum(1 for f in findings if f["proposed_action"].get("verb", "none") != "none"),
        "decisions_needed": sum(1 for f in findings if f["decision_needed"]),
    }
    return data


def _nothing(lines: list[str]) -> None:
    lines.append("Nothing found.")
    lines.append("")


def render(data: dict) -> str:
    data = normalize(data)
    s = data["summary"]
    L: list[str] = []
    L += ["# Skills reorganize report", ""]
    L += ["## 1. Summary", ""]
    L.append(data.get("summary_text") or f"We looked at {s['skills_found']} skills from {s['sources']} sources. "
             + ("Nothing needs your attention." if s["decisions_needed"] == 0 else f"{s['decisions_needed']} items need a decision from you."))
    L += ["", "| Metric | Count |", "| --- | --- |"]
    for label, key in [("Skills found", "skills_found"), ("Sources", "sources"), ("Duplicate groups", "duplicate_groups"),
                       ("Conflicts", "conflicts"), ("Broken references", "broken_references"),
                       ("Actions proposed", "actions_proposed"), ("Decisions needed from you", "decisions_needed")]:
        L.append(f"| {label} | {s[key]} |")
    L.append("")

    L += ["## 2. What we looked at", ""]
    if data["inventory"]:
        L += ["| Skill | Source | Location | Files | Words | Last changed |", "| --- | --- | --- | --- | --- | --- |"]
        for i in data["inventory"]:
            L.append(f"| {i.get('id','')} | {i.get('source','local')} | `{i.get('path','')}` | {i.get('files','')} | {i.get('words','')} | {i.get('last_changed','')} |")
        L.append("")
    else:
        _nothing(L)

    by = lambda t: [f for f in data["findings"] if f.get("type") == t]  # noqa: E731

    L += ["## 3. Duplicates", ""]
    dups = by("duplicate")
    if not dups:
        _nothing(L)
    for f in dups:
        L += _finding_block(f, show_options=False)

    L += ["## 4. Conflicts", ""]
    confs = by("conflict")
    if not confs:
        _nothing(L)
    for f in confs:
        L += _finding_block(f, show_options=True)

    L += ["## 5. Broken references", ""]
    refs = by("broken_reference")
    if refs:
        L += ["| Skill | Reference | Problem | Suggested fix |", "| --- | --- | --- | --- |"]
        for f in refs:
            ev = f["evidence"][0] if f["evidence"] else {}
            L.append(f"| {', '.join(f['skills'])} | `{ev.get('quote','')}` | {f.get('why_it_matters','')} | {f.get('recommendation','')} |")
        L.append("")
    else:
        _nothing(L)

    L += ["## 6. Proposed changes", ""]
    ready = [f for f in data["findings"] if f["proposed_action"].get("verb", "none") != "none" and not f["decision_needed"]]
    waiting = [f for f in data["findings"] if f["proposed_action"].get("verb", "none") != "none" and f["decision_needed"]]
    if not ready and not waiting:
        _nothing(L)
    for f in ready:
        L.append(f"- {_action_line(f)}")
    if ready:
        L.append("")
    if waiting:
        L += ["### Waiting on your decision", ""]
        for f in waiting:
            L.append(f"- {_action_line(f)}")
        L.append("")

    L += ["## 7. What we left alone", ""]
    if data.get("left_alone"):
        for x in data["left_alone"]:
            L.append(f"- **{x.get('skill','')}**: {x.get('reason','')}")
        L.append("")
    else:
        _nothing(L)

    L += ["## 8. How to respond", ""]
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
        L.append("Options:")
        for i, o in enumerate(f["options"], 1):
            L.append(f"{i}. {o}")
        L.append("")
    if f.get("recommendation"):
        L += [f"**Recommendation** ({f['confidence']}): {f['recommendation']}", ""]
    L += [f"Decision needed: {'yes' if f['decision_needed'] else 'no'}", ""]
    return L


def _action_line(f: dict) -> str:
    a = f["proposed_action"]
    verb = VERBS.get(a.get("verb", "none"), a.get("verb"))
    parts = [verb]
    if a.get("from"):
        parts.append(", ".join(a["from"]) if isinstance(a["from"], list) else str(a["from"]))
    if a.get("into"):
        parts.append(f"into {a['into']}")
    if a.get("detail"):
        parts.append(f"({a['detail']})")
    return " ".join(parts) + f" [{f['id']}]"


def render_file(json_path: Path, md_path: Path) -> None:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    md_path.write_text(render(data), encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
