# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-27
**Run Time:** 2026-10-27T15:36:33.415084+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 6 |
| Redirects | 21 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | copilot-teams-transcription | HIGH | 4.2 | Update portal-walkthrough |
| 3 | whats-new | HIGH | 4.15 | Update portal-walkthrough |
| 4 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 5 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 6 | cowork-faq | HIGH | 4.15 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.9/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.9/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -381,8 +381,8 @@ Microsoft Copilot adheres to Microsoft's
 Responsible AI principles
 . For more information, see
-Microsoft Copilot Responsible AI FAQ
-, and
+Application card: Microsoft Copilot (for organizations)
+and
 Responsible AI at Microsoft
 .
 Model selection

```

---

### 2. Copilot in Teams meetings

**URL:** https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.2: Control 4.2: Copilot in Teams Meetings Governance
  - File: `controls/pillar-4-operations/4.2-teams-meetings-governance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.2/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -24,7 +24,7 @@ When organizers create a meeting or event, they can set Copilot's value to
 Only during the meeting
 from the dropdown list in their meeting options. Once someone with a Microsoft Copilot license selects the Copilot button during the meeting or event, Copilot runs for all licensed users. This option relies on speech-to-text audio processing data that isn't saved after the meeting or event ends.
-Depending on your organization's Microsoft Purview retention policies, Copilot prompts and responses during meetings might be retained for compliance purposes, even if recording and transcription are turned off. This applies only to the Commercial cloud and doesn't apply to GCC or DoD cloud environments.
+Depending on your organization's Microsoft Purview retention policies, Copilot prompts and responses during meetings might be retained for compliance purposes, even if recording and transcription are turned off. This applies to Commercial and GCC cloud environments but not to DoD.
 To learn more about how organizers can use Copilot only during the meeting, see
 Use Microsoft Copilot in Teams without recording a Teams meeting
 .

```

---

### 3. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
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
--- +++ @@ -1,7 +1,21 @@ What's new in Copilot Cowork
-This article lists recent features, improvements, and changes in Microsoft 365 Copilot Cowork. Get a full guide to Cowork's capabilities in
-Use Cowork
-.
+This article lists recent features, improvements, and changes in Microsoft Copilot Cowork. Get a full guide to Cowork's capabilities in
+Use Cowork
+.
+October 2026
+New features
+Feature
+Description
+Learn more
+GPT 6.1 Sol model
+GPT 6.1 Sol is now available in the model selector as an intelligent and efficient model for hard work, replacing GPT 6 Sol.
+Choose a model for Cowork
+Grok 4.7 model
+Grok 4.7 is now available in the model selector for long documents, coding, and multi-step tasks. Grok 4.7 is provided by xAI as an independent processor.
+Choose a model for Cowork
+Projects
+Use projects in Copilot Cowork to keep related tasks, instructions, and context together. Start tasks from a project, return to related chats, and review the files those tasks produce.
+Use projects in Copilot Cowork
 September 2026
 New features
 Feature
@@ -60,7 +74,7 @@ Description
 Learn more
 General availability
-Microsoft 365 Copilot Cowork is generally available to all Microsoft 365 Copilot tenants worldwide in tier-1 languages.
+Microsoft Copilot Cowork is generally available to all Microsoft 365 Copilot tenants worldwide in tier-1 languages.
 Cowork overview
 Claude Opus 4.8 model
 Opus 4.8 is now available as a model option in the model selector.
@@ -147,7 +161,7 @@ Opus 4.7 is now available as a model option in the model selector.
 Use Cowork
 Mobile app support
-Cowork is now available on iPhone and Android through the Microsoft 365 Copilot mobile app.
+Cowork is now available on iPhone and Android through the Microsoft Copilot mobile app.
 Use Cowork on mobile
 April 2026
 New features

```

---

### 4. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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
--- +++ @@ -80,7 +80,7 @@ Get the admin guide on plugin deployment, availability controls, connector authentication, and monitoring in
 Manage plugins for Cowork
 and
-Manage plugins in Microsoft 365 admin center
+Manage plugins, skills, and MCP servers
 .
 Manage models
 Cowork ships with several models, which are described in

```

---

### 5. Copilot Cowork available models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -33,36 +33,44 @@ The default. When you select
 Auto
 , Cowork picks the model based on the models enabled by your organization.
-GPT 5.5 (Frontier)
-Capable model for medium effort work.
-Hosted in Azure AI Foundry.
-GPT 5.6 Sol
-Intelligent and efficient for hard workâ.
-Provided by OpenAI as a subprocessor. More information:
-OpenAI as a subprocessor in Microsoft Online Services
-GPT 5.6 Terra
-Balanced effort for common tasksâ.
+GPT 6.1 Sol
+Intelligent and efficient for hard work.
 Provided by OpenAI as a subprocessor. More information:
 OpenAI as a subprocessor in Microsoft Online Services
 GPT 6 Astra
 Latest model for tough problems.
 Provided by OpenAI as a subprocessor. More information:
 OpenAI as a subprocessor in Microsoft Online Services
-Opus 5
+GPT 5.6 Terra
+Balanced effort for common tasks.
+Provided by OpenAI as a subprocessor. More information:
+OpenAI as a subprocessor in Microsoft Online Services
+GPT 5.5 (Frontier)
+Capable model for medium effort work.
+Hosted in Azure AI Foundry.
+Claude Opus 5.5
 For complex, high stakes work.
 More information:
 Anthropic subprocessor
-Claude Sonnet 5
-For everyday tasks and fast responses such as drafting, quick lookups, and day-to-day work.
+Claude Sonnet 5.5
+Efficient for everyday tasks.
 Use when you want a shorter response cycle for common tasks. More information:
 Anthropic subprocessor
-Claude Fable 5.1
-Most advanced model for ambitious work.
+Claude Fable 5.1 (Frontier)
+Most advanced model for ambitious projects.
 More information:
 Anthropic subprocessor
 . Learn about data retention in
 Anthropic models in Microsoft Online Services
 .
+Grok 4.7
+Strong on long documents, coding, and multi-step tasks.
+Provided by xAI as an independent processor. More information:
+Connect to SpaceXAI models (as an independent processor)
+Note
+Model availability may vary based on tenant configuration. If your organization is within the
+EU Data Boundary
+, only GPT models are supported.
 How mode
```

---

### 6. Copilot Cowork FAQ

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
--- +++ @@ -332,9 +332,9 @@ Auto
 and Cowork chooses the model that fits your task. To pick a specific model, select
 Auto
-in the compose box and choose from the list that your organization makes available. The choices include GPT 5.5, GPT 5.6, and GPT 6 variants, Claude Opus, Claude Sonnet, and Claude Fable 5.1 and 5 (Preview). Claude Fable 5 (Preview) is off by default, so it appears only after an admin turns it on in the
-Microsoft 365 admin center
-under Copilot settings. Some models, such as Claude Fable 5, require data retention, and Cowork shows a note in the picker and a banner while the model is selected. Learn more in
+in the compose box and choose from the list that your organization makes available. The choices include GPT 5.5, GPT 5.6, and GPT 6 variants, Claude Opus, Claude Sonnet, Claude Fable, and Grok 4.7. Model availability may vary based on tenant configuration. If your organization is within the
+EU Data Boundary
+, only GPT models are supported. Some models, such as Claude Fable, require data retention, and Cowork shows a note in the picker and a banner while the model is selected. Learn more in
 Choose a model for Cowork
 .
 You can also set the reasoning effort level that determines how Cowork balances quality, speed, and cost. Since your tasks might require different levels of power, you can choose the level next to the model picker.

```

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

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*