# Skills reorganize report

## 1. Summary

We looked at 7 skills from 2 sources and scored all 21 pairs for how much ground they share. Three pairs share a lot of ground: the two observability skills and the two reliability skills are each a thin fork copy next to a fuller google copy, and the cluster-creation template disagrees with the golden-path settings on one monitoring component. Ten skills that these skills send the agent to are not in this repo but are available from the google source. A second, independent pass re-read every quoted line as a sceptic; it kept all 16 findings and changed 6 of them (lowered confidence on 3, tightened wording on 5). At the user's request nothing was applied and no pull request was opened; this run produced the report only.

| Question | Answer |
| --- | --- |
| Are any skills out of date? | Yes, 1 |
| Are any skills duplicated? | Yes, 2 |
| Do any skills give conflicting information? | Yes, 3 |
| Are any skills missing pieces they refer to? | Yes, 10 |
| Are any skills unuseful or out of place? | No |
| Actions we can take without asking | 10 |
| Decisions needed from you | 4 |

## 2. What we looked at

| Skill | Source | Status | Location | Files | Words | Last changed |
| --- | --- | --- | --- | --- | --- | --- |
| gcloud | google | ok | `.agents/skills/gcloud` | 3 | 3267 | 2026-10-08 |
| gke-cluster-creation | google | ok | `.agents/skills/gke-cluster-creation` | 1 | 1375 | 2026-10-08 |
| gke-golden-path | google | ok | `.agents/skills/gke-golden-path` | 2 | 1058 | 2026-10-08 |
| gke-observability | google | ok | `.agents/skills/gke-observability` | 1 | 1923 | 2026-10-08 |
| gke-observability-fork | gke-fork | ok | `.agents/skills/gke-observability-fork` | 1 | 510 | 2026-10-08 |
| gke-reliability | google | ok | `.agents/skills/gke-reliability` | 1 | 813 | 2026-10-08 |
| gke-reliability-fork | gke-fork | ok | `.agents/skills/gke-reliability-fork` | 1 | 409 | 2026-10-08 |

## 3. Out of date

These skills are behind their source, or describe things that have since changed.

### old-3f8abe: gke-observability-fork

The skill names a gcloud flag that does not exist. Running `gcloud container clusters update --help` on gcloud 587.0.0 shows --enable-dataplane-v2-flow-observability and --enable-dataplane-v2-metrics; there is no --enable-dataplane-v2-observability. The only related flag gcloud reports as removed is --dataplane-v2-observability-mode, so the fork's spelling may never have been valid rather than having aged out. Either way, an agent copying this command gets an 'unrecognized arguments' error.

Evidence:
- `gke-observability-fork/SKILL.md:126`: "--enable-dataplane-v2-observability \"

**Recommendation** (confident): If the duplicate finding above is accepted and the fork is removed, nothing more is needed. If the fork is kept, write a local patch that replaces the flag with --enable-dataplane-v2-flow-observability.

Decision needed: yes

## 4. Duplicates

These skills cover the same ground: 0 or 1 star in the coverage matrix (see the appendix). Keeping both wastes the agent's attention and lets them drift apart.

### dup-f87aa3: gke-observability, gke-observability-fork

Two skills answer the same GKE monitoring questions. The fork is a 510-word checklist; the google copy is a 1,923-word guide that covers every step the fork has and adds cost, alerting and Managed Prometheus troubleshooting. Agents that pick the fork get the thinner answer and, in one place, a flag that gcloud rejects.

Evidence:
- `gke-observability/SKILL.md:3`: "description: Configures GKE observability, including Cloud Logging, Cloud Monitoring, and managed Prometheus."
- `gke-observability-fork/SKILL.md:3`: "description: Workflows for setting up and auditing observability (logging, monitoring, tracing) on GKE."
- `gke-observability/SKILL.md:96`: "gcloud container clusters update <CLUSTER_NAME> --region <REGION> \ --enable-managed-prometheus"
- `gke-observability-fork/SKILL.md:40`: "gcloud container clusters update <cluster-name> \ --enable-managed-prometheus"

**Recommendation** (confident): Keep gke-observability. It comes from the google source of truth, carries a version (1.1.0), and covers everything the fork does. Remove gke-observability-fork. The fork's one extra tip, log as JSON, is a single line and can be added to a local patch if the team wants it.

Decision needed: yes

### dup-5e3bec: gke-reliability, gke-reliability-fork

Two skills answer the same GKE reliability questions. Five of the fork's six workflows appear in the google copy with recommended probe timings, MCP commands and replica counts the fork lacks. Agents that pick the fork get less guidance and a lower bar for probes and PDBs.

Evidence:
- `gke-reliability/SKILL.md:3`: "description: Improves GKE workload reliability, using PDBs, health probes, and topology spread constraints."
- `gke-reliability-fork/SKILL.md:3`: "description: Workflows for ensuring high availability and reliability of GKE workloads."
- `gke-reliability/SKILL.md:56`: "gcloud container clusters describe <CLUSTER> --region <REGION> \ --format="json(location, locations)""
- `gke-reliability-fork/SKILL.md:27`: "gcloud container clusters describe <cluster-name> --region <region> --format="json(location, locations)""

**Recommendation** (confident): Keep gke-reliability. It comes from the google source of truth, carries a version (1.0.1), and covers everything the fork does except a six-line maintenance-window command. The gke-upgrades skill, proposed for import in this report, covers maintenance windows and the same gcloud flags. Remove gke-reliability-fork.

Decision needed: yes

## 5. Conflicts

These skills disagree. An agent that loads both will get two answers.

### conf-2995f5: gke-observability, gke-observability-fork

The two skills give different gcloud flags for the same job. Only one of them exists: gcloud 587 accepts --enable-dataplane-v2-flow-observability and has no --enable-dataplane-v2-observability (the nearest removed flag is --dataplane-v2-observability-mode). An agent following the fork will hand the user a command that fails. The fork also scopes control-plane metrics to Standard clusters (lines 108 and 137), while the google copy says they are off on every new cluster until enabled and treats them as part of the golden path, which is an Autopilot configuration (gke-cluster-creation template 1 enables them with create-auto).

Evidence:
- `gke-observability/SKILL.md:102`: "--enable-dataplane-v2-flow-observability \"
- `gke-observability-fork/SKILL.md:126`: "--enable-dataplane-v2-observability \"
- `gke-observability/SKILL.md:61`: "**Control-plane metrics are NOT enabled by default.** State this outright in your answer"
- `gke-observability-fork/SKILL.md:108`: "For Standard clusters, you can enable collection of metrics from the Kubernetes API server, scheduler, and controller manager."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 1: keep gke-observability (A), retire gke-observability-fork (B). The google copy has the flag that gcloud actually accepts, confirmed against gcloud 587 on this machine.

Decision needed: yes

### conf-2df4b9: gke-reliability, gke-reliability-fork

The two skills set different minimum bars in their Best Practices sections. The fork's best practice says a readiness probe is the minimum and frames PDBs as being for critical apps; the google copy says every production container needs both liveness and readiness probes with explicit timeouts, and every workload with two or more replicas needs a PDB. The disagreement is softer than it first looks: the fork's own workflow 3 (line 59) already asks for liveness and readiness on all production containers, so the fork is internally inconsistent rather than flatly opposed. Agents reading only the best-practice lists would still give users two different answers to 'is my deployment production ready'.

Evidence:
- `gke-reliability/SKILL.md:207`: "**Probes with Explicit Timeouts**: Every production container must have both liveness and readiness probes defined. **Always explicitly define `initialDelaySeconds`, `periodSeconds`, and `timeoutSeconds`**"
- `gke-reliability-fork/SKILL.md:108`: "**Probes for All Containers**: Every container in a production pod should have at least a readiness probe."
- `gke-reliability-fork/SKILL.md:59`: "Ensure all production containers have Liveness, Readiness, and optionally Startup probes."
- `gke-reliability/SKILL.md:205`: "**PDBs for everything**: Every production workload with 2+ replicas needs a PodDisruptionBudget (PDB)"
- `gke-reliability-fork/SKILL.md:109`: "**PDBs for Critical Apps**: Use PDBs to prevent downtime during automated node upgrades."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): Option 1: keep gke-reliability (A), retire gke-reliability-fork (B). The PDB rule matches the upgrade-disruption advice in gke-golden-path, which asks for PDBs and readiness probes on every production workload (gke-golden-path does not itself require liveness probes; only gke-reliability does).

Decision needed: yes

### conf-7bdb56: gke-cluster-creation, gke-golden-path

gke-cluster-creation says its production template matches the golden-path file exactly, but its --monitoring list leaves out JOBSET, which gke-golden-path, its asset file and gke-observability all list as a default. Its MCP create_cluster payload sets no monitoring components at all. A cluster built from either form of the template will then fail a golden-path audit on monitoring components. The unpatched upstream copy in .sss/sources/google has the same gap (SKILL.md line 124 and no monitoringConfig in the payload), so the local patch did not cause it; this is an upstream slip.

Evidence:
- `gke-cluster-creation/SKILL.md:120`: "This is the default. All settings match"
- `gke-cluster-creation/SKILL.md:136`: "--monitoring=SYSTEM,API_SERVER,SCHEDULER,CONTROLLER_MANAGER,STORAGE,POD,DEPLOYMENT,STATEFULSET,DAEMONSET,HPA,CADVISOR,KUBELET,DCGM \"
- `gke-golden-path/SKILL.md:88`: "SYSTEM_COMPONENTS, STORAGE, POD, DEPLOYMENT, STATEFULSET, DAEMONSET, HPA, JOBSET, CADVISOR, KUBELET, DCGM, APISERVER, SCHEDULER, CONTROLLER_MANAGER"
- `gke-golden-path/assets/golden-path-autopilot.yaml:124`: "- JOBSET"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4: open an issue upstream in google/skills, and meanwhile extend the existing local patch for gke-cluster-creation so template 1's --monitoring list includes JOBSET and its MCP payload carries a monitoringConfig matching the golden-path file. Keep both skills; they do different jobs.

Decision needed: yes

## 6. Missing pieces

These skills point at files or other skills that are not here.

### dep-9cc612: gke-cluster-creation

gke-cluster-creation sends the agent to a skill called gke-app-onboarding, which is not in this repo. The agent either stops or guesses. The skill is available from the google source. Also available from gke-fork/gke-app-onboarding (383 words). Prefer the google copy (650 words, versioned, the source the fork was taken from).

Evidence:
- `gke-cluster-creation/SKILL.md:7`: "or deployment configuration (use gke-app-onboarding instead)."

**Recommendation** (confident): Import google/cloud/gke-app-onboarding with `python3 .sss/tool/sss.py import google/cloud/gke-app-onboarding`.

Decision needed: no

### dep-67fb82: gke-cluster-creation

gke-cluster-creation sends the agent to a skill called gke-compute-classes, which is not in this repo. The agent either stops or guesses. The skill is available from the google source. Confidence is lower because the only mention is a comment inside a bash code block that points at a file (gke-compute-classes.md), the same kind of passing reference as the gke-platform-security YAML comment.

Evidence:
- `gke-cluster-creation/SKILL.md:267`: "# 2. Apply GPU ComputeClass (see gke-compute-classes.md)"

**Recommendation** (likely): Import google/cloud/gke-compute-classes with `python3 .sss/tool/sss.py import google/cloud/gke-compute-classes`.

Decision needed: no

### dep-83ebc8: gke-cluster-creation

gke-cluster-creation sends the agent to a skill called gke-inference, which is not in this repo. The agent either stops or guesses. The skill is available from the google source. Confidence is lower because the only mention is a comment inside a bash code block that points at a file (gke-inference.md), the same kind of passing reference as the gke-platform-security YAML comment.

Evidence:
- `gke-cluster-creation/SKILL.md:270`: "# 3. Or use GIQ for inference (see gke-inference.md)"

**Recommendation** (likely): Import google/cloud/gke-inference with `python3 .sss/tool/sss.py import google/cloud/gke-inference`.

Decision needed: no

### dep-66a61c: gke-golden-path

gke-golden-path sends the agent to a skill called gke-basics, which is not in this repo. The agent either stops or guesses. The skill is available from the google source.

Evidence:
- `gke-golden-path/SKILL.md:51`: "See the `gke-basics` skill's CLI reference for full coverage matrix and override options."

**Recommendation** (confident): Import google/cloud/gke-basics with `python3 .sss/tool/sss.py import google/cloud/gke-basics`.

Decision needed: no

### dep-90f015: gke-golden-path

gke-golden-path sends the agent to a skill called gke-cluster-autoscaler, which is not in this repo. The agent either stops or guesses. The skill is available from the google source.

Evidence:
- `gke-golden-path/SKILL.md:26`: "use `gke-cluster-autoscaler` for node autoscaling"

**Recommendation** (confident): Import google/cloud/gke-cluster-autoscaler with `python3 .sss/tool/sss.py import google/cloud/gke-cluster-autoscaler`.

Decision needed: no

### dep-8169c5: gke-golden-path

gke-golden-path sends the agent to a skill called gke-workload-scaling, which is not in this repo. The agent either stops or guesses. The skill is available from the google source. Also available from gke-fork/gke-workload-scaling (540 words). Prefer the google copy (667 words, versioned).

Evidence:
- `gke-golden-path/SKILL.md:27`: "`gke-workload-scaling` for workload autoscaling (HPA/VPA)."

**Recommendation** (confident): Import google/cloud/gke-workload-scaling with `python3 .sss/tool/sss.py import google/cloud/gke-workload-scaling`.

Decision needed: no

### dep-dfd880: gke-golden-path, gke-reliability

gke-golden-path and gke-reliability send the agent to a skill called gke-upgrades, which is not in this repo. The agent either stops or guesses. The skill is available from the google source.

Evidence:
- `gke-golden-path/SKILL.md:166`: "For rollback procedures and maintenance windows, see the `gke-upgrades` skill."
- `gke-reliability/SKILL.md:218`: "**Maintenance windows**: Schedule upgrades during low-traffic periods (see the `gke-upgrades` skill)."

**Recommendation** (confident): Import google/cloud/gke-upgrades with `python3 .sss/tool/sss.py import google/cloud/gke-upgrades`.

Decision needed: no

### dep-a44fa6: gke-reliability

gke-reliability sends the agent to a skill called gke-manifest-generation, which is not in this repo. The agent either stops or guesses. The skill is available from the google source.

Evidence:
- `gke-reliability/SKILL.md:22`: "To generate Kubernetes YAML manifests (`Deployment`, `StatefulSet`, `Service`, `ConfigMap`, `HTTPRoute`, `PodDisruptionBudget`), open `gke-manifest-generation/SKILL.md`."

**Recommendation** (confident): Import google/cloud/gke-manifest-generation with `python3 .sss/tool/sss.py import google/cloud/gke-manifest-generation`.

Decision needed: no

### dep-d5464f: gke-reliability

gke-reliability sends the agent to a skill called gke-backup-dr, which is not in this repo. The agent either stops or guesses. The skill is available from the google source. Also available from gke-fork/gke-backup-dr (294 words). Prefer the google copy (869 words, versioned).

Evidence:
- `gke-reliability/SKILL.md:7`: "backups (use gke-backup-dr)."

**Recommendation** (confident): Import google/cloud/gke-backup-dr with `python3 .sss/tool/sss.py import google/cloud/gke-backup-dr`.

Decision needed: no

### dep-49ebeb: gke-golden-path

gke-golden-path sends the agent to a skill called gke-platform-security, which is not in this repo. The agent either stops or guesses. The skill is available from the google source. Found by reading the asset file; the inventory only scans SKILL.md. Confidence is lower because the mention is a comment in a YAML file.

Evidence:
- `gke-golden-path/assets/golden-path-autopilot.yaml:54`: "# gke-platform-security skill"

**Recommendation** (likely): Import google/cloud/gke-platform-security with `python3 .sss/tool/sss.py import google/cloud/gke-platform-security`.

Decision needed: no

## 7. Unuseful or out of place

Nothing found.

## 8. Proposed changes

These are safe and the pull request applies them:

- Import google/cloud/gke-app-onboarding into gke-app-onboarding [dep-9cc612]
- Import google/cloud/gke-compute-classes into gke-compute-classes [dep-67fb82]
- Import google/cloud/gke-inference into gke-inference [dep-83ebc8]
- Import google/cloud/gke-basics into gke-basics [dep-66a61c]
- Import google/cloud/gke-cluster-autoscaler into gke-cluster-autoscaler [dep-90f015]
- Import google/cloud/gke-workload-scaling into gke-workload-scaling [dep-8169c5]
- Import google/cloud/gke-upgrades into gke-upgrades [dep-dfd880]
- Import google/cloud/gke-manifest-generation into gke-manifest-generation [dep-a44fa6]
- Import google/cloud/gke-backup-dr into gke-backup-dr [dep-d5464f]
- Import google/cloud/gke-platform-security into gke-platform-security [dep-49ebeb]

### Waiting on your decision

One line per action. Several findings can point at the same action; all their IDs are listed.

- Remove gke-observability-fork into gke-observability [dup-f87aa3, conf-2995f5]
- Remove gke-reliability-fork into gke-reliability [dup-5e3bec, conf-2df4b9]
- Patch gke-cluster-creation (Extend .sss/patches/gke-cluster-creation.md: add JOBSET to the template 1 --monitoring list and add a matching monitoringConfig to the template 1 MCP payload; file an upstream issue against google/skills.) [conf-7bdb56]
- Patch gke-observability-fork (Replace --enable-dataplane-v2-observability with --enable-dataplane-v2-flow-observability. Only if the fork is kept.) [old-3f8abe]

## 9. What we left alone

- **gcloud**: Scores 4 stars with every other skill. It is the rulebook the GKE skills' gcloud commands should follow, not a copy of any of them.
- **gke-golden-path, gke-observability**: 3 stars. Both list the golden-path monitoring components and they agree line for line; observability's core is operating the monitoring, golden-path's is the cluster settings.
- **gke-golden-path, gke-reliability**: 3 stars. Both ask for PDBs, two or more replicas and readiness probes around node upgrades, and they agree; each has its own core.
- **gke-cluster-creation, gke-reliability**: gke-reliability's defaults table says a regional cluster spans 4 zones (us-central1-a/b/c/f) while gke-cluster-creation says Standard regional defaults to 3 zones. Both are true: Autopilot uses every zone in the region, Standard picks three. Pair is 4 stars, so not filed.
- **gke-observability-fork**: Its Managed Prometheus check uses namespace gmp-system only; gke-observability notes Autopilot uses gke-gmp-system. Covered by the duplicate recommendation, not filed separately.
- **gke-cluster-creation, gke-golden-path**: Both local patches pin project kitchen-prod-1234 and both skills say regional; the team overrides agree with each other.
- **gke-cluster-creation**: Mentions of gke-app-onboarding, gke-compute-classes, gke-inference are in passing (a 'don't use for' note and two comments in a code block). Filed as imports per the rules, but these three are the least urgent of the imports.

## 10. How to respond

Each item marked "needs decision" has an ID like `conf-81be44`. Reply with the ID and your choice,
either as a comment on the pull request or by adding a line to `.sss/decisions.yaml`:

```yaml
dup-3f9a2c: accept
conf-81be44:
  choice: 3
  note: "Both are right in different regions."
```

The next run reads those answers and applies them. Items you have answered are not asked again.

## Appendix: every skill we found

One entry per skill. "Goal" is what the skill is for, in one line. "Concerns" lists every finding above that involves it.

### gcloud

- **Source:** google  **Status:** ok  **Location:** `.agents/skills/gcloud`
- **Goal:** Keep an agent's gcloud commands safe, correct and small: check syntax first, limit output, never delete without asking.
- **Concerns:** none

### gke-cluster-creation

- **Source:** google  **Status:** ok  **Location:** `.agents/skills/gke-cluster-creation`
- **Goal:** Create a new GKE cluster from one of five templates, defaulting to golden-path Autopilot in us-central1 and project kitchen-prod-1234.
- **Concerns:**
  - conflicts with gke-golden-path [conf-7bdb56]: Option 4: open an issue upstream in google/skills, and meanwhile extend the existing local patch for gke-cluster-creation so template 1's -… Decision needed.
  - missing dependency [dep-9cc612]: Import google/cloud/gke-app-onboarding with `python3 .sss/tool/sss.py import google/cloud/gke-app-onboarding`.
  - missing dependency [dep-67fb82]: Import google/cloud/gke-compute-classes with `python3 .sss/tool/sss.py import google/cloud/gke-compute-classes`.
  - missing dependency [dep-83ebc8]: Import google/cloud/gke-inference with `python3 .sss/tool/sss.py import google/cloud/gke-inference`.

### gke-golden-path

- **Source:** google  **Status:** ok  **Location:** `.agents/skills/gke-golden-path`
- **Goal:** List the settings a production GKE cluster should have, and what to tell users about node upgrade disruption.
- **Concerns:**
  - conflicts with gke-cluster-creation [conf-7bdb56]: Option 4: open an issue upstream in google/skills, and meanwhile extend the existing local patch for gke-cluster-creation so template 1's -… Decision needed.
  - missing dependency [dep-66a61c]: Import google/cloud/gke-basics with `python3 .sss/tool/sss.py import google/cloud/gke-basics`.
  - missing dependency [dep-90f015]: Import google/cloud/gke-cluster-autoscaler with `python3 .sss/tool/sss.py import google/cloud/gke-cluster-autoscaler`.
  - missing dependency [dep-8169c5]: Import google/cloud/gke-workload-scaling with `python3 .sss/tool/sss.py import google/cloud/gke-workload-scaling`.
  - missing dependency with gke-reliability [dep-dfd880]: Import google/cloud/gke-upgrades with `python3 .sss/tool/sss.py import google/cloud/gke-upgrades`.
  - missing dependency [dep-49ebeb]: Import google/cloud/gke-platform-security with `python3 .sss/tool/sss.py import google/cloud/gke-platform-security`.

### gke-observability

- **Source:** google  **Status:** ok  **Location:** `.agents/skills/gke-observability`
- **Goal:** Set up and troubleshoot logging, monitoring and Managed Prometheus on GKE.
- **Concerns:**
  - duplicate with gke-observability-fork [dup-f87aa3]: Keep gke-observability. It comes from the google source of truth, carries a version (1.1.0), and covers everything the fork does. Remove gk… Decision needed.
  - conflicts with gke-observability-fork [conf-2995f5]: Option 1: keep gke-observability (A), retire gke-observability-fork (B). The google copy has the flag that gcloud actually accepts, confirm… Decision needed.

### gke-observability-fork

- **Source:** gke-fork  **Status:** ok  **Location:** `.agents/skills/gke-observability-fork`
- **Goal:** A short checklist for turning on logging, monitoring and tracing on GKE.
- **Concerns:**
  - duplicate with gke-observability [dup-f87aa3]: Keep gke-observability. It comes from the google source of truth, carries a version (1.1.0), and covers everything the fork does. Remove gk… Decision needed.
  - conflicts with gke-observability [conf-2995f5]: Option 1: keep gke-observability (A), retire gke-observability-fork (B). The google copy has the flag that gcloud actually accepts, confirm… Decision needed.
  - out of date [old-3f8abe]: If the duplicate finding above is accepted and the fork is removed, nothing more is needed. If the fork is kept, write a local patch that r… Decision needed.

### gke-reliability

- **Source:** google  **Status:** ok  **Location:** `.agents/skills/gke-reliability`
- **Goal:** Keep GKE workloads up through node failures and upgrades with PDBs, probes, zone spread and enough replicas.
- **Concerns:**
  - duplicate with gke-reliability-fork [dup-5e3bec]: Keep gke-reliability. It comes from the google source of truth, carries a version (1.0.1), and covers everything the fork does except a six… Decision needed.
  - conflicts with gke-reliability-fork [conf-2df4b9]: Option 1: keep gke-reliability (A), retire gke-reliability-fork (B). The PDB rule matches the upgrade-disruption advice in gke-golden-path,… Decision needed.
  - missing dependency with gke-golden-path [dep-dfd880]: Import google/cloud/gke-upgrades with `python3 .sss/tool/sss.py import google/cloud/gke-upgrades`.
  - missing dependency [dep-a44fa6]: Import google/cloud/gke-manifest-generation with `python3 .sss/tool/sss.py import google/cloud/gke-manifest-generation`.
  - missing dependency [dep-d5464f]: Import google/cloud/gke-backup-dr with `python3 .sss/tool/sss.py import google/cloud/gke-backup-dr`.

### gke-reliability-fork

- **Source:** gke-fork  **Status:** ok  **Location:** `.agents/skills/gke-reliability-fork`
- **Goal:** A short checklist for PDBs, probes, zone spread and maintenance windows on GKE.
- **Concerns:**
  - duplicate with gke-reliability [dup-5e3bec]: Keep gke-reliability. It comes from the google source of truth, carries a version (1.0.1), and covers everything the fork does except a six… Decision needed.
  - conflicts with gke-reliability [conf-2df4b9]: Option 1: keep gke-reliability (A), retire gke-reliability-fork (B). The PDB rule matches the upgrade-disruption advice in gke-golden-path,… Decision needed.

## Appendix: coverage matrix

Every skill was compared with every other skill and scored by how much they cover the same ground.

Legend: 0 = same, 1 = subset, 2 = large overlap, 3 = some overlap, 4 = related, 5 = distinct, · = not scored yet.

| Skill | S1 | S2 | S3 | S4 | S5 | S6 | S7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **S1** gcloud | — | 4 | 4 | 4 | 4 | 4 | 4 |
| **S2** gke-cluster-creation | 4 | — | 2 | 4 | 4 | 4 | 4 |
| **S3** gke-golden-path | 4 | 2 | — | 3 | 4 | 3 | 4 |
| **S4** gke-observability | 4 | 4 | 3 | — | 1 | 4 | 4 |
| **S5** gke-observability-fork | 4 | 4 | 4 | 1 | — | 4 | 4 |
| **S6** gke-reliability | 4 | 4 | 3 | 4 | 4 | — | 1 |
| **S7** gke-reliability-fork | 4 | 4 | 4 | 4 | 4 | 1 | — |

Coverage summaries:

- **S1 gcloud**: Safety rules for any use of the gcloud CLI on Google Cloud: check leaf-level syntax with `gcloud help` before every command, always pass `--quiet` and `--project`, never run a `list` without `--limit`, `--filter` or `--format`, and never run delete, IAM, billing, org or KMS commands without a human saying yes. Two reference files cover install and authentication, and the remote Cloud CLI MCP server. It does not describe how to configure any particular product such as GKE.
- **S2 gke-cluster-creation**: Walks an agent through creating a GKE cluster: gather project, region and name, pick Autopilot or Standard, then use one of five ready-made templates (golden-path Autopilot, Autopilot dev/test, Standard regional, L4 GPU, A3 hypercompute) given both as a gcloud command and as an MCP `create_cluster` payload. A team patch sets the default region to us-central1 and project to kitchen-prod-1234. It lists security, cost and HA best practices in brief and does not cover app deployment, detailed monitoring, or workload reliability.
- **S3 gke-golden-path**: The reference list of golden-path Autopilot cluster settings (private nodes, Secret Manager, Dataplane V2, full monitoring suite, VPA, Stateful HA and so on), which settings a customer may change, guardrails, and a section on what to say about node upgrade disruption (PDBs, replicas, readiness probes, surge settings). A team patch makes clusters always regional and pins project kitchen-prod-1234. Used to design or audit a cluster against defaults; it does not walk through the create flow or cover workload autoscaling.
- **S4 gke-observability**: Full guide to GKE monitoring and logging: the golden-path monitoring component list, how to enable control-plane metrics with `--monitoring` and the CLI versus API spelling trap, Managed Prometheus, `kubectl top`, `gcloud logging read` queries, alert thresholds, cost notes, tracing and profiling, LQL examples, and a long Managed Prometheus troubleshooting section (pods, PodMonitoring, permissions, rules, Grafana, quota). It does not cover app logging libraries or non-Google APMs.
- **S5 gke-observability-fork**: A short nine-step checklist for GKE observability: check logging and monitoring config, enable Managed Prometheus, confirm workload logs reach Cloud Logging, suggest dashboards and alerts, recommend Cloud Trace and Cloud Profiler, two LQL examples, enable control-plane metrics, and enable Dataplane V2 observability. It has no troubleshooting, no cost guidance, and no table of golden-path defaults.
- **S6 gke-reliability**: GKE workload reliability with MCP-first and kubectl fallback commands: verify the cluster is regional, Pod Disruption Budgets, liveness, readiness and startup probes with recommended timings, graceful shutdown with a preStop hook, zone and node topology spread, minimum replica counts by workload type, and a table of golden-path reliability defaults. It hands manifest generation, backup and DR, and maintenance windows to other skills.
- **S7 gke-reliability-fork**: A short checklist for GKE reliability: verify the cluster is regional, a PDB example, which probes to have and how to check for them, a one-line note on graceful shutdown, a zone topology spread example, and a gcloud command to set a maintenance window. No MCP commands, no probe timings, no replica guidance.

Pairs at 2 stars or fewer:

- 1 star: gke-observability and gke-observability-fork. Every one of the fork's nine steps (audit config, Managed Prometheus, workload logs, dashboards, tracing, profiling, LQL, control-plane metrics, Dataplane V2) appears in gke-observability with more detail, which also adds cost, alert thresholds and GMP troubleshooting; the fork's only extra is a one-line tip to log as JSON.
- 1 star: gke-reliability and gke-reliability-fork. Five of the fork's six workflows (regional check, PDB, probes, graceful shutdown, topology spread) appear in gke-reliability with more detail plus MCP commands and replica guidance; the fork's only extra is a six-line maintenance-window command, which gke-reliability hands to the gke-upgrades skill.
- 2 stars: gke-cluster-creation and gke-golden-path. Both define the golden-path Autopilot defaults, the same required inputs, the same Day-0 warnings and the same team project id; cluster-creation adds templates and golden-path adds the full settings table and upgrade disruption advice.
