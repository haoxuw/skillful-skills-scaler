# Reorganize report schema

This document defines the report that the `reorganize` command produces.
The report is output (A) in the README. Output (B), the pull request, is
generated from the same findings, so the two always agree.

## High level summary

When many skills are collected from different places, some fall behind the
place they came from, some say the same thing twice, some disagree with each
other, some point at things that are not there, and some simply do not belong.
The reorganize command reads every skill, looks for those problems, and writes
them up in this report.

The report is written for a person who owns the skills but may not have
written them. It answers five questions, in this order:

1. Do any skills give conflicting information?
2. Are any skills out of date?
3. Are any skills duplicated?
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

A single run writes two files into `.sss/reports/` in the target repo:

| File | Audience | Purpose |
| --- | --- | --- |
| `.sss/reports/reorganize-report.md` | People | The readable report, structured as described below |
| `.sss/reports/reorganize-report.json` | Tools | The same findings in a fixed machine-readable shape |
| `.sss/reports/similarity.json` | Tools | Coverage summaries and pair scores, cached by content hash |

The report is a local working document. `.sss/reports/` is gitignored by
`sss init`, so reports are never committed. When a pull request is opened,
the markdown is pasted into the pull request description instead.

The markdown file is rendered from the JSON file by `sss report`, which fills
the template at `skills/reorganize-skills/templates/reorganize-report.md`.
The template is a resource of the reorganize skill, so the agent and the
renderer share one definition of the report's shape. To change wording or
order of sections, edit the template; to change what a block contains, edit
the renderer. If markdown and JSON ever disagree, the JSON file is
authoritative.

## The coverage matrix

SSS does not decide similarity from text. For every pair of skills the agent
reads the two coverage summaries, and the files for anything close, and scores
how much they cover the same ground:

| Stars | Meaning |
| --- | --- |
| 0 | Same. Interchangeable; one could replace the other with no loss. |
| 1 | Subset. One covers everything the other does, and more. |
| 2 | Large overlap. Mostly the same ground from different angles. |
| 3 | Some overlap. Share a few topics, each has its own core. |
| 4 | Related. Same area, different jobs. |
| 5 | Distinct. Nothing meaningful in common. |

Pairs at 0 or 1 star become duplicate findings. Pairs at 2 stars or lower are
checked for conflicts. The scores and the one-line coverage summary per skill
live in `.sss/reports/similarity.json`, keyed by the content hash of each
skill, so a rerun only scores pairs where a skill changed. The full table is
printed at the end of the report. The number of pairs grows with the square
of the number of skills; the agent is told to fan out across workers, one
per skill for summaries and one per row or batch for scores.

## Second opinion

Before the report is rendered, a separate worker with no other context
re-reads every finding against its quoted evidence as a sceptic, and may
downgrade confidence or remove findings whose evidence does not hold. The
summary says that this pass ran and how many findings it changed.

## Finding types

| Type | Question it answers | Found by | Typical action |
| --- | --- | --- | --- |
| `out_of_date` | 1 | SSS status (`stale`, `conflict`, `pending`) for managed skills; the model for content that describes things that have since changed, with evidence | `update` |
| `duplicate` | 2 | the coverage matrix: pairs at 0 or 1 star, plus byte-identical bodies | `merge` or `remove` |
| `conflict` | 3 | the model, checking pairs at 2 stars or lower for disagreement | `patch`, or a decision |
| `missing_dependency` | 4 | the inventory: a skill names another skill that is not here but is available from a source | `import` |
| `broken_reference` | 4 | the inventory: a link to a file that does not exist | `fix_link` |
| `out_of_place` | 5 | the model: the skill is unrelated to this repo, or is in the wrong folder | `move` or `remove` |
| `low_value` | 5 | the model: the skill's `adds` is "Nothing" (it repeats general knowledge of a tool or product, or is vague, trivially short, or only links elsewhere), action `remove`; or its preference is buried in general text, action `patch` to cut the skill down to that preference |
| `invalid_frontmatter` | 5 | the inventory: the SKILL.md front matter is not valid YAML, so a runtime may skip the skill | `patch` |

## Markdown report structure

The markdown report has exactly these sections, in this order, followed by
two appendices. A section with nothing to say still appears, with the line
"Nothing found." This keeps reports comparable between runs. The shape is
defined once, in the template at
`skills/reorganize-skills/templates/reorganize-report.md`.

### 1. Summary

One short paragraph, then a table with one row per question in section
order and a yes or no answer with a count, followed by how many actions are
safe to take and how many need a decision.

### 2. Conflicts

One subsection per conflict. Each states the two skills, the disagreement as
a direct quote from each side, why it matters in plain language, the four
fixed options, our recommendation with a confidence word, and always
"Decision needed: yes".

The four options are always:

1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

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

### 5. Missing pieces

Missing dependencies and broken references. Each states the skill, what it
points at, where that thing can be found if we know, and the fix.

### 6. Unuseful or out of place

One subsection per finding. Each quotes the skill, says why it does not help
or does not belong here, and recommends moving or removing it. Removal
always needs a decision.

"Unuseful" has one definition. The model already knows how most tools and
products work. A skill is useful when it records what the model cannot know:
the team's preferred behaviour, a business workflow, a methodology, a house
rule, a chosen default. A skill is unuseful when nothing of that kind remains
after every sentence a capable model would follow unprompted is removed; its
finding is `low_value` with a `remove` action. A skill that mixes both is also
filed as `low_value`, with a `patch` action to cut the general part and the
confidence word `likely`. Skills whose front matter does not parse appear in
this section too, as `invalid_frontmatter`, because a runtime may skip them.

The renderer checks the two against each other: a skill whose `adds` is
"Nothing" without a `low_value` finding, or a `low_value` finding with a
`remove` action on a skill whose `adds` names a preference, produces a
warning.

### 7. What we looked at

The inventory. One row per skill: name, source, status, location, number of
files, word count, date of last change. "Source" names the origin the skill
was imported from, or "local" if it was written in this repo. "Status" is the
SSS status for managed skills and "unmanaged" otherwise.

### 8. Proposed changes

The list of actions the pull request will perform, one line each, starting
with a verb: Move, Merge, Remove, Patch, Rename, Fix link, Update, Import.
Each line ends with the finding IDs that call for it. Actions that need a
decision are listed under a separate heading "Waiting on your decision" and
are not in the pull request.

### 9. How to respond

How to record decisions, by finding ID, in a pull request comment or in
`.sss/decisions.yaml`.

### Appendix: every skill we found

One entry per skill discovered, in inventory order. Each entry has:

- **Source, status, location.**
- **Goal.** What the skill is for, in one plain line. The agent writes this
  as `goal` on the inventory entry; if it is missing, the skill's own
  description is used, cut to one line.
- **Adds beyond the model.** What the skill makes the agent do that a capable
  model would not do unprompted: the preference, workflow, methodology or
  rule it carries. The agent writes this as `adds` on the inventory entry.
  "Nothing" here is what makes a `low_value` finding.
- **Concerns.** Every finding in sections 2 to 6 that involves this skill,
  one per line, with the type, the other skills involved, the finding ID,
  the recommendation, and whether a decision is needed. A skill with no
  findings says "none".

This is the part of the report to read when the question is "what do we
have, and is this particular skill fine?"

### Appendix: coverage matrix

The full star table, one row and one column per skill, followed by each
skill's coverage summary and a list of every pair at 2 stars or fewer with
its reason. Pairs at 3 stars or more appear only here.

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
      "goal": "Set up and troubleshoot logging, monitoring and Managed Prometheus on GKE.",
      "adds": "The team's golden-path monitoring component list and the rule to always name the cost of enabling it.",
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
  ]
}
```

Field rules:

- `findings[].type` is one of the eight types in the table above.
- `findings[].id` is stable across runs. It is a short hash of the type plus
  the sorted skill IDs involved, with a type prefix such as `dup-`, `conf-`,
  `old-`, `dep-`, `ref-`, `place-`, `low-`, `fm-`. A finding keeps its ID until the
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
  and `detail` are optional. When `from` is omitted, a `patch`, `update`,
  `fix_link` or `import` applies to all of the finding's `skills`. A `remove`,
  `move`, `rename` or `merge` on a finding with two or more skills must name
  `from`; otherwise the renderer marks the target unresolved, forces a
  decision, and does not group it with any other action. The renderer writes
  the resolved `from` back into the JSON.
- Every finding has at least one `evidence` entry. A finding without
  evidence is a bug in the tool, not a finding.
- `summary` is computed by the renderer and overwritten on every render.
- `generated_at` and `repo` are written into the JSON by the first render and
  kept, so rendering the same JSON twice gives the same markdown.
- `inventory[].goal` is optional and written by the agent. Keep it to one
  sentence a newcomer would understand.
- `inventory[].adds` is written by the agent: one sentence naming what the
  skill adds beyond what the model does unprompted, or the word "Nothing".
  The renderer warns when it is missing.
- When two skills share a name, their `id` is `name (path)` so findings can
  tell them apart.

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
