# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-18
**Run Time:** 2026-07-18T10:55:46.676508+00:00
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
| 1 | ...osoft365-copilot-location-learn-about | HIGH | 2.1 | Update portal-walkthrough |
| 2 | audit-log-activities | HIGH | 3.1, 1.15 | Update portal-walkthrough |
| 3 | cowork-admin-governance | CRITICAL | 4.15 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. DLP for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -26,8 +26,8 @@ Restrict Microsoft 365 Copilot from using external web search when prompts contain sensitive data.
 You can use DLP policies to prevent Microsoft 365 Copilot and Copilot Chat from sending sensitive information to external web services. When a prompt contains sensitive information types (SITs)âsuch as credit card numbers, passport numbers, Social Security numbers, or custom SITs defined by your organizationâCopilot automatically blocks the use of external web search as a grounding source for that prompt. Instead, Copilot continues to generate responses using permitted internal Microsoft 365 data sources. This ensures that sensitive data remains protected and isn't shared with external search providers.
 Restrict Microsoft 365 Copilot and Copilot Chat from processing sensitive prompts.
-You can create a DLP policy to help protect against the use of sensitive information types (SITs), such as credit card numbers, passport numbers, or Social Security numbers in Microsoft 365 Copilot prompts. This includes Microsoft-provided SITs and custom SITs that you create. This real-time control helps organizations reduce data leakage and oversharing risks. It prevents Microsoft 365 Copilot and Copilot Chat, including prebuilt agents, from returning a response when prompts contain sensitive data and from using that sensitive data for both internal and external web searches.
-Restrict Microsoft 365 Copilot and Copilot Chat from processing sensitive files and emails (generally available).
+You can create a DLP policy to help protect against the use of sensitive information types (SITs), such as credit card numbers, passport numbers, or Social Security numbers in Microsoft 365 Copilot prompts. This includes Microsoft-provided SITs and custom SITs that you create. This real-time control helps organizations reduce data leakage and oversharing risks. It prevents Microsoft 365 Copilot and Copilot Chat from returning a response when prompts contain sensitive d
```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -395,7 +395,7 @@ RelabelItem
 A disposition reviewer relabeled the retention label.
 Dragon Copilot admin activities
-The following table lists administrative activities for Dragon Copilot recorded in the Microsoft 365 audit log. These events are logged when an administrator changes Dragon Copilot configuration. These event include changes in environments, products, EHR connectors, billing plans, groups, role assignments, settings, and extensions. If your organization uses Dragon Copilot, you can
+The following table lists administrative activities for Dragon Copilot recorded in the Microsoft 365 audit log. These events are logged when an administrator changes Dragon Copilot configuration. These events include changes in environments, products, Electronic Health Record (EHR) connectors, billing plans, groups, role assignments, settings, and extensions. If your organization uses Dragon Copilot, you can
 search the audit log
 for these activities by using the
 Activities
@@ -575,6 +575,100 @@ Viewed setting
 ViewedSetting
 A setting value was viewed.
+Dragon Copilot Web activities
+The following table lists user and application activities for Dragon Copilot Web recorded in the Microsoft 365 audit log. These events capture user access, clinical workflow actions, AI-assisted operations, and session lifecycle events performed within Dragon Copilot Web. Dragon Copilot Web supports clinical documentation workflows including ambient recording, transcript review, AI-assisted note generation, clinical chat, and EHR-integrated experiences.
+If your organization uses Dragon Copilot Web, you can search for these activities in Microsoft Purview Audit by selecting the appropriate activity name or by filtering on the Dragon Copilot record types. Audit records are emitted under the following record types:
+DragonCopilotAccess
+DragonCopilotClinicalData
+DragonCopilotSession
+You can also search for Dragon Copilot Web audit events by using
+Search-UnifiedAuditLog
+and filt
```

---

### 3. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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
--- +++ @@ -23,6 +23,23 @@ Feedback
 Summarize this article for me
 Learn how to manage plugins, models, browser use, security and compliance, and usage-based billing in Copilot Cowork.
+Note
+Copilot Cowork is now generally available and is no longer managed in the Microsoft 365 admin center by selecting
+All Agents
+>
+Cowork
+in the left navigation menu. The agent-based access control that was available in the Preview version isn't used to manage user access.
+Cowork is now an
+agentic system
+(different from an
+agent
+). You can access it in the Microsoft 365 admin center by selecting
+Agents
+>
+All Agents
+, and then selecting
+Cowork
+from the dropdown menu to the right.
 Allow access to Cowork
 To allow users to access Cowork, admins must enable usage-based billing. To learn how to set up and enable usage-based billing, see
 Managing AI experiences enabled by usage-based billing
@@ -71,22 +88,17 @@ Use the local browser with Cowork
 .
 Usage-based billing
-Cowork uses a usage-based billing model. Activities such as model responses, tool and skill calls, image generation, and browser tasks count toward your organization's consumption. Admins see usage in the Microsoft 365 admin center and can set per-user or per-group limits. To learn more about usage-based billing, visit
+Cowork uses a usage-based billing model. Activities such as model responses, tool and skill calls, image generation, and browser tasks count toward your organization's consumption. Admins see usage in the Microsoft 365 admin center and can set per-user or per-group limits. Learn more about usage-based billing in
 Microsoft 365 pay-as-you-go services
 .
-Learn to
-Set up and configure Usage-based billing.
-Learn more about what Copilot Credits are at
-What is Copilot Credits?
-.
-Learn more about how to estimate costs with the
-Cowork cost estimator
-.
-Learn how to
-setup Copilot Credits
-.
+Learn more about usage-based billing in the following links:
+Set up and configure usage-based bill
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