# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-31
**Run Time:** 2026-07-31T11:51:53.470728+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | HIGH | 4.12 | Update portal-walkthrough |
| 2 | audit-log-activities | HIGH | 3.1, 1.15 | Update portal-walkthrough |
| 3 | ...-based-billing-manage-copilot-credits | CRITICAL | 4.15 | Update portal-walkthrough |
| 4 | data-connectors-reference | HIGH | 3.1, 4.11 | Update portal-walkthrough |
| 5 | data-access-governance-reports | HIGH | 1.15, 1.14, 1.1, 1.7 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

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
--- +++ @@ -30,6 +30,208 @@ Android
 iOS
 Mac
+July 29, 2026
+Updates released between July 15, 2026, and July 29, 2026.
+Microsoft 365 Copilot
+Surface rich images inline within responses
+[Windows, Web]
+Copilot now displays rich images from files and meetings directly within responses to improve comprehension.
+Details:
+What changed:
+Previously, Copilot responses included text only. Now, it surfaces relevant images inline from files and meetings to provide visual context. This enhancement supports richer content formats while maintaining data security and compliance with Microsoft 365 policies.
+Why:
+Visual information helps users understand complex content faster and reduces the need to switch between apps or documents.
+Try this:
+Ask Copilot a question related to your meeting notes or documents.
+Review the inline images that appear alongside the text response.
+Click images to open the source file or meeting contenvt for more details.
+Why this matters:
+Including images directly in responses helps users grasp information quickly and reduces context switching.
+Business impact:
+Teams can collaborate more effectively by accessing visual content without leaving the Copilot interface.
+Personal impact:
+You save time by seeing relevant images immediately, improving comprehension and decision-making.
+OneNote
+Redesign Overview experience in Copilot notebooks in OneNote
+[Windows, Mac, Web]
+The Copilot Notebooks Overview now provides a redesigned experience for crisper AI-generated summaries, key insights, and one-click artifacts to move work forward in the notebook.
+Details:
+What changed:
+The Notebook Overview experience has been redesigned with a better layout and direct visibility of meaningful artifacts users can create in the notebook in one click.
+Why:
+This redesign helps users quickly grasp notebook context and take relevant actions without spending time on manual content review.
+Try this:
+Open a Copilot Notebook and navigate to the Overview Pa
```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

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
--- +++ @@ -59,6 +59,9 @@ Made AI inference call
 AIInferenceCall
 AI agent leveraged an AI model to produce an answer or determine next steps.
+Applied AI guardrail
+AIGuardrail
+A guardrail was applied to an AI agent's request or response to enforce safety or compliance policies.
 Application administration activities
 The following table lists application admin activities that Microsoft 365 audit logs when an admin adds or changes an application registered in Microsoft Entra ID. You must register any application that relies on Microsoft Entra ID for authentication in the directory.
 Friendly name

```

---

### 3. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -23,7 +23,7 @@ Feedback
 Summarize this article for me
 Microsoft uses a usage-based billing model that uses Copilot Credits to provide flexible payment options alongside fixed licensing. This model enables organizations to manage and optimize AI service expenses effectively through centralized tools like the Cost management dashboard in the Microsoft 365 admin center.
-The Cost Management dashboard in the Microsoft 365 admin center helps organizations control, monitor, and optimize Copilot Credit spending for AI experiences enabled by usage-based billing. Administrators can allocate credits, set access policies and limits, use prepaid purchase plans or pay-as-you-go billing, and rely on budgets, alerts, and hard caps to track usage, understand cost drivers, and prevent overspending.
+The Cost Management dashboard in the Microsoft 365 admin center helps organizations control, monitor, and optimize Copilot Credit spending for AI experiences enabled by usage-based billing. Administrators can assign spending limits, set access policies and limits, use prepaid purchase plans or pay-as-you-go billing, and rely on budgets, alerts, and hard caps to track usage, understand cost drivers, and prevent overspending.
 Important
 For a list of services managed by usage-based billing method, see
 Services managed by usage-based billing
@@ -104,13 +104,18 @@ Configuration
 tab within the Cost management page is displayed. Copilot consumptive services are now available. You can configure more policies to scope access to specific groups, users, or services.
 Add or edit spending policies
-You can edit the default spending policy or add more spending policies. There's no set maximum number of policies that you can create.
-Set the tenant-level limit for
+In the Microsoft 365 admin center, go to
+Copilot > Cost Management
+. Select the
+Configuration
+tab.
+You can edit the default spending policy or add more spending policies. You can create any number of policies.
+When yo
```

---

### 4. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** HIGH (UI element names)

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
--- +++ @@ -146,7 +146,7 @@ STEP 2 - Deploy the functionApp using DeployToAzure button to create the table, dcr and the associated Azure Function
 IMPORTANT:
 Before deploying the 1Password connector, a custom table needs to be created.
-Option 1 - Azure Resource Manager (ARM) Template
+Option 1 - Azure Resource Manager (ARM) Template:
 This method provides an automated deployment of the 1Password connector using an ARM Tempate.
 Click the
 Deploy to Azure
@@ -177,11 +177,12 @@ 1Password
 The 1Password CCF connector allows the user to ingest 1Password Audit, Signin & ItemUsage events into Microsoft Sentinel.
 Log Analytics table(s):
-|Table|DCR support|Lake-only ingestion|
-|---|---|---|
-|
+Table
+DCR support
+Lake-only ingestion
 OnePasswordEventLogs_CL
-|No|No|
+No
+No
 Data collection rule support:
 Not currently supported
 Prerequisites:
@@ -259,7 +260,7 @@ Stream Name (FortyTwoCrunchAPIProtectionV2):
 <variable value provided at install time>
 Note: Keep these values secure. You will need them to configure your external security system.
-2. Configure your external system to push logs
+2. Configure your external system to push logs:
 Use the following parameters to configure your external security system to send logs to the workspace.
 Configuration Steps
 Access your external security system's configuration interface.
@@ -327,7 +328,7 @@ This is a
 push-based connector - it receives data from the 42Crunch Log Forwarder and does not maintain an active polling connection. The connector shows as Connected
 when data has been received within the last 7 days.
-Uninstall connector
+Uninstall connector:
 Use this PowerShell script to delete the connector instance.
 Delete the Connector Instance
 Run the following PowerShell commands to remove the data connector instance:
@@ -395,7 +396,7 @@ Abnormal Security:
 Active Abnormal Security subscription with access to the SIEM integration settings.
 Setup Instructions:
-1. Deploy Connector Resources
+1. Deploy Connector Re
```

---

### 5. Data access governance reports

**URL:** https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 1.14: Control 1.14: Item-Level Permission Scanning
  - File: `controls/pillar-1-readiness/1.14-item-level-permission-scanning.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -94,8 +94,15 @@ Learn how to create and use the
 site permissions for users report
 .
+What is the sites and files shared via special SharePoint groups report?
+The sites and files shared via special SharePoint groups report is a snapshot report that identifies all sites, folders, and files across SharePoint and OneDrive that are effectively public because of the special SharePoint groups 'Everyone except external users' (EEEU) or 'Everyone'. While the
+site permissions for your organization report
+tells you which sites are overshared, this report tells you exactly which items are overshared and how access was granted, so you can accelerate cleanup through scripting instead of depending on site owners.
+Learn how to run and use the
+sites and files shared via special SharePoint groups report
+.
 What is the sensitivity labels for files report?
-The sensitivity labels for files report is the other snapshot report that helps you control access to sensitive content across your organization. This report identifies sites containing
+The sensitivity labels for files report is another snapshot report that helps you control access to sensitive content across your organization. This report identifies sites containing
 files with sensitivity labels applied
 , allowing you to verify that appropriate security policies are applied.
 Learn how to use the

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
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*