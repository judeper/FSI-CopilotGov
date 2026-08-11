# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-11
**Run Time:** 2026-08-11T10:41:40.134887+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 1 |
| HIGH Changes | 1 |
| MEDIUM Changes | 1 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | data-connectors-reference | MEDIUM | 3.1, 4.11 | Update portal-walkthrough |
| 2 | create-analytics-rules | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -17480,9 +17480,9 @@ Workspace transform DCR
 Setup Instructions:
 Configuration steps for the Palo Alto Cortex XDR API
-Follow the instructions to obtain the credentials. you can also follow this
-guide
-to generate API key.
+Follow the instructions to obtain the credentials. You can also review the
+Cortex XDR documentation
+to generate an API key.
 Retrieve API URL
 1.1. Log in to the Palo Alto Cortex XDR [
 Management Console

```

---

## HIGH: Control Review Recommended

### 1. Create analytics rules

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/create-analytics-rules
**Section:** Microsoft Sentinel
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -38,9 +38,9 @@ to find and install the recommended rules specific to that recommendation. For more information, see
 SOC optimization usage flow
 .
-This section describes the process of creating an analytics rule from scratch, including using the
+This article explains how to create a Microsoft Sentinel analytics rule from scratch by using the
 Analytics rule wizard
-. It includes screenshots and directions to access the wizard in both the Azure portal and the Defender portal.
+. It includes screenshots and directions for both the Azure portal and the Defender portal.
 Important
 After
 March 31, 2027
@@ -55,7 +55,7 @@ Prerequisites
 You must have the Microsoft Sentinel Contributor role, or any other role or set of permissions that includes write permissions on your Log Analytics workspace and its resource group.
 You should have at least a basic familiarity with data science and analysis and the Kusto Query Language.
-You should familiarize yourself with the analytics rule wizard and all the configuration options that are available. For more information, see
+You should familiarize yourself with the analytics rule wizard and all the configuration options that are available. For more information about how scheduled rules work and their configuration options, see
 Scheduled analytics rules in Microsoft Sentinel
 .
 Design and build your query
@@ -138,9 +138,9 @@ .
 Status
 Enabled
-: The rule runs immediately upon creation, or at the
-specific date and time you choose to schedule it (currently in PREVIEW)
-.
+: The rule runs immediately upon creation, or at a specific date and time that you set in the
+Query scheduling
+section (currently in PREVIEW).
 Disabled
 : The rule is created but doesn't run. Enable it later from your
 Active rules
@@ -271,6 +271,8 @@ .
 Defender portal
 Azure portal
+The following screenshots show the rule logic settings in the analytics rule wizard.
+The following screenshots show the rule logic settings in the Azure portal.
 Co
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Connect Microsoft 365 data
**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
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