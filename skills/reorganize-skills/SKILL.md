---
name: reorganize-skills
description: Find every skill in the repo, score how much each pair covers the same ground (0 to 5 stars), spot duplicates, conflicts, missing pieces and out-of-place skills, write a plain-language report, and open a PR that tidies the skills. Use when asked to reorganize, dedupe, audit, compare, or clean up skills, or when "reorganize-skills using sss" is mentioned.
license: Apache-2.0
metadata:
  sss: {command: reorganize}
---

# Reorganize skills

You are running SSS (Skillful-skills-scaler). The CLI does the bookkeeping. You
do the judgement, and you write findings in the fixed shape described in
`.sss/tool/docs/report-schema.md`. Read that file first. The report itself
follows the template next to this file, `templates/reorganize-report.md`;
`sss report` fills its placeholders from your JSON, so you never write the
markdown by hand. Read the template once so you know what each section asks.

Run the CLI as `python3 .sss/tool/sss.py` from the repo root. All report files
live in `.sss/reports/`, which is gitignored. Never commit them.

## Fan out

Most of this work is independent per skill or per pair. If your runtime can run
subagents or parallel tasks, fan out: one worker per skill for summaries and
own-skill judgements, one worker per row (or per batch of about 50 pairs) for
scoring, and one worker for the second-opinion pass. Each worker returns JSON
in the shape the step asks for; you merge and apply. If you cannot fan out, do
the same steps in sequence. The results must be identical either way.

## Steps

1. **Inventory.**
   ```bash
   python3 .sss/tool/sss.py inventory > .sss/reports/inventory.json
   ```
   Every skill (excluding replicas and mirrors) with its source, SSS status,
   size, last change date, references, `broken_references`,
   `missing_dependencies` (skills it names that are not here but are available
   from a source), and `identical` (groups whose bodies are byte for byte the
   same). SSS does not guess similarity from text. That is your job, next.

2. **Earlier decisions.** Read `.sss/decisions.yaml`. A finding whose ID has a
   recorded decision is settled: apply the decision, do not ask again.

3. **Coverage summaries.** Ask what is still needed:
   ```bash
   python3 .sss/tool/sss.py matrix pending
   ```
   For every entry in `summaries_needed`, read the whole skill folder and write
   a coverage summary: two or three sentences saying what the skill lets an
   agent do, which tasks it covers, and what it explicitly does not cover.
   Fan out one worker per skill. Summaries are cached by content hash, so a
   rerun only asks for new or changed skills.

4. **Score every pair, 0 to 5 stars.** `scores_needed` lists every pair that
   has no score yet. Score from the two summaries first. The scale is:

   | Stars | Meaning |
   | --- | --- |
   | 0 | Same. Interchangeable; one could replace the other with no loss. |
   | 1 | Subset. One covers everything the other does, and more. |
   | 2 | Large overlap. Mostly the same ground from different angles. |
   | 3 | Some overlap. Share a few topics, each has its own core. |
   | 4 | Related. Same area, different jobs. |
   | 5 | Distinct. Nothing meaningful in common. |

   For any pair you would score 2 or lower, open both SKILL.md files and
   confirm before you commit to the score. Every score of 2 or lower needs a
   one-sentence reason. Fan out by row or by batch. Then merge:
   ```bash
   python3 .sss/tool/sss.py matrix apply scores.json
   ```
   where `scores.json` is `{"summaries": {"<id>": "..."}, "scores": [{"a": "<id>", "b": "<id>", "stars": 0-5, "reason": "..."}]}`.
   Repeat `matrix pending` until `scores_still_needed` is 0. The number of
   pairs grows with the square of the skill count; the cache means each pair is
   paid for once.

5. **Turn the matrix into findings.**
   - Every pair at 0 or 1 star, and every `identical` group, is a `duplicate`.
     Recommend the keeper. Prefer a skill from a source of truth over a local
     one, and the newer over the older. Quote a line from each.
   - For every pair at 2 stars or lower, check for disagreement on a fact or an
     instruction. Each disagreement is a `conflict`: quote the exact lines from
     each side and say in one sentence what goes wrong if nothing is done. A
     pair can be both a duplicate and a conflict; file both.
   - Pairs at 3 stars or more are not findings. Do not list them anywhere; the
     matrix appendix already shows their score.

6. **Findings that need no judgement.**
   - every managed skill whose `status` is `stale`, `pending` or `conflict` is an
     `out_of_date` finding, with `status_reasons` as evidence;
   - every `missing_dependencies` entry is a `missing_dependency` finding with an
     `import` action;
   - every `broken_references` entry is a `broken_reference` finding with a
     `fix_link` action;
   - every skill with a `frontmatter_error` is an `invalid_frontmatter` finding
     (section 6, unuseful or out of place: a runtime may skip a skill whose
     front matter does not parse) with a `patch` action, quoting the error.

7. **Judge every skill on its own.** Fan out one worker per skill. Each writes
   the skill's one-line `goal` for the inventory, in words a newcomer would
   understand, and checks:
   - `out_of_date` by content: it describes a flag, API, version or product that
     has since changed. Quote the line and say what is true now. Only file this
     when you are sure.
   - `out_of_place`: it has nothing to do with what this repo does, or sits in
     the wrong folder. Quote its description and say why it does not fit.
   - `low_value`: it would not help an agent do anything: vague, trivially short,
     or only a list of links. Quote what little it says.

8. **Second opinion.** Before rendering, hand the complete findings JSON to one
   worker with no other context and this brief: "You are a sceptical reviewer.
   For each finding, open the quoted evidence and confirm it says what the
   finding claims. Downgrade confidence or delete findings whose evidence does
   not hold. Flag any duplicate or conflict you think is wrong, with a reason.
   Return the corrected JSON and a list of what you changed." Apply its
   corrections. Note in `summary_text` that a second pass was done and how many
   findings it changed.

9. **Write and render.** Save the findings to
   `.sss/reports/reorganize-report.json` with the inventory entries from step 1
   plus each skill's `goal`. Then:
   ```bash
   python3 .sss/tool/sss.py report
   ```
   This writes `.sss/reports/reorganize-report.md`: nine sections (summary,
   conflicts, out of date, duplicates, missing pieces, unuseful or out of
   place, what we looked at, proposed changes, how to respond), then an
   appendix with every skill, its goal and its concerns, then the full coverage
   matrix. The renderer fills IDs, forces `decision_needed` for conflicts, for
   `unsure` findings and for any `remove` action, and prints a warning for every
   skill without a goal. Fix warnings before you continue.

10. **Apply only the safe actions**, meaning findings with `decision_needed: false`:
    - A reconcile is a new patch: `python3 .sss/tool/sss.py patch new <skill> --intent "..."`,
      then follow the `update-skills` flow for that skill.
    - A missing dependency is an import: `python3 .sss/tool/sss.py import <source>/<path>`.
    - A broken link is fixed in the patch or local skill, never in generated output.
    Anything needing a decision is left alone and listed in the report.

11. **Open the PR** against this repo on a new branch, if there is at least one
    safe action or the user asked for one. The PR body is the full text of
    `.sss/reports/reorganize-report.md`. Title: "Reorganize skills: N findings,
    M need a decision". Do not commit the report files. If there is nothing safe
    to apply, skip the PR and hand the user the report path instead.

## Reporting back

Summarise for the user in plain language: how many skills, how many pairs
scored, how many at 2 stars or fewer, what you changed, and exactly which IDs
need their answer. A second-year CS student should be able to follow it. Give
them the path `.sss/reports/reorganize-report.md` and point at section 9 for
how to answer.

## Rules

- Never write "semantic", "deduplicate", "normalize", or "refactor" in the report.
  Say "means the same", "remove the copy", "tidy", "reorganize".
- Never remove a skill without a recorded decision.
- Never edit files under `.sss/sources/` or generated output by hand.
- Never score a pair from its names alone. Read the summaries, and the files
  for anything at 2 stars or lower.
