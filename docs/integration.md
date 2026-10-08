# Integrating SSS into a repo

This document defines what SSS puts into a target repo and how the pieces
relate. "Target repo" means any repo that wants to use skills managed by
SSS. SSS itself is generic and does not care what the target repo does.

## For non-technical readers

Think of a cookbook you borrowed from a friend. You want to keep your own
copy, make a few changes to some recipes, and still pick up your friend's
corrections when they update their book.

SSS keeps four things in your repo:

1. An exact copy of your friend's cookbook, untouched.
2. Your notes on what to change, written per recipe, in plain language.
3. A table of contents saying where each recipe came from, when you last
   copied it, and which notes apply to it.
4. The finished recipes you actually cook from, produced by applying your
   notes to your friend's recipes.

You only ever edit 2 and 3. SSS refreshes 1 from your friend and rebuilds 4
whenever 1 or 2 changes. The finished recipes in 4 are saved in the repo so
anyone can read them without running anything, but nobody edits them by
hand, because the next rebuild would overwrite the edit.

## The four parts

| Part | What it is | Who writes it | Hand edits |
| --- | --- | --- | --- |
| 1. Source replica | Letter-for-letter copy of the source of truth | SSS, on sync | Never |
| 2. Semantic patches | Local, high-level change requests per skill | People | Yes |
| 3. Manifest | Where each skill came from, when it was synced, which patches apply | People and SSS | Yes, for the parts people own |
| 4. Generated skills | The skills the repo actually uses | SSS, on generate | Never |

Part 4 is committed to the repo. It is derived, so it must be regenerated
whenever part 1 or part 2 changes. A generated skill that is older than the
last change to its source or its patches is stale.

## Layout in the target repo

```
.sss/
  manifest.yaml              # part 3
  sources/
    <source-name>/           # part 1, one folder per source
  patches/
    <skill-name>.md          # part 2, one file per patched skill
<output_dir>/
  <skill-name>/              # part 4, path set in the manifest
    SKILL.md
```

The source replica under `.sss/sources/` can be either a plain copy or a git
submodule. The manifest records which. Both give the same guarantee: the
files match the source commit exactly.

The output directory is whatever the target repo's agent runtime reads
from. For Claude Code that is `.claude/skills`. SSS does not assume a
runtime, it only writes where the manifest says.

## The manifest

```yaml
schema_version: 1
output_dir: .claude/skills

sources:
  - name: upstream-a
    url: https://github.com/org/repo
    ref: main
    mode: copy            # or: submodule
    path: .sss/sources/upstream-a
    skills_root: skills   # folder inside the source where skills live
    synced_commit: 3f9a2c1
    synced_at: 2026-10-08T14:30:00Z

skills:
  - name: omelette
    from: upstream-a/omelette
    patches:
      - .sss/patches/omelette-kage.md
    generated_at: 2026-10-08T14:31:00Z

  - name: cluster-lifecycle
    from: upstream-a/cluster-lifecycle
    patches: []           # pure copy, no local changes
    generated_at: 2026-10-08T14:31:00Z
```

Who owns which fields:

- People write `output_dir`, each source's `name`, `url`, `ref`, `mode`,
  `path`, `skills_root`, and each skill's `name`, `from`, `patches`.
- SSS writes `synced_commit`, `synced_at`, and `generated_at`. It never
  changes the fields people own.

A skill listed with an empty `patches` list is still generated, as a
straight copy, so that part 4 is always the single place the repo reads
from.

## Semantic patches

A patch is a markdown file with a small front matter block and a body
written for a model to read.

```markdown
---
target: omelette
intent: Make the Kage flavored variant.
checks:
  - The final skill says three eggs, not two.
  - The final skill mentions bell pepper in the ingredients.
---

Add one more egg and add bell pepper to the ingredient list. Keep every
other step exactly as the source has it.
```

`checks` are plain sentences. After generation, SSS asks a model whether
each check holds against the generated skill, and fails the generation if
any does not. This is what keeps a model-driven step honest.

## When part 4 gets rebuilt

Part 4 is rebuilt for a skill when either of these is true:

- The source replica for that skill changed since the skill was last
  generated. SSS finds this with `git log` on the replica path, compared
  against the skill's `generated_at` commit.
- Any patch listed for that skill changed since it was last generated. Same
  check, on the patch files.

If neither changed, the skill is left exactly as committed. A `sync` with no
upstream changes and no patch edits produces no diff.

A CI check can enforce this by running generate and failing if the working
tree is dirty afterwards, the same way generated code is checked today.

## Provenance in generated skills

Every generated SKILL.md carries its origin in front matter, so a reader
who opens it directly knows not to edit it:

```yaml
---
name: omelette
description: ...
sss:
  source: upstream-a
  source_commit: 3f9a2c1
  source_path: skills/omelette
  patches: [omelette-kage.md]
  generated_at: 2026-10-08T14:31:00Z
---
```

## Commands against this layout

| Command | Reads | Writes |
| --- | --- | --- |
| `update` import | manifest | adds a source replica, adds skill entries |
| `update` sync | manifest, source | refreshes replica, updates `synced_*`, regenerates stale skills |
| `update` patch | manifest, patches | regenerates the patched skill |
| `reorganize` | everything | report, and a PR editing patches, manifest, and generated skills |
| `deprecate` | manifest | removes the skill entry, its patches, its generated folder, and references to it |
