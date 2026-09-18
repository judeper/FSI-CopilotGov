# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-18
**Run Time:** 2026-09-18T13:58:52.079213+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 4 |
| MEDIUM Changes | 2 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4 | Update portal-walkthrough |
| 2 | audit-log-activities | MEDIUM | 3.1, 2.2, 2.13, 1.15 | Update portal-walkthrough |
| 3 | information-barriers | CRITICAL | 2.4 | Update portal-walkthrough |
| 4 | authoring-select-agent-model | HIGH | 4.14, 1.16 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -209,7 +209,7 @@ Cowork
 via
 usage-based billing
-. Cowork carries out tasks across your Microsoft 356 environment on your behalf.
+. Cowork carries out tasks across your Microsoft 365 environment on your behalf.
 You can access Microsoft 365 Copilot (Premium) through:
 https://m365copilot.com/
 Microsoft 365 desktop app

```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1310,9 +1310,9 @@ Automatically bound user credentials to Git
 AutoBoundGitCredentials
 Automatically bound user credentials to Git.
-Branch workspace configuration retrieved
-BranchWorkspaceConfigurationRetrieved
-Branch workspace configuration retrieved.
+Branch workspace admin profile configured
+GitBranchWorkspaceAdminProfileConfigured
+Branch workspace admin profile configured.
 Branch workspace configured
 GitBranchWorkspaceConfigured
 Branch workspace configured.

```

---

### 3. Learn about information barriers

**URL:** https://learn.microsoft.com/en-us/purview/information-barriers
**Section:** Information Barriers
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 2.4: Control 2.4: Information Barriers for Copilot (Chinese Wall)
  - File: `controls/pillar-2-security/2.4-information-barriers.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -50,6 +50,11 @@ two-way communication and collaboration restrictions. For example, a scenario where Marketing can communicate and collaborate with Day Traders, but Day Traders can't communicate and collaborate with Marketing
 isn't supported
 .
+Important
+Information barrier (IB) policies can't restrict communication and collaboration between groups and users in email messages including Exchange Online.
+If your organization needs to define and control email communications, consider using
+Exchange mail flow rules
+.
 Information Barriers and Microsoft Teams
 In Microsoft Teams, IB policies determine and prevent the following kinds of unauthorized communication and collaboration:
 Searching for a user
@@ -89,8 +94,10 @@ Policy behavior
 When IB policy administrators create a new policy or modify an existing policy, users can still access existing plans shared with them or already assigned tasks. For any subsequent plan sharing or task assignment, an IB policy check is triggered and collaboration is permitted or restricted as defined by the policy.
 Information Barriers and Exchange Online
-Information barrier (IB) policies can't restrict communication and collaboration between groups and users in email messages. Only Exchange Online deployments currently support IB policies. If your organization needs to define and control email communications, consider using
+Information barrier (IB) policies can't restrict communication and collaboration between groups and users in email messages. If your organization needs to define and control email communications, consider using
 Exchange mail flow rules
+.
+Enabling Information Barriers in environments without configured ABPs can result in the loss of Address List visibility between all users
 .
 The following table summarizes the key differences between IB modes for Exchange Online Address Book Policies (ABPs):
 Feature
@@ -115,9 +122,14 @@ If your organization uses
 single
 or
-multisegment
+multi-segment
 mode
-
```

---

### 4. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -49,7 +49,7 @@ list of models
 in Copilot Studio.
 The following tables show the availability status of selected models across regions and special scopes.
-Public availability
+Standard harness availability
 Model
 Tag/Category
 Asia
@@ -230,21 +230,6 @@ GA (cross-geo)
 GA (cross-geo)
 GA
-Claude Sonnet 5*
-General
-GA (cross-geo)
--
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
--
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (early access environment)
 Claude Opus 4.6
 Deep
 GA (cross-geo)
@@ -305,9 +290,6 @@ Experimental (cross-geo)
 Experimental (cross-geo)
 Experimental (cross-geo)
-* Claude Sonnet 5 is available only in
-agents powered by the GitHub Copilot harness
-.
 Note
 Models marked as
 cross-geo

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

### 2. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*