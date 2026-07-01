# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-01
**Run Time:** 2026-07-01T12:27:32.980134+00:00
**Total URLs Checked:** 152

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 5 |
| MEDIUM Changes | 5 |
| Redirects | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | HIGH | 4.12 | Review and update |
| 2 | connect-to-ai-subprocessor | CRITICAL | 3.8a, 2.7 | Monitor |
| 3 | sensitivity-labels-office-apps | HIGH | None | Review and update |
| 4 | audit-log-activities | MEDIUM | 1.15 | Review optional |
| 5 | overview | HIGH | 2.3 | Review and update |
| 6 | turn-external-sharing-on-or-off | HIGH | None | Review and update |
| 7 | advanced-management | MEDIUM | 1.7, 2.5 | Review optional |
| 8 | site-lifecycle-management | MEDIUM | 1.7 | Review optional |
| 9 | restricted-content-discovery | HIGH | 1.7 | Review and update |
| 10 | content-governance-agent | MEDIUM | 1.7 | Review optional |

---

## HIGH: Control Review Recommended

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**What Changed:**
```diff
--- +++ @@ -120,6 +120,15 @@ Singapore physical addresses
 South Africa physical addresses
 Ukraine physical addresses
+Sensitivity labels
+Preview
+: Rolling out, the sensitivity label setting to
+prevent connected experiences that analyze content
+now prevents all connected experiences in Word, Excel, and PowerPoint for Windows, rather than a subset of these experiences.
+Preview
+: Rolling out, the sensitivity label setting to
+prevent connected experiences that analyze content
+extends to Word, Excel, and PowerPoint across MacOS, iOS, and Android.
 May 2026
 Agent 365
 General availability (GA)

```

---

### 2. Mandatory labeling

**URL:** https://learn.microsoft.com/en-us/purview/sensitivity-labels-office-apps#require-users-to-apply-a-label
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -783,12 +783,14 @@ For more help in specifying PowerShell advanced settings, see
 PowerShell tips for specifying the advanced settings
 .
+Prevent connected experiences that analyze content
+Note
+Support for this setting differs for clients and apps. Identify the minimum versions of Office that support this setting by using the
+capabilities tables
+and the rows
 Prevent some connected experiences that analyze content
-Note
-This setting isn't yet available across all client platforms. Identify the minimum versions of Office that support this setting by using the
-capabilities tables
-and the row
-Prevent connected experiences that analyze content
+and
+Prevent all connected experiences that analyze content
 .
 This configuration isn't available in the Microsoft Purview portal. You must use the PowerShell advanced setting
 BlockContentAnalysisServices
@@ -799,7 +801,9 @@ cmdlet after you've
 connected to Security & Compliance PowerShell
 .
-The setting lets you prevent content in Word, Excel, PowerPoint, and Outlook from being sent to Microsoft for content analysis as a privacy control. However, when it's set, it means that some services won't work as designed, such as data loss prevention policy tips for Outlook, automatic and recommended labeling, and Microsoft 365 Copilot.
+The setting lets you prevent content in Word, Excel, PowerPoint, and Outlook (for
+Prevent all connected experiences that analyze content
+) from being sent to Microsoft for content analysis as a privacy control. However, when it's set, it means that some services won't work as designed, such as data loss prevention policy tips for Outlook, automatic and recommended labeling, and Microsoft 365 Copilot.
 Important
 Although content with the configured sensitivity label will be excluded from Microsoft 365 Copilot in the named Office apps, the content remains available to Microsoft 365 Copilot for other scenarios. For example, in Teams, and in Microsoft 365 Copilot Chat.
 Example Powe
```

---

### 3. Microsoft Agent 365 overview

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/overview
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.3: Control 2.3: Conditional Access Policies for Copilot Workloads
  - File: `controls/pillar-2-security/2.3-conditional-access-policies.md`

**What Changed:**
```diff
--- +++ @@ -42,7 +42,7 @@ Agent management overview
 .
 Secure
-Microsoft Agent 365 delivers endâtoâend protection for every agent by extending Microsoftâs enterpriseâgrade identity, data, and threatâdefense capabilities across your AI ecosystem. Microsoft Entra enforces consistent, riskâbased access controls for users and agents acting on their behalf, while MicrosoftPurview provides deep visibility into data risks with information protection, DLP, and risk safeguards. Microsoft Defender adds continuous threat detection and realâtime protection to block unsafe behaviors and malicious activity. Together, these capabilities ensure agents only access authorized resources, prevent data leakage, and defend against evolving threats. Learn more:
+Microsoft Agent 365 delivers endâtoâend protection for every agent by extending Microsoftâs enterpriseâgrade identity, data, and threatâdefense capabilities across your AI ecosystem. Microsoft Entra enforces consistent, riskâbased access controls for users and agents acting on their behalf, while Microsoft Purview provides deep visibility into data risks with information protection, DLP, and risk safeguards. Microsoft Defender adds continuous threat detection and realâtime protection to block unsafe behaviors and malicious activity. Together, these capabilities ensure agents only access authorized resources, prevent data leakage, and defend against evolving threats. Learn more:
 Use Microsoft Purview to manage data security and compliance
 ,
 Protect your agents in real-time during runtime

```

---

### 4. Manage sharing settings

**URL:** https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off
**Section:** SharePoint Administration
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -52,7 +52,7 @@ Sites
 SharePoint external authentication
 (Microsoft Entra B2B integration not enabled)
-No guest account created*
+No guest account created (see the note following this table)
 Microsoft Entra settings don't apply
 N/A
 (Microsoft Entra B2B always used)
@@ -61,41 +61,43 @@ Microsoft Entra settings apply
 Guest account always created
 Microsoft Entra settings apply
-*A guest account might already exist from another sharing workflow, such as sharing a team, in which case it's used for sharing.
+Note
+A guest account might already exist from another sharing workflow, such as sharing a team, in which case it's used for sharing.
 For information on how to enable or disable Microsoft Entra B2B integration, see
 SharePoint and OneDrive integration with Microsoft Entra B2B
 .
-Video demonstration
-This video shows how the settings on the
+Change organization-level external sharing setting
+In the SharePoint admin center, expand
+Policies
+, and then select
 Sharing
-page in the SharePoint admin center
-affect the sharing options available to users.
-How do I change the organization-level external sharing setting?
-Go to
-Sharing
-in the SharePoint admin center
-, and sign in with an account that has
-admin permissions
-for your organization.
+.
 Under
 External sharing
-, specify your sharing level for SharePoint and OneDrive. The default level for both is
-Anyone
-.
-Note
-The SharePoint setting applies to all site types, including those connected to Microsoft 365 groups and teams. Groups and Teams guest sharing settings also affect connected SharePoint sites.
+, set your sharing level for SharePoint and OneDrive. Keep these points in mind:
+The SharePoint setting applies to all site types, including sites connected to Microsoft 365 groups and teams. Groups and Teams guest sharing settings also affect connected SharePoint sites.
 The OneDrive setting can be more restrictive than the SharePoint setting, but not more permissive.
-This setting is f
```

---

### 5. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -44,7 +44,6 @@ SharePoint Admin Agent
 Content management assessment
 Data Access Governance reports
-Catalog management
 How Restricted Content Discovery works
 Restricted Content Discovery is a site-level setting. When you turn on the setting, Microsoft 365 search systems propagate it so that content from the site doesn't appear in organization-wide discovery experiences.
 Even when Restricted Content Discovery is enabled:
@@ -110,18 +109,6 @@ Check Restricted Content Discovery status for a site
 Open PowerShell as an administrator and run the following command:
 Get-SPOSite -Identity <site-url> | Select RestrictContentOrgWideSearch
-Restricted Content Discovery states
-The following table lists states you might see when you check Restricted Content Discovery status:
-State
-What it means
-RDC applied
-Restricted Content Discovery was successfully applied to the indicated site (or sites). No further action is required.
-RCD was already applied
-Rescricted Content Discovery was already applied to the indicated site (or sites), and no further action is required.
-RDCed site moved site group
-When a site is moved to a different catalog group after Restricted Content Discovery is applied, that site retains its Restricted Content Discovery settings in the new group.
-RCD failed site locked
-Restricted Content Discovery couldn't be applied because the site was locked when the request was submitted. Administrators can look into which sites failed and why.
 Monitor Restricted Content Discovery across your tenant
 Administrators can use PowerShell to generate reports that identify sites where Restricted Content Discovery is enabled.
 Generate a report
@@ -135,17 +122,6 @@ Get-SPORestrictedContentDiscoverabilityReport -Action Download -ReportId <ReportGUID>
 Tip
 If a site is configured for Restricted Content Discovery but continues to appear in search results, allow time for index propagation and review the number of items stored in the site. Large sites can req
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Anthropic as a Microsoft subprocessor
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Classification:** CRITICAL (Deprecation notice)

---

### 2. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

### 3. SharePoint Advanced Management
**URL:** https://learn.microsoft.com/en-us/sharepoint/advanced-management
**Classification:** MEDIUM (General content update)

---

### 4. SharePoint site lifecycle management
**URL:** https://learn.microsoft.com/en-us/sharepoint/site-lifecycle-management
**Classification:** MEDIUM (General content update)

---

### 5. SharePoint Admin Agent (Content Governance Agent)
**URL:** https://learn.microsoft.com/en-us/sharepoint/content-governance-agent
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started | https://learn.microsoft.com/en-us/SharePoint/copilot-in-sharepoint-get-started |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*