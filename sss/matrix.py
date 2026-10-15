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
"""The coverage matrix: for every pair of skills, how alike they are, judged by the
model, scored 0 to 5 stars. 0 means the same thing, 5 means distinct.

SSS does not judge similarity from text. It keeps the bookkeeping: which skills
still need a coverage summary, which pairs still need a score, and the table.
Scores are cached by content hash so a rerun only scores what changed. Keys are
content hashes, not names: a skill that is renamed, moved, or that gains a
same-named twin keeps its summary and every score it took part in.

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


SCHEMA = 3   # 1: name keys, 12-hex body hashes; 2: 12-hex body-hash keys; 3: full folder-content hashes


def empty() -> dict:
    return {"schema_version": SCHEMA, "skills": {}, "pairs": {}}


def _migrate_v1(data: dict, inv: dict | None) -> dict:
    """v1 keyed skills by id and pairs by 'idA|idB', with 12-hex body-only hashes.
    Map those to today's content hashes through the live inventory (each skill
    carries its legacy hash); records whose content is gone cannot be mapped and
    are dropped."""
    out = empty()
    if not inv:
        return out
    legacy_to_new = {s["legacy_sha"]: s["content_sha"] for s in inv["skills"] if s.get("legacy_sha")}
    for sid, rec in (data.get("skills") or {}).items():
        new = legacy_to_new.get(rec.get("body_sha"))
        if new and rec.get("summary"):
            out["skills"][new] = {"summary": rec["summary"], "last_id": sid}
    for k, rec in (data.get("pairs") or {}).items():
        shas = [legacy_to_new.get(x) for x in (rec.get("scored_with") or [])]
        if len(shas) == 2 and all(shas) and rec.get("stars") is not None:
            out["pairs"][key(*shas)] = {"stars": rec["stars"], "reason": rec.get("reason", ""), "last_ids": k.split("|", 1)}
    return out


def _migrate_v2(data: dict, inv: dict | None) -> dict:
    """v2 keyed by the 12-hex body hash. Map to today's folder-content hashes
    through the live inventory's legacy hashes; unmatched records are dropped."""
    out = empty()
    if not inv:
        return out
    legacy_to_new = {s["legacy_sha"]: s["content_sha"] for s in inv["skills"] if s.get("legacy_sha")}
    for h, rec in (data.get("skills") or {}).items():
        new = legacy_to_new.get(h)
        if new and rec.get("summary"):
            out["skills"][new] = {"summary": rec["summary"], "last_id": rec.get("last_id", "")}
    for k, rec in (data.get("pairs") or {}).items():
        shas = [legacy_to_new.get(x) for x in k.split("|", 1)]
        if len(shas) == 2 and all(shas) and rec.get("stars") is not None:
            out["pairs"][key(*shas)] = {"stars": rec["stars"], "reason": rec.get("reason", ""), "last_ids": rec.get("last_ids", [])}
    return out


def load(path: Path, inv: dict | None = None) -> dict:
    if not path.exists():
        return empty()
    data = json.loads(path.read_text(encoding="utf-8"))
    try:
        version = int(data.get("schema_version") or 1)
    except (TypeError, ValueError):
        version = 1
    if version < 2:
        data = _migrate_v1(data, inv)
    elif version < 3:
        data = _migrate_v2(data, inv)
    data.setdefault("schema_version", SCHEMA)
    data.setdefault("skills", {})
    data.setdefault("pairs", {})
    return data


def save(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _pair_key(skills: dict, a: str, b: str) -> str:
    return key(skills[a]["content_sha"], skills[b]["content_sha"])


def _by_hash(inv: dict) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for s in inv["skills"]:
        groups.setdefault(s["content_sha"], []).append(s["id"])
    return {h: sorted(ids) for h, ids in groups.items()}


def pending(inv: dict, data: dict) -> dict:
    """What the agent still has to do, given the current inventory. Work is per
    distinct content: byte-identical skills share one summary and one row, and
    `same_as` names the other ids that share it."""
    skills = {s["id"]: s for s in inv["skills"]}
    groups = _by_hash(inv)
    rep = {h: ids[0] for h, ids in groups.items()}            # one representative id per content
    need_summary = []
    for h, ids in groups.items():
        rec = data["skills"].get(h)
        if not rec or not rec.get("summary"):
            s = skills[ids[0]]
            need_summary.append({"id": ids[0], "same_as": ids[1:], "path": s["path"], "description": s["description"]})
    need_score = []
    for ha, hb in combinations(sorted(groups), 2):
        rec = data["pairs"].get(key(ha, hb))
        if not rec or rec.get("stars") is None:
            a, b = sorted((rep[ha], rep[hb]))
            need_score.append({"a": a, "b": b, "path_a": skills[a]["path"], "path_b": skills[b]["path"],
                               "same_as_a": [i for i in groups[skills[a]["content_sha"]] if i != a],
                               "same_as_b": [i for i in groups[skills[b]["content_sha"]] if i != b]})
    need_score.sort(key=lambda x: (x["a"], x["b"]))   # stable, id-ordered rows for fan-out
    total_pairs = len(skills) * (len(skills) - 1) // 2
    distinct = len(groups)
    distinct_pairs = distinct * (distinct - 1) // 2
    return {
        "skills_total": len(skills), "pairs_total": total_pairs,
        "distinct_contents": distinct, "distinct_pairs": distinct_pairs,
        "summaries_needed": need_summary, "scores_needed": need_score,
        "scores_cached": distinct_pairs - len(need_score),
    }


def apply(inv: dict, data: dict, update: dict) -> dict:
    """Merge agent output: {"summaries": {id: text}, "scores": [{"a","b","stars","reason"}]}."""
    skills = {s["id"]: s for s in inv["skills"]}
    errors = []
    for sid, text in (update.get("summaries") or {}).items():
        if sid not in skills:
            errors.append(f"unknown skill in summaries: {sid}"); continue
        data["skills"][skills[sid]["content_sha"]] = {"summary": " ".join(str(text).split()), "last_id": sid}
    for sc in update.get("scores") or []:
        a, b = sc.get("a"), sc.get("b")
        if a not in skills or b not in skills:
            errors.append(f"unknown skill in score: {a} / {b}"); continue
        a, b = sorted((a, b))   # keys and hash order are always sorted
        if skills[a]["content_sha"] == skills[b]["content_sha"]:
            errors.append(f"{a} vs {b}: byte-identical content is 0 stars automatically; do not score it"); continue
        try:
            stars = int(sc.get("stars"))
        except (TypeError, ValueError):
            errors.append(f"{a} vs {b}: stars must be an integer 0-5"); continue
        if not 0 <= stars <= 5:
            errors.append(f"{a} vs {b}: stars must be 0-5, got {stars}"); continue
        reason = " ".join(str(sc.get("reason", "")).split())
        if stars <= OVERLAP_MAX and not reason:
            errors.append(f"{a} vs {b}: a score of {stars} needs a reason"); continue
        data["pairs"][_pair_key(skills, a, b)] = {"stars": stars, "reason": reason, "last_ids": [a, b]}
    # No pruning here: content that is absent right now may be back after a rename
    # or a move. `prune` is a separate, explicit step.
    return {"errors": errors, **pending(inv, data)}


def prune(inv: dict, data: dict) -> dict:
    """Drop records for content that no longer exists anywhere in the repo."""
    live = {s["content_sha"] for s in inv["skills"]}
    before = (len(data["skills"]), len(data["pairs"]))
    data["skills"] = {k: v for k, v in data["skills"].items() if k in live}
    data["pairs"] = {k: v for k, v in data["pairs"].items() if all(p in live for p in k.split("|", 1))}
    return {"summaries_dropped": before[0] - len(data["skills"]), "pairs_dropped": before[1] - len(data["pairs"])}


def scored_pairs(inv: dict, data: dict) -> dict[str, dict]:
    """{'idA|idB': record} for every live pair with a score, identical content at 0.
    Build once and pass around; it walks every pair."""
    skills = {s["id"]: s for s in inv["skills"]}
    out: dict[str, dict] = {}
    for a, b in combinations(sorted(skills), 2):
        if skills[a]["content_sha"] == skills[b]["content_sha"]:
            out[key(a, b)] = {"stars": 0, "reason": "Identical content (every file the same; name and provenance ignored)."}
            continue
        rec = data["pairs"].get(_pair_key(skills, a, b))
        if rec and rec.get("stars") is not None:
            out[key(a, b)] = rec
    return out


def duplicates(inv: dict, data: dict, scored: dict | None = None) -> list[dict]:
    """Pairs at 0 or 1 star, for the report's duplicate section."""
    scored = scored if scored is not None else scored_pairs(inv, data)
    out = [{"skills": k.split("|", 1), "stars": r["stars"], "reason": r.get("reason", "")}
           for k, r in scored.items() if r["stars"] <= DUPLICATE_MAX]
    return sorted(out, key=lambda x: (x["stars"], x["skills"]))


def overlaps(inv: dict, data: dict, scored: dict | None = None) -> list[dict]:
    scored = scored if scored is not None else scored_pairs(inv, data)
    out = [{"skills": k.split("|", 1), "stars": 2, "reason": r.get("reason", "")}
           for k, r in scored.items() if r["stars"] == OVERLAP_MAX]
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
    skills = {s["id"]: s for s in inv["skills"]}
    scored = scored_pairs(inv, data)
    for a in ids:
        cells = []
        for b in ids:
            if a == b:
                cells.append("—")
            else:
                rec = scored.get(key(a, b))
                cells.append(str(rec["stars"]) if rec else "·")
        L.append(f"| **{short[a]}** {a} | " + " | ".join(cells) + " |")
    L += ["", "Coverage summaries:", ""]
    for sid in ids:
        rec = data["skills"].get(skills[sid]["content_sha"]) or {}
        L.append(f"- **{short[sid]} {sid}**: {rec.get('summary') or '(no summary yet)'}")
    low = duplicates(inv, data, scored) + overlaps(inv, data, scored)
    if low:
        L += ["", "Pairs at 2 stars or fewer:", ""]
        for x in low:
            L.append(f"- {x['stars']} star{'s' if x['stars'] != 1 else ''}: {x['skills'][0]} and {x['skills'][1]}. {x['reason']}")
    return "\n".join(L) + "\n"
