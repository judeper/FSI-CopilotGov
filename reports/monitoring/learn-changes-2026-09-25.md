# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-25
**Run Time:** 2026-09-25T14:51:43.125057+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 4 |
| HIGH Changes | 3 |
| MEDIUM Changes | 3 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | HIGH | 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | release-notes | CRITICAL | 4.12, 3.8a | Update portal-walkthrough |
| 3 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 4 | ...m/en-us/microsoft-365/copilot/cowork/ | MEDIUM | None | Review optional |
| 5 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 6 | cowork-faq | HIGH | None | Review and update |
| 7 | ...t.com/en-us/microsoft-copilot-studio/ | HIGH | None | Review and update |
| 8 | ...ication-fundamentals-publish-channels | HIGH | None | Review and update |
| 9 | copilot-in-sharepoint-get-started | CRITICAL | None | Monitor |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.9/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.9/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -22,6 +22,12 @@ Microsoft 365 app and network requirements for Microsoft Copilot
 Feedback
 Summarize this article for me
+Important
+Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. The primary URL for accessing the updated Copilot app will be
+copilot.cloud.microsoft
+. To help ensure users' connections aren't blocked, see
+Recommended actions
+(in this article).
 Microsoft Copilot
 is an AI-powered productivity tool that integrates with Microsoft 365 Apps. This integration allows users to use Copilot in individual apps, such as Word, PowerPoint, Teams, Excel, Outlook, and more. The Copilot experiences are designed to provide users with an AI assistant in the apps they use every day.
 As a result of this integration, there are some app and network requirements for Microsoft Copilot to integrate with your Microsoft 365 apps. These requirements are nearly identical to the requirements for using Microsoft 365 Apps.
@@ -42,7 +48,7 @@ accounts. You can add or sync users by using the
 onboarding wizard in the Microsoft 365 admin center
 .
-Microsoft Copilot supports primary mailboxes that are hosted on Exchange Online. It is also available on users' archive mailboxes and shared and delegate mailboxes that they have access to.
+Microsoft Copilot supports primary mailboxes that are hosted on Exchange Online. It's also available on users' archive mailboxes and shared and delegate mailboxes that they have access to.
 Note
 Chat experiences in Word, Excel, and PowerPoint vary depending on your tenant configuration and license. Learn more in
 Microsoft Copilot overview
@@ -129,9 +135,32 @@ network connections and endpoints that Microsoft 365 apps
 use.
 Baseline network configuration customers should:
-Ensure that their environment doesn't block the Microsoft 365 endpoints listed in this section.
+Ensure that their environment doesn't block the Microsoft 365 endpoints listed in the section,
+N
```

---

### 2. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -30,6 +30,557 @@ Android
 iOS
 Mac
+September 23, 2026
+Updates released between August 26, 2026, and September 22, 2026.
+Excel
+Navigate to your workbook changes directly from the Copilot chat pane response
+[Windows, Web, Mac]
+In Copilot in Excel, the response contains links to highlight where changes are made in your workbook. Navigate directly to new sheets, tables, ranges, and objects like charts and shapes.
+Details:
+What changed:
+In the Copilot chat response, there now is a link you can click that will take you directly to changes in the workbook. Previously, you would need to locate the change in the response and navigate in the sheet on your own.
+Why:
+We want you to understand where copilot made edits and connect you to them directly from the chat response. This will help build confidence in the changes and allow you to review while you're reading the response in the chat pane.
+Try this:
+Send a prompt to Copilot where the workbook is modified.
+The chat response will show the changes in a different format with a highlight to indicate a link you can click for navigation. New Sheets, tables, ranges, and objects will be highlighted.
+Why this matters:
+The feature allows quick review of document changes made by Copilot, increasing transparency of the edits.
+Business impact:
+Teams can understand changes made while reading the response from Copilot and quickly navigate to those places for review.
+Personal impact:
+You can review the Copilot Edits in your document.
+See Copilot usage in show changes pane
+[Windows, Mac, Web]
+Users can now view Copilot usage details directly within the Show Changes pane in Excel.
+Details:
+What changed:
+Previously, Copilot activity was not visible in the Show Changes pane. Now, the pane includes on-card attribution showing when Copilot made edits or suggestions. This transparency helps users track AI contributions alongside manual changes.
+Why:
+Providing clear visibility into Copilotâs actions increase
```

---

### 3. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

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
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
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
--- +++ @@ -1382,9 +1382,6 @@ Get Items Sizes
 GetItemsSize
 Retrieved cached item sizes for the OneLake item-size report.
-Get OneLake file soft-delete settings
-GetFileSoftDelete
-Generated when a user reads the workspace's OneLake file soft-delete status and retention period.
 Get connection by tenant admin
 GetGatewayClusterDatasourceAsAdmin
 A tenant admin retrieved the connection details.
@@ -1438,7 +1435,7 @@ Modified OneLake default tier.
 Modified OneLake file soft-delete settings
 ModifiedOneLakeFileSoftDeleteSettings
-Generated when a workspace admin enables or disables OneLake file soft delete, or changes the retention period (1â365 days).
+Generated when a workspace admin changes the OneLake file-level soft-delete retention settings (enable/disable, retention period).
 Planning session upgraded
 PlanningSessionUpgraded
 Session type is upgraded in planning workload.

```

---

### 4. What's new in Copilot Cowork

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
--- +++ @@ -46,6 +46,13 @@ Skills
 .
 Cowork common questions
+Enhancements
+Feature
+Description
+Learn more
+Edit existing Office files
+Edit Word, Excel, and PowerPoint files in OneDrive and SharePoint while preserving the shared file and its existing version history.
+Edit an existing Office file
 August 2026
 Enhancements
 Feature

```

---

## HIGH: Control Review Recommended

### 1. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -367,6 +367,12 @@ Files that Cowork creates are saved to your
 OneDrive and SharePoint
 workspace. You can browse them in the side panel during a session or access them directly in OneDrive at any time.
+Can Cowork edit an existing Office file?
+Yes. Cowork can edit existing Word, Excel, and PowerPoint files stored in OneDrive or SharePoint. You can approve edit access for the current task or select
+Always allow
+to let Cowork edit the file without asking again in the current conversation. Cowork updates the shared file in its existing location, and the file's version history remains available if you need an earlier version. For steps, see
+Edit an existing Office file
+.
 Can I download all output files at once?
 Yes. When Cowork produces multiple files, select
 Download All

```

---

### 2. Microsoft Copilot Studio documentation

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,5 +1,5 @@ Microsoft Copilot Studio documentation
-Discover how to build AI-driven agents and workflows with Microsoft Copilot Studio. Access documentation, implementation guidance, online training, and other resources.
+Discover how to build AI-driven agents, workflows, and apps with Microsoft Copilot Studio. Access documentation, implementation guidance, online training, and other resources.
 Overview
 What is Microsoft Copilot Studio?
 What's new
@@ -9,7 +9,7 @@ How-To Guide
 Troubleshoot
 Create
-Create agents and workflows in Microsoft Copilot Studio.
+Create agents, workflows, and apps in Microsoft Copilot Studio.
 Get started
 Choose your harness before you build
 Build in Copilot Studio
@@ -25,6 +25,11 @@ Edit and manage your workflow
 Add an agent node to a workflow
 Add a Copilot node to a workflow
+Apps (preview)
+Apps overview
+Create an app
+Publish and share an app
+Manage data in your app
 Build agents using the GitHub Copilot harness
 Plan and build
 About agents powered by the GitHub Copilot harness

```

---

### 3. Publish and deploy Copilot Studio agents

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -129,6 +129,21 @@ GroupMe
 Direct Line Speech
 Email
+Note
+If your organization has
+blocked a channel due to data policies
+or due to the type of
+authentication configuration
+, you won't be able to select it. Learn more in
+Channels blocked by your organization's policies
+.
+Channels blocked by your organization's policies
+Your organization's governance policies or your agent's configuration might block some channels.
+An unavailable channel appears disabled on the
+Channels
+page. Select the information
+icon next to the channel to see why the channel isn't available.
+Depending on the restriction, you might need to use a different channel, change the applicable configuration, or contact your administrator.
 Channel experience reference table
 Different channels offer different user experiences. The following table shows a high-level overview of the experiences for each channel. Consider the channel experiences when you optimize your agent content for specific channels.
 Experience

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

### 3. Copilot in SharePoint (preview)
**URL:** https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-get-started
**Classification:** CRITICAL (Deprecation notice)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*