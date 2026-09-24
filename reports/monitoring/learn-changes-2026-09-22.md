# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-22
**Run Time:** 2026-09-22T14:15:07.298808+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| HIGH Changes | 2 |
| MEDIUM Changes | 3 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | ...m/en-us/microsoft-365/copilot/cowork/ | MEDIUM | None | Review optional |
| 2 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 3 | get-started | MEDIUM | None | Review optional |
| 4 | cowork-faq | HIGH | None | Review and update |
| 5 | agent-registry | HIGH | 2.14, 4.14, 4.13 | Update portal-walkthrough |
| 6 | connected-platforms | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
**Section:** Copilot Cowork
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 4.15: Control 4.15: Copilot Cowork Governance
  - File: `controls/pillar-4-operations/4.15-copilot-cowork-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -166,7 +166,7 @@ Use Cowork
 Mobile app support
 Cowork is now available on iPhone and Android through the Microsoft 365 Copilot mobile app.
-Get started
+Use Cowork on mobile
 April 2026
 New features
 Feature

```

---

### 2. Agent registry in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Policy callout blocks)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -58,8 +58,8 @@ Description
 Total agents
 The number of agents available in your organization's tenant.
-NOTE
-: Applying filters to the list of agents will not change the
+Note:
+Applying filters to the list of agents doesn't change the
 Total agents
 count.
 Agents without owners
@@ -169,185 +169,65 @@ - Selecting the dashboard pane instantly filters the agent list to display only shared agents missing an owner. This feature allows for quick triage and action.
 Real-time updates
 - The ownerless agent count automatically updates when you hard delete a user from the organization. This feature ensures that the dashboard reflects the current state without requiring manual refreshes.
+Agent risks
+Note
+The updated risk details experience is rolling out gradually. If you see the previous interface, the updated experience hasn't reached your region yet.
+Risk signals in the Agent Registry are a consolidated set of agent-related security detections that give IT administrators a single view of agent risks across their tenant. By bringing signals from multiple security platforms into one place, IT administrators can understand what is flagged without switching between portals or elevating their permissions to different security roles.
+Security platforms detect risk signals when an agent's activities conflict with your organization's security policies. You can share these details with your security team for investigation and remediation.
+Prerequisites for viewing risk signals
+Your tenant must have an E7 or A365 license. To view your subscriptions in the Microsoft 365 admin center, select
+Billing
+>
+Licenses
+>
+Subscriptions
+. For more information, see
+Licensing for agent management
+.
+The Risks column and risk details
+The
+Risks
+column on the
+All agents
+page shows the aggregated count of risk signals for each agent. When you select the count, the
+Risk details
+pane opens. This pane offers a focused, actionable view of the agent's risk signals. It p
```

---

## HIGH: Control Review Recommended

### 1. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -114,14 +114,17 @@ Send your message. Cowork begins processing your request.
 Does Cowork work on mobile devices?
 Yes. You can access Cowork in the following ways:
-On the Microsoft Copilot mobile app for iPhone and Android
+On the Microsoft Copilot mobile app for iOS and Android devices (for example, iPhone, iPad, and Galaxy)
+Learn more about the experience and what's different on mobile in
+Use Cowork on mobile
+.
 Plugins are discoverable and configurable on the mobile app. To find them, select the attach menu (
 +
 ) >
 Skills
 . Plugins are also accessible in the Cowork mobile app if you set it up on your desktop.
 From your browser at
-m365.cloud.microsoft
+copilot.cloud.microsoft
 (desktop)
 On the Microsoft Copilot desktop app for Windows and macOS
 What file types does Cowork support?

```

---

### 2. Microsoft Agent 365 registry sync

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms
**Section:** Agent Governance
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -76,6 +76,9 @@ button.
 Agents from the connected environment synchronize into the agent registry.
 You can configure future synchronizations to occur on a scheduled basis, in a future release.
+For supported platforms, see
+Third-party agent observability with Microsoft Agent 365 (Frontier)
+to learn how to monitor synchronized agent activity and operational health.
 View details after a sync
 Select an existing connection to view sync details and monitor synchronization status.
 Connection details include:
@@ -149,13 +152,44 @@ Google Vertex AI project ID
 : The ID of your Google Vertex AI project.
 Google Vertex AI credentials
-: Secret access key
+: Google Cloud service account key in JSON format. Enter the complete JSON key document in the connection's credential field, from the opening
+{
+to the closing
+}
+, not only the
+private_key
+value.
 Create a new or use an existing service account with the following access to project resources:
 Vertex AI Administrator role or custom role with permissions:
 aiplatform.reasoningEngines.list
 aiplatform.reasoningEngines.get
 aiplatform.reasoningEngines.delete
-Generate a new secret key
+Generate a new service account key in JSON format
+The permissions above cover agent discovery and management. They're sufficient to create the connection and synchronize agents, but they don't grant access to observability telemetry.
+Additional permissions for agent observability
+If you want to collect agent observability data, grant the following roles to the same service account, in addition to the Vertex AI permissions above. Agent 365 reads Vertex AI telemetry from BigQuery and Cloud Monitoring rather than from the Vertex AI API, so Vertex AI access alone isn't sufficient for observability.
+Required role
+Role ID
+Purpose
+BigQuery Data Viewer
+roles/bigquery.dataViewer
+Read exported trace tables.
+BigQuery Job User
+roles/bigquery.jobUser
+Execute queries to retrieve spans; requires
+bigquery.jobs.create
+.
+Monito
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Cowork overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Classification:** MEDIUM (General content update)

---

### 2. What's new in Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
**Classification:** MEDIUM (General content update)

---

### 3. Get started with Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*