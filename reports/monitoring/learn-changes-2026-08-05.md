# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-05
**Run Time:** 2026-08-05T11:50:32.360463+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 4 |
| MEDIUM Changes | 2 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | apply-sensitivity-label-automatically | MEDIUM | 1.5, 2.2 | Update portal-walkthrough |
| 2 | audit-log-activities | CRITICAL | 3.1, 1.15 | Update portal-walkthrough |
| 3 | faq | HIGH | 4.16 | Update portal-walkthrough |
| 4 | agent-builder | MEDIUM | None | Review optional |
| 5 | data-connectors-reference | CRITICAL | 3.1, 4.11 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Apply sensitivity labels automatically

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
--- +++ @@ -60,8 +60,8 @@ Auto-labeling isn't available in my region.
 The
 Auto-labeling
-page isn't visible in unsupported regions. See
-Azure dependency availability by country/region
+page isn't visible in unsupported regions. See the
+regional availability prerequisite
 .
 I want to set a default label for Teams meetings, sites, groups, or Microsoft 365 Copilot.
 This article covers files and emails. For container-level default labels (including Teams instant meetings and Meet Now), see
@@ -600,9 +600,7 @@ Items to review
 views can mix auto-labeling and DLP results and can fail to load if either signal is under load. If a view returns an error, retry a few hours later before you open a support case.
 Simulation limits are documented separately.
-Item caps (100 per site displayed, 50,000-record CSV export ceiling, 4,000,000-item scan limit), 12-hour target completion time, and stall-detection guidance are in
-Limits for auto-labeling policies
-.
+The following guidance covers item caps (100 per site displayed, 50,000-record CSV export ceiling, and 4,000,000-item scan limit), the 12-hour target completion time, and stall detection.
 Simulation mode supports up to 4,000,000 matched files. If more than this number of files are matched from an auto-labeling policy, you can't turn on the policy to apply the labels. In this case, you must reconfigure the auto-labeling policy so that fewer files are matched, and rerun simulation. This maximum of 4,000,000 matched files applies to simulation mode only and not to an auto-labeling policy that's already turned on to apply sensitivity labels.
 Note
 Simulation results can differ from what happens when the policy is turned on:

```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -2752,6 +2752,28 @@ Declassified file as part of an on-demand classification scan
 DataScanDeClassification
 File no longer matches the sensitive information types defined in the corresponding On-demand classification scan triggered for SharePoint or OneDrive locations.
+Microsoft Purview permission activities
+The following table lists Microsoft Purview administration activities that the Microsoft 365 audit log records when an administrator manages role-based access control (RBAC) role groups and user assignments. For more information, see
+Permissions in the Microsoft Purview portal
+.
+Friendly name
+Operation
+Description
+Create RBAC role group definition
+CreateRBACRoleGroupDefinition
+An RBAC role group definition is created.
+Delete RBAC role group definition
+DeleteRBACRoleGroupDefinition
+An RBAC role group definition is deleted.
+Update RBAC role group definition
+UpdateRBACRoleGroupDefinition
+An RBAC role group definition is updated.
+Add user assignments to role group
+GrantPermissionsAsync
+User assignments to an RBAC role group are added.
+Remove user assignments to role group
+DeletePermissionAsync
+User assignments to an RBAC role group are removed.
 Microsoft Security Copilot agent management
 The following table lists the Agent management operations in Security Copilot that the Microsoft 365 audit log records. These activities characterize activities for agents and the components necessary for them to function such as triggers. For more information about Security Copilot agent management, see
 Microsoft Security Copilot agents overview

```

---

### 3. Microsoft Scout FAQ

**URL:** https://learn.microsoft.com/microsoft-scout/faq
**Section:** Microsoft Scout (Frontier preview)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -413,9 +413,21 @@ Microsoft doesn't validate custom skills created by users. Review custom skill outputs carefully.
 Background modes (heartbeat and automations) use a more restrictive permission policy than interactive conversations.
 Does Microsoft Scout connect to external models for processing?
-Yes. Microsoft Scout uses the GitHub Copilot SDK, which might connect to external AI models as a subprocessor to ensure secure and responsible use. You can find details about model providers and data handling in the Microsoft 365 Copilot documentation.
+Yes. Microsoft Scout processes your prompts and content through GitHub Copilot, which connects to AI models from Microsoft and from third-party providers, including open-source models. Scout inherits its model catalog from GitHub Copilot, and your GitHub Copilot admin determines which models are available for Scout to use. You can find details about model providers and related information in the Microsoft GitHub Copilot documentation. Supported models can include third-party and open-source models, including models from China-based providers. Because this processing occurs through GitHub Copilot, it is governed by your organization's
+GitHub Customer Agreement
+and the
+GitHub General Privacy Statement
+.
 Are there unsupported countries or regions?
-Access to Microsoft Scout follows the same regional restrictions as other Microsoft 365 Copilot features. Check with your administrator or Microsoft support for region-specific availability.
+Microsoft Scout is currently available through the Frontier preview program. Availability is determined by enrollment in that program rather than by a Scout-specific list of supported countries or regions, and your organization's administrator controls whether Scout is enabled for you.
+Because Microsoft Scout processes prompts and content through GitHub Copilot, GitHub's terms and restrictions apply to that processing, including applicable trade control and sanctions requirem
```

---

### 4. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** CRITICAL (UI navigation steps changed)

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
--- +++ @@ -114,17 +114,17 @@ DCR support
 Lake-only ingestion
 OnePasswordEventLogs_CL
-No
-No
-Data collection rule support:
-Not currently supported
-Prerequisites:
-Microsoft.Web/sites permissions:
-Read and write permissions to Azure Functions to create a Function App is required. For more information, see
+Yes
+Yes
+Data collection rule support:
+Workspace transform DCR
+Prerequisites:
+Microsoft.Web/sites permissions
+: Read and write permissions to Azure Functions to create a Function App is required. For more information, see
 Azure Functions
 .
-1Password Events API Token:
-A 1Password Events API Token is required. For more information, see
+1Password Events API Token
+: A 1Password Events API Token is required. For more information, see
 the 1Password API
 .
 Note:
@@ -146,7 +146,7 @@ STEP 2 - Deploy the functionApp using DeployToAzure button to create the table, dcr and the associated Azure Function
 IMPORTANT:
 Before deploying the 1Password connector, a custom table needs to be created.
-Option 1 - Azure Resource Manager (ARM) Template:
+Option 1 - Azure Resource Manager (ARM) Template
 This method provides an automated deployment of the 1Password connector using an ARM Tempate.
 Click the
 Deploy to Azure
@@ -181,13 +181,13 @@ DCR support
 Lake-only ingestion
 OnePasswordEventLogs_CL
-No
-No
-Data collection rule support:
-Not currently supported
-Prerequisites:
-1Password API token:
-A 1Password API Token is required. See the
+Yes
+Yes
+Data collection rule support:
+Workspace transform DCR
+Prerequisites:
+1Password API token
+: A 1Password API Token is required. See the
 1Password documentation
 on how to create an API token.
 Setup Instructions:
@@ -201,10 +201,10 @@ to choose the correct server. Input the base URL as displayed by the documentation (including 'https://' and without a trailing '/').
 STEP 3 - Enter your 1Password Details:
 Enter the 1Password base URL & API Token below:
-Base Url:
-(Enter your Base Url)
-API Token:
-(Enter your API
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Apply sensitivity labels automatically
**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Classification:** MEDIUM (General content update)

---

### 2. Agent Builder capabilities
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
**Classification:** MEDIUM (General content update)

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