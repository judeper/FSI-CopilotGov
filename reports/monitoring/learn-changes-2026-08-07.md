# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-07
**Run Time:** 2026-08-07T10:42:13.488010+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| HIGH Changes | 4 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | ...-based-billing-manage-copilot-credits | HIGH | 4.15 | Update portal-walkthrough |
| 2 | what-is-microsoft-entra-agent-id | HIGH | None | Review and update |
| 3 | what-are-agent-identities | HIGH | None | Review and update |
| 4 | what-is-agent-id-platform | HIGH | None | Review and update |
| 5 | concept-secure-web-ai-gateway-agents | HIGH | None | Review and update |
| 6 | data-connectors-reference | CRITICAL | 3.1, 4.11 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

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
--- +++ @@ -138,7 +138,11 @@ If a policy doesn't have a per-user limit set, the system uses its overall policy limit as the per-user value for this comparison. The chosen policy applies in full and settings from other policies aren't combined.
 When users reach their limit within a policy, they can request more credits but they don't default to other policies. The system keeps the user on the assigned policy and doesn't reevaluate the user against other policies.
 Spending policy behavior when a user moves between Entra ID Groups
-If a user moves from one Entra ID group to another during a billing period, the new group's spending policy becomes effective for that user. Credits consumed before the move are retained for billing at a policy level but aren't tracked at a user level in the Consumption tab view. Only the current usage against the current spending policy is displayed at a user level in the Consumption tab view.
+If a user moves from one Entra ID group to another during a billing period, the new group's spending policy becomes effective for that user. Credits consumed before the move remain billed against the previous spending policy. In the
+Consumption
+tab, the displayed spending limit reflects the user's current spending policy, while
+Total credits used
+includes credit consumption across all spending policies assigned to the user during the billing period.
 For example,
 User belongs to Group 1, which is assigned Spending Policy A with a spending limit of 10,000 credits.
 The user consumes 9,000 credits under Spending Policy A, which is visible in the
@@ -147,10 +151,13 @@ Mid month, the user is moved to Group 2, which is assigned Spending Policy B with a spending limit of 20,000 credits. The user's usage is reset to 0 and now aligned to Spending Policy B. Usage is only visible in the
 Consumption
 tab view by user after the user actually consumes credits under the Spending Policy B.
-The user then consumes 15,000 credits after the move under Spending
```

---

### 2. Connect Microsoft 365 data

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
--- +++ @@ -96,7 +96,47 @@ For a list of tables ingested into Microsoft Sentinel and the connectors that ingest them, see
 Microsoft Sentinel tables and associated connectors
 .
+1Password (Serverless)
+Supported by:
 1Password
+The 1Password CCF connector allows the user to ingest 1Password Audit, Signin & ItemUsage events into Microsoft Sentinel.
+Log Analytics table(s)
+:
+Table
+DCR support
+Lake-only ingestion
+OnePasswordEventLogs_CL
+Yes
+Yes
+Data collection rule support:
+Workspace transform DCR
+Prerequisites
+:
+1Password API token
+: A 1Password API Token is required. See the
+1Password documentation
+on how to create an API token.
+Setup Instructions
+:
+STEP 1 - Create a 1Password API token
+:
+Follow the
+1Password documentation
+for guidance on this step.
+STEP 2 - Choose the correct base URL
+:
+There are multiple 1Password servers which might host your events. The correct server depends on your license and region. Follow the
+1Password documentation
+to choose the correct server. Input the base URL as displayed by the documentation (including 'https://' and without a trailing '/').
+STEP 3 - Enter your 1Password Details
+:
+Enter the 1Password base URL & API Token below:
+Base Url
+: (Enter your Base Url)
+API Token
+: (Enter your API Token)
+Enable/Disable Connection
+1Password (using Azure Functions)
 Supported by:
 1Password
 The
@@ -104,12 +144,14 @@ solution for Microsoft Sentinel enables you to ingest sign-in attempts, item usage, and audit events from your 1Password Business account using the
 1Password Events Reporting API
 . This allows you to monitor and investigate events in 1Password in Microsoft Sentinel along with the other applications and services your organization uses.
-Underlying Microsoft Technologies used:
+Underlying Microsoft Technologies used
+:
 This solution depends on the following technologies, and some of which may be in
 Preview
 state or may incur additional ingestion or operational costs:
 Azure Functions
-Log Analyt
```

---

## HIGH: Control Review Recommended

### 1. Microsoft Entra Agent ID overview

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -50,24 +50,8 @@ license for each user. For pricing details, see
 Microsoft Agent 365 plans and pricing
 .
-Extending Microsoft Entra security features to agents requires
-Microsoft 365 E7
-(includes Agent 365 and Microsoft Entra Suite) or
-Microsoft 365 E5
-paired with a
-Microsoft Agent 365
-license. Customers without E5 or E7 can use the following standalone licensing options with a
-Microsoft Agent 365
-license:
-Conditional Access for agents
-: Microsoft Entra ID P1
-ID Protection for agents
-: Microsoft Entra ID P2
-ID Governance for agents
-: Microsoft Entra ID P1
-Network controls for agents
-: Microsoft Entra Internet Access, included in Microsoft Entra Suite or licensed separately. For more information, see
-What is Global Secure Access
+Extending Microsoft Entra security features to agents requires Microsoft Agent 365. Agent 365 is included with Microsoft 365 E7 and is available as an add-on to Microsoft E5/A5/Business Premium (or Microsoft Defender Suite + Microsoft Purview Suite). See our latest
+Agent 365 product terms for more details
 .
 Related content
 Microsoft Entra security for AI overview

```

---

### 2. Microsoft Entra agent identity concepts

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -74,24 +74,8 @@ license for each user. For pricing details, see
 Microsoft Agent 365 plans and pricing
 .
-Extending Microsoft Entra security features to agents requires
-Microsoft 365 E7
-(includes Agent 365 and Microsoft Entra Suite) or
-Microsoft 365 E5
-paired with a
-Microsoft Agent 365
-license. Customers without E5 or E7 can use the following standalone licensing options with a
-Microsoft Agent 365
-license:
-Conditional Access for agents
-: Microsoft Entra ID P1
-ID Protection for agents
-: Microsoft Entra ID P2
-ID Governance for agents
-: Microsoft Entra ID P1
-Network controls for agents
-: Microsoft Entra Internet Access, included in Microsoft Entra Suite or licensed separately. For more information, see
-What is Global Secure Access
+Extending Microsoft Entra security features to agents requires Microsoft Agent 365. Agent 365 is included with Microsoft 365 E7 and is available as an add-on to Microsoft E5/A5/Business Premium (or Microsoft Defender Suite + Microsoft Purview Suite). See our latest
+Agent 365 product terms for more details
 .
 Related content
 Agent identities in Microsoft Entra Agent ID

```

---

### 3. Microsoft Entra Agent identity platform

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -33,24 +33,8 @@ license for each user. For pricing details, see
 Microsoft Agent 365 plans and pricing
 .
-Extending Microsoft Entra security features to agents requires
-Microsoft 365 E7
-(includes Agent 365 and Microsoft Entra Suite) or
-Microsoft 365 E5
-paired with a
-Microsoft Agent 365
-license. Customers without E5 or E7 can use the following standalone licensing options with a
-Microsoft Agent 365
-license:
-Conditional Access for agents
-: Microsoft Entra ID P1
-ID Protection for agents
-: Microsoft Entra ID P2
-ID Governance for agents
-: Microsoft Entra ID P1
-Network controls for agents
-: Microsoft Entra Internet Access, included in Microsoft Entra Suite or licensed separately. For more information, see
-What is Global Secure Access
+Extending Microsoft Entra security features to agents requires Microsoft Agent 365. Agent 365 is included with Microsoft 365 E7 and is available as an add-on to Microsoft E5/A5/Business Premium (or Microsoft Defender Suite + Microsoft Purview Suite). See our latest
+Agent 365 product terms for more details
 .
 Platform architecture overview
 The Microsoft agent identity platform is built on several foundational technical components that work together to provide a complete identity and authorization solution for AI agents:

```

---

### 4. Network controls for Copilot Studio agents

**URL:** https://learn.microsoft.com/en-us/entra/global-secure-access/concept-secure-web-ai-gateway-agents
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -41,24 +41,8 @@ license for each user. For pricing details, see
 Microsoft Agent 365 plans and pricing
 .
-Extending Microsoft Entra security features to agents requires
-Microsoft 365 E7
-(includes Agent 365 and Microsoft Entra Suite) or
-Microsoft 365 E5
-paired with a
-Microsoft Agent 365
-license. Customers without E5 or E7 can use the following standalone licensing options with a
-Microsoft Agent 365
-license:
-Conditional Access for agents
-: Microsoft Entra ID P1
-ID Protection for agents
-: Microsoft Entra ID P2
-ID Governance for agents
-: Microsoft Entra ID P1
-Network controls for agents
-: Microsoft Entra Internet Access, included in Microsoft Entra Suite or licensed separately. For more information, see
-What is Global Secure Access
+Extending Microsoft Entra security features to agents requires Microsoft Agent 365. Agent 365 is included with Microsoft 365 E7 and is available as an add-on to Microsoft E5/A5/Business Premium (or Microsoft Defender Suite + Microsoft Purview Suite). See our latest
+Agent 365 product terms for more details
 .
 Next steps
 Configure network security for Microsoft Copilot Studio agents

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