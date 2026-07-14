# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-14
**Run Time:** 2026-07-14T11:17:43.599511+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| HIGH Changes | 1 |
| MEDIUM Changes | 2 |
| Redirects | 13 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | None | Review and update |
| 2 | cowork-faq | CRITICAL | None | Monitor |
| 3 | ...-based-billing-manage-copilot-credits | HIGH | 4.15 | Update portal-walkthrough |
| 4 | overview-declarative-agent | MEDIUM | 1.13, 2.14 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (Portal references)

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
--- +++ @@ -32,8 +32,8 @@ Discovery setting for AI experiences enabled by usage-based billing
 .
 Role requirements
-Global administrator and Billing administrator roles have access to add, select, and change billing methods, and set billing methods in policies.
-AI administrator and License administrator roles have access to create spending policies, manage limits and alerts, and view the Cost management dashboard. They can't set or modify the billing method.
+Global administrator and Billing administrator roles can add, select, and change billing methods, and set billing methods in policies.
+AI administrator and License administrator roles can create spending policies, manage limits and alerts, and view the Cost management dashboard. They can't set or modify the billing method.
 Important
 Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global administrator is a highly privileged role that you should limit to emergency scenarios when you can't use an existing role. For more information, see
 About administrator roles in the Microsoft 365 admin center
@@ -96,7 +96,7 @@ You can edit the default spending policy or add more spending policies. Have a policy for
 All users
 as a default policy that applies when no other policy is assigned.
-You set the tenant-level limit for all users when you activate the default spending policy. Each additional spending policy has its own independent limit and doesn't inherit the tenant-level limit.
+Set the tenant-level limit for all users when you activate the default spending policy. Each additional spending policy has its own independent limit and doesn't inherit the tenant-level limit.
 Select
 +Add spending policy
 and go through the screens to create the spending policy. The following sections describe the steps that you need to complete as you go through the tabs.
@@ -227,20 +227,25 @@ tab once processing is complete. Th
```

---

### 2. Declarative agents for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -74,15 +74,15 @@ Responsible AI validation checks
 .
 National cloud support
-Limited support for declarative agents is available for
+Declarative agent support for
 Microsoft 365 Government
-tenants:
+tenants varies by cloud:
 Government Community Cloud (GCC)
 : Full declarative agent support is available.
 Government Community Cloud High (GCCH)
-: Limited support â only pro-code agents built with Microsoft 365 Agents Toolkit are supported. Agent Builder isn't available for declarative agents in GCCH.
+: Pro-code agents built with Microsoft 365 Agents Toolkit are supported. Agent Builder is also now available in GCCH.
 Department of Defense (DoD)
-: Declarative agents aren't currently available.
+: Limited support - only pro-code agents built with Microsoft 365 Agents Toolkit are supported. Agent Builder isn't available for declarative agents in DoD.
 Related content
 Agents in the Microsoft 365 ecosystem
 Agents are apps for Microsoft 365

```

---

## HIGH: Control Review Recommended

### 1. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -45,7 +45,7 @@ : Drafts stakeholder communications such as status updates and announcements.
 Schedules prompts
 : Runs prompts on a schedule so recurring tasks happen automatically.
-Cowork shows each step in your conversation, so you can follow along as it works.
+Cowork shows each step in your session, so you can follow along as it works.
 What can Cowork do for you?
 The following sections describe what you can ask Cowork to do.
 Communication
@@ -56,14 +56,14 @@ Prepare polished stakeholder communications such as status updates, announcements, and follow-ups.
 Documents and files
 Create Word documents, Excel spreadsheets, PowerPoint presentations, and PDFs from scratch.
-Edit and refine existing documents you share in the conversation.
+Edit and refine existing documents you share in the session.
 Browse your entire Work IQ to pull in the content you need.
 Create SharePoint and OneDrive folders.
 Reorganize your existing files into new or existing folders.
 Calendar and meetings
 Schedule meetings using natural language, such as "set up a 30-minute check-in with Alex tomorrow at 2 PM."
 Manage your calendarâadd events, move things around, or clean up conflicts by declining meetings. Cowork can include a message to the organizer on the reason you're declining.
-Get meeting intelligence and insights to help you prepare for upcoming conversations.
+Get meeting intelligence and insights to help you prepare for upcoming sessions.
 Start your day with a daily briefing that highlights what's ahead.
 Research and search
 Search across your organization to find documents, messages, and information.
@@ -72,15 +72,15 @@ Automation
 Run prompts on a schedule, so recurring tasks happen automatically.
 Skills
-Cowork uses specialized skills as it works. When Cowork loads a new skill during your conversation, the skill shows up in the side panel. Each skill corresponds to a specific type of task.
+Cowork uses specialized skills as it works. When Cowork loads a 
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Cowork FAQ
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Classification:** CRITICAL (Deprecation notice)

---

### 2. Declarative agents for Copilot
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
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

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*