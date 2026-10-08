---
name: update-skills
description: Sync skills from their sources of truth and regenerate the ones that changed, applying this repo's semantic patches. Use when asked to update skills, sync skills, pull the latest skills, re-apply skill patches, or when "update-skills using sss" is mentioned.
license: Apache-2.0
metadata:
  sss: {command: update}
---

# Update skills

You are running SSS (Skillful-skills-scaler) in this repo. SSS keeps four things
under `.sss/`: an exact replica of each source, local semantic patches, a manifest,
and the generated skills the repo actually uses. Your job is the model step. The
deterministic steps are done by the `sss` CLI.

Run the CLI as `python3 .sss/tool/sss.py` from the repo root. If `sss` is on PATH,
that works too. Always pass `--json` when you need to read the result.

## Steps

1. **Sync and see what is stale.**
   ```bash
   python3 .sss/tool/sss.py --json sync
   ```
   The `status` list tells you, per skill: `ok`, `stale`, `pending`, `conflict`, or
   `failed`, with reasons. Report conflicts to the user and do not touch them.

2. **Unpatched skills** (`patched: false`) that are `stale` or `pending`:
   ```bash
   python3 .sss/tool/sss.py --json generate <skill>
   ```
   This is a straight copy. No judgement needed.

3. **Patched skills** (`patched: true`) that are `stale` or `pending`. Each is
   independent of the others, so fan out: if your runtime can run subagents or
   parallel tasks, give each patched skill its own worker that does everything
   in this step and returns `finalized`, `failed` or `conflict` with one line of
   explanation. If you cannot fan out, do them one at a time. For each skill:
   ```bash
   python3 .sss/tool/sss.py plan <skill>
   ```
   Follow the `instructions` in the JSON exactly. In short:
   - Read the new source under `source.dir`, every file.
   - Read each patch's `intent` and `body`.
   - If `previous_source_dir` is set, diff it against the current output to see the
     edits made last time, and re-apply those same edits to the new source. Use the
     patch body only where an old edit no longer fits.
   - Make the smallest edits that satisfy each patch. Everything the patches do not
     mention must stay letter for letter as the source has it.
   - If a patch assumes something the source no longer contains, stop and record it:
     ```bash
     python3 .sss/tool/sss.py conflict <skill> --reason "<what no longer applies>"
     ```
   - Write the result into `output_dir` (SKILL.md plus any other source files).
   - Check every `sentence_checks` item against what you wrote. Fix or record a
     conflict if one fails.
   - Stamp it:
     ```bash
     python3 .sss/tool/sss.py --json finalize <skill> --model "<your model id>"
     ```
     If finalize reports `failed`, read `failures`, fix the output, and run it again.

4. **Verify** nothing is left:
   ```bash
   python3 .sss/tool/sss.py --json status
   ```

5. **Commit** the changes under `.sss/` and the output directory together, in one
   commit per sync, with a message that names the sources and commits synced. Do
   not commit if the user asked only for a dry run.

## Reporting back

Tell the user in plain language: which sources moved and to which commit, which
skills were regenerated and why, which are in conflict and what the conflict is.
A second-year CS student should be able to follow it. Do not paste JSON.

## Rules

- Never edit files under `.sss/sources/` or under the output directory by hand,
  except as the generation step above.
- Never change manifest fields that SSS owns (`synced_commit`, `synced_at`,
  `generated_at`, `status`, `conflict`).
- If the manifest or `.sss/` is missing, tell the user to run
  `python3 .sss/tool/sss.py init` first, or do it if they ask.
