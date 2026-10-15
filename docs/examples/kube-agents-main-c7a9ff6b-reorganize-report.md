# Skills reorganize report: kube-agents

Generated 2026-10-15 19:04 UTC by SSS. This is a local working document in
`.sss/reports/`; it is not committed. Sections 2 to 6 answer one question each.

## 1. Summary

We found 112 skills in six places: repo-level skills under .agents/skills, the Platform Agent and Cluster Agent profiles, the a2a persona, one agent plugin, and the upstream google/skills mirror under third_party. None is managed by SSS yet, so there are no stale-against-source findings; every finding here comes from reading the files. We compared every pair: 6,216 pairs in all, 4,656 once skills with the same content are counted once. 3,320 pair scores were already cached; 1,336 were scored this run (15 skills had changed or were new). 27 pairs sit at 2 stars or fewer, 21 of them at 0 or 1 star, and 15 more skill pairs are identical byte for byte. Most of that is by design: the shipped gke-* skills are generated from the upstream mirror plus an overlay, so every mirror/shipped pair is a duplicate on purpose and needs no change. The real work is in the hand-maintained Cluster Agent copies, which have drifted from the Platform copies on facts (conflicts below), in a run of out-of-date commands and defaults inside the mirrored skills, and in two disagreements between unrelated skills. The inventory tool reported 48 broken references; we checked each one and every target exists, either at the repo root or at the Platform Agent profile root where the skill runs, so none is filed. A second, sceptical pass re-read every finding against its quoted evidence and changed 1 of them. 107 findings remain: 23 conflicts, 24 out of date, 34 duplicate groups, 5 out of place, 20 unuseful or padded, 1 with front matter that does not parse. No action was applied and no pull request was opened in this run, at the user's request.

| Question | Answer |
| --- | --- |
| Do any skills give conflicting information? | Yes, 23 |
| Are any skills out of date? | Yes, 24 |
| Are any skills duplicated? | Yes, 34 |
| Are any skills missing pieces they refer to? | No |
| Are any skills unuseful or out of place? | Yes, 26 |
| Actions we can take without asking | 27 |
| Decisions needed from you | 38 |

## 2. Conflicts

These skills disagree. An agent that loads both will get two answers.

### conf-b0e7b5: gke-app-onboarding (agents/platform/skills/gke-app-onboarding), gke-app-onboarding (third_party/google-skills/gke-app-onboarding)

The upstream mirror and the shipped copy give different instructions: The sample Dockerfile pins a different Node.js base image in each copy. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-app-onboarding (third_party/google-skills/gke-app-onboarding)/assets/Dockerfile:2`: "FROM node:18-slim"
- `gke-app-onboarding (agents/platform/skills/gke-app-onboarding)/assets/Dockerfile:2`: "FROM node:26-slim"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-37aa78: gke-backup-dr (agents/platform/skills/gke-backup-dr), gke-backup-dr (third_party/google-skills/gke-backup-dr)

The upstream mirror and the shipped copy give different instructions: Upstream tells the agent to install the gcloud beta component; the shipped copy forbids running gcloud components install. The restore-plan command restores volume data in the shipped copy but not in upstream, which omits --volume-data-restore-policy. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-backup-dr (third_party/google-skills/gke-backup-dr)/SKILL.md:68`: "(`gcloud components install beta`)."
- `gke-backup-dr (agents/platform/skills/gke-backup-dr)/SKILL.md:70`: "already includes. Do not run `gcloud components install`: the credential"
- `gke-backup-dr (third_party/google-skills/gke-backup-dr)/SKILL.md:41`: "gcloud beta container backup-restore restore-plans create {restore_plan_name} \"
- `gke-backup-dr (third_party/google-skills/gke-backup-dr)/SKILL.md:45`: "  --all-namespaces \"
- `gke-backup-dr (agents/platform/skills/gke-backup-dr)/SKILL.md:46`: "  --volume-data-restore-policy=restore-volume-data-from-backup \"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-d72b76: gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler), gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler)

The upstream mirror and the shipped copy give different instructions: The two copies route ComputeClass YAML questions to differently named skills. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler)/SKILL.md:19`: "**Overlap Warning:** Defer to the `gke-compute-class` skill for ComputeClass YAML generation, schemas, and priority configurations"
- `gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler)/SKILL.md:19`: "**Overlap Warning:** Defer to the `gke-compute-classes` skill for ComputeClass YAML generation, schemas, and priority configurations"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-aecc4e: gke-manifest-generation (agents/platform/skills/gke-manifest-generation), gke-manifest-generation (third_party/google-skills/gke-manifest-generation)

The upstream mirror and the shipped copy give different instructions: The inference-quickstart manifest is written with --output-path in upstream and with a stdout redirect in the shipped copy, which says the flag is refused. Upstream makes answer_query the preferred Developer Knowledge tool and names get_document; the shipped copy forbids answer_query and names get_documents. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-manifest-generation (third_party/google-skills/gke-manifest-generation)/SKILL.md:206`: "          --output-path={output_file_path}"
- `gke-manifest-generation (agents/platform/skills/gke-manifest-generation)/SKILL.md:206`: "          > {output_file_path}"
- `gke-manifest-generation (agents/platform/skills/gke-manifest-generation)/SKILL.md:209`: "Redirect stdout rather than passing `--output-path`: `gcloud` runs in"
- `gke-manifest-generation (third_party/google-skills/gke-manifest-generation)/SKILL.md:217`: "-   **`answer_query`**: Use this to ask direct questions (e.g., *"How to"
- `gke-manifest-generation (third_party/google-skills/gke-manifest-generation)/SKILL.md:222`: "-   **`get_document`**: Use this to fetch full document contents when"
- `gke-manifest-generation (agents/platform/skills/gke-manifest-generation)/SKILL.md:226`: "-   Do not call **`answer_query`**: its quota is 50 requests per day per"
- `gke-manifest-generation (agents/platform/skills/gke-manifest-generation)/SKILL.md:224`: "-   **`get_documents`**: Use this to fetch full document contents when"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-1e0e2d: gke-productionize (agents/platform/skills/gke-productionize), gke-productionize (third_party/google-skills/gke-productionize)

The upstream mirror and the shipped copy give different instructions: Workload Identity is routed to gke-platform-security/gke-workload-security upstream and to gke-workload-identity in the shipped copy. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-productionize (third_party/google-skills/gke-productionize)/SKILL.md:98`: "-   **Action**: You MUST run the `gke-platform-security` and"
- `gke-productionize (third_party/google-skills/gke-productionize)/SKILL.md:99`: "    `gke-workload-security` skills for Workload Identity, Network Policies, and"
- `gke-productionize (agents/platform/skills/gke-productionize)/SKILL.md:98`: "-   **Action**: You MUST run the `gke-workload-identity` skill for Workload"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-6bb808: gke-platform-security (agents/platform/skills/gke-platform-security), gke-platform-security (third_party/google-skills/gke-platform-security)

The upstream mirror and the shipped copy give different instructions: Workload Identity GSA-to-KSA bindings are routed to gke-workload-security upstream and to gke-workload-identity in the shipped copy. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:166`: "    `gke-workload-security` skill."
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:25`: "Standards), refer to the `gke-workload-security` skill."
- `gke-platform-security (agents/platform/skills/gke-platform-security)/SKILL.md:166`: "    `gke-workload-identity` skill."
- `gke-platform-security (agents/platform/skills/gke-platform-security)/SKILL.md:25`: "Identity Service Account bindings, the `gke-workload-identity` skill."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-cb96e1: gke-upgrades (agents/platform/skills/gke-upgrades), gke-upgrades (third_party/google-skills/gke-upgrades)

The upstream mirror and the shipped copy give different instructions: Upstream says any upgrade pauses when the maintenance window closes; the shipped copy says only surge upgrades pause and blue-green upgrades run to completion. The PDB-relax patch body differs: upstream sets maxUnavailable only, the shipped copy also clears minAvailable. Upstream restores the relaxed PDB with kubectl apply of the backup file; the shipped copy says to patch the original value back and not to apply the backup. The GPU-driver rollback step uses a nonexistent gcloud command upstream and the real one in the shipped copy. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-upgrades (third_party/google-skills/gke-upgrades)/SKILL.md:182`: "- **Silent Pause Behavior:** If a maintenance window closes before an upgrade (auto or manual) completes, GKE intentionally pauses the rollout to prevent disruption outside allowed times."
- `gke-upgrades (agents/platform/skills/gke-upgrades)/SKILL.md:182`: "- **Silent Pause Behavior:** If a maintenance window closes before a surge upgrade (auto or manual) completes, GKE intentionally pauses the rollout to prevent disruption outside allowed times. A blue-green node-pool upgrade does not pause: it continues past the window to completion"
- `gke-upgrades (third_party/google-skills/gke-upgrades)/references/runbook-template.md:164`: "  --type merge -p '{"spec":{"maxUnavailable":"100%"}}'"
- `gke-upgrades (agents/platform/skills/gke-upgrades)/references/runbook-template.md:164`: "  --type merge -p '{"spec":{"minAvailable":null,"maxUnavailable":"100%"}}'"
- `gke-upgrades (third_party/google-skills/gke-upgrades)/references/runbook-template.md:171`: "kubectl apply -f /tmp/pdb-backup-TIMESTAMP.yaml"
- `gke-upgrades (third_party/google-skills/gke-upgrades)/references/troubleshooting.md:41`: "kubectl apply -f pdb-backup.yaml"
- `gke-upgrades (agents/platform/skills/gke-upgrades)/references/runbook-template.md:170`: "#    the backup records for PDB_NAME and clear the field step 1 set. Do not"
- `gke-upgrades (agents/platform/skills/gke-upgrades)/references/runbook-template.md:174`: "  --type merge -p '{"spec":{"maxUnavailable":null,"minAvailable":ORIGINAL_MIN_AVAILABLE}}'"
- `gke-upgrades (agents/platform/skills/gke-upgrades)/references/troubleshooting.md:41`: "# 3. Once the upgrade completes, RESTORE (mandatory): patch back the value"
- `gke-upgrades (third_party/google-skills/gke-upgrades)/references/troubleshooting.md:191`: "   gcloud container node-pools upgrade NODE_POOL_NAME \"
- `gke-upgrades (agents/platform/skills/gke-upgrades)/references/troubleshooting.md:198`: "   gcloud container clusters upgrade CLUSTER_NAME \"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-baafb0: gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security)

The upstream mirror and the shipped copy give different instructions: Upstream calls KSA-to-GSA impersonation the recommended Workload Identity method; the shipped copy calls it legacy and makes direct KSA principal binding the default. Upstream enables Network Policy enforcement with one command (the addon); the shipped copy requires two sequential commands, addon then --enable-network-policy. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:56`: "Google Service Accounts (GSAs). This is the recommended method for workloads to"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:53`: "### 2. Configure Workload Identity (legacy GSA impersonation)"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:56`: "Kubernetes Service Account (KSA) principal directly is the current default, and"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:98`: "**Enable Network Policy Enforcement:**"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:102`: "    --update-addons=NetworkPolicy=ENABLED \"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:123`: "two sequential commands in this order: first enable the Calico addon on the"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:136`: "    --enable-network-policy \"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-f492c5: gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

The upstream mirror and the shipped copy give different instructions: The Cloud Logging events query bounds the time window with --start-time/--end-time flags upstream and with timestamp terms inside the filter in the shipped copy. Upstream always opens a pull request with the fix; the shipped copy opens one only when the request asked for the fix to be submitted, and otherwise replies with the manifest. Nothing is wrong for the Platform Agent today, because it loads only the shipped copy and the overlay patch is what makes the difference. The mirror is the source of truth, so the fix should also go upstream, or the overlay stays forever.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:112`: "--start-time="{start_time}" --end-time="{end_time}" --project="{project_id}""
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:112`: "AND timestamp>=\"{start_time}\" AND timestamp<=\"{end_time}\"" --project="{project_id}""
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:230`: "    change, open a Pull Request (PR) on GitHub, and conclude the workflow (do"
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:227`: "3.  If the request asked for the fix to be submitted or applied ("fix it","
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:235`: "    one message away; do not open one (`SOUL.md` §3, item 3)."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skills so the overlay can retire.

Decision needed: yes

### conf-4a9226: gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security)

Which Workload Identity model is the default: KSA-impersonates-GSA (cluster: 'the recommended method') versus direct IAM binding on the KSA principal (platform: impersonation is legacy). For the same workload the Cluster Agent proposes creating a GSA plus a `roles/iam.workloadIdentityUser` binding, while the Platform Agent treats that as legacy and binds roles to the KSA principal; the user receives opposite recommendations depending on which agent answers.

Evidence:
- `agents/cluster/skills/gke-workload-security/SKILL.md:38`: "Google Service Accounts (GSAs). This is the recommended method for workloads to"
- `agents/platform/skills/gke-workload-security/SKILL.md:56`: "Kubernetes Service Account (KSA) principal directly is the current default, and"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:56`: "Google Service Accounts (GSAs). This is the recommended method for workloads to"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 3. The platform copy is right: direct IAM binding on the KSA principal is the current default and GSA impersonation is legacy, as gke-workload-identity says in both trees. Patch the cluster copy to match; report upstream.

Decision needed: yes

### conf-b5e384: gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security)

How many steps enable Calico network policy enforcement on a non-Dataplane-V2 cluster: upstream gives one command (the addon), the cluster copy requires two (addon, then node enforcement). Following upstream (lines 98-104), the agent enables the NetworkPolicy addon on the control plane only and reports enforcement as on, but NetworkPolicy objects are not enforced on nodes until `--enable-network-policy` / `spec.networkPolicy.enabled: true` is also set, so the default-deny policy that follows does nothing.

Evidence:
- `agents/cluster/skills/gke-workload-security/SKILL.md:99`: "On clusters without Dataplane V2 this is two sequential changes, in this order:"
- `third_party/google-skills/gke-workload-security/SKILL.md:98`: "**Enable Network Policy Enforcement:**"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:123`: "two sequential commands in this order: first enable the Calico addon on the"
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:136`: "    --enable-network-policy \"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. The cluster and platform copies are right (two ordered changes); only the upstream mirror is wrong. Report upstream; the overlay already fixes the shipped copy.

Decision needed: yes

### conf-e46fb2: gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security)

Where GKE Sandbox (gVisor) is enabled: a cluster-level `--enable-gke-sandbox` flag versus a node-pool `sandboxConfig`. GKE Sandbox is a node-pool setting (`gcloud container node-pools create --sandbox type=gvisor`); `gcloud container clusters update` has no `--enable-gke-sandbox` flag, so the route the platform/upstream copy gives (and the matching command in gke-platform-security line 118) fails, while the cluster copy's node-pool proposal is the working one.

Evidence:
- `agents/cluster/skills/gke-workload-security/SKILL.md:141`: "Propose a node pool with GKE Sandbox enabled (Config Connector"
- `agents/platform/skills/gke-workload-security/SKILL.md:153`: "(`--enable-gke-sandbox`) at the cluster control plane level are platform-level"
- `third_party/google-skills/gke-workload-security/SKILL.md:122`: "(`--enable-gke-sandbox`) at the cluster control plane level are platform-level"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): Option 3. The cluster copy is right: GKE Sandbox is a node-pool setting. Patch the platform copy (overlay) to drop the cluster-level flag; report upstream.

Decision needed: yes

### conf-cb2e3b: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

The default issue timestamp when the user gives none: current system time (platform) versus the crashing/pending pod's state-transition time, falling back to now (cluster). The same prompt produces two different 1-hour Cloud Logging windows (Step 2): the platform's, centred on now, misses the events of a crash older than 30 minutes that the cluster's window, centred on the crash, catches.

Evidence:
- `agents/platform/skills/gke-workload-troubleshooting/SKILL.md:53`: "        -   **No Time Provided (Default)**: Use current system time as"
- `agents/cluster/skills/gke-workload-troubleshooting/SKILL.md:36`: "     2. If there are crashing or pending containers, check their state transition timestamps (e.g. `status.containerStatuses[*].lastState.terminated.finishedAt` or `status.startTime`) and use that transition time as $T$."
- `third_party/google-skills/gke-workload-troubleshooting/SKILL.md:53`: "        -   **No Time Provided (Default)**: Use current system time as"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 3. The cluster copy gives the better default (centre the log window on the pod's last state transition, fall back to now). Patch the platform copy via its overlay to match; report upstream.

Decision needed: yes

### conf-fad338: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

How the time window is passed to `gcloud logging read`: `--start-time`/`--end-time` flags (upstream) versus `timestamp>=`/`timestamp<=` terms inside the filter (cluster). `gcloud logging read` has no `--start-time` or `--end-time` flag (it takes `--freshness` and a filter), so the upstream command exits with 'unrecognized arguments' and the historical-events path of Step 2 never runs.

Evidence:
- `third_party/google-skills/gke-workload-troubleshooting/SKILL.md:112`: "gcloud logging read "resource.type=\"k8s_cluster\" AND logName=\"projects/{project_id}/logs/events\" AND jsonPayload.involvedObject.namespace=\"{workload_namespace}\"" --start-time="{start_time}" --end-time="{end_time}" --project="{project_id}""
- `agents/cluster/skills/gke-workload-troubleshooting/SKILL.md:87`: "gcloud logging read "resource.type=\"k8s_cluster\" AND logName=\"projects/<project_id>/logs/events\" AND jsonPayload.involvedObject.namespace=\"<workload_namespace>\" AND timestamp>=\"[Start_Time]\" AND timestamp<=\"[End_Time]\"" --project="<project_id>""
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:112`: "AND timestamp>=\"{start_time}\" AND timestamp<=\"{end_time}\"" --project="{project_id}""

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. The cluster and platform copies are right (bounds inside the filter); only the upstream mirror is wrong. Report upstream.

Decision needed: yes

### conf-e9fbf7: gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

Upstream always opens a pull request with the fix; the shipped copy opens one only when the request asked for the fix to be submitted, and otherwise replies with the manifest. On an investigate-or-diagnose request, an agent following upstream writes a branch and pull request to the GitOps repository that nobody asked for, which the Platform Agent's SOUL.md section 3 forbids.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:230`: "    change, open a Pull Request (PR) on GitHub, and conclude the workflow (do"
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:227`: "3.  If the request asked for the fix to be submitted or applied ("fix it","
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:235`: "    one message away; do not open one (`SOUL.md` §3, item 3)."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 4. The shipped copy is right for this install (SOUL.md forbids an unrequested pull request). Keep the overlay; report upstream.

Decision needed: yes

### conf-0feb2d: gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability)

Whether control-plane metrics (APISERVER, SCHEDULER, CONTROLLER_MANAGER) are available on every cluster or on Standard clusters only. On an Autopilot cluster the Cluster Agent tells the user control-plane metrics are not an option and never proposes them, while the Platform Agent's golden path (an Autopilot config per gke-storage line 22) turns them on; the two agents give opposite answers on the same cluster.

Evidence:
- `agents/platform/skills/gke-observability/SKILL.md:35`: "The golden path adds three control-plane monitoring components not present in"
- `agents/cluster/skills/gke-observability/SKILL.md:96`: "For Standard clusters, you can enable collection of metrics from the Kubernetes API server, scheduler, and controller manager."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): Option 3. The platform copy is right on both points (Autopilot supports control-plane metrics; the golden-path component list is the full suite). Patch the cluster copy to propose the full list and drop the Standard-only wording.

Decision needed: yes

### conf-9a2485: gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability)

The value proposed for `monitoringConfig.enableComponents`: the full golden-path suite versus a four-item list. `enableComponents` is a replace-list, so a Config Connector change written from the cluster proposal sets exactly four components and switches off STORAGE/POD/DEPLOYMENT/HPA/KUBELET/DCGM workload metrics the platform golden path keeps on.

Evidence:
- `agents/platform/skills/gke-observability/SKILL.md:27`: "`monitoringConfig` components                       | SYSTEM_COMPONENTS, STORAGE, POD, DEPLOYMENT, STATEFULSET, DAEMONSET, HPA, JOBSET, CADVISOR, KUBELET, DCGM, APISERVER, SCHEDULER, CONTROLLER_MANAGER | Full suite including control-plane"
- `agents/cluster/skills/gke-observability/SKILL.md:98`: "Propose the monitoring components `SYSTEM_COMPONENTS`, `APISERVER`,"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): Option 3. The platform copy is right on both points (Autopilot supports control-plane metrics; the golden-path component list is the full suite). Patch the cluster copy to propose the full list and drop the Standard-only wording.

Decision needed: yes

### conf-e64b5d: gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability)

The minimum probe set a production container must have: liveness and readiness both, versus at least a readiness probe. Auditing a Deployment that has only a readiness probe, the Cluster Agent reports it compliant while the Platform Agent flags a missing liveness probe; the fleet gets two different verdicts on the same workload.

Evidence:
- `agents/platform/skills/gke-reliability/SKILL.md:198`: "3.  **Probes with Explicit Timeouts**: Every production container must have both"
- `agents/cluster/skills/gke-reliability/SKILL.md:97`: "2. **Probes for All Containers**: Every container in a production pod should have at least a readiness probe."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 3. Pick one audit bar for the fleet. We recommend the platform copy's stricter rule (both probes; a PDB on every 2+ replica production Deployment) and patching the cluster copy to match, so a per-cluster audit and a fleet audit agree.

Decision needed: yes

### conf-a22a9b: gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability)

Which workloads need a PodDisruptionBudget: every production workload with 2+ replicas, versus critical apps only. A multi-replica non-critical Deployment without a PDB is a finding for the Platform Agent and not for the Cluster Agent, so a fleet audit and a per-cluster audit of the same cluster disagree.

Evidence:
- `agents/platform/skills/gke-reliability/SKILL.md:86`: "> Every production Deployment with 2+ replicas should have a PDB."
- `agents/cluster/skills/gke-reliability/SKILL.md:98`: "3. **PDBs for Critical Apps**: Use PDBs to prevent downtime during automated node upgrades."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): Option 3. Pick one audit bar for the fleet. We recommend the platform copy's stricter rule (both probes; a PDB on every 2+ replica production Deployment) and patching the cluster copy to match, so a per-cluster audit and a fleet audit agree.

Decision needed: yes

### conf-dd74e6: gke-storage (agents/cluster/skills/gke-storage), gke-storage (agents/platform/skills/gke-storage)

The name of GKE's built-in Filestore ReadWriteMany StorageClass: `standard-rwx` versus `standard-rwm`. A PVC proposed from the cluster copy references a StorageClass GKE does not ship, so it stays Pending with 'storageclass.storage.k8s.io "standard-rwm" not found'.

Evidence:
- `agents/platform/skills/gke-storage/SKILL.md:93`: "  storageClassName: standard-rwx"
- `agents/cluster/skills/gke-storage/SKILL.md:55`: "  storageClassName: standard-rwm # Pre-defined for Filestore"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (confident): Option 1. The platform copy is right (standard-rwx is the built-in Filestore class; premium-rwo is a built-in zonal pd-ssd class). Retire the cluster copy, which the unuseful-skill finding also recommends.

Decision needed: yes

### conf-8c70b6: gke-storage (agents/cluster/skills/gke-storage), gke-storage (agents/platform/skills/gke-storage)

What `premium-rwo` is: GKE's built-in zonal pd-ssd class, versus a custom regional-pd class the cluster copy asks the agent to create under that name. Applying the cluster manifest collides with the built-in `premium-rwo` (StorageClass parameters are immutable, so the apply is rejected), and an agent holding both copies has two definitions of what `premium-rwo` provisions (zonal versus regional pd-ssd, cluster line 30).

Evidence:
- `agents/platform/skills/gke-storage/SKILL.md:46`: "`premium-rwo`  | `pd-ssd`              | High IOPS, databases"
- `agents/cluster/skills/gke-storage/SKILL.md:26`: "  name: premium-rwo"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): Option 1. The platform copy is right (standard-rwx is the built-in Filestore class; premium-rwo is a built-in zonal pd-ssd class). Retire the cluster copy, which the unuseful-skill finding also recommends.

Decision needed: yes

### conf-937bf6: capacity-obtainability, gke-stockout-investigator

The two copies of Diagnostics B state opposite things about whether a reservation guarantees capacity: capacity-obtainability forbids the word and says a reservation only holds capacity, the stockout investigator says reservations guarantee compute capacity. An agent running the stockout investigator copies the 'guarantee' framing into the remediation PR and chat notification, telling the SRE that a reservation guarantees capacity, which is the claim capacity-obtainability was edited to forbid because a reservation does not make a stocked-out shape appear.

Evidence:
- `capacity-obtainability/SKILL.md:361`: "Check if any zonal reservations are available for the target workload's machine type; a reservation holds capacity for it (the report must not describe this as a guarantee):"
- `capacity-obtainability/SKILL.md:49`: "**Never use the word "guarantee" about capacity, allocations, or scheduling anywhere in the report** — not even for reservations or ProvisioningRequests;"
- `gke-stockout-investigator/SKILL.md:159`: "Check if any zonal reservations are available for the target workload's machine type to guarantee compute capacity:"

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (likely): Option 3. capacity-obtainability is right: a reservation holds capacity and the report must never say "guarantee". Patch line 159 of gke-stockout-investigator to the same wording.

Decision needed: yes

### conf-bbee9a: review-security-k8s-agents-firewall, review-security-k8s-network

The threshold for flagging a NodePort Service differs: network flags every NodePort unconditionally, firewall flags NodePort on agent containers only when a strict ingress NetworkPolicy is missing. For an agent pod exposed by NodePort behind a strict ingress NetworkPolicy, the two sub-skills return contradictory findings to review-security-k8s-main (one flags, one is silent), and the triage step has no rule to say which is right.

Evidence:
- `review-security-k8s-agents-firewall/SKILL.md:21`: "**Bypass Prevention**: Flag LoadBalancer or NodePort exposure on main agent containers lacking strict ingress NetworkPolicies."
- `review-security-k8s-network/SKILL.md:16`: "**NodePort Usage**: Flag `NodePort` usage (bypasses standard protections)."

Options:
1. Keep A, retire B.
2. Keep B, retire A.
3. Keep both, and write a local patch that reconciles them.
4. Open an issue upstream, and patch locally meanwhile.

**Recommendation** (unsure): Option 3. Decide one NodePort rule for the review family. We lean to the firewall skill's conditional rule (flag NodePort only without a strict ingress NetworkPolicy) and patching review-security-k8s-network to match, but the stricter unconditional rule is defensible for a general audit.

Decision needed: yes

## 3. Out of date

These skills are behind their source, or describe things that have since changed.

### old-1aab6b: gke-observability (agents/cluster/skills/gke-observability)

The skill limits control-plane metrics to Standard clusters, so the agent will skip proposing them on Autopilot clusters, where GKE also supports APISERVER, SCHEDULER and CONTROLLER_MANAGER metrics. The repo's own Autopilot golden-path asset enables all three.

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:96`: "For Standard clusters, you can enable collection of metrics from the Kubernetes API server, scheduler, and controller manager."
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:118`: "4. **Control Plane Metrics**: Enable control plane metrics (if using Standard) to monitor the health of the API server and scheduler."
- `gke-observability (agents/cluster/skills/gke-observability)/../../../platform/skills/gke-golden-path/assets/golden-path-autopilot.yaml:120`: "- APISERVER"

**Recommendation** (confident): Drop the Standard-only qualifier in section 8 and best practice 4; control-plane metrics are available on both Autopilot and Standard clusters (GKE 1.22.13+).

Decision needed: no

### old-b9e025: gke-storage (agents/cluster/skills/gke-storage)

The example PVC names a StorageClass that GKE does not predefine. GKE's built-in Filestore classes are `standard-rwx` and `premium-rwx` (plus `enterprise-rwx`, `enterprise-multishare-rwx`, `zonal-rwx`); a PVC asking for `standard-rwm` stays Pending with no matching StorageClass. The upstream copy in third_party/google-skills/gke-storage uses `standard-rwx`.

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:55`: "storageClassName: standard-rwm # Pre-defined for Filestore"

**Recommendation** (confident): If the file is kept, change `standard-rwm` to `standard-rwx`.

Decision needed: no

### old-651932: gke-workload-security (agents/cluster/skills/gke-workload-security)

The skill tells the agent that KSA-to-GSA impersonation via the iam.gke.io/gcp-service-account annotation is the recommended Workload Identity method. GKE now recommends granting IAM roles directly to the KSA principal (principal://iam.googleapis.com/projects/<number>/locations/global/workloadIdentityPools/<project>.svc.id.goog/subject/ns/<ns>/sa/<ksa>) and treats GSA impersonation as the legacy path; the repo's own upstream sibling skill gke-workload-identity says so. Proposals from this skill would steer clusters to the legacy setup.

Evidence:
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:37`: "Workload Identity allows Kubernetes Service Accounts (KSAs) to impersonate"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:38`: "Google Service Accounts (GSAs). This is the recommended method for workloads to"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:62`: "2. **Bind KSA to GSA:** propose granting `roles/iam.workloadIdentityUser` on"

**Recommendation** (confident): Rewrite section 2 to propose direct IAM binding to the KSA principal as the default and present the GSA annotation path as legacy, or replace the section with a pointer to the Workload Identity skill, which already distinguishes direct binding from legacy impersonation.

Decision needed: no

### old-e716c6: fleet-audit

The module docstring of the harness is the first thing an agent or maintainer reads via `--help`-style inspection, and it describes a smaller CLI and a smaller stream set than the script now implements: it lists five subcommands where main() dispatches seven (`grep` and `draft` are missing, both relied on by SKILL.md for content mode and collector streams), names six streams where AUDITS registers nine (stockout-prevention, gcp-networking-fabric-audit, gce-compute-fleet-audit are absent), and says 'GitHub issue' where the skill now supports GitLab merge requests and GitHub Enterprise Server hosts.

Evidence:
- `fleet-audit/scripts/audit_report.py:5`: "Every autonomous audit watchdog (compliance, security patch, obtainability,"
- `fleet-audit/scripts/audit_report.py:17`: "Two-command lifecycle, plus three on-demand commands:"
- `fleet-audit/scripts/audit_report.py:26`: "    audit_report.py list      --audit <audit-id> [--prefix <repo-path>]"
- `fleet-audit/SKILL.md:340`: "./skills/fleet-audit/scripts/audit_report.py grep  --audit <audit-id> --pattern 'namespace: payments'"
- `fleet-audit/SKILL.md:376`: "`audit_report.py draft --audit <audit-id> --manifest-file <manifest> [--out <path>]` starts the"

**Recommendation** (confident): Update the docstring's usage block to list all seven subcommands (start, finish, remediate, fetch, list, grep, draft), name the nine registered streams (or point at AUDITS instead of enumerating), and say 'forge issue / pull or merge request' rather than 'GitHub issue'. SKILL.md itself is current; only the script header lags.

Decision needed: no

### old-cf6cda: gke-app-onboarding (agents/platform/skills/gke-app-onboarding), gke-app-onboarding (third_party/google-skills/gke-app-onboarding)

The sample manifest's placeholder image lives on gcr.io; Container Registry is shut down and Artifact Registry (REGION-docker.pkg.dev) is the supported registry, which is what SKILL.md itself and the comment one line above use. The shipped copy already moves the Node base image to node:26-slim; the golang:1.22 base and the gcr.io image path are still in both copies.

Evidence:
- `gke-app-onboarding (agents/platform/skills/gke-app-onboarding)/assets/deployment.yaml:27`: "        image: gcr.io/my-project/node-app@sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
- `gke-app-onboarding (third_party/google-skills/gke-app-onboarding)/SKILL.md:43`: "FROM golang:1.22 AS builder"
- `gke-app-onboarding (third_party/google-skills/gke-app-onboarding)/assets/Dockerfile:2`: "FROM node:18-slim"
- `gke-app-onboarding (third_party/google-skills/gke-app-onboarding)/assets/deployment.yaml:27`: "image: gcr.io/my-project/node-app@sha256:0123456789abcdef..."

**Recommendation** (confident): Replace the placeholder with a REGION-docker.pkg.dev path so the asset matches the Artifact Registry guidance in SKILL.md.

Decision needed: no

### old-05fae9: gke-basics (agents/platform/skills/gke-basics)

Autopilot clusters are charged the same $0.10 per cluster per hour management fee as Standard (one cluster is covered by the free tier); the reference tells the agent there is none, which skews any cost explanation built on it.

Evidence:
- `gke-basics (agents/platform/skills/gke-basics)/references/core-concepts.md:75`: "-   **Autopilot**: Pay for pod resource requests (vCPU, memory, ephemeral"
- `gke-basics (agents/platform/skills/gke-basics)/references/core-concepts.md:76`: "    storage). No cluster management fee."

**Recommendation** (confident): State that both modes carry the per-cluster management fee (free tier covers one zonal or Autopilot cluster) and that Autopilot additionally bills Pod requests (or node-based for hardware-rule ComputeClasses).

Decision needed: no

### old-51e150: gke-batch-hpc (agents/platform/skills/gke-batch-hpc)

The skill installs the standalone kubeflow/mpi-operator (which serves MPIJob v2beta1) but then tells the agent to use the Kubeflow Training Operator; the Training Operator only served MPIJob v1 and has since been superseded by Kubeflow Trainer v2 (TrainJob), so the instruction points at a component that does not serve the CRD shown.

Evidence:
- `gke-batch-hpc (agents/platform/skills/gke-batch-hpc)/SKILL.md:143`: "kubectl apply -f https://raw.githubusercontent.com/kubeflow/mpi-operator/master/deploy/v2beta1/mpi-operator.yaml"
- `gke-batch-hpc (agents/platform/skills/gke-batch-hpc)/SKILL.md:212`: "-   **MPI Workloads**: Use the **Kubeflow Training Operator** to orchestrate"

**Recommendation** (likely): Name one operator consistently: the MPI Operator for MPIJob v2beta1, or Kubeflow Trainer v2 if the team wants the current Kubeflow path, and pin the install manifest to a release tag instead of master.

Decision needed: no

### old-7457aa: gke-cluster-creation (agents/platform/skills/gke-cluster-creation)

On a regional Standard cluster --num-nodes is the node count per zone, so the template as written creates 9 nodes (3 zones x 3), not 3; an agent quoting the line under-states the cost of the recommended Standard template by 3x.

Evidence:
- `gke-cluster-creation (agents/platform/skills/gke-cluster-creation)/SKILL.md:186`: "requirements). Creates 3 nodes across zones by default."
- `gke-cluster-creation (agents/platform/skills/gke-cluster-creation)/SKILL.md:194`: "  --num-nodes 3 \"

**Recommendation** (confident): Say 'creates 3 nodes per zone (9 for a 3-zone region)' or change the template to --num-nodes 1, and align the MCP payload's initialNodeCount with the same note.

Decision needed: no

### old-ea1e0a: gke-manifest-generation (agents/platform/skills/gke-manifest-generation), gke-manifest-generation (third_party/google-skills/gke-manifest-generation)

The rule tells the agent that Autopilot raises requests to match higher limits and so inflates cost; Autopilot does the opposite (it lowers limits to equal requests, and only derives requests from limits when requests are absent), and clusters with Pod bursting (GKE 1.30.2-gke.1394000 and later) keep limits above requests. An agent following the sentence will refuse or rewrite valid burstable specs for the wrong reason. The same line is in the upstream mirror, so the fix belongs in an overlay patch and an upstream report.

Evidence:
- `gke-manifest-generation (agents/platform/skills/gke-manifest-generation)/SKILL.md:36`: "        limits must be equal. If they differ, Autopilot will automatically scale"
- `gke-manifest-generation (agents/platform/skills/gke-manifest-generation)/SKILL.md:37`: "        requests up to match limits, which can significantly increase costs."
- `gke-manifest-generation (third_party/google-skills/gke-manifest-generation)/SKILL.md:35`: "*GKE Autopilot*: Requests determine pod billing directly; requests and"
- `gke-manifest-generation (third_party/google-skills/gke-manifest-generation)/SKILL.md:36`: "limits must be equal. If they differ, Autopilot will automatically scale"
- `gke-manifest-generation (third_party/google-skills/gke-manifest-generation)/SKILL.md:37`: "requests up to match limits, which can significantly increase costs."

**Recommendation** (likely): Replace the two sentences with: Autopilot bills on requests; when limits differ from requests it sets limits equal to requests (requests are copied from limits only when requests are missing), except on clusters with Pod bursting where limits above requests are kept. Apply as an overlay patch since the file is a google/skills mirror.

Decision needed: no

### old-13f14a: gke-observability (agents/platform/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability)

The command labelled as enabling the golden-path metric setting (`advancedDatapathObservabilityConfig.enableMetrics`) uses the flag that enables Advanced Datapath Observability (the Hubble relay), not the metrics flag; an agent that runs it does not reach the golden-path state and turns on a different component. Verified against `gcloud container clusters update --help` in Google Cloud SDK 587.0.0: `--enable-dataplane-v2-metrics` exposes the flow metrics, `--enable-dataplane-v2-flow-observability` enables the real-time pod-to-pod view.

Evidence:
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:61`: "# Enable Dataplane V2 observability metrics"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:63`: "  --enable-dataplane-v2-flow-observability \"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:29`: "`advancedDatapathObservabilityConfig.enableMetrics` | `true`                                                                                                                                              | Dataplane V2 flow metrics"

**Recommendation** (confident): Change line 63 to `--enable-dataplane-v2-metrics`, which sets `advancedDatapathObservabilityConfig.enableMetrics`. Apply as an overlay patch.

Decision needed: no

### old-12b4ae: gke-platform-security (agents/platform/skills/gke-platform-security), gke-platform-security (third_party/google-skills/gke-platform-security)

`gcloud container clusters update` has no `--enable-gke-sandbox` flag (absent from `--help` in Google Cloud SDK 587.0.0). GKE Sandbox is enabled per node pool on Standard with `gcloud container node-pools create --sandbox type=gvisor`, and Autopilot offers gVisor with no cluster flag through `runtimeClassName: gvisor`. An agent running the command as written fails. The same line is in the upstream mirror, so the fix belongs in an overlay patch and an upstream report.

Evidence:
- `gke-platform-security (agents/platform/skills/gke-platform-security)/SKILL.md:116`: "# Enable GKE Sandbox (gVisor) runtime on an existing cluster"
- `gke-platform-security (agents/platform/skills/gke-platform-security)/SKILL.md:118`: "  --enable-gke-sandbox \"
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:116`: "# Enable GKE Sandbox (gVisor) runtime on an existing cluster"
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:117`: "gcloud container clusters update <CLUSTER_NAME> --region <REGION> \"
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:118`: "  --enable-gke-sandbox \"

**Recommendation** (confident): Replace the block with the node-pool form for Standard (`gcloud container node-pools create <POOL> --cluster <CLUSTER> --sandbox type=gvisor`) and a note that Autopilot needs only `runtimeClassName: gvisor`. Apply as an overlay patch.

Decision needed: no

### old-d4508b: gke-storage (agents/platform/skills/gke-storage), gke-storage (third_party/google-skills/gke-storage)

The built-in StorageClass table maps standard-rwo to pd-standard; on GKE standard-rwo provisions pd-balanced (the in-tree legacy class named standard is the pd-standard one). An agent reading this table will mis-describe existing PVCs and pick premium-rwo to avoid a slow disk it would not get.

Evidence:
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:45`: "`standard-rwo` | `pd-standard`         | Cost-effective, low IOPS"

**Recommendation** (confident): Change the row to standard-rwo = pd-balanced (general purpose) and, if a pd-standard class is wanted, name the legacy `standard` class or a custom class.

Decision needed: no

### old-e5c4a5: gke-upgrades (agents/platform/skills/gke-upgrades)

The skill mandates (MUST) a specific kubectl command for deprecated-API detection, and that command greps apiserver_request_total for a 'deprecated' label that metric does not carry. The agent will report 'no deprecated API usage' on every cluster. The metric that records deprecated API calls is apiserver_requested_deprecated_apis (gauge with group/version/resource/removed_release labels), present since Kubernetes 1.19.

Evidence:
- `gke-upgrades (agents/platform/skills/gke-upgrades)/SKILL.md:167`: "You MUST include specific `kubectl` commands for API deprecation checks, specifically: `kubectl get --raw /metrics | grep apiserver_request_total | grep deprecated` to check if any active workloads are using deprecated APIs."
- `gke-upgrades (agents/platform/skills/gke-upgrades)/references/checklists.md:14`: "- [ ] No deprecated API usage (check GKE deprecation insights dashboard or check metrics: `kubectl get --raw /metrics | grep apiserver_request_total | grep deprecated`)"
- `gke-upgrades (agents/platform/skills/gke-upgrades)/references/runbook-template.md:25`: "kubectl get --raw /metrics | grep apiserver_request_total | grep deprecated"

**Recommendation** (confident): Replace the command in all three places with `kubectl get --raw /metrics | grep apiserver_requested_deprecated_apis` (and keep the pointer to GKE Deprecation Insights for client attribution). Because this is a mirrored gke-* skill, make the change as an overlay patch via edit-mirrored-skill and file it upstream.

Decision needed: no

### old-6cf579: gke-workload-scaling (agents/platform/skills/gke-workload-scaling), gke-workload-scaling (third_party/google-skills/gke-workload-scaling)

The skill tells the agent that External metrics from Cloud Monitoring need no adapter; on GKE the external.metrics.k8s.io API is served by the Custom Metrics Stackdriver Adapter (or a Prometheus adapter), so an HPA written on this advice reports FailedGetExternalMetric until the adapter is deployed. The same line is in the upstream mirror, so the fix belongs in an overlay patch and an upstream report.

Evidence:
- `gke-workload-scaling (agents/platform/skills/gke-workload-scaling)/SKILL.md:62`: "**Custom Metrics & External Metrics:** For GKE, the modern and recommended approach for scaling based on Cloud Monitoring metrics (e.g., Pub/Sub queue length) is to use the **External** metric type, which is natively supported by the GKE control plane without requiring the Custom Metrics Adapter."
- `gke-workload-scaling (third_party/google-skills/gke-workload-scaling)/SKILL.md:64`: "length) is to use the **External** metric type, which is natively supported by"
- `gke-workload-scaling (third_party/google-skills/gke-workload-scaling)/SKILL.md:65`: "the GKE control plane without requiring the Custom Metrics Adapter. For"

**Recommendation** (likely): State that External metrics require the Custom Metrics Stackdriver Adapter (custom-metrics-stackdriver-adapter) deployed in the cluster, or Managed Service for Prometheus with its adapter.

Decision needed: no

### old-db732e: workload-rebalancing

The skill names Config Connector (KCC) as the component that performs the workload move. KCC reconciles Google Cloud resources from custom resources; it does not apply workload manifests across clusters. In this repository the GitOps reconciler (Config Sync, Argo CD or Flux, per docs/site deploy pages and the gcp-config-connector skill, which scopes KCC to provisioning/) is what applies the merged PR. An agent following this text will describe the wrong mechanism to the user and may look for KCC status where none exists.

Evidence:
- `workload-rebalancing/SKILL.md:8`: "**you** _declare_ the change as a single GitOps PR; **KCC** reconciles the actual move."
- `workload-rebalancing/SKILL.md:22`: "(The actual make-before-break ordering of the move is handled by KCC when it reconciles the PR, not by the agents.)"
- `workload-rebalancing/SKILL.md:54`: "KCC/Config Sync performs the move."

**Recommendation** (likely): Replace KCC with 'the GitOps reconciler (Config Sync, Argo CD or Flux)' in all three places; keep KCC only if the moved object is itself a Google Cloud resource expressed as a KCC manifest.

Decision needed: no

### old-04c923: gke-platform-security (third_party/google-skills/gke-platform-security)

The body routes Workload Identity to gke-workload-security while the description (same file) and the mirror's gke-workload-identity skill say Workload Identity has its own skill; an agent that follows the body lands on the legacy impersonation steps.

Evidence:
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:12`: "for Workload Identity (use gke-workload-identity) or workload-level security"
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:165`: "Service Accounts (`roles/iam.workloadIdentityUser`), refer to the"
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:166`: "`gke-workload-security` skill."

**Recommendation** (confident): Point line 166 (and line 23-25 in the intro) at gke-workload-identity. The repository overlay agents/platform/skill-overlays/gke-platform-security/0001-point-workload-identity-at-gke-workload-identity.patch already does this in the shipped copy; file it upstream so the overlay can retire.

Decision needed: no

### old-5a7c45: gke-productionize (third_party/google-skills/gke-productionize)

The security step routes Workload Identity to gke-platform-security and gke-workload-security although the mirror has a dedicated gke-workload-identity skill and both named skills say not to use them for Workload Identity.

Evidence:
- `gke-productionize (third_party/google-skills/gke-productionize)/SKILL.md:98`: "-   **Action**: You MUST run the `gke-platform-security` and"
- `gke-productionize (third_party/google-skills/gke-productionize)/SKILL.md:99`: "    `gke-workload-security` skills for Workload Identity, Network Policies, and"

**Recommendation** (confident): Name gke-workload-identity for the Workload Identity item and keep the other two for Network Policies and Shielded Nodes. The overlay agents/platform/skill-overlays/gke-productionize/0001-point-workload-identity-at-gke-workload-identity.patch already does this in the shipped copy; file upstream.

Decision needed: no

### old-1b10d8: gke-productionize (third_party/google-skills/gke-productionize)

The description tells the agent to hand scaling off to a skill named gke-scaling, which does not exist in the mirror (the body and the directory have gke-workload-scaling and gke-cluster-autoscaler), so the routing hint cannot be followed.

Evidence:
- `gke-productionize (third_party/google-skills/gke-productionize)/SKILL.md:5`: "(use specific domain skills like gke-scaling, gke-platform-security, gke-workload-security, gke-service-networking, gke-reliability instead)"
- `gke-productionize (third_party/google-skills/gke-productionize)/SKILL.md:77`: "-   **Action**: You MUST run the `gke-workload-scaling` skill for configuring"

**Recommendation** (confident): Replace gke-scaling in the description with gke-workload-scaling (and gke-cluster-autoscaler if cluster-level scaling is meant).

Decision needed: no

### old-da4e9e: gke-upgrades (third_party/google-skills/gke-upgrades)

The GPU rollback step uses a gcloud command that does not exist; the skill's own runbook template says so one file over, so an agent gets a command error at the moment production is blocked.

Evidence:
- `gke-upgrades (third_party/google-skills/gke-upgrades)/references/troubleshooting.md:191`: "   gcloud container node-pools upgrade NODE_POOL_NAME \"
- `gke-upgrades (third_party/google-skills/gke-upgrades)/references/runbook-template.md:58`: "# Upgrade (note: node pool upgrades use `clusters upgrade --node-pool`;"
- `gke-upgrades (third_party/google-skills/gke-upgrades)/references/runbook-template.md:59`: "# there is no `gcloud container node-pools upgrade` command)"

**Recommendation** (confident): Use gcloud container clusters upgrade CLUSTER_NAME --node-pool NODE_POOL_NAME --zone ZONE --cluster-version PREVIOUS_VERSION. The overlay agents/platform/skill-overlays/gke-upgrades/0005-roll-a-node-pool-back-with-clusters-upgrade-node.patch already fixes the shipped copy; file upstream so the overlay can retire.

Decision needed: no

### old-5c755f: gke-workload-identity (third_party/google-skills/gke-workload-identity)

The description (v1.0.1) routes Workload Identity setup here, but the body is a troubleshooting procedure that forbids creating bindings or annotations; an agent sent here to set up a KSA binding finds no setup workflow and is told to only propose commands.

Evidence:
- `gke-workload-identity (third_party/google-skills/gke-workload-identity)/SKILL.md:7`: "Configures and diagnoses Workload Identity Federation for GKE authentication failures for Pods"
- `gke-workload-identity (third_party/google-skills/gke-workload-identity)/SKILL.md:13`: "health. Use when setting up KSA/GSA bindings (`roles/iam.workloadIdentityUser`,"
- `gke-workload-identity (third_party/google-skills/gke-workload-identity)/SKILL.md:20`: "# GKE Workload Identity Federation Troubleshooting Skill"
- `gke-workload-identity (third_party/google-skills/gke-workload-identity)/SKILL.md:36`: "changes for a human to apply. It must **never** create or modify IAM bindings,"

**Recommendation** (likely): Either add a short setup section (direct principal binding first, legacy impersonation second, with the read-only boundary relaxed to 'propose unless asked to apply'), or narrow the description back to diagnosis and leave setup to gke-workload-security's section 2.

Decision needed: no

### old-48b66b: gke-workload-security (third_party/google-skills/gke-workload-security)

The body still teaches GSA impersonation as 'the recommended method' and keeps a full setup section, while the description and the mirror's gke-workload-identity skill call impersonation legacy and direct principal binding the default; an agent routed here configures the older model.

Evidence:
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:11`: "configuring network policies and secret volume mounts. Don't use for Workload Identity (use gke-workload-identity), cluster-wide"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:55`: "Workload Identity allows Kubernetes Service Accounts (KSAs) to impersonate"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:56`: "Google Service Accounts (GSAs). This is the recommended method for workloads to"

**Recommendation** (likely): Retitle section 2 as the legacy impersonation path, point to gke-workload-identity for direct binding, or drop the section. The overlay agents/platform/skill-overlays/gke-workload-security/0002-point-workload-identity-at-gke-workload-identity.patch already does this in the shipped copy; file upstream.

Decision needed: no

### old-7250e9: gke-workload-security (third_party/google-skills/gke-workload-security)

Enabling Calico network policy on a non-Dataplane V2 cluster needs two sequential updates; the skill gives only the addon step, so enforcement never turns on and the skill's own audit script (which reads networkPolicy.enabled) then reports FAIL.

Evidence:
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:98`: "**Enable Network Policy Enforcement:**"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:102`: "    --update-addons=NetworkPolicy=ENABLED \"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/scripts/audit_cluster.sh:25`: "    (.networkPolicy.enabled // "FALSE" | tostring),"

**Recommendation** (confident): Add the second command, gcloud container clusters update CLUSTER --enable-network-policy, after the addon step, and check networkConfig.datapathProvider first. The overlay agents/platform/skill-overlays/gke-workload-security/0001-enforce-networkpolicy-in-two-steps-on-non-dpv2-c.patch already carries this; file upstream.

Decision needed: no

### old-c97f33: gke-workload-security (third_party/google-skills/gke-workload-security)

The parenthetical repeats a cluster-level --enable-gke-sandbox flag that gcloud does not have; GKE Sandbox is a node-pool setting on Standard and implicit on Autopilot.

Evidence:
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:121`: "Enabling Shielded Nodes (`--enable-shielded-nodes`) and GKE Sandbox"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:122`: "(`--enable-gke-sandbox`) at the cluster control plane level are platform-level"

**Recommendation** (likely): Say that a Standard cluster needs a node pool created with --sandbox type=gvisor (see gke-platform-security) and Autopilot needs only runtimeClassName: gvisor.

Decision needed: no

### old-91907e: gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

The Endpoints API is deprecated since Kubernetes 1.33 in favour of EndpointSlices; kubectl get endpoints now prints a deprecation warning and will stop being the right read for dual-stack and large services.

Evidence:
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:186`: "kubectl get endpoints {target_service_name} -n {target_namespace}"
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:211`: "    -   Present the exact `kubectl get endpoints` and `kubectl get"

**Recommendation** (confident): Use kubectl get endpointslices -l kubernetes.io/service-name={target_service_name} -n {target_namespace} in Step 4 and in the dry-run text.

Decision needed: no

## 4. Duplicates

These skills cover the same ground: 0 or 1 star in the coverage matrix (see the
appendix). Keeping both wastes the agent's attention and lets them drift apart.

### dup-643247: gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu), gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)/SKILL.md:5`: "description: >-"
- `gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)/SKILL.md:5`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-09f37b: gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption), gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption)/SKILL.md:5`: "description: >-"
- `gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption)/SKILL.md:5`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-b868a4: gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom), gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom)/SKILL.md:3`: "description: >-"
- `gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-6612b2: gke-compute-classes (agents/platform/skills/gke-compute-classes), gke-compute-classes (third_party/google-skills/gke-compute-classes)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-compute-classes (agents/platform/skills/gke-compute-classes)/SKILL.md:3`: "description: >-"
- `gke-compute-classes (third_party/google-skills/gke-compute-classes)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-1f9b50: gke-cost-analysis (agents/platform/skills/gke-cost-analysis), gke-cost-analysis (third_party/google-skills/gke-cost-analysis)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-cost-analysis (agents/platform/skills/gke-cost-analysis)/SKILL.md:5`: "description: >-"
- `gke-cost-analysis (third_party/google-skills/gke-cost-analysis)/SKILL.md:5`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-648d40: gke-cost-optimization (agents/platform/skills/gke-cost-optimization), gke-cost-optimization (third_party/google-skills/gke-cost-optimization)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-cost-optimization (agents/platform/skills/gke-cost-optimization)/SKILL.md:3`: "description: >-"
- `gke-cost-optimization (third_party/google-skills/gke-cost-optimization)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-45c55e: gke-golden-path (agents/platform/skills/gke-golden-path), gke-golden-path (third_party/google-skills/gke-golden-path)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-golden-path (agents/platform/skills/gke-golden-path)/SKILL.md:3`: "description: >-"
- `gke-golden-path (third_party/google-skills/gke-golden-path)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-1e7056: gke-inference (agents/platform/skills/gke-inference), gke-inference (third_party/google-skills/gke-inference)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-inference (agents/platform/skills/gke-inference)/SKILL.md:3`: "description: >-"
- `gke-inference (third_party/google-skills/gke-inference)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-25acb5: gke-multitenancy (agents/platform/skills/gke-multitenancy), gke-multitenancy (third_party/google-skills/gke-multitenancy)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-multitenancy (agents/platform/skills/gke-multitenancy)/SKILL.md:3`: "description: >-"
- `gke-multitenancy (third_party/google-skills/gke-multitenancy)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-81b83e: gke-observability (agents/platform/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:3`: "description: >-"
- `gke-observability (third_party/google-skills/gke-observability)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-b69159: gke-reliability (agents/platform/skills/gke-reliability), gke-reliability (third_party/google-skills/gke-reliability)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:3`: "description: >-"
- `gke-reliability (third_party/google-skills/gke-reliability)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-7e054c: gke-service-networking (agents/platform/skills/gke-service-networking), gke-service-networking (third_party/google-skills/gke-service-networking)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-service-networking (agents/platform/skills/gke-service-networking)/SKILL.md:5`: "description: >-"
- `gke-service-networking (third_party/google-skills/gke-service-networking)/SKILL.md:5`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-210197: gke-storage (agents/platform/skills/gke-storage), gke-storage (third_party/google-skills/gke-storage)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:3`: "description: >-"
- `gke-storage (third_party/google-skills/gke-storage)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-01b7c5: gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring), gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring)/SKILL.md:3`: "description: >-"
- `gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-8d741a: gke-tpu-metrics-monitoring (agents/platform/skills/gke-tpu-metrics-monitoring), gke-tpu-metrics-monitoring (third_party/google-skills/gke-tpu-metrics-monitoring)

The two folders are the same byte for byte. This is by design: the shipped copy under agents/platform/skills is generated from the upstream mirror under third_party/google-skills with no overlay. Nothing is wrong today, but any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-tpu-metrics-monitoring (agents/platform/skills/gke-tpu-metrics-monitoring)/SKILL.md:3`: "description: >-"
- `gke-tpu-metrics-monitoring (third_party/google-skills/gke-tpu-metrics-monitoring)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-c57a03: gke-app-onboarding (agents/platform/skills/gke-app-onboarding), gke-app-onboarding (third_party/google-skills/gke-app-onboarding)

0 stars: Every file is identical except assets/Dockerfile, where the shipped copy pins node:26-slim and upstream pins node:18-slim; same coverage. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-app-onboarding (agents/platform/skills/gke-app-onboarding)/SKILL.md:3`: "description: >-"
- `gke-app-onboarding (third_party/google-skills/gke-app-onboarding)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-0ce17e: gke-backup-dr (agents/platform/skills/gke-backup-dr), gke-backup-dr (third_party/google-skills/gke-backup-dr)

0 stars: Upstream source vs the shipped copy of the same Backup for GKE skill; the bodies read the same, the shipped copy differing only by a three-line overlay (one extra --volume-data-restore-policy flag, a note that gcloud beta is preinstalled and 'gcloud components install' is refused by the credential proxy, and a repaired heading), not an added section. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-backup-dr (agents/platform/skills/gke-backup-dr)/SKILL.md:3`: "description: >-"
- `gke-backup-dr (third_party/google-skills/gke-backup-dr)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-57ee22: gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler), gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler)

0 stars: Upstream source vs the shipped copy of the same skill: the overlay only renames the gke-compute-class reference to gke-compute-classes, adds a '(Standard clusters only)' qualifier to one gcloud line and drops an unused variable in a script; the bodies read the same and no section is added. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler)/SKILL.md:5`: "description: >-"
- `gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler)/SKILL.md:5`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-b7c478: gke-manifest-generation (agents/platform/skills/gke-manifest-generation), gke-manifest-generation (third_party/google-skills/gke-manifest-generation)

0 stars: Upstream source vs the shipped copy; the bodies read the same apart from four overlay substitutions (stdout redirect for gcloud, a Config Connector routing sentence, a neutral ServiceAccount name, search_documents before answer_query) and no added section. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-manifest-generation (agents/platform/skills/gke-manifest-generation)/SKILL.md:5`: "description: >-"
- `gke-manifest-generation (third_party/google-skills/gke-manifest-generation)/SKILL.md:5`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-13c04c: gke-productionize (agents/platform/skills/gke-productionize), gke-productionize (third_party/google-skills/gke-productionize)

0 stars: Upstream source vs shipped copy; the 142-line bodies are identical except a one-line overlay patch that routes Workload Identity to gke-workload-identity instead of gke-platform-security, no section added. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-productionize (agents/platform/skills/gke-productionize)/SKILL.md:5`: "description: Orchestrates comprehensive production readiness reviews and assessments for GKE clusters and workloads across scalability, security, reliability, observability, backup/DR, and cost optimi"
- `gke-productionize (third_party/google-skills/gke-productionize)/SKILL.md:5`: "description: Orchestrates comprehensive production readiness reviews and assessments for GKE clusters and workloads across scalability, security, reliability, observability, backup/DR, and cost optimi"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-05949d: gke-basics (agents/platform/skills/gke-basics), gke-basics (third_party/google-skills/gke-basics)

1 star: Upstream source vs shipped copy: the shipped SKILL.md carries two overlay patches that add the per-target KUBECONFIG export under $HERMES_HOME/.kubeconfigs/ to the get-credentials step and rank Developer Knowledge MCP first in the tool hierarchy; otherwise the bodies read the same, so the shipped copy is a superset. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-basics (agents/platform/skills/gke-basics)/SKILL.md:6`: "description: >-"
- `gke-basics (third_party/google-skills/gke-basics)/SKILL.md:6`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-b1dca1: gke-batch-hpc (agents/platform/skills/gke-batch-hpc), gke-batch-hpc (third_party/google-skills/gke-batch-hpc)

1 star: Upstream source versus the shipped copy: the bodies are identical except that the shipped copy appends a kube-agents section routing GPU/TPU deadline jobs to capacity-obtainability, so the shipped copy covers everything upstream does and more. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-batch-hpc (agents/platform/skills/gke-batch-hpc)/SKILL.md:3`: "description: >-"
- `gke-batch-hpc (third_party/google-skills/gke-batch-hpc)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-823681: gke-cluster-creation (agents/platform/skills/gke-cluster-creation), gke-cluster-creation (third_party/google-skills/gke-cluster-creation)

1 star: The shipped copy is the upstream body verbatim plus three appended local sections (Cluster Agent profile create at creation, profile delete at teardown, and loading capacity-obtainability before recommending GPU/TPU capacity), so the shipped copy is a strict superset. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-cluster-creation (agents/platform/skills/gke-cluster-creation)/SKILL.md:3`: "description: >-"
- `gke-cluster-creation (third_party/google-skills/gke-cluster-creation)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-abe210: gke-networking (agents/platform/skills/gke-networking), gke-networking (third_party/google-skills/gke-networking)

1 star: Upstream source vs shipped copy: the shipped SKILL.md is the upstream body verbatim plus one appended local section on checking controlPlaneEndpointsConfig before --dns-endpoint and gke_endpoint.py. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-networking (agents/platform/skills/gke-networking)/SKILL.md:3`: "description: >-"
- `gke-networking (third_party/google-skills/gke-networking)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-ed076d: gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability)

1 star: The cluster copy is a hand-trimmed subset of the platform skill: same audit of loggingConfig/monitoringConfig, Managed Prometheus, control-plane metrics, Dataplane V2 observability, LQL examples, tracing and profiling, with changes expressed as Config Connector proposals instead of gcloud update commands, while the platform skill adds key-metric and alert-threshold tables, node-health metrics, audit-log queries, kubectl top and cost notes. The cluster copy is a hand-maintained read-only variant of the platform copy, and the two have already drifted apart on facts (see the conflicts that name this pair).

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:3`: "description: Workflows for setting up and auditing observability (logging, monitoring, tracing) on GKE."
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:3`: "description: >-"
- `gke-observability (third_party/google-skills/gke-observability)/SKILL.md:3`: "description: >-"

**Recommendation** (likely): Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platform copy now (the conflicts above list the lines) and consider generating it from the platform copy with a read-only overlay so they cannot drift again.

Decision needed: yes

### dup-cb4e8f: gke-platform-security (agents/platform/skills/gke-platform-security), gke-platform-security (third_party/google-skills/gke-platform-security)

1 star: The shipped copy is the upstream body plus a routing patch to gke-workload-identity and an appended section on --database-encryption-key (Cloud KMS) and --security-posture; the upstream copy has neither, so the shipped copy is a strict superset. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-platform-security (agents/platform/skills/gke-platform-security)/SKILL.md:3`: "description: >-"
- `gke-platform-security (third_party/google-skills/gke-platform-security)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-6ba2a7: gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability), gke-reliability (third_party/google-skills/gke-reliability)

1 star: The cluster copy is a hand-trimmed subset of the platform SKILL.md: same six workflows (regional check, PDB, probes, SIGTERM, topology spread, maintenance window) while the platform copy adds golden-path defaults, full probe YAML, a preStop hook, hostname spread and a minimum-replica table; the only cluster-side addition is a one-paragraph Config Connector recurringWindow proposal. The cluster copy is a hand-maintained read-only variant of the platform copy, and the two have already drifted apart on facts (see the conflicts that name this pair).

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:3`: "description: Workflows for ensuring high availability and reliability of GKE workloads."
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:3`: "description: >-"
- `gke-reliability (third_party/google-skills/gke-reliability)/SKILL.md:3`: "description: >-"

**Recommendation** (likely): Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platform copy now (the conflicts above list the lines) and consider generating it from the platform copy with a read-only overlay so they cannot drift again.

Decision needed: yes

### dup-cc232f: gke-storage (agents/cluster/skills/gke-storage), gke-storage (agents/platform/skills/gke-storage), gke-storage (third_party/google-skills/gke-storage)

1 star: The platform copy covers everything in the cluster copy (pd-ssd regional StorageClass, CSI driver choice, Filestore RWX PVC, PVC expansion, best practices) and adds the built-in StorageClass table, a GCS FUSE mount manifest, MCP patch tooling and a backup pointer. The cluster copy adds no house rule of its own and is write-path guidance in the read-only Cluster Agent profile.

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:3`: "description: Guidance on managing storage in Google Kubernetes Engine (GKE) clusters."
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:3`: "description: >-"
- `gke-storage (third_party/google-skills/gke-storage)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep the platform copy (generated from the upstream source of truth). Remove the cluster copy; if the Cluster Agent needs storage help, it needs a read-only storage-binding diagnostic, which this file is not.

Decision needed: yes

### dup-74b14d: gke-upgrades (agents/platform/skills/gke-upgrades), gke-upgrades (third_party/google-skills/gke-upgrades)

1 star: The shipped platform copy is the upstream SKILL.md plus five small patches and an appended fleet-upgrade-verification section (diff confirmed), so the platform skill covers everything the third_party copy does and more. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-upgrades (agents/platform/skills/gke-upgrades)/SKILL.md:6`: "description: >-"
- `gke-upgrades (third_party/google-skills/gke-upgrades)/SKILL.md:6`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-50a096: gke-workload-identity (agents/platform/skills/gke-workload-identity), gke-workload-identity (third_party/google-skills/gke-workload-identity)

1 star: Upstream source vs the shipped copy: bodies are identical except the shipped copy appends a 'Reads this install withholds' section naming the three commands the Platform Agent's command gate refuses and how to hand them to the user. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-workload-identity (agents/platform/skills/gke-workload-identity)/SKILL.md:6`: "description: >-"
- `gke-workload-identity (third_party/google-skills/gke-workload-identity)/SKILL.md:6`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-3f0ff2: gke-workload-scaling (agents/platform/skills/gke-workload-scaling), gke-workload-scaling (third_party/google-skills/gke-workload-scaling)

1 star: Diff shows the shipped platform copy is the upstream body byte-for-byte plus one injected footer section (load capacity-obtainability before GPU/TPU or large-shape scale-ups), so upstream is a strict subset. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-workload-scaling (agents/platform/skills/gke-workload-scaling)/SKILL.md:3`: "description: >-"
- `gke-workload-scaling (third_party/google-skills/gke-workload-scaling)/SKILL.md:3`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-b3b16d: gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security)

1 star: The Cluster Agent copy keeps every section of the platform copy (audit script, legacy Workload Identity, DPv2 check plus two-step Calico, default-deny, gVisor, PSS labels, SecretProviderClass, NetworkLogging) rewritten as manifest or Config Connector proposals, and adds Shielded Nodes and a gVisor node pool that the platform copy routes to gke-platform-security. The cluster copy is a hand-maintained read-only variant of the platform copy, and the two have already drifted apart on facts (see the conflicts that name this pair).

Evidence:
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:3`: "description: Workflows for auditing and hardening the security of GKE workloads."
- `gke-workload-security (agents/platform/skills/gke-workload-security)/SKILL.md:3`: "description: >-"
- `gke-workload-security (third_party/google-skills/gke-workload-security)/SKILL.md:3`: "description: >-"

**Recommendation** (likely): Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platform copy now (the conflicts above list the lines) and consider generating it from the platform copy with a read-only overlay so they cannot drift again.

Decision needed: yes

### dup-1cf49e: gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

1 star: The platform copy is the upstream file plus two patches (a timestamp filter inside the logging query and a step-5 gate that opens a PR only when the request asked for a fix), so it covers everything the third_party copy does and more. This is by design: the shipped copy is generated from the upstream mirror plus an overlay patch. Any edit made directly to the shipped copy is lost on the next make skills-refresh.

Evidence:
- `gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)/SKILL.md:5`: "description: >-"
- `gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)/SKILL.md:5`: "description: >-"

**Recommendation** (confident): Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirrored-skill). No file change.

Decision needed: no

### dup-89a268: review-security-k8s-agents-main, review-security-k8s-main

1 star: Same four-step workflow (take context, launch sub-skills in parallel with the identical JSON findings schema, triage against context, merge), and main launches agents-main as one of its ten sub-skills, so main covers everything agents-main does and more.

Evidence:
- `review-security-k8s-agents-main/SKILL.md:3`: "description: Orchestrates comprehensive Kubernetes security audits specifically tailored for AI agent workloads."
- `review-security-k8s-main/SKILL.md:3`: "description: Orchestrates comprehensive Kubernetes security reviews."

**Recommendation** (confident): Keep both. review-security-k8s-main launches review-security-k8s-agents-main as one of its sub-skills, so the shared orchestration text is the protocol they agree on, not a copy to remove. No file change.

Decision needed: no

## 5. Missing pieces

These skills point at files or other skills that are not here.

Nothing found.

## 6. Unuseful or out of place

These skills do not belong in this repo, add nothing beyond what the model
already does unprompted, or cannot be loaded because their front matter does
not parse. A useful skill carries the team's preference, workflow, methodology
or house rule; one that only repeats how a tool works is unuseful, and one that
buries a preference in general text should be cut down to it.

### low-0ab013: review-security-k8s-agents-prompt-injection

The skill is two generic bullets that any capable model produces when asked to review an agent deployment for prompt injection; it names no field, resource, threshold or repo default to look for, so it adds tokens to the orchestrator fan-out without changing what the reviewer does.

Evidence:
- `review-security-k8s-agents-prompt-injection/SKILL.md:10`: "- **Gateway/WAF**: Require LLM-specific API Gateway or WAF sidecar. Flag raw agent APIs exposed to untrusted traffic."
- `review-security-k8s-agents-prompt-injection/SKILL.md:11`: "- **Guardrails**: Ensure system prompts/safety instructions in `ConfigMaps`/`EnvVars` cannot be tampered with by less privileged workloads."

**Recommendation** (likely): Remove the skill. If the ConfigMap/EnvVar tamper check is wanted, move that one bullet into review-security-k8s-agents-credentials (it is an RBAC-on-config check) and delete the entry from the parallel list in review-security-k8s-agents-main/SKILL.md line 17.

Decision needed: yes

### low-afb095: review-security-k8s-rbac

`resources/gke-rbac.md` is a 435-line verbatim copy of the public GKE RBAC best-practices page; every actionable item in it is already encoded as a check in SKILL.md, so the copy costs tokens on every load and will drift from the source without adding a team preference.

Evidence:
- `review-security-k8s-rbac/resources/gke-rbac.md:1`: "2026-05-21 copy of Best practices for GKE RBAC from https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac"
- `review-security-k8s-rbac/SKILL.md:34`: "Refer to `resources/gke-rbac.md` for additional guidance. Identify if any of this guidance is both relevant and missing from your review and include those findings as well."

**Recommendation** (likely): Keep SKILL.md's check list (sections 1-4) as the team's RBAC baseline; replace the vendor-page copy with a one-line pointer to the source URL, or trim it to the page's `Checklist summary` section only.

Decision needed: no

### low-d827f5: gke-observability (agents/cluster/skills/gke-observability)

Most of the file is generic GKE/Cloud Operations product description a model produces unprompted (what LQL is, use JSON logs, add OpenTelemetry and Cloud Profiler, make CPU/memory/latency/error dashboards). The repo-specific part, the read-only rule and the Config Connector proposal convention, is four short passages buried in it. Section 1 also tells the agent to look for fields its own command filters out: loggingService and monitoringService are top-level cluster fields, not members of loggingConfig/monitoringConfig, so the describe output as written never shows them.

Evidence:
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:78`: "Use Logging Query Language (LQL) in Cloud Logging to find specific logs."
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:66`: "- **Action**: Recommend using **OpenTelemetry** in the application to send traces to **Cloud Trace**."
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:10`: "> You are read-only: each change below is a proposal you report with your findings, never a command you run."
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:30`: "**To enable:** propose turning on Managed Service for Prometheus (Config"
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:21`: "gcloud container clusters describe <cluster-name> --region <region> --project <project-id> --format="json(loggingConfig, monitoringConfig)""
- `gke-observability (agents/cluster/skills/gke-observability)/SKILL.md:24`: "Look for `loggingService` and `monitoringService` to be set to something other than `none` (usually `logging.googleapis.com/kubernetes` and `monitoring.googleapis.com/kubernetes`)."

**Recommendation** (likely): Cut the skill to the audit checklist and the proposal convention: the read-only line, the describe command (with loggingService and monitoringService added to the format filter, or the check pointed at loggingConfig.componentConfig.enableComponents), the gmp-system check, and the three Config Connector ContainerCluster proposals. Drop sections 3 to 7 and the Best Practices list, which only restate how Cloud Logging, Cloud Trace, Cloud Profiler and Cloud Monitoring work.

Decision needed: no

### low-18cbaf: gke-reliability (agents/cluster/skills/gke-reliability)

Most of the file explains what PDBs, probes, terminationGracePeriodSeconds and topologySpreadConstraints are, which any capable model produces unprompted; the house rules (read-only proposal posture, the production must-haves, the Config Connector form for the maintenance window) are a few lines buried among them and cost the Cluster Agent context on every load.

Evidence:
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:29`: "PDBs ensure that a minimum number of pods are available during voluntary disruptions (like node upgrades)."
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:55`: "- **Readiness Probe**: Determines when a container is ready to start accepting traffic."
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:10`: "> You are read-only: each change below is a proposal you report with your findings, never a command you run."
- `gke-reliability (agents/cluster/skills/gke-reliability)/SKILL.md:90`: "**Maintenance window:** propose a recurring window with a start time, an end time and a"

**Recommendation** (likely): Cut the skill to the read-only banner, a checklist of the six checks with the one command each needs, the production must-haves from Best Practices, and the Config Connector form of the maintenance-window proposal; drop the concept explanations and the generic example manifests.

Decision needed: no

### low-cf1d60: gke-storage (agents/cluster/skills/gke-storage)

Every sentence restates GKE storage documentation or a generic recommendation; nothing in it is a team workflow, default or rule. The Cluster Agent's SOUL.md (line 25) expects it to diagnose 'storage binding', and this skill holds no diagnostic step at all (no PVC Pending, FailedAttachVolume, or provisioner-error path).

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:74`: "1. **Use CSI Drivers**: Always use the official Google Cloud CSI drivers for best integration and performance."
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:75`: "2. **Enable Volume Expansion**: Always set `allowVolumeExpansion: true` in your StorageClasses to allow for growth."
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:70`: "Kubernetes will automatically resize the file system on the volume."

**Recommendation** (confident): Remove the cluster copy. A capable model produces this content unprompted; if the Cluster Agent needs a storage skill, it needs a read-only storage-binding diagnostic (PVC/PV status, events, CSI driver pod health), which this file does not provide.

Decision needed: yes

### place-411e11: gke-storage (agents/cluster/skills/gke-storage)

agents/cluster/skills is for read-only, single-cluster runtime debugging. This skill is configuration-and-write guidance (author a StorageClass, apply a PVC, edit the PVC to resize), which belongs to the Platform Agent, and agents/platform/skills/gke-storage already carries a fuller version mirrored from google/skills.

Evidence:
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:3`: "description: Guidance on managing storage in Google Kubernetes Engine (GKE) clusters."
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:67`: "1. Edit the PVC manifest and increase the storage request."
- `gke-storage (agents/cluster/skills/gke-storage)/SKILL.md:68`: "2. Apply the changes."

**Recommendation** (likely): Do not keep write-path storage guidance in the Cluster Agent profile. Either drop it (see the low_value finding) or replace it with a diagnostic skill that fits the persona.

Decision needed: yes

### low-37403d: gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)

Most of the file is a generic HPA/VPA/Cluster Autoscaler primer a capable model produces unprompted; the repo-specific rules (read-only proposal framing, Config Connector field names, the asset manifests, the HPA-on-CPU/VPA-on-memory pattern) are a handful of lines buried inside it, so the skill spends context budget on text that adds nothing.

Evidence:
- `gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)/SKILL.md:22`: "Automatically scale the number of pods based on observed CPU utilization, memory utilization, or custom metrics."
- `gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)/SKILL.md:50`: "- `Off`: Calculates recommendations but does not apply them. Good for "dry run" analysis."
- `gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)/SKILL.md:10`: "> You are read-only: each change below is a proposal you report with your findings, never a command you run."
- `gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)/SKILL.md:46`: "Propose turning on vertical Pod autoscaling for the cluster (Config Connector `ContainerCluster` field `spec.verticalPodAutoscaling.enabled: true`)."

**Recommendation** (likely): Cut the skill down to what the team decided: the read-only proposal rule, the shape of each proposal (Deployment patch, HPA/VPA manifest with links to the two assets, Config Connector ContainerCluster/ContainerNodePool fields), and the metric-conflict pattern; drop the HPA/VPA definitions, the update-mode glossary and the generic best-practice bullets.

Decision needed: no

### place-69406c: gke-workload-security (agents/cluster/skills/gke-workload-security)

Sections 3 (Calico enablement), 4 and 5 propose cluster-level provisioning changes on Config Connector ContainerCluster/ContainerNodePool resources. Per the placement rules those are Platform Agent (provisioning, GitOps-write) concerns; the upstream skill routes Shielded Nodes and GKE Sandbox enablement to gke-platform-security, and the Cluster Agent copy dropped that routing note and added the sections instead. The 'propose, never run' framing softens this, but the Cluster Agent is scoped to read-only single-cluster runtime debugging and these proposals land in the Platform Agent's GitOps repository.

Evidence:
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:133`: "Propose enabling Shielded Nodes (Config Connector `ContainerCluster` field"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:141`: "Propose a node pool with GKE Sandbox enabled (Config Connector"
- `gke-workload-security (agents/cluster/skills/gke-workload-security)/SKILL.md:3`: "description: Workflows for auditing and hardening the security of GKE workloads."

**Recommendation** (unsure): Keep the workload-level items (default-deny NetworkPolicy, PSS labels, runtimeClassName, SecretProviderClass, NetworkLogging) in the Cluster Agent copy and reduce the cluster-level ContainerCluster/ContainerNodePool proposals to a one-line hand-off to the Platform Agent's gke-platform-security skill. The two-step Calico ordering is pinned by tests/test_skill_content.py, so decide with the owner whether that stays as a cluster-side proposal.

Decision needed: yes

### low-abea93: fleet-upgrade-verification

SKILL.md is 377 lines, and roughly 50 of them (the fail-closed webhook bullet, lines 210-259) restate Kubernetes admission mechanics (failurePolicy default, apiVersions and resource wildcard matching, served versions, namespaceSelector evaluation) that the script already encodes in `upgrade_readiness.py` and renders into the readiness cell. The skill itself tells the agent to take every per-object verdict from the table and never re-grade by hand, so that mechanics text is context the agent is instructed not to act on; it costs tokens on every load without changing behaviour.

Evidence:
- `fleet-upgrade-verification/SKILL.md:215`: "`admissionregistration.k8s.io/v1` defaults to `Fail`) and its backend is a Service the API"
- `fleet-upgrade-verification/SKILL.md:227`: "API group, API version, operation, resource (with the API's `*`, `*/*` and `pods/*` semantics)"
- `fleet-upgrade-verification/SKILL.md:366`: "yes, a webhook under `outage` is no, with the outage named; do not re-grade by hand. An exclusion"

**Recommendation** (likely): Keep the run commands, the flag semantics, the status/progress/readiness vocabulary (what each grade and cell means) and the Report section; cut the grading mechanics in the webhook and PDB bullets down to one sentence each that names the rule and points at `upgrade_readiness.py` (`UPGRADE_PATH_TARGETS`, `CONTROL_PLANE_*_WRITES`) and `docs/designs/upgrade-readiness-checks.md` for the derivation.

Decision needed: no

### place-30da22: gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu), gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)

The placement rule sends read-only, single-cluster runtime debugging to agents/cluster/skills. This skill is a per-cluster diagnostic (node labels, node taints, PromQL and log reads) and only recommends, never writes. It lives only in agents/platform/skills, where the mirror pipeline puts every gke-* copy, while the comparable gke-workload-troubleshooting is also shipped to the Cluster Agent.

Evidence:
- `gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)/SKILL.md:6`: "Diagnoses, predicts, and mitigates node disruptions during Compute Engine host maintenance and hardware or software maintenance events for GPU and TPU workloads on GKE."
- `gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)/SKILL.md:32`: "kubectl get nodes -l cloud.google.com/scheduled-maintenance-time -L cloud.google.com/scheduled-maintenance-time"

**Recommendation** (unsure): Ship it to the Cluster Agent profile as well (as gke-workload-troubleshooting is), or state why the Platform Agent runs this per-cluster diagnosis itself. Unsure because the mirror tooling targets agents/platform and the Platform Agent may use it for fleet-wide maintenance questions. Where a skill ships is a persona design choice, so this is left for you to decide.

Decision needed: yes

### place-71d24b: gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption), gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption)

The placement rule sends read-only, single-cluster runtime debugging to agents/cluster/skills. This skill reads one cluster's metrics and logs for one JobSet and only recommends actions; it lives only in agents/platform/skills, where the mirror pipeline puts every gke-* copy.

Evidence:
- `gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption)/SKILL.md:6`: "Diagnoses GKE JobSet interruptions, restarts, and preemptions for AI/ML training workloads autonomously."
- `gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption)/SKILL.md:70`: "| filter resource.cluster_name == '{cluster_name}' && metric.jobset_name == '{workload_name}'"

**Recommendation** (unsure): Ship it to the Cluster Agent profile as well, or state why the Platform Agent runs this per-cluster diagnosis itself. Unsure because the mirror tooling targets agents/platform. Where a skill ships is a persona design choice, so this is left for you to decide.

Decision needed: yes

### place-f7089e: gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom), gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom)

The skill is read-only, single-node runtime debugging (Cloud Logging filters plus a kubectl listing) with no fleet, provisioning or GitOps-write action; the repo's placement rule sends that kind of skill to the Cluster Agent, not the Platform Agent.

Evidence:
- `gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom)/SKILL.md:4`: "Diagnoses and prevents vbar_control_agent segfaults, out-of-memory (OOM) errors,"
- `gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom)/SKILL.md:9`: "collection conflicts on GKE TPU v6e nodes. Don't use for general non-TPU container"

**Recommendation** (likely): Decide whether the Cluster Agent profile should carry this runbook. It is a mirrored gke-* skill, so moving it means either mirroring into agents/cluster/skills/ (the mirror tooling only targets agents/platform/skills today) or dropping it from the platform image if TPU node debugging is delegated to the Cluster Agent. Where a skill ships is a persona design choice, so this is left for you to decide.

Decision needed: yes

### low-235c89: gke-app-onboarding (agents/platform/skills/gke-app-onboarding)

Most of the file is a generic Docker multi-stage build, Artifact Registry push and Deployment/Service tutorial that a capable model writes unprompted; the team's few preferences (MCP first, Gateway API for external, manifest checklist, skill hand-offs) are buried in it, and the bundled Node.js sample app is never referenced from SKILL.md.

Evidence:
- `gke-app-onboarding (agents/platform/skills/gke-app-onboarding)/SKILL.md:57`: "-   Use multi-stage builds to keep production images small"
- `gke-app-onboarding (agents/platform/skills/gke-app-onboarding)/SKILL.md:155`: "-   Service type appropriate (ClusterIP for internal, use Gateway API for"
- `gke-app-onboarding (agents/platform/skills/gke-app-onboarding)/assets/deployment.yaml:64`: "  type: LoadBalancer"

**Recommendation** (likely): Cut the skill down to the assessment questions, the manifest checklist, the MCP-first deploy step and the Next Steps hand-offs; drop the Dockerfile/docker push walkthrough, and either remove the unreferenced assets/ sample app or align its Service type with the Gateway API rule. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-414b06: gke-basics (agents/platform/skills/gke-basics)

Three of the five references (client libraries, Terraform IaC, core concepts) only restate Kubernetes and GKE product facts a model already knows, while the house rules live in SKILL.md and the tool-preference parts of cli-reference.md and mcp-usage.md.

Evidence:
- `gke-basics (agents/platform/skills/gke-basics)/references/client-library-usage.md:20`: "    pip install kubernetes"
- `gke-basics (agents/platform/skills/gke-basics)/references/iac-usage.md:25`: "  enable_autopilot = true"
- `gke-basics (agents/platform/skills/gke-basics)/references/mcp-usage.md:91`: "| `answer_query`     | READ | `query` (string) | Do not use. Its quota is 50 requests per day per project, shared by every agent in the install, and it reads the same corpus as `search_documents`. Never retry its `429 RESOURCE_EXHAUSTED`. |"

**Recommendation** (likely): Keep SKILL.md, the Tool Preference / user-override sections of cli-reference.md and the Developer Knowledge section of mcp-usage.md; drop client-library-usage.md and iac-usage.md, and fold the two non-generic lines of core-concepts.md (Autopilot default, golden-path private/Dataplane V2) into SKILL.md. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-67c9e2: gke-batch-hpc (agents/platform/skills/gke-batch-hpc)

The Job, JobSet, Kueue ClusterQueue/LocalQueue and MPIJob manifests and the compact-placement node-pool command are stock examples a capable model produces unprompted; the team's rules are the local capacity-obtainability addition and a handful of bullets under Best Practices and Cost Optimization.

Evidence:
- `gke-batch-hpc (agents/platform/skills/gke-batch-hpc)/SKILL.md:39`: "  parallelism: 10"
- `gke-batch-hpc (agents/platform/skills/gke-batch-hpc)/SKILL.md:225`: "especially one that must finish inside a horizon — load the"

**Recommendation** (likely): Keep the When-to-Use list, the Cost Optimization and Best Practices bullets and the capacity-obtainability section; replace the five YAML/CLI blocks with one-line pointers to the upstream Kueue, JobSet and MPI Operator docs. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-6cec87: gke-cost-optimization (agents/platform/skills/gke-cost-optimization), gke-cost-optimization (third_party/google-skills/gke-cost-optimization)

Most of the file explains GCP pricing products (CUDs, machine family cost tiers, Spot discounts, console paths) that a capable model states unprompted; the house rules (P95 * 1.2 thresholds, Spot warning, dev/test deviations) are a small fraction and sit between them.

Evidence:
- `gke-cost-optimization (agents/platform/skills/gke-cost-optimization)/SKILL.md:198`: "For steady-state workloads with predictable baseline usage, purchase 1-year or"
- `gke-cost-optimization (agents/platform/skills/gke-cost-optimization)/SKILL.md:102`: "CPU request >5x P95 actual    | Reduce to `P95 * 1.2`              | High"
- `gke-cost-optimization (agents/platform/skills/gke-cost-optimization)/SKILL.md:141`: "> explicitly warn users about this preemption risk when recommending Spot VMs."

**Recommendation** (likely): Keep the golden-path cost table, the optimization-rules table, the Spot ComputeClass with fallback plus the preemption warning, the dev/test deviation table and the pointer to gke-cost-analysis; drop the CUD, machine-family and generic cluster-management prose. This is a google/skills mirror, so the cut is an overlay patch under agents/platform/skill-overlays/gke-cost-optimization/. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-ba8315: gke-inference (agents/platform/skills/gke-inference), gke-inference (third_party/google-skills/gke-inference)

The accelerator catalogue, the LLM optimization tips (quantization, batching, tensor parallelism, KV cache) and the troubleshooting table are general knowledge a model produces unprompted; the team's preference is only the GIQ-first workflow, the ComputeClass and the DCGM autoscaling rules.

Evidence:
- `gke-inference (agents/platform/skills/gke-inference)/SKILL.md:186`: "-   **Quantization**: Use quantized models (GPTQ, AWQ) to reduce GPU memory and"
- `gke-inference (agents/platform/skills/gke-inference)/SKILL.md:14`: "This reference covers deploying AI/ML inference workloads on GKE using Google's"
- `gke-inference (agents/platform/skills/gke-inference)/SKILL.md:175`: "1.  **Use DCGM metrics**: Golden path enables DCGM monitoring for GPU"

**Recommendation** (likely): Keep the three-step GIQ workflow, the GPU ComputeClass and the inference-autoscaling best practices; drop the Accelerator Selection Guide, Optimization Tips and Troubleshooting sections. Mirror of google/skills, so apply as an overlay patch. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-788bf4: gke-multitenancy (agents/platform/skills/gke-multitenancy), gke-multitenancy (third_party/google-skills/gke-multitenancy)

The namespace, Role, ResourceQuota, LimitRange and NetworkPolicy examples are stock Kubernetes multi-tenancy that a model writes unprompted; the team's choices (namespace-per-team default, Google Groups subjects, mandatory LimitRange defaults, cost-center label) are a few lines among them.

Evidence:
- `gke-multitenancy (agents/platform/skills/gke-multitenancy)/SKILL.md:95`: "Prevent any single team from consuming all cluster resources:"
- `gke-multitenancy (agents/platform/skills/gke-multitenancy)/SKILL.md:43`: "> **Golden path recommendation**: Start with namespace-per-team for cost"
- `gke-multitenancy (agents/platform/skills/gke-multitenancy)/SKILL.md:89`: "**RBAC best practices:** Use Google Groups for subject bindings. Prefer"

**Recommendation** (likely): Keep the model table with its recommendation, the Google Groups and namespace-Role rule, the LimitRange mandatory-defaults note, the DNS allowance and the cost-center label convention; drop the boilerplate manifests. Mirror of google/skills, so apply as an overlay patch. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-e6fe3c: gke-networking (agents/platform/skills/gke-networking)

The VPC-native benefits, IP-planning arithmetic and egress bullets restate GKE documentation; the team's content is the golden-path table with Day-0/1 marks and the local `--dns-endpoint` pre-check, which sit around it.

Evidence:
- `gke-networking (agents/platform/skills/gke-networking)/SKILL.md:83`: "1.  **Scalability**: Traffic routes natively inside the VPC, bypassing the need"
- `gke-networking (agents/platform/skills/gke-networking)/SKILL.md:140`: "Do not infer support from the command succeeding. When external traffic is disabled, a caller that"
- `gke-networking (agents/platform/skills/gke-networking)/SKILL.md:24`: "Setting                                                              | Golden Path Value                  | Day-0/1 | Notes"

**Recommendation** (likely): Keep the golden-path table, the access-pattern commands, the BYO-VPC Day-0 warning and the local `--dns-endpoint` section; drop VPC-Native Mode Benefits, the IP Planning rule of thumb and Egress. Apply as an overlay patch (the local section already lives in skill-overlays/gke-networking/append.md). This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-3c8a48: gke-observability (agents/platform/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability)

Metric catalogues, LQL examples, pricing notes and tracing/profiling advice are standard Cloud Operations knowledge; the team's rules (component set, production dashboard and alert rules, node-health metric pairing, thresholds) are the minority of the text.

Evidence:
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:174`: "-   **Cloud Logging**: Charged per GiB ingested beyond free tier (50"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:156`: "1.  **Always explicitly name Google Cloud Monitoring** as the platform to"
- `gke-observability (agents/platform/skills/gke-observability)/SKILL.md:165`: "A comprehensive assessment of node health relies on analyzing these two metrics together:"

**Recommendation** (likely): Keep the golden-path defaults table, the enable commands, the Alerting section with its Production Rules and Node Health rules; drop the Key GKE metrics table, Live Resource Usage, Cloud Logging examples, Cost Considerations, Tracing/Profiling and LQL Query Examples. Apply as an overlay patch. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-e5fabe: gke-platform-security (agents/platform/skills/gke-platform-security)

The predefined IAM roles table and the Cross-Service Authentication bindings (storage.objectViewer, cloudsql.client, pubsub.subscriber) restate GCP IAM documentation; the team's content is the golden-path defaults table, the node service-account rule, the RBAC rules and the appended KMS/Security Posture section.

Evidence:
- `gke-platform-security (agents/platform/skills/gke-platform-security)/SKILL.md:170`: "Common project-level IAM policy binding patterns for granting backend Google"
- `gke-platform-security (agents/platform/skills/gke-platform-security)/SKILL.md:160`: "-   **Node Service Account**: By default, nodes use the Compute Engine default"
- `gke-platform-security (agents/platform/skills/gke-platform-security)/SKILL.md:213`: "of the cluster's project (`CLUSTER_PROJECT_NUMBER`, not the key project's number) needs"

**Recommendation** (likely): Keep the defaults table, Secret Manager and RBAC sections, Binary Authorization, the Service Accounts bullets and the local secrets-encryption/Security Posture section; drop Common IAM Roles and Cross-Service Authentication Patterns. Apply as an overlay patch. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-1bc1ab: gke-reliability (agents/platform/skills/gke-reliability), gke-reliability (third_party/google-skills/gke-reliability)

Sections 2 to 5 are generic Kubernetes manifests (PDB, probes, preStop, topologySpreadConstraints) a capable model writes unprompted; the team's choices sit in the two tables and the Best Practices list and are diluted by the tutorial text.

Evidence:
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:58`: "PDBs ensure minimum pod availability during voluntary disruptions (node upgrades, autoscaler scale-down)."
- `gke-reliability (agents/platform/skills/gke-reliability)/SKILL.md:198`: "**Probes with Explicit Timeouts**: Every production container must have both liveness and readiness probes defined. **Always explicitly define `initialDelaySeconds`, `periodSeconds`, and `timeoutSeconds`** for all probes."

**Recommendation** (likely): Keep the Golden Path table, the probe values, the Replicas table and the Best Practices list; drop the PDB/probe/preStop/topology explanations and the check-existing command blocks. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-134424: gke-service-networking (agents/platform/skills/gke-service-networking), gke-service-networking (third_party/google-skills/gke-service-networking)

The six workflows are template manifests for Gateway, HTTPRoute, Ingress, BackendConfig, ManagedCertificate, NEG annotation and ServiceAttachment that a capable model produces from the resource names alone; the team's four defaults are confined to the Best Practices list at the end.

Evidence:
- `gke-service-networking (agents/platform/skills/gke-service-networking)/SKILL.md:23`: "The Gateway API is the modern way to manage routing in Kubernetes."
- `gke-service-networking (agents/platform/skills/gke-service-networking)/SKILL.md:235`: "**Enable Cloud Armor**: Always protect public-facing endpoints with Cloud Armor."

**Recommendation** (likely): Keep the four Best Practices, the chosen gatewayClassName and the BackendConfig/Service annotation wiring; drop the generic Gateway, HTTPRoute, Ingress, ManagedCertificate and ServiceAttachment manifests. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-408f69: gke-storage (agents/platform/skills/gke-storage), gke-storage (third_party/google-skills/gke-storage)

The PVC, GCS FUSE pod and volume-expansion blocks are stock Kubernetes/GKE examples; the house defaults are the golden-path table, the custom StorageClass block and the Best Practices list.

Evidence:
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:146`: "Kubernetes automatically resizes the filesystem."
- `gke-storage (agents/platform/skills/gke-storage)/SKILL.md:150`: "**Always enable volume expansion**: Set `allowVolumeExpansion: true` on all"

**Recommendation** (likely): Keep the golden-path table, the custom StorageClass defaults and the Best Practices; drop the generic PVC examples and the expansion explanation. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### low-228e4a: gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring), gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring)

scripts/validate_queries.sh validates nothing: it resolves a project and then prints that there are no queries. It costs a read for an agent that opens it and misdescribes itself as an LQL validator.

Evidence:
- `gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring)/scripts/validate_queries.sh:2`: "# Validate Cloud Logging LQL queries used in SKILL.md"
- `gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring)/scripts/validate_queries.sh:16`: "echo "No Cloud Logging LQL queries defined in this skill to validate.""

**Recommendation** (confident): Delete the no-op script from the mirrored copy (or exclude it in the overlay); SKILL.md never references it. This is a mirrored skill: the cut would be an overlay patch that diverges from upstream, so it is left for you to decide.

Decision needed: yes

### fm-43438a: fleet-audit-reports

The description value is an unquoted YAML scalar that contains a second ": " (in "...a request to run an audit: a run collects..."), which YAML reads as a nested mapping key. A strict loader rejects the front matter with "mapping values are not allowed here", and a runtime that does so would skip the skill.

Evidence:
- `fleet-audit-reports/SKILL.md:3`: "description: Answer a question about a past autonomous fleet audit from the on-pod report store — what a stream last found, how many criticals are open, what changed between ..."

**Recommendation** (confident): Quote the description value or write it as a block scalar (description: >-). The inventory tool repaired it on read; the error text it reported was "repaired: mapping values are not allowed here".

Decision needed: no

## 7. What we looked at

| Skill | Source | Status | Location | Files | Words | Last changed |
| --- | --- | --- | --- | --- | --- | --- |
| edit-mirrored-skill | local | unmanaged | `.agents/skills/edit-mirrored-skill` | 1 | 1436 | 2026-10-13 |
| install-kube-agents | local | unmanaged | `.agents/skills/install-kube-agents` | 1 | 6244 | 2026-10-15 |
| review-address-feedback | local | unmanaged | `.agents/skills/review-address-feedback` | 1 | 1254 | 2026-10-09 |
| review-adversarial | local | unmanaged | `.agents/skills/review-adversarial` | 1 | 4818 | 2026-10-09 |
| review-docs-drift | local | unmanaged | `.agents/skills/review-docs-drift` | 1 | 1590 | 2026-10-07 |
| review-preflight | local | unmanaged | `.agents/skills/review-preflight` | 1 | 2145 | 2026-10-09 |
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
| uninstall-kube-agents | local | unmanaged | `.agents/skills/uninstall-kube-agents` | 1 | 626 | 2026-10-14 |
| upgrade-kube-agents | local | unmanaged | `.agents/skills/upgrade-kube-agents` | 1 | 1130 | 2026-10-14 |
| a2a-topics | local | unmanaged | `a2a/persona/platform/skills/a2a-topics` | 1 | 1013 | 2026-09-18 |
| gke-stockout-investigator | local | unmanaged | `agentplugins/gke-stockout-investigator/files/skills/gke-stockout-investigator` | 1 | 3703 | 2026-10-03 |
| gke-observability (agents/cluster/skills/gke-observability) | local | unmanaged | `agents/cluster/skills/gke-observability` | 1 | 514 | 2026-10-14 |
| gke-reliability (agents/cluster/skills/gke-reliability) | local | unmanaged | `agents/cluster/skills/gke-reliability` | 1 | 404 | 2026-10-14 |
| gke-stall-detection | local | unmanaged | `agents/cluster/skills/gke-stall-detection` | 1 | 1330 | 2026-10-05 |
| gke-storage (agents/cluster/skills/gke-storage) | local | unmanaged | `agents/cluster/skills/gke-storage` | 1 | 324 | 2026-07-28 |
| gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) | local | unmanaged | `agents/cluster/skills/gke-workload-scaling` | 3 | 582 | 2026-10-14 |
| gke-workload-security (agents/cluster/skills/gke-workload-security) | local | unmanaged | `agents/cluster/skills/gke-workload-security` | 4 | 874 | 2026-10-14 |
| gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) | local | unmanaged | `agents/cluster/skills/gke-workload-troubleshooting` | 1 | 1284 | 2026-09-09 |
| capacity-obtainability | local | unmanaged | `agents/platform/skills/capacity-obtainability` | 1 | 3385 | 2026-09-26 |
| cluster-agent-lifecycle | local | unmanaged | `agents/platform/skills/cluster-agent-lifecycle` | 1 | 1852 | 2026-10-15 |
| fleet-audit | local | unmanaged | `agents/platform/skills/fleet-audit` | 44 | 16855 | 2026-10-15 |
| fleet-audit-reports | local | unmanaged | `agents/platform/skills/fleet-audit-reports` | 3 | 1927 | 2026-10-15 |
| fleet-upgrade-verification | local | unmanaged | `agents/platform/skills/fleet-upgrade-verification` | 8 | 5019 | 2026-10-15 |
| gce-compute-fleet-audit | local | unmanaged | `agents/platform/skills/gce-compute-fleet-audit` | 3 | 311 | 2026-10-13 |
| gcp-config-connector | local | unmanaged | `agents/platform/skills/gcp-config-connector` | 5 | 4869 | 2026-10-01 |
| gcp-networking-fabric-audit | local | unmanaged | `agents/platform/skills/gcp-networking-fabric-audit` | 3 | 431 | 2026-10-13 |
| github-issue-resolver | local | unmanaged | `agents/platform/skills/github-issue-resolver` | 3 | 2065 | 2026-10-08 |
| gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) | local | unmanaged | `agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu` | 1 | 711 | 2026-08-07 |
| gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption) | local | unmanaged | `agents/platform/skills/gke-ai-troubleshooting-jobset-interruption` | 3 | 1532 | 2026-08-07 |
| gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom) | local | unmanaged | `agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom` | 3 | 929 | 2026-08-07 |
| gke-app-onboarding (agents/platform/skills/gke-app-onboarding) | local | unmanaged | `agents/platform/skills/gke-app-onboarding` | 5 | 541 | 2026-08-20 |
| gke-backup-dr (agents/platform/skills/gke-backup-dr) | local | unmanaged | `agents/platform/skills/gke-backup-dr` | 1 | 899 | 2026-10-08 |
| gke-basics (agents/platform/skills/gke-basics) | local | unmanaged | `agents/platform/skills/gke-basics` | 6 | 3782 | 2026-10-09 |
| gke-batch-hpc (agents/platform/skills/gke-batch-hpc) | local | unmanaged | `agents/platform/skills/gke-batch-hpc` | 1 | 744 | 2026-09-26 |
| gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler) | local | unmanaged | `agents/platform/skills/gke-cluster-autoscaler` | 9 | 2639 | 2026-10-13 |
| gke-cluster-creation (agents/platform/skills/gke-cluster-creation) | local | unmanaged | `agents/platform/skills/gke-cluster-creation` | 1 | 1645 | 2026-09-23 |
| gke-compute-classes (agents/platform/skills/gke-compute-classes) | local | unmanaged | `agents/platform/skills/gke-compute-classes` | 27 | 7434 | 2026-08-07 |
| gke-cost-analysis (agents/platform/skills/gke-cost-analysis) | local | unmanaged | `agents/platform/skills/gke-cost-analysis` | 1 | 1039 | 2026-08-07 |
| gke-cost-optimization (agents/platform/skills/gke-cost-optimization) | local | unmanaged | `agents/platform/skills/gke-cost-optimization` | 1 | 1200 | 2026-08-07 |
| gke-golden-path (agents/platform/skills/gke-golden-path) | local | unmanaged | `agents/platform/skills/gke-golden-path` | 2 | 594 | 2026-08-07 |
| gke-inference (agents/platform/skills/gke-inference) | local | unmanaged | `agents/platform/skills/gke-inference` | 1 | 917 | 2026-08-07 |
| gke-manifest-generation (agents/platform/skills/gke-manifest-generation) | local | unmanaged | `agents/platform/skills/gke-manifest-generation` | 5 | 2218 | 2026-09-24 |
| gke-multitenancy (agents/platform/skills/gke-multitenancy) | local | unmanaged | `agents/platform/skills/gke-multitenancy` | 1 | 626 | 2026-08-07 |
| gke-networking (agents/platform/skills/gke-networking) | local | unmanaged | `agents/platform/skills/gke-networking` | 1 | 870 | 2026-08-17 |
| gke-observability (agents/platform/skills/gke-observability) | local | unmanaged | `agents/platform/skills/gke-observability` | 1 | 993 | 2026-08-07 |
| gke-platform-security (agents/platform/skills/gke-platform-security) | local | unmanaged | `agents/platform/skills/gke-platform-security` | 1 | 1161 | 2026-10-09 |
| gke-productionize (agents/platform/skills/gke-productionize) | local | unmanaged | `agents/platform/skills/gke-productionize` | 1 | 719 | 2026-10-09 |
| gke-reliability (agents/platform/skills/gke-reliability) | local | unmanaged | `agents/platform/skills/gke-reliability` | 1 | 767 | 2026-08-07 |
| gke-service-networking (agents/platform/skills/gke-service-networking) | local | unmanaged | `agents/platform/skills/gke-service-networking` | 1 | 686 | 2026-08-07 |
| gke-storage (agents/platform/skills/gke-storage) | local | unmanaged | `agents/platform/skills/gke-storage` | 1 | 581 | 2026-08-07 |
| gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring) | local | unmanaged | `agents/platform/skills/gke-tpu-dynamic-slices-monitoring` | 3 | 1287 | 2026-08-07 |
| gke-tpu-metrics-monitoring (agents/platform/skills/gke-tpu-metrics-monitoring) | local | unmanaged | `agents/platform/skills/gke-tpu-metrics-monitoring` | 3 | 855 | 2026-08-07 |
| gke-upgrades (agents/platform/skills/gke-upgrades) | local | unmanaged | `agents/platform/skills/gke-upgrades` | 4 | 6150 | 2026-10-15 |
| gke-workload-identity (agents/platform/skills/gke-workload-identity) | local | unmanaged | `agents/platform/skills/gke-workload-identity` | 1 | 2241 | 2026-10-09 |
| gke-workload-scaling (agents/platform/skills/gke-workload-scaling) | local | unmanaged | `agents/platform/skills/gke-workload-scaling` | 3 | 755 | 2026-09-26 |
| gke-workload-security (agents/platform/skills/gke-workload-security) | local | unmanaged | `agents/platform/skills/gke-workload-security` | 4 | 1046 | 2026-10-09 |
| gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) | local | unmanaged | `agents/platform/skills/gke-workload-troubleshooting` | 1 | 1306 | 2026-10-02 |
| inspect-repository | local | unmanaged | `agents/platform/skills/inspect-repository` | 3 | 838 | 2026-10-08 |
| kube-agents-observability | local | unmanaged | `agents/platform/skills/kube-agents-observability` | 6 | 1612 | 2026-10-15 |
| manage-cluster | local | unmanaged | `agents/platform/skills/manage-cluster` | 1 | 716 | 2026-10-15 |
| pr-conversation | local | unmanaged | `agents/platform/skills/pr-conversation` | 3 | 2305 | 2026-10-08 |
| submit-suggestion | local | unmanaged | `agents/platform/skills/submit-suggestion` | 2 | 3215 | 2026-10-15 |
| version-control | local | unmanaged | `agents/platform/skills/version-control` | 3 | 3167 | 2026-10-15 |
| workload-rebalancing | local | unmanaged | `agents/platform/skills/workload-rebalancing` | 1 | 535 | 2026-09-25 |
| gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) | local | unmanaged | `third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu` | 1 | 711 | 2026-10-10 |
| gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption) | local | unmanaged | `third_party/google-skills/gke-ai-troubleshooting-jobset-interruption` | 3 | 1532 | 2026-10-10 |
| gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom) | local | unmanaged | `third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom` | 3 | 929 | 2026-10-10 |
| gke-app-onboarding (third_party/google-skills/gke-app-onboarding) | local | unmanaged | `third_party/google-skills/gke-app-onboarding` | 5 | 541 | 2026-10-10 |
| gke-backup-dr (third_party/google-skills/gke-backup-dr) | local | unmanaged | `third_party/google-skills/gke-backup-dr` | 1 | 869 | 2026-10-10 |
| gke-basics (third_party/google-skills/gke-basics) | local | unmanaged | `third_party/google-skills/gke-basics` | 6 | 3594 | 2026-10-10 |
| gke-batch-hpc (third_party/google-skills/gke-batch-hpc) | local | unmanaged | `third_party/google-skills/gke-batch-hpc` | 1 | 632 | 2026-10-10 |
| gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler) | local | unmanaged | `third_party/google-skills/gke-cluster-autoscaler` | 9 | 2636 | 2026-10-10 |
| gke-cluster-creation (third_party/google-skills/gke-cluster-creation) | local | unmanaged | `third_party/google-skills/gke-cluster-creation` | 1 | 1324 | 2026-10-10 |
| gke-compute-classes (third_party/google-skills/gke-compute-classes) | local | unmanaged | `third_party/google-skills/gke-compute-classes` | 27 | 7434 | 2026-10-10 |
| gke-cost-analysis (third_party/google-skills/gke-cost-analysis) | local | unmanaged | `third_party/google-skills/gke-cost-analysis` | 1 | 1039 | 2026-10-10 |
| gke-cost-optimization (third_party/google-skills/gke-cost-optimization) | local | unmanaged | `third_party/google-skills/gke-cost-optimization` | 1 | 1200 | 2026-10-10 |
| gke-golden-path (third_party/google-skills/gke-golden-path) | local | unmanaged | `third_party/google-skills/gke-golden-path` | 2 | 594 | 2026-10-10 |
| gke-inference (third_party/google-skills/gke-inference) | local | unmanaged | `third_party/google-skills/gke-inference` | 1 | 917 | 2026-10-10 |
| gke-manifest-generation (third_party/google-skills/gke-manifest-generation) | local | unmanaged | `third_party/google-skills/gke-manifest-generation` | 5 | 2168 | 2026-10-10 |
| gke-multitenancy (third_party/google-skills/gke-multitenancy) | local | unmanaged | `third_party/google-skills/gke-multitenancy` | 1 | 626 | 2026-10-10 |
| gke-networking (third_party/google-skills/gke-networking) | local | unmanaged | `third_party/google-skills/gke-networking` | 1 | 692 | 2026-10-10 |
| gke-observability (third_party/google-skills/gke-observability) | local | unmanaged | `third_party/google-skills/gke-observability` | 1 | 993 | 2026-10-10 |
| gke-platform-security (third_party/google-skills/gke-platform-security) | local | unmanaged | `third_party/google-skills/gke-platform-security` | 1 | 983 | 2026-10-10 |
| gke-productionize (third_party/google-skills/gke-productionize) | local | unmanaged | `third_party/google-skills/gke-productionize` | 1 | 714 | 2026-10-10 |
| gke-reliability (third_party/google-skills/gke-reliability) | local | unmanaged | `third_party/google-skills/gke-reliability` | 1 | 767 | 2026-10-10 |
| gke-service-networking (third_party/google-skills/gke-service-networking) | local | unmanaged | `third_party/google-skills/gke-service-networking` | 1 | 686 | 2026-10-10 |
| gke-storage (third_party/google-skills/gke-storage) | local | unmanaged | `third_party/google-skills/gke-storage` | 1 | 581 | 2026-10-10 |
| gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring) | local | unmanaged | `third_party/google-skills/gke-tpu-dynamic-slices-monitoring` | 3 | 1287 | 2026-10-10 |
| gke-tpu-metrics-monitoring (third_party/google-skills/gke-tpu-metrics-monitoring) | local | unmanaged | `third_party/google-skills/gke-tpu-metrics-monitoring` | 3 | 855 | 2026-10-10 |
| gke-upgrades (third_party/google-skills/gke-upgrades) | local | unmanaged | `third_party/google-skills/gke-upgrades` | 4 | 5523 | 2026-10-10 |
| gke-workload-identity (third_party/google-skills/gke-workload-identity) | local | unmanaged | `third_party/google-skills/gke-workload-identity` | 1 | 2136 | 2026-10-10 |
| gke-workload-scaling (third_party/google-skills/gke-workload-scaling) | local | unmanaged | `third_party/google-skills/gke-workload-scaling` | 3 | 665 | 2026-10-10 |
| gke-workload-security (third_party/google-skills/gke-workload-security) | local | unmanaged | `third_party/google-skills/gke-workload-security` | 4 | 832 | 2026-10-10 |
| gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) | local | unmanaged | `third_party/google-skills/gke-workload-troubleshooting` | 1 | 1242 | 2026-10-09 |

## 8. Proposed changes

These are safe and the pull request applies them:

- Patch review-security-k8s-rbac (Delete resources/gke-rbac.md or reduce it to the checklist summary; change section 5 of SKILL.md to cite the GKE RBAC best-practices URL instead of the local copy.) [low-afb095]
- Update gke-observability (agents/cluster/skills/gke-observability) (Replace 'For Standard clusters, you can enable' with 'You can enable' on line 96 and remove '(if using Standard)' on line 118.) [old-1aab6b]
- Patch gke-observability (agents/cluster/skills/gke-observability) (Keep lines 10, 14-37 (fix the format filter on line 21 to include loggingService,monitoringService), 94-111; remove lines 39-93 and 113-118.) [low-d827f5]
- Patch gke-reliability (agents/cluster/skills/gke-reliability) (Keep lines 10, 16-25 (regional check), 34 (pdb list), 62 (probe grep), 86-92 (Config Connector maintenance window) and 94-100 (Best Practices as the audit criteria); remove lines 29, 37-49, 53-57, 67, 71-84 (definitions and generic manifests).) [low-18cbaf]
- Update gke-storage (agents/cluster/skills/gke-storage) (Replace `standard-rwm` with `standard-rwx` on line 55, or remove the file per the other findings.) [old-b9e025]
- Patch gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) (Keep lines 1-10 (frontmatter and the read-only rule), the single 'Propose ...' sentence from each of sections 1-4 with the asset links, and best practice 2 (HPA on CPU, VPA on memory); remove the explanatory prose for HPA, VPA, update modes, Cluster Autoscaler and best practices 1, 3, 4, 5.) [low-37403d]
- Update gke-workload-security (agents/cluster/skills/gke-workload-security) (In SKILL.md section 2 (lines 35-72), make direct KSA principal binding the proposed default, label GSA impersonation via iam.gke.io/gcp-service-account as legacy, and keep the assets/workload-identity-pod.yaml example (its nodeSelector is still valid).) [old-651932]
- Patch fleet-audit (Edit lines 3-26 of scripts/audit_report.py: add `grep` and `draft` usage lines, change 'three on-demand commands' to 'five', replace the six-stream parenthetical with 'every stream registered in AUDITS (nine today)', and generalise 'GitHub **issue**' to the forge.) [old-e716c6]
- Patch fleet-upgrade-verification (Trim SKILL.md lines 189-259 (PDB and webhook bullets) to the rule name, the verdict it produces and a pointer to the script constants and design doc; leave the rest of the file as is.) [low-abea93]
- Update gke-app-onboarding (agents/platform/skills/gke-app-onboarding), gke-app-onboarding (third_party/google-skills/gke-app-onboarding) (Change the image placeholder in assets/deployment.yaml to us-docker.pkg.dev/<PROJECT>/<REPO>/node-app@sha256:... via the overlay patch.) [old-cf6cda]
- Update gke-basics (agents/platform/skills/gke-basics) (Edit references/core-concepts.md Pricing section via the overlay: remove 'No cluster management fee.' and say both modes pay the per-cluster fee after the free tier.) [old-05fae9]
- Update gke-batch-hpc (agents/platform/skills/gke-batch-hpc) (Change the Best Practices bullet to 'Use the MPI Operator (MPIJob v2beta1)' and pin the install URL to a tagged release via the overlay.) [old-51e150]
- Update gke-cluster-creation (agents/platform/skills/gke-cluster-creation) (Via agents/platform/skill-overlays/gke-cluster-creation/: fix the sentence on line 186 (and the matching note in the HA best practice) to state per-zone semantics, or set --num-nodes 1 / initialNodeCount 1.) [old-7457aa]
- Update gke-manifest-generation (agents/platform/skills/gke-manifest-generation), gke-manifest-generation (third_party/google-skills/gke-manifest-generation) (Overlay patch correcting the Autopilot requests/limits sentence at SKILL.md lines 35-37 to the current behaviour (limits lowered to requests; bursting keeps higher limits).) [old-ea1e0a]
- Update gke-observability (agents/platform/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability) (Overlay patch replacing `--enable-dataplane-v2-flow-observability` with `--enable-dataplane-v2-metrics` in the Enabling Full Monitoring block.) [old-13f14a]
- Update gke-platform-security (agents/platform/skills/gke-platform-security), gke-platform-security (third_party/google-skills/gke-platform-security) (Overlay patch replacing the `--enable-gke-sandbox` cluster update with the `node-pools create --sandbox type=gvisor` command and the Autopilot note.) [old-12b4ae]
- Update gke-storage (agents/platform/skills/gke-storage), gke-storage (third_party/google-skills/gke-storage) (Overlay patch: standard-rwo row -> `pd-balanced`, 'General purpose (GKE default)'; add a note that pd-standard requires a custom StorageClass.) [old-d4508b]
- Update gke-upgrades (agents/platform/skills/gke-upgrades) (Overlay patch under agents/platform/skill-overlays/gke-upgrades/ swapping `apiserver_request_total | grep deprecated` for `apiserver_requested_deprecated_apis` in SKILL.md:167, references/checklists.md:14, references/runbook-template.md:25; record with make skills-refresh.) [old-e5c4a5]
- Update gke-workload-scaling (agents/platform/skills/gke-workload-scaling), gke-workload-scaling (third_party/google-skills/gke-workload-scaling) (Overlay patch on lines 62-67: replace 'natively supported by the GKE control plane without requiring the Custom Metrics Adapter' with the adapter prerequisite.) [old-6cf579]
- Patch workload-rebalancing (Edit lines 8, 22 and 54 of agents/platform/skills/workload-rebalancing/SKILL.md to name the GitOps reconciler as the actor that applies the merged PR, matching docs/site/src/content/docs/deploy/gitops-argocd.md and agents/platform/skills/gcp-config-connector/SKILL.md.) [old-db732e]
- Update gke-platform-security (third_party/google-skills/gke-platform-security) (Change the Workload Identity pointer at lines 23-25 and 164-166 to gke-workload-identity; report upstream.) [old-04c923]
- Update gke-productionize (third_party/google-skills/gke-productionize) (Fix the skill name in the description on line 5.; Rewrite lines 98-100 to route Workload Identity to gke-workload-identity; report upstream.) [old-5a7c45, old-1b10d8]
- Update gke-upgrades (third_party/google-skills/gke-upgrades) (Replace the node-pools upgrade command at troubleshooting.md lines 191-194 with clusters upgrade --node-pool; report upstream.) [old-da4e9e]
- Patch gke-workload-identity (third_party/google-skills/gke-workload-identity) (Align description and body: add a direct-binding setup section or drop 'Configures' and 'Use when setting up KSA/GSA bindings' from the description.) [old-5c755f]
- Update gke-workload-security (third_party/google-skills/gke-workload-security) (Make the Network Policy enablement a dataplane check plus two-step command sequence at lines 98-107; report upstream.; Mark section 2 (lines 53-91) as legacy impersonation and route direct binding to gke-workload-identity; report upstream.; Replace the --enable-gke-sandbox reference at lines 120-123 with the node-pool --sandbox type=gvisor prerequisite.) [old-48b66b, old-7250e9, old-c97f33]
- Update gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) (Replace the two kubectl get endpoints references (lines 186 and 211) with the EndpointSlice query.) [old-91907e]
- Patch fleet-audit-reports (Quote the description value in agents/platform/skills/fleet-audit-reports/SKILL.md front matter.) [fm-43438a]

### Waiting on your decision

One line per action. Several findings can point at the same action; all their IDs are listed.

- Remove review-security-k8s-agents-prompt-injection (Delete .agents/skills/review-security-k8s-agents-prompt-injection/ and remove the `review-security-k8s-agents-prompt-injection` line from review-security-k8s-agents-main; optionally carry the Guardrails bullet into review-security-k8s-agents-credentials.) [low-0ab013]
- Remove gke-storage (agents/cluster/skills/gke-storage) (Delete agents/cluster/skills/gke-storage; if storage-binding diagnosis is wanted on the Cluster Agent, write a diagnostic skill in its place rather than keeping this configuration guide.; Remove from agents/cluster/skills; the Platform Agent's mirrored gke-storage covers configuration.) [low-cf1d60, place-411e11, dup-cc232f]
- Patch gke-workload-security (agents/cluster/skills/gke-workload-security) (Trim sections 4 and 5's node-pool/cluster field proposals (lines 129-142) to a pointer to gke-platform-security on the Platform Agent; leave section 3's dataplane check and Calico ordering only if the owner confirms the Cluster Agent should propose control-plane changes.) [place-69406c]
- Move one of gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu), gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) (which one is not named; decide) (Add the skill to agents/cluster/skills (keeping the platform mirror only if the Platform Agent needs it) so the Cluster Agent can load it for a disruption on its cluster.) [place-30da22]
- Move one of gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption), gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption) (which one is not named; decide) (Add the skill to agents/cluster/skills (keeping the platform mirror only if the Platform Agent needs it).) [place-71d24b]
- Move one of gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom), gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom) (which one is not named; decide) (Relocate (or additionally mirror) the skill under agents/cluster/skills/ where read-only single-cluster debugging lives; keep the Platform Agent copy only if the Cluster Agent lacks Cloud Logging access for serial-console logs.) [place-f7089e]
- Patch gke-app-onboarding (agents/platform/skills/gke-app-onboarding) (Via the overlay in agents/platform/skill-overlays/gke-app-onboarding/: keep sections 1, 4 (checklist), 5 and Next Steps; remove sections 2-3 and the unreferenced assets/ sample (or change its Service to ClusterIP + Gateway).) [low-235c89]
- Patch gke-basics (agents/platform/skills/gke-basics) (Via agents/platform/skill-overlays/gke-basics/: remove references/client-library-usage.md and references/iac-usage.md and their Reference Directory entries; trim core-concepts.md to the golden-path defaults.) [low-414b06]
- Patch gke-batch-hpc (agents/platform/skills/gke-batch-hpc) (Add an overlay patch under agents/platform/skill-overlays/gke-batch-hpc/ that removes the Job/JobSet/Kueue/MPIJob manifests and the compact-placement command, keeping the rules and the appended capacity-obtainability section.) [low-67c9e2]
- Patch gke-cost-optimization (agents/platform/skills/gke-cost-optimization), gke-cost-optimization (third_party/google-skills/gke-cost-optimization) (Overlay patch that removes sections 5 (Machine Type Selection), 6 (CUDs) and 7 (Cluster Management) and the duplicated Best Practices Summary, keeping the rules tables, Spot guidance and dev/test deviations.) [low-6cec87]
- Patch gke-inference (agents/platform/skills/gke-inference), gke-inference (third_party/google-skills/gke-inference) (Overlay patch removing the Accelerator Selection Guide, Optimization Tips and Troubleshooting sections; keep Workflow, GPU ComputeClass and Autoscaling LLM Inference.) [low-ba8315]
- Patch gke-multitenancy (agents/platform/skills/gke-multitenancy), gke-multitenancy (third_party/google-skills/gke-multitenancy) (Overlay patch that trims the generic namespace/RBAC/quota/NetworkPolicy manifests to the rules the team adds (default model, Google Groups subjects, LimitRange defaults, cost-center labels).) [low-788bf4]
- Patch gke-networking (agents/platform/skills/gke-networking) (Overlay patch removing the VPC-Native Mode Benefits, IP Planning and Egress sections; keep defaults table, access patterns, Day-0 warning and the appended dns-endpoint check.) [low-e6fe3c]
- Patch gke-observability (agents/platform/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability) (Overlay patch trimming the generic metrics, logging, cost and LQL sections; keep defaults, enable commands and the alerting/production rules.) [low-3c8a48]
- Patch gke-platform-security (agents/platform/skills/gke-platform-security) (Overlay patch removing the Common IAM Roles table and the Cross-Service Authentication Patterns block (which also closes the unterminated code fence that swallows the Resources list).) [low-e5fabe]
- Patch gke-reliability (agents/platform/skills/gke-reliability), gke-reliability (third_party/google-skills/gke-reliability) (Via an overlay patch in agents/platform/skill-overlays/gke-reliability/: cut the explanatory prose and 'check existing' blocks in workflows 2-5, keep the golden-path table, the recommended probe YAML values, the Replicas table and the Best Practices list.) [low-1bc1ab]
- Patch gke-service-networking (agents/platform/skills/gke-service-networking), gke-service-networking (third_party/google-skills/gke-service-networking) (Via an overlay patch in agents/platform/skill-overlays/gke-service-networking/: reduce to the defaults (Gateway API with gke-l7-global-external-managed, Cloud Armor on every public endpoint, managed certs, NEGs) plus the BackendConfig annotation, and remove the template manifests.) [low-134424]
- Patch gke-storage (agents/platform/skills/gke-storage), gke-storage (third_party/google-skills/gke-storage) (Overlay patch: remove the Block/Shared PVC examples and the Volume Expansion prose, keep the GCS FUSE Workload Identity note, the fast-regional StorageClass and the Best Practices list.) [low-408f69]
- Patch gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring), gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring) (Remove scripts/validate_queries.sh from agents/platform/skills/gke-tpu-dynamic-slices-monitoring via the overlay; nothing in SKILL.md calls it.) [low-228e4a]
- Patch gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) (No local change; report upstream.; Overlay patch on gke-workload-security line 153; also gke-platform-security line 118 (see the out-of-date finding).; Reconcile the cluster copy against the platform copy.; Rewrite section 2 of the cluster copy to match the platform copy.) [conf-4a9226, conf-b5e384, conf-e46fb2, dup-b3b16d]
- Patch gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) (No local change; report upstream.; Overlay patch on gke-workload-troubleshooting step 0.) [conf-cb2e3b, conf-fad338]
- Patch gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) (No local change; report upstream.) [conf-e9fbf7]
- Patch gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability) (Patch the cluster copy.) [conf-0feb2d, conf-9a2485]
- Patch gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability) (Patch the cluster copy.) [conf-e64b5d, conf-a22a9b]
- Patch gke-storage (agents/cluster/skills/gke-storage), gke-storage (agents/platform/skills/gke-storage) (Remove agents/cluster/skills/gke-storage.) [conf-dd74e6, conf-8c70b6]
- Patch capacity-obtainability, gke-stockout-investigator (Edit agentplugins/gke-stockout-investigator/files/skills/gke-stockout-investigator/SKILL.md line 159.) [conf-937bf6]
- Patch review-security-k8s-agents-firewall, review-security-k8s-network (Align the NodePort bullet in review-security-k8s-network with review-security-k8s-agents-firewall, or the reverse.) [conf-bbee9a]
- Patch gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability) (Reconcile the cluster copy against the platform copy.) [dup-ed076d]
- Patch gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability), gke-reliability (third_party/google-skills/gke-reliability) (Reconcile the cluster copy against the platform copy.) [dup-6ba2a7]

## 9. How to respond

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

One entry per skill. "Goal" is what the skill is for, in one line. "Adds beyond
the model" is what it makes the agent do that a capable model would not do
unprompted; that is the skill's value. "Concerns" lists every finding above
that involves it.

### edit-mirrored-skill

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/edit-mirrored-skill`
- **Goal:** Change, sync or adopt a gke-* skill copied from google/skills so the local edit is recorded as an overlay patch and survives the next upstream sync.
- **Adds beyond the model:** Edit the shipped skill and record it with make skills-refresh (one patch per reason, headers Why/Local-Issue/Retire-When/Upstream-Issue), never touch third_par…
- **Concerns:** none

### install-kube-agents

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/install-kube-agents`
- **Goal:** Guide an agent through installing kube-agents on a GKE cluster safely: find out what the operator has, agree every choice, preview the install, and apply only…
- **Adds beyond the model:** The team's install protocol: always run `install.sh --non-interactive` in three stages (detect and interview, `--dry-run` preview, explicit go-ahead then apply…
- **Concerns:** none

### review-address-feedback

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-address-feedback`
- **Goal:** Work a review round on an open pull request: fix or decline each finding, reply in every thread, resolve what was settled, and stop asking for re-reads once th…
- **Adds beyond the model:** Decline by default on later rounds (fix only a behaviour Medium on code this PR added by one mechanical edit, fix a correct High on any round, defer anything t…
- **Concerns:** none

### review-adversarial

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-adversarial`
- **Goal:** Review a diff range as a hostile second reader: derive its intent, hunt candidates from ten angles, re-verify every candidate against source, and report only c…
- **Adds beyond the model:** Run the pass in a context that did not write the change and withhold intent and commit bodies from it, work all ten named angles with up to six candidates each…
- **Concerns:** none

### review-docs-drift

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-docs-drift`
- **Goal:** Check a pull request in both directions for documentation drift: which docs the code change invalidated, and whether changed docs match source, the canonical-h…
- **Adds beyond the model:** Navigate only through AGENTS.md's rules and docs/README.md's map, test every doc sentence naming an identifier against the PR's source rather than other docs,…
- **Concerns:** none

### review-preflight

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-preflight`
- **Goal:** Run the adversarial and docs-drift passes before a pull request opens, each in a fresh context that did not write the change, and merge their results into the…
- **Adds beyond the model:** Fetch the base into refs/kube-agents-base and diff three-dot before any pass, run make docs-check in the main loop and hand its output on, always spawn both pa…
- **Concerns:** none

### review-security-k8s-admission

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-admission`
- **Goal:** Review admission webhooks and ValidatingAdmissionPolicy/MutatingAdmissionPolicy objects for bypass, denial-of-service, scope-evasion and unsafe-mutation risks.
- **Adds beyond the model:** Prefer failurePolicy Fail on security webhooks and VAPs, require a NetworkPolicy limiting webhook ingress to the API server, and ask whether reinvocationPolicy…
- **Concerns:** none

### review-security-k8s-agents-audit-logs

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-audit-logs`
- **Goal:** Review the logging setup around AI agent workloads so every agent action, prompt and tool call is recorded where the agent cannot alter it.
- **Adds beyond the model:** Require a dedicated ServiceAccount per agent, stdout/stderr logging with no hostPath access to aggregated logs, full prompt and raw output telemetry plus exact…
- **Concerns:** none

### review-security-k8s-agents-credentials

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-credentials`
- **Goal:** Review AI agent pod and RBAC configuration so the agent container never holds credentials directly.
- **Adds beyond the model:** Route all authenticated outbound requests through an injecting credential proxy sidecar, forbid secret env vars and mounts in the agent container, set automoun…
- **Concerns:** none

### review-security-k8s-agents-data-exfil

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-data-exfil`
- **Goal:** Review network egress and data-access configuration so a prompt-injected AI agent cannot send data out of the cluster.
- **Adds beyond the model:** Require egress NetworkPolicies allowlisting only internal services and authorized LLM APIs, route outbound traffic through an egress gateway or transparent pro…
- **Concerns:** none

### review-security-k8s-agents-firewall

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-firewall`
- **Goal:** Check the network rules around an AI agent and its execution sandbox so the agent cannot reach things it should not and nothing untrusted can call it.
- **Adds beyond the model:** Sandbox egress is default-deny with a minimal allowlist, and a metadata-server block must target the credential ports (TCP 80 pre-NAT, 988 post-NAT) and leave…
- **Concerns:**
  - conflicts with review-security-k8s-network [conf-bbee9a]: Option 3. Decide one NodePort rule for the review family. We lean to the firewall skill's conditional rule (flag NodePort only without a st… Decision needed.

### review-security-k8s-agents-main

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-main`
- **Goal:** Run the six AI-agent security review skills in parallel, filter their findings against the project context, and return one JSON report.
- **Adds beyond the model:** Fan out to the fixed set of six agents-* review skills, require each to answer in the `[{agent, findings:[{message,file,line}]}]` JSON shape, then drop finding…
- **Concerns:**
  - duplicate with review-security-k8s-main [dup-89a268]: Keep both. review-security-k8s-main launches review-security-k8s-agents-main as one of its sub-skills, so the shared orchestration text is…

### review-security-k8s-agents-prompt-injection

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-prompt-injection`
- **Goal:** Check that an AI agent's inputs pass through a filtering layer and that its system prompts cannot be edited by less trusted workloads.
- **Adds beyond the model:** Nothing
- **Concerns:**
  - low value [low-0ab013]: Remove the skill. If the ConfigMap/EnvVar tamper check is wanted, move that one bullet into review-security-k8s-agents-credentials (it is a… Decision needed.

### review-security-k8s-agents-sandbox

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-agents-sandbox`
- **Goal:** Check that the place where an AI agent runs code (a REPL, shell or WASM tool) is isolated so a hijacked agent cannot break out or persist.
- **Adds beyond the model:** A sandbox is treated as hostile: it must run under a secure RuntimeClass (gVisor or Kata), be separate from the agent loop container, carry a restrictive secco…
- **Concerns:** none

### review-security-k8s-gateway

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-gateway`
- **Goal:** Check Gateway API objects (Gateway, HTTPRoute, TLSRoute, ReferenceGrant) for route takeover, loose cross-namespace access and weak TLS.
- **Adds beyond the model:** Listeners must restrict `allowedRoutes` to `namespaces.from: Same` or a `Selector`, every cross-namespace route or Secret reference needs a narrow `ReferenceGr…
- **Concerns:** none

### review-security-k8s-main

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-main`
- **Goal:** Run the whole Kubernetes security review family in parallel, filter the findings against the project context, and return one JSON report.
- **Adds beyond the model:** First call review-security-k8s-understand, then fan out to the fixed list of ten review skills (including the agents orchestrator), require the shared `[{agent…
- **Concerns:**
  - duplicate with review-security-k8s-agents-main [dup-89a268]: Keep both. review-security-k8s-main launches review-security-k8s-agents-main as one of its sub-skills, so the shared orchestration text is…

### review-security-k8s-namespaces

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-namespaces`
- **Goal:** Check how a cluster is split into namespaces so tenants and environments stay apart and nobody hides workloads in system namespaces.
- **Adds beyond the model:** Flag when more than roughly 80-90% of workloads share one namespace, any custom workload in `default`/`kube-*`, namespace names that imitate system components,…
- **Concerns:** none

### review-security-k8s-network

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-network`
- **Goal:** Check NetworkPolicies, Services, Ingresses and service-mesh policies so workloads are isolated and nothing is exposed by accident.
- **Adds beyond the model:** Every namespace needs a default-deny NetworkPolicy for both ingress and egress, any `NodePort` or `hostNetwork: true` is a finding, Ingresses need a `tls` bloc…
- **Concerns:**
  - conflicts with review-security-k8s-agents-firewall [conf-bbee9a]: Option 3. Decide one NodePort rule for the review family. We lean to the firewall skill's conditional rule (flag NodePort only without a st… Decision needed.

### review-security-k8s-nodes

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-nodes`
- **Goal:** Check manifests for ways a pod or a compromised node could take over the rest of the cluster through host mounts, node RBAC or scheduling.
- **Adds beyond the model:** Flag hostPath mounts to kubelet or control-plane directories and runtime sockets and recommend ValidatingAdmissionPolicies as the fix, flag any extra RBAC on `…
- **Concerns:** none

### review-security-k8s-pod

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-pod`
- **Goal:** Give a reviewer a fixed checklist for judging whether a Pod's security context lets it escape or escalate.
- **Adds beyond the model:** The team's pod baseline is the restricted Pod Security Standard plus three extras: images pinned by digest, no `default` service account or static token Secret…
- **Concerns:** none

### review-security-k8s-rbac

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-rbac`
- **Goal:** Give a reviewer a fixed checklist for finding over-broad or escalatable RBAC roles and bindings, tuned to GKE.
- **Adds beyond the model:** RBAC review is graded against the GKE RBAC best-practices checklist (default groups, wildcards, CSR/webhook/CRD write verbs, secrets list/watch, self-modificat…
- **Concerns:**
  - low value [low-afb095]: Keep SKILL.md's check list (sections 1-4) as the team's RBAC baseline; replace the vendor-page copy with a one-line pointer to the source U…

### review-security-k8s-service-accounts

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-service-accounts`
- **Goal:** Give a reviewer a fixed checklist for ServiceAccount identity hygiene: one account per app, no automount, no long-lived tokens.
- **Adds beyond the model:** The team requires a 1:1 application-to-ServiceAccount mapping (including one Workload Identity cloud identity per workload), `automountServiceAccountToken: fal…
- **Concerns:** none

### review-security-k8s-storage

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-storage`
- **Goal:** Give a reviewer a fixed checklist for storage objects and volume mounts that could leak data or let a container reach the node.
- **Adds beyond the model:** The team's storage defaults are: mounts read-only unless write is needed, `ReadWriteMany` flagged in favour of RWO/ROX, encryption at rest (CMEK) required on S…
- **Concerns:** none

### review-security-k8s-understand

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/review-security-k8s-understand`
- **Goal:** Build a short architectural picture of a Kubernetes repo before the specialised security review skills run on it.
- **Adds beyond the model:** Before any specialised review, the reviewer must classify every workload as Infrastructure or Application and list cluster-wide compensating controls (mesh mTL…
- **Concerns:** none

### skill-review

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/skill-review`
- **Goal:** Review a SKILL.md against this repo's house style so it is short, loadable, and found by the harness when a user asks for it.
- **Adds beyond the model:** House style for skills: the frontmatter description opens with the action the user asks for and names the object (the harness matches on it), frontmatter must…
- **Concerns:** none

### uninstall-kube-agents

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/uninstall-kube-agents`
- **Goal:** Remove a kube-agents install and the GCP/GKE resources it provisioned using the project's own uninstall script.
- **Adds beyond the model:** Run the uninstall.sh pinned to the installed release (or pass --source-ref) rather than an unstamped copy that falls back to main, with terraform (and helm on…
- **Concerns:** none

### upgrade-kube-agents

- **Source:** local  **Status:** unmanaged  **Location:** `.agents/skills/upgrade-kube-agents`
- **Goal:** Guide an agent through upgrading a running kube-agents install to a chosen release with the correct upgrade.sh flags and mode.
- **Adds beyond the model:** Upgrade only through the release-pinned upgrade.sh (or a bundle's own copy) with full mode as the default, pass --image-tag only for a CI/dev candidate (SemVer…
- **Concerns:** none

### a2a-topics

- **Source:** local  **Status:** unmanaged  **Location:** `a2a/persona/platform/skills/a2a-topics`
- **Goal:** Let an agent read and publish standing fleet state on named A2A bus topics instead of re-diagnosing what another agent already found.
- **Adds beyond the model:** Before a fresh diagnosis check `a2a topics list`/`read`; relay the entry's author and date verbatim and never present it as your own check; treat exit 2 as 'pr…
- **Concerns:** none

### gke-stockout-investigator

- **Source:** local  **Status:** unmanaged  **Location:** `agentplugins/gke-stockout-investigator/files/skills/gke-stockout-investigator`
- **Goal:** Turn a GKE autoscaler stockout alert from Pub/Sub into a diagnosed root cause and a GitOps pull request that adds ComputeClass fallbacks or fixes the workload…
- **Adds beyond the model:** A fixed runbook: notify via `send_notification` first, never use `execute_code` in Pub/Sub sessions, dedupe only by the fixed branch `platform-agent/remediate-…
- **Concerns:**
  - conflicts with capacity-obtainability [conf-937bf6]: Option 3. capacity-obtainability is right: a reservation holds capacity and the report must never say "guarantee". Patch line 159 of gke-st… Decision needed.

### gke-observability (agents/cluster/skills/gke-observability)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-observability`
- **Goal:** Help the per-cluster agent check whether a GKE cluster's logging, metrics and tracing are set up and report what to turn on.
- **Adds beyond the model:** The Cluster Agent never runs an observability change; it reports each one as a proposal expressed as a Config Connector ContainerCluster field (managedPromethe…
- **Concerns:**
  - out of date [old-1aab6b]: Drop the Standard-only qualifier in section 8 and best practice 4; control-plane metrics are available on both Autopilot and Standard clust…
  - low value [low-d827f5]: Cut the skill to the audit checklist and the proposal convention: the read-only line, the describe command (with loggingService and monitor…
  - conflicts with gke-observability (agents/platform/skills/gke-observability) [conf-0feb2d]: Option 3. The platform copy is right on both points (Autopilot supports control-plane metrics; the golden-path component list is the full s… Decision needed.
  - conflicts with gke-observability (agents/platform/skills/gke-observability) [conf-9a2485]: Option 3. The platform copy is right on both points (Autopilot supports control-plane metrics; the golden-path component list is the full s… Decision needed.
  - duplicate with gke-observability (agents/platform/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability) [dup-ed076d]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-reliability (agents/cluster/skills/gke-reliability)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-reliability`
- **Goal:** Check a single GKE cluster and its workloads for availability gaps (regional control plane, PDBs, probes, graceful shutdown, zone spread, maintenance windows)…
- **Adds beyond the model:** The agent runs this as a read-only audit whose output is proposals in the report (never applied changes), it treats regional control plane, a readiness probe o…
- **Concerns:**
  - low value [low-18cbaf]: Cut the skill to the read-only banner, a checklist of the six checks with the one command each needs, the production must-haves from Best P…
  - conflicts with gke-reliability (agents/platform/skills/gke-reliability) [conf-e64b5d]: Option 3. Pick one audit bar for the fleet. We recommend the platform copy's stricter rule (both probes; a PDB on every 2+ replica producti… Decision needed.
  - conflicts with gke-reliability (agents/platform/skills/gke-reliability) [conf-a22a9b]: Option 3. Pick one audit bar for the fleet. We recommend the platform copy's stricter rule (both probes; a PDB on every 2+ replica producti… Decision needed.
  - duplicate with gke-reliability (agents/platform/skills/gke-reliability), gke-reliability (third_party/google-skills/gke-reliability) [dup-6ba2a7]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-stall-detection

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-stall-detection`
- **Goal:** Find controllers that silently stopped reconciling (no error, no progress) in one namespace or kind, using a read-only report script.
- **Adds beyond the model:** Stall detection is the four heuristics in `/opt/data/scripts/stall_report.py` (generation-lag, stale-condition, repeating-warnings, dangling-reference) gated b…
- **Concerns:** none

### gke-storage (agents/cluster/skills/gke-storage)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-storage`
- **Goal:** Tells the Cluster Agent how GKE storage is set up: StorageClasses, the CSI drivers, and growing a PVC.
- **Adds beyond the model:** Nothing
- **Concerns:**
  - low value [low-cf1d60]: Remove the cluster copy. A capable model produces this content unprompted; if the Cluster Agent needs a storage skill, it needs a read-only… Decision needed.
  - out of place [place-411e11]: Do not keep write-path storage guidance in the Cluster Agent profile. Either drop it (see the low_value finding) or replace it with a diagn… Decision needed.
  - out of date [old-b9e025]: If the file is kept, change `standard-rwm` to `standard-rwx`.
  - conflicts with gke-storage (agents/platform/skills/gke-storage) [conf-dd74e6]: Option 1. The platform copy is right (standard-rwx is the built-in Filestore class; premium-rwo is a built-in zonal pd-ssd class). Retire t… Decision needed.
  - conflicts with gke-storage (agents/platform/skills/gke-storage) [conf-8c70b6]: Option 1. The platform copy is right (standard-rwx is the built-in Filestore class; premium-rwo is a built-in zonal pd-ssd class). Retire t… Decision needed.
  - duplicate with gke-storage (agents/platform/skills/gke-storage), gke-storage (third_party/google-skills/gke-storage) [dup-cc232f]: Keep the platform copy (generated from the upstream source of truth). Remove the cluster copy; if the Cluster Agent needs storage help, it… Decision needed.

### gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-workload-scaling`
- **Goal:** Help the Cluster Agent recommend how a GKE workload should be scaled, by hand or with HPA and VPA, without applying anything itself.
- **Adds beyond the model:** Scaling changes are reported as proposals (a Deployment replicas patch, HPA/VPA manifests, or Config Connector ContainerCluster/ContainerNodePool fields), neve…
- **Concerns:**
  - low value [low-37403d]: Cut the skill down to what the team decided: the read-only proposal rule, the shape of each proposal (Deployment patch, HPA/VPA manifest wi…

### gke-workload-security (agents/cluster/skills/gke-workload-security)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-workload-security`
- **Goal:** Help the per-cluster agent check how well a GKE cluster's workloads are secured and write up the fixes it would make.
- **Adds beyond the model:** Because the Cluster Agent is read-only, every hardening step is reported as a proposal expressed as a Kubernetes manifest or Config Connector field rather than…
- **Concerns:**
  - out of date [old-651932]: Rewrite section 2 to propose direct IAM binding to the KSA principal as the default and present the GSA annotation path as legacy, or repla…
  - out of place [place-69406c]: Keep the workload-level items (default-deny NetworkPolicy, PSS labels, runtimeClassName, SecretProviderClass, NetworkLogging) in the Cluste… Decision needed.
  - conflicts with gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) [conf-4a9226]: Option 3. The platform copy is right: direct IAM binding on the KSA principal is the current default and GSA impersonation is legacy, as gk… Decision needed.
  - conflicts with gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) [conf-b5e384]: Option 4. The cluster and platform copies are right (two ordered changes); only the upstream mirror is wrong. Report upstream; the overlay… Decision needed.
  - conflicts with gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) [conf-e46fb2]: Option 3. The cluster copy is right: GKE Sandbox is a node-pool setting. Patch the platform copy (overlay) to drop the cluster-level flag;… Decision needed.
  - duplicate with gke-workload-security (agents/platform/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) [dup-b3b16d]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/cluster/skills/gke-workload-troubleshooting`
- **Goal:** The step-by-step procedure the Cluster Agent follows to diagnose a failing GKE workload and hand the root cause and a patch back on its kanban card.
- **Adds beyond the model:** Diagnose in a fixed order (pod status, namespace events, logs, connectivity) inside a one-hour window centred on the container's last state transition, use git…
- **Concerns:**
  - conflicts with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-cb2e3b]: Option 3. The cluster copy gives the better default (centre the log window on the pod's last state transition, fall back to now). Patch the… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-fad338]: Option 4. The cluster and platform copies are right (bounds inside the filter); only the upstream mirror is wrong. Report upstream. Decision needed.

### capacity-obtainability

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/capacity-obtainability`
- **Goal:** Gather live quota and hardware-availability evidence before recommending GKE capacity, and find future reservation windows for deadline-bound GPU/TPU batch job…
- **Adds beyond the model:** Report quota and live obtainability separately with the verbatim sentence "Quota is separate from live capacity." and never the word "guarantee", probe Spot an…
- **Concerns:**
  - conflicts with gke-stockout-investigator [conf-937bf6]: Option 3. capacity-obtainability is right: a reservation holds capacity and the report must never say "guarantee". Patch line 159 of gke-st… Decision needed.

### cluster-agent-lifecycle

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/cluster-agent-lifecycle`
- **Goal:** Tells the Platform Agent when to create or delete a cluster's Cluster Agent profile and how to hand single-cluster debugging work to it through the kanban boar…
- **Adds beyond the model:** Profiles are created only at onboarding and deleted only at teardown (never repaired from other work or by the discovery sweep; use scope exclusion for a live…
- **Concerns:** none

### fleet-audit

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/fleet-audit`
- **Goal:** Lets the Platform Agent run a fleet audit and publish what it found as one tracked ledger issue per audit stream plus small fix pull requests, with the harness…
- **Adds beyond the model:** The agent only inspects read-only and emits a validated findings.json (one finding per durable object, literal commands per check, no invented ids, timestamps…
- **Concerns:**
  - out of date [old-e716c6]: Update the docstring's usage block to list all seven subcommands (start, finish, remediate, fetch, list, grep, draft), name the nine regist…

### fleet-audit-reports

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/fleet-audit-reports`
- **Goal:** Answer questions about what earlier fleet audits found by querying the stored run envelopes through a small script instead of reading the large report files.
- **Adds beyond the model:** Answer every question about a past audit only through report_query.py's seven bounded subcommands, never by opening a store file; treat an absent, unreadable,…
- **Concerns:**
  - invalid front matter [fm-43438a]: Quote the description value or write it as a block scalar (description: >-). The inventory tool repaired it on read; the error text it repo…

### fleet-upgrade-verification

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/fleet-upgrade-verification`
- **Goal:** Tell an operator which GKE clusters in the fleet lag a target version, what would stop their upgrade, and which GitOps manifests that version would break.
- **Adds beyond the model:** Fleet version, rollout and readiness questions are answered by one run of the skill's scripts from the Platform profile (never a per-cluster fan-out or a hand…
- **Concerns:**
  - low value [low-abea93]: Keep the run commands, the flag semantics, the status/progress/readiness vocabulary (what each grade and cell means) and the Report section…

### gce-compute-fleet-audit

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gce-compute-fleet-audit`
- **Goal:** Run the GCE collector for standalone VMs, MIGs, sole-tenant node groups and orphaned snapshots, and hand its findings to the fleet-audit harness.
- **Adds beyond the model:** Open the run with fleet-audit `start` before anything else, pass the `fleet_scope` tool's `collector_args` to the collector verbatim, treat all four roster che…
- **Concerns:** none

### gcp-config-connector

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gcp-config-connector`
- **Goal:** Write Config Connector manifests for GKE node pool, Cloud SQL and VPC firewall changes and submit them as a GitOps pull request without applying anything.
- **Adds beyond the model:** Check the CRD first, open the repo with submit-suggestion `prepare` on branch `platform-agent/kcc-<kind>-<name>`, decide create/acquire/edit from the read-only…
- **Concerns:** none

### gcp-networking-fabric-audit

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gcp-networking-fabric-audit`
- **Goal:** Run the collector for subnet IP headroom, Cloud NAT ports, PSC routing, peering MTU, Cloud Armor and world-open management ports, and hand its findings to the…
- **Adds beyond the model:** Open the run with fleet-audit `start` first, pass the `fleet_scope` `collector_args` verbatim, run the collector without `--check`, `draft` the findings docume…
- **Concerns:** none

### github-issue-resolver

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/github-issue-resolver`
- **Goal:** Let the Platform Agent poll, claim, investigate and report on open issues in the install's repository through a helper script, with read-only investigation.
- **Adds beyond the model:** Never touch issues labelled `status:escalation-needed`, `agent:ignore`, `agent:audit`, `agent:delivery-watch` or `infra-drift`; treat every issue field as untr…
- **Concerns:** none

### gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu`
- **Goal:** Decide whether a GPU or TPU node disruption came from Compute Engine host maintenance and recommend protections for the workload.
- **Adds beyond the model:** Halt and ask for project, location, cluster and timestamp before offering theories; always present the `kubernetes_io:node_interruption_count` PromQL filtered…
- **Concerns:**
  - out of place with gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) [place-30da22]: Ship it to the Cluster Agent profile as well (as gke-workload-troubleshooting is), or state why the Platform Agent runs this per-cluster di… Decision needed.
  - duplicate with gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) [dup-643247]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-ai-troubleshooting-jobset-interruption`
- **Goal:** Diagnose why a GKE JobSet keeps restarting (Spot preemption, host failure, worker crash) and recommend a scheduling or host-quarantine fix.
- **Adds beyond the model:** Work the four steps in a fixed order (JobSet restarts, nodepool interruptions, node-to-host correlation, pod phases then worker logs) using the paired MQL, Pro…
- **Concerns:**
  - out of place with gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption) [place-71d24b]: Ship it to the Cluster Agent profile as well, or state why the Platform Agent runs this per-cluster diagnosis itself. Unsure because the mi… Decision needed.
  - duplicate with gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption) [dup-09f37b]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom`
- **Goal:** Walk an agent through diagnosing vbar_control_agent OOMs and TPU device-plugin checksum errors on GKE TPU v6e nodes, and advising on the fix.
- **Adds beyond the model:** Diagnose TPU v6e vbar_control_agent crashes in a fixed order inside a +/-30-minute window (serial-console OOM, tpu-device-plugin checksum errors, then search f…
- **Concerns:**
  - out of place with gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom) [place-f7089e]: Decide whether the Cluster Agent profile should carry this runbook. It is a mirrored gke-* skill, so moving it means either mirroring into… Decision needed.
  - duplicate with gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom) [dup-b868a4]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-app-onboarding (agents/platform/skills/gke-app-onboarding)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-app-onboarding`
- **Goal:** Guide an agent through containerizing an application and deploying it to GKE for the first time.
- **Adds beyond the model:** Deploy through the GKE MCP apply_k8s_manifest tool before falling back to kubectl, require requests/limits, probes, at least two replicas, ClusterIP plus Gatew…
- **Concerns:**
  - low value [low-235c89]: Cut the skill down to the assessment questions, the manifest checklist, the MCP-first deploy step and the Next Steps hand-offs; drop the Do… Decision needed.
  - out of date with gke-app-onboarding (third_party/google-skills/gke-app-onboarding) [old-cf6cda]: Replace the placeholder with a REGION-docker.pkg.dev path so the asset matches the Artifact Registry guidance in SKILL.md.
  - conflicts with gke-app-onboarding (third_party/google-skills/gke-app-onboarding) [conf-b0e7b5]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-app-onboarding (third_party/google-skills/gke-app-onboarding) [dup-c57a03]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-backup-dr (agents/platform/skills/gke-backup-dr)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-backup-dr`
- **Goal:** Tell an agent how to set up Backup for GKE plans, run restores safely, and apply the team's backup defaults.
- **Adds beyond the model:** Always pass --include-volume-data and --include-secrets, default restores to use-existing-version plus fail-on-conflict and get explicit confirmation before a…
- **Concerns:**
  - conflicts with gke-backup-dr (third_party/google-skills/gke-backup-dr) [conf-37aa78]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-backup-dr (third_party/google-skills/gke-backup-dr) [dup-0ce17e]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-basics (agents/platform/skills/gke-basics)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-basics`
- **Goal:** Give an agent the baseline rules for GKE work: Autopilot versus Standard, which tool to reach for, how to fetch credentials, and where sibling skills live.
- **Adds beyond the model:** Default to Autopilot with three named Standard exceptions, rank Developer Knowledge MCP over web search for facts and GKE MCP over gcloud over kubectl for oper…
- **Concerns:**
  - out of date [old-05fae9]: State that both modes carry the per-cluster management fee (free tier covers one zonal or Autopilot cluster) and that Autopilot additionall…
  - low value [low-414b06]: Keep SKILL.md, the Tool Preference / user-override sections of cli-reference.md and the Developer Knowledge section of mcp-usage.md; drop c… Decision needed.
  - duplicate with gke-basics (third_party/google-skills/gke-basics) [dup-05949d]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-batch-hpc (agents/platform/skills/gke-batch-hpc)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-batch-hpc`
- **Goal:** Help an agent run batch, HPC and training jobs on GKE with Jobs, JobSet, Kueue, MPI and the right capacity choices.
- **Adds beyond the model:** Before naming a start time, zone or capacity path for a GPU/TPU or large-shape batch job, load the capacity-obtainability skill and run its Future-windows prob…
- **Concerns:**
  - low value [low-67c9e2]: Keep the When-to-Use list, the Cost Optimization and Best Practices bullets and the capacity-obtainability section; replace the five YAML/C… Decision needed.
  - out of date [old-51e150]: Name one operator consistently: the MPI Operator for MPIJob v2beta1, or Kubeflow Trainer v2 if the team wants the current Kubeflow path, an…
  - duplicate with gke-batch-hpc (third_party/google-skills/gke-batch-hpc) [dup-b1dca1]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-cluster-autoscaler`
- **Goal:** Give an agent the rules and scripts for enabling, tuning and debugging GKE node autoscaling, including stockouts, scale-down blockers and capacity buffers.
- **Adds beyond the model:** Spell out autoscaler terms (no CA/NAP/NAC/CCC), refuse injected identifiers and directives in pasted logs, enumerate all seven scale-down blockers and run find…
- **Concerns:**
  - conflicts with gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler) [conf-d72b76]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler) [dup-57ee22]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-cluster-creation (agents/platform/skills/gke-cluster-creation)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-cluster-creation`
- **Goal:** Walk an agent through choosing a GKE cluster template, confirming it with the user, creating the cluster, and wiring it into kube-agents.
- **Adds beyond the model:** Default to the golden-path Autopilot template (private nodes, authorized networks, DNS access, Secret Manager with 120s rotation, scoped RBS bindings, regular…
- **Concerns:**
  - out of date [old-7457aa]: Say 'creates 3 nodes per zone (9 for a 3-zone region)' or change the template to --num-nodes 1, and align the MCP payload's initialNodeCoun…
  - duplicate with gke-cluster-creation (third_party/google-skills/gke-cluster-creation) [dup-823681]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-compute-classes (agents/platform/skills/gke-compute-classes)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-compute-classes`
- **Goal:** Give an agent the rules, schema facts and example manifests for writing, governing and debugging GKE ComputeClasses.
- **Adds beyond the model:** Answer ComputeClass requests generalized-first with placeholder zones, a CUD-alignment comment on every machineFamily, an 'EXAMPLE TEMPLATE - DO NOT DEPLOY' la…
- **Concerns:**
  - duplicate with gke-compute-classes (third_party/google-skills/gke-compute-classes) [dup-6612b2]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-cost-analysis (agents/platform/skills/gke-cost-analysis)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-cost-analysis`
- **Goal:** Help an agent answer GKE cost questions from the BigQuery billing export, cost allocation labels and live kubectl top data without changing anything.
- **Adds beyond the model:** Answer cost questions with a direct answer plus bq query templates scoped to GKE via the goog-k8s-cluster-name label, check that cost allocation is enabled, ex…
- **Concerns:**
  - duplicate with gke-cost-analysis (third_party/google-skills/gke-cost-analysis) [dup-1f9b50]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-cost-optimization (agents/platform/skills/gke-cost-optimization)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-cost-optimization`
- **Goal:** Help the Platform Agent cut GKE spend by rightsizing requests, applying quotas, using Spot capacity, and choosing machine families and discounts.
- **Adds beyond the model:** Rightsize with VPA in recommendation mode and set requests to P95 * 1.2 at the stated over-provisioning thresholds, prefer Spot through a ComputeClass with on-…
- **Concerns:**
  - low value with gke-cost-optimization (third_party/google-skills/gke-cost-optimization) [low-6cec87]: Keep the golden-path cost table, the optimization-rules table, the Spot ComputeClass with fallback plus the preemption warning, the dev/tes… Decision needed.
  - duplicate with gke-cost-optimization (third_party/google-skills/gke-cost-optimization) [dup-648d40]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-golden-path (agents/platform/skills/gke-golden-path)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-golden-path`
- **Goal:** Define the default Autopilot cluster configuration the agent applies, and audits against, when it designs or reviews a production GKE cluster.
- **Adds beyond the model:** Default every cluster design to the listed Autopilot golden-path values (private nodes, Dataplane V2, Cloud DNS, Secret Manager with 120s rotation, OPTIMIZE_UT…
- **Concerns:**
  - duplicate with gke-golden-path (third_party/google-skills/gke-golden-path) [dup-45c55e]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-inference (agents/platform/skills/gke-inference)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-inference`
- **Goal:** Deploy and tune LLM and other AI model servers on GKE with GPUs or TPUs.
- **Adds beyond the model:** Start from GKE Inference Quickstart (`gcloud container ai profiles`) to pick the model, server and accelerator tuple and generate the manifest, run it on an Au…
- **Concerns:**
  - low value with gke-inference (third_party/google-skills/gke-inference) [low-ba8315]: Keep the three-step GIQ workflow, the GPU ComputeClass and the inference-autoscaling best practices; drop the Accelerator Selection Guide,… Decision needed.
  - duplicate with gke-inference (third_party/google-skills/gke-inference) [dup-1e7056]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-manifest-generation (agents/platform/skills/gke-manifest-generation)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-manifest-generation`
- **Goal:** Write or edit Kubernetes manifests for GKE that follow the team's security, resource, probe and routing rules.
- **Adds beyond the model:** Every manifest gets an explicit namespace and a dedicated ServiceAccount, requests and limits with the stated density defaults, Spot selectors in -dev/-test/-s…
- **Concerns:**
  - out of date with gke-manifest-generation (third_party/google-skills/gke-manifest-generation) [old-ea1e0a]: Replace the two sentences with: Autopilot bills on requests; when limits differ from requests it sets limits equal to requests (requests ar…
  - conflicts with gke-manifest-generation (third_party/google-skills/gke-manifest-generation) [conf-aecc4e]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-manifest-generation (third_party/google-skills/gke-manifest-generation) [dup-b7c478]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-multitenancy (agents/platform/skills/gke-multitenancy)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-multitenancy`
- **Goal:** Set up a shared GKE cluster for several teams with namespace isolation, RBAC, quotas and network policy.
- **Adds beyond the model:** Default to namespace-per-team and escalate isolation only when compliance requires it, bind RBAC to Google Groups through namespace Roles, pair every ResourceQ…
- **Concerns:**
  - low value with gke-multitenancy (third_party/google-skills/gke-multitenancy) [low-788bf4]: Keep the model table with its recommendation, the Google Groups and namespace-Role rule, the LimitRange mandatory-defaults note, the DNS al… Decision needed.
  - duplicate with gke-multitenancy (third_party/google-skills/gke-multitenancy) [dup-25acb5]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-networking (agents/platform/skills/gke-networking)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-networking`
- **Goal:** Plan and configure GKE cluster networking: private clusters, VPC-native IP ranges, DNS, Dataplane V2 and egress.
- **Adds beyond the model:** Clusters are private, VPC-native, Dataplane V2 with Cloud DNS, 48 pods per node and auto IPAM, reached by default through the DNS endpoint; before passing `--d…
- **Concerns:**
  - low value [low-e6fe3c]: Keep the golden-path table, the access-pattern commands, the BYO-VPC Day-0 warning and the local `--dns-endpoint` section; drop VPC-Native… Decision needed.
  - duplicate with gke-networking (third_party/google-skills/gke-networking) [dup-abe210]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-observability (agents/platform/skills/gke-observability)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-observability`
- **Goal:** Configure logging, monitoring, managed Prometheus and alerts for a GKE cluster.
- **Adds beyond the model:** Enable the golden-path component set including APISERVER, SCHEDULER and CONTROLLER_MANAGER metrics with managed Prometheus, name Cloud Monitoring as the alerti…
- **Concerns:**
  - out of date with gke-observability (third_party/google-skills/gke-observability) [old-13f14a]: Change line 63 to `--enable-dataplane-v2-metrics`, which sets `advancedDatapathObservabilityConfig.enableMetrics`. Apply as an overlay patc…
  - low value with gke-observability (third_party/google-skills/gke-observability) [low-3c8a48]: Keep the golden-path defaults table, the enable commands, the Alerting section with its Production Rules and Node Health rules; drop the Ke… Decision needed.
  - duplicate with gke-observability (third_party/google-skills/gke-observability) [dup-81b83e]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…
  - conflicts with gke-observability (agents/cluster/skills/gke-observability) [conf-0feb2d]: Option 3. The platform copy is right on both points (Autopilot supports control-plane metrics; the golden-path component list is the full s… Decision needed.
  - conflicts with gke-observability (agents/cluster/skills/gke-observability) [conf-9a2485]: Option 3. The platform copy is right on both points (Autopilot supports control-plane metrics; the golden-path component list is the full s… Decision needed.
  - duplicate with gke-observability (agents/cluster/skills/gke-observability), gke-observability (third_party/google-skills/gke-observability) [dup-ed076d]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-platform-security (agents/platform/skills/gke-platform-security)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-platform-security`
- **Goal:** Harden a GKE cluster's control plane and node settings: Secret Manager add-on, RBAC, Binary Authorization, Shielded Nodes, secrets encryption and IAM roles.
- **Adds beyond the model:** Clusters keep the golden-path security defaults (Workload Identity pool, Secret Manager with 120s rotation, insecure bindings off, Shielded Nodes, GKE_METADATA…
- **Concerns:**
  - out of date with gke-platform-security (third_party/google-skills/gke-platform-security) [old-12b4ae]: Replace the block with the node-pool form for Standard (`gcloud container node-pools create <POOL> --cluster <CLUSTER> --sandbox type=gviso…
  - low value [low-e5fabe]: Keep the defaults table, Secret Manager and RBAC sections, Binary Authorization, the Service Accounts bullets and the local secrets-encrypt… Decision needed.
  - conflicts with gke-platform-security (third_party/google-skills/gke-platform-security) [conf-6bb808]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-platform-security (third_party/google-skills/gke-platform-security) [dup-cb4e8f]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-productionize (agents/platform/skills/gke-productionize)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-productionize`
- **Goal:** Run a production-readiness review of a GKE cluster or application by discovering its state and delegating each domain to the matching skill.
- **Adds beyond the model:** Production readiness is a fixed sequence: discover cluster and workload state, then run each named domain skill (app-onboarding, workload-scaling, observabilit…
- **Concerns:**
  - conflicts with gke-productionize (third_party/google-skills/gke-productionize) [conf-1e0e2d]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-productionize (third_party/google-skills/gke-productionize) [dup-13c04c]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-reliability (agents/platform/skills/gke-reliability)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-reliability`
- **Goal:** Make GKE workloads survive node, zone and upgrade disruptions with PDBs, health probes, graceful shutdown and topology spread.
- **Adds beyond the model:** House defaults: regional four-zone cluster on the REGULAR channel with SURGE upgrades and auto-repair/upgrade; a PDB on every production workload with 2+ repli…
- **Concerns:**
  - low value with gke-reliability (third_party/google-skills/gke-reliability) [low-1bc1ab]: Keep the Golden Path table, the probe values, the Replicas table and the Best Practices list; drop the PDB/probe/preStop/topology explanati… Decision needed.
  - duplicate with gke-reliability (third_party/google-skills/gke-reliability) [dup-b69159]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…
  - conflicts with gke-reliability (agents/cluster/skills/gke-reliability) [conf-e64b5d]: Option 3. Pick one audit bar for the fleet. We recommend the platform copy's stricter rule (both probes; a PDB on every 2+ replica producti… Decision needed.
  - conflicts with gke-reliability (agents/cluster/skills/gke-reliability) [conf-a22a9b]: Option 3. Pick one audit bar for the fleet. We recommend the platform copy's stricter rule (both probes; a PDB on every 2+ replica producti… Decision needed.
  - duplicate with gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (third_party/google-skills/gke-reliability) [dup-6ba2a7]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-service-networking (agents/platform/skills/gke-service-networking)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-service-networking`
- **Goal:** Expose GKE services to the internet or other VPCs with Gateway API or Ingress, Cloud Armor, managed certificates, NEGs and Private Service Connect.
- **Adds beyond the model:** Prefer Gateway API (gatewayClass gke-l7-global-external-managed) over Ingress, always front public endpoints with Cloud Armor, use Google-managed certificates,…
- **Concerns:**
  - low value with gke-service-networking (third_party/google-skills/gke-service-networking) [low-134424]: Keep the four Best Practices, the chosen gatewayClassName and the BackendConfig/Service annotation wiring; drop the generic Gateway, HTTPRo… Decision needed.
  - duplicate with gke-service-networking (third_party/google-skills/gke-service-networking) [dup-7e054c]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-storage (agents/platform/skills/gke-storage)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-storage`
- **Goal:** Provision and resize persistent storage for GKE workloads with the right StorageClass, Filestore for shared access and GCS FUSE for bucket mounts.
- **Adds beyond the model:** Golden-path CSI set (PD, Filestore, GCS FUSE, Parallelstore; pd-balanced boot disks) and StorageClass defaults: allowVolumeExpansion true on every class, regio…
- **Concerns:**
  - out of date with gke-storage (third_party/google-skills/gke-storage) [old-d4508b]: Change the row to standard-rwo = pd-balanced (general purpose) and, if a pd-standard class is wanted, name the legacy `standard` class or a…
  - low value with gke-storage (third_party/google-skills/gke-storage) [low-408f69]: Keep the golden-path table, the custom StorageClass defaults and the Best Practices; drop the generic PVC examples and the expansion explan… Decision needed.
  - duplicate with gke-storage (third_party/google-skills/gke-storage) [dup-210197]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…
  - conflicts with gke-storage (agents/cluster/skills/gke-storage) [conf-dd74e6]: Option 1. The platform copy is right (standard-rwx is the built-in Filestore class; premium-rwo is a built-in zonal pd-ssd class). Retire t… Decision needed.
  - conflicts with gke-storage (agents/cluster/skills/gke-storage) [conf-8c70b6]: Option 1. The platform copy is right (standard-rwx is the built-in Filestore class; premium-rwo is a built-in zonal pd-ssd class). Retire t… Decision needed.
  - duplicate with gke-storage (agents/cluster/skills/gke-storage), gke-storage (third_party/google-skills/gke-storage) [dup-cc232f]: Keep the platform copy (generated from the upstream source of truth). Remove the cluster copy; if the Cluster Agent needs storage help, it… Decision needed.

### gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-tpu-dynamic-slices-monitoring`
- **Goal:** Inspect GKE TPU Dynamic Slice custom resources, explain their lifecycle state, check workload manifests target a slice correctly, and clean up stuck slices or…
- **Adds beyond the model:** Start every slice question with kubectl describe slice and read Status.Conditions against the fixed state/reason table and the three-point provisioning checkli…
- **Concerns:**
  - low value with gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring) [low-228e4a]: Delete the no-op script from the mirrored copy (or exclude it in the overlay); SKILL.md never references it. This is a mirrored skill: the… Decision needed.
  - duplicate with gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring) [dup-01b7c5]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-tpu-metrics-monitoring (agents/platform/skills/gke-tpu-metrics-monitoring)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-tpu-metrics-monitoring`
- **Goal:** Tell whether a GKE TPU workload's interruptions or slowness come from the nodes and node pools underneath it, using GKE system metrics and ready-made PromQL.
- **Adds beyond the model:** A fixed diagnostic order (confirm metric export on port 8431, runtime duty cycle and memory, node Ready condition, node-pool status and multi-host availability…
- **Concerns:**
  - duplicate with gke-tpu-metrics-monitoring (third_party/google-skills/gke-tpu-metrics-monitoring) [dup-8d741a]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-upgrades (agents/platform/skills/gke-upgrades)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-upgrades`
- **Goal:** Guide an agent through planning, running, and unsticking GKE cluster and node pool upgrades without losing workload protection.
- **Adds beyond the model:** Frame every upgrade around auto-upgrade with maintenance windows and exclusions, default node pools to surge with per-workload maxSurge values (zero surge for…
- **Concerns:**
  - out of date [old-e5c4a5]: Replace the command in all three places with `kubectl get --raw /metrics | grep apiserver_requested_deprecated_apis` (and keep the pointer…
  - conflicts with gke-upgrades (third_party/google-skills/gke-upgrades) [conf-cb96e1]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-upgrades (third_party/google-skills/gke-upgrades) [dup-74b14d]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-workload-identity (agents/platform/skills/gke-workload-identity)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-workload-identity`
- **Goal:** Find out why a Pod cannot authenticate to Google Cloud through Workload Identity Federation and hand a human the exact fix.
- **Adds beyond the model:** Read-only and non-interactive: name one root cause, rule the others out explicitly, propose the exact gcloud or GitOps change and never apply IAM, KSA or node-…
- **Concerns:**
  - duplicate with gke-workload-identity (third_party/google-skills/gke-workload-identity) [dup-50a096]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-workload-scaling (agents/platform/skills/gke-workload-scaling)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-workload-scaling`
- **Goal:** Scale GKE workloads with manual replicas, HPA and VPA, and right-size their resource requests.
- **Adds beyond the model:** Manifests over kubectl autoscale, HPA on CPU with VPA on memory to avoid thrashing, a right-sizing workflow (VPA Off for 24h, apply target times 1.2, with the…
- **Concerns:**
  - out of date with gke-workload-scaling (third_party/google-skills/gke-workload-scaling) [old-6cf579]: State that External metrics require the Custom Metrics Stackdriver Adapter (custom-metrics-stackdriver-adapter) deployed in the cluster, or…
  - duplicate with gke-workload-scaling (third_party/google-skills/gke-workload-scaling) [dup-3f0ff2]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-workload-security (agents/platform/skills/gke-workload-security)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-workload-security`
- **Goal:** Audit and harden the security of GKE workloads and namespaces: network policies, gVisor sandboxing, Pod Security Standards and Secret Manager CSI mounts.
- **Adds beyond the model:** Run audit_cluster.sh first; route Workload Identity to gke-workload-identity and use GSA impersonation only when a GSA must be the identity; check datapathProv…
- **Concerns:**
  - conflicts with gke-workload-security (third_party/google-skills/gke-workload-security) [conf-baafb0]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - conflicts with gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) [conf-4a9226]: Option 3. The platform copy is right: direct IAM binding on the KSA principal is the current default and GSA impersonation is legacy, as gk… Decision needed.
  - conflicts with gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) [conf-b5e384]: Option 4. The cluster and platform copies are right (two ordered changes); only the upstream mirror is wrong. Report upstream; the overlay… Decision needed.
  - conflicts with gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) [conf-e46fb2]: Option 3. The cluster copy is right: GKE Sandbox is a node-pool setting. Patch the platform copy (overlay) to drop the cluster-level flag;… Decision needed.
  - duplicate with gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (third_party/google-skills/gke-workload-security) [dup-b3b16d]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/gke-workload-troubleshooting`
- **Goal:** Diagnose why a GKE pod is Pending, crashing, OOMKilled or failing to pull its image, and propose the manifest fix through GitOps.
- **Adds beyond the model:** Discover context non-interactively and fall back to handing the operator the kubectl commands when the cluster is unreachable instead of retrying; centre a one…
- **Concerns:**
  - conflicts with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-f492c5]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-cb2e3b]: Option 3. The cluster copy gives the better default (centre the log window on the pod's last state transition, fall back to now). Patch the… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-fad338]: Option 4. The cluster and platform copies are right (bounds inside the filter); only the upstream mirror is wrong. Report upstream. Decision needed.
  - conflicts with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [conf-e9fbf7]: Option 4. The shipped copy is right for this install (SOUL.md forbids an unrequested pull request). Keep the overlay; report upstream. Decision needed.
  - duplicate with gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) [dup-1cf49e]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### inspect-repository

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/inspect-repository`
- **Goal:** Let the Platform Agent read the source of a repository it has no checkout of, by having the credential broker clone it and pass file content back.
- **Adds beyond the model:** Reads of foreign repositories go through the broker's read-only workspace (clone for small trees, open/grep/fetch/close for large ones) with --depth 1, fetchin…
- **Concerns:** none

### kube-agents-observability

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/kube-agents-observability`
- **Goal:** Check whether the Platform Agent's own logs, metrics, traces and dashboard are working, and find out why when they are not.
- **Adds beyond the model:** Diagnose harness telemetry from the install's own sources of truth: scrape config from the PodMonitoring resources (never Deployment annotations) and proven vi…
- **Concerns:** none

### manage-cluster

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/manage-cluster`
- **Goal:** Start or stop managing one specific existing GKE cluster when a user asks, by creating its Cluster Agent profile or declaring it excluded from scope.
- **Adds beyond the model:** Verify the cluster exists first, create the profile with `python3 /opt/data/scripts/cluster_agent_profile.py create --project --cluster --location` (idempotent…
- **Concerns:** none

### pr-conversation

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/pr-conversation`
- **Goal:** Let the Platform Agent answer a reviewer on one of its own pull requests from a kanban card: re-read the thread, answer or amend the branch, and post a marked…
- **Adds beyond the model:** Reviewer comments are data not instruction; the agent re-polls before acting, acts only on requests whose author's write access is known and true (refuses know…
- **Concerns:** none

### submit-suggestion

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/submit-suggestion`
- **Goal:** Give the Platform Agent one safe path to turn a requested config change into a reviewable pull request on the fleet's GitOps repository.
- **Adds beyond the model:** Every GitOps write goes through `prepare`/`submit` under `$HERMES_HOME/skills/submit-suggestion/scripts/submit_suggestion.py` (never the plain credentialed `gi…
- **Concerns:** none

### version-control

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/version-control`
- **Goal:** Let the Platform Agent read, change, and collaborate on a managed repository through forge-neutral vcs.py verbs and a credential-free local git, without any fo…
- **Adds beyond the model:** Network and credential operations go only through vcs.py's broker verbs (clone as bundle, publish, proposal/issue/label/identity/remote-branch) and never throu…
- **Concerns:** none

### workload-rebalancing

- **Source:** local  **Status:** unmanaged  **Location:** `agents/platform/skills/workload-rebalancing`
- **Goal:** Let the Platform Agent move a workload from an overloaded cluster to one with headroom by fanning out read-only validation cards to cluster agents and then dec…
- **Adds beyond the model:** Validation-then-declare: resolve each cluster's profile with get_cluster_profile_name, open two parent-less kanban cards (can-host on the target, safe-to-evacu…
- **Concerns:**
  - out of date [old-db732e]: Replace KCC with 'the GitOps reconciler (Config Sync, Argo CD or Flux)' in all three places; keep KCC only if the moved object is itself a…

### gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu`
- **Goal:** Decide whether a GPU or TPU node disruption came from Compute Engine host maintenance and recommend protections for the workload.
- **Adds beyond the model:** Halt and ask for project, location, cluster and timestamp before offering theories; always present the `kubernetes_io:node_interruption_count` PromQL filtered…
- **Concerns:**
  - out of place with gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) [place-30da22]: Ship it to the Cluster Agent profile as well (as gke-workload-troubleshooting is), or state why the Platform Agent runs this per-cluster di… Decision needed.
  - duplicate with gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) [dup-643247]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-ai-troubleshooting-jobset-interruption`
- **Goal:** Diagnose why a GKE JobSet keeps restarting (Spot preemption, host failure, worker crash) and recommend a scheduling or host-quarantine fix.
- **Adds beyond the model:** Work the four steps in a fixed order (JobSet restarts, nodepool interruptions, node-to-host correlation, pod phases then worker logs) using the paired MQL, Pro…
- **Concerns:**
  - out of place with gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption) [place-71d24b]: Ship it to the Cluster Agent profile as well, or state why the Platform Agent runs this per-cluster diagnosis itself. Unsure because the mi… Decision needed.
  - duplicate with gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption) [dup-09f37b]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom`
- **Goal:** Walk an agent through diagnosing vbar_control_agent OOMs and TPU device-plugin checksum errors on GKE TPU v6e nodes, and advising on the fix.
- **Adds beyond the model:** Diagnose TPU v6e vbar_control_agent crashes in a fixed order inside a +/-30-minute window (serial-console OOM, tpu-device-plugin checksum errors, then search f…
- **Concerns:**
  - out of place with gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom) [place-f7089e]: Decide whether the Cluster Agent profile should carry this runbook. It is a mirrored gke-* skill, so moving it means either mirroring into… Decision needed.
  - duplicate with gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom) [dup-b868a4]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-app-onboarding (third_party/google-skills/gke-app-onboarding)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-app-onboarding`
- **Goal:** Guide an agent through containerizing an application and deploying it to GKE for the first time: assess, build the image, push to Artifact Registry, write mani…
- **Adds beyond the model:** Prefer multi-stage distroless non-root images (or Buildpacks when no Dockerfile is wanted), push to Artifact Registry with vulnerability scanning on, ship mani…
- **Concerns:**
  - out of date with gke-app-onboarding (agents/platform/skills/gke-app-onboarding) [old-cf6cda]: Replace the placeholder with a REGION-docker.pkg.dev path so the asset matches the Artifact Registry guidance in SKILL.md.
  - conflicts with gke-app-onboarding (agents/platform/skills/gke-app-onboarding) [conf-b0e7b5]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-app-onboarding (agents/platform/skills/gke-app-onboarding) [dup-c57a03]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-backup-dr (third_party/google-skills/gke-backup-dr)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-backup-dr`
- **Goal:** Guide an agent through setting up Backup for GKE (addon, backup plans, restore plans, restores) and running a restore safely.
- **Adds beyond the model:** Always pass --include-volume-data and --include-secrets explicitly, prefer the safe conflict policies (use-existing-version plus fail-on-conflict), validate re…
- **Concerns:**
  - conflicts with gke-backup-dr (agents/platform/skills/gke-backup-dr) [conf-37aa78]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-backup-dr (agents/platform/skills/gke-backup-dr) [dup-0ce17e]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-basics (third_party/google-skills/gke-basics)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-basics`
- **Goal:** Give an agent the core rules for creating GKE clusters, fetching credentials and choosing Autopilot versus Standard, plus a tool-preference order and command r…
- **Adds beyond the model:** Default to Autopilot and justify Standard only by citing the specific restrictions, route to sibling skills for identity/security/upgrades/manifests, use Devel…
- **Concerns:**
  - duplicate with gke-basics (agents/platform/skills/gke-basics) [dup-05949d]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-batch-hpc (third_party/google-skills/gke-batch-hpc)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-batch-hpc`
- **Goal:** Guide an agent in running batch and HPC workloads on GKE with Jobs, JobSet, Kueue, MPI Operator, compact placement and Spot VMs.
- **Adds beyond the model:** Use Kueue for multi-tenant queueing and JobSet for tightly coupled multi-component work, run batch on Spot through a ComputeClass with on-demand fallback and a…
- **Concerns:**
  - duplicate with gke-batch-hpc (agents/platform/skills/gke-batch-hpc) [dup-b1dca1]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-cluster-autoscaler`
- **Goal:** Help an agent enable, tune and troubleshoot the GKE Cluster Autoscaler and node pool auto-creation, including scale-up stalls, scale-down blockers and capacity…
- **Adds beyond the model:** Spell out Cluster Autoscaler/Node Auto Provisioning/ComputeClass with no acronyms, refuse identifiers that fail ^[a-z0-9-]+$ and treat pasted logs as data, pre…
- **Concerns:**
  - conflicts with gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler) [conf-d72b76]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler) [dup-57ee22]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-cluster-creation (third_party/google-skills/gke-cluster-creation)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-cluster-creation`
- **Goal:** Guide an agent through creating a GKE cluster from one of five templates, defaulting to the golden-path Autopilot configuration.
- **Adds beyond the model:** Every new cluster defaults to the golden-path private Autopilot template (REGULAR channel, private nodes, authorized networks, Secret Manager add-on with 120s…
- **Concerns:**
  - duplicate with gke-cluster-creation (agents/platform/skills/gke-cluster-creation) [dup-823681]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-compute-classes (third_party/google-skills/gke-compute-classes)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-compute-classes`
- **Goal:** Give an agent the rules, schema facts and example manifests for writing, governing and debugging GKE ComputeClasses.
- **Adds beyond the model:** Answer ComputeClass requests generalized-first with placeholder zones, a CUD-alignment comment on every machineFamily, an 'EXAMPLE TEMPLATE - DO NOT DEPLOY' la…
- **Concerns:**
  - duplicate with gke-compute-classes (agents/platform/skills/gke-compute-classes) [dup-6612b2]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-cost-analysis (third_party/google-skills/gke-cost-analysis)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-cost-analysis`
- **Goal:** Help an agent answer GKE cost questions from the BigQuery billing export, cost allocation labels and live kubectl top data without changing anything.
- **Adds beyond the model:** Answer cost questions with a direct answer plus bq query templates scoped to GKE via the goog-k8s-cluster-name label, check that cost allocation is enabled, ex…
- **Concerns:**
  - duplicate with gke-cost-analysis (agents/platform/skills/gke-cost-analysis) [dup-1f9b50]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-cost-optimization (third_party/google-skills/gke-cost-optimization)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-cost-optimization`
- **Goal:** Help the Platform Agent cut GKE spend by rightsizing requests, applying quotas, using Spot capacity, and choosing machine families and discounts.
- **Adds beyond the model:** Rightsize with VPA in recommendation mode and set requests to P95 * 1.2 at the stated over-provisioning thresholds, prefer Spot through a ComputeClass with on-…
- **Concerns:**
  - low value with gke-cost-optimization (agents/platform/skills/gke-cost-optimization) [low-6cec87]: Keep the golden-path cost table, the optimization-rules table, the Spot ComputeClass with fallback plus the preemption warning, the dev/tes… Decision needed.
  - duplicate with gke-cost-optimization (agents/platform/skills/gke-cost-optimization) [dup-648d40]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-golden-path (third_party/google-skills/gke-golden-path)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-golden-path`
- **Goal:** Define the default Autopilot cluster configuration the agent applies, and audits against, when it designs or reviews a production GKE cluster.
- **Adds beyond the model:** Default every cluster design to the listed Autopilot golden-path values (private nodes, Dataplane V2, Cloud DNS, Secret Manager with 120s rotation, OPTIMIZE_UT…
- **Concerns:**
  - duplicate with gke-golden-path (agents/platform/skills/gke-golden-path) [dup-45c55e]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-inference (third_party/google-skills/gke-inference)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-inference`
- **Goal:** Deploy and tune LLM and other AI model servers on GKE with GPUs or TPUs.
- **Adds beyond the model:** Start from GKE Inference Quickstart (`gcloud container ai profiles`) to pick the model, server and accelerator tuple and generate the manifest, run it on an Au…
- **Concerns:**
  - low value with gke-inference (agents/platform/skills/gke-inference) [low-ba8315]: Keep the three-step GIQ workflow, the GPU ComputeClass and the inference-autoscaling best practices; drop the Accelerator Selection Guide,… Decision needed.
  - duplicate with gke-inference (agents/platform/skills/gke-inference) [dup-1e7056]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-manifest-generation (third_party/google-skills/gke-manifest-generation)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-manifest-generation`
- **Goal:** Generate or edit Kubernetes manifests for GKE workloads that follow a fixed set of security, sizing, probe and routing rules.
- **Adds beyond the model:** House defaults for every manifest: explicit namespace and a dedicated ServiceAccount, conservative Standard requests with 2x-4x limits and equal requests/limit…
- **Concerns:**
  - out of date with gke-manifest-generation (agents/platform/skills/gke-manifest-generation) [old-ea1e0a]: Replace the two sentences with: Autopilot bills on requests; when limits differ from requests it sets limits equal to requests (requests ar…
  - conflicts with gke-manifest-generation (agents/platform/skills/gke-manifest-generation) [conf-aecc4e]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-manifest-generation (agents/platform/skills/gke-manifest-generation) [dup-b7c478]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-multitenancy (third_party/google-skills/gke-multitenancy)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-multitenancy`
- **Goal:** Set up a shared GKE cluster for several teams with namespace isolation, RBAC, quotas and network policy.
- **Adds beyond the model:** Default to namespace-per-team and escalate isolation only when compliance requires it, bind RBAC to Google Groups through namespace Roles, pair every ResourceQ…
- **Concerns:**
  - low value with gke-multitenancy (agents/platform/skills/gke-multitenancy) [low-788bf4]: Keep the model table with its recommendation, the Google Groups and namespace-Role rule, the LimitRange mandatory-defaults note, the DNS al… Decision needed.
  - duplicate with gke-multitenancy (agents/platform/skills/gke-multitenancy) [dup-25acb5]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-networking (third_party/google-skills/gke-networking)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-networking`
- **Goal:** Set the network layout of a GKE cluster: private nodes, VPC-native ranges, Dataplane V2, DNS endpoint access, IP sizing and egress.
- **Adds beyond the model:** Golden-path networking defaults for every cluster: private nodes with private-endpoint enforcement and DNS-endpoint access, Dataplane V2, Cloud DNS, intra-node…
- **Concerns:**
  - duplicate with gke-networking (agents/platform/skills/gke-networking) [dup-abe210]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-observability (third_party/google-skills/gke-observability)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-observability`
- **Goal:** Configure logging, monitoring, managed Prometheus and alerts for a GKE cluster.
- **Adds beyond the model:** Enable the golden-path component set including APISERVER, SCHEDULER and CONTROLLER_MANAGER metrics with managed Prometheus, name Cloud Monitoring as the alerti…
- **Concerns:**
  - out of date with gke-observability (agents/platform/skills/gke-observability) [old-13f14a]: Change line 63 to `--enable-dataplane-v2-metrics`, which sets `advancedDatapathObservabilityConfig.enableMetrics`. Apply as an overlay patc…
  - low value with gke-observability (agents/platform/skills/gke-observability) [low-3c8a48]: Keep the golden-path defaults table, the enable commands, the Alerting section with its Production Rules and Node Health rules; drop the Ke… Decision needed.
  - duplicate with gke-observability (agents/platform/skills/gke-observability) [dup-81b83e]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…
  - duplicate with gke-observability (agents/cluster/skills/gke-observability), gke-observability (agents/platform/skills/gke-observability) [dup-ed076d]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-platform-security (third_party/google-skills/gke-platform-security)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-platform-security`
- **Goal:** Harden cluster-level GKE security: Secret Manager add-on, RBAC binding config, Binary Authorization, Shielded Nodes, GKE Sandbox enablement and IAM roles.
- **Adds beyond the model:** Golden-path security defaults (Secret Manager add-on with 120s rotation, insecure system:authenticated and system:unauthenticated bindings disabled, secure boo…
- **Concerns:**
  - out of date with gke-platform-security (agents/platform/skills/gke-platform-security) [old-12b4ae]: Replace the block with the node-pool form for Standard (`gcloud container node-pools create <POOL> --cluster <CLUSTER> --sandbox type=gviso…
  - out of date [old-04c923]: Point line 166 (and line 23-25 in the intro) at gke-workload-identity. The repository overlay agents/platform/skill-overlays/gke-platform-s…
  - conflicts with gke-platform-security (agents/platform/skills/gke-platform-security) [conf-6bb808]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-platform-security (agents/platform/skills/gke-platform-security) [dup-cb4e8f]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-productionize (third_party/google-skills/gke-productionize)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-productionize`
- **Goal:** Run a production-readiness review of a GKE cluster or workload by delegating each domain to its specialist skill and reporting a RAG score.
- **Adds beyond the model:** The review is an orchestration, not an implementation: discover cluster and workload state first, invoke each domain skill in turn (onboarding, workload scalin…
- **Concerns:**
  - out of date [old-5a7c45]: Name gke-workload-identity for the Workload Identity item and keep the other two for Network Policies and Shielded Nodes. The overlay agent…
  - out of date [old-1b10d8]: Replace gke-scaling in the description with gke-workload-scaling (and gke-cluster-autoscaler if cluster-level scaling is meant).
  - conflicts with gke-productionize (agents/platform/skills/gke-productionize) [conf-1e0e2d]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-productionize (agents/platform/skills/gke-productionize) [dup-13c04c]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-reliability (third_party/google-skills/gke-reliability)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-reliability`
- **Goal:** Make GKE workloads survive node, zone and upgrade disruptions with PDBs, health probes, graceful shutdown and topology spread.
- **Adds beyond the model:** House defaults: regional four-zone cluster on the REGULAR channel with SURGE upgrades and auto-repair/upgrade; a PDB on every production workload with 2+ repli…
- **Concerns:**
  - low value with gke-reliability (agents/platform/skills/gke-reliability) [low-1bc1ab]: Keep the Golden Path table, the probe values, the Replicas table and the Best Practices list; drop the PDB/probe/preStop/topology explanati… Decision needed.
  - duplicate with gke-reliability (agents/platform/skills/gke-reliability) [dup-b69159]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…
  - duplicate with gke-reliability (agents/cluster/skills/gke-reliability), gke-reliability (agents/platform/skills/gke-reliability) [dup-6ba2a7]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-service-networking (third_party/google-skills/gke-service-networking)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-service-networking`
- **Goal:** Expose GKE services to the internet or other VPCs with Gateway API or Ingress, Cloud Armor, managed certificates, NEGs and Private Service Connect.
- **Adds beyond the model:** Prefer Gateway API (gatewayClass gke-l7-global-external-managed) over Ingress, always front public endpoints with Cloud Armor, use Google-managed certificates,…
- **Concerns:**
  - low value with gke-service-networking (agents/platform/skills/gke-service-networking) [low-134424]: Keep the four Best Practices, the chosen gatewayClassName and the BackendConfig/Service annotation wiring; drop the generic Gateway, HTTPRo… Decision needed.
  - duplicate with gke-service-networking (agents/platform/skills/gke-service-networking) [dup-7e054c]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-storage (third_party/google-skills/gke-storage)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-storage`
- **Goal:** Provision and resize persistent storage for GKE workloads with the right StorageClass, Filestore for shared access and GCS FUSE for bucket mounts.
- **Adds beyond the model:** Golden-path CSI set (PD, Filestore, GCS FUSE, Parallelstore; pd-balanced boot disks) and StorageClass defaults: allowVolumeExpansion true on every class, regio…
- **Concerns:**
  - out of date with gke-storage (agents/platform/skills/gke-storage) [old-d4508b]: Change the row to standard-rwo = pd-balanced (general purpose) and, if a pd-standard class is wanted, name the legacy `standard` class or a…
  - low value with gke-storage (agents/platform/skills/gke-storage) [low-408f69]: Keep the golden-path table, the custom StorageClass defaults and the Best Practices; drop the generic PVC examples and the expansion explan… Decision needed.
  - duplicate with gke-storage (agents/platform/skills/gke-storage) [dup-210197]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…
  - duplicate with gke-storage (agents/cluster/skills/gke-storage), gke-storage (agents/platform/skills/gke-storage) [dup-cc232f]: Keep the platform copy (generated from the upstream source of truth). Remove the cluster copy; if the Cluster Agent needs storage help, it… Decision needed.

### gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-tpu-dynamic-slices-monitoring`
- **Goal:** Inspect GKE TPU Dynamic Slice custom resources, explain their lifecycle state, check workload manifests target a slice correctly, and clean up stuck slices or…
- **Adds beyond the model:** Start every slice question with kubectl describe slice and read Status.Conditions against the fixed state/reason table and the three-point provisioning checkli…
- **Concerns:**
  - low value with gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring) [low-228e4a]: Delete the no-op script from the mirrored copy (or exclude it in the overlay); SKILL.md never references it. This is a mirrored skill: the… Decision needed.
  - duplicate with gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring) [dup-01b7c5]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-tpu-metrics-monitoring (third_party/google-skills/gke-tpu-metrics-monitoring)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-tpu-metrics-monitoring`
- **Goal:** Tell whether a GKE TPU workload's interruptions or slowness come from the nodes and node pools underneath it, using GKE system metrics and ready-made PromQL.
- **Adds beyond the model:** A fixed diagnostic order (confirm metric export on port 8431, runtime duty cycle and memory, node Ready condition, node-pool status and multi-host availability…
- **Concerns:**
  - duplicate with gke-tpu-metrics-monitoring (agents/platform/skills/gke-tpu-metrics-monitoring) [dup-8d741a]: Keep both as they are. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overla…

### gke-upgrades (third_party/google-skills/gke-upgrades)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-upgrades`
- **Goal:** Plan, run and troubleshoot GKE control-plane and node-pool upgrades, producing plans, checklists and runbooks tailored to the cluster.
- **Adds beyond the model:** House stance that release channels with maintenance windows and scoped exclusions are the control mechanism (never 'No channel'); surge as the default node-poo…
- **Concerns:**
  - out of date [old-da4e9e]: Use gcloud container clusters upgrade CLUSTER_NAME --node-pool NODE_POOL_NAME --zone ZONE --cluster-version PREVIOUS_VERSION. The overlay a…
  - conflicts with gke-upgrades (agents/platform/skills/gke-upgrades) [conf-cb96e1]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - duplicate with gke-upgrades (agents/platform/skills/gke-upgrades) [dup-74b14d]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-workload-identity (third_party/google-skills/gke-workload-identity)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-workload-identity`
- **Goal:** Diagnose why a Pod using Workload Identity Federation cannot authenticate to Google Cloud APIs and hand a human the exact fix.
- **Adds beyond the model:** A read-only diagnostic discipline: never modify IAM, KSAs or node pools; name one root cause and explicitly rule out the others; prefer direct principal bindin…
- **Concerns:**
  - out of date [old-5c755f]: Either add a short setup section (direct principal binding first, legacy impersonation second, with the read-only boundary relaxed to 'prop…
  - duplicate with gke-workload-identity (agents/platform/skills/gke-workload-identity) [dup-50a096]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-workload-scaling (third_party/google-skills/gke-workload-scaling)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-workload-scaling`
- **Goal:** Configure HPA and VPA for GKE workloads and right-size their resource requests.
- **Adds beyond the model:** Prefer version-controlled HPA/VPA manifests over kubectl autoscale, split metrics between HPA (CPU) and VPA (memory), and right-size by running VPA in Off mode…
- **Concerns:**
  - out of date with gke-workload-scaling (agents/platform/skills/gke-workload-scaling) [old-6cf579]: State that External metrics require the Custom Metrics Stackdriver Adapter (custom-metrics-stackdriver-adapter) deployed in the cluster, or…
  - duplicate with gke-workload-scaling (agents/platform/skills/gke-workload-scaling) [dup-3f0ff2]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

### gke-workload-security (third_party/google-skills/gke-workload-security)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-workload-security`
- **Goal:** Audit and harden workload-level security on GKE: network policies, Pod Security Standards, gVisor pods and Secret Manager CSI mounts.
- **Adds beyond the model:** Run audit_cluster.sh first, then apply a default-deny ingress-and-egress policy per namespace, label non-system namespaces restricted (or baseline) with enforc…
- **Concerns:**
  - out of date [old-48b66b]: Retitle section 2 as the legacy impersonation path, point to gke-workload-identity for direct binding, or drop the section. The overlay age…
  - out of date [old-7250e9]: Add the second command, gcloud container clusters update CLUSTER --enable-network-policy, after the addon step, and check networkConfig.dat…
  - out of date [old-c97f33]: Say that a Standard cluster needs a node pool created with --sandbox type=gvisor (see gke-platform-security) and Autopilot needs only runti…
  - conflicts with gke-workload-security (agents/platform/skills/gke-workload-security) [conf-baafb0]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - conflicts with gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security) [conf-4a9226]: Option 3. The platform copy is right: direct IAM binding on the KSA principal is the current default and GSA impersonation is legacy, as gk… Decision needed.
  - conflicts with gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security) [conf-b5e384]: Option 4. The cluster and platform copies are right (two ordered changes); only the upstream mirror is wrong. Report upstream; the overlay… Decision needed.
  - conflicts with gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security) [conf-e46fb2]: Option 3. The cluster copy is right: GKE Sandbox is a node-pool setting. Patch the platform copy (overlay) to drop the cluster-level flag;… Decision needed.
  - duplicate with gke-workload-security (agents/cluster/skills/gke-workload-security), gke-workload-security (agents/platform/skills/gke-workload-security) [dup-b3b16d]: Keep both, because the Cluster Agent needs a read-only variant, but stop hand-maintaining the cluster copy: reconcile it against the platfo… Decision needed.

### gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)

- **Source:** local  **Status:** unmanaged  **Location:** `third_party/google-skills/gke-workload-troubleshooting`
- **Goal:** Diagnose a failing GKE workload (CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending) from pod status, events and logs, and propose the fix as a GitOps chan…
- **Adds beyond the model:** Work non-interactively from prompt and environment context with a one-hour window centred on the issue time; when the cluster is unreachable, stop retrying and…
- **Concerns:**
  - out of date [old-91907e]: Use kubectl get endpointslices -l kubernetes.io/service-name={target_service_name} -n {target_namespace} in Step 4 and in the dry-run text.
  - conflicts with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [conf-f492c5]: Option 4. Keep the shipped copy as it is; the overlay already carries the correction. Report the upstream lines quoted here to google/skill… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [conf-cb2e3b]: Option 3. The cluster copy gives the better default (centre the log window on the pod's last state transition, fall back to now). Patch the… Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting), gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [conf-fad338]: Option 4. The cluster and platform copies are right (bounds inside the filter); only the upstream mirror is wrong. Report upstream. Decision needed.
  - conflicts with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [conf-e9fbf7]: Option 4. The shipped copy is right for this install (SOUL.md forbids an unrequested pull request). Keep the overlay; report upstream. Decision needed.
  - duplicate with gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) [dup-1cf49e]: Keep both. The upstream mirror is the source of truth and the shipped copy is its generated output; edit only through an overlay (edit-mirr…

## Appendix: coverage matrix

Every skill was compared with every other skill and scored by how much they
cover the same ground.

Legend: 0 = same, 1 = subset, 2 = large overlap, 3 = some overlap, 4 = related, 5 = distinct, · = not scored yet.

| Skill | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 | S22 | S23 | S24 | S25 | S26 | S27 | S28 | S29 | S30 | S31 | S32 | S33 | S34 | S35 | S36 | S37 | S38 | S39 | S40 | S41 | S42 | S43 | S44 | S45 | S46 | S47 | S48 | S49 | S50 | S51 | S52 | S53 | S54 | S55 | S56 | S57 | S58 | S59 | S60 | S61 | S62 | S63 | S64 | S65 | S66 | S67 | S68 | S69 | S70 | S71 | S72 | S73 | S74 | S75 | S76 | S77 | S78 | S79 | S80 | S81 | S82 | S83 | S84 | S85 | S86 | S87 | S88 | S89 | S90 | S91 | S92 | S93 | S94 | S95 | S96 | S97 | S98 | S99 | S100 | S101 | S102 | S103 | S104 | S105 | S106 | S107 | S108 | S109 | S110 | S111 | S112 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **S1** a2a-topics | — | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 |
| **S2** capacity-obtainability | 5 | — | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S3** cluster-agent-lifecycle | 5 | 5 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 3 |
| **S4** edit-mirrored-skill | 5 | 5 | 5 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 |
| **S5** fleet-audit | 4 | 5 | 5 | 5 | — | 4 | 4 | 3 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 |
| **S6** fleet-audit-reports | 4 | 5 | 5 | 5 | 4 | — | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S7** fleet-upgrade-verification | 4 | 5 | 5 | 5 | 4 | 4 | — | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S8** gce-compute-fleet-audit | 5 | 4 | 5 | 5 | 3 | 4 | 4 | — | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S9** gcp-config-connector | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 |
| **S10** gcp-networking-fabric-audit | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 3 | 4 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S11** github-issue-resolver | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 5 |
| **S12** gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 0 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S13** gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | — | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S14** gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | — | 0 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 3 | 3 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S15** gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | — | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 3 | 3 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S16** gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | — | 0 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S17** gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 0 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S18** gke-app-onboarding (agents/platform/skills/gke-app-onboarding) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 0 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S19** gke-app-onboarding (third_party/google-skills/gke-app-onboarding) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | — | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S20** gke-backup-dr (agents/platform/skills/gke-backup-dr) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 0 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S21** gke-backup-dr (third_party/google-skills/gke-backup-dr) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | — | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S22** gke-basics (agents/platform/skills/gke-basics) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | — | 1 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S23** gke-basics (third_party/google-skills/gke-basics) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 1 | — | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 3 | 3 | 3 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S24** gke-batch-hpc (agents/platform/skills/gke-batch-hpc) | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | — | 1 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S25** gke-batch-hpc (third_party/google-skills/gke-batch-hpc) | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 1 | — | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S26** gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler) | 5 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | — | 0 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S27** gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler) | 5 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 0 | — | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S28** gke-cluster-creation (agents/platform/skills/gke-cluster-creation) | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | — | 1 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S29** gke-cluster-creation (third_party/google-skills/gke-cluster-creation) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 1 | — | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S30** gke-compute-classes (agents/platform/skills/gke-compute-classes) | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | — | 0 | 5 | 5 | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S31** gke-compute-classes (third_party/google-skills/gke-compute-classes) | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 0 | — | 5 | 5 | 3 | 3 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S32** gke-cost-analysis (agents/platform/skills/gke-cost-analysis) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | — | 0 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S33** gke-cost-analysis (third_party/google-skills/gke-cost-analysis) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 0 | — | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S34** gke-cost-optimization (agents/platform/skills/gke-cost-optimization) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | — | 0 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 3 | 3 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S35** gke-cost-optimization (third_party/google-skills/gke-cost-optimization) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 0 | — | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 3 | 3 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S36** gke-golden-path (agents/platform/skills/gke-golden-path) | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | — | 0 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S37** gke-golden-path (third_party/google-skills/gke-golden-path) | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 0 | — | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S38** gke-inference (agents/platform/skills/gke-inference) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | — | 0 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S39** gke-inference (third_party/google-skills/gke-inference) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 0 | — | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S40** gke-manifest-generation (agents/platform/skills/gke-manifest-generation) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | — | 0 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 |
| **S41** gke-manifest-generation (third_party/google-skills/gke-manifest-generation) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 0 | — | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 3 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 |
| **S42** gke-multitenancy (agents/platform/skills/gke-multitenancy) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | — | 0 | 4 | 4 | 5 | 5 | 5 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S43** gke-multitenancy (third_party/google-skills/gke-multitenancy) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 0 | — | 4 | 4 | 5 | 5 | 5 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S44** gke-networking (agents/platform/skills/gke-networking) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | — | 1 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S45** gke-networking (third_party/google-skills/gke-networking) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 1 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S46** gke-observability (agents/cluster/skills/gke-observability) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | — | 1 | 1 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S47** gke-observability (agents/platform/skills/gke-observability) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 1 | — | 0 | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S48** gke-observability (third_party/google-skills/gke-observability) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 1 | 0 | — | 4 | 4 | 3 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S49** gke-platform-security (agents/platform/skills/gke-platform-security) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | — | 1 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 3 | 3 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S50** gke-platform-security (third_party/google-skills/gke-platform-security) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 1 | — | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S51** gke-productionize (agents/platform/skills/gke-productionize) | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | — | 0 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S52** gke-productionize (third_party/google-skills/gke-productionize) | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 0 | — | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S53** gke-reliability (agents/cluster/skills/gke-reliability) | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | — | 1 | 1 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S54** gke-reliability (agents/platform/skills/gke-reliability) | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 3 | 1 | — | 0 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S55** gke-reliability (third_party/google-skills/gke-reliability) | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 3 | 3 | 1 | 0 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S56** gke-service-networking (agents/platform/skills/gke-service-networking) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | — | 0 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S57** gke-service-networking (third_party/google-skills/gke-service-networking) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 0 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S58** gke-stall-detection | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | — | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S59** gke-stockout-investigator | 5 | 2 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | — | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 4 |
| **S60** gke-storage (agents/cluster/skills/gke-storage) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | — | 1 | 1 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S61** gke-storage (agents/platform/skills/gke-storage) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 1 | — | 0 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S62** gke-storage (third_party/google-skills/gke-storage) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 1 | 0 | — | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S63** gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | — | 0 | 3 | 3 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S64** gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 0 | — | 3 | 3 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S65** gke-tpu-metrics-monitoring (agents/platform/skills/gke-tpu-metrics-monitoring) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 3 | 3 | — | 0 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S66** gke-tpu-metrics-monitoring (third_party/google-skills/gke-tpu-metrics-monitoring) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 3 | 3 | 0 | — | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S67** gke-upgrades (agents/platform/skills/gke-upgrades) | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 1 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S68** gke-upgrades (third_party/google-skills/gke-upgrades) | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 3 | 3 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 1 | — | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 |
| **S69** gke-workload-identity (agents/platform/skills/gke-workload-identity) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | — | 1 | 5 | 5 | 5 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S70** gke-workload-identity (third_party/google-skills/gke-workload-identity) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 1 | — | 5 | 5 | 5 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S71** gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 2 | 2 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S72** gke-workload-scaling (agents/platform/skills/gke-workload-scaling) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 2 | — | 1 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S73** gke-workload-scaling (third_party/google-skills/gke-workload-scaling) | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 2 | 1 | — | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S74** gke-workload-security (agents/cluster/skills/gke-workload-security) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 3 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | — | 1 | 1 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S75** gke-workload-security (agents/platform/skills/gke-workload-security) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 5 | 1 | — | 1 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | 4 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S76** gke-workload-security (third_party/google-skills/gke-workload-security) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 5 | 1 | 1 | — | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 3 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S77** gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | — | 2 | 2 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 |
| **S78** gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 2 | — | 1 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 |
| **S79** gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 2 | 1 | — | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 |
| **S80** inspect-repository | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 3 | 5 |
| **S81** install-kube-agents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | — | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 5 |
| **S82** kube-agents-observability | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 4 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 |
| **S83** manage-cluster | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | — | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 |
| **S84** pr-conversation | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | — | 3 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 4 | 5 |
| **S85** review-address-feedback | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | — | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 |
| **S86** review-adversarial | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | — | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 |
| **S87** review-docs-drift | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | — | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 |
| **S88** review-preflight | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | — | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 |
| **S89** review-security-k8s-admission | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | — | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S90** review-security-k8s-agents-audit-logs | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S91** review-security-k8s-agents-credentials | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S92** review-security-k8s-agents-data-exfil | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | — | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S93** review-security-k8s-agents-firewall | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 3 | — | 4 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S94** review-security-k8s-agents-main | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | — | 3 | 3 | 4 | 1 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S95** review-security-k8s-agents-prompt-injection | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S96** review-security-k8s-agents-sandbox | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 3 | 4 | — | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S97** review-security-k8s-gateway | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S98** review-security-k8s-main | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 1 | 4 | 4 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S99** review-security-k8s-namespaces | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S100** review-security-k8s-network | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 2 | 4 | 4 | 4 | 3 | 4 | 4 | — | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S101** review-security-k8s-nodes | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S102** review-security-k8s-pod | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | — | 4 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S103** review-security-k8s-rbac | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | — | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S104** review-security-k8s-service-accounts | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | — | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S105** review-security-k8s-storage | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| **S106** review-security-k8s-understand | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | — | 5 | 5 | 5 | 5 | 5 | 5 |
| **S107** skill-review | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 5 | 5 | 5 | 5 | 5 |
| **S108** submit-suggestion | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 5 | 5 | 3 | 4 |
| **S109** uninstall-kube-agents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | — | 3 | 5 | 5 |
| **S110** upgrade-kube-agents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | — | 5 | 5 |
| **S111** version-control | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | — | 5 |
| **S112** workload-rebalancing | 4 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | — |

Coverage summaries:

- **S1 a2a-topics**: Platform Agent skill (shipped only on a `next`-mode install with the A2A bus) for the `a2a topics list|read|write` CLI: discover provisioned topics and their class (state vs journal), read standing state such as `upgrade-readiness` while relaying provenance and treating exit 2 as 'empty', write topics the profile owns with `--text`/`--data` and task/context/correlation ids, and append dated findings to the shared `annotations` journal. Read and write, fleet-level shared state. It explicitly excludes task status (stream replay), private memory, scratch notes, topics not in `a2a topics list`, and installs without `NATS_URL` or where the shell sandbox has no `a2a` binary.
- **S2 capacity-obtainability**: Platform Agent, read-only diagnosis and design, project and region scope rather than one cluster. Checks regional quota (gcloud compute regions describe), reservations, live node and pod usage (kubectl top), Spot and Flex-Start obtainability (gcloud beta compute advice capacity, capacity-history) across zones, and future reservation windows for deadline-bound TPU or VM batch jobs (gcloud beta compute advice calendar-mode); records each check with record_evidence (or an Evidence section when the tool is absent), attaches ComputeClass, NAP, ProvisioningRequest and Kueue LocalQueue manifests with attach_artifact, requires a three-path On-Demand/Spot/Flex-Start report, and lists eight ComputeClass resilience rules (fallbacks, large shapes, disk generation mix, On-Demand floor, regional scarcity, quota exceeded, priority starvation, Hyperdisk compatibility). It explicitly excludes creating clusters, applying manifests, opening PRs and handling inbound stockout alerts, which it sends to the gke-stockout-investigator plugin skill.
- **S3 cluster-agent-lifecycle**: Lets the Platform Agent create, delegate to, and delete per-cluster Cluster Agent Hermes profiles: it scaffolds a profile with `cluster_agent_profile.py create` at cluster onboarding, deletes it with `delete` at teardown, resolves the profile name with the `get_cluster_profile_name`/`list_cluster_profiles` tools, dispatches single-cluster runtime diagnostics as kanban cards assigned to that profile (one card per cluster with no `parents` for fan-out, polled with `kanban_show`), reads the RCA from the card's `result`/`metadata`, and opens any resulting PR itself via `submit-suggestion`. It also documents the hourly `cluster_agent_reconcile.py` cron (create for every in-scope cluster, prune on definitive NotFound/exclusion/project-left-scope over two clean runs, `fleet_scope.json`, `--require-create-pass` exit codes 3/4, `--dry-run`). It does not cover cluster provisioning or deletion (`gke-cluster-creation`), scope exclusion mechanics (`manage-cluster`), the Cluster Agent's own debugging procedures, or GitOps PR authoring (`submit-suggestion`).
- **S4 edit-mirrored-skill**: Lets a repo contributor (not a runtime agent) maintain the three-layer mirrored gke-* skills: the upstream copy in third_party/google-skills/<skill>/, the overlay in agents/platform/skill-overlays/<skill>/ (numbered .patch files with Why/Local-Issue/Retire-When/Upstream-Issue headers, append.md, upstream.lock), and the shipped skill in agents/platform/skills/<skill>/. It covers recording a local edit as a patch or folding it into an existing one (make skills-refresh SKILL= MSG=/PATCH=), adding a '<!-- kube-agents: local addition' appended section, removing a patch and rebuilding (make skills-generate), syncing to a newer google/skills commit and resolving CONFLICT: stops in .skill-sync/ (make skills-status, skills-sync REF=, skills-continue), adopting or importing an upstream gke-* skill (skills-sync, skills-import, SKILL_GROUPS in scripts/generate_docs.py, make docs-generate), diagnosing each make skills-check failure, plus the surrounding rules: shellcheck on shipped scripts, deploy/docker/check_skill_commands.py KNOWN_FINDINGS, and the eval loop for any change the agent reads. It does not cover writing or editing non-mirrored skills, stopping mirroring (left to a maintainer), editing third_party/ or upstream.lock by hand, or any cluster/GKE operation.
- **S5 fleet-audit**: Lets the Platform Agent run one of nine registered fleet-audit streams (security/RBAC compliance, upgrade and patch readiness, workload reliability, fleet waste, consistency drift, AI workload security, stockout prevention, GCP networking fabric, GCE compute) end to end: `audit_report.py start` claims the stream and a per-audit workspace, the agent inspects clusters read-only per the stream's governance SOP (usually by running a bundled deterministic collector: collect.py, fleet_drift.py, patch_readiness.py, fleet_waste.py, fleet_stockout.py), writes a schema-validated findings.json with per-check commands, and `audit_report.py finish` publishes exactly one rewritten ledger issue per stream on the GitOps forge, computes the run-over-run delta, auto-promotes up to five critical manifest fixes into narrow remediation pull requests (merge requests on GitLab), answers `/remediate` comments, and handles declared-intent context repositories, partial coverage, held and clean closes, `silent_ok`, and no-forge installs. It also says how to trigger a scheduled stream (`hermes cron run`) instead of re-enacting it, and ships `report_status.py` for the report store's read side. It does not define the checks themselves (those live in governance/*_sop.md), does not answer questions about past runs (fleet-audit-reports), never mutates a cluster or hand-writes an issue or PR, and does not cover the upgrade-retrospective review even though its collector (upgrade_retrospective.py) sits in this scripts folder.
- **S6 fleet-audit-reports**: Lets the Platform Agent answer questions about past autonomous fleet-audit runs (what a stream last found, open criticals, what changed between two runs, which clusters were skipped or partly covered, when each stream last ran, whether one is running or died) from the on-pod report store at /opt/data/fleet-audit/reports, exclusively through the bundled bounded query CLI report_query.py (subcommands streams, show, findings, finding, checks, diff, runs) which imports the sibling fleet-audit skill's report_status.py helpers. It explicitly does not run, publish or remediate an audit, does not touch a stream's lease, does not read the live GitHub ledger issue, and forbids opening latest.json or ring entries with file tools or shell (cat, head, grep, jq).
- **S7 fleet-upgrade-verification**: Lets the Platform Agent run two read-only scripts. `fleet_upgrade_report.py` lists every GKE cluster's control-plane and lowest node-pool version against a `--target-version` or each cluster's release-channel default, grades members lagging/patch-behind/current/ahead/unknown, records each run so a later run shows started/completed/stalled progress, and with `--readiness` grades each member blocked/ready/unknown on drain-blocking PodDisruptionBudgets, fail-closed admission webhooks with unreachable backends on the node-upgrade or bootstrap-RBAC path, maintenance exclusions and windows, and node-pool version skew. `api_deprecation_scan.py` scans the managed GitOps repositories' manifests for apiVersions removed between the fleet's lowest control-plane minor and the target (table through Kubernetes 1.32). It does not plan or run upgrades (gke-upgrades does), does not detect configuration drift (fleet-audit does), does not read live deprecated-API client usage (GKE Deprecation Insights does), does not render Helm or Kustomize, and cites no CVEs.
- **S8 gce-compute-fleet-audit**: Lets the Platform Agent audit non-GKE Compute Engine resources across every project in the install's declared scope (from the platform_control `fleet_scope` tool) with one collector, `scripts/compute_fleet_audit.py`, which runs `gcloud compute` reads (instances list, project-info describe, instances get-serial-port-output, instance-groups managed list, sole-tenancy node-groups list/list-nodes, snapshots list, disks list) and writes a collector manifest for the `fleet-audit` harness's `audit_report.py start`/`finish --manifest-file`. It covers exactly four roster checks from `agents/platform/governance/gce_compute_fleet_sop.md`: startup-script failures in the serial console (`gce-startup-script-status`), MIG resize loops (`mig-convergence-stalled`), sole-tenant node groups at 90% vCPU/memory with no spare host (`sole-tenant-headroom`), and snapshots older than 90 days whose source disk is gone and that no schedule took (`orphaned-snapshots`). It does not audit Ops Agent guest telemetry (`ops-agent-guest-health`, rejected by `finish`), GKE clusters or node pools, networking, cost, or any write/remediation action; exclusions such as GKE-node, pod-driven-scale, legal-hold and maintenance-window are left to the model's triage of each candidate rather than applied by the collector.
- **S9 gcp-config-connector**: Platform Agent skill that authors Config Connector (KCC) v1beta1 manifests for Google Cloud resource changes and submits them as a pull request through submit-suggestion (prepare and submit on branch platform-agent/kcc-<kind>-<name>) under clusters/<cluster>/provisioning/. It covers ContainerCluster and ContainerNodePool changes (grow, autoscale, release channel, adopt), SQLInstance changes (read replica, tier, backups), and ComputeFirewall rules, with a read-only create/acquire/edit decision from kubectl get, kubectl auth can-i and gcloud describe, mandatory deletion-policy: abandon and state-into-spec: absent annotations, immutable-field catalogues per kind in references/, and validation with kubectl explain. GitOps-write via PR only; never applies. It explicitly excludes Kubernetes workload manifests (gke-manifest-generation), imperative cluster creation (gke-cluster-creation), Terraform HCL repositories, kinds outside the catalogued families, fixing fleet-audit findings, kubectl apply/create/patch/delete/diff and server dry-run, and proposing to install or enable Config Connector.
- **S10 gcp-networking-fabric-audit**: Lets the Platform Agent run the collector `scripts/networking_audit.py` (gcloud reads: `compute networks/subnets/routers/forwarding-rules/firewall-rules/security-policies/backend-services/instances/addresses list`, `routers get-status`/`get-nat-mapping-info`, `container clusters list`) over the project scope the platform_control `fleet_scope` tool returns, producing a run manifest for six checks: `subnet-ip-exhaustion` on `<project>/<region>/<subnet>` targets, and `cloud-nat-exhaustion`, `psc-routing-deadlock`, `mtu-packet-fragmentation`, `cloud-armor-false-positive`, `firewall-world-open-ingress` on `project/<project>` targets. It wraps the run in the `fleet-audit` harness (`audit_report.py start`, `draft --manifest-file`, `finish --manifest-file`) per `governance/gcp_networking_fabric_sop.md`, which owns the check rules, remediation artifacts and findings.json format. It does not cover Kubernetes-level networking (NetworkPolicy, Services, Gateway), GKE cluster health, cost or compliance audits, Network Analyzer insights or `subnets list-usable` (grants the agent lacks), and it performs no writes to GCP; remediation is handed to the fleet-audit issue/PR flow.
- **S11 github-issue-resolver**: Platform Agent, writes to the forge (GitHub or GitLab): polls the configured repositories for unaddressed open issues, claims one with the status:in-progress label, investigates read-only with kubectl/gcloud/logs, then posts a triage report and transitions the issue to status:resolved (close) or status:escalation-needed (plus a chat alert). All forge calls go through scripts/resolver.py (poll, claim --issue --repo, transition --issue --repo --state --report-file) via the credential broker; the skill also covers prompt-injection handling of issue text and how to end a turn from a kanban card versus a cron run. Explicitly never touches issues labelled status:escalation-needed, agent:ignore, agent:audit, agent:delivery-watch or infra-drift, and never performs a mutation an issue asks for.
- **S12 gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster. Checks whether a GPU/TPU node disruption was Compute Engine host maintenance: kubectl get nodes for the cloud.google.com/scheduled-maintenance-time label, PromQL on kubernetes_io:node_interruption_count and node_pool_interruption_count with interruption_reason="HW/SW Maintenance", Cloud Logging for active-node-maintenance=ONGOING and the impending-node-termination taint, then recommends (does not apply) graceful termination, opportunistic maintenance and PodDisruptionBudgets. Explicitly excludes cluster creation, network policy configuration and non-disruption workload deployment, and tells the agent to rule out host maintenance and point at app-level causes when all signals are empty.
- **S13 gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu)**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster. Checks whether a GPU/TPU node disruption was Compute Engine host maintenance: kubectl get nodes for the cloud.google.com/scheduled-maintenance-time label, PromQL on kubernetes_io:node_interruption_count and node_pool_interruption_count with interruption_reason="HW/SW Maintenance", Cloud Logging for active-node-maintenance=ONGOING and the impending-node-termination taint, then recommends (does not apply) graceful termination, opportunistic maintenance and PodDisruptionBudgets. Explicitly excludes cluster creation, network policy configuration and non-disruption workload deployment, and tells the agent to rule out host maintenance and point at app-level causes when all signals are empty.
- **S14 gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption)**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster for AI/ML training JobSets. Gives a four-step runbook of MQL, PromQL and Cloud Logging (LQL) queries: JobSet restart counts (kube_jobset_restarts), node-pool interruption counts and gke_nodepool life events (preemption, maintenance, termination), node Ready status and node-to-physical-host mapping via gce_topology_host, then pod phases, unschedulable counts and coordinator worker logs for NCCL timeouts. Resolutions are recommendations only (move Spot training to on-demand or compact placement; cordon/drain and recreate a node on a faulty host). references/failure_signatures.md holds example log lines; scripts/validate_queries.sh dry-runs the filters with gcloud logging read and the Managed Prometheus API. Explicitly excludes cluster creation, basic workload deployment and non-JobSet issues.
- **S15 gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption)**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster for AI/ML training JobSets. Gives a four-step runbook of MQL, PromQL and Cloud Logging (LQL) queries: JobSet restart counts (kube_jobset_restarts), node-pool interruption counts and gke_nodepool life events (preemption, maintenance, termination), node Ready status and node-to-physical-host mapping via gce_topology_host, then pod phases, unschedulable counts and coordinator worker logs for NCCL timeouts. Resolutions are recommendations only (move Spot training to on-demand or compact placement; cordon/drain and recreate a node on a faulty host). references/failure_signatures.md holds example log lines; scripts/validate_queries.sh dry-runs the filters with gcloud logging read and the Managed Prometheus API. Explicitly excludes cluster creation, basic workload deployment and non-JobSet issues.
- **S16 gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom)**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster, narrowed to TPU v6e nodes. Three Cloud Logging filter templates (used through a query_logs tool): serial-console OOM kills of vbar_control_agent, tpu-device-plugin 'checksum didn't match' metric fetch errors, and signs of custom libtpu.sdk.tpumonitoring polling, plus a kubectl get pods -A image listing. Resolutions are recommendations only: disable the custom metrics collector, and upgrade GKE when the resilient agent ships. references/failure_signatures.md holds example log lines; scripts/validate_queries.sh dry-runs two filters with gcloud logging read. Explicitly excludes non-TPU container OOMs and standard node lifecycle operations.
- **S17 gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom)**: Upstream google/skills copy under the Platform Agent; read-only diagnosis on one GKE cluster, narrowed to TPU v6e nodes. Three Cloud Logging filter templates (used through a query_logs tool): serial-console OOM kills of vbar_control_agent, tpu-device-plugin 'checksum didn't match' metric fetch errors, and signs of custom libtpu.sdk.tpumonitoring polling, plus a kubectl get pods -A image listing. Resolutions are recommendations only: disable the custom metrics collector, and upgrade GKE when the resilient agent ships. references/failure_signatures.md holds example log lines; scripts/validate_queries.sh dry-runs two filters with gcloud logging read. Explicitly excludes non-TPU container OOMs and standard node lifecycle operations.
- **S18 gke-app-onboarding (agents/platform/skills/gke-app-onboarding)**: Upstream google/skills copy under the Platform Agent; a write path for one cluster. Covers first-time onboarding of an application to GKE: assess the app, write a Dockerfile (or use Cloud Native Buildpacks), build and push to Artifact Registry (gcloud auth configure-docker, docker build/push, gcloud artifacts docker images describe --show-package-vulnerability), generate a Deployment plus ClusterIP Service manifest with probes and resource limits, then deploy with the GKE MCP tools apply_k8s_manifest / get_k8s_rollout_status / get_k8s_resource or kubectl apply as fallback. assets/ holds a sample Node.js app (Dockerfile, index.js, package.json) and a hardened deployment.yaml that SKILL.md itself does not reference. Explicitly excludes general cluster administration and upgrades, pointing to gke-basics and gke-upgrades, and defers autoscaling, observability, security and reliability to other gke-* skills.
- **S19 gke-app-onboarding (third_party/google-skills/gke-app-onboarding)**: Upstream google/skills copy under the Platform Agent; a write path for one cluster. Covers first-time onboarding of an application to GKE: assess the app, write a Dockerfile (or use Cloud Native Buildpacks), build and push to Artifact Registry (gcloud auth configure-docker, docker build/push, gcloud artifacts docker images describe --show-package-vulnerability), generate a Deployment plus ClusterIP Service manifest with probes and resource limits, then deploy with the GKE MCP tools apply_k8s_manifest / get_k8s_rollout_status / get_k8s_resource or kubectl apply as fallback. assets/ holds a sample Node.js app (Dockerfile, index.js, package.json) and a hardened deployment.yaml that SKILL.md itself does not reference. Explicitly excludes general cluster administration and upgrades, pointing to gke-basics and gke-upgrades, and defers autoscaling, observability, security and reliability to other gke-* skills.
- **S20 gke-backup-dr (agents/platform/skills/gke-backup-dr)**: Platform Agent skill for Backup for GKE. It gives the gcloud beta container backup-restore commands to enable the BackupRestore addon, create backup plans (with --include-volume-data, --include-secrets, retention, cron or RPO schedules, CMEK), trigger manual backups, create restore plans and run and verify restores. It is a write skill on one GKE cluster at a time, with restore-safety rules on conflict policies and a rule to confirm before restoring into production. It explicitly does not cover database backups and does not cover the broader Google Cloud Backup and DR service.
- **S21 gke-backup-dr (third_party/google-skills/gke-backup-dr)**: Gives the gcloud command sequence for Backup for GKE: enable the BackupRestore addon with `gcloud container clusters update --update-addons=BackupRestore=ENABLED`, then `gcloud beta container backup-restore` to create BackupPlan resources (`--include-volume-data`, `--include-secrets`, `--backup-retain-days`, `--cron-schedule` or `--target-rpo-minutes`, `--encryption-key` for CMEK), trigger manual backups, create RestorePlan resources with conflict policies (`--cluster-resource-conflict-policy`, `--namespaced-resource-restore-mode`), execute restores, and describe restore status. It covers restore safety rules (safe defaults, confirm before restoring into production, do not poll for the addon to activate), golden-path defaults (volumes and secrets included, 30-day retention, CMEK), and notes on cross-project backup, namespace-based pricing, RPO scheduling, and Hyperdisk support. It explicitly excludes database backups, and does not cover Terraform or Kubernetes-manifest expression of plans, GKE Backup IAM, or the Google Cloud Backup and DR Service beyond naming it as distinct.
- **S22 gke-basics (agents/platform/skills/gke-basics)**: The skill lets an agent choose Autopilot versus Standard (Standard only for custom sysctls, custom taints or hardware node pools, or hostPath DaemonSets), create a private Autopilot cluster with `gcloud container clusters create-auto` and the private-nodes, private-endpoint and master-authorized-networks flags, round Autopilot CPU requests to 250m increments, and run `gcloud container clusters get-credentials` with `--location` into a per-target `KUBECONFIG` under `$HERMES_HOME/.kubeconfigs/`. Its references cover a tool-preference hierarchy (Developer Knowledge MCP `search_documents`/`get_documents` then web search for facts; GKE MCP tools then gcloud then kubectl for live operations), a table mapping each cluster, node pool, Kubernetes resource, diagnostics and operations action to a GKE MCP tool and its gcloud/kubectl fallback, `gcloud container ai profiles` for GIQ inference manifests, Kubernetes client-library snippets (Python, Go, Node.js, Java), a Terraform `google_container_cluster` Autopilot example, and a short error-to-remediation table. It explicitly routes away Workload Identity (gke-workload-identity), networking (gke-networking), security hardening (gke-platform-security, gke-workload-security), upgrades and maintenance windows (gke-upgrades), manifest authoring (gke-manifest-generation) and detailed node-pool planning (gke-cluster-creation).
- **S23 gke-basics (third_party/google-skills/gke-basics)**: The skill lets an agent provision and operate GKE clusters at the entry level: it defaults to Autopilot and names the three cases that force Standard (custom sysctls, custom taints or hardware node pools, hostPath DaemonSets), gives the private-cluster create-auto flags (--enable-private-nodes, --enable-private-endpoint, --master-authorized-networks), Autopilot resource-request rounding (250m CPU increments, requests equal limits), and the get-credentials command with an explicit --region/--zone. Its references map every cluster, node-pool, Kubernetes-resource, diagnostics and operations task to a GKE MCP tool (list/get/create/update_cluster, list/get/create/update_node_pool, get/describe/apply/patch/delete_k8s_resource, list_k8s_events, get_k8s_logs, get_k8s_rollout_status, check_k8s_auth, list/get/cancel_operation) with its gcloud or kubectl fallback and a READ/MUTATE/DESTRUCTIVE label, list kubectl-only operations (top, scale, exec, port-forward, cp, drain, helm), the GIQ `gcloud container ai profiles` commands, a Developer Knowledge MCP section (search_documents, get_documents; never answer_query), Terraform `google_container_cluster` (Autopilot) and `kubernetes_deployment_v1` examples, Python/Go/Node client-library snippets, and an error-to-remediation table. It explicitly routes away from Workload Identity (gke-workload-identity), networking (gke-networking), security flags (gke-platform-security, gke-workload-security), upgrades and maintenance windows (gke-upgrades), manifest generation (gke-manifest-generation) and advanced node-pool planning (gke-cluster-creation); it is the upstream copy at google/skills commit 9ad3d2b (upstream's latest), and the harness overlay changes only the kubeconfig isolation and Developer-Knowledge ranking, so its mutating MCP tool guidance does not reflect that the install offers the gke MCP server's read tools only.
- **S24 gke-batch-hpc (agents/platform/skills/gke-batch-hpc)**: Platform Agent skill for running batch and HPC work on GKE. It gives manifests for Kubernetes Jobs, JobSet, Kueue ClusterQueue and LocalQueue, and Kubeflow MPIJob, the kubectl install lines for Kueue and the MPI Operator, a gcloud node-pools create command for compact placement on Standard clusters, and cost rules (Spot via ComputeClass, scale-to-zero, backoffLimit, checkpointing, maintenance exclusions). It writes workloads into a single cluster. A local footer requires loading capacity-obtainability before scheduling GPU/TPU jobs with a deadline. It explicitly excludes standard web application deployments (gke-app-onboarding) and defers Spot-fallback YAML to gke-compute-classes.
- **S25 gke-batch-hpc (third_party/google-skills/gke-batch-hpc)**: Lets an agent set up batch and HPC workloads on GKE using the gke MCP tools (apply_k8s_manifest, get_k8s_resource, describe_k8s_resource, get_k8s_logs, delete_k8s_resource, list_k8s_events): it gives manifests for a batch/v1 Job (parallelism, completions, backoffLimit), a jobset.x-k8s.io JobSet, Kueue ClusterQueue and LocalQueue with the Kueue install command, a `gcloud container node-pools create --placement-type COMPACT` node pool for low-latency HPC, and a Kubeflow MPIJob with the MPI Operator install command, plus cost advice (Spot VMs via a ComputeClass, scale-to-zero with `--min-nodes 0` or Autopilot) and best practices (resource requests and limits, maintenance exclusions for long TPU/Spot training, checkpointing). The kube-agents overlay adds one rule: before scheduling a GPU/TPU or large-shape batch job with a deadline, run the capacity-obtainability skill's Future windows section. It does not cover standard web application deployments (deferred to gke-app-onboarding), the Spot-with-fallback ComputeClass pattern itself (deferred to gke-compute-classes), the capacity probe and ProvisioningRequest shapes (deferred to capacity-obtainability), GPU/TPU driver or accelerator node-pool setup, debugging a failing job, or any GitOps or fleet-level write.
- **S26 gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler)**: Platform Agent skill for the GKE Cluster Autoscaler, Node Auto Provisioning and node pool auto-creation. It covers enabling autoscaling (gcloud node-pools and clusters update flags), tuning (autoscaling profiles, location policy, consolidation delay), reading cluster-autoscaler-visibility logs, and diagnosing scale-up failures (stockouts, quota, IP exhaustion, cooldown cascade) and scale-down blockers, with two scripts (log-autoscaler-events.sh tails Cloud Logging; find-scale-down-blockers.sh scans pods, PDBs and nodes with kubectl) and a CapacityBuffer example. It mixes read-only diagnosis with cluster-level write commands on a single cluster. It explicitly defers ComputeClass YAML, schemas and priority configuration to gke-compute-classes.
- **S27 gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler)**: Lets an agent enable node autoscaling on GKE (per-pool `gcloud container node-pools ... --enable-autoscaling`, cluster-wide `--enable-autoprovisioning`, or per-ComputeClass `nodePoolAutoCreation.enabled`), tune it (`--autoscaling-profile=optimize-utilization`, ComputeClass `autoscalingPolicy` consolidation delay/threshold, `locationPolicy` BALANCED/ANY, Spot `shutdownGracePeriodSeconds`, CUD vs reservation consumption, CapacityBuffer CRD pre-warming with a sample manifest), and troubleshoot scale-up stalls (stockout, quota, IP exhaustion, zonal stockout cooldown cascade) and scale-down blockers (bare pods, safe-to-evict, local storage, PDBs, min-nodes floor, node annotations, hostname pins, non-DaemonSet kube-system pods). Ships two scripts: `log-autoscaler-events.sh` tails `container.googleapis.com/cluster-autoscaler-visibility` Cloud Logging entries via `gcloud logging read`, and `find-scale-down-blockers.sh` scans the current kube context with kubectl+jq. Explicitly does not cover ComputeClass YAML generation, schemas, or priority/fallback configuration (deferred to the `gke-compute-classes` skill), and does not cover pod-level autoscaling (HPA/VPA).
- **S28 gke-cluster-creation (agents/platform/skills/gke-cluster-creation)**: Platform Agent provisioning skill that creates GKE clusters from five templates (golden-path Autopilot, Autopilot dev/test, Standard regional, L4 GPU inference, A3 Hypercompute), each as a gcloud command and a create_cluster MCP payload, with a workflow (discover, gather inputs, choose mode, confirm, create, track with get_operation, verify with get_cluster) and rules to warn about Standard mode, Day-0 choices, cost and quota. Local footers require creating the Cluster Agent profile (python3 /opt/data/scripts/cluster_agent_profile.py create) right after creation, deleting it at teardown, and loading capacity-obtainability before recommending GPU/TPU capacity. It is a write skill at project scope. It explicitly excludes application onboarding and deployment configuration (gke-app-onboarding).
- **S29 gke-cluster-creation (third_party/google-skills/gke-cluster-creation)**: Lets an agent plan and run GKE cluster creation with the gke MCP tools (list_clusters, create_cluster, get_cluster, list_operations, get_operation) or gcloud, from five ready templates: golden-path Autopilot (private nodes, authorized networks, Secret Manager CSI, REGULAR channel, full monitoring), Autopilot dev/test, Standard regional (e2-standard-4, Shielded nodes, Workload Identity, Dataplane V2), GPU inference (Autopilot ComputeClass or g2-standard-4/nvidia-l4 pool, with a GIQ `gcloud container ai profiles manifests create` example), and A3 HighGPU hypercompute. It covers the workflow (discover project, gather project/location/name, explain Autopilot-vs-Standard and cost/availability trade-offs, present the config for confirmation, create, track the operation, verify with get_cluster readMask=*), a mode-selection table, and best-practice rules on private clusters, VPC-native, Workload Identity, Shielded nodes, autoscaling, Spot, regional control planes and release channels, with mandatory warnings on Day-0 networking choices and GPU quota/cost. It explicitly does not cover application onboarding or deployment configuration (deferred to gke-app-onboarding), and the upstream text has no post-creation steps such as node pool management, upgrades, or Cluster Agent profile provisioning (the kube-agents overlay appends the latter).
- **S30 gke-compute-classes (agents/platform/skills/gke-compute-classes)**: Platform Agent skill for authoring, tuning and debugging GKE ComputeClass objects: priorities with Spot, reservation, DWS FlexStart and On-Demand fallbacks, GPU and TPU targeting, machine families, location policy, activeMigration and consolidation, the dynamic-rwo StorageClass for stateful PVs, Autopilot mode on Standard clusters, Karpenter migration, and access control via RBAC plus a ValidatingAdmissionPolicy. It ships fifteen example YAML assets (labelled EXAMPLE TEMPLATE - DO NOT DEPLOY), ten reference files and a copy of log-autoscaler-events.sh identical to the one in gke-cluster-autoscaler. It writes cluster-scoped CRDs on a single cluster. It explicitly excludes cluster-level Node Auto Provisioning configuration and general cluster creation.
- **S31 gke-compute-classes (third_party/google-skills/gke-compute-classes)**: Platform Agent skill for authoring, tuning and debugging GKE ComputeClass objects: priorities with Spot, reservation, DWS FlexStart and On-Demand fallbacks, GPU and TPU targeting, machine families, location policy, activeMigration and consolidation, the dynamic-rwo StorageClass for stateful PVs, Autopilot mode on Standard clusters, Karpenter migration, and access control via RBAC plus a ValidatingAdmissionPolicy. It ships fifteen example YAML assets (labelled EXAMPLE TEMPLATE - DO NOT DEPLOY), ten reference files and a copy of log-autoscaler-events.sh identical to the one in gke-cluster-autoscaler. It writes cluster-scoped CRDs on a single cluster. It explicitly excludes cluster-level Node Auto Provisioning configuration and general cluster creation.
- **S32 gke-cost-analysis (agents/platform/skills/gke-cost-analysis)**: Platform Agent skill (agents/platform/skills, upstream google/skills copy) for answering GKE cost questions. It covers BigQuery billing-export queries with `bq query` (per-workload, per-cluster, per-namespace cost, net vs gross credits), checking that GKE Cost Allocation is enabled, `gcloud billing budgets list`, and live `kubectl top nodes/pods` to compare usage with requests; it explains Autopilot (per-pod-request) vs Standard (per-VM plus management fee) pricing. Scope spans projects and clusters (fleet-wide billing data) and is read-only apart from one `gcloud container clusters update --enable-cost-allocation` snippet; it explicitly excludes applying optimizations, VPA/MPA rightsizing manifests, and ComputeClass selection (deferred to gke-cost-optimization).
- **S33 gke-cost-analysis (third_party/google-skills/gke-cost-analysis)**: Platform Agent skill (agents/platform/skills, upstream google/skills copy) for answering GKE cost questions. It covers BigQuery billing-export queries with `bq query` (per-workload, per-cluster, per-namespace cost, net vs gross credits), checking that GKE Cost Allocation is enabled, `gcloud billing budgets list`, and live `kubectl top nodes/pods` to compare usage with requests; it explains Autopilot (per-pod-request) vs Standard (per-VM plus management fee) pricing. Scope spans projects and clusters (fleet-wide billing data) and is read-only apart from one `gcloud container clusters update --enable-cost-allocation` snippet; it explicitly excludes applying optimizations, VPA/MPA rightsizing manifests, and ComputeClass selection (deferred to gke-cost-optimization).
- **S34 gke-cost-optimization (agents/platform/skills/gke-cost-optimization)**: Platform Agent skill (upstream google/skills copy) for reducing GKE cost once waste is known. It covers ResourceQuota manifests, VPA in recommendation mode (`updateMode: Off`) with a P95*1.2 rightsizing rule and MPA, Spot VMs via a `ComputeClass` with fallback or the Autopilot `cloud.google.com/gke-provisioning: Spot` nodeSelector, a machine-family cost table, Committed Use Discounts, stopping idle dev clusters, and dev/test deviations from the golden path. Write-oriented (its examples use `kubectl apply`, which this install routes through the GitOps PR path), single cluster or namespace at a time; it explicitly excludes general ComputeClass provisioning and GPU selection (gke-compute-classes) and billing analysis (gke-cost-analysis).
- **S35 gke-cost-optimization (third_party/google-skills/gke-cost-optimization)**: Platform Agent skill (upstream google/skills copy) for reducing GKE cost once waste is known. It covers ResourceQuota manifests, VPA in recommendation mode (`updateMode: Off`) with a P95*1.2 rightsizing rule and MPA, Spot VMs via a `ComputeClass` with fallback or the Autopilot `cloud.google.com/gke-provisioning: Spot` nodeSelector, a machine-family cost table, Committed Use Discounts, stopping idle dev clusters, and dev/test deviations from the golden path. Write-oriented (its examples use `kubectl apply`, which this install routes through the GitOps PR path), single cluster or namespace at a time; it explicitly excludes general ComputeClass provisioning and GPU selection (gke-compute-classes) and billing analysis (gke-cost-analysis).
- **S36 gke-golden-path (agents/platform/skills/gke-golden-path)**: Platform Agent skill (upstream google/skills copy) holding the recommended Autopilot cluster configuration. It lists always-apply defaults (private nodes, Workload Identity, ADVANCED_DATAPATH, Cloud DNS, OPTIMIZE_UTILIZATION, VPA, monitoring/logging components, Secret Manager rotation), customer-configurable settings (DNS endpoint, IPAM, maxPodsPerNode, boot disk, maintenance exclusions), Day-0 vs Day-1 rules, guardrails for auditing an existing cluster against the baseline, and a condensed `assets/golden-path-autopilot.yaml`. It names the `get_cluster`/`create_cluster`/`update_cluster` MCP tools and is a design and audit reference for one cluster at a time; it explicitly excludes workload autoscaling (gke-workload-scaling).
- **S37 gke-golden-path (third_party/google-skills/gke-golden-path)**: Platform Agent skill (upstream google/skills copy) holding the recommended Autopilot cluster configuration. It lists always-apply defaults (private nodes, Workload Identity, ADVANCED_DATAPATH, Cloud DNS, OPTIMIZE_UTILIZATION, VPA, monitoring/logging components, Secret Manager rotation), customer-configurable settings (DNS endpoint, IPAM, maxPodsPerNode, boot disk, maintenance exclusions), Day-0 vs Day-1 rules, guardrails for auditing an existing cluster against the baseline, and a condensed `assets/golden-path-autopilot.yaml`. It names the `get_cluster`/`create_cluster`/`update_cluster` MCP tools and is a design and audit reference for one cluster at a time; it explicitly excludes workload autoscaling (gke-workload-scaling).
- **S38 gke-inference (agents/platform/skills/gke-inference)**: Platform Agent skill (upstream google/skills copy) for serving AI/ML models on GKE. It covers the GKE Inference Quickstart CLI (`gcloud container ai profiles models list`, `profiles list --model`, `profiles manifests create` with `--model-server`, `--accelerator-type`, `--target-ntpot-milliseconds`), reviewing and deploying the generated manifest with `kubectl apply`, a GPU `ComputeClass` for Autopilot, an accelerator selection table (T4 through GB200 and TPU v5e-v7x), an HPA on GPU metrics, vLLM tuning tips, and a troubleshooting table. Single-cluster, write-oriented deployment guidance; it explicitly excludes generic batch and HPC work (gke-batch-hpc).
- **S39 gke-inference (third_party/google-skills/gke-inference)**: Platform Agent skill (upstream google/skills copy) for serving AI/ML models on GKE. It covers the GKE Inference Quickstart CLI (`gcloud container ai profiles models list`, `profiles list --model`, `profiles manifests create` with `--model-server`, `--accelerator-type`, `--target-ntpot-milliseconds`), reviewing and deploying the generated manifest with `kubectl apply`, a GPU `ComputeClass` for Autopilot, an accelerator selection table (T4 through GB200 and TPU v5e-v7x), an HPA on GPU metrics, vLLM tuning tips, and a troubleshooting table. Single-cluster, write-oriented deployment guidance; it explicitly excludes generic batch and HPC work (gke-batch-hpc).
- **S40 gke-manifest-generation (agents/platform/skills/gke-manifest-generation)**: Platform Agent skill (upstream google/skills copy with repo-specific substitutions) for writing or editing Kubernetes YAML for GKE Autopilot and Standard. It mandates explicit namespaces, dedicated ServiceAccounts, requests/limits, Spot nodeSelector plus toleration for non-prod, Pod Security Standards hardening, liveness/readiness/startup probes, ClusterIP and Gateway API over Ingress, subPath and StorageClass rules, anti-affinity and PDBs, and stable list keys for server-side apply; references hold full examples for a hardened Nginx Deployment, NetworkPolicy, a vLLM GPU workload with GCS FUSE, and Gateway/HTTPRoute. It directs inference manifests to `gcloud container ai profiles manifests create` on stdout and grounding lookups to `search_documents`/`get_documents`; it is authoring-only (no cluster operations) and explicitly excludes troubleshooting (gke-workload-troubleshooting), cluster provisioning (gke-cluster-creation), and Config Connector manifests (gcp-config-connector).
- **S41 gke-manifest-generation (third_party/google-skills/gke-manifest-generation)**: The skill lets an agent generate or update Kubernetes YAML manifests for GKE Autopilot and GKE Standard: Deployments, Services, ConfigMaps, Secrets, PVCs, ServiceAccounts, PodDisruptionBudgets, NetworkPolicies, and Gateway API `Gateway`/`HTTPRoute` resources. It fixes rules for explicit namespaces and dedicated ServiceAccounts, CPU/memory requests and limits (equal on Autopilot), Spot VM nodeSelector plus toleration, non-root securityContext with seccomp RuntimeDefault and readOnlyRootFilesystem, secret file mounts with defaultMode 0400, liveness/readiness/startup probes, ClusterIP by default with Gateway API over Ingress, `subPath` mounts, GKE StorageClasses (`standard-rwo`, `premium-rwo`), anti-affinity and PDBs, and stable list keys for Server-Side Apply; for AI inference (vLLM, TGI, Gemma) it requires `nvidia.com/gpu` requests, `cloud.google.com/gke-accelerator` nodeSelectors, a Memory-backed `/dev/shm` emptyDir, GCS FUSE CSI read-only weight mounts, and `gcloud container ai profiles manifests create` as the preferred generator, with Developer Knowledge MCP lookups (`search_documents`, `get_document(s)`, `answer_query`) for grounding; four reference files hold complete example manifests. It explicitly does not cover live cluster operations, pod troubleshooting (gke-workload-troubleshooting), or cluster provisioning (gke-cluster-creation), and it does not apply manifests to a cluster.
- **S42 gke-multitenancy (agents/platform/skills/gke-multitenancy)**: Platform Agent skill (upstream google/skills copy) for sharing one GKE cluster between teams or environments. It compares namespace-per-team, namespace-per-environment, node-pool-per-team and cluster-per-team models, then gives manifests for namespaces and labels, namespace-scoped Role/RoleBinding to Google Groups, ResourceQuota, LimitRange (with the rule that min/max need defaults), a same-namespace-plus-DNS NetworkPolicy, cost-center labels and `--enable-cost-allocation`. Single-cluster, write-oriented (`kubectl create/label/apply`, `gcloud container clusters update`); it explicitly excludes single-tenant cluster configuration and general deployment steps (gke-basics, gke-app-onboarding) and defers RBAC hardening and default-deny policy to gke-platform-security and gke-workload-security.
- **S43 gke-multitenancy (third_party/google-skills/gke-multitenancy)**: Platform Agent skill (upstream google/skills copy) for sharing one GKE cluster between teams or environments. It compares namespace-per-team, namespace-per-environment, node-pool-per-team and cluster-per-team models, then gives manifests for namespaces and labels, namespace-scoped Role/RoleBinding to Google Groups, ResourceQuota, LimitRange (with the rule that min/max need defaults), a same-namespace-plus-DNS NetworkPolicy, cost-center labels and `--enable-cost-allocation`. Single-cluster, write-oriented (`kubectl create/label/apply`, `gcloud container clusters update`); it explicitly excludes single-tenant cluster configuration and general deployment steps (gke-basics, gke-app-onboarding) and defers RBAC hardening and default-deny policy to gke-platform-security and gke-workload-security.
- **S44 gke-networking (agents/platform/skills/gke-networking)**: Platform Agent reference for core GKE cluster networking, read and write at the cluster level: golden-path settings for private nodes, private endpoint enforcement, DNS endpoint access, Dataplane V2, Cloud DNS, Auto IPAM and max pods per node; get-credentials via --dns-endpoint or --internal-ip; create-auto with a bring-your-own VPC and subnet; Pod and Service CIDR sizing; Cloud NAT egress; and a local footer that checks controlPlaneEndpointsConfig before passing --dns-endpoint and points at /opt/data/scripts/gke_endpoint.py. Uses MCP get_cluster, update_cluster, apply_k8s_manifest, get_k8s_resource plus gcloud. Explicitly excludes application ingress, load balancing and service networking (gke-service-networking) and defers NetworkPolicy manifests to gke-workload-security and gke-multitenancy.
- **S45 gke-networking (third_party/google-skills/gke-networking)**: Lets an agent design and configure core GKE cluster networking: it states golden-path values for GKE cluster fields (privateClusterConfig.enablePrivateNodes, masterAuthorizedNetworksConfig, controlPlaneEndpointsConfig.dnsEndpointConfig.allowExternalTraffic, networkConfig.datapathProvider=ADVANCED_DATAPATH, clusterDns=CLOUD_DNS, autoIpamConfig, maxPodsPerNode), shows `gcloud container clusters get-credentials --dns-endpoint|--internal-ip` for private-cluster access, `gcloud container clusters create-auto` with bring-your-own `--network/--subnetwork` and secondary ranges, explains VPC-native (Alias IP) benefits, gives Pod/Service CIDR sizing rules per maxPodsPerNode, and lists Cloud NAT egress options; it names the gke MCP tools get_cluster, update_cluster, apply_k8s_manifest, get_k8s_resource. It explicitly does not cover application ingress, load balancing or Service/Gateway networking (deferred to gke-service-networking), and defers NetworkPolicy manifests to gke-workload-security and gke-multitenancy. It is a reference of settings and single commands, not a troubleshooting procedure, and it contains no Kubernetes manifests.
- **S46 gke-observability (agents/cluster/skills/gke-observability)**: Lets the read-only Cluster Agent audit one GKE cluster's observability: it reads loggingConfig/monitoringConfig with gcloud describe, checks gmp-system pods, reads workload logs, and gives example Cloud Logging (LQL) queries. For every gap it reports a proposal rather than a change: Managed Service for Prometheus, control-plane metrics, Dataplane V2 observability, each expressed as a Config Connector ContainerCluster field, plus generic advice on structured logging, dashboards/alerts, OpenTelemetry tracing and Cloud Profiler. It does not run any cluster or GCP mutation, does not open PRs, and does not cover harness/kube-agents self-observability (that is kube-agents-observability) or fleet-wide audits.
- **S47 gke-observability (agents/platform/skills/gke-observability)**: Platform Agent reference for GKE monitoring and logging on a single cluster, mostly write: golden-path loggingConfig and monitoringConfig components including APISERVER, SCHEDULER and CONTROLLER_MANAGER, gcloud container clusters update --monitoring / --enable-managed-prometheus / --enable-dataplane-v2-flow-observability, kubectl top for live usage, gcloud logging read and LQL queries for system, workload and audit logs, key metrics, an alert threshold table with Cloud Monitoring rules, node-health metrics, cost notes and a pointer to Cloud Trace and Profiler. Uses MCP gke:get_cluster, gke:list_k8s_events, gke:get_k8s_logs, gke:get_k8s_cluster_info, gke:describe_k8s_resource. Explicitly excludes application logging frameworks and external APMs outside GKE.
- **S48 gke-observability (third_party/google-skills/gke-observability)**: Platform Agent reference for GKE monitoring and logging on a single cluster, mostly write: golden-path loggingConfig and monitoringConfig components including APISERVER, SCHEDULER and CONTROLLER_MANAGER, gcloud container clusters update --monitoring / --enable-managed-prometheus / --enable-dataplane-v2-flow-observability, kubectl top for live usage, gcloud logging read and LQL queries for system, workload and audit logs, key metrics, an alert threshold table with Cloud Monitoring rules, node-health metrics, cost notes and a pointer to Cloud Trace and Profiler. Uses MCP gke:get_cluster, gke:list_k8s_events, gke:get_k8s_logs, gke:get_k8s_cluster_info, gke:describe_k8s_resource. Explicitly excludes application logging frameworks and external APMs outside GKE.
- **S49 gke-platform-security (agents/platform/skills/gke-platform-security)**: Lets an agent verify and change platform-level GKE cluster security with gcloud: a golden-path table of cluster fields (workloadIdentityConfig.workloadPool, secretManagerConfig with rotation, rbacBindingConfig.enableInsecureBindingSystem{Authenticated,Unauthenticated}=false, shieldedInstanceConfig secure boot and integrity monitoring, workloadMetadataConfig GKE_METADATA), then `gcloud container clusters describe/update` recipes for --enable-secret-manager with rotation interval, auditing rbacBindingConfig, --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE, --enable-shielded-nodes, GKE Sandbox enablement, --database-encryption-key with the Cloud KMS IAM grant to the GKE service agent, and --security-posture / --workload-vulnerability-scanning. It also covers the five predefined roles/container.* IAM roles with when to use each, the GKE service agent and a dedicated minimal node service account (monitoring.metricWriter, logging.logWriter), RBAC best practices audited via check_k8s_auth / get_k8s_resource or kubectl auth can-i, and `gcloud projects add-iam-policy-binding` patterns giving a GSA storage.objectViewer, cloudsql.client or pubsub.subscriber. It explicitly excludes Workload Identity GSA-to-KSA binding (gke-workload-identity), workload-level controls such as SecretProviderClass, Pod Security Standards, NetworkPolicy and runtimeClassName gvisor (gke-workload-security), private cluster and Dataplane V2 settings (gke-networking), and enterprise RBAC planning (gke-multitenancy).
- **S50 gke-platform-security (third_party/google-skills/gke-platform-security)**: Lets an agent verify and change cluster-level GKE security settings with `gcloud container clusters describe/update` and the `gke:get_cluster`, `k8s:check_k8s_auth`, `k8s:get_k8s_resource` MCP tools: a golden-path defaults table (`workloadIdentityConfig`, `secretManagerConfig` with rotation, `rbacBindingConfig.enableInsecureBinding*`, Shielded Node secure boot and integrity monitoring, `GKE_METADATA`), enabling the Secret Manager add-on (`--enable-secret-manager`, `--secret-manager-rotation-interval`), checking insecure `system:authenticated`/`system:unauthenticated` bindings, enabling Binary Authorization (`--binauthz-evaluation-mode`), Shielded Nodes (`--enable-shielded-nodes`) and GKE Sandbox, the five predefined `roles/container.*` IAM roles, the GKE service agent and node service account, and project-level `gcloud projects add-iam-policy-binding` grants for a GSA (`roles/storage.objectViewer`, `roles/cloudsql.client`, `roles/pubsub.subscriber`); the repo overlay appends `--database-encryption-key` (Cloud KMS secrets encryption) and `--security-posture` / `--workload-vulnerability-scanning`. It explicitly does not cover Workload Identity bindings (gke-workload-identity), workload-level controls such as SecretProviderClass manifests, Pod Security Standards, NetworkPolicy and `runtimeClassName: gvisor` (gke-workload-security), private cluster and Dataplane V2 networking (gke-networking), or enterprise RBAC planning (gke-multitenancy).
- **S51 gke-productionize (agents/platform/skills/gke-productionize)**: An orchestrator (meta-skill) for productionizing a GKE cluster, one application, or a set of applications. It prescribes a discovery phase (`gcloud container clusters describe` for Autopilot vs Standard and release channel; `kubectl get deployment/namespace/pods/hpa/pdb/networkpolicy` for resource requests and limits, probes, Pod Security Standards labels, dedicated ServiceAccounts), then mandates delegating to `gke-app-onboarding`, `gke-workload-scaling`, `gke-observability`, `gke-reliability`, `gke-workload-identity`, `gke-platform-security`, `gke-workload-security`, `gke-backup-dr`, `gke-service-networking`, and `gke-cost-optimization`, and ends with a RAG status per area plus an overall readiness score, asking the user before any state-changing step. It explicitly does not cover deep single-domain implementation (HPA/VPA tuning, Workload Identity setup, network policy authoring, Backup for GKE configuration, Gateway/Cloud Armor, rightsizing) and holds no domain procedures of its own; it is read-only assessment plus routing.
- **S52 gke-productionize (third_party/google-skills/gke-productionize)**: Platform Agent orchestrator for a production readiness review of a GKE cluster or one or more applications, mostly read-only discovery (gcloud container clusters describe, kubectl get deployment/namespace/pods/hpa/pdb/networkpolicy) followed by mandatory delegation to gke-app-onboarding, gke-workload-scaling, gke-observability, gke-reliability, gke-platform-security, gke-workload-security, gke-backup-dr, gke-service-networking and gke-cost-optimization, ending in a Red/Amber/Green report per area. It asks for user confirmation before state-changing work. Explicitly excludes deep single-domain implementation, which it hands to the domain skills.
- **S53 gke-reliability (agents/cluster/skills/gke-reliability)**: Lets the Cluster Agent audit one GKE cluster and its workloads for high-availability posture and report proposed fixes: whether the control plane is regional and node pools span zones, whether namespaces carry PodDisruptionBudgets, whether Deployments define readiness/liveness/startup probes, whether terminationGracePeriodSeconds and SIGTERM handling are set, whether topologySpreadConstraints spread pods across zones, and whether a maintenance window exists (proposed as a Config Connector ContainerCluster recurringWindow). It is explicitly read-only: every manifest or setting it shows is a proposal for the report, never an applied change. It does not cover disaster recovery, backups, upgrades, autoscaling, or observability.
- **S54 gke-reliability (agents/platform/skills/gke-reliability)**: Platform Agent reference for workload and cluster availability on a single cluster, read and write via MCP (get_cluster, get_k8s_resource, describe_k8s_resource, apply_k8s_manifest, list_k8s_events) with gcloud and kubectl fallbacks: golden-path regional cluster, surge upgrades, auto-repair, auto-upgrade and REGULAR channel; verifying regional control plane and multi-zone nodes; PodDisruptionBudget manifests; liveness, readiness and startup probe YAML with explicit timeouts; SIGTERM handling with preStop sleep; zone and hostname topology spread constraints; and minimum replica counts per workload type. Explicitly excludes disaster recovery and cluster backups (gke-backup-dr) and defers maintenance windows to gke-upgrades.
- **S55 gke-reliability (third_party/google-skills/gke-reliability)**: Platform Agent reference for workload and cluster availability on a single cluster, read and write via MCP (get_cluster, get_k8s_resource, describe_k8s_resource, apply_k8s_manifest, list_k8s_events) with gcloud and kubectl fallbacks: golden-path regional cluster, surge upgrades, auto-repair, auto-upgrade and REGULAR channel; verifying regional control plane and multi-zone nodes; PodDisruptionBudget manifests; liveness, readiness and startup probe YAML with explicit timeouts; SIGTERM handling with preStop sleep; zone and hostname topology spread constraints; and minimum replica counts per workload type. Explicitly excludes disaster recovery and cluster backups (gke-backup-dr) and defers maintenance windows to gke-upgrades.
- **S56 gke-service-networking (agents/platform/skills/gke-service-networking)**: Platform Agent reference for exposing GKE applications, write via Kubernetes manifests on a single cluster: Gateway and HTTPRoute with the gke-l7-global-external-managed class, legacy GKE Ingress with the gce class annotation, Cloud Armor via BackendConfig securityPolicy and the cloud.google.com/backend-config Service annotation, ManagedCertificate for Ingress and Certificate Manager or Secret TLS on a Gateway HTTPS listener, container-native load balancing via the cloud.google.com/neg annotation, and Private Service Connect via ServiceAttachment. No MCP tools or gcloud commands are listed. Explicitly excludes cluster IP planning, Dataplane V2 network policies and node NAT egress (gke-networking).
- **S57 gke-service-networking (third_party/google-skills/gke-service-networking)**: Platform Agent reference for exposing GKE applications, write via Kubernetes manifests on a single cluster: Gateway and HTTPRoute with the gke-l7-global-external-managed class, legacy GKE Ingress with the gce class annotation, Cloud Armor via BackendConfig securityPolicy and the cloud.google.com/backend-config Service annotation, ManagedCertificate for Ingress and Certificate Manager or Secret TLS on a Gateway HTTPS listener, container-native load balancing via the cloud.google.com/neg annotation, and Private Service Connect via ServiceAttachment. No MCP tools or gcloud commands are listed. Explicitly excludes cluster IP planning, Dataplane V2 network policies and node NAT egress (gke-networking).
- **S58 gke-stall-detection**: Cluster Agent, read-only, single cluster and one namespace (or one kind in it). Runs /opt/data/scripts/stall_report.py (agents/platform/scripts/stall_report.py), which applies four heuristics (generation-lag, stale-condition, repeating-warnings, dangling-reference) over kubectl get output for Gateways, HTTPRoutes, Deployments, custom resources and other namespaced kinds, with age thresholds and --kind/--threshold-minutes/--json flags, then records the finding on the kanban card via kanban_complete (including the Session KV controller-stall card format). It explicitly excludes failing-pod and bad-event symptoms (those go to gke-workload-troubleshooting and gke-reliability), never patches, opens PRs or reads Secret contents, and notes that Secret-typed references are unchecked under the default read-only identity.
- **S59 gke-stockout-investigator**: Platform Agent plugin skill (installed into the `platform` profile via the gke-stockout-investigator AgentPlugin) that handles a GKE autoscaler stockout alert from Pub/Sub end to end: send a `send_notification`, check for an open PR on `platform-agent/remediate-stockout-<workload>` with `vcs.py proposal list --source`, confirm the stockout is live via `kubectl get/describe pod`, take a GitOps working copy with `submit_suggestion.py prepare`, run quota/reservation/`kubectl top`/`gcloud beta compute advice capacity[-history]`/`cluster-autoscaler-status` diagnostics, apply eight ComputeClass debugging rules (A-H), edit ComputeClass or workload YAML with remediation comments, commit, and open the PR with `submit_suggestion.py submit --body-file`. Fleet-facing but one alert and one cluster per run; GitOps write, never a live-cluster mutation. It explicitly forbids `execute_code`, forge CLIs, `git add .`, `--body`, and branch-name suffixes.
- **S60 gke-storage (agents/cluster/skills/gke-storage)**: A short how-to on configuring GKE storage: writing a StorageClass for the Persistent Disk CSI driver, choosing between the PD, Filestore and Cloud Storage FUSE CSI drivers, creating a ReadWriteMany PVC, and expanding a volume by editing the PVC. Every workflow is a create-or-apply write and there are no diagnostic commands, so it reads as configuration guidance rather than single-cluster debugging. Sits under the Cluster Agent; a longer upstream-synced copy with the same name lives under agents/platform/skills. Does not state exclusions.
- **S61 gke-storage (agents/platform/skills/gke-storage)**: Platform Agent skill (upstream google/skills copy) for configuring storage on a single GKE cluster: it lists the golden-path CSI drivers and built-in StorageClasses, gives manifests for a custom regional pd-ssd StorageClass, ReadWriteOnce PVCs, Filestore ReadWriteMany PVCs and a GCS FUSE bucket mount, and shows PVC expansion via kubectl patch or the gke MCP patch_k8s_resource tool. It is a write skill (apply_k8s_manifest, patch) with best-practice guidance and a pointer to gke-backup-dr for PVC backup. It explicitly excludes database administration and replication strategies outside volume provisioning.
- **S62 gke-storage (third_party/google-skills/gke-storage)**: Platform Agent skill (upstream google/skills copy) for configuring storage on a single GKE cluster: it lists the golden-path CSI drivers and built-in StorageClasses, gives manifests for a custom regional pd-ssd StorageClass, ReadWriteOnce PVCs, Filestore ReadWriteMany PVCs and a GCS FUSE bucket mount, and shows PVC expansion via kubectl patch or the gke MCP patch_k8s_resource tool. It is a write skill (apply_k8s_manifest, patch) with best-practice guidance and a pointer to gke-backup-dr for PVC backup. It explicitly excludes database administration and replication strategies outside volume provisioning.
- **S63 gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring)**: Platform Agent skill (upstream google/skills copy) for the GKE TPU Dynamic Slices feature on a single cluster: it diagnoses a Slice custom resource with kubectl describe slice and a lifecycle-state table (SliceNotCreated, SliceCreationFailed, ACTIVATING, ACTIVE, ACTIVE_DEGRADED, FAILED, DEACTIVATING, INCOMPLETE), checks single-slice and JobSet multi-slice pod annotations and nodeSelectors, and gives two confirm-first write procedures: removing stuck finalizers with kubectl patch, and disabling the slice controller (gcloud container clusters update --no-enable-slice-controller, delete the slices.accelerator.gke.io CRD, strip node labels). A references file shows example failure conditions. It explicitly excludes generic node pool creation and non-TPU workloads (pointing to gke-basics and gke-cluster-creation).
- **S64 gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring)**: Platform Agent skill (upstream google/skills copy) for the GKE TPU Dynamic Slices feature on a single cluster: it diagnoses a Slice custom resource with kubectl describe slice and a lifecycle-state table (SliceNotCreated, SliceCreationFailed, ACTIVATING, ACTIVE, ACTIVE_DEGRADED, FAILED, DEACTIVATING, INCOMPLETE), checks single-slice and JobSet multi-slice pod annotations and nodeSelectors, and gives two confirm-first write procedures: removing stuck finalizers with kubectl patch, and disabling the slice controller (gcloud container clusters update --no-enable-slice-controller, delete the slices.accelerator.gke.io CRD, strip node labels). A references file shows example failure conditions. It explicitly excludes generic node pool creation and non-TPU workloads (pointing to gke-basics and gke-cluster-creation).
- **S65 gke-tpu-metrics-monitoring (agents/platform/skills/gke-tpu-metrics-monitoring)**: Platform Agent skill (upstream google/skills copy), read-only: it monitors GKE TPU containers, nodes and multi-host node pools through Cloud Monitoring system metrics and PromQL. It covers checking the runtime-metrics prerequisites (containerPort 8431, JAX and GKE versions), the accelerator duty_cycle, memory and tensorcore/bandwidth utilization metrics, node status conditions, node pool status and multi-host availability, interruption counts by type and reason, and 7-day MTTR and MTBI calculations, for one cluster or project-wide. A references file lists metric signatures (node unready, node pool error, preemption, host error, low utilization). It explicitly excludes non-TPU workload monitoring and non-metric TPU debugging.
- **S66 gke-tpu-metrics-monitoring (third_party/google-skills/gke-tpu-metrics-monitoring)**: Platform Agent skill (upstream google/skills copy), read-only: it monitors GKE TPU containers, nodes and multi-host node pools through Cloud Monitoring system metrics and PromQL. It covers checking the runtime-metrics prerequisites (containerPort 8431, JAX and GKE versions), the accelerator duty_cycle, memory and tensorcore/bandwidth utilization metrics, node status conditions, node pool status and multi-host availability, interruption counts by type and reason, and 7-day MTTR and MTBI calculations, for one cluster or project-wide. A references file lists metric signatures (node unready, node pool error, preemption, host error, low utilization). It explicitly excludes non-TPU workload monitoring and non-metric TPU debugging.
- **S67 gke-upgrades (agents/platform/skills/gke-upgrades)**: Lets the Platform Agent plan, execute, and troubleshoot GKE control-plane and node-pool upgrades on Standard and Autopilot clusters: it produces upgrade plans, pre/post-upgrade checklists, gcloud/kubectl runbooks (surge and blue-green strategies, rollback, maintenance windows and exclusions), release-channel and support-lifecycle advice, GPU/TPU upgrade guidance, and a fixed 5-cause diagnosis for stuck upgrades (PDBs, capacity, bare pods, webhooks, PVCs) plus stockout/quota and maintenance-window-pause handling. A local addition hands fleet-wide version lag, readiness (PDB/exclusion/skew/webhook) and GitOps deprecated-API scans to the sibling fleet-upgrade-verification scripts. It explicitly does not cover cluster creation, application onboarding, networking/routing setup, or security policy configuration.
- **S68 gke-upgrades (third_party/google-skills/gke-upgrades)**: Lets an agent produce environment-specific GKE upgrade artifacts for one cluster at a time: an upgrade plan (sequential control-plane minor path, skip-level node pools, 2-minor skew rule, dev-to-prod progression with Rollout Sequencing), pre/post-upgrade checklists (references/checklists.md), and runbooks built from `gcloud container clusters upgrade --master|--node-pool`, `gcloud container node-pools update --max-surge-upgrade/--max-unavailable-upgrade`, `--enable-blue-green-upgrade` soak tuning, maintenance window and exclusion flags (`--add-maintenance-exclusion-name/-start/-end/-until-end-of-support/-scope`), and PDB backup/relax/restore steps (references/runbook-template.md). It covers release-channel strategy (Rapid/Regular/Stable/Extended, 14/24-month support), exclusion scopes and their 90-day/3-per-cluster/48h-per-92-day limits, mandatory GKE override scenarios, surge vs blue-green vs autoscaled blue-green per workload type (stateless, stateful, GPU/TPU with maxSurge=0 and driver/CUDA coupling), maintenance-window pauses, and a 12-step stuck-upgrade diagnosis (PDB ALLOWED DISRUPTIONS=0, Pending pods, bare pods, admission webhooks, PVC attach, long grace periods, `gcloud container operations list`, ZONE_RESOURCE_POOL_EXHAUSTED/QUOTA_EXCEEDED stockouts with credential rotation and DNS endpoint, GPU driver regressions, `get-upgrade-info` paused reasons, NotReady nodes) in references/troubleshooting.md. It explicitly does not cover cluster creation, application onboarding, networking/routing, or security policy (deferred to gke-basics and other gke-* skills), and in this upstream copy it has no executed fleet-wide version or readiness scan (the shipped copy appends a pointer to fleet-upgrade-verification for that).
- **S69 gke-workload-identity (agents/platform/skills/gke-workload-identity)**: Gives the Platform Agent a seven-step, read-only diagnostic for Workload Identity Federation for GKE: classify the error signature from Pod logs and Cloud Logging (403 iam.serviceAccounts.getAccessToken, 403 PERMISSION_DENIED on the target API, 'could not find default credentials', or calls running as the node default service account); check the cluster workloadPool and node-pool workloadMetadataConfig.mode (GKE_METADATA vs GCE_METADATA) with gcloud container clusters/node-pools describe; verify the KSA-to-identity binding for both direct principal binding (principal://iam.googleapis.com/.../svc.id.goog/subject/ns/.../sa/...) and legacy GSA impersonation (iam.gke.io/gcp-service-account annotation plus roles/iam.workloadIdentityUser); search IAM roles on the target resource with gcloud asset search-all-iam-policies or gcloud projects get-iam-policy; check gke-metadata-server DaemonSet health, its logs, 169.254.169.254 connectivity, DNS, network-policy egress and OOM from >3,000 KSAs; handle the legacy 'Invalid form of account ID' case with the iam.gke.io/return-principal-id-as-email annotation; and escalate when logs are missing or the cause is undetermined. It only proposes gcloud add-iam-policy-binding, node-pools update and kubectl annotate commands for a human, never applies them, and a kube-agents appendix tells the agent that the command gate refuses gcloud iam service-accounts get-iam-policy, gcloud asset search-all-iam-policies and kubectl exec, so those steps are handed to the user. It does not cover in-cluster Kubernetes RBAC errors, general workload crashes (gke-workload-troubleshooting), Pod Security Standards or NetworkPolicies (gke-workload-security), or Workload Identity outside GKE.
- **S70 gke-workload-identity (third_party/google-skills/gke-workload-identity)**: Gives a read-only, seven-step diagnostic for Workload Identity Federation for GKE: classify the error signature from Pod logs, gke-metadata-server logs and Cloud Logging deep links (403 iam.serviceAccounts.getAccessToken, 403 PERMISSION_DENIED on the target API, could not find default credentials, calls running as the node default service account); verify the cluster workloadPool and node-pool workloadMetadataConfig.mode=GKE_METADATA with gcloud container clusters/node-pools describe; verify the KSA-to-identity binding for both direct principal binding (principal://iam.googleapis.com/.../workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NS/sa/KSA) and legacy GSA impersonation (iam.gke.io/gcp-service-account annotation plus roles/iam.workloadIdentityUser on the GSA); verify target-resource IAM with gcloud asset search-all-iam-policies; check gke-metadata-server DaemonSet health, OOM eviction above 3000 service accounts, 169.254.169.254 connectivity, DNS (GCE_METADATA_HOST), NetworkPolicy egress (169.254.169.252:988, sts.googleapis.com:443) and startup races; and handle the legacy 'Invalid form of account ID' case with iam.gke.io/return-principal-id-as-email. It proposes gcloud add-iam-policy-binding, node-pools update --workload-metadata=GKE_METADATA, or kubectl annotate commands for a human and never applies IAM, KSA, node-pool or cluster changes itself, escalating to GKE support when logs are missing or the cause is undetermined. It explicitly does not cover in-cluster Kubernetes RBAC (API-server authorization) errors, general workload crashes (gke-workload-troubleshooting), or Pod Security Standards and NetworkPolicy review (gke-workload-security).
- **S71 gke-workload-scaling (agents/cluster/skills/gke-workload-scaling)**: Lets the read-only Cluster Agent propose scaling changes for workloads on one GKE cluster: a fixed replica count on a Deployment, an autoscaling/v2 HorizontalPodAutoscaler (CPU, memory, External or Prometheus metrics), an autoscaling.k8s.io/v1 VerticalPodAutoscaler with an update mode and per-container bounds, and, through Config Connector ContainerCluster/ContainerNodePool fields, turning on VPA and node-pool autoscaling. It ships two example manifests (assets/hpa-example.yaml, assets/vpa-example.yaml) and a best-practice list (resource requests, no shared HPA/VPA metric, PDBs, HPA stabilization lag, VPA Auto-mode restarts). It never runs kubectl or gcloud: every change is reported as a proposal, and it does not cover diagnosing why a workload is unhealthy, node-level machine shapes, or fleet-wide rollout of the change.
- **S72 gke-workload-scaling (agents/platform/skills/gke-workload-scaling)**: Platform Agent skill (upstream google/skills copy with a repo-added footer) for scaling workloads on a single GKE cluster: manual kubectl scale, Horizontal Pod Autoscaler via kubectl autoscale or the bundled autoscaling/v2 manifest, Vertical Pod Autoscaler enablement on Standard clusters and its update modes (Off, Initial, Auto, InPlaceOrRecreate), a VPA manifest, a rightsizing workflow from VPA Off-mode recommendations with a 20% buffer, and HPA/VPA best practices. The footer requires loading the capacity-obtainability skill before recommending GPU/TPU or large-shape scale-ups. It writes HPA/VPA objects and deployment replica counts. It explicitly excludes Cluster Autoscaler, static cluster sizing and node machine-type choices.
- **S73 gke-workload-scaling (third_party/google-skills/gke-workload-scaling)**: Lets an agent scale a GKE Deployment manually (`kubectl scale deployment --replicas`), configure a Horizontal Pod Autoscaler on CPU, memory, External or Prometheus-backed metrics (`kubectl autoscale` or an `autoscaling/v2` HPA manifest from assets/hpa-example.yaml), and configure a Vertical Pod Autoscaler (`gcloud container clusters update --enable-vertical-pod-autoscaling` on Standard, `autoscaling.k8s.io/v1` manifest from assets/vpa-example.yaml, update modes Off/Initial/Auto/InPlaceOrRecreate). It also gives a VPA-based rightsizing workflow (run in Off mode 24h, read `kubectl describe vpa`, apply target*1.2 with a condition/recommendation/risk table) and best practices on resource requests, HPA/VPA metric conflicts, PDBs and HPA stabilization. It explicitly does not cover cluster-level autoscaling (Cluster Autoscaler), static cluster sizing, or node machine types; it is the upstream google/skills source copy for the generated agents/platform/skills/gke-workload-scaling.
- **S74 gke-workload-security (agents/cluster/skills/gke-workload-security)**: Lets the read-only Cluster Agent audit one GKE cluster's security posture (Workload Identity, Network Policy / Dataplane V2, Shielded Nodes, Binary Authorization, private nodes via scripts/audit_cluster.sh and gcloud describe) and report hardening proposals as manifests or Config Connector field changes: Workload Identity KSA/GSA setup, Calico enablement on non-DPv2 clusters as two ordered changes, a default-deny NetworkPolicy per namespace, Shielded Nodes, a gVisor node pool plus runtimeClassName, restricted Pod Security Standards labels, Secret Manager CSI SecretProviderClass mounts, and Dataplane V2 NetworkLogging. It never applies a change; it does not cover RBAC hardening, control-plane security flags, Binary Authorization policy authoring, or Policy Controller constraints beyond a one-line recommendation.
- **S75 gke-workload-security (agents/platform/skills/gke-workload-security)**: Lets the Platform Agent audit a GKE cluster's security posture with `scripts/audit_cluster.sh <cluster> <region> <project>` (gcloud describe + jq checks for Workload Identity pool, NetworkPolicy/Dataplane V2, Shielded Nodes, Binary Authorization, private nodes), then apply workload-level controls: check `networkConfig.datapathProvider` and enable Calico NetworkPolicy enforcement in two steps on non-DPv2 clusters (`--update-addons=NetworkPolicy=ENABLED`, then `--enable-network-policy`), apply the bundled `assets/default-deny-netpol.yaml` to a namespace, run pods under GKE Sandbox with `runtimeClassName: gvisor`, label namespaces with `pod-security.kubernetes.io/enforce=restricted`, mount Secret Manager secrets through the Secrets Store CSI driver (`SecretProviderClass` with `provider: gcp`), and turn on Dataplane V2 `NetworkLogging` (networking.gke.io/v1alpha1). It also retains a legacy Workload Identity GSA-impersonation walkthrough (`roles/iam.workloadIdentityUser` binding, `iam.gke.io/gcp-service-account` annotation, `assets/workload-identity-pod.yaml`) but tells the agent to load `gke-workload-identity` first. It explicitly does not cover Workload Identity as the primary path (gke-workload-identity), cluster-wide control-plane security, RBAC hardening, Binary Authorization, Shielded Nodes, or enabling GKE Sandbox/platform add-ons (gke-platform-security), nor container securityContext authoring (gke-manifest-generation).
- **S76 gke-workload-security (third_party/google-skills/gke-workload-security)**: Lets an agent audit a GKE cluster's posture with `scripts/audit_cluster.sh <cluster> <region> <project>` (gcloud describe + jq: Workload Identity pool, NetworkPolicy/Dataplane V2, Shielded Nodes, Binary Authorization, private nodes), then apply workload-level controls: a default-deny NetworkPolicy asset (`assets/default-deny-netpol.yaml`) per namespace plus `gcloud container clusters update --update-addons=NetworkPolicy=ENABLED` on non-DPv2 clusters, a `NetworkLogging` (networking.gke.io/v1alpha1) manifest for Dataplane V2 allow/deny logging, `runtimeClassName: gvisor` for GKE Sandbox pods, `pod-security.kubernetes.io/enforce=restricted` namespace labels, and a `SecretProviderClass` plus CSI volume for Secret Manager secrets. It also still carries a full Workload Identity KSA-to-GSA impersonation walkthrough (create KSA, `roles/iam.workloadIdentityUser` binding, `iam.gke.io/gcp-service-account` annotation, test pod `assets/workload-identity-pod.yaml`). Its description explicitly excludes Workload Identity (route to gke-workload-identity), control-plane security, RBAC hardening, Binary Authorization, Shielded Nodes, and enabling GKE add-ons (route to gke-platform-security); it does not cover container securityContext authoring, Policy Controller/Gatekeeper beyond a one-line mention, or image signing.
- **S77 gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting)**: Cluster Agent, read-only, single workload in one namespace. A five-step SOP: acquire project, cluster, workload and a one-hour time window; read pod and Deployment status and classify Pending, CrashLoopBackOff (exit 137 vs other), ContainerCreating; read namespace events with kubectl get events or gcloud logging read and match FailedScheduling, FailedMount, image-pull failures (with a git log search for the last working tag); read current and previous container logs for OOM, stack traces, egress timeouts and read-only-filesystem errors; check Service endpoints and NetworkPolicies; then record the RCA and a proposed YAML patch on the kanban card with kanban_complete. It explicitly excludes applying patches, opening PRs (submit-suggestion is the Platform Agent's) and passing findings through the chat reply.
- **S78 gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting)**: Platform Agent copy (overlaid from google/skills, with an upstream.lock and two local patches) of a five-step runbook for a failing workload on one GKE cluster: read pod and Deployment status with kubectl, read namespace events (kubectl or gcloud logging read), read current and previous container logs, check Service endpoints and NetworkPolicies, then write a root-cause summary and a corrected manifest. Covers CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, ContainerCreating, FailedMount, read-only filesystem and egress timeouts, with a dry-run mode that prints the commands when the cluster is unreachable. Diagnostics are read-only; the only write is a GitOps pull request, and only when the request asked for the fix (SOUL.md section 3, item 3). It excludes cluster provisioning, node pool creation and non-Kubernetes Google Cloud services.
- **S79 gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting)**: A byte-identical copy of the upstream `google/skills` `gke-workload-troubleshooting` skill at the commit pinned in `agents/platform/skill-overlays/gke-workload-troubleshooting/upstream.lock`; it is layer 1 of the upstream-skill-overlay design (`scripts/skill_overlay.py`, `docs/designs/upstream-skill-overlays.md`), and `make skills-check` verifies its sha256 against the lock and regenerates the shipped `agents/platform/skills/gke-workload-troubleshooting` from it plus two patches. Its content is a five-step read-only diagnostic SOP for a single GKE workload (pod status and exit codes, namespace events via `kubectl get events` and `gcloud logging read`, `kubectl logs`, endpoints and NetworkPolicy checks, then a proposed GitOps manifest fix opened as a PR), with a dry-run fallback when the cluster is unreachable. It explicitly does not cover cluster provisioning, node pool creation, or non-Kubernetes Google Cloud services; the folder is excluded from prettier, shellcheck and docs-link checks and is not shipped in any agent image.
- **S80 inspect-repository**: Platform Agent, read-only. Lets the agent read the source of any GitHub or GitLab repository the install can reach, with no local git, through the credential broker: `inspect_repository.py` offers `clone` (copy a tree or `--prefix` into /opt/data/scratch), and `open`/`list`/`grep`/`fetch`/`close` on a broker-side handle, each printing one JSON object. Covers answering questions about code, reading upstream projects and dependencies, and reading the GitOps repository for context. It does not change repositories (that is submit-suggestion or fleet-audit) and it tells the agent not to re-open a repository that fleet-audit or submit-suggestion already handed it.
- **S81 install-kube-agents**: Lets an agent drive a fresh kube-agents install onto a GKE cluster through `install.sh` in non-interactive mode: detect the operator's GCP project, region, credentials and existing clusters, interview them for the choices that shape the install (cluster, model provider, chat platform, GitOps forge, permission set), preview with `--dry-run` or `--generate-only`, obtain explicit consent for every change to a pre-existing cluster (Workload Identity, CMEK, node-pool migration, NetworkPolicy, gVisor pool), apply, read the JSON report and hand over the terminal access commands. It also covers the GitHub token-minter paths (PEM import via install.sh or ahead-of-time KMS key), GitLab as the GitOps forge (token file, private CA), and the manual Terraform + Helm route for GitHub Enterprise Server. It does not cover upgrading or uninstalling an existing install (it defers to `upgrade-kube-agents` and `uninstall-kube-agents`), nor the token-minter key procedure or flag default values, which it defers to the site docs, `scripts/installer/README.md` and `install.defaults.env`.
- **S82 kube-agents-observability**: Lets the Platform Agent audit and troubleshoot the kube-agents install's own telemetry: agent log files and the audit.jsonl tool-call trail, the fluent-bit sidecar, the four chart-rendered PodMonitoring scrapes (watcher, chat plugin, credential broker, A2A gateway) proved through Cloud Monitoring, LiteLLM token metrics, OTLP collector resolution read off PlatformAgent status.telemetry, Cloud Trace span latency, and the API/dashboard listeners. It ships five Python helpers (chat users from Cloud Logging, token usage, metric descriptors, trace list, trace latency breakdown) that call GCP REST APIs with gcloud ADC. It does not cover workload or cluster observability for user applications (that is gke-observability), does not change any configuration, and does not fetch metrics from vLLM or non-LiteLLM providers.
- **S83 manage-cluster**: Lets the Platform Agent bring one existing GKE cluster under management on an explicit user request by verifying the cluster exists and running the in-image `cluster_agent_profile.py create` script, which scaffolds a read-only Cluster Agent profile immediately instead of waiting for the `cluster-agent-reconcile` cron. It also covers the reverse, stopping management, by routing the user to declare an exclusion where the install's scope lives (`SCOPE_EXCLUDE_CLUSTERS` in `install.env` plus `./upgrade.sh --upgrade-mode=full`, the chart value, the tfvars entry, or `spec.scope.exclude.clusters` on a hand-applied `PlatformAgent`) because deleting the profile alone is undone by the next reconcile. It does not cover creating or deleting GKE clusters (that is `gke-cluster-creation`), bulk reconciliation across the fleet, or any mutation of workloads on the managed cluster.
- **S84 pr-conversation**: Platform Agent, reached from a kanban card filed by the github-repo-watcher cron. Covers answering a reviewer on a pull request the agent itself opened (head branch `platform-agent/*`): `pr_conversation.py poll` to read requests and the whole thread with `can_write`/`can_write_known` gates, deciding question vs change request, making a change via submit-suggestion `prepare --branch <head>`/`submit`, confirming the commit landed with `vcs.py proposal view/commits`, then `reply --verify-commit|--no-change` or `refuse`, and ending with `kanban_complete`/`kanban_block`. It explicitly excludes other people's pull requests, changes wider than the branch under review, merging, closing or approving, and pull requests labelled `agent:ignore`.
- **S85 review-address-feedback**: Lets an agent work one review round on an open pull request: collect unresolved threads, review-body findings and red checks; cross-check them against the PR's Self-Review; triage each as fix, push-back or defer (to an issue or an expected_fail eval case); bracket fixes with red/green evidence; fix the whole class of a finding; re-review non-trivial fixes with review-preflight; push once with Testing, Live validation and Self-Review updated; reply in every thread with proof; and resolve addressed threads. It encodes the kube-agents-bot budget rules: at most two self-requested /review (or /review fresh for a body-only edit) before green, /request-review at the third reviewed commit, no re-read after a green AI Review check, and decline-by-default for later-round Medium findings unless Kind is behaviour on code the PR added. It does not run the review itself (review-adversarial, review-docs-drift, review-preflight do that), does not cover opening the PR, merging (Tide), the eval loop mechanics, or GitHub command syntax (delegated to docs/pull-request-workflow.md and AGENTS.md).
- **S86 review-adversarial**: The skill is the repository's adversarial code-review method for a git diff range (`git diff $BASE...HEAD`): a fresh context that did not write the change derives the change's intent, hunts candidates from ten named angles (A line-by-line scan and error-handler audit, B removed behaviour and weakened CI gates, C cross-file consumers and unverified new references, D IAM/RBAC/NetworkPolicy/credential blast radius and pinned GitHub Actions, E reuse, F simplification, G altitude, H AGENTS.md/.agents/rules violations and prose the diff makes false, I scope, Self-Review/Testing/Bug-Fix claims and red-then-green test coverage, J sibling pull requests via `gh pr list`/`gh pr view`), then re-derives each candidate as CONFIRMED/PLAUSIBLE/REFUTED, writes severity-ordered findings (BLOCKER/HIGH/MEDIUM/LOW) with a Fixed or Deliberately-not-fixed disposition that becomes the PR body's Self-Review section. It is used by authors through `review-preflight`, by reviewers through `.claude/commands/pr-review-batch.md`, and by `kube-agents-bot` as the `playbook:` in `.github/kube-agents-bot.yml`. It explicitly holds no plumbing (no subagent spawning, no GitHub-side posting or thread handling), and leaves the exhaustive documentation-drift check to the companion `review-docs-drift` skill, stopping at rules the diff visibly breaks and prose one hop from a hunk.
- **S87 review-docs-drift**: Lets a repo contributor or reviewer agent check a branch diff against main for documentation drift in both directions: which docs a code change should have updated (generated regions, identifier sources, prose pages), and whether changed docs still match source, the canonical-home table in AGENTS.md, the docs/README.md map, and the site audience rule. It names git diff and git grep steps, the make docs-check, make docs-generate, prettier and site build gates, and reports a Blocking/Advisory triage table. It is read-only by design (the report is the deliverable, no silent fixes) and holds no repository facts of its own; it does not cover code defects, which it leaves to review-adversarial.
- **S88 review-preflight**: The skill is orchestration plumbing for the pre-PR self-review: it fixes one three-dot diff range against a freshly fetched gke-labs/kube-agents base (refs/kube-agents-base/<branch>), runs `make docs-check` as a mechanical gate, then fans out `review-adversarial` and `review-docs-drift` as concurrent subagents (or `claude -p` headless sessions) with a handoff that withholds the author's intent, plan, and commit-message bodies and forbids the passes from editing the tree. It covers deduping and merging the two passes' output while keeping each pass's own severity scale (BLOCKER/HIGH/MEDIUM/LOW with CONFIRMED/PLAUSIBLE vs Blocking/Advisory), assigning a disposition per finding to the bar in `.agents/rules/pre_pr_review.md`, re-running only what a fix invalidated, and formatting the result as the PR's **Self-Review** section (passes run, context type, gaps). It explicitly contains no review method of its own, does not state the review requirement (AGENTS.md 'Pull Request Hygiene' does), does not discharge the other local validation checks (prettier, Docker build, go build), and runs no security or skill-quality review passes.
- **S89 review-security-k8s-admission**: A short checklist for a repo-level security reviewer auditing Kubernetes admission control manifests: ValidatingWebhookConfiguration, MutatingWebhookConfiguration, ValidatingAdmissionPolicy and MutatingAdmissionPolicy. It covers failurePolicy and timeouts, namespaceSelector/objectSelector exemptions, binding scope, CEL failure handling and message leakage, caBundle/HTTPS and NetworkPolicy ingress to the webhook, and mutating risks such as sidecar injection, reinvocationPolicy, CEL side effects and execution order. It is read-only review guidance applicable to any cluster or manifest, part of the review-security-k8s-* family; it does not state exclusions.
- **S90 review-security-k8s-agents-audit-logs**: A repo-level review skill for a contributor or review agent, run as a sub-agent of review-security-k8s-agents-main. It is a read-only checklist applied to manifests and agent configs: one dedicated ServiceAccount per agent, an API audit policy that captures agent requests at Metadata or RequestResponse level, logging to stdout/stderr rather than local disk, no hostPath mounts of /var/log/containers or /var/log/pods, and application-level logging of full prompts, outputs and tool input/output with sensitive data scrubbed first. It does not run any command, targets no specific cluster or fleet, and does not state exclusions.
- **S91 review-security-k8s-agents-credentials**: A repo-level review skill (sub-agent of review-security-k8s-agents-main) for a contributor or review agent reading Kubernetes manifests of AI agent workloads. It is a read-only checklist: authenticated outbound calls must go through an injecting credential proxy or sidecar, the main agent container must not receive Secrets via env, envFrom or volume mounts, no plaintext keys in manifests, automountServiceAccountToken false with the token only in the sidecar, a dedicated non-default serviceAccountName, and no wildcard verbs or resources in RBAC. It names no commands or cluster scope and does not state exclusions.
- **S92 review-security-k8s-agents-data-exfil**: A repo-level review skill (sub-agent of review-security-k8s-agents-main) for a contributor or review agent reading Kubernetes configuration of AI agent workloads. It is a read-only checklist on three fronts: egress NetworkPolicies that must be restrictive with no 0.0.0.0/0 and allowlisted to internal services and the LLM API, outbound routing through an egress gateway or proxy (service mesh, HTTP_PROXY) for inspection and SNI allowlisting, and RBAC or volume mounts that give broad get/list/watch on secrets and configmaps. It names no commands or cluster scope and does not state exclusions; its egress checks overlap with review-security-k8s-agents-firewall.
- **S93 review-security-k8s-agents-firewall**: A repo-level review skill (sub-agent of review-security-k8s-agents-main) for a contributor or review agent reading NetworkPolicies and firewall configuration for AI agent control loops and execution sandboxes. Read-only checklist: default-deny egress with a minimal allowlist, blocking agent access to internal cluster APIs and the cloud metadata address 169.254.169.254 on its credential ports (TCP 80 pre-NAT, 988 post-NAT) while leaving port 53 open for Cloud DNS for GKE, flagging 0.0.0.0/0 egress, restricting ingress to trusted upstreams, and flagging LoadBalancer or NodePort exposure without ingress NetworkPolicies. It names no commands or cluster scope; the only stated exclusion is that port 53 to the metadata address is not flagged.
- **S94 review-security-k8s-agents-main**: A repo-level orchestration skill for a contributor or review agent; it is itself a sub-agent of review-security-k8s-main. It takes the project context produced by review-security-k8s-understand, launches six sub-skills in parallel (sandbox, firewall, credentials, prompt-injection, data-exfil, audit-logs), requires each to return a fixed JSON findings shape, triages findings against the context (for example dropping egress-proxy findings for an air-gapped sandbox, or root-in-sandbox findings when a gVisor or Kata RuntimeClass is confirmed) and merges them into one JSON array. It performs no checks of its own, runs no commands, and does not state exclusions.
- **S95 review-security-k8s-agents-prompt-injection**: A repo-level review skill (sub-agent of review-security-k8s-agents-main) for a contributor or review agent reading AI agent deployment configuration. It is read-only and holds only two checks: require an LLM-specific API gateway or WAF sidecar and flag raw agent APIs exposed to untrusted traffic, and ensure system prompts or safety instructions kept in ConfigMaps or environment variables cannot be altered by less privileged workloads. It names no commands or cluster scope and does not state exclusions; despite the description it has no input-sanitization check.
- **S96 review-security-k8s-agents-sandbox**: A repo-level review skill (under .agents/skills, run by a reviewing agent against manifests in a pull request or a cluster, read-only) that audits the execution sandboxes an LLM agent uses to run untrusted code (Python REPLs, bash tools, WASM). It checks three things: a hardened RuntimeClass (gVisor or Kata) instead of a standard pod, separation of the sandbox from the main agent loop plus restrictive seccomp/AppArmor profiles, and ephemeral lifecycles with low CPU, memory and ephemeral-storage limits. It is one of six sub-skills launched by review-security-k8s-agents-main and does not state exclusions.
- **S97 review-security-k8s-gateway**: A repo-level review skill (under .agents/skills, read-only, run against manifests in a pull request or a cluster) that audits Kubernetes Gateway API objects: Gateway, HTTPRoute, TCPRoute, TLSRoute and ReferenceGrant. It flags overlapping hostnames or paths that let one route hijack another, cross-namespace route or secret references without a narrow ReferenceGrant, weak TLS listener settings, missing allowedRoutes namespace restrictions, and wildcard or overly broad hostnames. It is one of ten sub-skills launched by review-security-k8s-main; it covers Gateway API only (classic Ingress is left to review-security-k8s-network) and does not state exclusions.
- **S98 review-security-k8s-main**: A repo-level orchestrator skill (under .agents/skills, read-only) that runs a general Kubernetes security review: it first invokes review-security-k8s-understand for project context, then launches ten sub-skills in parallel (rbac, nodes, network, gateway, namespaces, service-accounts, storage, admission, pod, and agents-main), each told to emit a fixed JSON findings schema with agent, message, file and line. It then triages the raw findings against the context (for example dropping hostPath warnings for CSI daemonsets, or downgrading NetworkPolicy warnings when a strict service mesh exists) and merges them into one JSON array. It performs no checks itself and does not state exclusions.
- **S99 review-security-k8s-namespaces**: A repo-level review skill (under .agents/skills, read-only, run against manifests in a pull request or a cluster) that audits how namespaces are used as isolation boundaries. It flags most workloads piled into one namespace, mixing of trust levels or tenants, custom workloads in default/kube-system/kube-public/kube-node-lease, namespace names that impersonate system components, labels or annotations that bypass policy (OPA exemptions, pod-security enforce=privileged), absurd ResourceQuotas or LimitRanges, suspicious namespace finalizers, cross-namespace references without ReferenceGrant or via ExternalName, and leftover Secrets, ServiceAccounts or RoleBindings in namespaces with no pods. It is a sub-skill of review-security-k8s-main and does not state exclusions.
- **S100 review-security-k8s-network**: A repo-level review skill (under .agents/skills, read-only, run against manifests in a pull request or a cluster) that audits Kubernetes network isolation and exposure: NetworkPolicies, Services, Ingresses and service mesh policy. It requires default-deny ingress and egress NetworkPolicies per namespace, flags missing egress limits and broad CIDRs or empty selectors, flags public LoadBalancers, NodePort services and exposed admin ports (22, 3389, 2379, 10250), requires TLS and HTTPS redirects on Ingress, flags hand-written Endpoints/EndpointSlices and hostNetwork: true, and for Istio-style meshes requires STRICT PeerAuthentication and default-deny AuthorizationPolicies. It is a sub-skill of review-security-k8s-main; Gateway API objects are left to review-security-k8s-gateway, and it does not state exclusions.
- **S101 review-security-k8s-nodes**: A repo-level review skill (under .agents/skills, read-only, run against manifests in a pull request or a cluster) that audits ways a compromised pod or node could escalate to cluster-wide control. It flags hostPath mounts of kubelet credentials (/etc/kubernetes, /var/lib/kubelet, kubeconfig) and of container runtime sockets (docker.sock, containerd.sock), extra RBAC bindings for system:nodes or system:node:<name> that bypass NodeRestriction, roles granting impersonate on system:nodes, service-account roles that can create/update/patch/delete nodes or nodes/status, and broad tolerations (operator: Exists with no key) that let untrusted workloads land on control-plane nodes. It recommends ValidatingAdmissionPolicies as the fix for hostPath abuse. It is a sub-skill of review-security-k8s-main and does not state exclusions.
- **S102 review-security-k8s-pod**: Repo-level review skill (run by a contributor or by the review-security-k8s-main orchestrator) that reads Pod specs and their PodSecurityContext/SecurityContext and flags: privileged, host namespaces (hostNetwork/hostPID/hostIPC/hostUsers), hostPath volumes, allowPrivilegeEscalation, root execution, added capabilities, missing capabilities.drop ALL, missing readOnlyRootFilesystem and seccomp, use of the default ServiceAccount, token automounting, Secret-based SA tokens, and images not pinned by digest. Read-only manifest review, cluster-agnostic, single resource type (Pods and pod templates). Does not state exclusions, though it does not cover RBAC, network, or storage settings beyond hostPath.
- **S103 review-security-k8s-rbac**: Repo-level review skill (contributor or review-security-k8s-main orchestrator) that reads Role, ClusterRole, RoleBinding and ClusterRoleBinding manifests and flags: bindings to system:anonymous/unauthenticated/authenticated/masters and system:serviceaccounts groups, cluster-admin grants, write access to system: bindings, escalation paths (bind/escalate/impersonate, writes to rbac.authorization.k8s.io, CSRs, webhooks, CRDs, tokenreviews, namespaces, networkpolicies), wildcards, deletecollection, over-scoped ClusterRoleBindings, self-modification, and access to secrets, pods/exec, pods/portforward, pods/attach, nodes/proxy, ephemeralcontainers and status subresources. Ships resources/gke-rbac.md, a copy of the GKE RBAC best-practices page with kubectl/jq detection commands and the gcloud --no-enable-insecure-binding-system-* flags. Read-only manifest review, single cluster, GKE-flavoured. Does not state exclusions.
- **S104 review-security-k8s-service-accounts**: Repo-level review skill (contributor or review-security-k8s-main orchestrator) that reads ServiceAccount objects and their bindings and flags: RBAC bound to the default ServiceAccount, one ServiceAccount shared by several apps, automountServiceAccountToken not set to false on the ServiceAccount, several workloads mapped to one GCP identity through the iam.gke.io/gcp-service-account Workload Identity annotation, long-lived kubernetes.io/service-account-token Secrets, imagePullSecrets with broad registry access, and ServiceAccounts with bindings but no workloads. Read-only manifest review, single cluster. Does not state exclusions; RBAC rule content and Pod-level security contexts are covered by sibling skills, not here.
- **S105 review-security-k8s-storage**: Repo-level review skill (contributor or review-security-k8s-main orchestrator) that reads StorageClass, PersistentVolume, PersistentVolumeClaim, volume and volumeMount definitions and flags: writable mounts missing readOnly, subPath on user-writable volumes, hostPath use (recommends local PVs), missing fsGroup, ReadWriteMany access mode, StorageClasses without encryption at rest (CMEK or encrypted parameter), Recycle and unmanaged Retain reclaim policies, allowVolumeExpansion without ResourceQuotas, and CSI Secrets Store mounts without strict limits. Read-only manifest review, single cluster, cloud-agnostic. Does not state exclusions.
- **S106 review-security-k8s-understand**: Repo-level context-building skill run first by the review-security-k8s-main and review-security-k8s-agents-main orchestrators (and cited in docs/architecture/03-security-model.md). It reads the target project's README, diagrams and architecture docs, names the main components and workloads, labels each workload Infrastructure (CSI drivers, ingress controllers) or Application (APIs, databases), and records global compensating controls such as a service mesh enforcing mTLS or cluster-wide OPA/Gatekeeper policies. Output is a short summary that the orchestrators use to triage sub-reviewer findings. Read-only, no checks of its own; it explicitly leaves specific security reviews to the specialized skills.
- **S107 skill-review**: Repo-level skill for a contributor reviewing SKILL.md files in this repository. It checks frontmatter (description opens with the user's action and names its object; YAML-safe values), structure (top-level # Task and # Checks or # Workflow sections, terse headers), prose (no persona setup, no filler, imperative bullets starting with Flag/Require/Ensure) and formatting (single-sentence rules, no loss of checks or domain knowledge when shortening). AGENTS.md and .agents/rules/documentation.md point to it as the style owner for SKILL.md files. Read-only review of skill text; it does not cover placement by persona or whether a skill's checks are correct.
- **S108 submit-suggestion**: Lets the Platform Agent propose a declarative configuration change to a managed GitOps repository as a pull request (or GitLab merge request) through a two-step helper: `prepare` clones the repository through the credential broker into a per-branch workspace under /opt/data/scratch and cuts or resumes a `platform-agent/<type>-<target>` branch, and `submit` records uncommitted edits, fast-forward publishes, and opens or refreshes the proposal; it also covers a second round on an open PR (read comments with the version-control skill's `vcs.py proposal view --comments`, edit on the PR's own branch, `--keep-description` or a fresh body, reply via `proposal comment`). It explicitly does not cover fixes of fleet-audit findings (the fleet-audit skill's `remediate` opens and tracks those PRs), diagnosis-only requests that did not ask for a change, and any direct cluster mutation or direct use of the credentialed `git`/`gh`.
- **S109 uninstall-kube-agents**: Lets an agent tear down a kube-agents install from a GCP project or GKE cluster by running the release-pinned uninstall.sh non-interactively, which drives lifecycle.sh destroy in terraform/examples/full-install against the install's Terraform state in GCS. It covers choosing the release-pinned script or --source-ref, how install.env is located, the pre-destroy asymmetries the engine handles (KMS forget, PlatformAgent finalizer, helm uninstall on a non-created cluster, backup purge, deletion protection), exit codes 1 and 3, and the GitLab Secrets a teardown leaves on a kept cluster. It does not cover installing or upgrading, installs made outside the Terraform engine except by hand-over to an older release, or removing namespaces, CRDs or volumes left on a kept cluster beyond pointing to the site page.
- **S110 upgrade-kube-agents**: Lets an agent upgrade an existing kube-agents install (Platform Agent, operator, chart and Terraform-rendered settings) on a GKE cluster by driving the repo's upgrade.sh: the release-pinned one-liner, the release bundle's own copy, or a checkout. It covers the three upgrade modes (full, harness, operator), the offline --dry-run and the state-backed --plan previews, the --image-tag/--keep-image-tag/--drop-undeclared-values targeting flags, and the install.env discovery rules. It does not cover a first install, an uninstall, or installs that predate the Terraform + Helm engine (those are sent to install.sh or to the release that installed them).
- **S111 version-control**: The skill gives the agent `scripts/vcs.py`, a forge-neutral CLI whose remote verbs (`capabilities`, `identity`, `clone`, `publish`, `proposal create|list|view|comment|update|close|commits|acknowledge`, `issue create|list|view|comment|update|close`, `label ensure`, `remote-branch view|delete`) go over loopback to a credential broker in another container, while all local work (`git log`, `git show`, `git blame`, `git grep`, `git diff`, `git status`, `git branch`, `git commit`, or the JSON wrappers `log`, `show`, `annotate`, `files`, `grep`, `diff`, `status`, `branch`, `commit`, `discard`) runs a credential-free, transport-less git against a working copy that `clone` unpacks from a bundle and `publish` sends back as a bundle. It covers repository history and file-mode queries, branching and committing on `platform-agent/` branches, opening pull/merge requests and later rounds (`publish --advance`), configured base branches (`baseBranch`, `TARGET_NOT_BASE`), reading issue queues with `--labels`/`--without-labels`/`--query`, pagination (`--page`, `truncated`, `commentsTruncated`), spent-branch cleanup, building file links from `capabilities` `fileUrl`, and the meaning of every `FORGE_*`/`BRANCH_*`/`BASE_*` refusal code; it names GitHub, GitLab, and Bitbucket as forges the broker may or may not serve. It explicitly does not cover repositories outside the install's managed list or one-off reads of large upstream repositories (that is `inspect-repository`), the GitOps workspaces owned by `fleet-audit` and `submit-suggestion`, and any direct `git push`/`git fetch`/`git clone`/`git remote add` or use of `gh`.
- **S112 workload-rebalancing**: Platform Agent orchestration skill for moving one workload from an overutilized cluster to one with headroom. It resolves each cluster's profile with `get_cluster_profile_name`, fans out two parallel read-only kanban cards (`kanban_create` with no `parents`) asking cluster agents to validate can-host and safe-to-evacuate, polls them with `kanban_show`, and if both are green declares the move as a single GitOps PR via `submit-suggestion` for KCC/Config Sync to reconcile, recording the decision in `kanban_complete` metadata. Fleet-scoped, write only through a PR, never imperative cluster mutation; it explicitly does not cover a trivial single-cluster change (act directly) and tells the agent not to declare when either validation is red.

Pairs at 2 stars or fewer:

- 0 stars: gke-ai-troubleshooting-handle-disruption-gpu-tpu (agents/platform/skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu) and gke-ai-troubleshooting-handle-disruption-gpu-tpu (third_party/google-skills/gke-ai-troubleshooting-handle-disruption-gpu-tpu). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-ai-troubleshooting-jobset-interruption (agents/platform/skills/gke-ai-troubleshooting-jobset-interruption) and gke-ai-troubleshooting-jobset-interruption (third_party/google-skills/gke-ai-troubleshooting-jobset-interruption). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-ai-troubleshooting-tpu-vbar-oom (agents/platform/skills/gke-ai-troubleshooting-tpu-vbar-oom) and gke-ai-troubleshooting-tpu-vbar-oom (third_party/google-skills/gke-ai-troubleshooting-tpu-vbar-oom). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-app-onboarding (agents/platform/skills/gke-app-onboarding) and gke-app-onboarding (third_party/google-skills/gke-app-onboarding). Every file is identical except assets/Dockerfile, where the shipped copy pins node:26-slim and upstream pins node:18-slim; same coverage.
- 0 stars: gke-backup-dr (agents/platform/skills/gke-backup-dr) and gke-backup-dr (third_party/google-skills/gke-backup-dr). Upstream source vs the shipped copy of the same Backup for GKE skill; the bodies read the same, the shipped copy differing only by a three-line overlay (one extra --volume-data-restore-policy flag, a note that gcloud beta is preinstalled and 'gcloud components install' is refused by the credential proxy, and a repaired heading), not an added section.
- 0 stars: gke-cluster-autoscaler (agents/platform/skills/gke-cluster-autoscaler) and gke-cluster-autoscaler (third_party/google-skills/gke-cluster-autoscaler). Upstream source vs the shipped copy of the same skill: the overlay only renames the gke-compute-class reference to gke-compute-classes, adds a '(Standard clusters only)' qualifier to one gcloud line and drops an unused variable in a script; the bodies read the same and no section is added.
- 0 stars: gke-compute-classes (agents/platform/skills/gke-compute-classes) and gke-compute-classes (third_party/google-skills/gke-compute-classes). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-cost-analysis (agents/platform/skills/gke-cost-analysis) and gke-cost-analysis (third_party/google-skills/gke-cost-analysis). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-cost-optimization (agents/platform/skills/gke-cost-optimization) and gke-cost-optimization (third_party/google-skills/gke-cost-optimization). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-golden-path (agents/platform/skills/gke-golden-path) and gke-golden-path (third_party/google-skills/gke-golden-path). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-inference (agents/platform/skills/gke-inference) and gke-inference (third_party/google-skills/gke-inference). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-manifest-generation (agents/platform/skills/gke-manifest-generation) and gke-manifest-generation (third_party/google-skills/gke-manifest-generation). Upstream source vs the shipped copy; the bodies read the same apart from four overlay substitutions (stdout redirect for gcloud, a Config Connector routing sentence, a neutral ServiceAccount name, search_documents before answer_query) and no added section.
- 0 stars: gke-multitenancy (agents/platform/skills/gke-multitenancy) and gke-multitenancy (third_party/google-skills/gke-multitenancy). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-observability (agents/platform/skills/gke-observability) and gke-observability (third_party/google-skills/gke-observability). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-productionize (agents/platform/skills/gke-productionize) and gke-productionize (third_party/google-skills/gke-productionize). Upstream source vs shipped copy; the 142-line bodies are identical except a one-line overlay patch that routes Workload Identity to gke-workload-identity instead of gke-platform-security, no section added.
- 0 stars: gke-reliability (agents/platform/skills/gke-reliability) and gke-reliability (third_party/google-skills/gke-reliability). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-service-networking (agents/platform/skills/gke-service-networking) and gke-service-networking (third_party/google-skills/gke-service-networking). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-storage (agents/platform/skills/gke-storage) and gke-storage (third_party/google-skills/gke-storage). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-tpu-dynamic-slices-monitoring (agents/platform/skills/gke-tpu-dynamic-slices-monitoring) and gke-tpu-dynamic-slices-monitoring (third_party/google-skills/gke-tpu-dynamic-slices-monitoring). Identical content (every file the same; name and provenance ignored).
- 0 stars: gke-tpu-metrics-monitoring (agents/platform/skills/gke-tpu-metrics-monitoring) and gke-tpu-metrics-monitoring (third_party/google-skills/gke-tpu-metrics-monitoring). Identical content (every file the same; name and provenance ignored).
- 1 star: gke-basics (agents/platform/skills/gke-basics) and gke-basics (third_party/google-skills/gke-basics). Upstream source vs shipped copy: the shipped SKILL.md carries two overlay patches that add the per-target KUBECONFIG export under $HERMES_HOME/.kubeconfigs/ to the get-credentials step and rank Developer Knowledge MCP first in the tool hierarchy; otherwise the bodies read the same, so the shipped copy is a superset.
- 1 star: gke-batch-hpc (agents/platform/skills/gke-batch-hpc) and gke-batch-hpc (third_party/google-skills/gke-batch-hpc). Upstream source versus the shipped copy: the bodies are identical except that the shipped copy appends a kube-agents section routing GPU/TPU deadline jobs to capacity-obtainability, so the shipped copy covers everything upstream does and more.
- 1 star: gke-cluster-creation (agents/platform/skills/gke-cluster-creation) and gke-cluster-creation (third_party/google-skills/gke-cluster-creation). The shipped copy is the upstream body verbatim plus three appended local sections (Cluster Agent profile create at creation, profile delete at teardown, and loading capacity-obtainability before recommending GPU/TPU capacity), so the shipped copy is a strict superset.
- 1 star: gke-networking (agents/platform/skills/gke-networking) and gke-networking (third_party/google-skills/gke-networking). Upstream source vs shipped copy: the shipped SKILL.md is the upstream body verbatim plus one appended local section on checking controlPlaneEndpointsConfig before --dns-endpoint and gke_endpoint.py.
- 1 star: gke-observability (agents/cluster/skills/gke-observability) and gke-observability (agents/platform/skills/gke-observability). The cluster copy is a hand-trimmed subset of the platform skill: same audit of loggingConfig/monitoringConfig, Managed Prometheus, control-plane metrics, Dataplane V2 observability, LQL examples, tracing and profiling, with changes expressed as Config Connector proposals instead of gcloud update commands, while the platform skill adds key-metric and alert-threshold tables, node-health metrics, audit-log queries, kubectl top and cost notes.
- 1 star: gke-observability (agents/cluster/skills/gke-observability) and gke-observability (third_party/google-skills/gke-observability). The cluster copy is a hand-trimmed subset of the platform skill: same audit of loggingConfig/monitoringConfig, Managed Prometheus, control-plane metrics, Dataplane V2 observability, LQL examples, tracing and profiling, with changes expressed as Config Connector proposals instead of gcloud update commands, while the platform skill adds key-metric and alert-threshold tables, node-health metrics, audit-log queries, kubectl top and cost notes.
- 1 star: gke-platform-security (agents/platform/skills/gke-platform-security) and gke-platform-security (third_party/google-skills/gke-platform-security). The shipped copy is the upstream body plus a routing patch to gke-workload-identity and an appended section on --database-encryption-key (Cloud KMS) and --security-posture; the upstream copy has neither, so the shipped copy is a strict superset.
- 1 star: gke-reliability (agents/cluster/skills/gke-reliability) and gke-reliability (agents/platform/skills/gke-reliability). The cluster copy is a hand-trimmed subset of the platform SKILL.md: same six workflows (regional check, PDB, probes, SIGTERM, topology spread, maintenance window) while the platform copy adds golden-path defaults, full probe YAML, a preStop hook, hostname spread and a minimum-replica table; the only cluster-side addition is a one-paragraph Config Connector recurringWindow proposal.
- 1 star: gke-reliability (agents/cluster/skills/gke-reliability) and gke-reliability (third_party/google-skills/gke-reliability). The cluster copy is a hand-trimmed subset of the platform SKILL.md: same six workflows (regional check, PDB, probes, SIGTERM, topology spread, maintenance window) while the platform copy adds golden-path defaults, full probe YAML, a preStop hook, hostname spread and a minimum-replica table; the only cluster-side addition is a one-paragraph Config Connector recurringWindow proposal.
- 1 star: gke-storage (agents/cluster/skills/gke-storage) and gke-storage (agents/platform/skills/gke-storage). The platform copy covers everything in the cluster copy (pd-ssd regional StorageClass, CSI driver choice, Filestore RWX PVC, PVC expansion, best practices) and adds the built-in StorageClass table, a GCS FUSE mount manifest, MCP patch tooling and a backup pointer.
- 1 star: gke-storage (agents/cluster/skills/gke-storage) and gke-storage (third_party/google-skills/gke-storage). The platform copy covers everything in the cluster copy (pd-ssd regional StorageClass, CSI driver choice, Filestore RWX PVC, PVC expansion, best practices) and adds the built-in StorageClass table, a GCS FUSE mount manifest, MCP patch tooling and a backup pointer.
- 1 star: gke-upgrades (agents/platform/skills/gke-upgrades) and gke-upgrades (third_party/google-skills/gke-upgrades). The shipped platform copy is the upstream SKILL.md plus five small patches and an appended fleet-upgrade-verification section (diff confirmed), so the platform skill covers everything the third_party copy does and more.
- 1 star: gke-workload-identity (agents/platform/skills/gke-workload-identity) and gke-workload-identity (third_party/google-skills/gke-workload-identity). Upstream source vs the shipped copy: bodies are identical except the shipped copy appends a 'Reads this install withholds' section naming the three commands the Platform Agent's command gate refuses and how to hand them to the user.
- 1 star: gke-workload-scaling (agents/platform/skills/gke-workload-scaling) and gke-workload-scaling (third_party/google-skills/gke-workload-scaling). Diff shows the shipped platform copy is the upstream body byte-for-byte plus one injected footer section (load capacity-obtainability before GPU/TPU or large-shape scale-ups), so upstream is a strict subset.
- 1 star: gke-workload-security (agents/cluster/skills/gke-workload-security) and gke-workload-security (agents/platform/skills/gke-workload-security). The Cluster Agent copy keeps every section of the platform copy (audit script, legacy Workload Identity, DPv2 check plus two-step Calico, default-deny, gVisor, PSS labels, SecretProviderClass, NetworkLogging) rewritten as manifest or Config Connector proposals, and adds Shielded Nodes and a gVisor node pool that the platform copy routes to gke-platform-security.
- 1 star: gke-workload-security (agents/cluster/skills/gke-workload-security) and gke-workload-security (third_party/google-skills/gke-workload-security). The Cluster Agent copy covers every workflow in the upstream copy as read-only proposals and adds the Dataplane V2 check, the ordered two-step Calico enablement, Shielded Nodes and a gVisor node pool; the upstream copy adds nothing the cluster copy lacks.
- 1 star: gke-workload-security (agents/platform/skills/gke-workload-security) and gke-workload-security (third_party/google-skills/gke-workload-security). Upstream source vs the shipped overlay-patched copy: the platform copy adds the Dataplane V2 datapath check, the two-step Calico enable sequence and a legacy-WI pointer to gke-workload-identity; the rest reads the same.
- 1 star: gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting) and gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting). The platform copy is the upstream file plus two patches (a timestamp filter inside the logging query and a step-5 gate that opens a PR only when the request asked for a fix), so it covers everything the third_party copy does and more.
- 1 star: review-security-k8s-agents-main and review-security-k8s-main. Same four-step workflow (take context, launch sub-skills in parallel with the identical JSON findings schema, triage against context, merge), and main launches agents-main as one of its ten sub-skills, so main covers everything agents-main does and more.
- 2 stars: capacity-obtainability and gke-stockout-investigator. Diagnostics A-D (gcloud compute regions describe quota, reservations list, kubectl top, gcloud beta compute advice capacity and capacity-history) and the eight ComputeClass rules A-H are verbatim the same text in both; capacity-obtainability wraps them in typed evidence, Flex-Start and calendar-mode planning for design requests, the stockout investigator wraps them in alert dedup, false-signal checks and a GitOps remediation PR.
- 2 stars: gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) and gke-workload-scaling (agents/platform/skills/gke-workload-scaling). Same HPA/VPA/manual-scaling text and the same two example manifests, rewritten as read-only proposals with Config Connector fields in place of kubectl/gcloud; the Platform copy alone has the VPA rightsizing workflow and the capacity-obtainability footer, the Cluster copy alone has a short Cluster Autoscaler node-pool proposal section.
- 2 stars: gke-workload-scaling (agents/cluster/skills/gke-workload-scaling) and gke-workload-scaling (third_party/google-skills/gke-workload-scaling). The upstream source of the same HPA/VPA/manual-scaling text and example manifests; the Cluster copy rewrites commands as read-only Config Connector proposals and adds a short Cluster Autoscaler section, while upstream alone keeps the kubectl/gcloud commands and the VPA rightsizing workflow.
- 2 stars: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) and gke-workload-troubleshooting (agents/platform/skills/gke-workload-troubleshooting). Both are the same five-step GKE workload diagnostic SOP (pod status, namespace events, logs, endpoints and NetworkPolicies, RCA plus YAML patch); they differ only in step 0 (dry-run fallback vs pod-timestamp heuristic) and in the hand-off (kanban_complete vs reply or GitOps PR).
- 2 stars: gke-workload-troubleshooting (agents/cluster/skills/gke-workload-troubleshooting) and gke-workload-troubleshooting (third_party/google-skills/gke-workload-troubleshooting). Same five-step GKE workload diagnostic SOP with near-identical commands and signature tables; the cluster copy swaps the upstream's unconditional PR step for a kanban_complete hand-off and drops the dry-run mode.
- 2 stars: review-security-k8s-agents-firewall and review-security-k8s-network. Both review NetworkPolicies and service exposure with the same core checks (default-deny egress, 0.0.0.0/0 egress, LoadBalancer/NodePort without ingress NetworkPolicies); network adds Ingress TLS, admin ports and mesh policy while firewall adds the agent-specific metadata-address block, so either could be picked for most NetworkPolicy reviews.
