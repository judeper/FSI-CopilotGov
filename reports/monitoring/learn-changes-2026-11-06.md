# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-06
**Run Time:** 2026-11-06T17:01:14.404506+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 7 |
| MEDIUM Changes | 3 |
| Redirects | 32 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | audit-log-activities | HIGH | 2.2, 2.13, 3.1, 1.15 | Update portal-walkthrough |
| 3 | create-retention-policies | CRITICAL | 3.2 | Update portal-walkthrough |
| 4 | whats-new | HIGH | 4.15 | Update portal-walkthrough |
| 5 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 6 | cowork-faq | MEDIUM | 4.15 | Update portal-walkthrough |
| 7 | .../microsoft-365/copilot/extensibility/ | MEDIUM | 2.16, 4.13 | Update portal-walkthrough |
| 8 | agents-are-apps | MEDIUM | None | Review optional |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (UI element names)

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
--- +++ @@ -17,12 +17,22 @@ )
 Access scoped by user permissions (security and compliance enforced)
 Note
+The
+Home
+tab provides a unified starting point for Chat and Cowork in the Copilot app. Users can switch between Chat and Cowork from either the
+left navigation or the prompt box
+. Cowork and Code require a
+Microsoft 365 Copilot license
+and an
+assigned usage-based billing policy
+.
+Compare Microsoft 365 Copilot licenses
+Note
 Anthropic subprocessors are available only in applicable Microsoft 365 licensed experiences and aren't available to all users by default. Anthropic operates with
 Microsoft Enterprise data protections
 . For more information, see
 Claude models from Anthropic in Microsoft Online Services
 .
-Compare Microsoft 365 Copilot licenses
 Copilot Chat (Basic) license
 Microsoft 365 Copilot (Basic) license
 Microsoft 365 Copilot (Premium) license

```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
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
--- +++ @@ -1401,6 +1401,9 @@ Get connection by tenant admin
 GetGatewayClusterDatasourceAsAdmin
 A tenant admin retrieved the connection details.
+When tenant admin tests the connection status.
+GetGatewayClusterDatasourceStatusAsAdmin
+When tenant admin tests the connection status.
 Get on-demand billing limits
 GetOnDemandBillingLimits
 Generated when a capacity admin opens the On-demand billing page and the current billing categories and their 24-hour compute limits are returned for a Fabric capacity.

```

---

### 3. Create and configure retention policies

**URL:** https://learn.microsoft.com/en-us/purview/create-retention-policies
**Section:** Audit and Retention
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 3.2: Control 3.2: Data Retention Policies for Copilot Interactions
  - File: `controls/pillar-3-compliance/3.2-data-retention-policies.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/3.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -387,9 +387,15 @@ Separate an existing 'Teams chats and Copilot interactions' policy
 Previously, retention policies used the location
 Teams chats and Copilot interactions
-that combined Teams chat and Copilot interactions. There are now separate retention locations for Teams chat and Copilot interactions.
-You can separate Teams chats from Copilot interactions from an existing retention policy.
-You can create new retention policies for just Teams chats, or for just Copilot interactions.
+that combined Teams chat and Copilot interactions. Beginning 15th January, 2027, Microsoft Purview will treat 'Teams chats and Copilot interactions" policy as
+Teams-only policies
+. After this change is applied to your organization:
+Microsoft 365 Copilot interactions will no longer be retained or deleted through these legacy Teams policies.
+This change applies to both previously retained Copilot interactions and new Copilot interactions.
+Retention behavior for Microsoft Teams content will remain unchanged.
+Create a new retention policy explicitly configured for Copilot by selecting
+"Microsoft Copilot Experiences"
+location to maintain the required retention coverage for Copilot interactions.
 Use the following PowerShell commands to separate an existing retention policy for
 Teams chats and Copilot interactions
 :
@@ -405,15 +411,11 @@ newer locations
 , such as Teams private channel messages and Viva Engage:
 Set-AppRetentionCompliancePolicy -Identity â<policy name>â -Applications "User:M365Copilot"
-For new retention policies, select the new locations, such as
-Teams chat
-or
-Microsoft Copilot Experiences
-.
-Note
-If you have existing retention policies for
-Teams chats and Copilot interactions
-, they continue to be supported, although they can't be edited when your tenant supports the separate locations. At this point, any new retention policies must use the new locations.
+Please note that doing a Get command on 'Teams chats and Copilot interactions' p
```

---

### 4. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -63,7 +63,7 @@ Learn more
 App skill (Frontier)
 Create lightweight, interactive apps from a description without writing code. Refine your app in chat, open it, publish it, and share it with people in your organization.
-Build apps with the App skill
+Build apps in Copilot Cowork (preview)
 Claude Fable 5.1 model
 Fable 5.1 is now available in the model selector as the most advanced model for ambitious work, replacing Fable 5.
 Choose a model for Cowork

```

---

### 5. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -107,13 +107,13 @@ Cowork can complete web tasks for users in Microsoft Edge on their device, using their existing sign-ins and your organization's policies. Because the browser tab runs on the user's machine, browser tasks inherit the same conditional access, DLP, and tenant browsing policies you already apply to your users.
 As an admin, you control:
 Whether browser use is available to users
-âThe
+: The
 Cowork Browsing
 tenant setting in the Microsoft 365 admin center turns the capability on or off for your organization.
 Which sites users can reach through Cowork
-âCowork respects any allowlist, blocklist, and view-only policies your organization applies to web browsing in Microsoft Edge.
+: Cowork respects any allowlist, blocklist, and view-only policies your organization applies to web browsing in Microsoft Edge.
 Audit visibility
-âEach browser task Cowork starts on behalf of a user is recorded in the unified audit log alongside other Cowork activity.
+: Each browser task Cowork starts on behalf of a user is recorded in the unified audit log alongside other Cowork activity.
 Learn about
 admin
 browser controls in
@@ -129,25 +129,29 @@ Microsoft 365 pay-as-you-go services
 .
 Learn more about usage-based billing in the following links:
-Set up and configure usage-based billing
-Understand how Copilot Credits are consumed and managed
-Set up Copilot Credits
-Estimate costs in the Cowork cost estimator
-Gain visibility into how users engage with Cowork in the Cowork Usage report
-Understand how Cowork is being used and where it provides value
-How to use the Consumption Dashboard in InsightsâCowork page
+Copilot Credits Guide
+Managing AI experiences enabled by usage-based billing
+Estimate costs in the
+Copilot Credit Estimator
+Gain visibility into how users engage with Cowork in the
+Copilot Cowork usage
+dashboard
+Understand how Cowork is being used and where it provides value by using the
+Value tab
+How to use the Consumption Dashboa
```

---

### 6. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
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
--- +++ @@ -1,5 +1,9 @@ Copilot Cowork common questions
-Find answers to common questions about Microsoft Copilot Cowork.
+Find answers to common questions about Microsoft Copilot Cowork in this article.
+Tip
+Find questions and answers specifically for building an app in
+FAQ for building apps with Cowork
+.
 What is Cowork?
 Cowork is available in Microsoft Copilot. It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multistep tasks across your Microsoft 365 environment.
 What can Cowork do for me?

```

---

### 7. Copilot extensibility overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.16: Control 2.16: Federated Copilot Connector and Model Context Protocol (MCP) Governance
  - File: `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -9,10 +9,12 @@ How-To Guide
 Build or reuse capabilities
 Package and test
+Build a plugin with Work IQ Dev Tools (GitHub)
 Validate and test your plugin
 Publish and make plugins available
 How-To Guide
 Publish or share
+Configure plugin CI/CD with Work IQ Dev Tools
 Make available and govern
 Monitor, update, and retire plugins
 How-To Guide

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Cowork FAQ
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Classification:** MEDIUM (General content update)

---

### 2. Copilot extensibility overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Classification:** MEDIUM (General content update)

---

### 3. Microsoft 365 Copilot agent governance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps
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