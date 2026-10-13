---
name: sync-skills
description: Bring this repo's skills in line with their sources of truth. Add a source, import new skills from it, write or change the local semantic patches, fetch upstream changes, and regenerate what is stale. Use when asked to sync, update, import, pull, or patch skills, to add a skill from another repo, or when "sync-skills using sss" is mentioned.
license: Apache-2.0
metadata:
  sss: {command: sync}
---

# Sync skills

You are running SSS (Skillful-skills-scaler) in this repo. SSS keeps four things
under `.sss/`: an exact replica of each source of truth, local semantic patches,
a manifest, and the generated skills the repo actually uses. The manifest,
`.sss/manifest.yaml`, is the mapping: for each skill, where it comes from and
which patches apply on top. Every step below creates or updates that manifest;
nothing is generated that the manifest does not describe.

Sync is one-way. SSS pulls from sources of truth and never pushes to them. A
fix that belongs upstream goes through an issue or a pull request there.

Run the CLI as `python3 .sss/tool/sss.py` from the repo root. Always pass
`--json` when you need to read the result. Rerunning this skill with nothing
new is a no-op.

## What the user may ask for

Work out which of these the request contains, and do them in this order:

| Request | Steps |
| --- | --- |
| "Add skills from <repo>" | 1, 2, 3 (if patches), 5, 6, 7 |
| "Import <skill> from <source>" | 2, 3 (if patches), 5, 6, 7 |
| "Patch <skill> so that ..." | 3, 5, 6, 7 |
| "Sync" / "update" / "pull the latest" | 4, 5, 6, 7 |

## Steps

1. **Add a source of truth** when the user names a repo that is not yet in the
   manifest. Ask for nothing you can infer: the skills root is usually
   `skills` or `.agents/skills`; check with a quick clone if unsure.
   ```bash
   python3 .sss/tool/sss.py --json source add <name> <url> --ref <branch> --skills-root <dir>
   ```
   The result lists `available_skills`. If the list is empty, the skills root is
   wrong: run `source add` again with the same name and the right
   `--skills-root`; a source nothing depends on yet is corrected in place.
   Choose copy mode unless the user asks for a submodule.

2. **Import skills.** For each skill the user wants:
   ```bash
   python3 .sss/tool/sss.py --json import <source>/<path> [--as <local-name>]
   ```
   An unpatched import is generated at once. If the user also wants local
   changes to it, add `--patch "<one-line intent>"` instead; that creates the
   patch file and leaves the skill `pending` for step 3. If the user says
   "all" or names a category, import every entry under it. A name that already
   exists in the manifest is an error; use `--as` to give it another name.

3. **Write or change a patch.** A patch is `.sss/patches/<skill>.md`: front
   matter with `target`, `intent`, and `checks`, then a body written for a
   model. Turn the user's words into it:
   - `intent`: one line.
   - body: what to add, remove or reword, and the sentence "Keep everything
     else exactly as the source has it."
   - `checks`: at least one deterministic check (`contains`, `not_contains`,
     `regex`, `file_exists`) for every concrete expectation, plus one plain
     sentence check for the overall intent. A text check reads SKILL.md unless
     it names another file in the skill folder:
     `- {contains: "02:00", file: "reference/runbook.md"}`. No other shapes.
   For a skill that has no patch yet, create one with
   `python3 .sss/tool/sss.py patch new <skill> --intent "..."` and then edit
   the file. Show the patch to the user in your summary; it is the thing they
   own.

4. **Fetch upstream changes.**
   ```bash
   python3 .sss/tool/sss.py --json fetch
   ```
   `fetched` says which sources moved and to which commit. `status` lists every
   skill as `ok`, `stale`, `pending`, `conflict`, or `failed`, with reasons.
   Report conflicts to the user and do not touch them.

5. **Regenerate unpatched skills** (`patched: false`) that are `stale` or
   `pending`:
   ```bash
   python3 .sss/tool/sss.py --json generate <skill>
   ```
   A straight copy. No judgement needed.

6. **Regenerate patched skills** (`patched: true`) that are `stale` or
   `pending`. Each is independent of the others, so fan out: if your runtime
   can run subagents or parallel tasks, give each patched skill its own worker
   that does everything in this step and returns `finalized`, `failed` or
   `conflict` with one line of explanation. If you cannot fan out, do them one
   at a time. For each skill:
   ```bash
   python3 .sss/tool/sss.py plan <skill>
   ```
   Follow the `instructions` in the JSON exactly. In short:
   - Read the new source under `source.dir`, every file.
   - Read each patch's `intent` and `body`.
   - If `previous_source_dir` is set, diff it against the current output to see
     the edits made last time, and re-apply those same edits to the new source.
     Use the patch body only where an old edit no longer fits.
   - Make the smallest edits that satisfy each patch. Everything the patches do
     not mention must stay letter for letter as the source has it.
   - If a patch assumes something the source no longer contains, stop and
     record it:
     ```bash
     python3 .sss/tool/sss.py conflict <skill> --reason "<what no longer applies>"
     ```
   - Write the result into the folder named by `output` in the plan (SKILL.md
     plus any other source files).
   - Check every `sentence_checks` item against what you wrote. Fix or record a
     conflict if one fails.
   - Stamp it:
     ```bash
     python3 .sss/tool/sss.py --json finalize <skill> --model "<your model id>"
     ```
     If finalize reports `failed`, read `failures`, fix the output, and run it
     again.

7. **Verify and commit.**
   ```bash
   python3 .sss/tool/sss.py --json status
   ```
   Then commit `.sss/` and the skills folder together, in one commit, with a
   message that names the sources and commits fetched and the skills imported
   or regenerated. Do not commit if the user asked only for a dry run.

## Reporting back

Tell the user in plain language: which sources were added or moved and to
which commit, which skills were imported, which patches were written or
changed (quote the intent), which skills were regenerated and why, and which
are in conflict and what the conflict is. A second-year CS student should be
able to follow it. Do not paste JSON.

## Rules

- Never edit files under `.sss/sources/` by hand, and never hand-edit a skill
  the manifest manages except as the generation step above. Skills in the same
  folder that the manifest does not list are the repo's own; leave them alone.
- Never change manifest fields that SSS owns (`synced_commit`, `synced_at`,
  `generated_at`, `status`, `conflict`).
- Never push to a source of truth.
- If `.sss/manifest.yaml` is missing, run `python3 .sss/tool/sss.py init` first
  and tell the user you did.
