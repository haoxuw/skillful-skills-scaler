---
name: deprecate-skills
description: Remove a skill managed by SSS along with its patches, generated output and links, then clean up references to it. Use when asked to deprecate, retire, remove or delete a skill, or when "deprecate-skills using sss" is mentioned.
license: Apache-2.0
metadata:
  sss: {command: deprecate}
---

# Deprecate a skill

You are running SSS (Skillful-skills-scaler). Run the CLI as
`python3 .sss/tool/sss.py` from the repo root.

## Steps

1. **Confirm the target** with the user if the name is ambiguous. Show them the
   entry from `.sss/manifest.yaml` and the output folder that will go away. Removal
   is destructive, so do not proceed on a guess.

2. **Remove it.**
   ```bash
   python3 .sss/tool/sss.py --json deprecate <skill>
   ```
   This drops the manifest entry, deletes its patches (unless `--keep-patches`),
   deletes the generated folder and every mirror link, and returns `references`:
   every remaining mention of the skill name in markdown, YAML, JSON and TOML files
   outside the replicas.

3. **Handle each reference.**
   - In a local skill or a doc: edit it to drop or replace the mention.
   - In a generated skill: do not edit the output. Add or extend that skill's patch
     with an instruction like "do not mention `<skill>`; it was removed", then follow
     the `sync-skills` flow for that skill.
   - In `.sss/decisions.yaml`: leave it, history is fine.

4. **Verify** with `python3 .sss/tool/sss.py --json status` and `git status`, then
   commit `.sss/`, the output directory and any edited files together.

## Reporting back

Tell the user what was removed, which files still mentioned it and what you did
about each, in plain language.
