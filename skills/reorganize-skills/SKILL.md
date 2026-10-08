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
   This lists every skill (excluding replicas and mirrors), its source, size,
   references, broken references, and `candidates`: pairs that look alike by
   identical body or by overlapping names and descriptions. Only judge candidates.
   Do not compare every skill against every other.

2. **Read any earlier decisions** in `.sss/decisions.yaml`. A finding whose ID has a
   recorded decision is settled: apply the decision, do not ask again.

3. **Judge each candidate pair.** Open both SKILL.md files. Decide:
   - `duplicate`: they cover the same ground. Recommend the keeper. Prefer a skill
     from a source of truth over a local one, and the newer over the older.
   - `conflict`: they disagree. Quote the exact lines that disagree from each side.
     Say in one sentence what goes wrong if nothing is done.
   - neither: list it under `left_alone` with a one-line reason.
   Every finding needs at least one `evidence` entry with a quote. Confidence is a
   word: `confident`, `likely`, or `unsure`.

4. **Broken references** from the inventory become `broken_reference` findings with
   a `fix_link` action.

5. **Write the JSON** to `reorganize-report.json` following the schema, then render:
   ```bash
   python3 .sss/tool/sss.py report reorganize-report.json --out reorganize-report.md
   ```
   The renderer fills IDs, forces `decision_needed` for conflicts, for `unsure`
   findings and for any `remove` action, and computes the summary.

6. **Apply only the safe actions**, meaning findings with `decision_needed: false`:
   - A duplicate of a managed skill is handled by `deprecate` on the copy.
   - A reconcile is a new patch: `python3 .sss/tool/sss.py patch new <skill> --intent "..."`,
     then follow the `update-skills` flow for that skill.
   - A broken link is fixed in the patch or local skill, never in generated output.
   Anything needing a decision is left alone and listed in the report.

7. **Open the PR** against this repo on a new branch. The PR body is the markdown
   report. Title: "Reorganize skills: N findings, M need a decision". Include both
   report files in the PR.

## Reporting back

Summarise for the user in plain language: how many skills, how many problems, what
you changed, and exactly which IDs need their answer. A second-year CS student
should be able to follow it. Point them at section 8 of the report for how to answer.

## Rules

- Never write "semantic", "deduplicate", "normalize", or "refactor" in the report.
  Say "means the same", "remove the copy", "tidy", "reorganize".
- Never remove a skill without a recorded decision.
- Never edit files under `.sss/sources/` or generated output by hand.
