# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-30
**Run Time:** 2026-07-30T11:45:05.689963+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 1 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | data-connectors-reference | CRITICAL | 3.1, 4.11 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -96,47 +96,7 @@ For a list of tables ingested into Microsoft Sentinel and the connectors that ingest them, see
 Microsoft Sentinel tables and associated connectors
 .
-1Password (Serverless)
-Supported by:
 1Password
-The 1Password CCF connector allows the user to ingest 1Password Audit, Signin & ItemUsage events into Microsoft Sentinel.
-Log Analytics table(s)
-:
-Table
-DCR support
-Lake-only ingestion
-OnePasswordEventLogs_CL
-Yes
-Yes
-Data collection rule support:
-Workspace transform DCR
-Prerequisites
-:
-1Password API token
-: A 1Password API Token is required. See the
-1Password documentation
-on how to create an API token.
-Setup Instructions
-:
-STEP 1 - Create a 1Password API token
-:
-Follow the
-1Password documentation
-for guidance on this step.
-STEP 2 - Choose the correct base URL
-:
-There are multiple 1Password servers which might host your events. The correct server depends on your license and region. Follow the
-1Password documentation
-to choose the correct server. Input the base URL as displayed by the documentation (including 'https://' and without a trailing '/').
-STEP 3 - Enter your 1Password Details
-:
-Enter the 1Password base URL & API Token below:
-Base Url
-: (Enter your Base Url)
-API Token
-: (Enter your API Token)
-Enable/Disable Connection
-1Password (using Azure Functions)
 Supported by:
 1Password
 The
@@ -144,36 +104,32 @@ solution for Microsoft Sentinel enables you to ingest sign-in attempts, item usage, and audit events from your 1Password Business account using the
 1Password Events Reporting API
 . This allows you to monitor and investigate events in 1Password in Microsoft Sentinel along with the other applications and services your organization uses.
-Underlying Microsoft Technologies used
-:
+Underlying Microsoft Technologies used:
 This solution depends on the following technologies, and some of which may be in
 Preview
 state or may incur additional ingestion or operational costs:
 Azure Functions
-Log Analyt
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