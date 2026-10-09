# Skills reorganize report: github.com/gke-labs/kube-agents

Generated 2026-10-09T14:51:41Z by SSS. This is a local working document in
`.sss/reports/`; it is not committed. Sections 3 to 7 answer one question each.

## 1. Summary

We found 81 skills, all written in this repository (none is managed by SSS yet), and compared every pair: 3,240 pairs scored, 12 at 2 stars or fewer (7 where one copy is a subset of the other, 5 with large overlap), 101 at 3 stars, and the rest related or distinct. Most problems sit in the six skills that exist twice, once for the Platform Agent and once as a trimmed Cluster Agent copy: the cluster copies have drifted, carry commands the read-only Cluster Agent may not run, and in several places name flags gcloud does not have. The upstream-synced gke-* skills carry a handful of wrong flags and dangling file pointers that need a substitution entry in the sync script rather than a hand edit. No skill is missing a dependency; every link the inventory flagged resolves from the repository root, points into a user's GitOps repository or the agent pod, or is a placeholder. A sceptical second pass re-read every finding against its quoted evidence (Changed: 7, Deleted: 0, Unchanged: 52). This run was report-only: nothing was applied and no pull request was opened.

| Question | Answer |
| --- | --- |
| Are any skills out of date? | Yes, 22 |
| Are any skills duplicated? | Yes, 7 |
| Do any skills give conflicting information? | Yes, 21 |
| Are any skills missing pieces they refer to? | No |
| Are any skills unuseful or out of place? | Yes, 9 |
| Actions we can take without asking | 6 |
| Decisions needed from you | 38 |

## 2. What we looked at

| Skill | Source | Status | Location | Files | Words | Last changed |
| --- | --- | --- | --- | --- | --- | --- |
| install-kube-agents | local | unmanaged | `.agents/skills/install-kube-agents` | 1 | 4724 | 2026-10-08 |
| review-address-feedback | local | unmanaged | `.agents/skills/review-address-feedback` | 1 | 689 | 2026-10-06 |
| review-adversarial | local | unmanaged | `.agents/skills/review-adversarial` | 1 | 4694 | 2026-09-30 |
| review-docs-drift | local | unmanaged | `.agents/skills/review-docs-drift` | 1 | 1590 | 2026-10-07 |
| review-preflight | local | unmanaged | `.agents/skills/review-preflight` | 1 | 2102 | 2026-09-16 |
| review-security-k8s-admission | local | unmanaged | `.agents/skills/review-security-k8s-admission` | 1 | 255 | 2026-05-22 |
| review-security-k8s-agents-audit-logs | local | unmanaged | `.agents/skills/review-security-k8s-agents-audit-logs` | 1 | 154 | 2026-05-21 |
| review-security-k8s-agents-credentials | local | unmanaged | `.agents/skills/review-security-k8s-agents-credentials` | 1 | 130 | 2026-05-21 |
| review-security-k8s-agents-data-exfil | local | unmanaged | `.agents/skills/review-security-k8s-agents-data-exfil` | 1 | 111 | 2026-05-21 |
| review-security-k8s-agents-firewall | local | unmanaged | `.agents/skills/review-security-k8s-agents-firewall` | 1 | 141 | 2026-09-03 |
| review-security-k8s-agents-main | local | unmanaged | `.agents/skills/review-security-k8s-agents-main` | 1 | 219 | 2026-05-22 |
| review-security-k8s-agents-prompt-injection | local | unmanaged | `.agents/skills/review-security-k8s-agents-prompt-injection` | 1 | 75 | 2026-05-21 |
| review-security-k8s-agents-sandbox | local | unmanaged | `.agents/skills/review-security-k8s-agents-sandbox` | 1 | 129 | 2026-05-21 |
| review-security-k8s-gateway | local | unmanaged | `.agents/skills/review-security-k8s-gateway` | 1 | 97 | 2026-05-21 |
| review-security-k8s-main | local | unmanaged | `.agents/skills/review-security-k8s-main` | 1 | 195 | 2026-05-22 |
| review-security-k8s-namespaces | local | unmanaged | `.agents/skills/review-security-k8s-namespaces` | 1 | 163 | 2026-05-21 |
| review-security-k8s-network | local | unmanaged | `.agents/skills/review-security-k8s-network` | 1 | 177 | 2026-05-21 |
| review-security-k8s-nodes | local | unmanaged | `.agents/skills/review-security-k8s-nodes` | 1 | 155 | 2026-05-21 |
| review-security-k8s-pod | local | unmanaged | `.agents/skills/review-security-k8s-pod` | 1 | 210 | 2026-06-16 |
| review-security-k8s-rbac | local | unmanaged | `.agents/skills/review-security-k8s-rbac` | 2 | 3739 | 2026-05-21 |
| review-security-k8s-service-accounts | local | unmanaged | `.agents/skills/review-security-k8s-service-accounts` | 1 | 138 | 2026-05-21 |
| review-security-k8s-storage | local | unmanaged | `.agents/skills/review-security-k8s-storage` | 1 | 181 | 2026-05-21 |
| review-security-k8s-understand | local | unmanaged | `.agents/skills/review-security-k8s-understand` | 1 | 105 | 2026-05-21 |
| skill-review | local | unmanaged | `.agents/skills/skill-review` | 1 | 260 | 2026-09-24 |
| uninstall-kube-agents | local | unmanaged | `.agents/skills/uninstall-kube-agents` | 1 | 489 | 2026-10-05 |
| upgrade-kube-agents | local | unmanaged | `.agents/skills/upgrade-kube-agents` | 1 | 1101 | 2026-09-30 |
| a2a-topics | local | unmanaged | `a2a/persona/platform/skills/a2a-topics` | 1 | 1013 | 2026-09-18 |
| gke-stockout-investigator | local | unmanaged | `agentplugins/gke-stockout-investigator/files/skills/gke-stockout-investigator` | 1 | 3703 | 2026-10-03 |
| gke-observability (agents/cluster/skills/gke-observability) | local | unmanaged | `agents/cluster/skills/gke-observability` | 1 | 484 | 2026-07-28 |
| gke-reliability (agents/cluster/skills/gke-reliability) | local | unmanaged | `agents/cluster/skills/gke-reliability` | 1 | 383 | 2026-07-28 |
| gke-stall-detection | local | unmanaged | `agents/cluster/skills/gke-stall-detection` | 1 | 1330 | 2026-10-05 |
| gke-storage (agents/cluster/skills/gke-storage) | local | unmanaged | `agents/cluster/skills/gke-storage` | 1 | 324 | 2026-07-28 |
| gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) | local | unmanaged | `agents/cluster/skills/gke-workload-scaling` | 3 | 540 | 2026-07-28 |
| gke-workload-security (agents/cluster/skills/gke-workload-security) | local | unmanaged | `agents/cluster/skills/gke-workload-security` | 4 | 829 | 2026-09-08 |
| gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) | local | unmanaged | `agents/cluster/skills/gke-workload-troubleshooting` | 1 | 1284 | 2026-09-09 |
| capacity-obtainability | local | unmanaged | `agents/platform/skills/capacity-obtainability` | 1 | 3385 | 2026-09-26 |
| cluster-agent-lifecycle | local | unmanaged | `agents/platform/skills/cluster-agent-lifecycle` | 1 | 1750 | 2026-10-08 |
| fleet-audit | local | unmanaged | `agents/platform/skills/fleet-audit` | 21 | 15626 | 2026-10-08 |
| fleet-audit-reports | local | unmanaged | `agents/platform/skills/fleet-audit-reports` | 3 | 1800 | 2026-10-08 |
| fleet-upgrade-verification | local | unmanaged | `agents/platform/skills/fleet-upgrade-verification` | 8 | 3239 | 2026-10-08 |
| gce-compute-fleet-audit | local | unmanaged | `agents/platform/skills/gce-compute-fleet-audit` | 3 | 265 | 2026-10-08 |
| gcp-config-connector | local | unmanaged | `agents/platform/skills/gcp-config-connector` | 5 | 4869 | 2026-10-01 |
| gcp-networking-fabric-audit | local | unmanaged | `agents/platform/skills/gcp-networking-fabric-audit` | 3 | 199 | 2026-10-07 |
| github-issue-resolver | local | unmanaged | `agents/platform/skills/github-issue-resolver` | 3 | 2065 | 2026-10-08 |
| gke-ai-troubleshooting-handle-disruption-gpu-tpu | local | unmanaged | `agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu` | 1 | 711 | 2026-08-07 |
| gke-ai-troubleshooting-jobset-interruption | local | unmanaged | `agents/platform/skills/gke-ai-troubleshooting-jobset-interruption` | 3 | 1532 | 2026-08-07 |
| gke-ai-troubleshooting-tpu-vbar-oom | local | unmanaged | `agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom` | 3 | 929 | 2026-08-07 |
| gke-app-onboarding | local | unmanaged | `agents/platform/skills/gke-app-onboarding` | 5 | 541 | 2026-08-20 |
| gke-backup-dr | local | unmanaged | `agents/platform/skills/gke-backup-dr` | 1 | 899 | 2026-10-08 |
| gke-basics | local | unmanaged | `agents/platform/skills/gke-basics` | 6 | 3582 | 2026-09-24 |
| gke-batch-hpc | local | unmanaged | `agents/platform/skills/gke-batch-hpc` | 1 | 744 | 2026-09-26 |
| gke-cluster-autoscaler | local | unmanaged | `agents/platform/skills/gke-cluster-autoscaler` | 9 | 2639 | 2026-09-09 |
| gke-cluster-creation | local | unmanaged | `agents/platform/skills/gke-cluster-creation` | 1 | 1645 | 2026-09-23 |
| gke-compute-classes | local | unmanaged | `agents/platform/skills/gke-compute-classes` | 27 | 7434 | 2026-08-07 |
| gke-cost-analysis | local | unmanaged | `agents/platform/skills/gke-cost-analysis` | 1 | 1039 | 2026-08-07 |
| gke-cost-optimization | local | unmanaged | `agents/platform/skills/gke-cost-optimization` | 1 | 1200 | 2026-08-07 |
| gke-golden-path | local | unmanaged | `agents/platform/skills/gke-golden-path` | 2 | 594 | 2026-08-07 |
| gke-inference | local | unmanaged | `agents/platform/skills/gke-inference` | 1 | 917 | 2026-08-07 |
| gke-manifest-generation | local | unmanaged | `agents/platform/skills/gke-manifest-generation` | 5 | 2218 | 2026-09-24 |
| gke-multitenancy | local | unmanaged | `agents/platform/skills/gke-multitenancy` | 1 | 626 | 2026-08-07 |
| gke-networking | local | unmanaged | `agents/platform/skills/gke-networking` | 1 | 870 | 2026-08-17 |
| gke-observability (agents/platform/skills/gke-observability) | local | unmanaged | `agents/platform/skills/gke-observability` | 1 | 993 | 2026-08-07 |
| gke-platform-security | local | unmanaged | `agents/platform/skills/gke-platform-security` | 1 | 973 | 2026-08-07 |
| gke-productionize | local | unmanaged | `agents/platform/skills/gke-productionize` | 1 | 714 | 2026-08-07 |
| gke-reliability (agents/platform/skills/gke-reliability) | local | unmanaged | `agents/platform/skills/gke-reliability` | 1 | 767 | 2026-08-07 |
| gke-service-networking | local | unmanaged | `agents/platform/skills/gke-service-networking` | 1 | 686 | 2026-08-07 |
| gke-storage (agents/platform/skills/gke-storage) | local | unmanaged | `agents/platform/skills/gke-storage` | 1 | 581 | 2026-08-07 |
| gke-tpu-dynamic-slices-monitoring | local | unmanaged | `agents/platform/skills/gke-tpu-dynamic-slices-monitoring` | 3 | 1287 | 2026-08-07 |
| gke-tpu-metrics-monitoring | local | unmanaged | `agents/platform/skills/gke-tpu-metrics-monitoring` | 3 | 855 | 2026-08-07 |
| gke-upgrades | local | unmanaged | `agents/platform/skills/gke-upgrades` | 4 | 4756 | 2026-09-15 |
| gke-workload-scaling (agents/platform/skills/gke-workload-scaling) | local | unmanaged | `agents/platform/skills/gke-workload-scaling` | 3 | 755 | 2026-09-26 |
| gke-workload-security (agents/platform/skills/gke-workload-security) | local | unmanaged | `agents/platform/skills/gke-workload-security` | 4 | 974 | 2026-09-08 |
| gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) | local | unmanaged | `agents/platform/skills/gke-workload-troubleshooting` | 1 | 1306 | 2026-10-02 |
| inspect-repository | local | unmanaged | `agents/platform/skills/inspect-repository` | 3 | 838 | 2026-10-08 |
| kube-agents-observability | local | unmanaged | `agents/platform/skills/kube-agents-observability` | 6 | 1328 | 2026-10-06 |
| manage-cluster | local | unmanaged | `agents/platform/skills/manage-cluster` | 1 | 503 | 2026-09-23 |
| pr-conversation | local | unmanaged | `agents/platform/skills/pr-conversation` | 3 | 2305 | 2026-10-08 |
| submit-suggestion | local | unmanaged | `agents/platform/skills/submit-suggestion` | 2 | 3209 | 2026-10-08 |
| version-control | local | unmanaged | `agents/platform/skills/version-control` | 3 | 3084 | 2026-10-07 |
| workload-rebalancing | local | unmanaged | `agents/platform/skills/workload-rebalancing` | 1 | 535 | 2026-09-25 |
| gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) | local | unmanaged | `third_party/google-skills/gke-workload-troubleshooting` | 1 | 1242 | 2026-10-09 |

## 3. Out of date

These skills are behind their source, or describe things that have since changed.

### old-53530a: install-kube-agents

install.sh now also takes --gitops-forge=gitlab with --gitops-host, --gitlab-token-file and --gitlab-token-secret (install.sh --help, lines 644-652), so an agent following this skill tells a GitLab user that GitOps needs a GitHub organization and a GitHub App, and never offers the GitLab path.

Evidence:
- `install-kube-agents/SKILL.md:100`: "   gives its access path. GitOps pull requests add `--gitops-org`, `--gitops-repo` and"
- `install-kube-agents/SKILL.md:354`: "When deploying `kube-agents` with GitOps pull-request workflows enabled, the Platform Agent creates pull requests against an infrastructure-as-code repository via the [GitHub Token Minter](https://github.com/abcxyz/github-token-minter) (`minty`). The minter runs in-cluster and signs short-lived GitHub App installation tokens using a private key securely stored in Google Cloud KMS."

**Recommendation** (likely): Add the GitLab forge option to the interview step, the GitOps section and the flag table, stating that the GitHub App and minter apply only when --gitops-forge is github.

Decision needed: no

### old-10bf86: review-preflight

make docs-check no longer runs a map-coverage check (docs-check-map was removed from the Makefile; docs-check is now generated, links, terminology, audience and context-budget), so an agent expects a result the gate does not produce.

Evidence:
- `review-preflight/SKILL.md:80`: "on. It does not substitute for its pass — it covers generated regions, links, terminology, map"

**Recommendation** (confident): Replace "map coverage" with the reachability check that docs-check-links performs today.

Decision needed: no

### old-59686b: review-preflight

AGENTS.md's Local Validation Checks now also name make shellcheck on changed shell scripts, go build in a2a/, and make terraform-test on a changed Terraform module, so an agent that trusts this restatement skips three checks CI will fail.

Evidence:
- `review-preflight/SKILL.md:87`: "the Docker build, the image-layer budget, `go build` in `k8s-operator/` — and a clean preflight"

**Recommendation** (likely): Either point at the AGENTS.md list without enumerating it or add shellcheck, a2a/ and terraform-test to the enumeration.

Decision needed: no

### old-af4d83: review-security-k8s-agents-audit-logs

There is no `AuditPolicy` kind in Kubernetes (the audit policy object is `kind: Policy` in `audit.k8s.io/v1`), and on GKE the API server audit policy is managed by Google and not editable, so a reviewer looking for this resource in a GKE repo finds nothing and either skips the check or files a finding nobody can act on.

Evidence:
- `review-security-k8s-agents-audit-logs/SKILL.md:11`: "- **Audit Policy**: Ensure `AuditPolicy` captures all agent API requests (minimum `Metadata` level, prefer `RequestResponse` for mutations)."

**Recommendation** (likely): Reword the check to name what a GKE user can control: Cloud Audit Logs with Data Access logging enabled for the Kubernetes Engine API, falling back to an `audit.k8s.io/v1 Policy` only for self-managed control planes.

Decision needed: no

### old-9ac7ee: review-security-k8s-pod

Kubernetes manifests spell capabilities without the CAP_ prefix (SYS_ADMIN, NET_ADMIN, NET_RAW), so a reviewer that searches for the CAP_ names will miss every real occurrence.

Evidence:
- `review-security-k8s-pod/SKILL.md:22`: "- **Linux Capabilities**: Require `capabilities.drop: ["ALL"]`. Flag highly privileged additions (e.g., `CAP_SYS_ADMIN`, `CAP_NET_ADMIN`, `CAP_NET_RAW`, `CAP_SYS_MODULE`, `CAP_SYS_PTRACE`, `CAP_DAC_OVERRIDE`)."

**Recommendation** (confident): Rewrite the examples in the form manifests use: SYS_ADMIN, NET_ADMIN, NET_RAW, SYS_MODULE, SYS_PTRACE, DAC_OVERRIDE.

Decision needed: yes

### old-cd8c4b: gke-stockout-investigator

The path is this repository's own skill-asset layout (the examples under agents/platform/skills/gke-compute-classes/assets/), not a layout a user's GitOps repository has, so the agent looks in a directory that does not exist before falling back to search.

Evidence:
- `gke-stockout-investigator/SKILL.md:137`: "   - For ComputeClass definitions, check `<workspace>/agents/platform/skills/gke-compute-classes/assets/` directly or use `search_files(pattern="compute-class")`."

**Recommendation** (likely): Drop the hard-coded `agents/platform/skills/gke-compute-classes/assets/` hint and keep only the `search_files(pattern="compute-class")` instruction.

Decision needed: yes

### old-7a047d: gke-observability (agents/cluster/skills/gke-observability)

`gcloud container clusters update` has no `--enable-dataplane-v2-observability` flag (gcloud 587 offers `--enable-dataplane-v2-flow-observability` and `--enable-dataplane-v2-metrics`; the older `--dataplane-v2-observability-mode` is marked removed), so the command fails as written.

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:117`: "    --enable-dataplane-v2-observability \"

**Recommendation** (confident): Replace the flag with `--enable-dataplane-v2-flow-observability` (and mention `--enable-dataplane-v2-metrics`), as the Platform Agent copy of this skill already does.

Decision needed: no

### old-831dba: gke-observability (agents/cluster/skills/gke-observability)

The command projects only `loggingConfig`/`monitoringConfig`, whose contents are `componentConfig.enableComponents` lists, while the text tells the agent to look for the legacy top-level `loggingService`/`monitoringService` fields, which that output never contains.

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:19`: "gcloud container clusters describe <cluster-name> --region <region> --project <project-id> --format="json(loggingConfig, monitoringConfig)""
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:22`: "Look for `loggingService` and `monitoringService` to be set to something other than `none` (usually `logging.googleapis.com/kubernetes` and `monitoring.googleapis.com/kubernetes`)."

**Recommendation** (confident): Either add `loggingService, monitoringService` to the `--format` projection or tell the agent to read `componentConfig.enableComponents` (empty means disabled) from the fields the command returns.

Decision needed: no

### old-a41048: gke-reliability (agents/cluster/skills/gke-reliability)

gcloud (587) requires `--maintenance-window-end` or `--maintenance-window-duration` alongside `--maintenance-window-start` and `--maintenance-window-recurrence`, so the command as written is rejected.

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:93`: "    --maintenance-window-start <start-time> \"
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:94`: "    --maintenance-window-recurrence "FREQ=DAILY""

**Recommendation** (likely): If the command stays anywhere, add `--maintenance-window-end <end-time>` (or `--maintenance-window-duration`) to it.

Decision needed: no

### old-2cdfcd: gke-storage (agents/cluster/skills/gke-storage)

The GKE Filestore CSI driver installs StorageClasses named standard-rwx, premium-rwx, enterprise-rwx and zonal-rwx (the platform copy of this skill uses standard-rwx), so a PVC copied from this example stays Pending with a missing StorageClass.

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:55`: "  storageClassName: standard-rwm # Pre-defined for Filestore"

**Recommendation** (confident): Change the example's storageClassName to standard-rwx.

Decision needed: no

### old-5fefe4: gke-workload-security (agents/cluster/skills/gke-workload-security)

gcloud container clusters update has no --enable-gke-sandbox flag (checked against Google Cloud SDK 587.0.0); GKE Sandbox is enabled per node pool with gcloud container node-pools create --sandbox type=gvisor, so the command as written fails.

Evidence:
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:144`: "gcloud container clusters update <cluster-name> \"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:145`: "    --enable-gke-sandbox \"

**Recommendation** (confident): Replace the cluster update command with the node-pool form, gcloud container node-pools create <pool> --cluster <cluster-name> --sandbox type=gvisor --region <region>.

Decision needed: yes

### old-986a59: gke-basics

gcloud 587 (GA, beta and alpha) has no --scoped-rbs-bindings flag, so the golden-path create-auto command fails with an unrecognized-argument error; the real flags are --no-enable-insecure-binding-system-authenticated and --no-enable-insecure-binding-system-unauthenticated, matching the rbacBindingConfig the golden-path asset uses.

Evidence:
- `gke-basics/references/cli-reference.md:92`: "  --enable-secret-manager --scoped-rbs-bindings \"

**Recommendation** (confident): Replace --scoped-rbs-bindings with the two --no-enable-insecure-binding-system-* flags. The flag absence is verified (gcloud 587 GA/beta/alpha `clusters create-auto --help` list only the --enable-insecure-binding-system-* pair), but the stale line is in references/cli-reference.md, not SKILL.md. Note: scripts/sync-upstream-skills.py applies SKILL_SUBSTITUTIONS to SKILL.md only (apply_substitutions opens SKILL_MD_FILENAME), so a substitution cannot reach this file; the fix has to land upstream in google/skills, or the sync script has to be extended to substitute inside references/ and assets/ first.

Decision needed: yes

### old-1a9274: gke-cluster-autoscaler

The skill has no resources/ folder; the file lives at references/ca-capacity-buffers.md, so an agent following the pointer finds nothing.

Evidence:
- `gke-cluster-autoscaler/assets/capacity-buffer-serving.yaml:5`: "# no gcloud surface). See resources/ca-capacity-buffers.md → Capacity Buffers."

**Recommendation** (confident): Change the pointer in assets/capacity-buffer-serving.yaml to references/ca-capacity-buffers.md (verified: the skill has references/ with ca-capacity-buffers.md and no resources/ folder). Note: scripts/sync-upstream-skills.py applies SKILL_SUBSTITUTIONS to SKILL.md only (apply_substitutions opens SKILL_MD_FILENAME), so a substitution cannot reach this file; the fix has to land upstream in google/skills, or the sync script has to be extended to substitute inside references/ and assets/ first.

Decision needed: yes

### old-09ef08: gke-cluster-creation

gcloud 587 (GA, beta and alpha) has no --scoped-rbs-bindings flag, so both golden-path gcloud templates fail with an unrecognized-argument error while the MCP payload beside them correctly uses rbacBindingConfig; the gcloud equivalents are --no-enable-insecure-binding-system-authenticated and --no-enable-insecure-binding-system-unauthenticated.

Evidence:
- `gke-cluster-creation/SKILL.md:81`: "    limits (`scoped-rbs-bindings`)."
- `gke-cluster-creation/SKILL.md:122`: "  --scoped-rbs-bindings \"
- `gke-cluster-creation/SKILL.md:251`: "  --enable-dns-access --enable-secret-manager --scoped-rbs-bindings \"

**Recommendation** (confident): Replace --scoped-rbs-bindings in both templates and the best-practice line with the two --no-enable-insecure-binding-system-* flags through a SKILL_SUBSTITUTIONS entry in scripts/sync-upstream-skills.py.

Decision needed: yes

### old-b36ef3: gke-compute-classes

Neither file exists in this skill or the repo; the binding steps now live in references/compute-class-provisioning-methods.md and the system-pod pattern in ../gke-cluster-autoscaler/references/ca-debug.md, so an agent following the comments finds nothing.

Evidence:
- `gke-compute-classes/assets/manual-pool-tiebreak-compute-class.yaml:12`: "  # See gke-compute-classes-create.md → "Binding a manual node pool to a ComputeClass"."
- `gke-compute-classes/assets/system-pool-compute-class.yaml:27`: "# See gke-cluster-autoscaling-debug.md → "System pods blocking consolidation"."

**Recommendation** (confident): Point the two asset comments at references/compute-class-provisioning-methods.md and ../gke-cluster-autoscaler/references/ca-debug.md (verified: neither gke-compute-classes-create.md nor gke-cluster-autoscaling-debug.md exists anywhere in the repo; both replacement files do). Note: scripts/sync-upstream-skills.py applies SKILL_SUBSTITUTIONS to SKILL.md only (apply_substitutions opens SKILL_MD_FILENAME), so a substitution cannot reach this file; the fix has to land upstream in google/skills, or the sync script has to be extended to substitute inside references/ and assets/ first.

Decision needed: yes

### old-3bbdcd: gke-golden-path

The skill folder has no `resources/` directory and no `recommended-ap.yaml` exists anywhere in the repo, so an agent sent there for the full `gcloud container clusters describe` export finds nothing.

Evidence:
- `gke-golden-path/assets/golden-path-autopilot.yaml:3`: "# Full export: resources/recommended-ap.yaml"
- `gke-golden-path/assets/golden-path-autopilot.yaml:147`: "# See resources/recommended-ap.yaml for the full describe output."

**Recommendation** (confident): Remove the two pointer comments (or ship the export they name) in upstream google/skills, since `scripts/sync-upstream-skills.py` only rewrites SKILL.md and would overwrite a local edit to the asset.

Decision needed: yes

### old-146246: gke-productionize

No skill named gke-scaling exists under agents/platform/skills; the scaling skill is gke-workload-scaling (which the body at line 77 names correctly), so an agent routing on the description looks for a skill that is not there.

Evidence:
- `gke-productionize/SKILL.md:5`: "description: Orchestrates comprehensive production readiness reviews and assessments for GKE clusters and workloads across scalability, security, reliability, observability, backup/DR, and cost optimization. Use when asked to productionize, prepare, assess, audit, or review a GKE cluster or workload before going live to production. Don't use for deep-dive single-domain implementation (use specific domain skills like gke-scaling, gke-platform-security, gke-workload-security, gke-service-networking, gke-reliability instead)."

**Recommendation** (likely): Rename gke-scaling to gke-workload-scaling in the description through a SKILL_SUBSTITUTIONS entry in scripts/sync-upstream-skills.py, since the skill file is overwritten on every sync.

Decision needed: yes

### old-3574a6: gke-service-networking

The GKE Gateway annotation for a Certificate Manager map is `networking.gke.io/certmap` (no hyphen), so a Gateway applied with the hyphenated key is silently ignored by the controller and the HTTPS listener gets no certificate.

Evidence:
- `gke-service-networking/SKILL.md:144`: "using `networking.gke.io/cert-map: {certificate_map_name}`, or reference a"
- `gke-service-networking/SKILL.md:154`: "    networking.gke.io/cert-map: {certificate_map_name} # For Certificate Manager maps"

**Recommendation** (likely): Change both occurrences to `networking.gke.io/certmap` through a SKILL_SUBSTITUTIONS entry in scripts/sync-upstream-skills.py.

Decision needed: yes

### old-dbccdf: gke-service-networking

Gateway API is enabled by default only on Autopilot clusters (1.26+); Standard clusters need `gcloud container clusters update <CLUSTER> --gateway-api=standard`, so an agent that trusts this line applies a Gateway on a Standard cluster and gets an unknown-kind error.

Evidence:
- `gke-service-networking/SKILL.md:25`: "**Prerequisites**: Gateway API must be enabled on the cluster (enabled by"
- `gke-service-networking/SKILL.md:26`: "default in GKE 1.24+)."

**Recommendation** (likely): State that Standard clusters require `--gateway-api=standard` and Autopilot enables it by default from 1.26, through a SKILL_SUBSTITUTIONS entry in scripts/sync-upstream-skills.py.

Decision needed: yes

### old-d758bd: gke-tpu-dynamic-slices-monitoring

The script claims to validate queries that SKILL.md no longer contains, so an agent that runs it gets a no-op and a misleading success message.

Evidence:
- `gke-tpu-dynamic-slices-monitoring/scripts/validate_queries.sh:2`: "# Validate Cloud Logging LQL queries used in SKILL.md"
- `gke-tpu-dynamic-slices-monitoring/scripts/validate_queries.sh:16`: "echo "No Cloud Logging LQL queries defined in this skill to validate.""

**Recommendation** (likely): Drop scripts/validate_queries.sh from the skill in upstream google/skills, since scripts/sync-upstream-skills.py overwrites a local removal on the next sync.

Decision needed: yes

### old-8dbbf7: gke-tpu-metrics-monitoring

The script requires PROJECT_ID, then validates nothing; the PromQL queries the skill actually uses are never checked, so an agent gets a false sense of validation.

Evidence:
- `gke-tpu-metrics-monitoring/scripts/validate_queries.sh:2`: "# Validate Cloud Logging LQL queries used in SKILL.md"
- `gke-tpu-metrics-monitoring/scripts/validate_queries.sh:13`: "echo "No Cloud Logging LQL queries defined in this skill to validate.""

**Recommendation** (likely): Drop scripts/validate_queries.sh from the skill in upstream google/skills, since scripts/sync-upstream-skills.py overwrites a local removal on the next sync.

Decision needed: yes

### old-659b7e: kube-agents-observability

The operator sets no prometheus.io annotations; the chart scrapes the gateway pod with a PodMonitoring selected by the `app: <name>-gateway` label on port 9095 (charts/kube-agents/templates/platform-agent-monitoring.yaml), so an agent looking for annotations will report a fault that is not one.

Evidence:
- `kube-agents-observability/SKILL.md:77`: "- Verify the agent deployment has correct annotations for Prometheus scraping:"

**Recommendation** (likely): Replace the annotation check with `kubectl get podmonitoring -n kubeagents-system` and a check that its selector matches the gateway pod label.

Decision needed: yes

## 4. Duplicates

These skills cover the same ground: 0 or 1 star in the coverage matrix (see the
appendix). Keeping both wastes the agent's attention and lets them drift apart.

### dup-5b7877: cluster-agent-lifecycle, manage-cluster

Two Platform Agent skills tell the model to run the same `cluster_agent_profile.py create` command, describe the same hourly `cluster-agent-reconcile` cron and the same `spec.scope.exclude.clusters` opt-out, so every change to the profile lifecycle (the RECONCILE_EXCLUDE retirement, the sandbox stub, a new flag) has to be made twice and the two copies will drift apart, as the multi-project-scope design doc already had to patch both at once.

Evidence:
- `cluster-agent-lifecycle/SKILL.md:16`: "Create the Cluster Agent profile as part of **cluster onboarding** — immediately after a cluster is successfully provisioned (see `gke-cluster-creation`) or when an existing cluster is first brought under management (see `manage-cluster`). A managed cluster and its Cluster Agent profile are created together: when you onboard or tear down a cluster, keep the profile in step with it. That rule is scoped to onboarding and teardown, where the profile is yours to manage. It is not a roster invariant to enforce from other work — the reconcile job below owns the roster, and an empty roster is a supported state, not damage to repair. In particular, the first-run discovery sweep must never create or repair profiles."
- `cluster-agent-lifecycle/SKILL.md:19`: "python3 /opt/data/scripts/cluster_agent_profile.py create \"
- `cluster-agent-lifecycle/SKILL.md:23`: "This scaffolds the profile home on the persistent data PVC, pins a kubeconfig scoped to that cluster, writes the cluster identity into the profile's `USER.md`, and registers the profile. It is **idempotent** — safe to re-run. It prints the profile name."
- `cluster-agent-lifecycle/SKILL.md:72`: "The roster is also reconciled automatically. An hourly, deterministic `no_agent` cron job"
- `cluster-agent-lifecycle/SKILL.md:79`: "  `spec.scope.exclude.clusters` or, for one more release, bare names in `RECONCILE_EXCLUDE`. A"
- `cluster-agent-lifecycle/SKILL.md:125`: "You still delete a profile explicitly during planned teardown (above) — reconciliation is the safety"
- `manage-cluster/SKILL.md:3`: "description: Bring an existing GKE cluster under management on user request (e.g. "manage my cluster <name> in <location>") by creating its Cluster Agent profile. Use whenever a user asks to manage/onboard/watch a specific existing cluster."
- `manage-cluster/SKILL.md:8`: "When a user asks you to **manage** (onboard / start watching) a specific existing GKE cluster — e.g. _"manage my cluster `payments-prod` in `us-central1`"_ — bring it under management by creating its **Cluster Agent profile**. After this, the cluster gets a per-cluster agent and is delegable via the kanban board."
- `manage-cluster/SKILL.md:26`: "   python3 /opt/data/scripts/cluster_agent_profile.py create \"
- `manage-cluster/SKILL.md:30`: "   This scaffolds the Cluster Agent profile home on the data PVC, pins a read-only `KUBECONFIG` to that cluster, stamps its `cluster_identity` into the profile config, and prints the profile name. It is idempotent — re-managing an already-managed cluster is a safe no-op."
- `manage-cluster/SKILL.md:34`: "> This step gives the cluster an agent **immediately**. Even without it, the `cluster-agent-reconcile` cron automatically gives every cluster in every project in scope — including the management cluster where kube-agents runs — an agent on its next run; this skill just does it now."
- `manage-cluster/SKILL.md:41`: "- Or **exclude it**: add the cluster's project, location and name to `spec.scope.exclude.clusters` on the `PlatformAgent` (the operator delivers it to the reconcile, which prunes the profile on its next run). The older `RECONCILE_EXCLUDE` bare-name variable on the `cluster-agent-reconcile` cron still works for one release."

**Recommendation** (confident): Keep `cluster-agent-lifecycle`: it is the superset, it is the newer file (last touched 2026-10-08 against 2026-09-23 for `manage-cluster`), it already cites `manage-cluster` as one of its two create triggers, and the repo's own wiring points at it as the mechanics owner (`scripts/sync-upstream-skills.py` appends links to it onto every synced `gke-*` lifecycle skill, `tests/test_persona_proposal_posture.py` pins a line in it). Neither copy is upstream-synced, both are hand-written and both ship into `/opt/platform-template/skills/` via `deploy/docker/Dockerfile:1915`, so nothing in the build forces a second file; fold `manage-cluster`'s four unique steps (project resolution, the `verify_gke_cluster` existence check, the user confirmation, the `Stop managing` paragraph) into a short `Manage an existing cluster on request` section of the keeper and remove the folder.

Decision needed: yes

### dup-a860b1: gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability)

Two hand-maintained copies of the same how-to drift apart (one already carries a flag that gcloud rejects), and whichever agent loads the stale one gives wrong instructions.

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:19`: "gcloud container clusters describe <cluster-name> --region <region> --project <project-id> --format="json(loggingConfig, monitoringConfig)""
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:134`: "gcloud container clusters describe <CLUSTER_NAME> --region <REGION> \"
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:32`: "    --enable-managed-prometheus \"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:58`: "  --enable-managed-prometheus \"
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:105`: "    --monitoring=SYSTEM,API_SERVER,SCHEDULER,CONTROLLER_MANAGER \"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:53`: "  --monitoring=SYSTEM,API_SERVER,SCHEDULER,CONTROLLER_MANAGER,STORAGE,POD,DEPLOYMENT,STATEFULSET,DAEMONSET,HPA,CADVISOR,KUBELET,DCGM \"
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:87`: "  resource.type="k8s_container""
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:207`: "resource.type="k8s_container" AND resource.labels.container_name="my-app" AND severity>=ERROR"
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:69`: "- **Action**: Recommend using **OpenTelemetry** in the application to send traces to **Cloud Trace**."
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:194`: "-   **Cloud Trace**: Add OpenTelemetry SDK to your app with the"

**Recommendation** (confident): Keep the Platform copy: it is the google/skills upstream copy that scripts/sync-upstream-skills.py overwrites on every sync (DEFAULT_TARGET_AGENTS is ["platform"], no overlay lock, no substitutions), it is newer (last synced 2026-08-07 vs the Cluster copy's single 2026-07-28 commit), it is the one gke-productionize and gke-app-onboarding point at, and it is a superset. The Cluster copy cannot simply be deleted because the Cluster Agent profile only ships agents/cluster/skills (Dockerfile copies agents/cluster/ to /opt/cluster-template, and agents/cluster/SOUL.md tells the agent to load the skill matching an observability gap), so shrink it to a read-only, single-cluster diagnostic subset that points at the Platform skill for anything that changes cluster configuration.

Decision needed: yes

### dup-90a10f: gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability)

The Cluster Agent copy is the pre-sync hand-written platform skill, git-moved unchanged in July 2026, so every upstream improvement that lands on the platform copy (explicit probe timeouts, preStop hook, hostname spread, replica minimums) is missing from the copy the Cluster Agent actually loads, and the two personas give a different answer to the same reliability question.

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:12`: "### 1. Verify Cluster High Availability"
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:19`: "gcloud container clusters describe <cluster-name> --region <region> --format="json(location, locations)""
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:60`: "kubectl get deployment <app-name> -n <namespace> -o yaml | grep -E "livenessProbe|readinessProbe|startupProbe""
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:39`: "### 1. Verify Cluster High Availability"
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:47`: "gcloud container clusters describe <CLUSTER> --region <REGION> \"
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:100`: "kubectl get deployment <APP> -n <NS> -o yaml | grep -E "livenessProbe|readinessProbe|startupProbe""

**Recommendation** (confident): Keep the platform copy: it is the upstream google/skills copy that scripts/sync-upstream-skills.py overwrites on every sync (no overlay lock, no SKILL_SUBSTITUTIONS entry) and it is the newer of the two (synced in #569 on 2026-08-07; the cluster copy is the old platform file moved in #441 on 2026-07-28 and untouched since). The cluster copy cannot simply be deleted because the Dockerfile ships agents/cluster/ to /opt/cluster-template and agents/platform/skills/ to /opt/platform-template separately, and agents/cluster/SOUL.md §3 tells the Cluster Agent to load a reliability skill, so shrink it instead to a read-only, persona-scoped checklist that points at the platform copy for the fix.

Decision needed: yes

### dup-e78aa6: gke-storage (agents/cluster/skills/gke-storage), gke-storage (agents/platform/skills/gke-storage)

Two hand-maintained copies of the same storage guidance drift apart (one already names a StorageClass that does not exist), so whichever agent loads the stale copy gives wrong answers while the other stays correct.

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:29`: "  type: pd-ssd"
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:30`: "  replication-type: regional-pd"
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:63`: "If `allowVolumeExpansion` is true in the StorageClass, you can resize a volume by updating the PVC manifest."
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:59`: "  type: pd-ssd"
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:60`: "  replication-type: regional-pd    # Replicate across 2 zones"
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:132`: "If `allowVolumeExpansion: true` is set on the StorageClass, resize by updating"

**Recommendation** (confident): Keep the platform copy: it is synced from google/skills by scripts/sync-upstream-skills.py (DEFAULT_TARGET_AGENTS = ["platform"]), is the newer of the two (2026-08-07 vs 2026-07-28), and is a strict superset. The cluster copy cannot simply be deleted because the Dockerfile ships agents/cluster/skills to /opt/cluster-template separately and the Cluster Agent never sees platform skills, but the Cluster Agent is read-only (CAPABILITIES.md: never mutates, routes to platform for provisioning), so its copy should shrink to read-only PVC/StorageClass diagnostics and point at the platform agent's gke-storage for provisioning.

Decision needed: yes

### dup-29508a: gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security)

Two copies of the same upstream google/skills text drift apart (the Platform copy has already been re-synced and rewritten while the Cluster copy kept the older body), so a fix to one copy, such as the NetworkPolicy two-step correction the sync script carries, has to be hand-applied to the other or the two agents follow different procedures for the same task.

Evidence:
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:52`: "   gcloud iam service-accounts add-iam-policy-binding <gsa-name>@<project-id>.iam.gserviceaccount.com \"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:70`: "    gcloud iam service-accounts add-iam-policy-binding <gsa-name>@<project-id>.iam.gserviceaccount.com \"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:107`: "    --update-addons=NetworkPolicy=ENABLED \"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:125`: "    --update-addons=NetworkPolicy=ENABLED \"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:159`: "kubectl label --overwrite ns <namespace> \"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:171`: "kubectl label --overwrite ns <namespace> \"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/scripts/audit_cluster.sh:17`: "CLUSTER_JSON=$(gcloud container clusters describe "$CLUSTER_NAME" --region "$REGION" --project "$PROJECT_ID" --format=json)"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/scripts/audit_cluster.sh:18`: "CLUSTER_JSON=$(gcloud container clusters describe "${CLUSTER_NAME}" --region "${REGION}" --project "${PROJECT_ID}" --format=json)"

**Recommendation** (confident): Keep the Platform copy: it is the upstream-synced one (scripts/sync-upstream-skills.py syncs google/skills into agents/platform/skills only and carries its local fix in SKILL_SUBSTITUTIONS), both copies were last touched together in e4edc3b6 (2026-09-08, the NetworkPolicy two-step fix, hand-applied to the cluster copy and carried for the platform copy in SKILL_SUBSTITUTIONS), which is itself the duplication cost, and the Platform Agent is the persona allowed to run its gcloud/kubectl writes. The Cluster copy cannot simply be deleted because agents/cluster/ is the per-cluster profile template the Dockerfile copies to /opt/cluster-template and the Cluster Agent is a read-only SRE (agents/cluster/SOUL.md 'Read-Only Boundary'), so shrink it to the read-only parts (Workflow 1 audit script and the `clusters describe` dataplane check) with a pointer to the Platform skill for every enablement/apply step.

Decision needed: yes

### dup-7c8050: gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

Two near-identical SKILL.md files with the same name sit in the repo, so a reader or tool that treats third_party/google-skills/ as a second installable skill will pick up the unpatched upstream text (broken gcloud command, PR opened on every run) instead of the copy the image actually ships.

Evidence:
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:2`: "name: gke-workload-troubleshooting"
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:11`: "Use this skill to systematically diagnose and resolve failures in application"
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:2`: "name: gke-workload-troubleshooting"
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:11`: "Use this skill to systematically diagnose and resolve failures in application"

**Recommendation** (confident): Keep agents/platform/skills/gke-workload-troubleshooting as the skill: it is the generated copy the platform image ships (deploy/docker/Dockerfile line 1915 copies agents/platform/skills/ only) and it carries the two repo patches. The third_party copy is not a competing skill but layer 1 of the overlay design (docs/designs/upstream-skill-overlays.md): a byte-identical snapshot of google/skills at commit 4b5a7c4 that scripts/skill_overlay.py (COPY_ROOT) reads to rebuild the platform copy, that `make skills-check` (validate.yml line 66) and `make skills-verify-upstream` (line 539) verify against agents/platform/skill-overlays/gke-workload-troubleshooting/upstream.lock, and that scripts/sync-upstream-skills.py, prettier, shellcheck and the docs link check all deliberately skip; it is never shipped or loaded by any agent. The wiring makes this copy necessary and it cannot be trimmed (any edit breaks the sha256 lock check), so leave both in place; the only legitimate way to end the pair is to stop mirroring (delete copy, lock and overlay), which forfeits upstream syncs and is not worth it for two small patches.

Decision needed: no

### dup-7e9127: review-security-k8s-agents-main, review-security-k8s-main

The two orchestrators carry the same four-step workflow, JSON schema, triage wording and aggregation text word for word, and because main also launches agents-main as a sub-skill, a CI gate that runs both runners (as docs/architecture/06 section 7 says it does) runs the six agent sub-reviews twice and reports their findings twice, while any edit to the shared steps has to be made in two places.

Evidence:
- `review-security-k8s-agents-main/SKILL.md:6`: "Coordinate AI agent security review sub-agents, gather findings, and produce a summarized JSON report."
- `review-security-k8s-main/SKILL.md:6`: "Coordinate Kubernetes security review sub-agents, gather findings, and produce a summarized JSON report."
- `review-security-k8s-agents-main/SKILL.md:23`: "[{"agent": "<skill-name>", "findings": [{"message": "<desc>", "file": "<name>", "line": "<num>"}]}]"
- `review-security-k8s-main/SKILL.md:27`: "[{"agent": "<skill>", "findings": [{"message": "<desc>", "file": "<name>", "line": "<num>"}]}]"
- `review-security-k8s-agents-main/SKILL.md:28`: "Evaluate the raw findings against the project context to determine actual risk. Filter out findings that are functionally required by the workload's specific role or adequately mitigated by broader architectural controls. "
- `review-security-k8s-main/SKILL.md:32`: "Evaluate the raw findings against the project context to determine actual risk. Filter out findings that are functionally required by the workload's specific role or adequately mitigated by broader architectural controls. "
- `review-security-k8s-agents-main/SKILL.md:33`: "Merge the filtered findings into a single JSON array. Output MUST be valid JSON string (markdown blocks okay). Omit agents with no findings or return empty `findings`."
- `review-security-k8s-main/SKILL.md:37`: "Merge the filtered findings into a single JSON array. Output MUST be valid JSON string (markdown blocks okay). Omit agents with no findings or return empty `findings`."
- `review-security-k8s-main/SKILL.md:23`: "- `review-security-k8s-agents-main`"

**Recommendation** (likely): Keep review-security-k8s-main as the single entry point (it is the superset and already fans out to agents-main), and keep agents-main only as the agent-scoped sub-orchestrator main calls, since docs/architecture/03, 04 and 06 name it and main's sub-skill list depends on it; shrink agents-main to its six-skill list plus its two agent-specific triage examples, and have the review-gate contract (06 section 7) invoke main alone rather than both, so the agent sub-reviews run once. Both copies are hand-written local skills with no upstream source (neither is in scripts/sync-upstream-skills.py, agents/platform/skill-overlays/ or the .sss manifest), so neither wins on provenance; main wins on coverage.

Decision needed: yes

## 5. Conflicts

These skills disagree. An agent that loads both will get two answers.

### conf-cc8c8e: gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability)

The Cluster copy's flag does not exist in gcloud, so an agent following it gets an unrecognized-argument error and never turns on Dataplane V2 observability.

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:117`: "    --enable-dataplane-v2-observability \"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:63`: "  --enable-dataplane-v2-flow-observability \"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The Platform copy is right: `gcloud container clusters update --help` (installed SDK) lists only `--enable-dataplane-v2-flow-observability` and `--enable-dataplane-v2-metrics`; `--enable-dataplane-v2-observability` matches nothing. Note the Platform copy's own golden-path row (line 29, `advancedDatapathObservabilityConfig.enableMetrics: true`) is actually set by `--enable-dataplane-v2-metrics`, not by the flow-observability flag, but that is an upstream inconsistency inside one file, not a disagreement between the pair.

Decision needed: yes

### conf-06309a: gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability)

`--monitoring` replaces the whole component set, so running the Cluster copy's command on a golden-path cluster silently switches off the STORAGE, POD, DEPLOYMENT, STATEFULSET, DAEMONSET, HPA, CADVISOR, KUBELET and DCGM metrics the Platform copy told the agent to enable.

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:105`: "    --monitoring=SYSTEM,API_SERVER,SCHEDULER,CONTROLLER_MANAGER \"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:53`: "  --monitoring=SYSTEM,API_SERVER,SCHEDULER,CONTROLLER_MANAGER,STORAGE,POD,DEPLOYMENT,STATEFULSET,DAEMONSET,HPA,CADVISOR,KUBELET,DCGM \"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:27`: "`monitoringConfig` components                       | SYSTEM_COMPONENTS, STORAGE, POD, DEPLOYMENT, STATEFULSET, DAEMONSET, HPA, JOBSET, CADVISOR, KUBELET, DCGM, APISERVER, SCHEDULER, CONTROLLER_MANAGER | Full suite including control-plane"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The Platform copy is right for this repo, whose golden path (gke-golden-path assets and the Platform copy's own table) enables the full component list; gcloud's help describes `--monitoring` as 'Set the components that have monitoring enabled', a replacement, so the Cluster copy's shorter list is a downgrade rather than an addition.

Decision needed: yes

### conf-2abc8c: gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability)

The cluster copy tells a persona that SOUL.md forbids from mutating cluster state to run `gcloud container clusters update` for the maintenance window, and the command it gives omits `--maintenance-window-end`, which gcloud requires alongside `--maintenance-window-start` and `--maintenance-window-recurrence` (the gke-upgrades runbook-template.md includes all three), so the Cluster Agent either breaks its read-only boundary or fails with a usage error.

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:91`: "gcloud container clusters update <cluster-name> \"
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:93`: "    --maintenance-window-start <start-time> \"
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:94`: "    --maintenance-window-recurrence "FREQ=DAILY""
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:209`: "6.  **Maintenance windows**: Schedule upgrades during low-traffic periods (see"
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:210`: "    the `gke-upgrades` skill)."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The platform copy is right: maintenance windows are a cluster-setting change owned by gke-upgrades (whose runbook has the complete start/end/recurrence command), and the Cluster Agent is read-only, so delete workflow 6 and best practice 5 from the cluster copy and point to the Platform Agent instead.

Decision needed: yes

### conf-3e36c1: gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability)

The two copies set a different minimum bar for probes, so the Cluster Agent passes a workload that has only a readiness probe while the Platform Agent (and the operator's own manifests, which cite the platform rule 3 for explicit timings) flag the same workload as non-compliant.

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:100`: "2. **Probes for All Containers**: Every container in a production pod should have at least a readiness probe."
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:198`: "3.  **Probes with Explicit Timeouts**: Every production container must have both"
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:199`: "    liveness and readiness probes defined. **Always explicitly define"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The platform copy is right: it is the upstream rule, and k8s-operator/internal/controller/platformagent_manifests.go already treats its rule 3 (both probes, explicit initialDelaySeconds/periodSeconds/timeoutSeconds) as the standard; raise the cluster copy's best practice 2 to the same bar.

Decision needed: yes

### conf-7e2e10: gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability)

The copies disagree on which workloads need a PodDisruptionBudget, so a Cluster Agent audit reports no gap for an ordinary 3-replica Deployment without a PDB while the Platform Agent's rule says that Deployment is missing one.

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:101`: "3. **PDBs for Critical Apps**: Use PDBs to prevent downtime during automated node upgrades."
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:86`: "> Every production Deployment with 2+ replicas should have a PDB."
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:196`: "2.  **PDBs for everything**: Every production workload with 2+ replicas needs a"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The platform copy is right: a replica-count rule is checkable from `kubectl get deploy` and `kubectl get pdb`, while 'critical' is a judgement the Cluster Agent has no data for; adopt the 2+ replicas threshold in the cluster copy.

Decision needed: yes

### conf-023f83: gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability)

The cluster copy presents ScheduleAnyway as an equally valid choice for zone spread while the platform copy makes zone spread a hard DoNotSchedule requirement, so the Cluster Agent may propose a patch the Platform Agent's own rule would reject.

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:78`: "      whenUnsatisfiable: DoNotSchedule # or ScheduleAnyway"
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:176`: "-   **Zone spread** (`DoNotSchedule`): Hard requirement -- pods must be balanced"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The platform copy is right and more precise (zone spread hard, hostname spread best-effort); drop the '# or ScheduleAnyway' comment from the cluster copy's zone constraint, or copy the platform's two-constraint example.

Decision needed: yes

### conf-111665: gke-storage (agents/cluster/skills/gke-storage), gke-storage (agents/platform/skills/gke-storage)

A Cluster Agent following its copy will tell a user that a Filestore PVC should use StorageClass `standard-rwm`, which GKE does not ship (the built-in Filestore classes are `standard-rwx`/`premium-rwx`, and the operator itself hardcodes `standard-rwx`), so the PVC stays Pending with a provisioner-not-found error.

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:55`: "  storageClassName: standard-rwm # Pre-defined for Filestore"
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:47`: "`standard-rwx` | Filestore (Basic HDD) | Shared NFS"
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:93`: "  storageClassName: standard-rwx"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The platform copy is right: GKE's pre-installed Filestore StorageClasses are `standard-rwx` and `premium-rwx` (RWX = ReadWriteMany), and the repo's own operator uses `standard-rwx` (k8s-operator/internal/controller/platformagent_manifests.go:340). Fix the cluster copy's `standard-rwm` to `standard-rwx`.

Decision needed: yes

### conf-813608: gke-storage (agents/cluster/skills/gke-storage), gke-storage (agents/platform/skills/gke-storage)

The cluster copy's example creates a custom regional pd-ssd StorageClass named `premium-rwo`, while the platform copy lists `premium-rwo` as a GKE built-in (zonal pd-ssd); applying the cluster example either fails because the name already exists or, if forced, redefines a built-in class other workloads rely on.

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:26`: "  name: premium-rwo"
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:30`: "  replication-type: regional-pd"
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:41`: "GKE provides built-in StorageClasses:"
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:46`: "`premium-rwo`  | `pd-ssd`              | High IOPS, databases"
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:56`: "  name: fast-regional"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The platform copy is right: `premium-rwo` is a StorageClass GKE pre-installs, so a custom regional class needs its own name, as the platform example's `fast-regional` does. Rename the cluster example's class (or drop the example per the duplicate finding).

Decision needed: yes

### conf-f4805c: gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security)

The Cluster copy tells a read-only agent to run `gcloud container clusters update --enable-gke-sandbox`, a flag that does not exist (`gcloud container clusters update --help` offers `--enable-agent-sandbox` and `--enable-shielded-nodes`; GKE Sandbox is enabled per node pool with `gcloud container node-pools create ... --sandbox type=gvisor`), so the step fails with an unknown-flag error and the Platform copy explicitly says this step is not this skill's to run.

Evidence:
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:144`: "gcloud container clusters update <cluster-name> \"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:145`: "    --enable-gke-sandbox \"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:146`: "Enabling Shielded Nodes (`--enable-shielded-nodes`) and GKE Sandbox"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:147`: "(`--enable-gke-sandbox`) at the cluster control plane level are platform-level"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:148`: "actions covered in the `gke-platform-security` skill.)*"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The Platform copy is right that enablement does not belong in this skill (and the Cluster Agent may not mutate anything), but both copies name a flag gcloud does not have; the correct fact is that GKE Sandbox is a node-pool setting (`--sandbox type=gvisor` on `node-pools create`), and agents/platform/skills/gke-platform-security/SKILL.md line 116 runs the same nonexistent `--enable-gke-sandbox` and needs the same correction via SKILL_SUBSTITUTIONS so the next sync does not restore it.

Decision needed: yes

### conf-be0048: gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security)

The Cluster copy instructs the agent to run a cluster-level mutation (`clusters update --enable-shielded-nodes`) from this skill while the Platform copy says the same action is out of scope for gke-workload-security and belongs to gke-platform-security, and the Cluster Agent's persona forbids mutating cluster state at all, so a Cluster Agent following its own skill either breaks its read-only boundary or produces a plan the Platform Agent will not find in the skill it is told to use.

Evidence:
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:125`: "### 4. Enable Shielded Nodes"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:133`: "    --enable-shielded-nodes \"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:13`: "  control plane security, RBAC hardening, Binary Authorization, Shielded Nodes,"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:14`: "  or enabling platform-level GKE add-ons (use gke-platform-security instead)."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The Platform copy is right: Shielded Nodes enablement is a cluster-level write that gke-platform-security already carries (its 'Shielded Nodes & GKE Sandbox Enablement' section) and the Cluster Agent is read-only, so the Cluster copy should only report the audit script's Shielded Nodes PASS/FAIL and leave enablement to the Platform Agent.

Decision needed: yes

### conf-af4023: gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

An agent following the upstream copy runs `gcloud logging read` with `--start-time`/`--end-time`, flags that command does not have, so gcloud rejects it and the historical-events query in Step 2 returns nothing.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:112`: "gcloud logging read "resource.type=\"k8s_cluster\" AND logName=\"projects/{project_id}/logs/events\" AND jsonPayload.involvedObject.namespace=\"{workload_namespace}\"" --start-time="{start_time}" --end-time="{end_time}" --project="{project_id}""
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:112`: "gcloud logging read "resource.type=\"k8s_cluster\" AND logName=\"projects/{project_id}/logs/events\" AND jsonPayload.involvedObject.namespace=\"{workload_namespace}\" AND timestamp>=\"{start_time}\" AND timestamp<=\"{end_time}\"" --project="{project_id}""

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The platform copy is right: `gcloud logging read` takes the time window as `timestamp>=`/`timestamp<=` terms inside the filter, not as flags, which is exactly what overlay patch 0001-logging-read-timestamp-filter.patch records (Local-Issue #843, fixed in #885). The upstream copy must stay as upstream wrote it, so the disagreement is already handled by the overlay; what is still open is the patch header's `Upstream-Issue: none filed yet`, and agents/platform/scripts/command_policy.py line 543 and test_command_policy.py line 1746 still describe the shipped skill as passing `--start-time`/`--end-time`, which it no longer does.

Decision needed: yes

### conf-87efa5: gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

Step 5 of the upstream copy tells the agent to open a GitHub pull request on every troubleshooting run, while the shipped copy opens one only when the request asked for a fix; an agent following the upstream text would push an unrequested PR onto the user's GitOps repository for a plain 'why is it crashlooping' question.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:227`: "3.  Check if a branch or Pull Request (PR) already exists for this"
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:230`: "    change, open a Pull Request (PR) on GitHub, and conclude the workflow (do"
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:227`: "3.  If the request asked for the fix to be submitted or applied ("fix it","
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:233`: "4.  If the request asked you to investigate, diagnose or report, the manifest"
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:235`: "    one message away; do not open one (`SOUL.md` §3, item 3)."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The platform copy is right for this repository: agents/platform/SOUL.md section 3 item 3 (line 118) says a pull request is opened only when the request asks for one, tests/test_persona_proposal_posture.py line 92 asserts the shipped skill carries that gate, and overlay patch 0002-submit-only-when-asked.patch records it with Retire-When: never. The upstream copy is a snapshot of google/skills and is expected to differ here.

Decision needed: yes

### conf-f079bb: review-security-k8s-agents-main, review-security-k8s-main

main's step 1 tells the orchestrator to invoke review-security-k8s-understand and wait for its summary, while agents-main's step 1 only says to pass context that is assumed to already exist, so when agents-main runs as its own runner (as docs/architecture/04 section 3 and 06 section 7 say it does) nothing produces that context, the six sub-agents review blind, and the step 3 triage has no project context to filter against.

Evidence:
- `review-security-k8s-main/SKILL.md:10`: "Invoke `review-security-k8s-understand`. Wait for summary."
- `review-security-k8s-agents-main/SKILL.md:10`: "Pass project context (from `review-security-k8s-understand`) to sub-agents."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): main's wording is right for a skill that can be the top-level runner; agents-main should say the same with a nested-call allowance: use the context the caller supplied, and invoke review-security-k8s-understand itself when none was supplied.

Decision needed: yes

### conf-f29ced: capacity-obtainability, gke-stockout-investigator

The shared Diagnostics B sentence has drifted: capacity-obtainability says a reservation holds capacity and bans the word guarantee from any report (the obtainability bench cases grade that ban), while the stockout investigator's copy still tells the agent reservations guarantee compute capacity, so a remediation PR body or notification that echoes its own skill text makes the claim the sibling skill and its evals treat as wrong.

Evidence:
- `capacity-obtainability/SKILL.md:361`: "Check if any zonal reservations are available for the target workload's machine type; a reservation holds capacity for it (the report must not describe this as a guarantee):"
- `capacity-obtainability/SKILL.md:50`: "the word "guarantee" about capacity, allocations, or scheduling anywhere"
- `capacity-obtainability/SKILL.md:51`: "in the report** — not even for reservations or ProvisioningRequests;"
- `gke-stockout-investigator/SKILL.md:159`: "Check if any zonal reservations are available for the target workload's machine type to guarantee compute capacity:"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): capacity-obtainability is right: its wording is the deliberate later edit of the same sentence, the repo's bench cases (obtainability-design-quota-vs-capacity, obtainability-window-planning-probe) grade the no-guarantee rule, and a GCE reservation holds capacity rather than guaranteeing scheduling; bring the stockout investigator's Diagnostics B line into step with it.

Decision needed: yes

### conf-27f689: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)

The Cluster Agent copy tells the agent to fetch credentials with --region only, so on a zonal cluster the mandatory first command fails before any diagnostics run, while the Platform copy allows --region or --zone.

Evidence:
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:23`: "Before running any diagnostics or `kubectl` commands, you **must** fetch GKE credentials and context for the target GKE cluster:"
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:26`: "gcloud container clusters get-credentials <cluster_name> --region <cluster_location>"
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:33`: "    -   Attempt credential fetch: `gcloud container clusters get-credentials"
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:34`: "        {cluster_name} --region/--zone {cluster_location}`"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The Platform copy is right that the flag must match the cluster's location type; the Cluster copy should use `--location <cluster_location>`, the form the repo's own scaffold (agents/platform/scripts/cluster_agent_profile.py) and agents/platform/AGENTS.md use, and since the Cluster Agent's KUBECONFIG is already pinned at scaffold time and verified by cluster_preflight.sh, the 'must fetch' sentence should point at the preflight instead of re-running get-credentials.

Decision needed: yes

### conf-3ce3a3: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)

When the user gives no time, the two copies centre the 1-hour event window on different instants (the pod's last crash transition versus now), so the Platform Agent walking the same crashloop queries Cloud Logging for a window that can miss the first failure's events and reach a different RCA than the Cluster Agent.

Evidence:
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:35`: "     1. Retrieve the GKE pod status (`kubectl get pods -n <namespace> -o yaml`)."
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:36`: "     2. If there are crashing or pending containers, check their state transition timestamps (e.g. `status.containerStatuses[*].lastState.terminated.finishedAt` or `status.startTime`) and use that transition time as $T$."
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:37`: "     3. If no active transitions are found, default to the **current system time** as $T$."
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:53`: "        -   **No Time Provided (Default)**: Use current system time as"
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:54`: "            `{issue_time}`."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The Cluster copy is right: the pod's `lastState.terminated.finishedAt` is the moment the failure happened and is the evidence the crashloop evals already expect the agent to read, so the Platform copy should gain the same three-step default via a third overlay patch rather than a hand edit.

Decision needed: yes

### conf-d08433: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

The upstream copy's Step 2 Cloud Logging command passes --start-time/--end-time, flags gcloud logging read does not have (local gcloud help lists only --freshness), so an agent following that copy gets an argument error instead of the historical events; the cluster copy puts the window in the filter and works.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:112`: "gcloud logging read "resource.type=\"k8s_cluster\" AND logName=\"projects/{project_id}/logs/events\" AND jsonPayload.involvedObject.namespace=\"{workload_namespace}\"" --start-time="{start_time}" --end-time="{end_time}" --project="{project_id}""
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:87`: "gcloud logging read "resource.type=\"k8s_cluster\" AND logName=\"projects/<project_id>/logs/events\" AND jsonPayload.involvedObject.namespace=\"<workload_namespace>\" AND timestamp>=\"[Start_Time]\" AND timestamp<=\"[End_Time]\"" --project="<project_id>""

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): The cluster copy is right (gcloud logging read takes the time bounds as timestamp>= / timestamp<= filter clauses; the repo fixed this in #885 and carries it for the platform copy as agents/platform/skill-overlays/gke-workload-troubleshooting/0001-logging-read-timestamp-filter.patch). The upstream copy must stay byte-identical to its upstream.lock, so leave it and raise the fix upstream.

Decision needed: yes

### conf-e5160c: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

Step 5 gives opposite instructions on the write path: the upstream copy tells the agent to create a branch and open a pull request on every walk, while the cluster copy forbids opening one and hands the RCA off through kanban_complete; an agent that followed the upstream wording inside the Cluster Agent would breach the persona's read-only, no-PR boundary.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:227`: "3.  Check if a branch or Pull Request (PR) already exists for this"
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:230`: "    change, open a Pull Request (PR) on GitHub, and conclude the workflow (do"
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:155`: "As a Cluster Agent you operate under a strict **read-only** boundary: **do not apply patches directly to the cluster, and do not open Pull Requests yourself.** The GitOps write path (`submit-suggestion`) is owned exclusively by the Platform Agent. You also **never pass context back through your chat reply** — you communicate only through the kanban task you were spawned on."
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:162`: "   kanban_complete("

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The cluster copy is right for where it runs: agents/cluster/SOUL.md line 14 and CAPABILITIES.md line 1 make the Cluster Agent read-only and say it never opens pull requests, and the platform copy already replaces the unconditional PR step with overlay patch 0002-submit-only-when-asked.patch. The upstream copy is an unshipped mirror (not copied by deploy/docker/Dockerfile, excluded from docs reachability), so no agent loads its Step 5.

Decision needed: yes

### conf-133f78: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

When no issue time is given, the upstream copy centres the one-hour event window on the current time while the cluster copy first reads the crashing container's state-transition timestamp and falls back to now only if none exists; an agent on the upstream default misses every event older than thirty minutes for a pod that has been crash-looping since the morning.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:53`: "        -   **No Time Provided (Default)**: Use current system time as"
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:54`: "            `{issue_time}`."
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:36`: "     2. If there are crashing or pending containers, check their state transition timestamps (e.g. `status.containerStatuses[*].lastState.terminated.finishedAt` or `status.startTime`) and use that transition time as $T$."
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:37`: "     3. If no active transitions are found, default to the **current system time** as $T$."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The cluster copy is right: anchoring the window on the container's last transition is what makes the Step 2 Cloud Logging query find the events that caused the failure, and the README's headline Cluster Agent example ('crash-looping since this morning') depends on it. The upstream mirror cannot be edited; the platform generated copy still carries the upstream default.

Decision needed: yes

### conf-a131a6: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

The credential-fetch command differs in its location flag: the upstream copy says --region/--zone, the cluster copy only --region, so an agent following the cluster copy against a zonal cluster (location like us-central1-a) gets a gcloud error before any diagnostics run.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:33`: "    -   Attempt credential fetch: `gcloud container clusters get-credentials"
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:34`: "        {cluster_name} --region/--zone {cluster_location}`"
- `gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)/SKILL.md:26`: "gcloud container clusters get-credentials <cluster_name> --region <cluster_location>"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The upstream copy is right that the flag depends on the cluster's location type; the cleanest fix for the cluster copy is `--location <cluster_location>`, which gcloud accepts for both regional and zonal clusters. In practice the line rarely runs for the Cluster Agent (SOUL.md line 19 pins its KUBECONFIG and the preflight verifies it), which is why nobody has hit it.

Decision needed: yes

### conf-3e92ca: review-security-k8s-agents-firewall, review-security-k8s-network

review-security-k8s-main runs both skills over the same manifests (network directly, firewall via review-security-k8s-agents-main), so a NodePort Service on an agent pod that has an ingress NetworkPolicy is flagged by one reviewer and passed by the other, and the merged report contradicts itself on whether NodePort is acceptable.

Evidence:
- `review-security-k8s-network/SKILL.md:16`: "- **NodePort Usage**: Flag `NodePort` usage (bypasses standard protections)."
- `review-security-k8s-agents-firewall/SKILL.md:21`: "- **Bypass Prevention**: Flag LoadBalancer or NodePort exposure on main agent containers lacking strict ingress NetworkPolicies."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): The network skill is right: NodePort opens a port on every node and kube-proxy SNATs external traffic to a node IP, so a pod-selector ingress NetworkPolicy can be satisfied by allowing the node CIDR, which is the bypass itself; the firewall skill should flag NodePort on agent containers unconditionally and keep the "lacking strict ingress NetworkPolicies" condition for LoadBalancer only.

Decision needed: yes

## 6. Missing pieces

These skills point at files or other skills that are not here.

Nothing found.

## 7. Unuseful or out of place

These skills do not belong in this repo, or do not help an agent do anything.

### low-239222: review-security-k8s-agents-prompt-injection

The whole skill is two bullets, neither covers input sanitization as the description promises, and neither covers the controls docs/architecture/03-security-model.md line 270 assigns to this skill (external input, cluster data and tool output treated as data never instructions, model output never an authorization signal), so the orchestrator's prompt-injection pass returns almost nothing useful.

Evidence:
- `review-security-k8s-agents-prompt-injection/SKILL.md:3`: "description: Reviews AI agent architectures (API gateways, WAFs, input sanitization) for prompt injection risks."
- `review-security-k8s-agents-prompt-injection/SKILL.md:10`: "- **Gateway/WAF**: Require LLM-specific API Gateway or WAF sidecar. Flag raw agent APIs exposed to untrusted traffic."
- `review-security-k8s-agents-prompt-injection/SKILL.md:11`: "- **Guardrails**: Ensure system prompts/safety instructions in `ConfigMaps`/`EnvVars` cannot be tampered with by less privileged workloads."

**Recommendation** (likely): Add checks for the controls the architecture doc assigns to this skill: tool output and cluster data treated as untrusted, model output not used as an authorization signal, and sensitive actions gated by the declarative review flow.

Decision needed: yes

### place-4e2e1f: gke-observability (agents/cluster/skills/gke-observability)

The Cluster Agent persona (agents/cluster/SOUL.md, CAPABILITIES.md) is strictly read-only and AGENTS.md reserves provisioning and write skills for the Platform Agent, yet workflows 2, 8 and 9 instruct `gcloud container clusters update`, so an agent following this skill would be told to mutate a cluster its persona forbids it to touch.

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:3`: "description: Workflows for setting up and auditing observability (logging, monitoring, tracing) on GKE."
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:31`: "gcloud container clusters update <cluster-name> \"
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:105`: "    --monitoring=SYSTEM,API_SERVER,SCHEDULER,CONTROLLER_MANAGER \"

**Recommendation** (confident): Cut the three `gcloud container clusters update` workflows from this copy and leave it as an audit-only skill, pointing at the Platform Agent's gke-observability for enabling features.

Decision needed: yes

### place-e2da8c: gke-reliability (agents/cluster/skills/gke-reliability)

The Cluster Agent is read-only by persona (agents/cluster/SOUL.md) and AGENTS.md places cluster-mutating work with the Platform Agent, so a maintenance-window `clusters update` step in this folder tells the agent to do what it is forbidden to do; the Platform Agent copy already defers this topic to `gke-upgrades`.

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:91`: "gcloud container clusters update <cluster-name> \"
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:93`: "    --maintenance-window-start <start-time> \"

**Recommendation** (confident): Remove workflow 6's update command from this copy and point at the Platform Agent's gke-upgrades skill for maintenance windows.

Decision needed: yes

### place-8f8a24: gke-storage (agents/cluster/skills/gke-storage)

The Cluster Agent is forbidden from kubectl apply, so a skill made only of create-and-apply workflows gives it nothing it may do, while the Platform Agent already carries a fuller copy of the same skill.

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:16`: "### 1. Configure Storage Classes"
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:61`: "### 3. Implement Volume Expansion"
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:68`: "2. Apply the changes."

**Recommendation** (likely): Replace the cluster copy with read-only storage diagnostics (PVC/PV phase, StorageClass and CSI driver presence, FailedMount and resize events) and leave configuration guidance to the platform copy.

Decision needed: yes

### place-ef892a: gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)

The Cluster Agent persona forbids kubectl scale and apply and cluster updates, so this copy either tempts the agent across its read-only boundary or gives it nothing usable when SOUL.md tells it to load a scaling diagnostic skill.

Evidence:
- `gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)/SKILL.md:19`: "kubectl scale deployment <deployment-name> --replicas=<number> -n <namespace>"
- `gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)/SKILL.md:34`: "kubectl autoscale deployment <deployment-name> --cpu-percent=50 --min=1 --max=10"
- `gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)/SKILL.md:42`: "kubectl apply -f assets/hpa-example.yaml"
- `gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)/SKILL.md:61`: "gcloud container clusters update <cluster-name> --enable-vertical-pod-autoscaling --zone <zone>"

**Recommendation** (likely): Rewrite the cluster copy as read-only scaling diagnostics (HPA and VPA status and conditions, metrics availability, ScalingLimited and FailedGetResourceMetric events) and keep the write workflows in the platform copy only.

Decision needed: yes

### place-f5e556: gke-workload-security (agents/cluster/skills/gke-workload-security)

Six of the eight workflows create namespaces, bind IAM roles, apply manifests or update the cluster, which the Cluster Agent persona forbids, so the copy under agents/cluster mostly describes work the Platform Agent owns.

Evidence:
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:44`: "   kubectl create namespace workload-identity-test-ns"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:52`: "   gcloud iam service-accounts add-iam-policy-binding <gsa-name>@<project-id>.iam.gserviceaccount.com \"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:106`: "gcloud container clusters update <cluster-name> \"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:122`: "kubectl apply -f ./assets/default-deny-netpol.yaml -n <target-namespace>"

**Recommendation** (likely): Trim the cluster copy to the audit script and the read-only describe checks, and point hardening steps at the platform copy.

Decision needed: yes

### place-5e99d1: gke-ai-troubleshooting-handle-disruption-gpu-tpu

This is read-only, single-cluster runtime debugging, which AGENTS.md assigns to the Cluster Agent, so a cluster-scoped agent asked about a GPU node disruption has no copy of the runbook while the fleet-level agent carries it.

Evidence:
- `gke-ai-troubleshooting-handle-disruption-gpu-tpu/SKILL.md:32`: "    kubectl get nodes -l cloud.google.com/scheduled-maintenance-time -L cloud.google.com/scheduled-maintenance-time"
- `gke-ai-troubleshooting-handle-disruption-gpu-tpu/SKILL.md:88`: "-   **Reporting Rule**: Signal Only. Report high-signal information indicating"

**Recommendation** (likely): Add a Cluster Agent copy under agents/cluster/skills (as gke-workload-troubleshooting has), keeping the platform copy because the upstream sync re-creates it.

Decision needed: yes

### place-c420aa: gke-ai-troubleshooting-jobset-interruption

This is read-only, single-cluster runtime debugging, which AGENTS.md assigns to the Cluster Agent, so a cluster-scoped agent asked about a restarting JobSet has no copy of the runbook while the fleet-level agent carries it.

Evidence:
- `gke-ai-troubleshooting-jobset-interruption/SKILL.md:13`: "Use this skill to systematically diagnose and resolve JobSet interruptions,"
- `gke-ai-troubleshooting-jobset-interruption/SKILL.md:58`: "### Step 1: Identify JobSet Restarts and Attempts [Low Risk]"

**Recommendation** (likely): Add a Cluster Agent copy under agents/cluster/skills (as gke-workload-troubleshooting has), keeping the platform copy because the upstream sync re-creates it.

Decision needed: yes

### place-5ea829: gke-ai-troubleshooting-tpu-vbar-oom

This is read-only, single-cluster runtime debugging, which AGENTS.md assigns to the Cluster Agent, so a cluster-scoped agent asked about a TPU node crash has no copy of the runbook while the fleet-level agent carries it.

Evidence:
- `gke-ai-troubleshooting-tpu-vbar-oom/SKILL.md:17`: "Use this skill to systematically diagnose and prevent `vbar_control_agent`"
- `gke-ai-troubleshooting-tpu-vbar-oom/SKILL.md:58`: "-   **Tool to use**: `query_logs` (for live diagnostics)"

**Recommendation** (likely): Add a Cluster Agent copy under agents/cluster/skills (as gke-workload-troubleshooting has), keeping the platform copy because the upstream sync re-creates it.

Decision needed: yes

## 8. Proposed changes

These are safe and the pull request applies them:

- Update install-kube-agents (Document --gitops-forge, --gitops-host, --gitlab-token-file and --gitlab-token-secret, and scope the minter prerequisites to the github forge.) [old-53530a]
- Patch review-preflight (Reword lines 81-82 to list the current docs-check components: generated regions, links and reachability, terminology, maintainer identifiers on site pages, context budget.; Update lines 87-88 to match the current Local Validation Checks bullet in AGENTS.md.) [old-10bf86, old-59686b]
- Patch review-security-k8s-agents-audit-logs (Replace `AuditPolicy` with `audit.k8s.io/v1 Policy` and add the GKE Cloud Audit Logs / Data Access logs form of the check.) [old-af4d83]
- Update gke-observability (agents/cluster/skills/gke-observability) (Align the audit text with the fields the describe command actually prints.; Change workflow 9 to the current flag names.) [old-7a047d, old-831dba]
- Update gke-reliability (agents/cluster/skills/gke-reliability) (Complete the flag set or drop the command per the out_of_place finding.) [old-a41048]
- Update gke-storage (agents/cluster/skills/gke-storage) (Replace `standard-rwm` with `standard-rwx` on line 55 of SKILL.md.) [old-2cdfcd]

### Waiting on your decision

One line per action. Several findings can point at the same action; all their IDs are listed.

- Patch review-security-k8s-agents-prompt-injection (Extend the checklist to the prompt-injection controls listed in docs/architecture/03-security-model.md and the input-sanitization scope the description claims.) [low-239222]
- Patch review-security-k8s-pod (Drop the CAP_ prefix from the capability names on line 22 of SKILL.md.) [old-9ac7ee]
- Patch gke-stockout-investigator (In agentplugins/gke-stockout-investigator/files/skills/gke-stockout-investigator/SKILL.md line 159, replace 'to guarantee compute capacity:' with '; a reservation holds capacity for it (the report must not describe this as a guarantee):' so the two copies of Diagnostics B read the same; the diagnostic commands (A-D) and Rules A-H otherwise match verbatim apart from the investigator's added Diagnosis sub-steps for Rules G and H and its extra Flex-Start/per-zone probes being absent, which are scope, not drift.; Remove the kube-agents-specific path from Step 3.3 so the search instruction stands alone.) [old-cd8c4b, conf-f29ced]
- Patch gke-observability (agents/cluster/skills/gke-observability) (Remove workflows 2, 8 and 9's update commands; keep the describe/logs/LQL audit steps.) [place-4e2e1f]
- Patch gke-reliability (agents/cluster/skills/gke-reliability) (Replace workflow 6 with a read-only check (`gcloud container clusters describe --format=json(maintenancePolicy)`) and a pointer to gke-upgrades.) [place-e2da8c]
- Patch gke-storage (agents/cluster/skills/gke-storage) (In agents/cluster/skills/gke-storage/SKILL.md line 26 rename the example StorageClass from `premium-rwo` to a non-built-in name such as `fast-regional`, matching the platform copy.; In agents/cluster/skills/gke-storage/SKILL.md line 55 change `storageClassName: standard-rwm` to `storageClassName: standard-rwx` (or remove the authoring example per the duplicate finding).; Rewrite agents/cluster/skills/gke-storage/SKILL.md around kubectl get/describe checks for PVC, PV, StorageClass, CSIDriver and volume events; drop the create and expand workflows.) [place-8f8a24, conf-111665, conf-813608]
- Patch gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) (Replace the scale/autoscale/apply/update commands in agents/cluster/skills/gke-workload-scaling/SKILL.md with kubectl get/describe hpa and vpa, kubectl top, and event reads; keep the best-practice notes as interpretation guidance.) [place-ef892a]
- Update gke-workload-security (agents/cluster/skills/gke-workload-security) (Rewrite the Enable GKE Sandbox block in SKILL.md lines 141-147 to use gcloud container node-pools create ... --sandbox type=gvisor.) [old-5fefe4]
- Patch gke-workload-security (agents/cluster/skills/gke-workload-security) (Keep workflow 1 and the Dataplane/NetworkPolicy describe check in agents/cluster/skills/gke-workload-security/SKILL.md; remove the enable, create, bind, annotate and apply steps.) [place-f5e556]
- Move gke-ai-troubleshooting-handle-disruption-gpu-tpu (Copy to agents/cluster/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu; do not delete the platform copy, scripts/sync-upstream-skills.py would restore it.) [place-5e99d1]
- Move gke-ai-troubleshooting-jobset-interruption (Copy to agents/cluster/skills/gke-ai-troubleshooting-jobset-interruption; do not delete the platform copy, scripts/sync-upstream-skills.py would restore it.) [place-c420aa]
- Move gke-ai-troubleshooting-tpu-vbar-oom (Copy to agents/cluster/skills/gke-ai-troubleshooting-tpu-vbar-oom; do not delete the platform copy, scripts/sync-upstream-skills.py would restore it.) [place-5ea829]
- Patch gke-basics (Add a gke-basics substitution in scripts/sync-upstream-skills.py that rewrites the flag in references/cli-reference.md.) [old-986a59]
- Patch gke-cluster-autoscaler (Rewrite 'resources/ca-capacity-buffers.md' to 'references/ca-capacity-buffers.md' in assets/capacity-buffer-serving.yaml.) [old-1a9274]
- Patch gke-cluster-creation (Add a gke-cluster-creation substitution in scripts/sync-upstream-skills.py for lines 81, 122 and 251 of SKILL.md.) [old-09ef08]
- Patch gke-compute-classes (Rewrite the two stale file names in the asset comments through scripts/sync-upstream-skills.py.) [old-b36ef3]
- Patch gke-golden-path (Drop lines 3 and 147 of assets/golden-path-autopilot.yaml upstream, or add the referenced resources/recommended-ap.yaml.) [old-3bbdcd]
- Patch gke-productionize (Add a SKILL_SUBSTITUTIONS entry for gke-productionize replacing 'gke-scaling,' with 'gke-workload-scaling,' in the frontmatter description.) [old-146246]
- Patch gke-service-networking (Add a SKILL_SUBSTITUTIONS entry for gke-service-networking replacing 'networking.gke.io/cert-map' with 'networking.gke.io/certmap'.; Replace the prerequisite sentence with one naming `--gateway-api=standard` for Standard clusters and Autopilot 1.26+ as the default-on case.) [old-3574a6, old-dbccdf]
- Remove gke-tpu-dynamic-slices-monitoring (Remove scripts/validate_queries.sh upstream (google/skills skills/cloud/gke-tpu-dynamic-slices-monitoring); it prints 'Validation skipped' unconditionally.) [old-d758bd]
- Remove gke-tpu-metrics-monitoring (Remove scripts/validate_queries.sh upstream (google/skills skills/cloud/gke-tpu-metrics-monitoring); it exits after printing 'Validation skipped'.) [old-8dbbf7]
- Patch kube-agents-observability (Rewrite Metrics step 1's second bullet to inspect the PodMonitoring resource instead of Deployment annotations.) [old-659b7e]
- Merge manage-cluster into cluster-agent-lifecycle (1) In agents/platform/skills/cluster-agent-lifecycle/SKILL.md add a section `## Manage an existing cluster on request` between `When to create a profile` and the kanban section, carrying manage-cluster's steps 1-2 (resolve `project` via `gcloud config get-value project` then `gcloud container clusters list` if absent; verify with `verify_gke_cluster` or `gcloud container clusters describe ... --format="value(status)"` and stop if missing), its step 4 confirmation wording, its `Stop managing` paragraph (tear down or add to `spec.scope.exclude.clusters`; deleting the profile alone is recreated by the next reconcile) and the `get-credentials` reachability note; drop its duplicated create command, reconcile and read-only notes since the keeper already has them. 2) Extend the keeper's frontmatter `description` with the trigger phrase `or when a user asks to manage/onboard/watch a specific existing cluster ("manage my cluster <name> in <location>")` so skill routing still fires on that request. 3) Change the keeper's line 16 `(see `manage-cluster`)` to point at the new section. 4) Delete agents/platform/skills/manage-cluster/. 5) Repoint the references: agents/platform/SOUL.md:186 and agents/platform/AGENTS.md:49 (name `cluster-agent-lifecycle`), scripts/generate_docs.py:90 (remove the `manage-cluster` entry), docs/site/src/content/docs/index.mdx:67, docs/site/src/content/docs/deploy/multi-project.md:50 and :194, docs/site/src/content/docs/concepts/cluster-agents.md:23, docs/site/src/content/docs/reference/security-and-iam.md:280, then run `make docs-generate` so docs/site/src/content/docs/skills/index.mdx drops the row; agents/platform/scripts/test_verify_skills_provenance.py uses `manage-cluster` only as a fixture directory name and needs no change. 6) While editing the merged create section, note that `/opt/data/scripts/cluster_agent_profile.py` is the agent-pod-only stub in the shell sandbox (deploy/sandbox/Dockerfile:521), the same caveat the keeper already states for the `name` subcommand at line 31, so the merged text does not keep presenting `create` as a shell command that succeeds from the agent's terminal.) [dup-5b7877]
- Patch gke-observability (agents/cluster/skills/gke-observability) into gke-observability (agents/platform/skills/gke-observability) (Drop workflow 8's update command from the Cluster copy (the Cluster Agent is read-only); if an enable command stays anywhere, it must carry the full golden-path list or say explicitly that `--monitoring` replaces the current set and the existing components must be re-listed.; Remove workflow 9 from the Cluster copy (it is a mutation the Cluster Agent may not run) and let the Platform copy own the command; if a Dataplane V2 line is kept in the Cluster copy at all, it must read `--enable-dataplane-v2-flow-observability` (or `--enable-dataplane-v2-metrics` for the enableMetrics golden-path setting).; Rewrite agents/cluster/skills/gke-observability/SKILL.md to keep only what a read-only Cluster Agent can do on its one cluster: the describe-loggingConfig/monitoringConfig audit (workflow 1), the gmp-system pod check, kubectl logs / kubectl top, and the LQL queries; drop every `gcloud container clusters update` block (workflows 2, 8, 9) and the Trace/Profiler/dashboard advice, which agents/cluster/CAPABILITIES.md says the agent never acts on, and end with one line saying enablement commands and golden-path values live in the Platform Agent's gke-observability skill, which is where the kanban result should route them. Do not add the skill to SKILL_AGENT_OVERRIDES in scripts/sync-upstream-skills.py: syncing the full upstream file into the cluster profile would ship mutation commands to a persona forbidden to run them.) [dup-a860b1, conf-cc8c8e, conf-06309a]
- Patch gke-reliability (agents/cluster/skills/gke-reliability) into gke-reliability (agents/platform/skills/gke-reliability) (Change line 100 of agents/cluster/skills/gke-reliability/SKILL.md to require both liveness and readiness probes with explicit initialDelaySeconds, periodSeconds and timeoutSeconds, and extend the workflow 3 grep so the audit also reads those three fields.; Change line 101 of agents/cluster/skills/gke-reliability/SKILL.md to 'every production workload with 2 or more replicas needs a PDB', matching the platform copy.; Remove section '### 6. Maintenance Windows and Exclusions' (lines 84-95) and best practice 5 (line 103) from agents/cluster/skills/gke-reliability/SKILL.md; replace with one sentence that maintenance windows are set by the Platform Agent through its gke-upgrades skill.; Replace the topologySpreadConstraints example at lines 73-82 of agents/cluster/skills/gke-reliability/SKILL.md with the platform copy's example (zone DoNotSchedule plus hostname ScheduleAnyway) and remove the '# or ScheduleAnyway' comment.; Rewrite agents/cluster/skills/gke-reliability/SKILL.md as a short read-only audit checklist for one cluster: keep the describe/get/grep checks of workflows 1, 2, 3 and 5 (regional control plane and zone spread, PDB presence and ALLOWED DISRUPTIONS, probe presence and explicit timeouts, topologySpreadConstraints), align its best-practice thresholds with the platform copy (both probes with explicit timings, PDB for every 2+ replica workload, zone spread DoNotSchedule), drop workflow 6 and every `gcloud container clusters update` and manifest-apply instruction, and end with one line saying the proposed manifest patch and any cluster setting change go to the Platform Agent, whose gke-reliability and gke-upgrades skills own them. Leave the platform copy as the sync writes it.) [dup-90a10f, conf-2abc8c, conf-3e36c1, conf-7e2e10, conf-023f83]
- Patch gke-storage (agents/cluster/skills/gke-storage) into gke-storage (agents/platform/skills/gke-storage) (Rewrite agents/cluster/skills/gke-storage/SKILL.md as a short read-only diagnostic skill (describe PVC/PV/StorageClass, read binding events, identify provisioner and access-mode mismatches, name the built-in GKE StorageClasses standard-rwo/premium-rwo/standard-rwx/premium-rwx) and drop the StorageClass/PVC authoring manifests, the Filestore PVC example and the volume-expansion procedure, replacing them with one line: provisioning and expansion belong to the Platform Agent's gke-storage skill. Do not touch the platform copy by hand (the sync overwrites it; corrections go in SKILL_SUBSTITUTIONS). Both skills/index.mdx rows are generated, so run make docs-generate after; check_prompt_assets.py already treats the two as independent bundles. Per .agents/rules/eval_driven_development.md a change to a shipped skill starts from a red bench case.) [dup-e78aa6]
- Patch gke-workload-security (agents/cluster/skills/gke-workload-security) into gke-workload-security (agents/platform/skills/gke-workload-security) (Delete Workflow 5's `gcloud container clusters update ... --enable-gke-sandbox` block from the cluster copy (it goes with the trim in the duplicate finding). In the platform copy, change the parenthetical on lines 146-148 to say GKE Sandbox is enabled per node pool (`gcloud container node-pools create <pool> --cluster <cluster> --sandbox type=gvisor`) by the gke-platform-security skill, and register that text as a (old, new) pair under SKILL_SUBSTITUTIONS['gke-workload-security'] in scripts/sync-upstream-skills.py so the sync keeps it; fix the same flag in gke-platform-security/SKILL.md line 116 the same way (new SKILL_SUBSTITUTIONS entry), ideally upstream in google/skills too.; Remove Workflow 4 (Enable Shielded Nodes) from agents/cluster/skills/gke-workload-security/SKILL.md as part of the read-only trim; the audit script's existing '[FAIL] Shielded Nodes are DISABLED' line is the Cluster Agent's whole contribution, and the proposed fix in its kanban result names the Platform Agent's gke-platform-security skill.; Trim agents/cluster/skills/gke-workload-security/SKILL.md to the Security Audit workflow plus the read-only `gcloud container clusters describe ... datapathProvider,networkPolicy.enabled` check and the Best Practices list; replace Workflows 2-8 (Workload Identity binding, Calico enablement, default-deny apply, Shielded Nodes, GKE Sandbox, PSS labels, Secret Manager CSI, NetworkLogging) with one line saying remediation is proposed to the Platform Agent, which runs them from its gke-workload-security / gke-platform-security skills. Drop assets/default-deny-netpol.yaml and assets/workload-identity-pod.yaml from the cluster copy (both are only applied, never read). Update scripts/test_sync_upstream_skills.py::test_repo_workload_security_skills_have_enforcement_command, which currently loops over both 'platform' and 'cluster' and asserts the cluster copy contains `--enable-network-policy` and `--update-addons=NetworkPolicy=ENABLED`, to check the platform copy only. Keep the docs/site skills catalogue row for the cluster copy, which scripts/generate_docs.py emits by persona.) [dup-29508a, conf-f4805c, conf-be0048]
- Patch review-security-k8s-agents-main into review-security-k8s-main (Leave review-security-k8s-main as is. In review-security-k8s-agents-main/SKILL.md keep the frontmatter, the six-item sub-skill list and the two agent-specific triage examples (lines 29-30); add one line to the Task section saying it is the agent-posture leg of review-security-k8s-main and emits the same finding schema, keeping the schema block so sub-agents can still be instructed when it runs nested. Separately update docs/architecture/06-api-and-data-contracts.md section 7 and 04-workflow-model.md section 3 to name review-security-k8s-main as the one runner the gate invokes, with agents-main reached through it, so the six agent sub-reviews are not launched twice per PR.) [dup-7e9127]
- Patch review-security-k8s-agents-main (Change review-security-k8s-agents-main/SKILL.md line 10 to: "Use the project context supplied by the caller; if none was supplied, invoke `review-security-k8s-understand` and wait for its summary. Pass it to sub-agents.") [conf-f079bb]
- Patch gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) (In agents/cluster/skills/gke-workload-troubleshooting/SKILL.md lines 23-27, replace the get-credentials block with: 'Your KUBECONFIG is pinned to this cluster at scaffold time; run `bash /opt/data/scripts/cluster_preflight.sh --json` (SOUL.md section 6 step 2) before any diagnostics. If you must refresh credentials for this cluster, use `gcloud container clusters get-credentials <cluster_name> --location <cluster_location> --project <project_id>`.' Do not touch the Platform copy; it is generated from third_party/google-skills plus the overlay patches and `make skills-check` would fail on a hand edit.) [conf-27f689]
- Patch gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) into gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) (Edit the 'No Time Provided (Default)' bullet in agents/platform/skills/gke-workload-troubleshooting/SKILL.md (lines 53-54) to the Cluster copy's three sub-steps (read pod status, use the crash/pending transition timestamp as {issue_time}, fall back to current time), then run `make skills-refresh SKILL=gke-workload-troubleshooting MSG="Default the issue time to the pod's last transition"` so it lands as 0003-*.patch under agents/platform/skill-overlays/gke-workload-troubleshooting/ and `make skills-check` stays green.) [conf-3ce3a3]
- Patch gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) into gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) (In agents/cluster/skills/gke-workload-troubleshooting/SKILL.md line 26 change `--region <cluster_location>` to `--location <cluster_location>` (or `--region/--zone` as upstream writes it). Leave the third_party mirror untouched.) [conf-a131a6]
- Patch review-security-k8s-agents-firewall (In .agents/skills/review-security-k8s-agents-firewall/SKILL.md line 21, split the bullet: "Flag NodePort exposure on agent containers (reachable on every node; a NetworkPolicy does not make it safe). Flag LoadBalancer exposure on main agent containers lacking strict ingress NetworkPolicies." This matches review-security-k8s-network line 16 so both reviewers give the same verdict on the same Service.) [conf-3e92ca]

## 9. What we left alone

- **install-kube-agents**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: scripts/installer/installer_common.sh, scripts/installer/README.md
- **review-address-feedback**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: agents/contributor/AGENTS.md, docs/pull-request-workflow.md
- **review-adversarial**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: .claude/commands/pr-review-batch.md, .claude/commands/pr-preflight.md, .github/kube-agents-bot.yml, docs/pull-request-workflow.md, .agents/rules/documentation.md, .agents/rules/pre_pr_review.md...
- **review-docs-drift**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: docs/README.md, .agents/rules/documentation.md, tests/test_docs_map_compact.py, scripts/generate_docs.py
- **review-preflight**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: .claude/commands/pr-preflight.md, .agents/rules/pre_pr_review.md, .claude/commands/pr-review-batch.md
- **upgrade-kube-agents**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: ./upgrade.sh
- **cluster-agent-lifecycle**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: scripts/cluster_agent_profile.py, scripts/cluster_agent_reconcile.py
- **fleet-audit**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: [a-z0-9._-]{0,98}[a-z0-9], cron/jobs.json, governance/compliance_audit_sop.md, .kube-agents/intent.yaml, governance/fleet_consistency_drift_sop.md, governance/security_patch_orchestrator_sop.md...
- **gce-compute-fleet-audit**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: governance/gce_compute_fleet_sop.md
- **gcp-networking-fabric-audit**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: governance/gcp_networking_fabric_sop.md
- **github-issue-resolver**: The inventory flagged these links as broken, but they resolve from the repository root, point into the user's GitOps repository or the agent pod's runtime path, or are placeholders: <issue_url>
- **(101 pairs at 3 stars)**: Pairs scored 3 share a few topics but each has its own core; the scale says they are not findings. The full list is in the coverage matrix appendix.
- **cluster-agent-lifecycle and manage-cluster**: No conflict found: both skills give the identical create command, the same `spec.scope.exclude.clusters` opt-out with `RECONCILE_EXCLUDE` as the one-release fallback, the same `cluster-agent-reconcile` cron covering every project in scope including the management cluster, and the same rule that a profile is not deleted while its cluster exists; the create-step wording differs only in which stamped file each names (`USER.md` versus the `cluster_identity` block in `config.yaml`) and `agents/platform/scripts/cluster_agent_profile.py` writes both, so that is not a disagreement.
- **gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) and gke-workload-scaling (agents/platform/skills/gke-workload-scaling)**: No drift in the shared text: the manual-scale, HPA (--cpu-percent=50 --min=1 --max=10), VPA-enable (--enable-vertical-pod-autoscaling --zone), update-mode (InPlaceOrRecreate, GKE 1.34+), external-metrics and best-practice lines (5 min stabilization window, 2-replica eviction floor, GKE 1.22+ minReplicas override) carry the same flags, thresholds and versions on both sides, and assets/hpa-example.yaml and assets/vpa-example.yaml are byte-identical; the only divergences are scope, not disagreement -- the platform copy (synced from google/skills by scripts/sync-upstream-skills.py, with its capacity-obtainability footer from SKILL_FOOTERS) declares in its frontmatter that it is not for Cluster Autoscaler and adds a rightsizing workflow, while the repo-native cluster copy (agents/cluster/skills is deliberately not synced, per the script's DEFAULT_TARGET_AGENTS comment) adds a Cluster Autoscaler section -- so the pair is left as is, with one observation outside the pair for the owners of the cluster copy: its Cluster Autoscaler section hands a read-only persona a `gcloud container clusters update --enable-autoscaling` command that agents/cluster/SOUL.md line 14 forbids it from running.
- **gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) and gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)**: Everything else that differs is persona scope, not disagreement: the Cluster copy's Step 2 note to query mcp-developer_knowledge first is already imposed on the Platform Agent by agents/platform/SOUL.md section 1 and section 2; the Platform copy's Step 0/Step 4 dry-run fallback and its Step 5 reply-or-PR hand-off (pinned by tests/test_persona_proposal_posture.py) versus the Cluster copy's kanban_complete hand-off are each correct for their own persona; Steps 1-4 commands, log filters, and signature lists are otherwise identical apart from <x> versus {x} placeholders.
- **gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) and gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)**: Steps 1 through 4 (pod status jsonpath, event sort, log --tail=100 and -p, endpoints and networkpolicies commands, and both signature tables) are identical between the two copies apart from placeholder style; the cluster copy's added mcp-developer_knowledge note and dropped dry-run mode are scope, not conflicts. No duplicate finding at 2 stars; the third_party copy is the pinned upstream layer behind agents/platform/skills, not a competitor to the cluster profile copy.
- **review-security-k8s-agents-firewall and review-security-k8s-network**: At 2 stars no duplicate is filed; the remaining differences (firewall's metadata-address rule on ports 80/988 but not 53, network's Ingress TLS, admin ports, hostNetwork and mesh checks, and per-namespace default-deny for ingress as well as egress) are scope, not contradictions.

## 10. How to respond

Each item marked "needs decision" has an ID like `conf-81be44`. Reply with the
ID and your choice, either as a comment on the pull request or by adding a line
to `.sss/decisions.yaml`:

```yaml
dup-3f9a2c: accept
conf-81be44:
  choice: 3
  note: "Both are right in different regions."
```

The next run reads those answers and applies them. Items you have answered are
not asked again.

## Appendix: every skill we found

One entry per skill. "Goal" is what the skill is for, in one line. "Concerns"
lists every finding above that involves it.

### install-kube-agents

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/install-kube-agents`
- **Goal:** Walk an operator through installing kube-agents on a GKE cluster safely, previewing first and applying only after they say yes.
- **Concerns:**
  - out of date [old-53530a]: Add the GitLab forge option to the interview step, the GitOps section and the flag table, stating that the GitHub App and minter apply only…

### review-address-feedback

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-address-feedback`
- **Goal:** Tell an agent how to work through reviewer comments on its own pull request until the PR is ready to merge.
- **Concerns:** none

### review-adversarial

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-adversarial`
- **Goal:** Teach an agent how to find and prove real defects in a code change before reporting them.
- **Concerns:** none

### review-docs-drift

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-docs-drift`
- **Goal:** Catch documentation that a code change has made wrong before the pull request merges.
- **Concerns:** none

### review-preflight

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-preflight`
- **Goal:** Make sure the two required pre-PR reviews run in a context that did not write the code, and combine their results into the PR's Self-Review.
- **Concerns:**
  - out of date [old-10bf86]: Replace "map coverage" with the reachability check that docs-check-links performs today.
  - out of date [old-59686b]: Either point at the AGENTS.md list without enumerating it or add shellcheck, a2a/ and terraform-test to the enumeration.

### review-security-k8s-admission

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-admission`
- **Goal:** Help a reviewer spot ways an admission webhook or admission policy can be bypassed or abused.
- **Concerns:** none

### review-security-k8s-agents-audit-logs

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-audit-logs`
- **Goal:** Checks that an AI agent's actions on Kubernetes are fully logged in a way the agent itself cannot read or erase.
- **Concerns:**
  - out of date [old-af4d83]: Reword the check to name what a GKE user can control: Cloud Audit Logs with Data Access logging enabled for the Kubernetes Engine API, fall…

### review-security-k8s-agents-credentials

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-credentials`
- **Goal:** Checks that an AI agent's pod never holds credentials directly, so a hijacked agent cannot steal them.
- **Concerns:** none

### review-security-k8s-agents-data-exfil

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-data-exfil`
- **Goal:** Checks that an AI agent cannot send cluster data out to the internet if it is tricked by a prompt injection.
- **Concerns:** none

### review-security-k8s-agents-firewall

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-firewall`
- **Goal:** Checks the network rules around an AI agent so it can only talk to the few places it needs and nobody can reach it directly.
- **Concerns:**
  - conflicts with review-security-k8s-network [conf-3e92ca]: The network skill is right: NodePort opens a port on every node and kube-proxy SNATs external traffic to a node IP, so a pod-selector ingre… Decision needed.

### review-security-k8s-agents-main

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-main`
- **Goal:** Runs all the AI-agent security review checklists at once and combines their findings into one report.
- **Concerns:**
  - duplicate with review-security-k8s-main [dup-7e9127]: Keep review-security-k8s-main as the single entry point (it is the superset and already fans out to agents-main), and keep agents-main only… Decision needed.
  - conflicts with review-security-k8s-main [conf-f079bb]: main's wording is right for a skill that can be the top-level runner; agents-main should say the same with a nested-call allowance: use the… Decision needed.

### review-security-k8s-agents-prompt-injection

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-prompt-injection`
- **Goal:** Checks whether an AI agent's front door and its system prompt are protected against injected malicious instructions.
- **Concerns:**
  - low value [low-239222]: Add checks for the controls the architecture doc assigns to this skill: tool output and cluster data treated as untrusted, model output not… Decision needed.

### review-security-k8s-agents-sandbox

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-sandbox`
- **Goal:** Checks that any place an AI agent runs untrusted code is locked down so code cannot break out of it or spread to other workloads.
- **Concerns:** none

### review-security-k8s-gateway

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-gateway`
- **Goal:** Reviews Gateway API traffic routing configs so one team cannot steal or expose another team's traffic.
- **Concerns:** none

### review-security-k8s-main

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-main`
- **Goal:** Runs the full set of Kubernetes security review skills at once and combines their findings into one filtered JSON report.
- **Concerns:**
  - duplicate with review-security-k8s-agents-main [dup-7e9127]: Keep review-security-k8s-main as the single entry point (it is the superset and already fans out to agents-main), and keep agents-main only… Decision needed.
  - conflicts with review-security-k8s-agents-main [conf-f079bb]: main's wording is right for a skill that can be the top-level runner; agents-main should say the same with a nested-call allowance: use the… Decision needed.

### review-security-k8s-namespaces

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-namespaces`
- **Goal:** Checks that namespaces actually separate workloads and tenants instead of being misused or bypassed.
- **Concerns:** none

### review-security-k8s-network

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-network`
- **Goal:** Reviews network rules and service exposure so workloads only talk to what they should and nothing is accidentally reachable from outside.
- **Concerns:**
  - conflicts with review-security-k8s-agents-firewall [conf-3e92ca]: The network skill is right: NodePort opens a port on every node and kube-proxy SNATs external traffic to a node IP, so a pod-selector ingre… Decision needed.

### review-security-k8s-nodes

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-nodes`
- **Goal:** Checks manifests for settings that would let an attacker on one node or pod take over the whole cluster.
- **Concerns:** none

### review-security-k8s-pod

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-pod`
- **Goal:** Checks Pod manifests for settings that would let a container break out of its sandbox or run with more privilege than it needs.
- **Concerns:**
  - out of date [old-9ac7ee]: Rewrite the examples in the form manifests use: SYS_ADMIN, NET_ADMIN, NET_RAW, SYS_MODULE, SYS_PTRACE, DAC_OVERRIDE. Decision needed.

### review-security-k8s-rbac

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-rbac`
- **Goal:** Checks Kubernetes RBAC roles and bindings for grants that are too broad or that let a subject escalate its own privileges.
- **Concerns:** none

### review-security-k8s-service-accounts

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-service-accounts`
- **Goal:** Checks that each workload has its own least-privilege Kubernetes identity and that no identity is shared, orphaned, or backed by a long-lived token.
- **Concerns:** none

### review-security-k8s-storage

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-storage`
- **Goal:** Checks storage and volume settings so data cannot leak between workloads or give a container a path onto the node.
- **Concerns:** none

### review-security-k8s-understand

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-understand`
- **Goal:** Builds a short picture of what a Kubernetes project is and how it is protected, so the detailed security reviewers can judge which findings really matter.
- **Concerns:** none

### skill-review

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/skill-review`
- **Goal:** Reviews a skill file so it stays short, clear, correctly formatted, and discoverable without losing any of its rules.
- **Concerns:** none

### uninstall-kube-agents

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/uninstall-kube-agents`
- **Goal:** Tells an operator how to run the uninstaller so that everything a kube-agents install created in a GCP project and GKE cluster is removed.
- **Concerns:** none

### upgrade-kube-agents

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/upgrade-kube-agents`
- **Goal:** Tells an operator how to move a running kube-agents install to a newer release, or preview what that move would change.
- **Concerns:** none

### a2a-topics

- **Source:** local  **Status:** unmanaged  **Location:** `a2a/persona/platform/skills/a2a-topics`
- **Goal:** Lets the Platform Agent check and record what other agents already know on the shared bus instead of re-diagnosing from scratch.
- **Concerns:** none

### gke-stockout-investigator

- **Source:** local  **Status:** unmanaged  **Location:** `agentplugins/gke-stockout-investigator/files/skills/gke-stockout-investigator`
- **Goal:** When GKE cannot find machines for a workload, this skill diagnoses why and opens a pull request that fixes the ComputeClass or workload config.
- **Concerns:**
  - out of date [old-cd8c4b]: Drop the hard-coded `agents/platform/skills/gke-compute-classes/assets/` hint and keep only the `search_files(pattern="compute-class")` ins… Decision needed.
  - conflicts with capacity-obtainability [conf-f29ced]: capacity-obtainability is right: its wording is the deliberate later edit of the same sentence, the repo's bench cases (obtainability-desig… Decision needed.

### gke-observability (agents/cluster/skills/gke-observability)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-observability`
- **Goal:** Gives the single-cluster agent a checklist for seeing whether a GKE cluster has logging, metrics and tracing set up, and how to turn them on.
- **Concerns:**
  - out of date [old-7a047d]: Replace the flag with `--enable-dataplane-v2-flow-observability` (and mention `--enable-dataplane-v2-metrics`), as the Platform Agent copy…
  - out of date [old-831dba]: Either add `loggingService, monitoringService` to the `--format` projection or tell the agent to read `componentConfig.enableComponents` (e…
  - out of place [place-4e2e1f]: Cut the three `gcloud container clusters update` workflows from this copy and leave it as an audit-only skill, pointing at the Platform Age… Decision needed.
  - duplicate with gke-observability (agents/platform/skills/gke-observability) [dup-a860b1]: Keep the Platform copy: it is the google/skills upstream copy that scripts/sync-upstream-skills.py overwrites on every sync (DEFAULT_TARGET… Decision needed.
  - conflicts with gke-observability (agents/platform/skills/gke-observability) [conf-cc8c8e]: The Platform copy is right: `gcloud container clusters update --help` (installed SDK) lists only `--enable-dataplane-v2-flow-observability`… Decision needed.
  - conflicts with gke-observability (agents/platform/skills/gke-observability) [conf-06309a]: The Platform copy is right for this repo, whose golden path (gke-golden-path assets and the Platform copy's own table) enables the full com… Decision needed.

### gke-reliability (agents/cluster/skills/gke-reliability)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-reliability`
- **Goal:** Gives the single-cluster agent a checklist for judging whether a GKE cluster and its workloads are set up to survive zone, node and pod failures.
- **Concerns:**
  - out of place [place-e2da8c]: Remove workflow 6's update command from this copy and point at the Platform Agent's gke-upgrades skill for maintenance windows. Decision needed.
  - out of date [old-a41048]: If the command stays anywhere, add `--maintenance-window-end <end-time>` (or `--maintenance-window-duration`) to it.
  - duplicate with gke-reliability (agents/platform/skills/gke-reliability) [dup-90a10f]: Keep the platform copy: it is the upstream google/skills copy that scripts/sync-upstream-skills.py overwrites on every sync (no overlay loc… Decision needed.
  - conflicts with gke-reliability (agents/platform/skills/gke-reliability) [conf-2abc8c]: The platform copy is right: maintenance windows are a cluster-setting change owned by gke-upgrades (whose runbook has the complete start/en… Decision needed.
  - conflicts with gke-reliability (agents/platform/skills/gke-reliability) [conf-3e36c1]: The platform copy is right: it is the upstream rule, and k8s-operator/internal/controller/platformagent_manifests.go already treats its rul… Decision needed.
  - conflicts with gke-reliability (agents/platform/skills/gke-reliability) [conf-7e2e10]: The platform copy is right: a replica-count rule is checkable from `kubectl get deploy` and `kubectl get pdb`, while 'critical' is a judgem… Decision needed.
  - conflicts with gke-reliability (agents/platform/skills/gke-reliability) [conf-023f83]: The platform copy is right and more precise (zone spread hard, hostname spread best-effort); drop the '# or ScheduleAnyway' comment from th… Decision needed.

### gke-stall-detection

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-stall-detection`
- **Goal:** Find Kubernetes objects whose controller has silently stopped making progress and report what each one is waiting for.
- **Concerns:** none

### gke-storage (agents/cluster/skills/gke-storage)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-storage`
- **Goal:** Tell an agent which GKE storage driver and StorageClass settings to use and how to grow a volume.
- **Concerns:**
  - out of date [old-2cdfcd]: Change the example's storageClassName to standard-rwx.
  - out of place [place-8f8a24]: Replace the cluster copy with read-only storage diagnostics (PVC/PV phase, StorageClass and CSI driver presence, FailedMount and resize eve… Decision needed.
  - duplicate with gke-storage (agents/platform/skills/gke-storage) [dup-e78aa6]: Keep the platform copy: it is synced from google/skills by scripts/sync-upstream-skills.py (DEFAULT_TARGET_AGENTS = ["platform"]), is the n… Decision needed.
  - conflicts with gke-storage (agents/platform/skills/gke-storage) [conf-111665]: The platform copy is right: GKE's pre-installed Filestore StorageClasses are `standard-rwx` and `premium-rwx` (RWX = ReadWriteMany), and th… Decision needed.
  - conflicts with gke-storage (agents/platform/skills/gke-storage) [conf-813608]: The platform copy is right: `premium-rwo` is a StorageClass GKE pre-installs, so a custom regional class needs its own name, as the platfor… Decision needed.

### gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-workload-scaling`
- **Goal:** Show an agent how to set up manual scaling, HPA, VPA and cluster autoscaling for a GKE workload.
- **Concerns:**
  - out of place [place-ef892a]: Rewrite the cluster copy as read-only scaling diagnostics (HPA and VPA status and conditions, metrics availability, ScalingLimited and Fail… Decision needed.

### gke-workload-security (agents/cluster/skills/gke-workload-security)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-workload-security`
- **Goal:** Help an agent check a GKE cluster's security settings and then turn on the common hardening features.
- **Concerns:**
  - out of date [old-5fefe4]: Replace the cluster update command with the node-pool form, gcloud container node-pools create <pool> --cluster <cluster-name> --sandbox ty… Decision needed.
  - out of place [place-f5e556]: Trim the cluster copy to the audit script and the read-only describe checks, and point hardening steps at the platform copy. Decision needed.
  - duplicate with gke-workload-security (agents/platform/skills/gke-workload-security) [dup-29508a]: Keep the Platform copy: it is the upstream-synced one (scripts/sync-upstream-skills.py syncs google/skills into agents/platform/skills only… Decision needed.
  - conflicts with gke-workload-security (agents/platform/skills/gke-workload-security) [conf-f4805c]: The Platform copy is right that enablement does not belong in this skill (and the Cluster Agent may not mutate anything), but both copies n… Decision needed.
  - conflicts with gke-workload-security (agents/platform/skills/gke-workload-security) [conf-be0048]: The Platform copy is right: Shielded Nodes enablement is a cluster-level write that gke-platform-security already carries (its 'Shielded No… Decision needed.

### gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-workload-troubleshooting`
- **Goal:** Walk an agent step by step from a broken GKE pod to a grounded root cause and a suggested manifest fix.
- **Concerns:**
  - conflicts with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [conf-27f689]: The Platform copy is right that the flag must match the cluster's location type; the Cluster copy should use `--location <cluster_location>… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [conf-3ce3a3]: The Cluster copy is right: the pod's `lastState.terminated.finishedAt` is the moment the failure happened and is the evidence the crashloop… Decision needed.
  - conflicts with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-d08433]: The cluster copy is right (gcloud logging read takes the time bounds as timestamp>= / timestamp<= filter clauses; the repo fixed this in #8… Decision needed.
  - conflicts with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-e5160c]: The cluster copy is right for where it runs: agents/cluster/SOUL.md line 14 and CAPABILITIES.md line 1 make the Cluster Agent read-only and… Decision needed.
  - conflicts with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-133f78]: The cluster copy is right: anchoring the window on the container's last transition is what makes the Step 2 Cloud Logging query find the ev… Decision needed.
  - conflicts with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-a131a6]: The upstream copy is right that the flag depends on the cluster's location type; the cleanest fix for the cluster copy is `--location <clus… Decision needed.

### capacity-obtainability

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/capacity-obtainability`
- **Goal:** Check, with real gcloud evidence, whether the machines a plan needs are both inside quota and actually obtainable, and when a batch job could get them.
- **Concerns:**
  - conflicts with gke-stockout-investigator [conf-f29ced]: capacity-obtainability is right: its wording is the deliberate later edit of the same sentence, the repo's bench cases (obtainability-desig… Decision needed.

### cluster-agent-lifecycle

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/cluster-agent-lifecycle`
- **Goal:** Lets the Platform Agent create, hand work to, and remove the one Cluster Agent that belongs to each managed GKE cluster.
- **Concerns:**
  - duplicate with manage-cluster [dup-5b7877]: Keep `cluster-agent-lifecycle`: it is the superset, it is the newer file (last touched 2026-10-08 against 2026-09-23 for `manage-cluster`),… Decision needed.

### fleet-audit

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/fleet-audit`
- **Goal:** Gives the Platform Agent one scripted way to publish what a scheduled fleet audit found as a single tracked issue and to propose each fix as its own small pull request.
- **Concerns:** none

### fleet-audit-reports

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/fleet-audit-reports`
- **Goal:** Lets the Platform Agent answer 'what did the audit find' questions from saved reports without re-running anything.
- **Concerns:** none

### fleet-upgrade-verification

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/fleet-upgrade-verification`
- **Goal:** Tells the Platform Agent which clusters are behind a target GKE version, what would block their upgrade, and which GitOps manifests use APIs that version removes.
- **Concerns:** none

### gce-compute-fleet-audit

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gce-compute-fleet-audit`
- **Goal:** Lets the Platform Agent audit a project's plain GCE virtual machines, instance groups, sole-tenant nodes and disk snapshots and feed the results into the fleet audit ledger.
- **Concerns:** none

### gcp-config-connector

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gcp-config-connector`
- **Goal:** Lets the Platform Agent change a GKE cluster, node pool, Cloud SQL instance or firewall rule by writing the matching Config Connector YAML and opening a pull request for a human to review.
- **Concerns:** none

### gcp-networking-fabric-audit

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gcp-networking-fabric-audit`
- **Goal:** Scan every GCP project in the fleet for VPC networking problems such as subnets running out of IPs and report them through the fleet audit ledger.
- **Concerns:** none

### github-issue-resolver

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/github-issue-resolver`
- **Goal:** Let the Platform Agent pick up new bug reports from the team's issue tracker, investigate them, and either close them with a write-up or hand them to a human.
- **Concerns:** none

### gke-ai-troubleshooting-handle-disruption-gpu-tpu

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu`
- **Goal:** Figure out whether a GPU or TPU node restart was caused by Google host maintenance and tell the user how to protect the workload next time.
- **Concerns:**
  - out of place [place-5e99d1]: Add a Cluster Agent copy under agents/cluster/skills (as gke-workload-troubleshooting has), keeping the platform copy because the upstream… Decision needed.

### gke-ai-troubleshooting-jobset-interruption

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-ai-troubleshooting-jobset-interruption`
- **Goal:** Walk through metrics and logs to explain why an AI training JobSet keeps restarting, from Spot preemption to a bad host to a crashed coordinator.
- **Concerns:**
  - out of place [place-c420aa]: Add a Cluster Agent copy under agents/cluster/skills (as gke-workload-troubleshooting has), keeping the platform copy because the upstream… Decision needed.

### gke-ai-troubleshooting-tpu-vbar-oom

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom`
- **Goal:** Diagnose a specific TPU v6e crash where the vbar_control_agent process runs out of memory because something polls TPU metrics too often.
- **Concerns:**
  - out of place [place-5ea829]: Add a Cluster Agent copy under agents/cluster/skills (as gke-workload-troubleshooting has), keeping the platform copy because the upstream… Decision needed.

### gke-app-onboarding

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-app-onboarding`
- **Goal:** Help a developer take an application that has never run on GKE, package it in a container, and get it deployed with sensible defaults.
- **Concerns:** none

### gke-backup-dr

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-backup-dr`
- **Goal:** Set up scheduled backups of a GKE cluster's resources and volumes, and restore them safely when something is lost.
- **Concerns:** none

### gke-basics

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-basics`
- **Goal:** Teach the agent the basic GKE rules and which tool to use for everyday cluster tasks before it reaches for a specialised skill.
- **Concerns:**
  - out of date [old-986a59]: Replace --scoped-rbs-bindings with the two --no-enable-insecure-binding-system-* flags. The flag absence is verified (gcloud 587 GA/beta/al… Decision needed.

### gke-batch-hpc

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-batch-hpc`
- **Goal:** Help the agent run large parallel jobs, HPC simulations and training jobs on GKE with queuing and cost controls.
- **Concerns:** none

### gke-cluster-autoscaler

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-cluster-autoscaler`
- **Goal:** Explain why GKE nodes are not scaling up or down and how to tune the autoscaler so they do.
- **Concerns:**
  - out of date [old-1a9274]: Change the pointer in assets/capacity-buffer-serving.yaml to references/ca-capacity-buffers.md (verified: the skill has references/ with ca… Decision needed.

### gke-cluster-creation

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-cluster-creation`
- **Goal:** Walk the agent through creating a new GKE cluster with safe defaults and registering it with a Cluster Agent.
- **Concerns:**
  - out of date [old-09ef08]: Replace --scoped-rbs-bindings in both templates and the best-practice line with the two --no-enable-insecure-binding-system-* flags through… Decision needed.

### gke-compute-classes

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-compute-classes`
- **Goal:** Help the agent write and fix ComputeClass YAML so GKE picks the right machines, with fallbacks, for a workload.
- **Concerns:**
  - out of date [old-b36ef3]: Point the two asset comments at references/compute-class-provisioning-methods.md and ../gke-cluster-autoscaler/references/ca-debug.md (veri… Decision needed.

### gke-cost-analysis

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-cost-analysis`
- **Goal:** Helps the agent explain where GKE spend goes, using billing data and live usage numbers.
- **Concerns:** none

### gke-cost-optimization

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-cost-optimization`
- **Goal:** Tells the agent which concrete changes cut a GKE bill and how to configure them.
- **Concerns:** none

### gke-golden-path

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-golden-path`
- **Goal:** Gives the agent the standard production settings for a GKE Autopilot cluster to design against or audit against.
- **Concerns:**
  - out of date [old-3bbdcd]: Remove the two pointer comments (or ship the export they name) in upstream google/skills, since `scripts/sync-upstream-skills.py` only rewr… Decision needed.

### gke-inference

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-inference`
- **Goal:** Walks the agent through picking hardware and deploying an LLM or other model server on GKE.
- **Concerns:** none

### gke-manifest-generation

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-manifest-generation`
- **Goal:** Makes the agent produce secure, well-formed Kubernetes manifests for GKE instead of ad-hoc YAML.
- **Concerns:** none

### gke-multitenancy

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-multitenancy`
- **Goal:** Shows the agent how to carve one GKE cluster into isolated, quota-bound spaces for several teams.
- **Concerns:** none

### gke-networking

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-networking`
- **Goal:** Helps the Platform Agent design and configure how a GKE cluster's nodes, pods and control plane are addressed and reached on the network.
- **Concerns:** none

### gke-observability (agents/platform/skills/gke-observability)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-observability`
- **Goal:** Helps the Platform Agent turn on and query Cloud Logging, Cloud Monitoring and Managed Prometheus for a GKE cluster and propose alerts.
- **Concerns:**
  - duplicate with gke-observability (agents/cluster/skills/gke-observability) [dup-a860b1]: Keep the Platform copy: it is the google/skills upstream copy that scripts/sync-upstream-skills.py overwrites on every sync (DEFAULT_TARGET… Decision needed.
  - conflicts with gke-observability (agents/cluster/skills/gke-observability) [conf-cc8c8e]: The Platform copy is right: `gcloud container clusters update --help` (installed SDK) lists only `--enable-dataplane-v2-flow-observability`… Decision needed.
  - conflicts with gke-observability (agents/cluster/skills/gke-observability) [conf-06309a]: The Platform copy is right for this repo, whose golden path (gke-golden-path assets and the Platform copy's own table) enables the full com… Decision needed.

### gke-platform-security

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-platform-security`
- **Goal:** Helps the Platform Agent harden a GKE cluster's control plane, nodes, RBAC and IAM roles.
- **Concerns:** none

### gke-productionize

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-productionize`
- **Goal:** Helps the Platform Agent check whether a GKE cluster or app is ready for production by running the specialist skills and scoring each area.
- **Concerns:**
  - out of date [old-146246]: Rename gke-scaling to gke-workload-scaling in the description through a SKILL_SUBSTITUTIONS entry in scripts/sync-upstream-skills.py, since… Decision needed.

### gke-reliability (agents/platform/skills/gke-reliability)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-reliability`
- **Goal:** Helps the Platform Agent make GKE workloads survive node, zone and upgrade disruptions with PDBs, probes, graceful shutdown and pod spreading.
- **Concerns:**
  - duplicate with gke-reliability (agents/cluster/skills/gke-reliability) [dup-90a10f]: Keep the platform copy: it is the upstream google/skills copy that scripts/sync-upstream-skills.py overwrites on every sync (no overlay loc… Decision needed.
  - conflicts with gke-reliability (agents/cluster/skills/gke-reliability) [conf-2abc8c]: The platform copy is right: maintenance windows are a cluster-setting change owned by gke-upgrades (whose runbook has the complete start/en… Decision needed.
  - conflicts with gke-reliability (agents/cluster/skills/gke-reliability) [conf-3e36c1]: The platform copy is right: it is the upstream rule, and k8s-operator/internal/controller/platformagent_manifests.go already treats its rul… Decision needed.
  - conflicts with gke-reliability (agents/cluster/skills/gke-reliability) [conf-7e2e10]: The platform copy is right: a replica-count rule is checkable from `kubectl get deploy` and `kubectl get pdb`, while 'critical' is a judgem… Decision needed.
  - conflicts with gke-reliability (agents/cluster/skills/gke-reliability) [conf-023f83]: The platform copy is right and more precise (zone spread hard, hostname spread best-effort); drop the '# or ScheduleAnyway' comment from th… Decision needed.

### gke-service-networking

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-service-networking`
- **Goal:** Helps the Platform Agent publish a service running on GKE to the internet or another VPC with load balancers, TLS and a WAF.
- **Concerns:**
  - out of date [old-3574a6]: Change both occurrences to `networking.gke.io/certmap` through a SKILL_SUBSTITUTIONS entry in scripts/sync-upstream-skills.py. Decision needed.
  - out of date [old-dbccdf]: State that Standard clusters require `--gateway-api=standard` and Autopilot enables it by default from 1.26, through a SKILL_SUBSTITUTIONS… Decision needed.

### gke-storage (agents/platform/skills/gke-storage)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-storage`
- **Goal:** Helps the agent set up disks, shared file storage and bucket mounts for apps running on a GKE cluster.
- **Concerns:**
  - duplicate with gke-storage (agents/cluster/skills/gke-storage) [dup-e78aa6]: Keep the platform copy: it is synced from google/skills by scripts/sync-upstream-skills.py (DEFAULT_TARGET_AGENTS = ["platform"]), is the n… Decision needed.
  - conflicts with gke-storage (agents/cluster/skills/gke-storage) [conf-111665]: The platform copy is right: GKE's pre-installed Filestore StorageClasses are `standard-rwx` and `premium-rwx` (RWX = ReadWriteMany), and th… Decision needed.
  - conflicts with gke-storage (agents/cluster/skills/gke-storage) [conf-813608]: The platform copy is right: `premium-rwo` is a StorageClass GKE pre-installs, so a custom regional class needs its own name, as the platfor… Decision needed.

### gke-tpu-dynamic-slices-monitoring

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-tpu-dynamic-slices-monitoring`
- **Goal:** Helps the agent find out why a TPU slice is not ready and clean up slices that are stuck.
- **Concerns:**
  - out of date [old-d758bd]: Drop scripts/validate_queries.sh from the skill in upstream google/skills, since scripts/sync-upstream-skills.py overwrites a local removal… Decision needed.

### gke-tpu-metrics-monitoring

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-tpu-metrics-monitoring`
- **Goal:** Helps the agent use Cloud Monitoring metrics to tell whether TPU jobs are slow or interrupted because of the underlying nodes.
- **Concerns:**
  - out of date [old-8dbbf7]: Drop scripts/validate_queries.sh from the skill in upstream google/skills, since scripts/sync-upstream-skills.py overwrites a local removal… Decision needed.

### gke-upgrades

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-upgrades`
- **Goal:** Helps the agent plan, carry out and unstick GKE version upgrades and maintenance windows safely.
- **Concerns:** none

### gke-workload-scaling (agents/platform/skills/gke-workload-scaling)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-workload-scaling`
- **Goal:** Helps the agent set up automatic pod scaling and right-size CPU and memory requests for an app on GKE.
- **Concerns:** none

### gke-workload-security (agents/platform/skills/gke-workload-security)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-workload-security`
- **Goal:** Helps the agent check and tighten the security of apps on a GKE cluster: identity, network isolation, sandboxing, pod policies and secrets.
- **Concerns:**
  - duplicate with gke-workload-security (agents/cluster/skills/gke-workload-security) [dup-29508a]: Keep the Platform copy: it is the upstream-synced one (scripts/sync-upstream-skills.py syncs google/skills into agents/platform/skills only… Decision needed.
  - conflicts with gke-workload-security (agents/cluster/skills/gke-workload-security) [conf-f4805c]: The Platform copy is right that enablement does not belong in this skill (and the Cluster Agent may not mutate anything), but both copies n… Decision needed.
  - conflicts with gke-workload-security (agents/cluster/skills/gke-workload-security) [conf-be0048]: The Platform copy is right: Shielded Nodes enablement is a cluster-level write that gke-platform-security already carries (its 'Shielded No… Decision needed.

### gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-workload-troubleshooting`
- **Goal:** Walk an agent through finding out why a pod on a GKE cluster is crashing or stuck, and drafting the manifest change that fixes it.
- **Concerns:**
  - duplicate with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [dup-7c8050]: Keep agents/platform/skills/gke-workload-troubleshooting as the skill: it is the generated copy the platform image ships (deploy/docker/Doc…
  - conflicts with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-af4023]: The platform copy is right: `gcloud logging read` takes the time window as `timestamp>=`/`timestamp<=` terms inside the filter, not as flag… Decision needed.
  - conflicts with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-87efa5]: The platform copy is right for this repository: agents/platform/SOUL.md section 3 item 3 (line 118) says a pull request is opened only when… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) [conf-27f689]: The Platform copy is right that the flag must match the cluster's location type; the Cluster copy should use `--location <cluster_location>… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) [conf-3ce3a3]: The Cluster copy is right: the pod's `lastState.terminated.finishedAt` is the moment the failure happened and is the evidence the crashloop… Decision needed.

### inspect-repository

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/inspect-repository`
- **Goal:** Let the agent read code from a repository it has no checkout of, without being able to change it.
- **Concerns:** none

### kube-agents-observability

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/kube-agents-observability`
- **Goal:** Help an agent check whether the kube-agents pods themselves are logging, emitting metrics and traces, and serving their API and dashboard.
- **Concerns:**
  - out of date [old-659b7e]: Replace the annotation check with `kubectl get podmonitoring -n kubeagents-system` and a check that its selector matches the gateway pod la… Decision needed.

### manage-cluster

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/manage-cluster`
- **Goal:** Give an existing GKE cluster its own read-only Cluster Agent right away when a user asks, instead of waiting for the hourly sweep.
- **Concerns:**
  - duplicate with cluster-agent-lifecycle [dup-5b7877]: Keep `cluster-agent-lifecycle`: it is the superset, it is the newer file (last touched 2026-10-08 against 2026-09-23 for `manage-cluster`),… Decision needed.

### pr-conversation

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/pr-conversation`
- **Goal:** Let the agent answer review comments on its own pull requests, fix the branch when asked, and record that it has replied.
- **Concerns:** none

### submit-suggestion

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/submit-suggestion`
- **Goal:** Let the agent propose a configuration change as a pull request for a human to review, instead of changing anything directly.
- **Concerns:** none

### version-control

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/version-control`
- **Goal:** Lets the Platform Agent read, change, and open pull requests or issues on a managed repository through one forge-neutral script instead of `gh` or raw `git push`.
- **Concerns:** none

### workload-rebalancing

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/workload-rebalancing`
- **Goal:** Tells the Platform Agent how to safely move a workload between two clusters by having each cluster check feasibility first and then opening one pull request for the move.
- **Concerns:** none

### gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-workload-troubleshooting`
- **Goal:** Holds the untouched upstream Google copy of the GKE workload troubleshooting skill so the repo can re-apply its own patches on top whenever upstream changes.
- **Concerns:**
  - duplicate with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [dup-7c8050]: Keep agents/platform/skills/gke-workload-troubleshooting as the skill: it is the generated copy the platform image ships (deploy/docker/Doc…
  - conflicts with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [conf-af4023]: The platform copy is right: `gcloud logging read` takes the time window as `timestamp>=`/`timestamp<=` terms inside the filter, not as flag… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [conf-87efa5]: The platform copy is right for this repository: agents/platform/SOUL.md section 3 item 3 (line 118) says a pull request is opened only when… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) [conf-d08433]: The cluster copy is right (gcloud logging read takes the time bounds as timestamp>= / timestamp<= filter clauses; the repo fixed this in #8… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) [conf-e5160c]: The cluster copy is right for where it runs: agents/cluster/SOUL.md line 14 and CAPABILITIES.md line 1 make the Cluster Agent read-only and… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) [conf-133f78]: The cluster copy is right: anchoring the window on the container's last transition is what makes the Step 2 Cloud Logging query find the ev… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) [conf-a131a6]: The upstream copy is right that the flag depends on the cluster's location type; the cleanest fix for the cluster copy is `--location <clus… Decision needed.

## Appendix: coverage matrix

Every skill was compared with every other skill and scored by how much they
cover the same ground.

Legend: 0 = same, 1 = subset, 2 = large overlap, 3 = some overlap, 4 = related, 5 = distinct, · = not scored yet.

| Skill | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 | S24 | S25 | S26 | S27 | S28 | S29 | S30 | S31 | S32 | S33 | S34 | S35 | S36 | S37 | S38 | S39 | S40 | S41 | S42 | S43 | S44 | S45 | S46 | S47 | S48 | S49 | S50 | S51 | S52 | S53 | S54 | S55 | S56 | S57 | S58 | S59 | S60 | S61 | S62 | S63 | S64 | S65 | S66 | S67 | S68 | S69 | S70 | S71 | S72 | S73 | S74 | S75 | S76 | S77 | S78 | S79 | S80 | S81 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **S1** a2a-topics | — | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S2** capacity-obtainability | 5 | — | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 3 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S3** cluster-agent-lifecycle | 4 | 5 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 1 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 |
| **S4** fleet-audit | 4 | 4 | 4 | — | 3 | 3 | 3 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 5 |
| **S5** fleet-audit-reports | 4 | 5 | 5 | 3 | — | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S6** fleet-upgrade-verification | 4 | 5 | 5 | 3 | 4 | — | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S7** gce-compute-fleet-audit | 5 | 4 | 5 | 3 | 4 | 4 | — | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 |
| **S8** gcp-config-connector | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 3 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 |
| **S9** gcp-networking-fabric-audit | 5 | 5 | 5 | 3 | 4 | 4 | 4 | 4 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S10** github-issue-resolver | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 5 |
| **S11** gke-ai-troubleshooting-handle-disruption-gpu-tpu | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 3 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 3 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S12** gke-ai-troubleshooting-jobset-interruption | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | — | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S13** gke-ai-troubleshooting-tpu-vbar-oom | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S14** gke-app-onboarding | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 5 | 3 | 4 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S15** gke-backup-dr | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S16** gke-basics | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | — | 5 | 4 | 3 | 4 | 4 | 5 | 3 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S17** gke-batch-hpc | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 4 | 5 | 5 | — | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S18** gke-cluster-autoscaler | 5 | 3 | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | — | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 4 | 3 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S19** gke-cluster-creation | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | — | 4 | 5 | 4 | 3 | 4 | 5 | 5 | 3 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S20** gke-compute-classes | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 3 | 4 | — | 5 | 3 | 4 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S21** gke-cost-analysis | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | — | 3 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S22** gke-cost-optimization | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 4 | 4 | 3 | 3 | — | 4 | 4 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S23** gke-golden-path | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 4 | 5 | 4 | — | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S24** gke-inference | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 5 | 4 | 4 | — | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S25** gke-manifest-generation | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 3 | — | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S26** gke-multitenancy | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 3 | 4 | 5 | 4 | — | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S27** gke-networking | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 4 | 3 | 5 | 5 | 5 | 3 | 5 | 4 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S28** gke-observability (agents/cluster/skills/gke-observability) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | — | 1 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S29** gke-observability (agents/platform/skills/gke-observability) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 4 | 1 | — | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S30** gke-platform-security | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 3 | 5 | 4 | 4 | 4 | 4 | 4 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S31** gke-productionize | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S32** gke-reliability (agents/cluster/skills/gke-reliability) | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 | 3 | — | 1 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S33** gke-reliability (agents/platform/skills/gke-reliability) | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 | 3 | 1 | — | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S34** gke-service-networking | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S35** gke-stall-detection | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | — | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S36** gke-stockout-investigator | 5 | 2 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | — | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 |
| **S37** gke-storage (agents/cluster/skills/gke-storage) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | — | 1 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S38** gke-storage (agents/platform/skills/gke-storage) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 1 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S39** gke-tpu-dynamic-slices-monitoring | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | — | 3 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S40** gke-tpu-metrics-monitoring | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 3 | — | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S41** gke-upgrades | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S42** gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 3 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | — | 2 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S43** gke-workload-scaling (agents/platform/skills/gke-workload-scaling) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 2 | — | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S44** gke-workload-security (agents/cluster/skills/gke-workload-security) | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 5 | 3 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | — | 1 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S45** gke-workload-security (agents/platform/skills/gke-workload-security) | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 5 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 1 | — | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S46** gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 2 | 2 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 |
| **S47** gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2 | — | 1 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 |
| **S48** gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 1 | — | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 |
| **S49** inspect-repository | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 5 |
| **S50** install-kube-agents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 |
| **S51** kube-agents-observability | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 |
| **S52** manage-cluster | 5 | 5 | 1 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 |
| **S53** pr-conversation | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | — | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 5 |
| **S54** review-address-feedback | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | — | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 5 |
| **S55** review-adversarial | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | — | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 |
| **S56** review-docs-drift | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 |
| **S57** review-preflight | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | — | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 |
| **S58** review-security-k8s-admission | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | — | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S59** review-security-k8s-agents-audit-logs | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S60** review-security-k8s-agents-credentials | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S61** review-security-k8s-agents-data-exfil | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | — | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S62** review-security-k8s-agents-firewall | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 3 | — | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S63** review-security-k8s-agents-main | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | — | 3 | 3 | 4 | 1 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S64** review-security-k8s-agents-prompt-injection | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S65** review-security-k8s-agents-sandbox | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 4 | — | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S66** review-security-k8s-gateway | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S67** review-security-k8s-main | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 1 | 4 | 4 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S68** review-security-k8s-namespaces | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S69** review-security-k8s-network | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 2 | 4 | 4 | 4 | 3 | 4 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S70** review-security-k8s-nodes | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S71** review-security-k8s-pod | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | — | 4 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S72** review-security-k8s-rbac | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | — | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S73** review-security-k8s-service-accounts | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | — | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S74** review-security-k8s-storage | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S75** review-security-k8s-understand | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 5 | 5 | 5 | 5 | 5 | 5 |
| **S76** skill-review | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 5 | 5 | 5 | 5 | 5 |
| **S77** submit-suggestion | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 5 | 5 | 3 | 4 |
| **S78** uninstall-kube-agents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 4 | 5 | 5 |
| **S79** upgrade-kube-agents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | — | 5 | 5 |
| **S80** version-control | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | — | 5 |
| **S81** workload-rebalancing | 4 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | — |

Coverage summaries:

- **S1 a2a-topics**: Platform Agent skill (shipped only on a `next`-mode install with the A2A bus) for the `a2a topics list|read|write` CLI: discover provisioned topics and their class (state vs journal), read standing state such as `upgrade-readiness` while relaying provenance and treating exit 2 as 'empty', write topics the profile owns with `--text`/`--data` and task/context/correlation ids, and append dated findings to the shared `annotations` journal. Read and write, fleet-level shared state. It explicitly excludes task status (stream replay), private memory, scratch notes, topics not in `a2a topics list`, and installs without `NATS_URL` or where the shell sandbox has no `a2a` binary.
- **S2 capacity-obtainability**: Platform Agent, read-only diagnosis and design, project and region scope rather than one cluster. Checks regional quota (gcloud compute regions describe), reservations, live node and pod usage (kubectl top), Spot and Flex-Start obtainability (gcloud beta compute advice capacity, capacity-history) across zones, and future reservation windows for deadline-bound TPU or VM batch jobs (gcloud beta compute advice calendar-mode); records each check with record_evidence (or an Evidence section when the tool is absent), attaches ComputeClass, NAP, ProvisioningRequest and Kueue LocalQueue manifests with attach_artifact, requires a three-path On-Demand/Spot/Flex-Start report, and lists eight ComputeClass resilience rules (fallbacks, large shapes, disk generation mix, On-Demand floor, regional scarcity, quota exceeded, priority starvation, Hyperdisk compatibility). It explicitly excludes creating clusters, applying manifests, opening PRs and handling inbound stockout alerts, which it sends to the gke-stockout-investigator plugin skill.
- **S3 cluster-agent-lifecycle**: Platform Agent skill for the lifecycle of per-cluster Cluster Agent Hermes profiles: create one at cluster onboarding and delete one at teardown with agents/platform/scripts/cluster_agent_profile.py (create/delete, --project --cluster --location), resolve a profile with the get_cluster_profile_name and list_cluster_profiles tools, and delegate any single-cluster runtime debugging task (crash loops, OOMs, scheduling, mounts, connectivity, autoscaling, storage) to that profile through a kanban card (kanban_create, kanban_show, kanban_complete), including a multi-cluster fan-out pattern. It also describes the hourly cluster-agent-reconcile cron job (cluster_agent_reconcile.py, --dry-run, --require-create-pass) that creates and prunes profiles across every project in scope, with its fleet_scope.json snapshot and two-clean-run prune rule. It writes profiles on the data PVC but is read-only against clusters; it explicitly excludes debugging tenant workloads directly, opening pull requests (that is submit-suggestion), and repairing the roster from other work.
- **S4 fleet-audit**: Platform Agent skill that turns the findings of the nine autonomous fleet audit streams into one continuously rewritten ledger issue per stream on the GitOps repository's forge (GitHub or GitLab) and into narrow remediation pull requests, through audit_report.py (start, finish, draft, list, grep, fetch, remediate). The streams it covers are compliance-audit (security and RBAC posture), security-patch-orchestrator (upgrade and patch readiness), obtainability-audit (workload reliability), fleet-wide-cost-analysis (fleet waste), fleet-consistency-drift, ai-security-audit (AI workload security), stockout-prevention (capacity), gcp-networking-fabric-audit (VPC and IPAM) and gce-compute-fleet-audit (GCE VMs and MIGs); the folder ships the collectors collect.py (compliance, obtainability, AI security), fleet_drift.py, fleet_waste.py, fleet_stockout.py and patch_readiness.py, plus the report store reader report_status.py. It defines the findings.json contract (scope.clusters with checks_run per check, checks_not_applicable, limitations, skipped, findings with evidence and a three-part recommendation, declared postures, resolved_because), the collector-manifest cross-check, partial and held runs, the silent_ok rule, the /remediate protocol, and the three request forms (run a stream per its SOP as a worker, trigger the cron job with hermes cron run, or answer from past reports). The agent is read-only against clusters and GCP; all git and forge writes are the script's. It explicitly excludes hand-written issues, bodies or timestamps, opening a second ledger, reopening merged PRs, deleting branches, running the audit inline when asked to trigger the cron job, and answering questions about past runs (that is fleet-audit-reports).
- **S5 fleet-audit-reports**: Platform Agent skill for answering questions about past fleet audit runs from the on-pod report store at /opt/data/fleet-audit/reports/<audit-id>/<owner>/<name>/ (latest.json plus a 14-run ring), using report_query.py subcommands streams, show, findings, finding, checks, diff and runs, with --repo, --run, --severity, --cluster, --check and --limit filters. It covers what a stream last found, open critical counts, what changed between two runs, which clusters were skipped or partly covered, held-open and partial ledgers, and when each stream last ran (liveness never/completed/running/died/error). Read-only, fleet-wide, no cluster or forge access. It explicitly excludes running, publishing or remediating an audit (fleet-audit owns those), opening store files directly, acting on a running or died lease, and treating a missing or unreadable record as a clean fleet.
- **S6 fleet-upgrade-verification**: Platform Agent skill that reports every GKE cluster's control-plane and lowest node-pool version against a target version or the cluster's release-channel default (fleet_upgrade_report.py: --project, --target-version, --output, --state-dir, --rollout-in-progress, --readiness, --at, --kubeconfig-dir), grading members lagging/patch-behind/current/ahead/unknown, tracking rollout progress across runs (completed/started/unchanged/stalled/new) from a record under /opt/data/state/fleet-upgrade-verification/, and with --readiness grading drain-blocking PodDisruptionBudgets, maintenance exclusions and windows, and node-pool skew. A second script, api_deprecation_scan.py (--versions, --target-version, --repo, --manifests-dir, --lease, --output), scans the managed GitOps repositories for apiVersions the target removes, from a removed_apis.json table covering Kubernetes 1.16 through 1.32. Read-only against GCP (gcloud container clusters list, get-server-config, get-credentials), clusters (one kubectl get per member) and Git, fleet-wide. It explicitly excludes upgrade plans and runbooks (gke-upgrades), configuration drift, running the upgrade or the manifest migrations, rendering Helm or Kustomize, deleting exclusions, running gcloud recommender insights, and citing CVE identifiers.
- **S7 gce-compute-fleet-audit**: Platform Agent skill for the gce-compute-fleet-audit stream: run the collector compute_fleet_audit.py (optional --project-id and --output) over the target GCP projects with gcloud compute reads, then evaluate its manifest against governance/gce_compute_fleet_sop.md and hand the result to the fleet-audit harness with start and finish --manifest-file. Its four collector-verified checks are gce-startup-script-status (serial console boot and startup-script failures), mig-convergence-stalled (MIG resize loops), sole-tenant-headroom (node groups at capacity) and orphaned-snapshots (snapshots of deleted disks older than 90 days). Read-only, project-scoped rather than cluster-scoped, fleet-wide. It explicitly excludes ops-agent-guest-health, which is off the roster, and hand-running any check.
- **S8 gcp-config-connector**: Platform Agent skill that authors Config Connector (KCC) v1beta1 manifests for Google Cloud resource changes and submits them as a pull request through submit-suggestion (prepare and submit on branch platform-agent/kcc-<kind>-<name>) under clusters/<cluster>/provisioning/. It covers ContainerCluster and ContainerNodePool changes (grow, autoscale, release channel, adopt), SQLInstance changes (read replica, tier, backups), and ComputeFirewall rules, with a read-only create/acquire/edit decision from kubectl get, kubectl auth can-i and gcloud describe, mandatory deletion-policy: abandon and state-into-spec: absent annotations, immutable-field catalogues per kind in references/, and validation with kubectl explain. GitOps-write via PR only; never applies. It explicitly excludes Kubernetes workload manifests (gke-manifest-generation), imperative cluster creation (gke-cluster-creation), Terraform HCL repositories, kinds outside the catalogued families, fixing fleet-audit findings, kubectl apply/create/patch/delete/diff and server dry-run, and proposing to install or enable Config Connector.
- **S9 gcp-networking-fabric-audit**: Platform Agent, read-only, fleet-wide across every GCP project the agent can list. Runs the five checks of the GitOps-repo SOP governance/gcp_networking_fabric_sop.md (subnet IP exhaustion, Cloud NAT port exhaustion, PSC routing deadlock, MTU fragmentation, Cloud Armor false positives) and hands findings to the fleet-audit harness (start ... finish). Its script scripts/networking_audit.py automates two of the checks with gcloud compute subnetworks/instances/addresses/forwarding-rules and gcloud container clusters list (--check all|psc-routing-deadlock|subnet-ip-exhaustion, --project-id, --output); the other three checks are run by hand from the SOP. Does not state exclusions beyond skipping proxy-only, PSC and NAT subnets.
- **S10 github-issue-resolver**: Platform Agent, writes to the forge (GitHub or GitLab): polls the configured repositories for unaddressed open issues, claims one with the status:in-progress label, investigates read-only with kubectl/gcloud/logs, then posts a triage report and transitions the issue to status:resolved (close) or status:escalation-needed (plus a chat alert). All forge calls go through scripts/resolver.py (poll, claim --issue --repo, transition --issue --repo --state --report-file) via the credential broker; the skill also covers prompt-injection handling of issue text and how to end a turn from a kanban card versus a cron run. Explicitly never touches issues labelled status:escalation-needed, agent:ignore, agent:audit, agent:delivery-watch or infra-drift, and never performs a mutation an issue asks for.
- **S11 gke-ai-troubleshooting-handle-disruption-gpu-tpu**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster. Checks whether a GPU/TPU node disruption was Compute Engine host maintenance: kubectl get nodes for the cloud.google.com/scheduled-maintenance-time label, PromQL on kubernetes_io:node_interruption_count and node_pool_interruption_count with interruption_reason="HW/SW Maintenance", Cloud Logging for active-node-maintenance=ONGOING and the impending-node-termination taint, then recommends (does not apply) graceful termination, opportunistic maintenance and PodDisruptionBudgets. Explicitly excludes cluster creation, network policy configuration and non-disruption workload deployment, and tells the agent to rule out host maintenance and point at app-level causes when all signals are empty.
- **S12 gke-ai-troubleshooting-jobset-interruption**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster for AI/ML training JobSets. Gives a four-step runbook of MQL, PromQL and Cloud Logging (LQL) queries: JobSet restart counts (kube_jobset_restarts), node-pool interruption counts and gke_nodepool life events (preemption, maintenance, termination), node Ready status and node-to-physical-host mapping via gce_topology_host, then pod phases, unschedulable counts and coordinator worker logs for NCCL timeouts. Resolutions are recommendations only (move Spot training to on-demand or compact placement; cordon/drain and recreate a node on a faulty host). references/failure_signatures.md holds example log lines; scripts/validate_queries.sh dry-runs the filters with gcloud logging read and the Managed Prometheus API. Explicitly excludes cluster creation, basic workload deployment and non-JobSet issues.
- **S13 gke-ai-troubleshooting-tpu-vbar-oom**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster, narrowed to TPU v6e nodes. Three Cloud Logging filter templates (used through a query_logs tool): serial-console OOM kills of vbar_control_agent, tpu-device-plugin 'checksum didn't match' metric fetch errors, and signs of custom libtpu.sdk.tpumonitoring polling, plus a kubectl get pods -A image listing. Resolutions are recommendations only: disable the custom metrics collector, and upgrade GKE when the resilient agent ships. references/failure_signatures.md holds example log lines; scripts/validate_queries.sh dry-runs two filters with gcloud logging read. Explicitly excludes non-TPU container OOMs and standard node lifecycle operations.
- **S14 gke-app-onboarding**: Upstream google/skills copy under the Platform Agent; a write path for one cluster. Covers first-time onboarding of an application to GKE: assess the app, write a Dockerfile (or use Cloud Native Buildpacks), build and push to Artifact Registry (gcloud auth configure-docker, docker build/push, gcloud artifacts docker images describe --show-package-vulnerability), generate a Deployment plus ClusterIP Service manifest with probes and resource limits, then deploy with the GKE MCP tools apply_k8s_manifest / get_k8s_rollout_status / get_k8s_resource or kubectl apply as fallback. assets/ holds a sample Node.js app (Dockerfile, index.js, package.json) and a hardened deployment.yaml that SKILL.md itself does not reference. Explicitly excludes general cluster administration and upgrades, pointing to gke-basics and gke-upgrades, and defers autoscaling, observability, security and reliability to other gke-* skills.
- **S15 gke-backup-dr**: Platform Agent skill for Backup for GKE. It gives the gcloud beta container backup-restore commands to enable the BackupRestore addon, create backup plans (with --include-volume-data, --include-secrets, retention, cron or RPO schedules, CMEK), trigger manual backups, create restore plans and run and verify restores. It is a write skill on one GKE cluster at a time, with restore-safety rules on conflict policies and a rule to confirm before restoring into production. It explicitly does not cover database backups and does not cover the broader Google Cloud Backup and DR service.
- **S16 gke-basics**: Platform Agent entry skill for core GKE work: choosing Autopilot vs Standard, private-cluster flags, Workload Identity annotation, Autopilot CPU rounding, and fetching cluster credentials into a per-target KUBECONFIG. The references add a tool-preference order (Developer Knowledge MCP for facts; GKE MCP tools, then gcloud, then kubectl for cluster operations), a table of 23 GKE MCP tools with gcloud and kubectl fallbacks for cluster, node pool, resource, log and operation actions, Terraform and client-library snippets, and an error table. It covers both read and write actions on single clusters. It explicitly excludes GKE networking (gke-networking), security hardening (gke-platform-security, gke-workload-security) and upgrades (gke-upgrades), and points to gke-cluster-creation for cluster architecture.
- **S17 gke-batch-hpc**: Platform Agent skill for running batch and HPC work on GKE. It gives manifests for Kubernetes Jobs, JobSet, Kueue ClusterQueue and LocalQueue, and Kubeflow MPIJob, the kubectl install lines for Kueue and the MPI Operator, a gcloud node-pools create command for compact placement on Standard clusters, and cost rules (Spot via ComputeClass, scale-to-zero, backoffLimit, checkpointing, maintenance exclusions). It writes workloads into a single cluster. A local footer requires loading capacity-obtainability before scheduling GPU/TPU jobs with a deadline. It explicitly excludes standard web application deployments (gke-app-onboarding) and defers Spot-fallback YAML to gke-compute-classes.
- **S18 gke-cluster-autoscaler**: Platform Agent skill for the GKE Cluster Autoscaler, Node Auto Provisioning and node pool auto-creation. It covers enabling autoscaling (gcloud node-pools and clusters update flags), tuning (autoscaling profiles, location policy, consolidation delay), reading cluster-autoscaler-visibility logs, and diagnosing scale-up failures (stockouts, quota, IP exhaustion, cooldown cascade) and scale-down blockers, with two scripts (log-autoscaler-events.sh tails Cloud Logging; find-scale-down-blockers.sh scans pods, PDBs and nodes with kubectl) and a CapacityBuffer example. It mixes read-only diagnosis with cluster-level write commands on a single cluster. It explicitly defers ComputeClass YAML, schemas and priority configuration to gke-compute-classes.
- **S19 gke-cluster-creation**: Platform Agent provisioning skill that creates GKE clusters from five templates (golden-path Autopilot, Autopilot dev/test, Standard regional, L4 GPU inference, A3 Hypercompute), each as a gcloud command and a create_cluster MCP payload, with a workflow (discover, gather inputs, choose mode, confirm, create, track with get_operation, verify with get_cluster) and rules to warn about Standard mode, Day-0 choices, cost and quota. Local footers require creating the Cluster Agent profile (python3 /opt/data/scripts/cluster_agent_profile.py create) right after creation, deleting it at teardown, and loading capacity-obtainability before recommending GPU/TPU capacity. It is a write skill at project scope. It explicitly excludes application onboarding and deployment configuration (gke-app-onboarding).
- **S20 gke-compute-classes**: Platform Agent skill for authoring, tuning and debugging GKE ComputeClass objects: priorities with Spot, reservation, DWS FlexStart and On-Demand fallbacks, GPU and TPU targeting, machine families, location policy, activeMigration and consolidation, the dynamic-rwo StorageClass for stateful PVs, Autopilot mode on Standard clusters, Karpenter migration, and access control via RBAC plus a ValidatingAdmissionPolicy. It ships fifteen example YAML assets (labelled EXAMPLE TEMPLATE - DO NOT DEPLOY), ten reference files and a copy of log-autoscaler-events.sh identical to the one in gke-cluster-autoscaler. It writes cluster-scoped CRDs on a single cluster. It explicitly excludes cluster-level Node Auto Provisioning configuration and general cluster creation.
- **S21 gke-cost-analysis**: Platform Agent skill (agents/platform/skills, upstream google/skills copy) for answering GKE cost questions. It covers BigQuery billing-export queries with `bq query` (per-workload, per-cluster, per-namespace cost, net vs gross credits), checking that GKE Cost Allocation is enabled, `gcloud billing budgets list`, and live `kubectl top nodes/pods` to compare usage with requests; it explains Autopilot (per-pod-request) vs Standard (per-VM plus management fee) pricing. Scope spans projects and clusters (fleet-wide billing data) and is read-only apart from one `gcloud container clusters update --enable-cost-allocation` snippet; it explicitly excludes applying optimizations, VPA/MPA rightsizing manifests, and ComputeClass selection (deferred to gke-cost-optimization).
- **S22 gke-cost-optimization**: Platform Agent skill (upstream google/skills copy) for reducing GKE cost once waste is known. It covers ResourceQuota manifests, VPA in recommendation mode (`updateMode: Off`) with a P95*1.2 rightsizing rule and MPA, Spot VMs via a `ComputeClass` with fallback or the Autopilot `cloud.google.com/gke-provisioning: Spot` nodeSelector, a machine-family cost table, Committed Use Discounts, stopping idle dev clusters, and dev/test deviations from the golden path. Write-oriented (its examples use `kubectl apply`, which this install routes through the GitOps PR path), single cluster or namespace at a time; it explicitly excludes general ComputeClass provisioning and GPU selection (gke-compute-classes) and billing analysis (gke-cost-analysis).
- **S23 gke-golden-path**: Platform Agent skill (upstream google/skills copy) holding the recommended Autopilot cluster configuration. It lists always-apply defaults (private nodes, Workload Identity, ADVANCED_DATAPATH, Cloud DNS, OPTIMIZE_UTILIZATION, VPA, monitoring/logging components, Secret Manager rotation), customer-configurable settings (DNS endpoint, IPAM, maxPodsPerNode, boot disk, maintenance exclusions), Day-0 vs Day-1 rules, guardrails for auditing an existing cluster against the baseline, and a condensed `assets/golden-path-autopilot.yaml`. It names the `get_cluster`/`create_cluster`/`update_cluster` MCP tools and is a design and audit reference for one cluster at a time; it explicitly excludes workload autoscaling (gke-workload-scaling).
- **S24 gke-inference**: Platform Agent skill (upstream google/skills copy) for serving AI/ML models on GKE. It covers the GKE Inference Quickstart CLI (`gcloud container ai profiles models list`, `profiles list --model`, `profiles manifests create` with `--model-server`, `--accelerator-type`, `--target-ntpot-milliseconds`), reviewing and deploying the generated manifest with `kubectl apply`, a GPU `ComputeClass` for Autopilot, an accelerator selection table (T4 through GB200 and TPU v5e-v7x), an HPA on GPU metrics, vLLM tuning tips, and a troubleshooting table. Single-cluster, write-oriented deployment guidance; it explicitly excludes generic batch and HPC work (gke-batch-hpc).
- **S25 gke-manifest-generation**: Platform Agent skill (upstream google/skills copy with repo-specific substitutions) for writing or editing Kubernetes YAML for GKE Autopilot and Standard. It mandates explicit namespaces, dedicated ServiceAccounts, requests/limits, Spot nodeSelector plus toleration for non-prod, Pod Security Standards hardening, liveness/readiness/startup probes, ClusterIP and Gateway API over Ingress, subPath and StorageClass rules, anti-affinity and PDBs, and stable list keys for server-side apply; references hold full examples for a hardened Nginx Deployment, NetworkPolicy, a vLLM GPU workload with GCS FUSE, and Gateway/HTTPRoute. It directs inference manifests to `gcloud container ai profiles manifests create` on stdout and grounding lookups to `search_documents`/`get_documents`; it is authoring-only (no cluster operations) and explicitly excludes troubleshooting (gke-workload-troubleshooting), cluster provisioning (gke-cluster-creation), and Config Connector manifests (gcp-config-connector).
- **S26 gke-multitenancy**: Platform Agent skill (upstream google/skills copy) for sharing one GKE cluster between teams or environments. It compares namespace-per-team, namespace-per-environment, node-pool-per-team and cluster-per-team models, then gives manifests for namespaces and labels, namespace-scoped Role/RoleBinding to Google Groups, ResourceQuota, LimitRange (with the rule that min/max need defaults), a same-namespace-plus-DNS NetworkPolicy, cost-center labels and `--enable-cost-allocation`. Single-cluster, write-oriented (`kubectl create/label/apply`, `gcloud container clusters update`); it explicitly excludes single-tenant cluster configuration and general deployment steps (gke-basics, gke-app-onboarding) and defers RBAC hardening and default-deny policy to gke-platform-security and gke-workload-security.
- **S27 gke-networking**: Platform Agent reference for core GKE cluster networking, read and write at the cluster level: golden-path settings for private nodes, private endpoint enforcement, DNS endpoint access, Dataplane V2, Cloud DNS, Auto IPAM and max pods per node; get-credentials via --dns-endpoint or --internal-ip; create-auto with a bring-your-own VPC and subnet; Pod and Service CIDR sizing; Cloud NAT egress; and a local footer that checks controlPlaneEndpointsConfig before passing --dns-endpoint and points at /opt/data/scripts/gke_endpoint.py. Uses MCP get_cluster, update_cluster, apply_k8s_manifest, get_k8s_resource plus gcloud. Explicitly excludes application ingress, load balancing and service networking (gke-service-networking) and defers NetworkPolicy manifests to gke-workload-security and gke-multitenancy.
- **S28 gke-observability (agents/cluster/skills/gke-observability)**: Cluster Agent skill with nine short workflows on one GKE cluster: audit logging/monitoring config with `gcloud container clusters describe`, enable Managed Service for Prometheus, check workload logs with `kubectl logs`, recommend dashboards/alerts, OpenTelemetry tracing and Cloud Profiler, two LQL query examples, enable control-plane metrics, and enable Dataplane V2 observability. Three of the workflows are `gcloud container clusters update` writes; the rest are read-only or advisory. It does not state exclusions. A separate, longer `gke-observability` skill exists under agents/platform/skills.
- **S29 gke-observability (agents/platform/skills/gke-observability)**: Platform Agent reference for GKE monitoring and logging on a single cluster, mostly write: golden-path loggingConfig and monitoringConfig components including APISERVER, SCHEDULER and CONTROLLER_MANAGER, gcloud container clusters update --monitoring / --enable-managed-prometheus / --enable-dataplane-v2-flow-observability, kubectl top for live usage, gcloud logging read and LQL queries for system, workload and audit logs, key metrics, an alert threshold table with Cloud Monitoring rules, node-health metrics, cost notes and a pointer to Cloud Trace and Profiler. Uses MCP gke:get_cluster, gke:list_k8s_events, gke:get_k8s_logs, gke:get_k8s_cluster_info, gke:describe_k8s_resource. Explicitly excludes application logging frameworks and external APMs outside GKE.
- **S30 gke-platform-security**: Platform Agent reference for cluster-level GKE security hardening, read and write via gcloud and MCP (gke:get_cluster, gke:update_cluster, k8s:check_k8s_auth, k8s:get_k8s_resource, k8s:apply_k8s_manifest): golden-path values for Workload Identity pool, Secret Manager add-on with rotation, insecure RBAC binding config, Shielded Nodes and GKE_METADATA; commands to enable Secret Manager, Binary Authorization, Shielded Nodes and GKE Sandbox on an existing cluster; RBAC audit via check_k8s_auth or kubectl auth can-i; a table of roles/container.* IAM roles; the GKE service agent and node service account; and gcloud projects add-iam-policy-binding patterns for GSAs. Explicitly excludes workload-level controls (Workload Identity bindings, SecretProviderClass, Pod Security Standards, NetworkPolicy, gvisor runtimeClassName), deferring to gke-workload-security, and enterprise RBAC planning (gke-multitenancy).
- **S31 gke-productionize**: Platform Agent orchestrator for a production readiness review of a GKE cluster or one or more applications, mostly read-only discovery (gcloud container clusters describe, kubectl get deployment/namespace/pods/hpa/pdb/networkpolicy) followed by mandatory delegation to gke-app-onboarding, gke-workload-scaling, gke-observability, gke-reliability, gke-platform-security, gke-workload-security, gke-backup-dr, gke-service-networking and gke-cost-optimization, ending in a Red/Amber/Green report per area. It asks for user confirmation before state-changing work. Explicitly excludes deep single-domain implementation, which it hands to the domain skills.
- **S32 gke-reliability (agents/cluster/skills/gke-reliability)**: Cluster Agent skill with six short workflows on one GKE cluster: check regional/multi-zonal layout via `gcloud container clusters describe --format=json(location, locations)`, list PDBs with `kubectl get pdb` plus an example PDB manifest, grep a Deployment for liveness/readiness/startup probes, a note on SIGTERM and `terminationGracePeriodSeconds`, an example `topologySpreadConstraints` block, and a `gcloud container clusters update --maintenance-window-*` command. Mostly read-only checks and example manifests the agent can propose; the maintenance-window step is a cluster write. It does not state exclusions. A separate, longer `gke-reliability` skill exists under agents/platform/skills.
- **S33 gke-reliability (agents/platform/skills/gke-reliability)**: Platform Agent reference for workload and cluster availability on a single cluster, read and write via MCP (get_cluster, get_k8s_resource, describe_k8s_resource, apply_k8s_manifest, list_k8s_events) with gcloud and kubectl fallbacks: golden-path regional cluster, surge upgrades, auto-repair, auto-upgrade and REGULAR channel; verifying regional control plane and multi-zone nodes; PodDisruptionBudget manifests; liveness, readiness and startup probe YAML with explicit timeouts; SIGTERM handling with preStop sleep; zone and hostname topology spread constraints; and minimum replica counts per workload type. Explicitly excludes disaster recovery and cluster backups (gke-backup-dr) and defers maintenance windows to gke-upgrades.
- **S34 gke-service-networking**: Platform Agent reference for exposing GKE applications, write via Kubernetes manifests on a single cluster: Gateway and HTTPRoute with the gke-l7-global-external-managed class, legacy GKE Ingress with the gce class annotation, Cloud Armor via BackendConfig securityPolicy and the cloud.google.com/backend-config Service annotation, ManagedCertificate for Ingress and Certificate Manager or Secret TLS on a Gateway HTTPS listener, container-native load balancing via the cloud.google.com/neg annotation, and Private Service Connect via ServiceAttachment. No MCP tools or gcloud commands are listed. Explicitly excludes cluster IP planning, Dataplane V2 network policies and node NAT egress (gke-networking).
- **S35 gke-stall-detection**: Cluster Agent, read-only, single cluster and one namespace (or one kind in it). Runs /opt/data/scripts/stall_report.py (agents/platform/scripts/stall_report.py), which applies four heuristics (generation-lag, stale-condition, repeating-warnings, dangling-reference) over kubectl get output for Gateways, HTTPRoutes, Deployments, custom resources and other namespaced kinds, with age thresholds and --kind/--threshold-minutes/--json flags, then records the finding on the kanban card via kanban_complete (including the Session KV controller-stall card format). It explicitly excludes failing-pod and bad-event symptoms (those go to gke-workload-troubleshooting and gke-reliability), never patches, opens PRs or reads Secret contents, and notes that Secret-typed references are unchecked under the default read-only identity.
- **S36 gke-stockout-investigator**: Platform Agent plugin skill (installed into the `platform` profile via the gke-stockout-investigator AgentPlugin) that handles a GKE autoscaler stockout alert from Pub/Sub end to end: send a `send_notification`, check for an open PR on `platform-agent/remediate-stockout-<workload>` with `vcs.py proposal list --source`, confirm the stockout is live via `kubectl get/describe pod`, take a GitOps working copy with `submit_suggestion.py prepare`, run quota/reservation/`kubectl top`/`gcloud beta compute advice capacity[-history]`/`cluster-autoscaler-status` diagnostics, apply eight ComputeClass debugging rules (A-H), edit ComputeClass or workload YAML with remediation comments, commit, and open the PR with `submit_suggestion.py submit --body-file`. Fleet-facing but one alert and one cluster per run; GitOps write, never a live-cluster mutation. It explicitly forbids `execute_code`, forge CLIs, `git add .`, `--body`, and branch-name suffixes.
- **S37 gke-storage (agents/cluster/skills/gke-storage)**: A short how-to on configuring GKE storage: writing a StorageClass for the Persistent Disk CSI driver, choosing between the PD, Filestore and Cloud Storage FUSE CSI drivers, creating a ReadWriteMany PVC, and expanding a volume by editing the PVC. Every workflow is a create-or-apply write and there are no diagnostic commands, so it reads as configuration guidance rather than single-cluster debugging. Sits under the Cluster Agent; a longer upstream-synced copy with the same name lives under agents/platform/skills. Does not state exclusions.
- **S38 gke-storage (agents/platform/skills/gke-storage)**: Platform Agent skill (upstream google/skills copy) for configuring storage on a single GKE cluster: it lists the golden-path CSI drivers and built-in StorageClasses, gives manifests for a custom regional pd-ssd StorageClass, ReadWriteOnce PVCs, Filestore ReadWriteMany PVCs and a GCS FUSE bucket mount, and shows PVC expansion via kubectl patch or the gke MCP patch_k8s_resource tool. It is a write skill (apply_k8s_manifest, patch) with best-practice guidance and a pointer to gke-backup-dr for PVC backup. It explicitly excludes database administration and replication strategies outside volume provisioning.
- **S39 gke-tpu-dynamic-slices-monitoring**: Platform Agent skill (upstream google/skills copy) for the GKE TPU Dynamic Slices feature on a single cluster: it diagnoses a Slice custom resource with kubectl describe slice and a lifecycle-state table (SliceNotCreated, SliceCreationFailed, ACTIVATING, ACTIVE, ACTIVE_DEGRADED, FAILED, DEACTIVATING, INCOMPLETE), checks single-slice and JobSet multi-slice pod annotations and nodeSelectors, and gives two confirm-first write procedures: removing stuck finalizers with kubectl patch, and disabling the slice controller (gcloud container clusters update --no-enable-slice-controller, delete the slices.accelerator.gke.io CRD, strip node labels). A references file shows example failure conditions. It explicitly excludes generic node pool creation and non-TPU workloads (pointing to gke-basics and gke-cluster-creation).
- **S40 gke-tpu-metrics-monitoring**: Platform Agent skill (upstream google/skills copy), read-only: it monitors GKE TPU containers, nodes and multi-host node pools through Cloud Monitoring system metrics and PromQL. It covers checking the runtime-metrics prerequisites (containerPort 8431, JAX and GKE versions), the accelerator duty_cycle, memory and tensorcore/bandwidth utilization metrics, node status conditions, node pool status and multi-host availability, interruption counts by type and reason, and 7-day MTTR and MTBI calculations, for one cluster or project-wide. A references file lists metric signatures (node unready, node pool error, preemption, host error, low utilization). It explicitly excludes non-TPU workload monitoring and non-metric TPU debugging.
- **S41 gke-upgrades**: Platform Agent skill (upstream google/skills copy with a repo-added footer) for planning, running and troubleshooting GKE control plane and node pool upgrades on Standard and Autopilot clusters. It covers release channels and support lifecycle, maintenance windows and the three exclusion scopes with their day limits and exact gcloud flags, mandatory overrides, surge and blue-green strategy per workload type, GPU/TPU upgrade constraints, pre- and post-upgrade checklists, gcloud and kubectl runbook templates (upgrade, downgrade, maintenance window), and a nine-item stuck-upgrade troubleshooting guide (PDBs, capacity, bare pods, webhooks, PVCs, stockouts, GPU driver regressions). The footer routes fleet-wide version and readiness checks to the fleet-upgrade-verification skill's fleet_upgrade_report.py and api_deprecation_scan.py scripts, which exist in this repo with the cited flags. It is a write skill producing plans and runbooks and issuing gcloud upgrade commands, for one cluster at a time. It explicitly excludes cluster creation, app onboarding, networking setup and security policy configuration.
- **S42 gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)**: Workflows for scaling GKE workloads: kubectl scale for manual replicas, kubectl autoscale and an HPA manifest (assets/hpa-example.yaml, CPU and memory targets), a VPA manifest (assets/vpa-example.yaml) with update modes including InPlaceOrRecreate, enabling VPA and node-pool Cluster Autoscaler with gcloud container clusters update, and best practices on requests, HPA/VPA metric conflicts, PDBs and the HPA stabilization window. All commands are writes to one cluster; there are no commands for reading HPA or VPA status. Sits under the Cluster Agent; an upstream-synced copy with a capacity-obtainability footer lives under agents/platform/skills. Does not state exclusions.
- **S43 gke-workload-scaling (agents/platform/skills/gke-workload-scaling)**: Platform Agent skill (upstream google/skills copy with a repo-added footer) for scaling workloads on a single GKE cluster: manual kubectl scale, Horizontal Pod Autoscaler via kubectl autoscale or the bundled autoscaling/v2 manifest, Vertical Pod Autoscaler enablement on Standard clusters and its update modes (Off, Initial, Auto, InPlaceOrRecreate), a VPA manifest, a rightsizing workflow from VPA Off-mode recommendations with a 20% buffer, and HPA/VPA best practices. The footer requires loading the capacity-obtainability skill before recommending GPU/TPU or large-shape scale-ups. It writes HPA/VPA objects and deployment replica counts. It explicitly excludes Cluster Autoscaler, static cluster sizing and node machine-type choices.
- **S44 gke-workload-security (agents/cluster/skills/gke-workload-security)**: Workflows for auditing and hardening one GKE cluster: a read-only audit script (scripts/audit_cluster.sh, gcloud container clusters describe for Workload Identity, Network Policy or Dataplane V2, Shielded Nodes, Binary Authorization, private nodes), then write steps for Workload Identity binding (kubectl create, gcloud iam add-iam-policy-binding, kubectl annotate, a test pod asset), enabling Calico network policy in two gcloud steps, a default-deny NetworkPolicy asset, Shielded Nodes, GKE Sandbox, Pod Security Standards labels, a Secret Manager CSI SecretProviderClass and Dataplane V2 NetworkLogging. Only the audit and the describe check are read-only; the rest mutates cluster or IAM state. Sits under the Cluster Agent; a longer upstream-synced copy lives under agents/platform/skills. Does not state exclusions.
- **S45 gke-workload-security (agents/platform/skills/gke-workload-security)**: Platform Agent skill (upstream google/skills copy with a repo-applied substitution for the network-policy enablement steps) for hardening workloads and namespaces on a single GKE cluster. It covers a read-only cluster posture audit (scripts/audit_cluster.sh checks Workload Identity, network policy or Dataplane V2, Shielded Nodes, Binary Authorization and private nodes via gcloud describe and jq), Workload Identity KSA-to-GSA binding with a test pod manifest, checking and enabling Calico or Dataplane V2 network policy enforcement and applying a default-deny NetworkPolicy, gVisor runtimeClassName, Pod Security Standards namespace labels, Secret Manager CSI SecretProviderClass, and Dataplane V2 NetworkLogging. It is a write skill (gcloud iam bindings, cluster updates, kubectl apply/label). It explicitly excludes control-plane security, RBAC hardening, Binary Authorization, Shielded Nodes and platform add-ons, pointing to gke-platform-security.
- **S46 gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)**: Cluster Agent, read-only, single workload in one namespace. A five-step SOP: acquire project, cluster, workload and a one-hour time window; read pod and Deployment status and classify Pending, CrashLoopBackOff (exit 137 vs other), ContainerCreating; read namespace events with kubectl get events or gcloud logging read and match FailedScheduling, FailedMount, image-pull failures (with a git log search for the last working tag); read current and previous container logs for OOM, stack traces, egress timeouts and read-only-filesystem errors; check Service endpoints and NetworkPolicies; then record the RCA and a proposed YAML patch on the kanban card with kanban_complete. It explicitly excludes applying patches, opening PRs (submit-suggestion is the Platform Agent's) and passing findings through the chat reply.
- **S47 gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)**: Platform Agent copy (overlaid from google/skills, with an upstream.lock and two local patches) of a five-step runbook for a failing workload on one GKE cluster: read pod and Deployment status with kubectl, read namespace events (kubectl or gcloud logging read), read current and previous container logs, check Service endpoints and NetworkPolicies, then write a root-cause summary and a corrected manifest. Covers CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, ContainerCreating, FailedMount, read-only filesystem and egress timeouts, with a dry-run mode that prints the commands when the cluster is unreachable. Diagnostics are read-only; the only write is a GitOps pull request, and only when the request asked for the fix (SOUL.md section 3, item 3). It excludes cluster provisioning, node pool creation and non-Kubernetes Google Cloud services.
- **S48 gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)**: A byte-identical copy of the upstream `google/skills` `gke-workload-troubleshooting` skill at the commit pinned in `agents/platform/skill-overlays/gke-workload-troubleshooting/upstream.lock`; it is layer 1 of the upstream-skill-overlay design (`scripts/skill_overlay.py`, `docs/designs/upstream-skill-overlays.md`), and `make skills-check` verifies its sha256 against the lock and regenerates the shipped `agents/platform/skills/gke-workload-troubleshooting` from it plus two patches. Its content is a five-step read-only diagnostic SOP for a single GKE workload (pod status and exit codes, namespace events via `kubectl get events` and `gcloud logging read`, `kubectl logs`, endpoints and NetworkPolicy checks, then a proposed GitOps manifest fix opened as a PR), with a dry-run fallback when the cluster is unreachable. It explicitly does not cover cluster provisioning, node pool creation, or non-Kubernetes Google Cloud services; the folder is excluded from prettier, shellcheck and docs-link checks and is not shipped in any agent image.
- **S49 inspect-repository**: Platform Agent, read-only. Lets the agent read the source of any GitHub or GitLab repository the install can reach, with no local git, through the credential broker: `inspect_repository.py` offers `clone` (copy a tree or `--prefix` into /opt/data/scratch), and `open`/`list`/`grep`/`fetch`/`close` on a broker-side handle, each printing one JSON object. Covers answering questions about code, reading upstream projects and dependencies, and reading the GitOps repository for context. It does not change repositories (that is submit-suggestion or fleet-audit) and it tells the agent not to re-open a repository that fleet-audit or submit-suggestion already handed it.
- **S50 install-kube-agents**: Lets a repo-level or operator-facing agent install kube-agents onto a GKE cluster in a GCP project by driving install.sh non-interactively: detect the environment with gcloud, interview the operator for project, region, cluster, model provider, chat channel and permission set, run --dry-run or --generate-only, then apply through terraform/examples/full-install/lifecycle.sh and the Helm chart. Covers adopting an existing cluster (Workload Identity, CMEK, node-pool migration, NetworkPolicy consent flags), the GitHub token minter setup for GitOps pull requests, the JSON status report, the terminal handover for a chat-less install, and the full install.sh flag table. It is a write skill against GCP and one host cluster; it explicitly hands upgrades to upgrade-kube-agents, never asks for secrets in chat, and never passes adoption flags without operator consent.
- **S51 kube-agents-observability**: Platform Agent, read-only, about kube-agents' own install on the management cluster rather than user workloads. Covers checking agent logs and the audit trail under /opt/data/logs, the fluent-bit sidecar and its ConfigMap, listing chat users from Cloud Logging, GMP and LiteLLM token metrics in Cloud Monitoring, OTel collector resolution from `platformagent.status.telemetry` and the hermes_otel plugin config, Cloud Trace latency breakdowns, and the API (8642/8643) and dashboard (9119) ports. Five Python scripts call the Logging, Monitoring and Trace REST APIs with a gcloud ADC token. It does not state exclusions; metrics guidance is LiteLLM-specific with pointers for vLLM and other providers.
- **S52 manage-cluster**: Platform Agent, write to the data PVC only (no cluster mutation). On a user request to manage an existing GKE cluster it resolves project/cluster/location, verifies the cluster with `verify_gke_cluster` or `gcloud container clusters describe`, runs `/opt/data/scripts/cluster_agent_profile.py create --project --cluster --location` to scaffold a read-only Cluster Agent profile, and confirms. It also explains how to stop managing a cluster: delete it (gke-cluster-creation) or add it to `spec.scope.exclude.clusters` on the PlatformAgent (RECONCILE_EXCLUDE still honoured). It does not create clusters and notes that the hourly cluster-agent-reconcile cron would do the same scaffold automatically.
- **S53 pr-conversation**: Platform Agent, reached from a kanban card filed by the github-repo-watcher cron. Covers answering a reviewer on a pull request the agent itself opened (head branch `platform-agent/*`): `pr_conversation.py poll` to read requests and the whole thread with `can_write`/`can_write_known` gates, deciding question vs change request, making a change via submit-suggestion `prepare --branch <head>`/`submit`, confirming the commit landed with `vcs.py proposal view/commits`, then `reply --verify-commit|--no-change` or `refuse`, and ending with `kanban_complete`/`kanban_block`. It explicitly excludes other people's pull requests, changes wider than the branch under review, merging, closing or approving, and pull requests labelled `agent:ignore`.
- **S54 review-address-feedback**: Guides a repo contributor agent through one review round on an open kube-agents pull request: collect unresolved threads, review-body findings and red checks, cross-check them against the Self-Review section, triage each as fix, push-back or deferral, bracket fixes with red/green evidence, fix the whole class, re-review with review-preflight, push once, reply in every thread with proof, request one re-read, and resolve settled threads once the re-read lands. It is GitHub-side, write-to-branch work for the author of the PR, with no cluster access involved. It defers the commands to docs/pull-request-workflow.md and the rules to AGENTS.md, and states no other exclusions.
- **S55 review-adversarial**: Gives a reviewing agent the method for a hostile read of a diff range in this repo: fix the range with a three-dot diff, state the change's intent, hunt candidates from ten named angles (line scan, removed behaviour, cross-file tracing, operations and security, reuse, simplification, altitude, conventions and docs, scope and test coverage, sibling pull requests), re-derive every candidate from source into CONFIRMED, PLAUSIBLE or REFUTED, then record a fixed or deliberately-not-fixed disposition per survivor with BLOCKER/HIGH/MEDIUM/LOW severity. It is read-only on the repo apart from step 6 (edit on CONFIRMED) and is used by authors before a PR, by reviewers through pr-review-batch, and by kube-agents-bot as its playbook. It explicitly excludes the full documentation-drift question (left to review-docs-drift) and all plumbing such as spawning the clean context (left to review-preflight).
- **S56 review-docs-drift**: Lets a repo contributor or reviewer agent check a branch diff against main for documentation drift in both directions: which docs a code change should have updated (generated regions, identifier sources, prose pages), and whether changed docs still match source, the canonical-home table in AGENTS.md, the docs/README.md map, and the site audience rule. It names git diff and git grep steps, the make docs-check, make docs-generate, prettier and site build gates, and reports a Blocking/Advisory triage table. It is read-only by design (the report is the deliverable, no silent fixes) and holds no repository facts of its own; it does not cover code defects, which it leaves to review-adversarial.
- **S57 review-preflight**: Plumbing for the author of a kube-agents branch before opening a pull request: fetch and fix the base diff range, run make docs-check in the main loop, spawn one subagent each for review-adversarial and review-docs-drift (or a fresh headless session when subagents are unavailable), hand each only the repo, range, skill path and gate output while withholding intent and commit messages, then merge the returned findings into one severity-ordered disposition list that becomes the PR's Self-Review section. It covers re-runs after fixes and what to do when no clean context can be obtained. It explicitly holds no review method of its own and does not restate the requirement, which AGENTS.md owns.
- **S58 review-security-k8s-admission**: A short checklist for a repo-level security reviewer auditing Kubernetes admission control manifests: ValidatingWebhookConfiguration, MutatingWebhookConfiguration, ValidatingAdmissionPolicy and MutatingAdmissionPolicy. It covers failurePolicy and timeouts, namespaceSelector/objectSelector exemptions, binding scope, CEL failure handling and message leakage, caBundle/HTTPS and NetworkPolicy ingress to the webhook, and mutating risks such as sidecar injection, reinvocationPolicy, CEL side effects and execution order. It is read-only review guidance applicable to any cluster or manifest, part of the review-security-k8s-* family; it does not state exclusions.
- **S59 review-security-k8s-agents-audit-logs**: A repo-level review skill for a contributor or review agent, run as a sub-agent of review-security-k8s-agents-main. It is a read-only checklist applied to manifests and agent configs: one dedicated ServiceAccount per agent, an API audit policy that captures agent requests at Metadata or RequestResponse level, logging to stdout/stderr rather than local disk, no hostPath mounts of /var/log/containers or /var/log/pods, and application-level logging of full prompts, outputs and tool input/output with sensitive data scrubbed first. It does not run any command, targets no specific cluster or fleet, and does not state exclusions.
- **S60 review-security-k8s-agents-credentials**: A repo-level review skill (sub-agent of review-security-k8s-agents-main) for a contributor or review agent reading Kubernetes manifests of AI agent workloads. It is a read-only checklist: authenticated outbound calls must go through an injecting credential proxy or sidecar, the main agent container must not receive Secrets via env, envFrom or volume mounts, no plaintext keys in manifests, automountServiceAccountToken false with the token only in the sidecar, a dedicated non-default serviceAccountName, and no wildcard verbs or resources in RBAC. It names no commands or cluster scope and does not state exclusions.
- **S61 review-security-k8s-agents-data-exfil**: A repo-level review skill (sub-agent of review-security-k8s-agents-main) for a contributor or review agent reading Kubernetes configuration of AI agent workloads. It is a read-only checklist on three fronts: egress NetworkPolicies that must be restrictive with no 0.0.0.0/0 and allowlisted to internal services and the LLM API, outbound routing through an egress gateway or proxy (service mesh, HTTP_PROXY) for inspection and SNI allowlisting, and RBAC or volume mounts that give broad get/list/watch on secrets and configmaps. It names no commands or cluster scope and does not state exclusions; its egress checks overlap with review-security-k8s-agents-firewall.
- **S62 review-security-k8s-agents-firewall**: A repo-level review skill (sub-agent of review-security-k8s-agents-main) for a contributor or review agent reading NetworkPolicies and firewall configuration for AI agent control loops and execution sandboxes. Read-only checklist: default-deny egress with a minimal allowlist, blocking agent access to internal cluster APIs and the cloud metadata address 169.254.169.254 on its credential ports (TCP 80 pre-NAT, 988 post-NAT) while leaving port 53 open for Cloud DNS for GKE, flagging 0.0.0.0/0 egress, restricting ingress to trusted upstreams, and flagging LoadBalancer or NodePort exposure without ingress NetworkPolicies. It names no commands or cluster scope; the only stated exclusion is that port 53 to the metadata address is not flagged.
- **S63 review-security-k8s-agents-main**: A repo-level orchestration skill for a contributor or review agent; it is itself a sub-agent of review-security-k8s-main. It takes the project context produced by review-security-k8s-understand, launches six sub-skills in parallel (sandbox, firewall, credentials, prompt-injection, data-exfil, audit-logs), requires each to return a fixed JSON findings shape, triages findings against the context (for example dropping egress-proxy findings for an air-gapped sandbox, or root-in-sandbox findings when a gVisor or Kata RuntimeClass is confirmed) and merges them into one JSON array. It performs no checks of its own, runs no commands, and does not state exclusions.
- **S64 review-security-k8s-agents-prompt-injection**: A repo-level review skill (sub-agent of review-security-k8s-agents-main) for a contributor or review agent reading AI agent deployment configuration. It is read-only and holds only two checks: require an LLM-specific API gateway or WAF sidecar and flag raw agent APIs exposed to untrusted traffic, and ensure system prompts or safety instructions kept in ConfigMaps or environment variables cannot be altered by less privileged workloads. It names no commands or cluster scope and does not state exclusions; despite the description it has no input-sanitization check.
- **S65 review-security-k8s-agents-sandbox**: A repo-level review skill (under .agents/skills, run by a reviewing agent against manifests in a pull request or a cluster, read-only) that audits the execution sandboxes an LLM agent uses to run untrusted code (Python REPLs, bash tools, WASM). It checks three things: a hardened RuntimeClass (gVisor or Kata) instead of a standard pod, separation of the sandbox from the main agent loop plus restrictive seccomp/AppArmor profiles, and ephemeral lifecycles with low CPU, memory and ephemeral-storage limits. It is one of six sub-skills launched by review-security-k8s-agents-main and does not state exclusions.
- **S66 review-security-k8s-gateway**: A repo-level review skill (under .agents/skills, read-only, run against manifests in a pull request or a cluster) that audits Kubernetes Gateway API objects: Gateway, HTTPRoute, TCPRoute, TLSRoute and ReferenceGrant. It flags overlapping hostnames or paths that let one route hijack another, cross-namespace route or secret references without a narrow ReferenceGrant, weak TLS listener settings, missing allowedRoutes namespace restrictions, and wildcard or overly broad hostnames. It is one of ten sub-skills launched by review-security-k8s-main; it covers Gateway API only (classic Ingress is left to review-security-k8s-network) and does not state exclusions.
- **S67 review-security-k8s-main**: A repo-level orchestrator skill (under .agents/skills, read-only) that runs a general Kubernetes security review: it first invokes review-security-k8s-understand for project context, then launches ten sub-skills in parallel (rbac, nodes, network, gateway, namespaces, service-accounts, storage, admission, pod, and agents-main), each told to emit a fixed JSON findings schema with agent, message, file and line. It then triages the raw findings against the context (for example dropping hostPath warnings for CSI daemonsets, or downgrading NetworkPolicy warnings when a strict service mesh exists) and merges them into one JSON array. It performs no checks itself and does not state exclusions.
- **S68 review-security-k8s-namespaces**: A repo-level review skill (under .agents/skills, read-only, run against manifests in a pull request or a cluster) that audits how namespaces are used as isolation boundaries. It flags most workloads piled into one namespace, mixing of trust levels or tenants, custom workloads in default/kube-system/kube-public/kube-node-lease, namespace names that impersonate system components, labels or annotations that bypass policy (OPA exemptions, pod-security enforce=privileged), absurd ResourceQuotas or LimitRanges, suspicious namespace finalizers, cross-namespace references without ReferenceGrant or via ExternalName, and leftover Secrets, ServiceAccounts or RoleBindings in namespaces with no pods. It is a sub-skill of review-security-k8s-main and does not state exclusions.
- **S69 review-security-k8s-network**: A repo-level review skill (under .agents/skills, read-only, run against manifests in a pull request or a cluster) that audits Kubernetes network isolation and exposure: NetworkPolicies, Services, Ingresses and service mesh policy. It requires default-deny ingress and egress NetworkPolicies per namespace, flags missing egress limits and broad CIDRs or empty selectors, flags public LoadBalancers, NodePort services and exposed admin ports (22, 3389, 2379, 10250), requires TLS and HTTPS redirects on Ingress, flags hand-written Endpoints/EndpointSlices and hostNetwork: true, and for Istio-style meshes requires STRICT PeerAuthentication and default-deny AuthorizationPolicies. It is a sub-skill of review-security-k8s-main; Gateway API objects are left to review-security-k8s-gateway, and it does not state exclusions.
- **S70 review-security-k8s-nodes**: A repo-level review skill (under .agents/skills, read-only, run against manifests in a pull request or a cluster) that audits ways a compromised pod or node could escalate to cluster-wide control. It flags hostPath mounts of kubelet credentials (/etc/kubernetes, /var/lib/kubelet, kubeconfig) and of container runtime sockets (docker.sock, containerd.sock), extra RBAC bindings for system:nodes or system:node:<name> that bypass NodeRestriction, roles granting impersonate on system:nodes, service-account roles that can create/update/patch/delete nodes or nodes/status, and broad tolerations (operator: Exists with no key) that let untrusted workloads land on control-plane nodes. It recommends ValidatingAdmissionPolicies as the fix for hostPath abuse. It is a sub-skill of review-security-k8s-main and does not state exclusions.
- **S71 review-security-k8s-pod**: Repo-level review skill (run by a contributor or by the review-security-k8s-main orchestrator) that reads Pod specs and their PodSecurityContext/SecurityContext and flags: privileged, host namespaces (hostNetwork/hostPID/hostIPC/hostUsers), hostPath volumes, allowPrivilegeEscalation, root execution, added capabilities, missing capabilities.drop ALL, missing readOnlyRootFilesystem and seccomp, use of the default ServiceAccount, token automounting, Secret-based SA tokens, and images not pinned by digest. Read-only manifest review, cluster-agnostic, single resource type (Pods and pod templates). Does not state exclusions, though it does not cover RBAC, network, or storage settings beyond hostPath.
- **S72 review-security-k8s-rbac**: Repo-level review skill (contributor or review-security-k8s-main orchestrator) that reads Role, ClusterRole, RoleBinding and ClusterRoleBinding manifests and flags: bindings to system:anonymous/unauthenticated/authenticated/masters and system:serviceaccounts groups, cluster-admin grants, write access to system: bindings, escalation paths (bind/escalate/impersonate, writes to rbac.authorization.k8s.io, CSRs, webhooks, CRDs, tokenreviews, namespaces, networkpolicies), wildcards, deletecollection, over-scoped ClusterRoleBindings, self-modification, and access to secrets, pods/exec, pods/portforward, pods/attach, nodes/proxy, ephemeralcontainers and status subresources. Ships resources/gke-rbac.md, a copy of the GKE RBAC best-practices page with kubectl/jq detection commands and the gcloud --no-enable-insecure-binding-system-* flags. Read-only manifest review, single cluster, GKE-flavoured. Does not state exclusions.
- **S73 review-security-k8s-service-accounts**: Repo-level review skill (contributor or review-security-k8s-main orchestrator) that reads ServiceAccount objects and their bindings and flags: RBAC bound to the default ServiceAccount, one ServiceAccount shared by several apps, automountServiceAccountToken not set to false on the ServiceAccount, several workloads mapped to one GCP identity through the iam.gke.io/gcp-service-account Workload Identity annotation, long-lived kubernetes.io/service-account-token Secrets, imagePullSecrets with broad registry access, and ServiceAccounts with bindings but no workloads. Read-only manifest review, single cluster. Does not state exclusions; RBAC rule content and Pod-level security contexts are covered by sibling skills, not here.
- **S74 review-security-k8s-storage**: Repo-level review skill (contributor or review-security-k8s-main orchestrator) that reads StorageClass, PersistentVolume, PersistentVolumeClaim, volume and volumeMount definitions and flags: writable mounts missing readOnly, subPath on user-writable volumes, hostPath use (recommends local PVs), missing fsGroup, ReadWriteMany access mode, StorageClasses without encryption at rest (CMEK or encrypted parameter), Recycle and unmanaged Retain reclaim policies, allowVolumeExpansion without ResourceQuotas, and CSI Secrets Store mounts without strict limits. Read-only manifest review, single cluster, cloud-agnostic. Does not state exclusions.
- **S75 review-security-k8s-understand**: Repo-level context-building skill run first by the review-security-k8s-main and review-security-k8s-agents-main orchestrators (and cited in docs/architecture/03-security-model.md). It reads the target project's README, diagrams and architecture docs, names the main components and workloads, labels each workload Infrastructure (CSI drivers, ingress controllers) or Application (APIs, databases), and records global compensating controls such as a service mesh enforcing mTLS or cluster-wide OPA/Gatekeeper policies. Output is a short summary that the orchestrators use to triage sub-reviewer findings. Read-only, no checks of its own; it explicitly leaves specific security reviews to the specialized skills.
- **S76 skill-review**: Repo-level skill for a contributor reviewing SKILL.md files in this repository. It checks frontmatter (description opens with the user's action and names its object; YAML-safe values), structure (top-level # Task and # Checks or # Workflow sections, terse headers), prose (no persona setup, no filler, imperative bullets starting with Flag/Require/Ensure) and formatting (single-sentence rules, no loss of checks or domain knowledge when shortening). AGENTS.md and .agents/rules/documentation.md point to it as the style owner for SKILL.md files. Read-only review of skill text; it does not cover placement by persona or whether a skill's checks are correct.
- **S77 submit-suggestion**: Platform Agent, the GitOps write path for one-off changes: `submit_suggestion.py prepare --repo --branch platform-agent/<change>-<id>` brings down a working copy under /opt/data/scratch/vcs, the agent edits and stages named files, `submit --title --body-file` (or `--keep-description`, optional `--base`) publishes the branch and opens or refreshes the pull or merge request on GitHub or GitLab, with named refusal codes for base and branch conflicts. Step 5 covers addressing review feedback on an existing PR through `vcs.py proposal view --comments` and the same prepare/submit on the PR's branch. It excludes diagnosis-only requests (answer in the reply per SOUL.md section 3, item 3) and fixes for fleet-audit findings, which fleet-audit's `remediate` opens itself.
- **S78 uninstall-kube-agents**: Repo-level lifecycle skill for a human or agent operator tearing down a kube-agents install. It gives the release-pinned `curl ... uninstall.sh | bash -s -- --non-interactive --gcp-project-id --gke-cluster-name --gcp-region` one-liner, explains that the engine is `lifecycle.sh destroy` in terraform/examples/full-install against the GCS Terraform state, covers `--source-ref` for pre-Terraform installs, the `terraform`/`helm` prerequisites, the exit-code contract (3 = nothing to remove, 1 = failure) and the JSON report at /tmp/kube-agents-uninstall-report.json. It is a GCP-project-and-cluster-wide write operation (destroys Terraform-owned resources, Helm releases, the PlatformAgent CR, backups) and does not state exclusions beyond pointing at `--help` and the site uninstall page.
- **S79 upgrade-kube-agents**: Repo-level lifecycle skill for upgrading an existing kube-agents install with `upgrade.sh`, either curl-piped at a release tag or from a release bundle. It covers the three `--upgrade-mode` values (harness = one `helm upgrade` re-tagging agent, sandbox and plugin images; operator = CRDs plus operator image; full = CRDs plus a `terraform apply` from install.env), `--drop-undeclared-values`, `--dry-run` versus `--plan`, `--image-tag` versus `--keep-image-tag`, how a baked release version changes flag behaviour, and the JSON report at /tmp/kube-agents-upgrade-report.json. It writes to the cluster and GCP project; it does not cover fresh installs or uninstalls and says installs without a `kube-agents` Helm release must use their own release's script.
- **S80 version-control**: Platform Agent skill for working with a hosted repository without a forge CLI. Remote verbs (`capabilities`, `identity`, `clone`, `publish`, `proposal create|list|view|comment|update|close|commits|acknowledge`, `issue create|list|view|comment|update|close`, `label ensure`, `remote-branch view|delete`) go through `scripts/vcs.py`, which talks to a credential-holding broker in another container; local work (history, blame, grep, diff, file modes, branch, commit) uses a credential-free `git` on the working copy that `clone` writes to disk, with `vcs.py` offering JSON wrappers (`log`, `show`, `annotate`, `files`, `grep`, `diff`, `status`, `branch`, `commit`, `discard`). It is read and write (branch, commit, publish, open proposals and issues) on any repository in the install's managed list, and documents every broker refusal code. It explicitly does not cover repositories outside the managed list or one-off shallow reads of large repositories (use `inspect-repository`), nor the workspace that `fleet-audit` and `submit-suggestion` already own.
- **S81 workload-rebalancing**: Platform Agent orchestration skill for moving one workload from an overutilized cluster to one with headroom. It resolves each cluster's profile with `get_cluster_profile_name`, fans out two parallel read-only kanban cards (`kanban_create` with no `parents`) asking cluster agents to validate can-host and safe-to-evacuate, polls them with `kanban_show`, and if both are green declares the move as a single GitOps PR via `submit-suggestion` for KCC/Config Sync to reconcile, recording the decision in `kanban_complete` metadata. Fleet-scoped, write only through a PR, never imperative cluster mutation; it explicitly does not cover a trivial single-cluster change (act directly) and tells the agent not to declare when either validation is red.

Pairs at 2 stars or fewer:

- 1 star: cluster-agent-lifecycle and manage-cluster. manage-cluster's whole flow (run cluster_agent_profile.py create for one cluster, note the reconcile cron and the spec.scope.exclude.clusters opt-out) is contained in cluster-agent-lifecycle, which adds delete, kanban delegation, fan-out and the reconcile details; manage-cluster only adds a cluster-exists check and project resolution.
- 1 star: gke-observability (agents/cluster/skills/gke-observability) and gke-observability (agents/platform/skills/gke-observability). The Platform copy covers every Cluster-copy workflow (describe loggingConfig/monitoringConfig, enable Managed Prometheus, control-plane metrics, Dataplane V2 observability, LQL queries, dashboards/alerts, Trace and Profiler) and adds golden-path tables, kubectl top, gcloud logging read, alert thresholds, node-health metrics and cost notes.
- 1 star: gke-reliability (agents/cluster/skills/gke-reliability) and gke-reliability (agents/platform/skills/gke-reliability). The Cluster Agent copy is a trimmed version of the Platform Agent skill: workflows 1-5 (regional/multi-zone check, PDB listing and manifest, probe grep, SIGTERM/terminationGracePeriodSeconds, zone topologySpreadConstraints) are the same text, while the platform copy adds MCP tool calls, a golden-path defaults table, full probe YAML, a preStop hook, hostname spread and a replicas table; the only thing the cluster copy has that the platform copy lacks is the one-line maintenance-window gcloud command, which the platform copy routes to gke-upgrades.
- 1 star: gke-storage (agents/cluster/skills/gke-storage) and gke-storage (agents/platform/skills/gke-storage). The platform copy covers everything in the cluster copy (pd-ssd regional StorageClass, CSI driver choice, Filestore RWX PVC, PVC expansion, best practices) and adds the built-in StorageClass table, a GCS FUSE mount manifest, MCP patch tooling and a backup pointer.
- 1 star: gke-workload-security (agents/cluster/skills/gke-workload-security) and gke-workload-security (agents/platform/skills/gke-workload-security). Same upstream gke-workload-security text at two versions: identical audit script, Workload Identity binding, Calico/Dataplane V2 network-policy enablement, default-deny policy, PSS labels, Secret Manager CSI and NetworkLogging sections; the Platform copy adds the long description, prerequisites, a gVisor pod manifest and resource links, while the Cluster copy's only extra content is the two cluster-level gcloud enable commands (Shielded Nodes, GKE Sandbox) the Platform copy hands to gke-platform-security.
- 1 star: gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) and gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting). The platform copy is the upstream file plus two patches (a timestamp filter inside the logging query and a step-5 gate that opens a PR only when the request asked for a fix), so it covers everything the third_party copy does and more.
- 1 star: review-security-k8s-agents-main and review-security-k8s-main. Same four-step workflow (take context, launch sub-skills in parallel with the identical JSON findings schema, triage against context, merge), and main launches agents-main as one of its ten sub-skills, so main covers everything agents-main does and more.
- 2 stars: capacity-obtainability and gke-stockout-investigator. Diagnostics A-D (gcloud compute regions describe quota, reservations list, kubectl top, gcloud beta compute advice capacity and capacity-history) and the eight ComputeClass rules A-H are verbatim the same text in both; capacity-obtainability wraps them in typed evidence, Flex-Start and calendar-mode planning for design requests, the stockout investigator wraps them in alert dedup, false-signal checks and a GitOps remediation PR.
- 2 stars: gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) and gke-workload-scaling (agents/platform/skills/gke-workload-scaling). Both carry the same manual scale, HPA, VPA-enablement and best-practice text with the same assets; the cluster copy adds a Cluster Autoscaler section the platform copy excludes, and the platform copy adds a rightsizing workflow and a capacity-obtainability footer, so neither is a strict superset
- 2 stars: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) and gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting). Both are the same five-step GKE workload diagnostic SOP (pod status, namespace events, logs, endpoints and NetworkPolicies, RCA plus YAML patch); they differ only in step 0 (dry-run fallback vs pod-timestamp heuristic) and in the hand-off (kanban_complete vs reply or GitOps PR).
- 2 stars: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) and gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting). Same five-step GKE workload diagnostic SOP with near-identical commands and signature tables; the cluster copy swaps the upstream's unconditional PR step for a kanban_complete hand-off and drops the dry-run mode.
- 2 stars: review-security-k8s-agents-firewall and review-security-k8s-network. Both review NetworkPolicies and service exposure with the same core checks (default-deny egress, 0.0.0.0/0 egress, LoadBalancer/NodePort without ingress NetworkPolicies); network adds Ingress TLS, admin ports and mesh policy while firewall adds the agent-specific metadata-address block, so either could be picked for most NetworkPolicy reviews.
