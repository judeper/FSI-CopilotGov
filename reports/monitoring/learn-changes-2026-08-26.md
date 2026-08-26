# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-26
**Run Time:** 2026-08-26T10:24:21.782743+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | HIGH | 4.12 | Update portal-walkthrough |
| 2 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -30,6 +30,397 @@ Android
 iOS
 Mac
+August 25, 2026
+Updates released between August 11, 2026, and August 25, 2026.
+Excel
+Use Python when Editing with Copilot in Excel
+[Windows, Mac, Web]
+Edit with Copilot helps you work with Python in Excel by executing Python code for advanced analysis, automation, and data transformation with results outputted directly in your workbook.
+Details:
+What changed:
+You can now use Edit with Copilot to perform advanced data analysis (statistics, simulations, advanced visualizations etc.) with your workbook data. Existing security and execution controls continue to help manage how code runs.
+Why:
+Python is widely used for data analysis, visualization, and automation. Bringing Copilot-assisted Python editing into Excel helps users move from intent to working analysis faster without switching tools.
+Try this:
+Open an Excel workbook with data you want to analyze.
+Open Edit with Copilot.
+Ask Copilot to complete a task like summarizing trends, cleaning data, or creating a visualization with Python.
+Review the output and inspect the results in Excel.
+Why this matters:
+This makes advanced analysis more approachable by pairing Pythonâs flexibility with Copilotâs assistance and Excelâs familiar workspace.
+Business impact:
+Teams can accelerate reporting, analysis, and repeatable data workflows in Excel, helping reduce manual effort and improve consistency.
+Personal impact:
+You can complete more advanced data tasks in Excel with Copilotâs help.
+Microsoft 365 admin center
+Organizational Messages now supports Hybrid-joined Devices
+[Web]
+Organizational Messages now supports Hybrid-joined Devices.
+Roadmap ID:
+503564
+Details:
+What changed:
+Previously, Organizational Messages were limited to devices fully joined to Azure Active Directory or on-premises Active Directory. Now, hybrid Azure AD joined devices can receive Organizational Messages, expanding device coverage. This update improves message delivery c
```

---

### 2. Audit log activities

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
--- +++ @@ -1316,15 +1316,6 @@ Branch workspace configured
 GitBranchWorkspaceConfigured
 Branch workspace configured.
-Automatically bound user credentials to Git
-AutoBoundGitCredentials
-Automatically bound user credentials to Git.
-Branch workspace configuration retrieved
-BranchWorkspaceConfigurationRetrieved
-Branch workspace configuration retrieved.
-Branch workspace configured
-GitBranchWorkspaceConfigured
-Branch workspace configured.
 Branched out to a workspace in Git
 GitBranchedOut
 Branched out to a workspace in Git.
@@ -1379,15 +1370,6 @@ Executed a tenant relocation
 TenantRelocationExecuted
 Executed tenant relocation.
-Export item definitions
-ExportItemDefinitions
-Export multiple item definitions from a workspace.
-Exported a PostgreSQL database schema
-PgSchemaExported
-Generated when a user dumps a PostgreSQL database schema through the custom PG schema service (pgschema-based ALM flow). The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
-Get Items Sizes
-GetItemsSize
-Retrieved cached item sizes for the OneLake item-size report.
 Export item definitions
 ExportItemDefinitions
 Export multiple item definitions from a workspace.

```

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