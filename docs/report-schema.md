# Reorganize report schema

This document defines the report that the `reorganize` command produces.
The report is output (A) in the README. Output (B), the pull request, is
generated from the same findings, so the two always agree.

## For non-technical readers

When many skills are collected from different places, some of them end up
saying the same thing twice, and some end up disagreeing with each other.
The reorganize command reads every skill, finds those problems, and writes
them up in this report.

The report is written for a person who owns the skills but may not have
written them. It should answer four questions, in this order:

1. What did we look at?
2. What problems did we find?
3. What do we suggest doing about each one?
4. Which of those suggestions need a decision from you?

Every problem in the report comes with the evidence we used to find it, a
plain-language explanation of why it matters, and one recommended action.
Nothing in the report is changed automatically. The pull request that goes
with the report only applies the actions marked as safe, and leaves the rest
for you to decide.

## Files produced

A single run writes two files next to each other:

| File | Audience | Purpose |
| --- | --- | --- |
| `reorganize-report.md` | People | The readable report, structured as described below |
| `reorganize-report.json` | Tools | The same findings in a fixed machine-readable shape |

The markdown file is rendered from the JSON file. If they ever disagree, the
JSON file is authoritative.

## Markdown report structure

The markdown report has exactly these sections, in this order. A section with
nothing to say still appears, with the line "Nothing found." This keeps
reports comparable between runs.

### 1. Summary

One short paragraph and one table. The paragraph says what was scanned and
whether the result needs attention. The table gives counts only.

| Metric | Count |
| --- | --- |
| Skills found | |
| Sources | |
| Duplicate groups | |
| Conflicts | |
| Broken references | |
| Actions proposed | |
| Decisions needed from you | |

### 2. What we looked at

The inventory. One row per skill.

| Skill | Source | Location | Files | Words | Last changed |
| --- | --- | --- | --- | --- | --- |

"Source" names the origin the skill was imported from, or "local" if it was
written in this repo. "Location" is the path relative to the repo root.

### 3. Duplicates

Skills that cover the same ground. Each group is one subsection.

Each group states:

- Which skills are in the group.
- Why we think they overlap, in one or two sentences, with a short quote
  from each skill as evidence.
- Which one we recommend keeping, and why. The default preference is the
  one that comes from a source of truth over a local copy, and the newer one
  over the older one.
- What happens to the others: merged into the keeper, or removed.
- Whether this is safe to apply without a decision.

### 4. Conflicts

Skills that disagree with each other. Each conflict is one subsection.

Each conflict states:

- The two skills involved.
- The disagreement, as a direct quote from each side.
- Why it matters, in plain language, for example "an agent following
  skill A will create a regional cluster, an agent following skill B will
  create a zonal one."
- The options. There are always the same four:
  1. Keep A, retire B.
  2. Keep B, retire A.
  3. Keep both, and write a local patch that reconciles them.
  4. Change the source of truth upstream.
- Our recommendation and how confident we are, in words: "confident",
  "likely", or "unsure".
- Decision needed: always yes for conflicts.

### 5. Broken references

Skills that point at files, sections, or other skills that do not exist.
One row per reference.

| Skill | Reference | Problem | Suggested fix |
| --- | --- | --- | --- |

### 6. Proposed changes

The list of actions the pull request will perform, one line each. Each line
starts with a verb: Move, Merge, Remove, Patch, Rename, Fix link. Each line
names the finding it comes from so the reader can look it up above.

Actions marked "needs decision" are listed here too, but under a separate
heading "Waiting on your decision", and are not in the pull request.

### 7. What we left alone

Anything we noticed but chose not to act on, with a one-line reason. This
section exists so the reader knows the omission was deliberate.

### 8. How to respond

Instructions for recording decisions. The reader answers each "needs
decision" item by its finding ID, either in a reply on the pull request or
by editing the decisions file. The next run reads those decisions and
applies them.

## JSON report structure

```json
{
  "schema_version": 1,
  "generated_at": "2026-10-08T14:30:00Z",
  "repo": "github.com/owner/repo",
  "commit": "abc1234",
  "summary": {
    "skills_found": 0,
    "sources": 0,
    "duplicate_groups": 0,
    "conflicts": 0,
    "broken_references": 0,
    "actions_proposed": 0,
    "decisions_needed": 0
  },
  "inventory": [
    {
      "id": "gke-reliability",
      "source": "gke-mcp",
      "path": "skills/gke-reliability",
      "files": 1,
      "words": 820,
      "last_changed": "2026-05-28"
    }
  ],
  "findings": [
    {
      "id": "dup-3f9a2c",
      "type": "duplicate",
      "skills": ["gke-reliability", "cluster-ha-checks"],
      "why_it_matters": "Both tell the agent how to check cluster availability. An agent may load both and spend tokens twice.",
      "evidence": [
        {"skill": "gke-reliability", "file": "SKILL.md", "line": 14, "quote": "Check if the cluster is regional"},
        {"skill": "cluster-ha-checks", "file": "SKILL.md", "line": 3, "quote": "Verify the cluster spans multiple zones"}
      ],
      "options": [],
      "recommendation": "Keep gke-reliability because it comes from the source of truth and is newer.",
      "confidence": "likely",
      "decision_needed": false,
      "proposed_action": {
        "verb": "merge",
        "from": ["cluster-ha-checks"],
        "into": "gke-reliability"
      }
    }
  ],
  "left_alone": [
    {"skill": "meme-maker", "reason": "Unrelated to the other skills, no overlap found."}
  ]
}
```

Field rules:

- `findings[].type` is one of `duplicate`, `conflict`, `broken_reference`,
  `orphan`, `oversize`.
- `findings[].id` is stable across runs. It is a short hash of the type plus
  the sorted skill IDs involved. A finding keeps its ID until the underlying
  skills change, so a decision recorded against it still applies next run.
- `findings[].confidence` is one of `confident`, `likely`, `unsure`. Words,
  not numbers, because the reader is a person.
- `findings[].decision_needed` is always `true` for `conflict`. For other
  types it is `true` when confidence is `unsure`.
- `findings[].options` is required for `conflict` and contains the four
  fixed options listed above. It is empty for other types.
- `findings[].proposed_action.verb` is one of `move`, `merge`, `remove`,
  `patch`, `rename`, `fix_link`, `none`.
- Every finding has at least one `evidence` entry. A finding without
  evidence is a bug in the tool, not a finding.

## Writing rules for the markdown report

These apply to every sentence the tool writes into the report.

- Assume the reader knows what a skill is and nothing else. Define any
  other term the first time it appears.
- Short sentences. One idea each.
- Quote the skills rather than paraphrasing them when showing evidence.
- Say what will happen if nothing is done. "Agents will keep getting two
  different answers" is more useful than "there is a conflict".
- Never say "semantic", "deduplicate", "normalize", or "refactor". Say
  "means the same", "remove the copy", "tidy", "reorganize".
- Give one recommendation per finding. Listing options is fine, hedging
  between them is not.

## Decisions file

The reader's answers are recorded in `.skills/decisions.yaml` in the target
repo so they survive between runs.

```yaml
dup-3f9a2c: accept
conf-81be44:
  choice: 3
  note: "Both are right in different regions, patch should branch on region."
```

A finding with a recorded decision is not asked about again unless its ID
changes.
