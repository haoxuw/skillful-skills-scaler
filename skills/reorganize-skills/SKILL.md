---
name: reorganize-skills
description: Find every skill in the repo, spot duplicates, conflicts and broken references, write a plain-language report, and open a PR that tidies the skills. Use when asked to reorganize, dedupe, audit, or clean up skills, or when "reorganize-skills using sss" is mentioned.
license: Apache-2.0
metadata:
  sss: {command: reorganize}
---

# Reorganize skills

You are running SSS (Skillful-skills-scaler). The CLI does the inventory and the
cheap matching. You do the judgement, and you write the findings in the fixed
shape described in `.sss/tool/docs/report-schema.md`. Read that file first.

Run the CLI as `python3 .sss/tool/sss.py` from the repo root.

## Steps

1. **Inventory.**
   ```bash
   python3 .sss/tool/sss.py inventory > /tmp/sss-inventory.json
   ```
   This lists every skill (excluding replicas and mirrors) with its source, SSS
   status, size, last change date, references, `broken_references`,
   `missing_dependencies` (skills it names that are not here but are available
   from a source), and `candidates`: pairs that look alike by identical body or
   by overlapping names, descriptions or headings. Only judge candidates. Do not
   compare every skill against every other.

   The report answers five questions in order: out of date, duplicated,
   conflicting, missing pieces, unuseful or out of place. Some answers are
   already in the inventory and need no judgement:
   - every managed skill whose `status` is `stale`, `pending` or `conflict` is an
     `out_of_date` finding, with `status_reasons` as evidence;
   - every `missing_dependencies` entry is a `missing_dependency` finding with an
     `import` action;
   - every `broken_references` entry is a `broken_reference` finding with a
     `fix_link` action.

2. **Read any earlier decisions** in `.sss/decisions.yaml`. A finding whose ID has a
   recorded decision is settled: apply the decision, do not ask again.

3. **Judge each candidate pair.** Open both SKILL.md files. Decide:
   - `duplicate`: they cover the same ground. Recommend the keeper. Prefer a skill
     from a source of truth over a local one, and the newer over the older.
   - `conflict`: they disagree on a fact or an instruction. Quote the exact lines
     that disagree from each side. Say in one sentence what goes wrong if nothing
     is done. A pair can be both a duplicate and a conflict; file both.
   - neither: list it under `left_alone` with a one-line reason.
   Every finding needs at least one `evidence` entry with a quote. Confidence is a
   word: `confident`, `likely`, or `unsure`.

4. **Judge every skill on its own** for the last two questions, briefly:
   - `out_of_date` by content: it describes a flag, API, version or product that
     has since changed. Quote the line and say what is true now. Only file this
     when you are sure; otherwise leave it alone.
   - `out_of_place`: it has nothing to do with what this repo does, or sits in
     the wrong folder. Quote its description and say why it does not fit.
   - `low_value`: it would not help an agent do anything: vague, trivially short,
     or only a list of links. Quote what little it says.

5. **Write the JSON** to `.sss/reports/reorganize-report.json` following the
   schema. Copy the inventory entries from step 1 and add a one-line `goal` to
   each, in words a newcomer would understand. Then render:
   ```bash
   python3 .sss/tool/sss.py report
   ```
   This writes `.sss/reports/reorganize-report.md`. The renderer fills IDs,
   forces `decision_needed` for conflicts, for `unsure` findings and for any
   `remove` action, computes the summary, and appends an appendix with every
   skill, its goal, and the concerns that touch it. `.sss/reports/` is
   gitignored: the report is a local working document and is never committed.

6. **Apply only the safe actions**, meaning findings with `decision_needed: false`:
   - A duplicate of a managed skill is handled by `deprecate` on the copy.
   - A reconcile is a new patch: `python3 .sss/tool/sss.py patch new <skill> --intent "..."`,
     then follow the `update-skills` flow for that skill.
   - A broken link is fixed in the patch or local skill, never in generated output.
   Anything needing a decision is left alone and listed in the report.

7. **Open the PR** against this repo on a new branch, if there is at least one
   safe action or the user asked for one. The PR body is the full text of
   `.sss/reports/reorganize-report.md`. Title: "Reorganize skills: N findings,
   M need a decision". Do not commit the report files; they are gitignored.
   If there is nothing safe to apply, skip the PR and hand the user the report
   path instead.

## Reporting back

Summarise for the user in plain language: how many skills, how many problems, what
you changed, and exactly which IDs need their answer. A second-year CS student
should be able to follow it. Give them the path `.sss/reports/reorganize-report.md`
and point at section 10 for how to answer.

## Rules

- Never write "semantic", "deduplicate", "normalize", or "refactor" in the report.
  Say "means the same", "remove the copy", "tidy", "reorganize".
- Never remove a skill without a recorded decision.
- Never edit files under `.sss/sources/` or generated output by hand.
