# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-18
**Run Time:** 2026-08-18T10:18:17.972395+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| HIGH Changes | 2 |
| MEDIUM Changes | 3 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 2 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | None | Review and update |
| 3 | get-started | MEDIUM | None | Review optional |
| 4 | cowork-models | MEDIUM | 4.15 | Update portal-walkthrough |
| 5 | cowork-faq | MEDIUM | None | Review optional |
| 6 | ...ication-fundamentals-publish-channels | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
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
--- +++ @@ -1301,6 +1301,9 @@ Friendly name
 Operation
 Description
+Applied a PostgreSQL database schema
+PgSchemaApplied
+Generated when a user applies (plans and executes) a PostgreSQL database schema through the custom PG schema service (pgschema-based ALM flow). The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
 Assign Warehouse Server Alias
 AssignWarehouseServerAlias
 A workspace administrator assigned a server alias to a Fabric Warehouse workspace.
@@ -1313,9 +1316,21 @@ Branch workspace configured
 GitBranchWorkspaceConfigured
 Branch workspace configured.
+Automatically bound user credentials to Git
+AutoBoundGitCredentials
+Automatically bound user credentials to Git.
+Branch workspace configuration retrieved
+BranchWorkspaceConfigurationRetrieved
+Branch workspace configuration retrieved.
+Branch workspace configured
+GitBranchWorkspaceConfigured
+Branch workspace configured.
 Branched out to a workspace in Git
 GitBranchedOut
 Branched out to a workspace in Git.
+Browsed PostgreSQL database objects
+PgSQLDbObjectExplorered
+Generated when a user browses PostgreSQL database schema objects through Object Explorer. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
 Cancelled a Digital Operations Ontology Agent conversation
 DigitalOperationsOntologyAgentConversationCancelled
 A user canceled a Digital Operations Ontology Agent conversation.
@@ -1361,12 +1376,27 @@ Edited Power BI semantic model options
 EditedSemanticModelOptions
 A user made a change to their semantic model options. This occurs when changes are made in the model options dialog.
+Executed a PostgreSQL database query
+QueryExecuted
+Generated when a user executes a SQL query against a Fabric Native PostgreSQL database. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
 Executed a tenant relocation
 TenantRelocationExecuted
 Execute
```

---

### 2. Copilot Cowork available models

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -99,19 +99,6 @@ Learn about organization-wide Cowork settings in
 Manage Cowork for your organization
 .
-Set the effort level to balance quality, speed, and cost
-Not every task needs the same level of power. Effort levels give you more control over how Cowork balances quality, speed, and cost.
-Medium
-is the default, which gives you a strong balance for everyday work. Select
-Light
-for lighter tasks. Select
-High
-or
-Extra High
-when you need deeper analysis, more complex reasoning, or a more thorough response. You can also select
-Max
-for your hardest work. Higher effort gives Cowork more room to work through the task, but takes longer and uses your limits faster.
-The model and effort controls are in the compose box, where your work begins. Choose your model, set the effort, and get working.
 Related content
 Use Cowork
 Manage Cowork for your organization

```

---

## HIGH: Control Review Recommended

### 1. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -46,6 +46,14 @@ Schedules prompts
 : Runs prompts on a schedule so recurring tasks happen automatically.
 Cowork shows each step in your session, so you can follow along as it works.
+Note
+Cowork is available in two versions. Both versions contain similar features.
+Cowork for work or school accounts
+is generally available. The articles here in the Microsoft 365 Copilot Hub focus on this version.
+Cowork for personal accounts
+is in preview. Learn more in
+Get started with Cowork
+.
 What can Cowork do for you?
 The following sections describe what you can ask Cowork to do.
 Communication

```

---

### 2. Publish and deploy Copilot Studio agents

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Section:** Copilot Studio
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -103,6 +103,12 @@ Only share the demo website URL with members of your team and other stakeholders to try out the agent. The demo website isn't intended for production use. You shouldn't share this URL with customers.
 Configure channels
 After you publish your agent at least once, add channels so your customers can reach it.
+Note
+Some channels might be unavailable or disabled in your environment. Administrators can control which channels are available for Copilot Studio agents by using
+Agent access channels
+in the Power Platform admin center. Learn more in
+Configure channel publishing and connected agent access (preview)
+.
 To configure channels for your agent:
 On the top menu bar, select
 Channels

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Get started with Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Classification:** MEDIUM (General content update)

---

### 2. Copilot Cowork available models
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
**Classification:** MEDIUM (General content update)

---

### 3. Copilot Cowork FAQ
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new |
| https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models |
| https://learn.microsoft.com/microsoft-365/copilot/discovery-setting-ai-experiences | https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences |
| https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits | https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits |
| https://learn.microsoft.com/microsoft-scout/overview | https://learn.microsoft.com/en-us/microsoft-scout/overview |
| https://learn.microsoft.com/microsoft-scout/get-started | https://learn.microsoft.com/en-us/microsoft-scout/get-started |
| https://learn.microsoft.com/microsoft-scout/admin-access-overview | https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview |
| https://learn.microsoft.com/microsoft-scout/admin-intune-setup | https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup |
| https://learn.microsoft.com/microsoft-scout/manage-group-policy | https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy |
| https://learn.microsoft.com/microsoft-scout/use-microsoft-scout | https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout |
| https://learn.microsoft.com/microsoft-scout/faq | https://learn.microsoft.com/en-us/microsoft-scout/faq |
| https://learn.microsoft.com/microsoft-scout/microsoft-scout-responsible-ai-overview | https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview |
| https://learn.microsoft.com/microsoft-scout/microsoft-scout-responsible-ai-faq | https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq |
| https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms |
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*