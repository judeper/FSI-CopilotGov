# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-17
**Run Time:** 2026-07-17T11:14:35.755369+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 2 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 3 | data-connectors-reference | CRITICAL | 4.11, 3.1 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Section:** Copilot Cowork
**Classification:** HIGH (Compliance features)

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
--- +++ @@ -42,7 +42,9 @@ Manage models
 Cowork ships with several models: Claude Opus and Sonnet variants from Anthropic, Claude Fable 5 (Preview), the Sonnet+Opus Advisor pairing, GPT 5.5, and Imagen 2 for image generation. Claude Fable 5 (Preview) is off by default; turn it on in the
 Microsoft 365 admin center
-under Copilot settings if you want to make it available. Some models, such as Claude Fable 5, require data retention, which means a user's prompts and responses for that model are retained by the model provider.
+under Copilot settings if you want to make it available. Some models, such as Claude Fable 5, require data retention, which means a user's prompts and responses for that model are retained by the model provider. For more information about preview models, including their limitations, see
+Manage preview AI models in Microsoft Online Services
+.
 As an admin, you can turn off the Anthropic model family in the
 Microsoft 365 admin center
 under Copilot settings.

```

---

### 2. Copilot Cowork available models

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -88,7 +88,11 @@ .
 To learn how Cowork handles your data, see the
 Anthropic subprocessor
-information.
+information. Claude Fable 5 (Preview) is an Anthropic preview model that requires data retention, and an admin must enable it before it's available. For more information, see
+Anthropic models in Microsoft Online Services
+and
+Manage preview AI models in Microsoft Online Services
+.
 Models hosted by Microsoft
 We may deploy other AI models for Microsoft 365 Copilot to use that are hosted and operated by Microsoft. These models are governed by the same contractual and data protection commitments already in place, including that no data leaves Microsoft. For more information about models that may be used by Copilot, see
 Understanding AI functionality and models in Microsoft Online Services
@@ -103,6 +107,8 @@ Related content
 Use Cowork
 Manage Cowork for your organization
+Anthropic models in Microsoft Online Services
+Manage preview AI models in Microsoft Online Services
 Responsible AI FAQ for Cowork
 Feedback
 Was this page helpful?

```

---

### 3. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** CRITICAL (UI navigation steps changed)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

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
--- +++ @@ -100,7 +100,8 @@ Supported by:
 1Password
 The 1Password CCF connector allows the user to ingest 1Password Audit, Signin & ItemUsage events into Microsoft Sentinel.
-Log Analytics table(s):
+Log Analytics table(s)
+:
 Table
 DCR support
 Lake-only ingestion
@@ -109,21 +110,26 @@ Yes
 Data collection rule support:
 Workspace transform DCR
-Prerequisites:
+Prerequisites
+:
 1Password API token
 : A 1Password API Token is required. See the
 1Password documentation
 on how to create an API token.
-Setup Instructions:
-STEP 1 - Create a 1Password API token:
+Setup Instructions
+:
+STEP 1 - Create a 1Password API token
+:
 Follow the
 1Password documentation
 for guidance on this step.
-STEP 2 - Choose the correct base URL:
+STEP 2 - Choose the correct base URL
+:
 There are multiple 1Password servers which might host your events. The correct server depends on your license and region. Follow the
 1Password documentation
 to choose the correct server. Input the base URL as displayed by the documentation (including 'https://' and without a trailing '/').
-STEP 3 - Enter your 1Password Details:
+STEP 3 - Enter your 1Password Details
+:
 Enter the 1Password base URL & API Token below:
 Base Url
 : (Enter your Base Url)
@@ -138,12 +144,14 @@ solution for Microsoft Sentinel enables you to ingest sign-in attempts, item usage, and audit events from your 1Password Business account using the
 1Password Events Reporting API
 . This allows you to monitor and investigate events in 1Password in Microsoft Sentinel along with the other applications and services your organization uses.
-Underlying Microsoft Technologies used:
+Underlying Microsoft Technologies used
+:
 This solution depends on the following technologies, and some of which may be in
 Preview
 state or may incur additional ingestion or operational costs:
 Azure Functions
-Log Analytics table(s):
+Log Analytics table(s)
+:
 Table
 DCR support
 Lake-only ingestion
@@ -152,7 +160,8 @@ Yes
 Data collection rule suppo
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