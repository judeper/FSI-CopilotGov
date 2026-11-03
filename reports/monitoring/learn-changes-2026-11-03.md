# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-03
**Run Time:** 2026-11-03T17:25:47.457364+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 8 |
| MEDIUM Changes | 8 |
| Redirects | 23 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | sensitivity-labels | MEDIUM | 2.2, 1.5 | Update portal-walkthrough |
| 2 | audit-log-activities | MEDIUM | 2.2, 2.13, 3.1, 1.15 | Update portal-walkthrough |
| 3 | ...m/en-us/microsoft-365/copilot/cowork/ | MEDIUM | 4.15 | Update portal-walkthrough |
| 4 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 5 | get-started | MEDIUM | None | Review optional |
| 6 | cowork-admin-governance | MEDIUM | 4.15 | Update portal-walkthrough |
| 7 | cowork-models | MEDIUM | 4.15 | Update portal-walkthrough |
| 8 | cowork-manage-plugins | MEDIUM | 4.15 | Update portal-walkthrough |
| 9 | cowork-faq | HIGH | 4.15 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Learn about sensitivity labels

**URL:** https://learn.microsoft.com/en-us/purview/sensitivity-labels
**Section:** Information Protection (Sensitivity Labels)
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`

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
--- +++ @@ -234,9 +234,15 @@ All users in the same organization can see the name of a sensitivity label applied to content, even if that label isn't published to them. They don't see sensitivity labels from other organizations.
 When you configure a publishing label policy, you can:
 Choose which users and groups see the labels.
-Labels can be published to any specific user or email-enabled security group, distribution group, or Microsoft 365 group (which can have
+Labels can be published to include or exclude specific users and supported groups. Supported groups include security groups (email-enabled or non-email-enabled), distribution groups, and Microsoft 365 groups. Microsoft 365 groups can also have
 dynamic membership
-) in Microsoft Entra ID.
+.
+Important
+The effect of user and group scoping depends on whether the sensitivity label applies protection:
+Label without protection:
+The publishing policy scope determines which users can see and apply the label.
+Label with protection:
+The publishing policy still determines who can see and apply the label. Access to protected content is also subject to Azure Rights Management. Azure Rights Management doesn't support non-email-enabled security groups or exclusions for protection. Make sure the users and groups that need access are supported and authorized by the protection configuration.
 Specify a default label
 for unlabeled documents and Loop components and pages, emails and meeting invites, new containers (when you've
 enabled sensitivity labels for containers
@@ -246,10 +252,6 @@ Consider using a default label to set a base level of protection settings that you want applied to all your content. However, without user training and other controls, this setting can also result in inaccurate labeling. It's usually not a good idea to select a label that applies encryption as a default label to documents. For example, many organizations need to send and share documents with external users who might not have apps t
```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -1341,6 +1341,12 @@ Created MirroredStorage
 CreatedMirroredStorage
 Generated when a user or service principal creates a Fabric MirroredStorage item, linking an external storage source to a workspace as OneLake shortcuts.
+Created an outbound IP firewall rule for a workspace.
+CreatedOutboundIpFirewallRule
+Created an outbound IP firewall rule for a workspace.
+Created multiple outbound IP firewall rules in a single bulk request for a workspace.
+CreatedOutboundIpFirewallRules
+Created multiple outbound IP firewall rules in a single bulk request for a workspace.
 Created workspace relation
 CreatedWorkspaceRelation
 Created workspace relation.
@@ -1422,6 +1428,9 @@ Logged out of Git provider
 DeletedGitProviderCredentials
 Logged out of Git provider.
+Deleted an outbound IP firewall rule for a workspace.
+DeletedOutboundIpFirewallRule
+Deleted an outbound IP firewall rule for a workspace.
 Microsoft Fabric Audit activity to retrieve FMI bindings
 GetFabricManagedIdentityBindings
 Microsoft Fabric Audit activity to retrieve FMI bindings.
@@ -1518,6 +1527,9 @@ Updated MirroredStorage definition
 UpdatedMirroredStorageDefinition
 Generated when a user or service principal modifies the mirroring scope of an existing MirroredStorage item, changing which external paths are exposed in OneLake.
+Updated an existing outbound IP firewall rule for a workspace.
+UpdatedOutboundIpFirewallRule
+Updated an existing outbound IP firewall rule for a workspace.
 Unassign Warehouse Server Alias
 UnassignWarehouseServerAlias
 A workspace administrator assigned a server alias to a Fabric Warehouse workspace.

```

---

### 3. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
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
--- +++ @@ -55,7 +55,7 @@ Browse your entire Work IQ to pull in the content you need.
 Create SharePoint and OneDrive folders.
 Reorganize your existing files into new or existing folders.
-To learn more, see
+Learn more in
 Edit an existing Office file
 .
 Calendar and meetings
@@ -156,7 +156,7 @@ Learn more in
 Get started with Cowork
 .
-Related content
+Related information
 Use Cowork
 Cowork common questions
 Was this page helpful?

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
--- +++ @@ -2,6 +2,14 @@ This article lists recent features, improvements, and changes in Microsoft Copilot Cowork. Get a full guide to Cowork's capabilities in
 Use Cowork
 .
+November 2026
+New features
+Feature
+Description
+Learn more
+Planner Plugin for Copilot Cowork
+The Planner Plugin connects Planner to Cowork.
+What is the Planner Plugin?
 October 2026
 New features
 Feature
@@ -218,7 +226,7 @@ Calendar timezone display
 Event times show in your local timezone with an abbreviation.
 Calendar and meetings
-Related content
+Related information
 Cowork overview
 Get started with Cowork
 Use Cowork

```

---

### 5. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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
--- +++ @@ -165,7 +165,7 @@ The Microsoft 365 service boundary is the security and data-processing boundary of your Microsoft 365 tenant. Learn more in
 Microsoft Copilot architecture and how it works
 .
-Related content
+Related information
 How access to Copilot Cowork is determined
 Choose a model for Cowork
 Use the local browser with Cowork

```

---

### 6. Copilot Cowork available models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -73,7 +73,7 @@ , only GPT models are supported.
 How model choice affects responses
 Changing the model can affect response speed, response depth, and output style. Some models are optimized for faster drafting, while others spend more time on reasoning and review.
-Cowork shows a model badge in the conversation so you can see which model produced a response.
+Cowork shows a model badge in the conversation so you can learn which model produced a response.
 Set the reasoning effort level to balance quality, speed, and cost
 Not every task needs the same level of power. Reasoning effort levels give you more control over how Cowork balances quality, speed, and cost. The level you select persists across future Cowork tasks until you change it.
 Medium
@@ -99,7 +99,7 @@ We might deploy other AI models for Microsoft Copilot to use that are hosted and operated by Microsoft. These models are governed by the same contractual and data protection commitments already in place, including that no data leaves Microsoft. Learn more about models that can be used by Copilot in
 Understanding AI functionality and models in Microsoft Online Services
 .
-Related content
+Related information
 How access to Copilot Cowork is determined
 Use Cowork
 Manage Cowork for your organization

```

---

### 7. Manage Copilot Cowork plugins

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
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
--- +++ @@ -67,7 +67,7 @@ Deploy agents in Microsoft Copilot
 .
 Control plugin availability
-After you deploy a plugin, you can configure who can see it and how users interact with it.
+After you deploy a plugin, you can configure who can view it and how users interact with it.
 Deployment types and user permissions
 Deployment type
 Who gets the plugin
@@ -102,7 +102,7 @@ Available to all users
 : All licensed Copilot users in your tenant can find and acquire the plugin.
 Available to specific users or groups
-: Only the users or security groups you specify can see the plugin.
+: Only the users or security groups you specify can view the plugin.
 Select
 Block
 : No users in your tenant can access the plugin.
@@ -278,7 +278,7 @@ Learn more about packaging and uploading a plugin to your tenant in
 Build plugins for Copilot Cowork
 .
-Related content
+Related information
 Cowork overview
 Use plugins with Cowork
 Build plugins for Cowork

```

---

### 8. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
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
--- +++ @@ -65,7 +65,7 @@ Yes. Cowork supports plugins from the Microsoft 365 App Store that add skills, connectors, or both. You can browse and install plugins from the
 Browse plugins
 menu. Once acquired, a plugin's included skills appear alongside the built-in skills, and any included connectors become available for your sessions.
-Microsoft's role-based plugins include Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork. See their capabilities and included skills in
+Microsoft's role-based plugins include Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork. Learn about their capabilities and included skills in
 Role-based and industry plugins
 .
 Get step-by-step instructions in
@@ -350,7 +350,7 @@ Can Cowork edit an existing Office file?
 Yes. Cowork can edit existing Word, Excel, and PowerPoint files stored in OneDrive or SharePoint. You can approve edit access for the current task or select
 Always allow
-to let Cowork edit the file without asking again in the current conversation. Cowork updates the shared file in its existing location, and the file's version history remains available if you need an earlier version. For steps, see
+to let Cowork edit the file without asking again in the current conversation. Cowork updates the shared file in its existing location, and the file's version history remains available if you need an earlier version. Find the steps in
 Edit an existing Office file
 .
 Can I download all output files at once?
@@ -414,7 +414,7 @@ Access to use Anthropic models through Microsoft services is limited to the
 regions that Anthropic currently supports
 . There are limited exceptions to these regional restrictions for features in worldwide products and services that constrain access and use of Anthropic models. Cowork isn't an exception, and use and access is currently limited to Anthropic-supported regions.
-Related content
+Related information
 Cowork overvi
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Learn about sensitivity labels
**URL:** https://learn.microsoft.com/en-us/purview/sensitivity-labels
**Classification:** MEDIUM (General content update)

---

### 2. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

### 3. Copilot Cowork overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Classification:** MEDIUM (General content update)

---

### 4. What's new in Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
**Classification:** MEDIUM (General content update)

---

### 5. Get started with Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Classification:** MEDIUM (General content update)

---

### 6. Copilot Cowork admin and governance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Classification:** MEDIUM (General content update)

---

### 7. Copilot Cowork available models
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
**Classification:** MEDIUM (General content update)

---

### 8. Manage Copilot Cowork plugins
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot | https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*