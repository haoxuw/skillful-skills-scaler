# Skillful-skills-scaler

# Problem
Smart agents needs a large amount of skills, which

May depends on each other, with base and derived variants.
May conflicts with each other: different approach, or outdated info.
May have many skills md and resources, each could be very long, and with dynamic reference to other files
May be stored in different media: file system, packages, submodules
May overlaps with each other after merged from sources

# Commands
1. Update
 1.1 Import skills from a different source of truth (SoT)
 1.2 Define a semantic patch, and apply it on a SoT to create a variant (used as the active skills locally)
 1.3 Sync with updates from SoT, and apply the patch

2. Reorganize
 (2.0) find all skills in the repo
 2.1 De-duplicate
 2.2 Discover poential conflicts, and align with user to create local semantic patch, or change SoT
 2.3 Output of reorganize is (A) a report of findings, using non technical language, and (B) a PR to the target repo (not this current repo), to reorganize the skills better

3. Deprecate
 3.1 remove a skill and references

## Semantic Patch
Refered in 1.2 . Often we have external sources of truth provide a base skill/doc. We want to import to our current solution, but adapt with a high level patch which is not built on string matching.

```
let's say, base says:
Skill01: To make a omelette, break two eggs, 1 butter, 1 tomato
Then in kube-agents, which defines a "patch" say
patch-Skill01: to make Kage flavored omelette, add one more egg, and bell pepper
Then we create a skill in kube-agents, say
1. pull the latest skills from Google skills as A
2. apply the matching agentic-patch from kube agents as f()
3. generate the "Integrated skill" A' = f(A)
4. update kube-agents with A'
so the final Skill01 would become:
 To make a omelette, break THREE eggs, 1 butter, 1 tomato, bell pepper
```

# Solution
We want to position this repo to be submodules for other repos to clone. During setup, we will put symlinks to the submodule, enable claude commands to evolve the parent repo to support `update` `reorganize` etc.
