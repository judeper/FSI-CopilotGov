# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-20
**Run Time:** 2026-10-20T14:33:55.549533+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 4 |
| MEDIUM Changes | 1 |
| Redirects | 9 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | HIGH | 4.12 | Update portal-walkthrough |
| 2 | apply-sensitivity-label-automatically | MEDIUM | 1.5, 2.2 | Update portal-walkthrough |
| 3 | audit-log-activities | CRITICAL | 1.15, 3.1, 2.13, 2.2 | Update portal-walkthrough |
| 4 | authoring-select-agent-model | HIGH | 1.16, 4.14 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
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
--- +++ @@ -17,7 +17,7 @@ October 2026
 Data Loss Prevention
 General availability
-: Endpoint data loss prevention (DLP) can now monitor sensitive data transferred over FTP and SFTP from managed Windows devices. It can enforce restrictive actions to help prevent data exfiltration. Configure FTP and SFTP transfer activities in your Endpoint DLP policies to get started. See
+: Endpoint data loss prevention (DLP) can now monitor sensitive data transferred over FTP and SFTP and apply restrictive actions based on your organizationâs requirements. To get started, configure FTP and SFTP transfer activities in your Endpoint DLP policies. See
 Protect FTP and SFTP transfers with Microsoft Purview Endpoint DLP
 .
 September 2026

```

---

### 2. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -45,7 +45,7 @@ Policy rule fails to load
 .
 I'm hitting a limit
-(500,000 files/day, 100 policies, 1,000 explicitly selected SharePoint sites, or 20,000,000 files in simulation). See
+(500,000 files/day, 100 policies, 1,000 explicitly selected SharePoint sites, or 20,000,000 matched files per policy simulation). See
 How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange
 , and
 Use PowerShell for auto-labeling policies
@@ -599,7 +599,7 @@ Items to review
 views can mix auto-labeling and DLP results and can fail to load if either signal is under load. If a view returns an error, retry a few hours later before you open a support case.
 Simulation limits are documented separately.
-The following guidance covers item caps (100 per site displayed, 50,000-record CSV export ceiling, and 20,000,000-item scan limit), the 12-hour target completion time, and stall detection.
+The following guidance covers item caps (100 per site displayed, 50,000-record CSV export ceiling, and 20,000,000 matched files per policy simulation), the 12-hour target completion time, and stall detection.
 Simulation mode supports up to 20,000,000 matched files. If more than this number of files are matched from an auto-labeling policy, you can't turn on the policy to apply the labels. In this case, you must reconfigure the auto-labeling policy so that fewer files are matched, and rerun simulation. This maximum of 20,000,000 matched files applies to simulation mode only and not to an auto-labeling policy that's already turned on to apply sensitivity labels.
 Note
 Simulation results can differ from what happens when the policy is turned on:
@@ -1123,7 +1123,7 @@ to verify that the label was applied automatically. Allow
 60 to 90 minutes for the activity to appear
 . Activity explorer identifies the resulting label and how it was applied, but doesn't identify the specific auto-labeling policy or rule that applied the label to an Exchange message.
-The labeling progr
```

---

### 3. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
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
--- +++ @@ -5387,6 +5387,33 @@ Viewed thread
 ThreadViewed
 User views a message thread.
+Added Community Agent to a community
+AgentAddedToCommunity
+A community admin adds Community Agent to a community.
+Updated Community Agent settings
+AgentSettingsUpdated
+A community admin updates Community Agent settings.
+Removed Community Agent from a community
+AgentRemovedFromCommunity
+A community admin removes Community Agent from a community.
+Added Community Agent grounding source
+AgentGroundingSourceAdded
+A community admin adds a SharePoint or web grounding source to Community Agent.
+Granted Community Agent access to a grounding source
+AgentGroundingSourceAccessGranted
+A community admin grants Community Agent access to a SharePoint grounding source.
+Removed Community Agent grounding source
+AgentGroundingSourceRemoved
+A community admin removes a SharePoint or web grounding source from Community Agent.
+Approved Community Agent suggested answer
+SuggestedAnswerApproved
+A community admin or community expert approves an answer suggested by Community Agent without editing it.
+Edited and approved Community Agent suggested answer
+SuggestedAnswerEditedAndApproved
+A community admin or community expert edits an answer suggested by Community Agent and then approves it.
+Dismissed Community Agent suggested answer
+SuggestedAnswerDismissed
+A community admin or community expert dismisses an answer suggested by Community Agent.
 Viva Glint activities
 The following table lists the user and admin activities in Viva Glint that the Microsoft 365 audit log records. The table includes the friendly name that's displayed in the
 Activities

```

---

### 4. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

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
--- +++ @@ -135,17 +135,17 @@ GPT-5.5 Chat
 General
 GA (cross-geo)
-GA
-GA (cross-geo)
-GA (cross-geo)
-GA
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
 GA
 Claude Sonnet 4.6
 General

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Apply sensitivity labels automatically
**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-setup-assign-licenses |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*