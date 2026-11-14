# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-14
**Run Time:** 2026-11-14T16:14:51.613742+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 6 |
| MEDIUM Changes | 4 |
| Redirects | 32 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | ...ilot-foundational-deployment-guidance | MEDIUM | 1.2 | Update portal-walkthrough |
| 2 | ...data-foundation-microsoft-365-copilot | MEDIUM | 1.7 | Update portal-walkthrough |
| 3 | sensitivity-labels-office-apps | HIGH | 2.2 | Update portal-walkthrough |
| 4 | audit-log-activities | MEDIUM | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 5 | manage-data-overview | HIGH | 4.11 | Update portal-walkthrough |
| 6 | ...opilot-sharepoint-advanced-management | MEDIUM | 1.13, 1.3 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Secure and Govern Copilot blueprint

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -21,11 +21,10 @@ Deployment model
 Description
 Use this blueprint to remediate oversharing, enforce guardrails, and meet AI regulations for a Microsoft Copilot deployment.
-Includes:
-- Blueprint overview and activities:
-PDF
 -
-PowerPoint
+Download the PowerPoint deck
+-
+Get the PDF version
 Related guidance
 Microsoft Purview blueprint: Secure by default
 Microsoft Purview

```

---

### 2. Configure secure and governed Copilot foundation

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -21,11 +21,10 @@ Deployment model
 Description
 Use this blueprint to remediate oversharing, enforce guardrails, and meet AI regulations for a Microsoft Copilot deployment.
-Includes:
-- Blueprint overview and activities:
-PDF
 -
-PowerPoint
+Download the PowerPoint deck
+-
+Get the PDF version
 Related guidance
 Microsoft Purview blueprint: Secure by default
 Microsoft Purview

```

---

### 3. Mandatory labeling

**URL:** https://learn.microsoft.com/en-us/purview/sensitivity-labels-office-apps#require-users-to-apply-a-label
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -6,7 +6,8 @@ This article helps you successfully manage sensitivity labels in Office apps. For example, you can find additional configuration information for specific labeling features.
 Sensitivity labeling support in apps
 To use sensitivity labels in Office apps, you must use a subscription edition of Office. Use the licensing link at the top of this page to identify eligible plans. Sensitivity labels aren't supported for standalone editions of Office, sometimes called "Office Perpetual".
-For Outlook (Windows, macOS, iOS, Android, and on the web), the mailbox must be hosted in Exchange Online. Sensitivity labels aren't supported for mailboxes that are hosted on-premises. This on-premises limitation also applies to shared mailboxes, even if the users accessing them have mailboxes in Exchange Online.
+For Outlook for Windows, Outlook for iOS and Android, Outlook on the web, and new Outlook for Windows, the mailbox must be hosted in Exchange Online. Sensitivity labels aren't supported for mailboxes that are hosted on-premises.
+For Outlook for Mac, sensitivity labels are supported for on-premises mailboxes starting with version 16.112. For other Outlook clients, the on-premises limitation also applies to shared mailboxes, even if the users accessing them have mailboxes in Exchange Online.
 Support for sensitivity label capabilities in apps
 Use the tables in
 Minimum versions for sensitivity labels in Office apps

```

---

### 4. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
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
--- +++ @@ -3911,13 +3911,13 @@ SiteSensitivityLabelChanged
 A different sensitivity label was applied to a SharePoint site, Teams site that isn't group-connected, or a Loop workspace.
 Failed to apply file sensitivity label
-FileSensitivityLabelAppliedFailed
+FileSensitivityLabelApplyFailed
 A sensitivity label failed to be applied to an item by using Office for the web, the details pane in a SharePoint document library or from the Files tab in Teams, or an auto-labeling policy.
 Failed to change file sensitivity label
-FileSensitivityLabelChangedFailed
+FileSensitivityLabelChangeFailed
 A different sensitivity label failed to be applied to an item using Office for the web, the details pane in a SharePoint document library or from the Files tab in Teams, or an auto-labeling policy.
 Failed to remove file sensitivity label
-FileSensitivityLabelRemovedFailed
+FileSensitivityLabelRemoveFailed
 A sensitivity label failed to be removed from an item by using Office for the web, the details pane in a SharePoint document library or from the Files tab in Teams, or an auto-labeling policy.
 Removed sensitivity label from file
 FileSensitivityLabelRemoved
@@ -5548,6 +5548,9 @@ Executed Data Apps Job
 GlintDataAppsJobRun
 Viva Glint Advanced Configuration Data app and Upload activity.
+Executed user hard delete
+GlintExecutedUserHardDelete
+User hard deletion complete in Viva Glint.
 Exported agentic campaign policy violations
 VivaGlintAgenticPolicyViolationsExported
 Agentic campaign policy violations export activity.
@@ -5635,6 +5638,9 @@ Updated Glint to Insights integration
 GlintToInsightsIntegrationUpdated
 A user updated the configuration for importing Viva Insights data in Viva Glint
+Updated retain data for deleted users setting
+GlintRetainDeletedUserDataSet
+A user updated the configuration for retaining user data after hard deletion.
 Viewed As
 ViewAs
 Admins' "View As" another user activity.

```

---

### 5. Manage data tiers and retention

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview
**Section:** Microsoft Sentinel
**Classification:** HIGH (Compliance features)

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
--- +++ @@ -139,6 +139,9 @@ Note
 You can view Basic Logs tables in your Microsoft Sentinel workspace from the Microsoft Defender portal, but you can currently manage them only from your Log Analytics workspace. To manage these tables from the Microsoft Defender portal, change the table plan from Basic Logs to Analytics in your Microsoft Sentinel workspace.
 How data tiers and retention work
+For regional support, see
+Data lake retention availability
+.
 You can retain data in Microsoft Sentinel in one of two tiers:
 Analytics tier
 : This tier makes data available for alerting, hunting, workbooks, and all Microsoft Sentinel features. It retains data in two states:

```

---

### 6. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -21,11 +21,10 @@ Deployment model
 Description
 Use this blueprint to remediate oversharing, enforce guardrails, and meet AI regulations for a Microsoft Copilot deployment.
-Includes:
-- Blueprint overview and activities:
-PDF
 -
-PowerPoint
+Download the PowerPoint deck
+-
+Get the PDF version
 Related guidance
 Microsoft Purview blueprint: Secure by default
 Microsoft Purview

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Secure and Govern Copilot blueprint
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance
**Classification:** MEDIUM (General content update)

---

### 2. Configure secure and governed Copilot foundation
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
**Classification:** MEDIUM (General content update)

---

### 3. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

### 4. Get ready for Copilot with SharePoint Advanced Management
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/copilot/plan/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access | https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/copilot/plan/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy | https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access | https://learn.microsoft.com/en-us/copilot/implement/copilot-ai-provider-user-sec-group-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences | https://learn.microsoft.com/en-us/copilot/implement/discovery-setting-ai-experiences |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits | https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide | https://learn.microsoft.com/en-us/copilot/manage/copilot-tuning-admin-guide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*