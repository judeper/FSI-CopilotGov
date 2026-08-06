# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-06
**Run Time:** 2026-08-06T11:56:39.236598+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| HIGH Changes | 1 |
| MEDIUM Changes | 4 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | endpoint-dlp-learn-about | MEDIUM | None | Review optional |
| 2 | audit-log-activities | HIGH | 3.1, 1.15 | Update portal-walkthrough |
| 3 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 4 | get-started | HIGH | None | Review and update |
| 5 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 6 | cowork-models | MEDIUM | 4.15 | Update portal-walkthrough |
| 7 | cowork-faq | MEDIUM | None | Review optional |
| 8 | agent-settings | CRITICAL | 4.13, 1.13, 2.13, 2.14 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -4124,7 +4124,7 @@ CallParticipantDetail
 Teams added information about the participants of a call, including the user ID of each participant, the time each participant joined and left the call, and participant connection information.
 Added information about meeting participants
-9, 12
+9, 12, 14
 MeetingParticipantDetail
 Teams added information about the participants of a meeting, including the user ID of each participant, the time a participant joined the meeting, the time a participant left the meeting, and the start/stop time of a meeting recording by the user.
 You can also see logs with timestamps and information about:
@@ -4509,6 +4509,9 @@ 1
 SubscribedToMessages
 A subscription was created by a listener application to receive change notifications for messages.
+Security Risk detected in a Teams call
+SecurityRiskInCallDetected
+An external Teams call is detected to have potential security concern such as impersonation
 Teams Admin Action
 TeamsAdminAction
 Logged when a Teams admin performs actions like updating, adding, or deleting Teams related settings or configurations using admin tools like PowerShell, Admin Center, API, etc.
@@ -4618,7 +4621,7 @@ 8
 This event is included in all chat conversations between external Teams users managed by an organization and external Teams users not managed by an organization.
 9
-This event is currently unavailable in Government Community Cloud (GCC), but is available in Government Community Cloud High (GCC-High) and Department of Defense (DoD) organizations.
+This event is currently available in Government Community Cloud (GCC), Government Community Cloud High (GCC-High), Department of Defense (DoD) organizations and air-gapped environments.
 10
 This event is included in all participating tenants.
 11
@@ -4627,6 +4630,8 @@ Calls that are recorded or transcribed are included in MeetingParticipantDetail.
 13
 This event is logged by Graph API access and not by Teams client.
+14
+This event is now shared wi
```

---

### 2. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new
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
--- +++ @@ -65,7 +65,7 @@ Fable 5 is now available in preview in the model selector for your toughest challenges. Fable 5 is off by default; an admin turns it on in the Microsoft 365 admin center under Copilot settings. Fable 5 requires data retention, so your prompts and responses for that model are retained by the model provider, and Cowork shows a banner while it's selected.
 Data retention
 Image generation
-Cowork can generate images using Imagen 2. Ask for an image in chat and Cowork saves it to your conversation and your OneDrive output folder.
+Cowork can generate images using ChatGPT Images 2.0. Ask for an image in chat and Cowork saves it to your conversation and your OneDrive output folder.
 Generate images
 Local browser use (Frontier)
 Cowork can complete web tasks for you in Microsoft Edge on your device, using your existing sign-ins and your organization's policies. In Frontier and requires that Edge is installed.

```

---

### 3. Copilot Cowork admin and governance

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
--- +++ @@ -57,9 +57,9 @@ Manage plugins in Microsoft 365 admin center
 .
 Manage models
-Cowork ships with several models: Claude Opus and Sonnet variants from Anthropic, Claude Fable 5 (Preview), the Sonnet+Opus Advisor pairing, GPT 5.5, and Imagen 2 for image generation. Claude Fable 5 (Preview) is off by default; turn it on in the
+Cowork ships with several models: Claude Opus and Sonnet variants from Anthropic, Claude Fable 5 (Preview), the Sonnet+Opus Advisor pairing, GPT 5.5, and ChatGPT Images 2.0 for image generation. Claude Fable 5 (Preview) is off by default; turn it on in the
 Microsoft 365 admin center
-under Copilot settings if you want to make it available. Some models, such as Claude Fable 5, require data retention, which means a user's prompts and responses for that model are retained by the model provider. For more information about preview models, including their limitations, see
+under Copilot settings if you want to make it available. Some models, such as Claude Fable 5, require data retention, which means a user's prompts and responses for that model are retained by the model provider. Learn about preview models, including their limitations, in
 Manage preview AI models in Microsoft Online Services
 .
 As an admin, you can turn off the Anthropic model family in the
@@ -70,7 +70,7 @@ , or for information about the use of Anthropic models, visit
 Anthropic as a subprocessor for Microsoft Online Services
 .
-For details on each model and how end users pick them, see
+Learn about each model and how end users pick them in
 Choose a model for Cowork
 .
 Browser use

```

---

### 4. Copilot Cowork available models

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -86,7 +86,7 @@ After you select the model, Cowork shows a banner while that model is selected. The banner clears when you switch to a model that doesn't require data retention, including
 Auto
 .
-To learn how Cowork handles your data, see the
+To learn how Cowork handles your data when using Anthropic models, see the
 Anthropic subprocessor
 information. Claude Fable 5 (Preview) is an Anthropic preview model that requires data retention, and an admin must enable it before it's available. For more information, see
 Anthropic models in Microsoft Online Services

```

---

### 5. Agent settings in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide
**Section:** Agent Governance
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -41,10 +41,14 @@ - Manage who can share AI agents within your organization and define the methods they can use to share them.
 User access
 - Control which users or groups can interact with AI agents, aligning access with organizational roles and permissions.
+Agent feedback sharing
+- Control whether agent usage feedback is shared with agent developers to help improve agent quality and reliability.
+Tags
+- Manage the labels that admins and users apply to agents to organize and find them.
 These settings allow you to customize agent behavior, control access, and maintain compliance with enterprise standards.
 Agent management rules
-Agent Management Rules in the Microsoft 365 Admin Center (MAC) enable tenant administrators to apply governance and lifecycle controls across AI agents at scale using bulk administrative actions.
-Rather than requiring you to manually review and take action on agents individually, Agent Management Rules allow you to:
+Agent Management Rules in the Microsoft 365 Admin Center (MAC) enable tenant administrators to apply governance and lifecycle controls across AI agents at scale by using bulk administrative actions.
+Instead of manually reviewing and taking action on agents individually, use Agent Management Rules to:
 Identify agents that meet defined conditions
 Review impacted agents prior to run
 Apply governance actions across affected agents in bulk
@@ -55,22 +59,27 @@ Reassign ownerless agents created with Agent Builder to manager
 Install Microsoft agents
 Microsoft first-party (1P) agents are consistently among the most installed and widely used agents. However, administrators currently lack a scalable way to install these agents proactively across their tenant.
-Using the Install Microsoft (1P) Agents rule, you can do the following:
+By using the
+Install Microsoft (1P) Agents
+rule, you can:
 Identify Microsoft-published agents within the tenant
-Review eligible agents prior to installation
+Review eligible agents bef
```

---

## HIGH: Control Review Recommended

### 1. Get started with Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -33,8 +33,7 @@ : Cowork is enabled in your Microsoft 365 Copilot environment.
 Usage-based billing
 : Usage-based and Cowork billing has been enabled.
-Anthropic enabled in tenant
-: Cowork uses Anthropic models as a subprocessor to ensure secure and responsible use of Anthropic models within your organization. Details about the integration can be found at
+Cowork can optionally use Anthropic models as a subprocessor. Integration details can be found at
 Anthropic as a subprocessor for Microsoft Online Services
 .
 Cowork works in your browser at
@@ -49,10 +48,10 @@ in the top toggle next to Chat.
 When the Cowork homepage loads, you'll have access to:
 A chat input where you can describe what you need, along with any recent tasks you can pick up where you left off.
-Search: instantly search and revisit your previous tasks, so your past work is always at your fingertips.
-Scheduled: view, edit, reschedule, and clean up your scheduled tasks without hunting through menus.
-Customize: add your own personal skills to Cowork, and discover and add plugins to extend what Cowork can do.
-Model picker: choose the model that works best for your task, or let Cowork decide.
+Search: Instantly search and revisit your previous tasks, so your past work is always at your fingertips.
+Scheduled: View, edit, reschedule, and clean up your scheduled tasks without hunting through menus.
+Customize: Add your own personal skills to Cowork, and discover and add plugins to extend what Cowork can do.
+Model picker: Select the model that works best for your task, or let Cowork decide.
 Start your first conversation
 Type what you want done in the chat input, or select one of the suggested prompts such as
 Catch me up
@@ -107,7 +106,7 @@ Create
 ): Allow this specific action to proceed.
 Always allow
-: Select the dropdown arrow next to the action button to allow the action and skip future approval prompts for similar actions in the current conversation.
+(for a specific session): S
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Endpoint DLP
**URL:** https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about
**Classification:** MEDIUM (General content update)

---

### 2. What's new in Copilot Cowork
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new
**Classification:** MEDIUM (General content update)

---

### 3. Copilot Cowork available models
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
**Classification:** MEDIUM (General content update)

---

### 4. Copilot Cowork FAQ
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
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