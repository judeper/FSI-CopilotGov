# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-01
**Run Time:** 2026-10-01T16:47:07.193684+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 8 |
| HIGH Changes | 1 |
| MEDIUM Changes | 2 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | microsoft-365-copilot-requirements | HIGH | 1.1, 1.9, 2.15, 1.4 | Update portal-walkthrough |
| 3 | ...soft-365-copilot-enablement-resources | MEDIUM | 1.11, 1.12 | Update portal-walkthrough |
| 4 | ...data-foundation-microsoft-365-copilot | HIGH | 1.7 | Update portal-walkthrough |
| 5 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 6 | audit-log-activities | CRITICAL | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 7 | ...-based-billing-manage-copilot-credits | HIGH | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 8 | m365-agents-admin-guide | HIGH | None | Review and update |
| 9 | agent-id | HIGH | 2.3, 2.14, 2.17 | Update portal-walkthrough |

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
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
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
--- +++ @@ -3,7 +3,7 @@ Microsoft Copilot is available in many regions worldwide. However, it might not be accessible in certain markets. Some organizations might gain access through an account support escalation process, but access is subject to approval. For more information, see
 International availability
 .
-Microsoft Copilot Chat and Microsoft Copilot responses and experiences differ by data grounding, integration depth, and licensing:
+Microsoft Copilot Chat and Microsoft Copilot responses and experiences differ by data grounding, integration depth, and licensing.
 However, all experiences are powered by:
 Large language models (LLMs)
 for natural language understanding and generation
@@ -113,7 +113,7 @@ to
 copilot.cloud.microsoft
 . To help ensure users' connections aren't blocked, see
-recommended network configurations for Microsoft Copilot
+Network requirements for Microsoft Copilot
 .
 Declarative agents that are grounded in instructions and public websites are included with Copilot Chat. Access to custom or other agents is pay-as-you-go only.
 To use organizational content with Copilot Chat:
@@ -135,7 +135,7 @@ to
 copilot.cloud.microsoft
 . To help ensure users' connections aren't blocked, see
-recommended network configurations for Microsoft Copilot
+Network requirements for Microsoft Copilot
 .
 In-app features you can use:
 Word: Draft, rewrite, and summarize documents
@@ -216,7 +216,7 @@ to
 copilot.cloud.microsoft
 . To help ensure users' connections aren't blocked, see
-recommended network configurations for Microsoft Copilot
+Network requirements for Microsoft Copilot
 .
 Other resources:
 Major services and features in Microsoft Graph

```

---

### 2. Microsoft 365 Copilot requirements

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
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
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
--- +++ @@ -1,203 +1,204 @@-Microsoft 365 app and network requirements for Microsoft Copilot
-Important
-Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. The primary URL for accessing the updated Copilot app will be
+Microsoft Copilot requirements
+Before you deploy Microsoft Copilot or make Microsoft Copilot Chat available in your organization, review the requirements in this article. Requirements vary based on the Copilot experience and Microsoft 365 app that your users access.
+Note
+Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. The primary URL for accessing the updated Copilot app is changing to
 copilot.cloud.microsoft
 . To help ensure users' connections aren't blocked, see
-Recommended actions
+Network requirements
 (in this article).
+Requirements at a glance
+The following table summarizes requirements for Microsoft Copilot and Microsoft Copilot Chat. For more information about the differences between these experiences, see
+Compare Copilot Chat to Microsoft Copilot
+.
+Category
 Microsoft Copilot
-is an AI-powered productivity tool that integrates with Microsoft 365 Apps. This integration allows users to use Copilot in individual apps, such as Word, PowerPoint, Teams, Excel, Outlook, and more. The Copilot experiences are designed to provide users with an AI assistant in the apps they use every day.
-As a result of this integration, there are some app and network requirements for Microsoft Copilot to integrate with your Microsoft 365 apps. These requirements are nearly identical to the requirements for using Microsoft 365 Apps.
-As part of your
-Microsoft Copilot adoption
-, make sure you configure the app and network requirements that allow the app integration.
-This article lists the Microsoft 365 app and network requirements to use Microsoft Copilot in your Microsoft 365 apps.
-This article applies to:
+(for
```

---

### 3. Microsoft 365 Copilot adoption guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.11: Control 1.11: Organizational Change Management and Adoption Planning
  - File: `controls/pillar-1-readiness/1.11-change-management-adoption.md`
- Control 1.12: Control 1.12: Training and Awareness Program
  - File: `controls/pillar-1-readiness/1.12-training-awareness.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.11/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -44,7 +44,7 @@ Step 3 - Get your Microsoft 365 apps and network ready
 Microsoft Copilot integrates with your Microsoft 365 apps, including Microsoft Teams. To use Microsoft Copilot with your apps, make sure that your Microsoft 365 apps and network meet the requirements, and that your app privacy settings allow Copilot.
 To learn more, see
-Microsoft 365 app and network requirements for Microsoft Copilot
+Microsoft 365 app and service requirements
 .
 Step 4 - Set up Copilot and assign licenses
 In this step, you assign Copilot licenses to your users and can configure some Microsoft Copilot features.

```

---

### 4. Configure secure and governed Copilot foundation

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

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
--- +++ @@ -178,15 +178,11 @@ Microsoft 365 Archive
 to exclude files from Copilot use while preserving them for recordkeeping obligations or discovery
 Next steps
-After completing the steps in this article:
-Use the
+After completing the steps in this article, use the
 Microsoft Purview portal
 and the
 SharePoint Admin Agent
 to view information and run reports on a scheduled basis.
-Educate site owners and users on labeling, sharing, and responsible Copilot use. (See
-Microsoft Copilot data and compliance readiness
-.)
 Was this page helpful?
 Yes
 No

```

---

### 5. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Portal references)

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
--- +++ @@ -45,11 +45,11 @@ Policy rule fails to load
 .
 I'm hitting a limit
-(100,000 files/day, 100 policies, 100 locations, or 4,000,000 files in simulation). See
+(500,000 files/day, 100 policies, 1,000 explicitly selected SharePoint sites, or 20,000,000 files in simulation). See
 How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange
 , and
 Use PowerShell for auto-labeling policies
-when you need to configure more than 100 locations.
+to target up to 50,000 SharePoint sites by using an adaptive scope.
 Auto-labeling isn't available in my region.
 The
 Auto-labeling
@@ -90,10 +90,13 @@ and Office files for Word (.docx), PowerPoint (.pptx), and Excel (.xlsx) are supported.
 These files can be auto-labeled at rest before or after the auto-labeling policies are created. Files can't be auto-labeled if they're part of an open session (the file is open).
 Currently, attachments to list items aren't supported and won't be auto-labeled.
-Maximum of 100,000 automatically labeled files in your tenant per day.
-Maximum of 100 auto-labeling policies per tenant. In the portal, each policy can target up to 100 explicitly included or excluded locations (SharePoint sites or OneDrive individual users or groups). If you keep the default configuration of
+Maximum of 500,000 automatically labeled files in your tenant per day.
+Maximum of 100 auto-labeling policies per tenant. In the portal, each policy can target up to 1,000 explicitly included or excluded SharePoint sites, or up to 100 explicitly included or excluded OneDrive individual users or groups. If you keep the default configuration of
 All
-, this configuration is exempt from the 100 locations maximum.
+, this configuration is exempt from these maximums.
+For SharePoint, an auto-labeling policy can use an adaptive scope to target up to 50,000 sites. For configuration instructions, see
+Use PowerShell for auto-labeling policies
+.
 Existing values for modified, modified by, and the date aren't cha
```

---

### 6. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -2618,6 +2618,15 @@ A case was assigned to a different user or team member
 ChangedCaseAssignment
 Generated when a case is assigned or reassigned to a different user.
+A comment in a case was edited
+UpdatedCommentInCase
+Generated when an existing comment on a case is edited.
+A comment was added to a case
+AddedCommentToCase
+Generated when a comment is added to a case.
+A comment was deleted from a case
+DeletedCommentFromCase
+Generated when a comment is deleted from a case.
 A new case was created in the system
 CreatedCase
 Generated when a user creates a new case. Not logged for cases created by application or service accounts.
@@ -2633,6 +2642,18 @@ Case content was changed
 UpdatedCase
 Generated when a case is updated with changes, such as custom fields, that aren't captured by a more specific operation.
+One or more tags were added to a case
+AddedTagsToCase
+Generated when one or more tags are added to a case.
+One or more tags were removed from a case
+RemovedTagsFromCase
+Generated when one or more tags are removed from a case.
+The classification of a case was changed
+ChangedCaseClassification
+Generated when the classification of a case is changed.
+The closing notes of a case were modified or updated
+ChangedCaseClosingNotes
+Generated when the closing notes of a case are changed.
 The description of a case was modified or updated
 ChangedCaseDescription
 Generated when the description of a case is changed.
@@ -2642,6 +2663,9 @@ The priority level of a case was modified
 ChangedCasePriority
 Generated when the priority of a case is changed.
+The severity of a case was changed
+ChangedCaseSeverity
+Generated when the severity of a case is changed.
 The status of a case was updated
 ChangedCaseStatus
 Generated when the status of a case is changed.

```

---

### 7. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 4.15: Control 4.15: Copilot Cowork Governance
  - File: `controls/pillar-4-operations/4.15-copilot-cowork-governance.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 4.8: Control 4.8: Cost Allocation and License Optimization
  - File: `controls/pillar-4-operations/4.8-cost-allocation.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.9/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.9/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.8/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.8/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.8/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.8/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -60,7 +60,7 @@ node.
 To unlock AI experiences enabled by usage-based billing, select
 Get Started
-. This feature is currently available for Cowork and Work IQ API.
+.
 A side-panel with the title
 Activate the default spending policy for your organization
 opens.
@@ -81,7 +81,7 @@ section, set a monthly limit for users to prevent a single person from spending all available credits. Although this selection is optional, review and set this option for your organization to prevent runaway spending of Copilot Credits by one individual user.
 In the
 Define alerts
-section, select the people who receive email notifications when policy usage reaches the threshold that you specify. You can set the threshold as a credit amount or a percentage. Alert emails begin when usage reaches the specified threshold and continue weekly until the monthly usage period resets or you adjust the spending policy. If you set a monthly credit limit per user, you can also configure a user monthly spend alert. This option appears only when a monthly per-user limit is configured.
+section, select the people who receive email notifications when policy usage reaches the threshold that you specify. You can set the threshold as a credit amount or a percentage. Alert emails begin when usage reaches the specified threshold and continue daily until the monthly usage period resets or you adjust the spending policy. If you set a monthly credit limit per user, you can also configure a user monthly spend alert. This option appears only when a monthly per-user limit is configured.
 Note
 The field prepopulates the logged in administrator email and suggests the administrators that you selected in billing notifications for alerting.
 If a monthly per-user limit is configured, set the user-level notification thresholds. These notifications alert users as they approach their spending limit and can help them manage consumption before access is affected.
@@ -128,7 +128,9 @@ is selected. To target this 
```

---

### 8. Conditional Access for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.3: Control 2.3: Conditional Access Policies for Copilot Workloads
  - File: `controls/pillar-2-security/2.3-conditional-access-policies.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.17/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.17/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.3/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,8 +1,6 @@ Conditional Access for agents
-Conditional Access is an intelligent policy engine that helps organizations control how users and agents access corporate resources. It brings together real-time signals such as user's and agent's context, device, location, and session risk information to determine when to allow, block, or limit access, or require more verification steps.
-Conditional Access for agents requires Microsoft Entra ID P1 or P2 and a Microsoft Agent 365 license for each user. Enforcement of Agent 365 licensing is coming soon. Network controls for agents require Microsoft Entra Internet Access. For more information, see
-What is Microsoft Entra Agent ID
-.
+Conditional Access for agents is an extension of the Conditional Access policy engine that controls how agents access resources protected by Microsoft Entra ID. It brings together real-time signals such as user's and agent's context, device, location, and risk information to determine when to allow, block, or limit access, or require more verification steps.
+Understanding the agent's access pattern helps you target the correct identity. An agent can act on behalf of a signed-in user, use its own agent identity, or use its own agent user account.
 Learn about Conditional Access for agents:
 High-level overview of Conditional Access:
 What is Conditional Access?
@@ -10,23 +8,29 @@ Manage agent identities in your organization
 .
 How to target agent identities in Conditional Access
-Configure policies for autonomous agent access
-How Conditional Access evaluates agent access requests
-To access a corporate resource such as SharePoint file, MCP servers, or Open API services, a user or agent first requests an access token from Microsoft Entra ID.
-When a Conditional Access policy applies, Microsoft Entra ID evaluates the configured policy requirements before issuing the token. If the requirements are satisfied, an access token is issued. The token is then presented to the target resourc
```

---

## HIGH: Control Review Recommended

### 1. M365 Agents admin guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,7 +19,7 @@ Microsoft Copilot Chat is available at no additional cost for all Microsoft Entra account users with a Microsoft 365 or Office 365 subscription. Members of your organization can use agents that are available at no additional cost from the Agent Store. You, as the administrator of your organization, would also need to enable these agents. If your organization requires agents that incorporate your organization's data, you can provide access to
 agents
 that are billed based on metered consumption. For more information about Microsoft Copilot Chat, see
-Minimum requirements and considerations for Microsoft Copilot Chat admins
+Requirements for Microsoft Copilot
 .
 Microsoft Copilot, which includes Microsoft Copilot Chat, requires a Microsoft 365
 Business
@@ -27,8 +27,8 @@ Enterprise
 plan. It includes AI-powered chat grounded in both web-based and work-based data, as well as the capabilities of Microsoft Copilot Chat. In addition, Microsoft Copilot unlocks embedded Copilot features in Word, Excel, Outlook, and Teams. Additionally, your organization can use
 custom agents
-. For more information about deploying Microsoft Copilot, including setting up a Microsoft Copilot rollout plan, see
-Minimum requirements to deploy Microsoft Copilot in your organization
+. For more information, see
+Requirements for Microsoft Copilot
 .
 Each Copilot option offers different capabilities. For a list of these capabilities, see
 Agent capabilities for Microsoft 365 users

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

### 2. Microsoft 365 Copilot adoption guide
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*