# Skillful-skills-scaler

## Problem

Smart agents need a large number of skills, which:

- May depend on each other, with base and derived variants.
- May conflict with each other: different approaches, or outdated info.
- May have many skill markdown files and resources, each of which could be very long, with dynamic references to other files.
- May be stored in different media: file system, packages, submodules.
- May overlap with each other after being merged from multiple sources.

## Commands

### 1. Update

- **1.1** Import skills from a different source of truth (SoT).
- **1.2** Define a semantic patch, and apply it on a SoT to create a variant (used as the active skills locally).
- **1.3** Sync with updates from the SoT, and apply the patch.

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

We want to position this repo as a submodule for other repos to clone. During setup, we will put symlinks to the submodule, and enable Claude commands to evolve the parent repo to support `update`, `reorganize`, etc.
