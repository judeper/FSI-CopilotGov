# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-18
**Run Time:** 2026-11-18T18:29:54.922566+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 7 |
| MEDIUM Changes | 2 |
| Redirects | 44 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | HIGH | 3.8a, 4.12 | Update portal-walkthrough |
| 2 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | 4.15 | Update portal-walkthrough |
| 3 | whats-new | CRITICAL | 4.15 | Update portal-walkthrough |
| 4 | get-started | MEDIUM | None | Review optional |
| 5 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 6 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 7 | cowork-faq | HIGH | 4.15 | Update portal-walkthrough |
| 8 | copilot-tuning-admin-guide | CRITICAL | 1.16 | Update portal-walkthrough |
| 9 | m365-agents-admin-guide | CRITICAL | None | Monitor |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -7,6 +7,203 @@ Android
 iOS
 Mac
+November 17, 2026
+Updates released between November 03, 2026, and November 17, 2026.
+Microsoft 365 admin center
+Share custom organizational attributes with Microsoft 365 people experiences
+[Web]
+We're introducing a new capability in Microsoft 365 Organizational Data Service that enables organizations to share selected custom organizational attributes with the Microsoft 365 people store.
+Details:
+What changed:
+Microsoft 365 Organizational Data Service now includes a setting that allows administrators to share selected custom organizational attributes with the Microsoft 365 people store. Custom attributes shared to Microsoft 365 experiences will be visible to all users in the tenant, and guests.
+This feature is off by default and requires administrator action to enable. During setup, administrators configure visibility for each attribute before it is shared. Organizations that do not use Microsoft 365 Organizational Data Service, or that do not enable this capability, experience no change.
+Why:
+The change allows organizations to select custom organizational data to make available in Microsoft 365 people experiences.
+Try this:
+Review existing custom attributes in Microsoft 365 Organizational Data Service.
+Determine whether Microsoft 365 experiences would benefit from including any custom attributes.
+Review internal organizational privacy, governance, and data-sharing requirements before enabling the capability.
+Confirm that custom attributes are appropriate to be shared with all users and guests in the tenant.
+Configure app access settings in Microsoft 365 Organizational Data Service to select custom attributes to make available to Microsoft 365.
+Why this matters:
+Organizations can enable new organizational data scenarios for Microsoft 365 while controlling which attributes are visible to Microsoft 365 experiences.
+Business impact:
+Administrators can extend people-related experiences with approved organi
```

---

### 2. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
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
--- +++ @@ -1,15 +1,9 @@ Copilot Cowork overview
 Microsoft Copilot Cowork can carry out tasks on your behalf. You describe what you need, and Cowork sends emails, schedules meetings, creates documents, posts in Teams, and manages your calendar. You approve each action before it happens.
 Note
-For users enrolled in the
-Frontier program
-, the tab options at the top of the left navigation might look different. To open Cowork, select the
-Home
-tab. The
-Chat
-and
-Cowork
-toggle appears in the conversation box. The default is the last choice you made.
+In Government Community Cloud (GCC), access and features differ from the worldwide experience described here. GCC access includes the Microsoft 365 Copilot web app and mobile progress checks and approvals. See
+GCC availability and prerequisites
+and Microsoft 365 Message Center for your tenant's availability information.
 What is Cowork?
 Cowork carries out tasks across your Microsoft 365 environment. Rather than describing what you could do, it does the work.
 Sends emails
@@ -131,6 +125,9 @@ : When Cowork finishes, review what it produced. Download documents, check sent messages, or ask Cowork to make changes.
 Stay in control
 You control what Cowork does throughout a session.
+For GCC,
+review the plan and approve every action
+, including file creation. The options below for skipping future approval prompts describe worldwide use and GCC.
 Approve actions
 : Cowork asks for your permission before taking sensitive actions, with a risk level indicator for medium and high risk actions. The button label matches the action (for example,
 Send
@@ -142,7 +139,7 @@ Pause, resume, and cancel
 : Pause at any time, resume when ready, or cancel the current task.
 Give feedback
-: Rate responses, leave comments on documents, or share general feedback.
+: Rate responses, leave comments on documents, or share general feedback. Note: in GCC environments, a user cannot leave comments.
 Learn more about each option in
 Approve a
```

---

### 3. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
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
--- +++ @@ -13,6 +13,17 @@ OneNote support
 Read OneNote notebooks and, when editing is available, update pages with your approval.
 Work with OneNote notebooks
+Claude Fable 5.2 model
+Fable 5.2 is now available in the model selector for select customers, replacing Fable 5.1. Fable 5.2 requires data retention.
+Choose a model for Cowork
+Claude Opus 5.5 Fast option
+Claude Opus 5.5 now includes a
+Fast
+option for quicker responses.
+Choose a model for Cowork
+GPT 5.5 retired
+GPT 5.5 is no longer available in the model selector. GPT 6.1 Sol, hosted by Microsoft in Azure, replaces it.
+Choose a model for Cowork
 Enhancements
 Added
 Plan and implement business processes with Copilot Cowork

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
--- +++ @@ -1,5 +1,9 @@ Manage Copilot Cowork for your organization
 Learn how to manage plugins, models, browser use, security and compliance, and usage-based billing in Copilot Cowork.
+Important
+This article describes worldwide administration. For government tenant enablement, feature differences, and feedback restrictions, see
+Cowork in GCC
+. Don't use the worldwide spending-policy or migration procedures below as government setup instructions.
 Note
 Cowork is now an
 agentic system
@@ -161,12 +165,18 @@ : Automated tasks have limits on how often they can run, and Cowork guards against tasks that trigger themselves in a loop.
 Audit visibility
 : Automated task activity is recorded in the unified audit log alongside other Cowork activity, and Microsoft Purview data security and compliance policies apply.
+In GCC, every action requires explicit approval, including actions in automated tasks and file creation. The preauthorization option above describes worldwide use. GCC supports only mail and calendar triggers. See
+GCC plan and approval requirements
+and
+GCC feature differences
+.
 Security and compliance
 Microsoft Purview is available to secure and govern Cowork. Learn more in
 Use Microsoft Purview to manage data security & compliance for Microsoft Copilot Cowork
 and
 What is Copilot Managed Runtime
 .
+In GCC, Cowork runs within the GCC boundary, and Purview features are not yet supported.
 Data residency
 Copilot Cowork follows the same data residency model as Copilot. Learn more in
 Data residency for Microsoft Copilot

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
--- +++ @@ -2,7 +2,6 @@ Copilot Cowork ships with many models so you can match the model to the work. Most of the time, leave the picker on
 Auto
 so Cowork can choose the model for your task.
-**
 For admins
 : You can disable models, including
 Anthropic models
@@ -23,45 +22,62 @@ When to use Auto
 Use
 Auto
-for most work. When you select
+for most work. You don't need to choose a model before every request.
+When you start a new conversation with
 Auto
-, Cowork picks the model based on the models enabled by your organization. You don't need to choose a model before every request.
+selected, Cowork reviews your first message to understand what kind of request it is and how much work it needs. Requests can range from a quick question or an email draft to a search, an analysis, a scheduling request, a file task, or a coding task. Cowork then picks a suitable model from the models enabled by your organization. Later messages in the same conversation continue on that model, unless the model stops being available.
+To check which model Cowork picked, look at the model badge on the response. If you choose a specific model instead of
+Auto
+, Cowork uses your choice.
+Note
+In some regions and for scheduled tasks,
+Auto
+uses the default model instead of picking one based on your request.
 Available models
 Your available options are in the
 Model
 dropdown menu in the chat input box. The options can include the following models and model modes.
 Model
 Description
+Zero data retention
 Notes
 Auto
-For most day-to-day work.
-The default. When you select
-Auto
-, Cowork picks the model based on the models enabled by your organization.
+Best model for the task.
+Depends on the model selected
+The default. Cowork picks a model based on the type and complexity of your request, from the models enabled by your organization. Learn more in
+When to use Auto
+.
 GPT 6.1 Sol
 Intelligent and efficient for hard work.
 Hosted by Microsoft. Tenants that turn off OpenAI as a subpro
```

---

### 6. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
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
--- +++ @@ -3,6 +3,14 @@ Tip
 Find questions and answers specifically for building an app in
 FAQ for building apps with Cowork
+.
+Note
+Unless a question specifies otherwise, these answers describe worldwide availability. For government access, supported features, and limitations, see
+Cowork in GCC
+.
+Can I use Cowork in GCC?
+Yes. Cowork is available in Government Community Cloud (GCC) through the Microsoft Copilot web app. Your admin must enable Cowork for your tenant. For licensing, tenant setup, and feature differences, see
+Cowork in GCC
 .
 What is Cowork?
 Cowork is available in Microsoft Copilot. It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multistep tasks across your Microsoft 365 environment.
@@ -75,6 +83,9 @@ .
 What can Cowork access?
 Cowork inherits your permissions, so it can access only the files and emails you can already access. If you don't have access to a file or email, Cowork can't access it either. When a referenced file or email has a sensitivity label, Cowork shows that label and displays the highest sensitivity label for the conversation.
+For GCC, labels from source content carry through to generated content. This doesn't establish support for every encrypted-file or label scenario. See
+GCC capabilities
+.
 Can I add plugins to Cowork?
 Yes. Cowork supports plugins from the Microsoft 365 App Store that add skills, connectors, or both. You can browse and install plugins from the
 Browse plugins
@@ -103,7 +114,9 @@ Plugins hub
 .
 How do I start using Cowork?
-Getting started takes just a few steps.
+For GCC, first follow
+Prepare for GCC access
+. The following steps describe worldwide access.
 Open
 Microsoft Copilot
 .
@@ -113,7 +126,7 @@ Describe the task you want to accomplish. You can type up to 250,000 characters and attach files by dragging them into the chat or using the file picker.
 Send your message. Cowork begins processing your request.
```

---

### 7. Copilot Tuning admin guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide
**Section:** Copilot Extensibility
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,10 +1,281 @@-Microsoft Copilot Tuning admin guide (early access preview)
-Microsoft Copilot Tuning (early access preview) is an AI customization capability that enables organizations to create task-specific Copilot agents by tuning large language models (LLMs) with their own organizational data. AI admins manage Copilot Tuning through Copilot controls in the Microsoft 365 admin center. Copilot Tuning provides multiple layers of governance to balance innovation with oversight.
-This article describes how administrators manage Microsoft Copilot Tuning, including role requirements, availability controls, agent lifecycle management, and data protection considerations.
+Frontier Tuning admin guide (early access preview)
+Frontier Tuning (early access preview) is an AI customization capability that enables organizations to create task-specific Copilot agents by tuning large language models (LLMs) with their own organizational data. AI admins manage Frontier Tuning through Copilot controls in the Microsoft 365 admin center. Frontier Tuning provides multiple layers of governance to balance innovation with oversight.
+This overview helps Microsoft 365 administrators and service owners assess access, spending, published assets, and data protection. It includes a Frontier Tuning administrative review draft and retains the existing Frontier Tuning and Agent Builder guidance separately.
+Scope and tuning entry points
+Treat the authoring experience, tuning service, consuming host, and published asset as separate administrative scopes. Access or approval in one scope doesn't establish authorization in the others.
+The shared notice is preserved here pending that decision:
 Important
 Microsoft Copilot Tuning is currently available to a limited set of customers through early access programs. Access through
 Frontier
 is planned for April 2026. Features and requirements are subject to change.
+Entry point or asset
+Administrative boundary
+Legacy Agent Builder templat
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Get started with Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Classification:** MEDIUM (General content update)

---

### 2. M365 Agents admin guide
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide
**Classification:** CRITICAL (Deprecation notice)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/copilot/plan/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access | https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/copilot/plan/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy | https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access | https://learn.microsoft.com/en-us/copilot/implement/copilot-ai-provider-user-sec-group-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences | https://learn.microsoft.com/en-us/copilot/implement/discovery-setting-ai-experiences |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits | https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json | https://learn.microsoft.com/en-us/plugins/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent | https://learn.microsoft.com/en-us/plugins/overview-declarative-agent |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents | https://learn.microsoft.com/en-us/plugins/agent-builder-build-agents |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge | https://learn.microsoft.com/en-us/plugins/agent-builder-add-knowledge |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder | https://learn.microsoft.com/en-us/plugins/agent-builder |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/knowledge-sources | https://learn.microsoft.com/en-us/plugins/knowledge-sources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites#agent-capabilities-and-licensing-models | https://learn.microsoft.com/en-us/plugins/prerequisites#agent-capabilities-and-licensing-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter | https://learn.microsoft.com/en-us/plugins/code-interpreter |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/image-generator | https://learn.microsoft.com/en-us/plugins/image-generator |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide | https://learn.microsoft.com/en-us/copilot/manage/copilot-tuning-admin-guide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/plugins/overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security | https://learn.microsoft.com/en-us/plugins/data-privacy-security |
| https://learn.microsoft.com/en-us/entra/agent-id/configure-third-party-agents | https://learn.microsoft.com/en-us/entra/agent-id/choose-agent-integration-path |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*