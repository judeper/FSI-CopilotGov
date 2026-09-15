# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-15
**Run Time:** 2026-09-15T14:32:52.211408+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| HIGH Changes | 1 |
| MEDIUM Changes | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | get-started | MEDIUM | None | Review optional |
| 2 | cowork-admin-governance | CRITICAL | 4.15 | Update portal-walkthrough |
| 3 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 4 | cowork-faq | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Copilot Cowork admin and governance

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
--- +++ @@ -106,13 +106,15 @@ Manage plugins in Microsoft 365 admin center
 .
 Manage models
-Cowork ships with several models: Claude Fable, Opus and Sonnet variants from Anthropic, the Sonnet+Opus Advisor pairing, GPT 5.5, and ChatGPT Images 2.0 for image generation. Learn more about data retention in
+Cowork ships with several models, which are described in
+Choose a model for Copilot Cowork
+.
+As an admin, you can turn off the Anthropic model family in the Microsoft 365 admin center under
+Copilot Settings
+. Learn more about managing models and data retention in
 Anthropic models in Microsoft Online Services
 .
-As an admin, you can turn off the Anthropic model family in the
-Microsoft 365 admin center
-under Copilot settings.
-Model availability vs. access
+Model availability versus access
 Model settings control which models a user sees, not whether the user can use Cowork. The two are separate concerns:
 Turning off the Anthropic model family is a model control and has no effect on whether a user can access Cowork. Access is granted by a spending policy that selects Cowork. Learn more in
 How access to Copilot Cowork is determined
@@ -121,13 +123,8 @@ When the Anthropic family is off, users with Cowork access keep working with the non-Anthropic models your organization allows, such as the GPT models.
 Auto
 continues to select from the remaining available models, so users aren't blocked from Cowork by this setting.
-Microsoft might deploy other AI models for Microsoft Copilot to use that are hosted and operated by Microsoft. These models are governed by the same contractual and data protection commitments already in place, including that no data leaves Microsoft. For more information about the use of Azure-hosted GPT models in Microsoft Copilot, visit
-Understanding AI functionality and models in Microsoft Online Services
-, or for information about the use of Anthropic models, visit
-Anthropic as a subprocessor for Microsoft Online Services
-.
-Learn about
```

---

### 2. Copilot Cowork available models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -22,9 +22,15 @@ Choose a model for Copilot Cowork
 Feedback
 Summarize this article for me
-Copilot Cowork ships with several models so you can match the model to the work. Most of the time, leave the picker on
+Copilot Cowork ships with many models so you can match the model to the work. Most of the time, leave the picker on
 Auto
 so Cowork can choose the model for your task.
+For admins
+: You can turn off the Anthropic model family in the
+Microsoft 365 admin center
+under Copilot settings. This model control has no effect on whether a user can access Cowork. The setting is tenant-wide, so it can't be used to grant Anthropic models to a subset of users. When the Anthropic family is off, users keep working with the non-Anthropic models your organization allows. When you select
+Auto
+, Cowork chooses from the remaining available models.
 Where you pick a model
 The default selection is
 Auto
@@ -39,7 +45,9 @@ Auto
 , Cowork picks the model based on the models enabled by your organization. You don't need to choose a model before every request.
 Available models
-The model picker can include the following models and model modes.
+Your available options are in the
+Model
+dropdown menu in the chat input box. The options can include the following models and model modes.
 Model
 Description
 Notes
@@ -75,34 +83,14 @@ Most advanced model for ambitious work.
 More information:
 Anthropic subprocessor
-. For information on data retention, see
+. Learn about data retention in
 Anthropic models in Microsoft Online Services
 .
 How model choice affects responses
 Changing the model can affect response speed, response depth, and output style. Some models are optimized for faster drafting, while others spend more time on reasoning and review.
 Cowork shows a model badge in the conversation so you can see which model produced a response.
-Data retention
-For information on data retention, see
-Anthropic models in Microsoft Online Services
-.
-Models hosted by Micros
```

---

## HIGH: Control Review Recommended

### 1. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -72,6 +72,15 @@ folder. Each file contains a YAML frontmatter block with a name and description, followed by the skill instructions. Cowork discovers your custom skills automatically at the start of each session.
 Get step-by-step instructions in
 Create custom skills
+.
+Can I give Cowork custom instructions?
+Yes. On the
+Preferences
+tab of the
+Customize
+page, add custom instructions that describe how you prefer to work, such as your preferred tone, document formatting, or scheduling rules. Cowork applies them to every task. Your instructions are personal to you and can contain up to 20 KB.
+Get details in
+Custom instructions in Cowork
 .
 What can Cowork access?
 Cowork inherits your permissions, so it can access only the files and emails you can already access. If you don't have access to a file or email, Cowork can't access it either. When a referenced file or email has a sensitivity label, Cowork shows that label and displays the highest sensitivity label for the session.
@@ -348,7 +357,9 @@ under Copilot settings. Some models, such as Claude Fable 5, require data retention, and Cowork shows a note in the picker and a banner while the model is selected. Learn more in
 Choose a model for Cowork
 .
-You can also set the effort level that determines how Cowork balances quality, speed, and cost. Since your tasks might require different levels of power, you can choose the effort level next to the model picker. Medium is the default, giving you a strong balance for everyday work.
+You can also set the reasoning effort level that determines how Cowork balances quality, speed, and cost. Since your tasks might require different levels of power, you can choose the level next to the model picker.
+Medium
+is the default, which gives you a strong balance for everyday work.
 Where are my files saved?
 Files that Cowork creates are saved to your
 OneDrive and SharePoint

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Get started with Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*