# Skillful-skills-scaler

## Problem

Smart agents need a large number of skills, which:

- May depend on each other, with base and derived variants.
- May conflict with each other: different approaches, or outdated info.
- May have many skill markdown files and resources, each of which could be very long, with dynamic references to other files.
- May be stored in different media: file system, packages, submodules.
- May overlap with each other after being merged from multiple sources.

## What makes a skill useful

A skill is a set of instructions an agent loads before it works. The model behind the agent already knows how most tools and products work. A skill that repeats that knowledge adds nothing: the agent would do the same without it, and the text costs attention on every task.

A useful skill records what the model cannot know on its own: how this team prefers the agent to behave. That is a business workflow, a preferred methodology, a house rule, a default the team has chosen, or an order of steps the team requires. The test for each skill is: remove every sentence a capable model would follow unprompted; what remains is the skill's value. If nothing remains, the skill is unuseful and should go. If what remains is preference, policy or workflow, the skill is useful; if it is buried in general text, the skill should be cut down to it. Skills should be biased towards those preferences and standards, not towards general knowledge.

The `reorganize` command applies this test to every skill. The report names, per skill, what it adds beyond what the model already does, and flags skills where that is nothing.

## Commands

### 1. Sync

- **1.1** Import skills from a different source of truth (SoT). The manifest records where each skill comes from.
- **1.2** Define a semantic patch, and apply it on a SoT to create a variant (used as the active skills locally). The manifest records which patches apply to which skill.
- **1.3** Fetch updates from the SoT, and re-apply the patches. Sync is one-way: SSS pulls from the SoT and never pushes to it.

### 2. Reorganize

- **2.0** Find all skills in the repo.
- **2.1** De-duplicate.
- **2.2** Discover potential conflicts, and align with the user to either create a local semantic patch or change the SoT.
- **2.3** The output of reorganize is:
  - **(A)** a report of findings, using non-technical language, and
  - **(B)** a PR to the target repo (not this current repo), to reorganize the skills better.

### 3. Deprecate

- **3.1** Remove a skill and its references.

## Semantic Patch

Referred to in 1.2. External sources of truth provide base skills. We want to import them, but adapt them with a high-level patch which is not built on string matching.

Think of the source of truth as a cookbook, and the repo as a kitchen. The cookbook says:

> **Skill01:** To make an omelette, break two eggs, 1 butter, 1 tomato.

The kitchen defines a patch:

> **patch-Skill01:** For the house omelette, add **one more** egg and bell pepper.

To produce the kitchen's skill:

1. Pull the latest cookbook as `A`.
2. Apply the kitchen's matching patch as `f()`.
3. Generate the integrated skill `A' = f(A)`.
4. Update the kitchen with `A'`.

The final Skill01 becomes:

> To make an omelette, break **three** eggs, 1 butter, 1 tomato, bell pepper.

## Solution

This repo is added to other repos as a git submodule at `.sss/tool`. Running `sss init` creates `.sss/` in the parent repo and symlinks the SSS command skills into the skill directories that Claude Code, Codex and Gemini CLI each read, so the parent repo gains `sync-skills`, `reorganize-skills` and `deprecate-skills` in every runtime.

```bash
git submodule add https://github.com/haoxuw/skillful-skills-scaler .sss/tool
python3 .sss/tool/sss.py init
python3 .sss/tool/sss.py source add cookbook https://github.com/org/cookbook --skills-root skills
python3 .sss/tool/sss.py import cookbook/omelette --patch "House omelette"
```

The deterministic steps (fetch, staleness, inventory, deprecate) are a small Python CLI. The model steps (applying a patch, judging duplicates and conflicts) are done by whichever agent the user is already in, guided by the command skills.

- [docs/integration.md](docs/integration.md): what SSS puts into a repo and how the commands work against it.
- [docs/report-schema.md](docs/report-schema.md): the shape of the reorganize report.

## License

Copyright 2026 Google LLC. Source code is licensed under the
[Apache License, Version 2.0](LICENSE). Documentation under `docs/` is licensed
under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This is not an
officially supported Google product.
