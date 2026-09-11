# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-11
**Run Time:** 2026-09-11T13:56:37.292370+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 9 |
| HIGH Changes | 2 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | connect-to-ai-subprocessor | HIGH | 3.8a, 2.7, 1.10 | Update portal-walkthrough |
| 2 | apply-sensitivity-label-automatically | CRITICAL | 2.2, 1.5 | Update portal-walkthrough |
| 3 | audit-log-activities | HIGH | 3.1, 2.2, 2.13, 1.15 | Update portal-walkthrough |
| 4 | cpcn-compliance-summary | HIGH | 2.11 | Update portal-walkthrough |
| 5 | purview-management | HIGH | None | Review and update |
| 6 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 7 | cowork-manage-plugins | HIGH | 4.15 | Update portal-walkthrough |
| 8 | ...-based-billing-manage-copilot-credits | CRITICAL | 4.15 | Update portal-walkthrough |
| 9 | data-connectors-reference | HIGH | 3.1, 4.11 | Update portal-walkthrough |
| 10 | zero-trust-microsoft-365-copilot | HIGH | None | Review and update |
| 11 | archive-overview | HIGH | 3.2 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -32,6 +32,8 @@ Microsoft Data Protection Addendum (DPA)
 apply to the use of Anthropic models through Microsoft's enterprise Online Services. Such use is also covered under our
 Enterprise Data Protection
+. Anthropic models have built-in safeguards, instantiated and operated by Anthropic, to detect illegal content. Anthropic strictly prohibits Child Sexual Abuse Material (CSAM) on its services. For more information about these safeguards, see Anthropicâs
+CSAM Detection and Reporting
 .
 For more information about subprocessor data access, see
 Microsoft Data Access Management

```

---

### 2. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -438,11 +438,6 @@ Azure dependency availability by country
 .
 [ ]
-Your rule includes at least one non-EDM sensitive information type.
-A rule that uses only exact data match (EDM) sensitive information types silently disables auto-labeling on the label. See
-Custom sensitive information types with Exact Data Match
-.
-[ ]
 The label you plan to apply is not a parent label.
 Parent labels (labels that have sublabels) can't be applied to content. If you select one, the policy will run but nothing will be labeled. See
 Don't configure a parent label to be applied automatically or recommended
@@ -571,28 +566,11 @@ configured to apply S/MIME protection
 .
 Scoping a policy with users and groups
-When you scope an auto-labeling policy to specific users or groups instead of
-All
-, the group type you choose and its membership lifecycle both affect whether a newly added user is protected by the policy.
-Supported group types for auto-labeling policy scope:
-Mail-enabled security groups.
-Supported. Static and, in most cases, dynamic membership.
-Distribution groups.
-Supported for Exchange location scoping.
-Microsoft 365 groups.
-Supported.
-Group types that are not supported (or partially supported) as policy targets:
-Mail-disabled security groups.
-Not supported as an auto-labeling policy target. A policy that references one may save but won't evaluate its members. Convert to a mail-enabled security group or list members individually.
-Dynamic distribution groups
-(Exchange dynamic distribution groups, not Entra dynamic-membership groups). Not supported â their membership is resolved at message send time, not at policy configuration time.
-Nested groups.
-Membership expansion depth is limited. Deeply nested memberships (a member of a group that is a member of another group referenced by the policy) may not resolve reliably. Where policy coverage matters, reference the innermost group directly.
-Propagation lag when membership changes.
-When you add a user
```

---

### 3. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
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
--- +++ @@ -1385,6 +1385,12 @@ Get connection by tenant admin
 GetGatewayClusterDatasourceAsAdmin
 A tenant admin retrieved the connection details.
+Get on-demand billing limits
+GetOnDemandBillingLimits
+Generated when a capacity admin opens the On-demand billing page and the current billing categories and their 24-hour compute limits are returned for a Fabric capacity.
+Get on-demand billing quota
+GetOnDemandBillingQuota
+Generated when the On-demand billing experience loads and the subscription-level on-demand billing quota usage and limits are retrieved.
 Git connection settings updated
 GitConnectionSettingsUpdated
 Git connection settings updated.
@@ -1469,6 +1475,9 @@ Switched Git branch
 GitSwitchedBranch
 Switched Git branch for workspace.
+Update on-demand billing limits
+UpdateOnDemandBillingLimits
+Generated when a capacity admin enables or disables a billing category, or changes its 24-hour compute limit, on a Fabric capacity. One audit event is emitted per billing category.
 Updated a Fabric Copilot session
 FabricCopilotSessionUpdated
 A user updated a Fabric Copilot session.

```

---

### 4. Copilot Pages and Notebooks compliance summary

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.11: Control 2.11: Copilot Pages Security and Sharing Controls
  - File: `controls/pillar-2-security/2.11-copilot-pages-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -45,7 +45,7 @@  Supported
 Legal Hold
 â- Supported; selecting the container in the custodian data source picker is rolling out (expected early August)
+ Supported; selecting the container in the custodian data source picker is rolling out (expected October 2026)
 Retention policies
 â  Supported via "All SharePoint Sites"
@@ -178,7 +178,7 @@ .
 When you add a user as a
 custodian
-in Purview eDiscovery, selecting their user-owned SharePoint Embedded container as a data source in the same experience where you select the user's OneDrive and Exchange mailbox is rolling out and expected in early August.
+in Purview eDiscovery, selecting their user-owned SharePoint Embedded container as a data source in the same experience where you select the user's OneDrive and Exchange mailbox is rolling out and expected in October 2026.
 Until then, retrieve the user-owned container URL using PowerShell or the SharePoint admin center, then add it as a data source manually. For instructions, see
 Retrieving the container URL for Purview
 .

```

---

### 5. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Section:** Copilot Cowork
**Classification:** HIGH (Policy language)

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
--- +++ @@ -36,14 +36,13 @@ Cowork
 from the dropdown menu to the right.
 Allow access to Cowork
-To allow users to access Cowork, admins must enable usage-based billing. To learn how to set up and enable usage-based billing, see
+To allow users to access Cowork, admins must enable usage-based billing. Learn how to set up and enable usage-based billing in
 Managing AI experiences enabled by usage-based billing
 .
 Important
-A spending policy is an access control, not only a budget. Any user in the scope of a spending policy that selects Cowork can use Cowork, regardless of how small the credit limit is. A policy with a limit of one credit still grants access. A very low limit doesn't prevent access; users can still open Cowork and start work until the limit is reached. To keep a user out of Cowork, don't include them in any spending policy that selects Cowork, rather than lowering their limit. For how access is determined across policies, discovery, and model settings, see
+A spending policy is an access control, not only a budget. Any user in the scope of a spending policy that selects Cowork can use Cowork, regardless of how small the credit limit is. A policy with a limit of one credit still grants access. A very low limit doesn't prevent access; users can still open Cowork and start work until the limit is reached. To keep a user out of Cowork, don't include them in any spending policy that selects Cowork, rather than lowering their limit. Learn how access is determined across policies, discovery, and model settings in
 How access to Copilot Cowork is determined
 .
-Important
 The agent-based access control from the Frontier and Preview versions is deprecated for access control. Copilot Cowork is generally available and is no longer managed by selecting
 All Agents
 >
@@ -55,6 +54,9 @@ >
 All Agents
 , but any configuration on it has no effect on who can use Cowork. Access is granted only through a spending policy that selects Cowork.
+Learn about Copilot admin
```

---

### 6. Manage Copilot Cowork plugins

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
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
--- +++ @@ -138,7 +138,7 @@ Share
 dialog to make it available to other people. A user can share a plugin with specific users in your organization, or request that it be published to your whole organization. Use the controls in this section to limit that.
 Important
-There's currently no single tenant setting that turns off plugin sharing for every user. Organization-wide sharing requires your approval, and you can block or unpublish any plugin after the fact. A user can still share an uploaded plugin with specific people they choose. If you need user-to-user plugin sharing disabled for your tenant, contact Microsoft Support.
+There's currently no single tenant setting that turns off plugin sharing for every user. Organization-wide sharing requires your approval, and you can block or unpublish any plugin after the fact. A user can still share an uploaded plugin with specific people they choose.
 Org-wide sharing requires admin approval
 When a user requests that a plugin be published to your entire organization, the plugin doesn't go live on its own. The request is held in a pending state, and the plugin only becomes available to your organization after a tenant administrator approves it. If you reject the request, the plugin stays unavailable to everyone else in your tenant.
 This approval step applies to org-wide publication only. It doesn't apply when a user shares a plugin with specific people.

```

---

### 7. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
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
--- +++ @@ -23,7 +23,16 @@ Feedback
 Summarize this article for me
 Microsoft uses a usage-based billing model that uses Copilot Credits to provide flexible payment options alongside fixed licensing. This model enables organizations to manage and optimize AI service expenses effectively through centralized tools like the Cost management dashboard in the Microsoft 365 admin center.
-The Cost Management dashboard in the Microsoft 365 admin center helps organizations control, monitor, and optimize Copilot Credit spending for AI experiences enabled by usage-based billing. Administrators can assign spending limits, set access policies and limits, use prepaid purchase plans or pay-as-you-go billing, and rely on budgets, alerts, and hard caps to track usage, understand cost drivers, and prevent overspending.
+The Cost Management dashboard in the Microsoft 365 admin center helps organizations control, monitor, and optimize Copilot Credit spending for AI experiences enabled by usage-based billing.
+Administrators can:
+Create spending policies that control access to supported agents and services.
+Automatically apply existing spending policies to future supported services and agents.
+Configure organizational and user-level spending limits.
+Configure threshold notifications for administrators and users.
+Use prepaid credits, pay-as-you-go billing, or supported combinations of these billing methods.
+Configure custom approval routing for credit requests.
+Monitor consumption by spending policy, group, user, agent, service, and funding source.
+These controls help organizations understand cost drivers, apply spending safeguards, and manage Copilot Credit consumption at scale.
 Important
 For a list of services managed by usage-based billing method, see
 Services managed by usage-based billing
@@ -31,6 +40,11 @@ To learn more about discovery settings for AI experiences enabled by usage-based billing, see
 Discovery setting for AI experiences enabled by usage-based billing
 .
+
```

---

### 8. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** HIGH (Compliance features)

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
--- +++ @@ -13607,7 +13607,7 @@ Microsoft Copilot
 Supported by:
 Microsoft
-The Microsoft Copilot logs connector in Microsoft Sentinel enables seamless ingestion of Copilot-generated activity logs from M365 Copilot and Security Copilot into Microsoft Sentinel for advanced threat detection, investigation and response. It collects telemetry from Microsoft Copilot services such as usage data and system responses and ingests into Microsoft Sentinel, allowing security teams to monitor for misuse, detect anomalies, and maintain compliance with organizational policies.
+The Microsoft Copilot logs connector in Microsoft Sentinel enables seamless ingestion of Copilot-generated activity logs from Microsoft Copilot and Security Copilot into Microsoft Sentinel for advanced threat detection, investigation and response. It collects telemetry from Microsoft Copilot services such as usage data and system responses and ingests into Microsoft Sentinel, allowing security teams to monitor for misuse, detect anomalies, and maintain compliance with organizational policies.
 Log Analytics table(s):
 Table
 DCR support

```

---

### 9. Microsoft 365 Archive overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide
**Section:** Microsoft 365 Archive
**Classification:** HIGH (Policy language)

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
--- +++ @@ -67,10 +67,10 @@ Sites associated with Teams that use only standard channels are supported for archiving. Sites associated with Teams that include private or shared channels are only partially supported:
 SharePoint admin center: Archiving a site with channel sites is not possible. (Message: "The group connected site with channel sites associated can't be archived.")
 PowerShell and Graph API: Archiving a site with channel sites isn't blocked.
-Only the main site associated to the Team (and its standard channels) is archived. The private and shared channel sites remain active. Archiving the channel sites directly is not possible, as these sites use unsupported site templates.
+Only the main site associated with the Team (and its standard channels) is archived. The private and shared channel sites remain active. Archiving the channel sites directly is not possible, as these sites use unsupported site templates.
 File Archive limitations
-Some Microsoft 365 applications and services don't yet support file-level archiving. These applications might display incorrect error messages, fail to load correctly, or fail actions taken with archived content. Because client support and user awareness for archived files continue to evolve, we recommend that you use file-level archive thoughtfully and ensure users understand how to reactivate files at their original location if access is requiredâespecially if they encounter unexpected open or load errors. The list of known limitation includes but isn't limited to:
-Word and PowerPoint online.
+Some Microsoft 365 applications and services don't yet support file-level archiving. These applications might display incorrect error messages, fail to load correctly, or fail actions taken with archived content. Because client support and user awareness for archived files continue to evolve, we recommend that you use file-level archive thoughtfully and ensure users understand how to reactivate files at their original location i
```

---

## HIGH: Control Review Recommended

### 1. Purview management for SharePoint Embedded containers

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/purview-management?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -43,13 +43,13 @@ Purview enables configuration of retention policies and other compliance features based on the content URL location. To locate the container URL for Copilot Pages, Notebooks, or Loop workspaces:
 Sign in to the SharePoint admin center with the
 SharePoint Embedded administrator role
-Navigate to
-Containers
->
+Expand
+SharePoint Embedded
+, and then select
 Active containers
 or
 Deleted containers
-where you can view the details of a selected Loop workspace or Copilot Pages and Copilot Notebooks container
+, where you can view the details of a selected Loop workspace or Copilot Pages and Copilot Notebooks container.
 From the flyout pane,
 General
 tab.

```

---

### 2. Zero Trust for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/security/zero-trust/copilots/zero-trust-microsoft-365-copilot
**Section:** Zero Trust and Security Architecture
**Classification:** HIGH (Compliance features)

**What Changed:**
```diff
--- +++ @@ -19,11 +19,11 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Apply principles of Zero Trust to Microsoft 365 Copilot
+Apply principles of Zero Trust to Microsoft Copilot
 Feedback
 Summarize this article for me
 Summary:
-To apply Zero Trust principles to Microsoft 365 Copilot, you need to apply seven layers of protection in your Microsoft 365 tenant:
+To apply Zero Trust principles to Microsoft Copilot, apply seven layers of protection in your Microsoft 365 tenant:
 Data protection
 Identity and access
 App protection
@@ -32,7 +32,7 @@ Secure collaboration with Teams
 User permissions to data
 Introduction
-Before you introduce Microsoft 365 Copilot (Copilot) into your environment, Microsoft recommends that you build a strong foundation of security. Fortunately, guidance for a strong security foundation exists in the form of
+Before you introduce Microsoft Copilot (Copilot) into your environment, Microsoft recommends that you build a strong foundation of security. Fortunately, guidance for a strong security foundation exists in the form of
 Zero Trust
 . The Zero Trust security strategy treats each connection and resource request as though it originated from an uncontrolled network and a bad actor. Regardless of where the request originates or what resource it accesses, Zero Trust teaches us to "never trust, always verify."
 This article provides steps to apply the
@@ -67,9 +67,9 @@ An instance of the Microsoft Graph for the data of your Microsoft 365 tenant
 Your Microsoft 365 tenant that contains your organization data
 Copilot results for a user contain only data that the user is allowed to access
-For additional technical illustrations, see the following articles in the Microsoft 365 Copilot library:
-Microsoft 365 Copilot architecture and how it works
-Microsoft 365 Copilot data protection and auditing architecture
+For additional technical illustrations, see the following articles in the Microsoft Copilot libra
```

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*