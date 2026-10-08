# Reorganize report schema

This document defines the report that the `reorganize` command produces.
The report is output (A) in the README. Output (B), the pull request, is
generated from the same findings, so the two always agree.

## For non-technical readers

When many skills are collected from different places, some fall behind the
place they came from, some say the same thing twice, some disagree with each
other, some point at things that are not there, and some simply do not belong.
The reorganize command reads every skill, looks for those problems, and writes
them up in this report.

The report is written for a person who owns the skills but may not have
written them. It answers five questions, in this order:

1. Are any skills out of date?
2. Are any skills duplicated?
3. Do any skills give conflicting information?
4. Are any skills missing pieces they refer to?
5. Are any skills unuseful or out of place?

Then it says what we suggest doing about each problem, and which suggestions
need a decision from you.

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

The markdown file is rendered from the JSON file by `sss report`. If they
ever disagree, the JSON file is authoritative.

## Finding types

| Type | Question it answers | Found by | Typical action |
| --- | --- | --- | --- |
| `out_of_date` | 1 | SSS status (`stale`, `conflict`, `pending`) for managed skills; the model for content that describes things that have since changed, with evidence | `update` |
| `duplicate` | 2 | the model, judging candidate pairs from the inventory | `merge` or `remove` |
| `conflict` | 3 | the model, judging candidate pairs | `patch`, or a decision |
| `missing_dependency` | 4 | the inventory: a skill names another skill that is not here but is available from a source | `import` |
| `broken_reference` | 4 | the inventory: a link to a file that does not exist | `fix_link` |
| `out_of_place` | 5 | the model: the skill is unrelated to this repo, or is in the wrong folder | `move` or `remove` |
| `low_value` | 5 | the model: the skill does not help an agent do anything, for example it is vague, trivially short, or only links elsewhere | `remove` or `patch` |

## Markdown report structure

The markdown report has exactly these sections, in this order. A section with
nothing to say still appears, with the line "Nothing found." This keeps
reports comparable between runs.

### 1. Summary

One short paragraph, then a table with one row per question and a yes or no
answer with a count, followed by how many actions are safe to take and how
many need a decision.

### 2. What we looked at

The inventory. One row per skill: name, source, status, location, number of
files, word count, date of last change. "Source" names the origin the skill
was imported from, or "local" if it was written in this repo. "Status" is the
SSS status for managed skills and "unmanaged" otherwise.

### 3. Out of date

One subsection per finding. Each states which skill, what it is behind or
what has changed, with a quote, and what updating would involve. A managed
skill that is `stale` is a confident finding with the status reason as
evidence. A claim that content is outdated needs a quote from the skill and a
sentence saying what is true now.

### 4. Duplicates

One subsection per group. Each states which skills are in the group, why we
think they overlap with a short quote from each, which one we recommend
keeping and why, and what happens to the others. The default preference is
the one that comes from a source of truth over a local copy, and the newer
over the older.

### 5. Conflicts

One subsection per conflict. Each states the two skills, the disagreement as
a direct quote from each side, why it matters in plain language, the four
fixed options, our recommendation with a confidence word, and always
"Decision needed: yes".

The four options are always:

1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

### 6. Missing pieces

Missing dependencies and broken references. Each states the skill, what it
points at, where that thing can be found if we know, and the fix.

### 7. Unuseful or out of place

One subsection per finding. Each quotes the skill, says why it does not help
or does not belong here, and recommends moving or removing it. Removal
always needs a decision.

### 8. Proposed changes

The list of actions the pull request will perform, one line each, starting
with a verb: Move, Merge, Remove, Patch, Rename, Fix link, Update, Import.
Each line ends with the finding ID. Actions that need a decision are listed
under a separate heading "Waiting on your decision" and are not in the pull
request.

### 9. What we left alone

Anything we noticed but chose not to act on, with a one-line reason, so the
reader knows the omission was deliberate. Candidate pairs judged to be fine
go here.

### 10. How to respond

How to record decisions, by finding ID, in a pull request comment or in
`.sss/decisions.yaml`.

## JSON report structure

```json
{
  "schema_version": 2,
  "generated_at": "2026-10-08T14:30:00Z",
  "repo": "github.com/owner/repo",
  "commit": "abc1234",
  "summary_text": "optional one-paragraph override for section 1",
  "inventory": [
    {
      "id": "gke-observability",
      "source": "google",
      "status": "ok",
      "path": ".agents/skills/gke-observability",
      "files": 1,
      "words": 1923,
      "last_changed": "2026-10-08"
    }
  ],
  "findings": [
    {
      "id": "conf-3f9a2c",
      "type": "conflict",
      "skills": ["gke-observability", "gke-observability-fork"],
      "why_it_matters": "An agent following one skill will pass a flag that gcloud rejects.",
      "evidence": [
        {"skill": "gke-observability", "file": "SKILL.md", "line": 72, "quote": "--enable-dataplane-v2-flow-observability"},
        {"skill": "gke-observability-fork", "file": "SKILL.md", "line": 98, "quote": "--enable-dataplane-v2-observability"}
      ],
      "options": ["Keep A, retire B.", "Keep B, retire A.", "Keep both, and write a local patch that reconciles them.", "Open an issue upstream, and patch locally meanwhile."],
      "recommendation": "Keep gke-observability. It is the current upstream; the fork copy predates the flag rename.",
      "confidence": "confident",
      "decision_needed": true,
      "proposed_action": {"verb": "remove", "from": ["gke-observability-fork"]}
    }
  ],
  "left_alone": [
    {"skill": "gcloud", "reason": "No overlap with the other skills here."}
  ]
}
```

Field rules:

- `findings[].type` is one of the seven types in the table above.
- `findings[].id` is stable across runs. It is a short hash of the type plus
  the sorted skill IDs involved, with a type prefix such as `dup-`, `conf-`,
  `old-`, `dep-`, `ref-`, `place-`, `low-`. A finding keeps its ID until the
  underlying skills change, so a decision recorded against it still applies
  next run.
- `findings[].confidence` is one of `confident`, `likely`, `unsure`. Words,
  not numbers, because the reader is a person.
- `findings[].decision_needed` is forced to `true` by the renderer for every
  `conflict`, for every finding with confidence `unsure`, and for every
  action whose verb is `remove`.
- `findings[].options` is filled with the four fixed options for `conflict`
  and is empty for other types.
- `findings[].proposed_action.verb` is one of `move`, `merge`, `remove`,
  `patch`, `rename`, `fix_link`, `update`, `import`, `none`. `from`, `into`
  and `detail` are optional.
- Every finding has at least one `evidence` entry. A finding without
  evidence is a bug in the tool, not a finding.
- `summary` is computed by the renderer and overwritten on every render.

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

The reader's answers are recorded in `.sss/decisions.yaml` in the target
repo so they survive between runs.

```yaml
dup-3f9a2c: accept
conf-81be44:
  choice: 3
  note: "Both are right in different regions, patch should branch on region."
```

A finding with a recorded decision is not asked about again unless its ID
changes.
