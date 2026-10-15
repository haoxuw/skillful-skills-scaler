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


SCHEMA = 3
# Key history: v1 keyed skills by id and pairs by "idA|idB", carrying 12-hex body hashes
# in body_sha / scored_with. v2 keyed by hash, but two shapes shipped under that
# number: 12-hex body hashes, then 64-hex folder-content hashes. v3 is 64-hex only.
# Migration therefore goes by key shape, never by the version number alone.


def empty() -> dict:
    return {"schema_version": SCHEMA, "skills": {}, "pairs": {}}


def _legacy_map(inv: dict) -> tuple[dict[str, list[str]], set[str]]:
    """12-hex body hash -> every live content hash with that body (two skills can
    share a body and differ in supporting files), plus the set of live hashes."""
    legacy: dict[str, list[str]] = {}
    live = set()
    for s in inv["skills"]:
        live.add(s["content_sha"])
        if s.get("legacy_sha"):
            legacy.setdefault(s["legacy_sha"], [])
            if s["content_sha"] not in legacy[s["legacy_sha"]]:
                legacy[s["legacy_sha"]].append(s["content_sha"])
    return legacy, live


def _targets(h: str, legacy: dict[str, list[str]], live: set[str]) -> list[str]:
    """Live content hashes an old key stands for. A 64-hex key maps to itself when
    still live; a 12-hex key fans out to every live skill with that body."""
    if len(h) == 64:
        return [h] if h in live else []
    return legacy.get(h, [])


def _migrate(data: dict, inv: dict | None) -> tuple[dict, dict]:
    """Re-key a v1 or v2 file to v3. Returns (new_data, {"summaries_dropped", "pairs_dropped"})."""
    out = empty()
    skills_in = data.get("skills") or {}
    pairs_in = data.get("pairs") or {}
    dropped = {"summaries_dropped": 0, "pairs_dropped": 0}
    if not inv:
        dropped["summaries_dropped"] = len(skills_in)
        dropped["pairs_dropped"] = len(pairs_in)
        return out, dropped
    legacy, live = _legacy_map(inv)
    from itertools import product
    for k, rec in skills_in.items():
        h = rec.get("body_sha") or k          # v1 records carry the hash in body_sha; v2 keys are the hash
        hit = False
        for new in _targets(h, legacy, live):
            if rec.get("summary"):
                out["skills"][new] = {"summary": rec["summary"], "last_id": rec.get("last_id", k if "|" not in k else "")}
                hit = True
        if not hit:
            dropped["summaries_dropped"] += 1
    for k, rec in pairs_in.items():
        shas = rec.get("scored_with") or k.split("|", 1)   # v1 pairs carry hashes in scored_with
        if len(shas) != 2 or rec.get("stars") is None:
            dropped["pairs_dropped"] += 1
            continue
        ta, tb = _targets(shas[0], legacy, live), _targets(shas[1], legacy, live)
        hit = False
        for a, b in product(ta, tb):
            if a != b:
                out["pairs"][key(a, b)] = {"stars": rec["stars"], "reason": rec.get("reason", ""),
                                           "last_ids": rec.get("last_ids") or (k.split("|", 1) if "|" in k else [])}
                hit = True
        if not hit:
            dropped["pairs_dropped"] += 1
    return out, dropped


def load(path: Path, inv: dict | None = None, persist: bool = True) -> dict:
    """Read the cache, migrating older files by key shape. A migrated file is
    written back (when persist is true and an inventory was available) so the
    upgrade happens once; the drop counts are stored under `migrated`."""
    if not path.exists():
        return empty()
    data = json.loads(path.read_text(encoding="utf-8"))
    try:
        version = int(data.get("schema_version") or 1)
    except (TypeError, ValueError):
        version = 1
    if version < SCHEMA:
        data, dropped = _migrate(data, inv)
        data["migrated"] = {"from_version": version, **dropped}
        if persist and inv:
            save(path, data)
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
