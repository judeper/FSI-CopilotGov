# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-08
**Run Time:** 2026-08-08T10:21:02.794650+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| MEDIUM Changes | 2 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | audit-log-activities | MEDIUM | 3.1, 1.15 | Update portal-walkthrough |
| 2 | ...-based-billing-manage-copilot-credits | MEDIUM | 4.15 | Update portal-walkthrough |
| 3 | manage-federated-connectors | CRITICAL | 2.16 | Update portal-walkthrough |
| 4 | data-connectors-reference | CRITICAL | 3.1, 4.11 | Update portal-walkthrough |
| 5 | monitor-your-data | HIGH | 4.11 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -2774,6 +2774,9 @@ Remove user assignments to role group
 DeletePermissionAsync
 User assignments to an RBAC role group are removed.
+Updated user role assignments expiration in role group
+UpdatePermission
+A user assignment expiration date is updated in an RBAC role group.
 Microsoft Security Copilot agent management
 The following table lists the Agent management operations in Security Copilot that the Microsoft 365 audit log records. These activities characterize activities for agents and the components necessary for them to function such as triggers. For more information about Security Copilot agent management, see
 Microsoft Security Copilot agents overview

```

---

### 2. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
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
--- +++ @@ -353,6 +353,13 @@ Monitoring spending of Copilot Credits
 Overview tab
 This dashboard provides a centralized view of spending patterns, helping administrators identify where credits are used, who consumes them, and how usage trends evolve over time.
+Note
+Users can view their approximate Copilot Credit usage directly in Microsoft Copilot Cowork by entering
+/cost
+. This command shows the approximate cost in credits for the opened task so far, and additional credit usage details. For more information, see
+Check your credit usage for Cowork tasks with
+/cost
+.
 The
 Overview
 tab refreshes every 4 hours.

```

---

### 3. Manage federated connector availability

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/manage-federated-connectors
**Section:** Agent Governance
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 2.16: Control 2.16: Federated Copilot Connector and Model Context Protocol (MCP) Governance
  - File: `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -24,6 +24,12 @@ Summarize this article for me
 Federated connectors for Microsoft 365 Copilot enable users to access information from external data sources directly within their Copilot experience. Microsoft provides default federated connectors that use the Model Context Protocol (MCP) to integrate with popular services and tools. While these connectors enhance Copilot's capabilities by extending its knowledge base, organizations might need to control their availability for security, compliance, or governance reasons.
 As an administrator, you can use PowerShell to manage the availability of all default federated connectors across your tenant. This centralized management approach allows you to quickly disable or enable connectors organization-wide while maintaining visibility and control over individual connector settings.
+Important
+Microsoft is retiring the command-line (CLI) toggle for setFederatedConnectors by
+August 20, 2026
+. The CLI is being deprecated so that connector and agent settings are honored from the same global tenant settings, giving you one consistent place to govern both. Going forward, you can manage the same intent through the 'Allowed agent types' setting in Agent 365. For more information, see
+Allowed agent types
+.
 Manage federated connector availability for your organization
 The federated connector management capability provides a tenant-wide toggle that allows you to:
 Disable all default federated connectors

```

---

### 4. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** CRITICAL (UI navigation steps changed)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -96,47 +96,7 @@ For a list of tables ingested into Microsoft Sentinel and the connectors that ingest them, see
 Microsoft Sentinel tables and associated connectors
 .
-1Password (Serverless)
-Supported by:
 1Password
-The 1Password CCF connector allows the user to ingest 1Password Audit, Signin & ItemUsage events into Microsoft Sentinel.
-Log Analytics table(s)
-:
-Table
-DCR support
-Lake-only ingestion
-OnePasswordEventLogs_CL
-Yes
-Yes
-Data collection rule support:
-Workspace transform DCR
-Prerequisites
-:
-1Password API token
-: A 1Password API Token is required. See the
-1Password documentation
-on how to create an API token.
-Setup Instructions
-:
-STEP 1 - Create a 1Password API token
-:
-Follow the
-1Password documentation
-for guidance on this step.
-STEP 2 - Choose the correct base URL
-:
-There are multiple 1Password servers which might host your events. The correct server depends on your license and region. Follow the
-1Password documentation
-to choose the correct server. Input the base URL as displayed by the documentation (including 'https://' and without a trailing '/').
-STEP 3 - Enter your 1Password Details
-:
-Enter the 1Password base URL & API Token below:
-Base Url
-: (Enter your Base Url)
-API Token
-: (Enter your API Token)
-Enable/Disable Connection
-1Password (using Azure Functions)
 Supported by:
 1Password
 The
@@ -144,14 +104,12 @@ solution for Microsoft Sentinel enables you to ingest sign-in attempts, item usage, and audit events from your 1Password Business account using the
 1Password Events Reporting API
 . This allows you to monitor and investigate events in 1Password in Microsoft Sentinel along with the other applications and services your organization uses.
-Underlying Microsoft Technologies used
-:
+Underlying Microsoft Technologies used:
 This solution depends on the following technologies, and some of which may be in
 Preview
 state or may incur additional ingestion or operational costs:
 Azure Functions
-Log Analyt
```

---

### 5. Create workbooks

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/monitor-your-data
**Section:** Microsoft Sentinel
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -67,7 +67,7 @@ Azure portal
 From the details pane, select
 Save
-, and then select the location where you want to save the workbook. This action creates an Azure resource in the selected location based on the relevant template. Only the workbook's JSON file is saved in this location, and no data.
+, and then select the location where you want to save the workbook. Saving the workbook creates an Azure resource in the selected location based on the relevant template. Only the workbook's JSON file is saved in this location, and no data.
 From the details pane, select
 View saved workbook
 to open it for editing.
@@ -123,7 +123,7 @@ , and then choose one or more workspaces.
 We recommend that your query uses an
 Advanced Security Information Model (ASIM) parser
-and not a built-in table. The query will then support any current or future relevant data source rather than a single data source.
+and not a built-in table. A query that uses an ASIM parser supports any current or future relevant data source rather than a single data source.
 When you're done with your edits, select
 Done editing
 and then
@@ -131,7 +131,7 @@ . In the side pane, enter a meaningful name for your workbook, and select the subscription and resource group for your workspace.
 When working in the Azure portal, switch between workbooks in your workspace by selecting
 Open
-in the toolbar of any workbook. The screen switches to a list of other workbooks you can switch to.
+in the toolbar of any workbook. The workbook view switches to a list of other saved workbooks you can open.
 Select the workbook you want to open:
 Create new tiles for your workbooks
 To add a custom tile to a Microsoft Sentinel workbook, first create the tile in Log Analytics. For more information, see
@@ -155,7 +155,7 @@ Auto refresh intervals are also restarted if you manually refresh your data.
 By default, auto refresh is turned off. If you've turned auto-refresh on, it's turned off again each time you close the not
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

### 2. Manage Copilot Credits (usage-based billing)
**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
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
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*