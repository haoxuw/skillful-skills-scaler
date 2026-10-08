"""The coverage matrix: for every pair of skills, how alike they are, judged by the
model, scored 0 to 5 stars. 0 means the same thing, 5 means distinct.

SSS does not judge similarity from text. It keeps the bookkeeping: which skills
still need a coverage summary, which pairs still need a score, and the table.
Scores are cached by content hash so a rerun only scores what changed.

File: .sss/reports/similarity.json (gitignored, local).
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

STARS = {
    0: "Same. Interchangeable; one could replace the other with no loss.",
    1: "Subset. One covers everything the other does, and more.",
    2: "Large overlap. Mostly the same ground from different angles.",
    3: "Some overlap. Share a few topics, each has its own core.",
    4: "Related. Same area, different jobs.",
    5: "Distinct. Nothing meaningful in common.",
}
DUPLICATE_MAX = 1   # 0 or 1 star is a duplicate finding
OVERLAP_MAX = 2     # 2 stars is worth a look for conflicts


def key(a: str, b: str) -> str:
    a, b = sorted((a, b))
    return f"{a}|{b}"


def empty() -> dict:
    return {"schema_version": 1, "skills": {}, "pairs": {}}


def load(path: Path) -> dict:
    if not path.exists():
        return empty()
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("skills", {})
    data.setdefault("pairs", {})
    return data


def save(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def pending(inv: dict, data: dict) -> dict:
    """What the agent still has to do, given the current inventory."""
    skills = {s["id"]: s for s in inv["skills"]}
    need_summary = []
    for sid, s in skills.items():
        rec = data["skills"].get(sid)
        if not rec or rec.get("body_sha") != s["body_sha"] or not rec.get("summary"):
            need_summary.append({"id": sid, "path": s["path"], "description": s["description"]})
    need_score = []
    for a, b in combinations(sorted(skills), 2):
        rec = data["pairs"].get(key(a, b))
        shas = [skills[a]["body_sha"], skills[b]["body_sha"]]
        if not rec or rec.get("scored_with") != shas or rec.get("stars") is None:
            need_score.append({"a": a, "b": b, "path_a": skills[a]["path"], "path_b": skills[b]["path"]})
    total_pairs = len(skills) * (len(skills) - 1) // 2
    return {
        "skills_total": len(skills), "pairs_total": total_pairs,
        "summaries_needed": need_summary, "scores_needed": need_score,
        "scores_cached": total_pairs - len(need_score),
    }


def apply(inv: dict, data: dict, update: dict) -> dict:
    """Merge agent output: {"summaries": {id: text}, "scores": [{"a","b","stars","reason"}]}."""
    skills = {s["id"]: s for s in inv["skills"]}
    errors = []
    for sid, text in (update.get("summaries") or {}).items():
        if sid not in skills:
            errors.append(f"unknown skill in summaries: {sid}"); continue
        data["skills"][sid] = {"body_sha": skills[sid]["body_sha"], "summary": " ".join(str(text).split())}
    for sc in update.get("scores") or []:
        a, b = sc.get("a"), sc.get("b")
        if a not in skills or b not in skills:
            errors.append(f"unknown skill in score: {a} / {b}"); continue
        try:
            stars = int(sc.get("stars"))
        except (TypeError, ValueError):
            errors.append(f"{a} vs {b}: stars must be an integer 0-5"); continue
        if not 0 <= stars <= 5:
            errors.append(f"{a} vs {b}: stars must be 0-5, got {stars}"); continue
        reason = " ".join(str(sc.get("reason", "")).split())
        if stars <= OVERLAP_MAX and not reason:
            errors.append(f"{a} vs {b}: a score of {stars} needs a reason"); continue
        data["pairs"][key(a, b)] = {"stars": stars, "reason": reason,
                                    "scored_with": [skills[a]["body_sha"], skills[b]["body_sha"]]}
    # drop records for skills that no longer exist
    data["skills"] = {k: v for k, v in data["skills"].items() if k in skills}
    data["pairs"] = {k: v for k, v in data["pairs"].items() if all(p in skills for p in k.split("|", 1))}
    return {"errors": errors, **pending(inv, data)}


def duplicates(inv: dict, data: dict) -> list[dict]:
    """Pairs at 0 or 1 star, for the report's duplicate section."""
    out = []
    for k, rec in data["pairs"].items():
        if rec.get("stars") is not None and rec["stars"] <= DUPLICATE_MAX:
            a, b = k.split("|", 1)
            out.append({"skills": [a, b], "stars": rec["stars"], "reason": rec.get("reason", "")})
    return sorted(out, key=lambda x: (x["stars"], x["skills"]))


def overlaps(inv: dict, data: dict) -> list[dict]:
    out = []
    for k, rec in data["pairs"].items():
        if rec.get("stars") == OVERLAP_MAX:
            a, b = k.split("|", 1)
            out.append({"skills": [a, b], "stars": 2, "reason": rec.get("reason", "")})
    return sorted(out, key=lambda x: x["skills"])


def render_table(inv: dict, data: dict) -> str:
    """The big table: one row and one column per skill, stars in the cells."""
    ids = sorted(s["id"] for s in inv["skills"])
    if not ids:
        return "No skills.\n"
    short = {sid: f"S{i+1}" for i, sid in enumerate(ids)}
    L = ["Legend: 0 = same, 1 = subset, 2 = large overlap, 3 = some overlap, 4 = related, 5 = distinct, · = not scored yet.", ""]
    L.append("| Skill | " + " | ".join(short[s] for s in ids) + " |")
    L.append("| --- | " + " | ".join("---" for _ in ids) + " |")
    for a in ids:
        cells = []
        for b in ids:
            if a == b:
                cells.append("—")
            else:
                rec = data["pairs"].get(key(a, b))
                cells.append(str(rec["stars"]) if rec and rec.get("stars") is not None else "·")
        L.append(f"| **{short[a]}** {a} | " + " | ".join(cells) + " |")
    L += ["", "Coverage summaries:", ""]
    for sid in ids:
        rec = data["skills"].get(sid) or {}
        L.append(f"- **{short[sid]} {sid}**: {rec.get('summary') or '(no summary yet)'}")
    low = [x for x in duplicates(inv, data)] + overlaps(inv, data)
    if low:
        L += ["", "Pairs at 2 stars or fewer:", ""]
        for x in low:
            L.append(f"- {x['stars']} star{'s' if x['stars'] != 1 else ''}: {x['skills'][0]} and {x['skills'][1]}. {x['reason']}")
    return "\n".join(L) + "\n"
