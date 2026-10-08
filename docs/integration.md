# Integrating SSS into a repo

This document defines what SSS puts into a target repo, how the pieces relate,
and how the three commands work against them. "Target repo" means any repo that
wants to use skills managed by SSS. SSS is generic: it does not care what the
target repo does, and it works with Claude Code, Codex and Gemini CLI.

## For non-technical readers

Think of the source of truth as a cookbook, and the repo as a kitchen. The
kitchen wants its own copy of the recipes, a few local changes to some of them,
and a way to pick up the cookbook's corrections later without losing those
changes.

SSS keeps four things in the kitchen:

1. An exact copy of the cookbook, untouched.
2. The kitchen's notes on what to change, written per recipe, in plain language.
3. A table of contents saying where each recipe came from, when it was last
   copied, and which notes apply to it.
4. The finished recipes the kitchen actually cooks from, produced by applying
   the notes to the cookbook's recipes.

People only ever edit 2 and 3. SSS refreshes 1 from the cookbook and rebuilds 4
whenever 1 or 2 changes. The finished recipes in 4 are saved in the repo so
anyone can read them without running anything, but nobody edits them by hand,
because the next rebuild would overwrite the edit.

If the cookbook changes a recipe so much that a note no longer makes sense, SSS
does not guess. It marks that recipe as needing a person's attention.

## The four parts

| Part | What it is | Who writes it | Hand edits |
| --- | --- | --- | --- |
| 1. Source replica | Letter-for-letter copy of the source of truth | SSS, on sync | Never |
| 2. Semantic patches | Local, high-level change requests per skill | People | Yes |
| 3. Manifest | Where each skill came from, when it was synced, which patches apply | People and SSS | Yes, for the fields people own |
| 4. Generated skills | The skills the repo actually uses | SSS, on generate | Never |

Part 4 is committed to the repo. It is derived, so it is regenerated whenever
part 1 or part 2 changes for that skill.

## Installation

SSS is added to the target repo as a git submodule at a fixed path, then
initialised. The fixed path matters because the command skills refer to it.

```bash
git submodule add https://github.com/haoxuw/skillful-skills-scaler .sss/tool
python3 .sss/tool/sss.py init
```

`init` creates `.sss/manifest.yaml`, the `patches`, `sources` and `local`
folders, and links SSS's three command skills into the skill directories that
each agent runtime reads:

| Runtime | Reads | How SSS reaches it |
| --- | --- | --- |
| Codex CLI | `.agents/skills/` | writes there directly (`output_dir`) |
| Gemini CLI | `.agents/skills/` or `.gemini/skills/` | same directory; workspace must be trusted |
| Claude Code | `.claude/skills/` only | a symlink per skill into `.claude/skills/` (`mirror_dirs`) |

All three runtimes follow symlinks. On a file system without symlinks, run
`init --copy` to copy instead, and re-run `sss links --copy` after each
generate. The command skills then appear as `/update-skills`,
`/reorganize-skills` and `/deprecate-skills` in Claude Code, as
`$update-skills` and friends in Codex, and by description in Gemini. Saying
"update skills using sss" works everywhere.

SSS needs Python 3.12 or newer and PyYAML. Nothing else.

## Layout in the target repo

```
.sss/
  tool/                      # SSS itself, as a submodule
  manifest.yaml              # part 3
  decisions.yaml             # answers to reorganize findings
  reports/                   # reorganize reports; gitignored, local only
  sources/
    <source-name>/           # part 1, one folder per source
      LICENSE                # carried along from the source
      <skills_root>/<skill>/
  local/
    <skill>/                 # skills authored in this repo, treated as a source
  patches/
    <skill-name>.md          # part 2, one file per patched skill
.agents/skills/              # part 4, output_dir (configurable)
  <skill-name>/SKILL.md
  update-skills -> ../../.sss/tool/skills/update-skills
.claude/skills/              # mirror_dirs: one symlink per entry above
```

Only the `skills_root` subtree of a source is replicated, not the whole source
repo, plus its LICENSE and NOTICE files. The replica can be a plain copy or a
git submodule. The manifest records which. Both give the same guarantee: the
files match the recorded source commit exactly.

Skill scanners that walk the whole repo would find the replica as a second copy
of every skill. SSS's own inventory excludes `.sss/`, and the replica folder
carries a `.sss-replica` marker file. Tell other scanners to ignore `.sss/`.

## The manifest

```yaml
schema_version: 1
output_dir: .agents/skills
mirror_dirs: [.claude/skills]

sources:
  - name: cookbook
    url: https://github.com/org/cookbook
    ref: main
    mode: copy            # copy | submodule | local
    path: .sss/sources/cookbook
    skills_root: skills   # folder inside the source where skills live
    synced_commit: 3f9a2c1e...
    synced_at: 2026-10-08T14:30:00Z

skills:
  - name: omelette
    from: cookbook/omelette
    patches: [.sss/patches/omelette.md]
    status: ok            # pending | ok | stale | conflict | failed
    generated_at: 2026-10-08T14:31:00Z

  - name: salad
    from: cookbook/salad
    patches: []           # pure copy, no local changes
    status: ok
```

Who owns which fields:

- People write `output_dir`, `mirror_dirs`, each source's `name`, `url`, `ref`,
  `mode`, `path`, `skills_root`, and each skill's `name`, `from`, `patches`.
- SSS writes `synced_commit`, `synced_at`, `generated_at`, `status` and
  `conflict`. It never changes the fields people own.

A skill with an empty `patches` list is still generated, as a straight copy, so
that part 4 is always the single place the repo reads from. The generated
skill's `name` is set to the manifest name, so two sources can both offer a
`cluster-lifecycle` and the repo can import both under different names.

Skills authored in the repo itself live under `.sss/local/<skill>/` and are
listed with a source of `mode: local`. They flow through the same generate step,
which means reorganize can treat local and imported skills alike.

## Semantic patches

A patch is a markdown file with a small front matter block and a body written
for a model to read.

```markdown
---
target: omelette
intent: Make the house omelette.
checks:
  - The final skill says three eggs, not two.
  - contains: "three eggs"
  - not_contains: "two eggs"
  - file_exists: pan.md
---

Add one more egg and add bell pepper to the ingredient list. Keep every other
step exactly as the source has it.
```

Checks come in two kinds. A plain sentence is judged by the model after
generation. A `contains`, `not_contains`, `regex` or `file_exists` entry is
checked by SSS itself when the skill is finalized, and a failure blocks the
skill from being stamped as generated. Use the deterministic kind wherever the
expectation can be written as text.

## When part 4 gets rebuilt

Staleness is decided from the inputs, using git history, and never by
regenerating. For each skill, SSS finds the last commit that touched its output
folder, then asks whether any later commit touched its inputs: the replica
path for that skill and its patch files. Uncommitted changes to inputs count
too. In submodule mode the replica path is diffed inside the submodule between
the commit recorded in the skill's provenance and the current pointer, so a
pointer bump only marks the skills whose files actually changed.

The result is one of five states:

| Status | Meaning | What happens next |
| --- | --- | --- |
| `pending` | Imported but never generated | generate or plan |
| `ok` | Output is newer than every input | nothing |
| `stale` | An input changed after the output was made | generate or plan |
| `conflict` | A patch no longer applies to the source, or the source skill vanished | a person decides |
| `failed` | A deterministic check failed at finalize | fix the output and finalize again |

A sync with no upstream changes and no patch edits produces no diff.

### The CI gate

```bash
python3 .sss/tool/sss.py status --fail-on-stale
```

This exits non-zero if any skill is anything other than `ok`. It reads git
history only. It never calls a model, so it needs no credentials and is
deterministic. Do not try to enforce freshness by regenerating in CI: the model
step is not byte-for-byte reproducible, so that check would always fail.

## How generation works

Unpatched skills are copied from the replica, their `name` is set, and a
provenance block is added. That step is deterministic and runs anywhere.

Patched skills are produced by the agent, inside whatever session the user is
in. `sss plan <skill>` gives the agent the new source, the patches, the
previous output, and a copy of the previous source when one exists. The agent
is told to diff the previous source against the previous output, re-apply those
same edits to the new source, and fall back to the patch's intent only where an
old edit no longer fits. That keeps the diff between generations small. If the
source no longer contains what a patch assumes, the agent records a conflict
instead of guessing. `sss finalize <skill>` then runs the deterministic checks,
stamps provenance, and marks the skill `ok`.

## Provenance in generated skills

Every generated SKILL.md carries its origin inside the portable `metadata`
field, so a reader who opens it directly knows not to edit it:

```yaml
---
name: omelette
description: ...
metadata:
  sss:
    source: cookbook
    source_commit: 3f9a2c1e...
    source_path: .sss/sources/cookbook/skills/omelette
    patches: [.sss/patches/omelette.md]
    generated_at: 2026-10-08T14:31:00Z
    model: <model id, for patched skills>
    note: Generated by SSS. Do not edit. Change the patch or the source instead.
---
```

## Commands against this layout

| CLI command | Reads | Writes |
| --- | --- | --- |
| `init` | nothing | manifest, folders, links for the command skills |
| `source add` | manifest | source entry, replica, `synced_*` |
| `sync` | manifest, sources | refreshed replicas, `synced_*`, then prints status |
| `import` | manifest, replica | skill entry; copies it if unpatched, or creates a patch template |
| `status` | manifest, git history | nothing; `--fail-on-stale` for CI |
| `generate` | replica | unpatched outputs, provenance, links |
| `plan` | replica, patches, previous output | nothing; prints the agent's job |
| `finalize` | agent-written output, patches | provenance, `status`, links |
| `conflict` | nothing | `status: conflict` with a reason |
| `patch new` | manifest | a patch template, `status: stale` |
| `inventory` | the whole repo except `.sss/` and mirrors | nothing; prints JSON |
| `matrix pending` / `apply` / `show` | inventory, `.sss/reports/similarity.json` | the cached 0-5 star coverage scores the agent produces |
| `report` | findings JSON | the markdown report |
| `deprecate` | manifest | removes entry, patches, output, links; prints references |

The three command skills, `update-skills`, `reorganize-skills` and
`deprecate-skills`, tell the agent which of these to run and what judgement to
apply between them. The README's command numbering maps as follows: 1.1 is
`source add` plus `import`, 1.2 is `import --patch` or `patch new` plus `plan`
and `finalize`, 1.3 is `sync` followed by the same, 2.x is the
`reorganize-skills` skill over `inventory` and `report`, and 3.1 is `deprecate`.
