# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-17
**Run Time:** 2026-11-17T18:52:02.274266+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 19 |
| HIGH Changes | 9 |
| MEDIUM Changes | 11 |
| Redirects | 43 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 3 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | 4.15 | Update portal-walkthrough |
| 4 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 5 | get-started | MEDIUM | None | Review optional |
| 6 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 7 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 8 | cowork-manage-plugins | HIGH | 4.15 | Update portal-walkthrough |
| 9 | cowork-faq | HIGH | 4.15 | Update portal-walkthrough |
| 10 | index | HIGH | 4.15 | Update portal-walkthrough |
| 11 | policy-risk-based-sign-in | MEDIUM | None | Review optional |
| 12 | information-barriers | MEDIUM | 2.4 | Update portal-walkthrough |
| 13 | information-barriers-teams | CRITICAL | 2.4 | Update portal-walkthrough |
| 14 | ...ication-fundamentals-publish-channels | MEDIUM | 2.14, 4.14 | Update portal-walkthrough |
| 15 | mcp-add-existing-server-to-agent | HIGH | None | Review and update |
| 16 | ...n.microsoft.com/en-us/entra/agent-id/ | MEDIUM | 2.17 | Update portal-walkthrough |
| 17 | what-is-microsoft-entra-agent-id | MEDIUM | 2.14 | Update portal-walkthrough |
| 18 | what-are-agent-identities | MEDIUM | None | Review optional |
| 19 | whats-new-agent-id | HIGH | None | Review and update |
| 20 | manage-agent-identities-admin | HIGH | None | Review and update |
| 21 | security-for-ai-overview | HIGH | None | Review and update |
| 22 | what-is-agent-id-platform | HIGH | None | Review and update |
| 23 | configure-third-party-agents | CRITICAL | None | Monitor |
| 24 | sign-in-audit-logs-agents | HIGH | None | Review and update |
| 25 | agent-id-governance-overview | HIGH | None | Review and update |
| 26 | agent-registry-convergence | MEDIUM | None | Review optional |
| 27 | best-practices-agent-id | HIGH | None | Review and update |
| 28 | overview | HIGH | index, 4.11 | Update portal-walkthrough |
| 29 | microsoft-sentinel-defender-portal | HIGH | 4.11 | Update portal-walkthrough |
| 30 | move-to-defender | HIGH | 4.11 | Update portal-walkthrough |
| 31 | manage-data-overview | CRITICAL | 4.11 | Update portal-walkthrough |
| 32 | create-analytics-rules | HIGH | None | Review and update |
| 33 | monitor-your-data | MEDIUM | 4.11 | Update portal-walkthrough |

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
--- +++ @@ -50,8 +50,10 @@ )
 Securely interact with Copilot,
 Copilot Cowork
-and
+,
 Copilot Code
+and
+Autopilot
 using web and work data (
 Microsoft Graph
 and
@@ -69,9 +71,9 @@ .
 You
 don't
-have the Microsoft 365 Copilot add-on license but have
-standard access
-to Copilot in Word, Excel, PowerPoint, and OneNote. Some features are subject to
+have the Microsoft 365 Copilot add-on license but
+can
+use Copilot in Word, Excel, PowerPoint, and OneNote. Some features are subject to
 fair use limits
 .
 For more information, see
@@ -79,20 +81,20 @@ .
 You
 have
-the Microsoft 365 Copilot add-on license with
-priority access
-to the full experience of Copilot in Word, Excel, PowerPoint, and OneNote.
+the Microsoft 365 Copilot add-on license with access to the full experience of Copilot in Word, Excel, PowerPoint, and OneNote. Some features are subject to
+fair use limits
+.
 For more information, see
 Microsoft 365 Copilot (Premium) license and experience
 .
 You
 have
-the Microsoft 365 Copilot add-on license with
-priority access
-to the full experience of Copilot in Word, Excel, PowerPoint, and OneNote, and access to
+the Microsoft 365 Copilot add-on license with access to the full experience of Copilot in Word, Excel, PowerPoint, and OneNote, and access to
 Copilot Cowork
-and
+,
 Copilot Code
+and
+Autopilot
 via
 usage-based billing
 .
@@ -108,7 +110,7 @@ and
 Work IQ
 ).
-Includes access to Cowork, Code, and agents that use web and work data (
+Includes access to Cowork, Code, Autopilot, and other agents that use web and work data (
 Microsoft Graph
 and
 Work IQ
@@ -173,9 +175,7 @@ Use Copilot Chat in select Microsoft 365 apps like Teams and Outlook with content you have open. In this context, Copilot Chat is aware of your open content and can use it instead of requiring you to copy and paste information or upload a file.
 Use a pay-as-you-go agent that has access to organizational content.
 Microsoft 365 Copilot (Basic)
-refers to users without the Copilo
```

---

### 2. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1333,6 +1333,16 @@ Files labeled in the last 30 days
 chart. The chart shows daily counts and an average calculated over all 30 days.
 These views count label-applied and label-changed activity for SharePoint and OneDrive files associated with your auto-labeling policies. They don't include Exchange email. Use them to spot activity trends, not to measure remaining daily capacity or the number of unique files currently labeled or protected.
+A file can contribute more than one recorded labeling operation in the selected time window. Activity doesn't count every access, scan, evaluation, or retry, and deleting a file doesn't remove its historical activity. These counts aren't directly interchangeable with the periodically refreshed
+Total labeled to date
+progress report on the
+Insights
+tab.
+For metric definitions and reporting guidance, see
+Compare progress and labeling activity
+. If counts differ or a report is unavailable or partial, see
+Troubleshoot auto-labeling count mismatches
+. Missing or partial reporting doesn't mean that zero files were labeled.
 Policy rule fails to load
 In rare cases, a malformed rule in an auto-labeling policy can prevent the policy from loading correctly. The most common symptom is that Exchange messages stop matching an otherwise enabled auto-labeling policy, and there might not be any item-level labeling failure to review because the rule never loaded in the first place.
 This is different from the SharePoint and OneDrive item-level labeling failures described earlier in this section. Those failures mean a specific file was evaluated against the policy but couldn't be labeled (for example, because of file format or existing protection). A rule-load failure means the policy's rule couldn't be compiled or loaded at all, so

```

---

### 3. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
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
--- +++ @@ -38,7 +38,7 @@ .
 Allows faculty and staff in the education industry to complete multi-step work across Microsoft 365
 : Prepares course materials, coordinates research and grant work, prepares materials for department or curriculum meetings, and other tasks.
-Create apps (Frontier)
+Create apps
 : Use the App skill to build lightweight, interactive apps from a description. There's no coding required. You can refine the app in chat, open, publish, and share it with your stakeholders.
 Cowork shows each step in your session, so you can follow along as it works.
 Note
@@ -91,7 +91,7 @@ .
 Skills
 Cowork uses specialized skills as it works. When Cowork loads a new skill during your session, the skill shows up in the side panel. Each skill corresponds to a specific type of task.
-Cowork has built-in skills, including Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, Adaptive Cards, and App (Frontier). When OneNote support is available, Cowork also uses the
+Cowork has built-in skills, including Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, Adaptive Cards, and App. When OneNote support is available, Cowork also uses the
 OneNote & Notebooks
 skill. You can also create your own custom skills.
 Learn more about each skill in
@@ -105,11 +105,11 @@ Cowork supports plugins from the Microsoft 365 App Store that add new skills and connectors. Plugins can give Cowork specialized expertiseâsuch as financial analysis or legal researchâor connect it to external data sources and services. Your organization's admin can also deploy plugins for everyone in your organization.
 Microsoft's
 role-based and industry plugins
-include Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork.
+include Accounting for Cowork (Frontier), Finance for Cowo
```

---

### 4. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
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
--- +++ @@ -175,7 +175,7 @@ >
 Plugins
 tab. Cowork converts a Claude or other compatible package into a publishable package, including bundled skills and connectors.
-Upload a plugin package
+Upload a skill or plugin
 Share skills and plugins
 Share a skill or plugin you created with only yourself or specific people in your organization, and re-share to keep recipients up to date when you make changes.
 Share skills and plugins

```

---

### 5. Copilot Cowork admin and governance

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
--- +++ @@ -82,6 +82,9 @@ and
 Manage plugins, skills, and MCP servers
 .
+Learn more in the
+Plugins hub
+.
 Manage models
 Cowork ships with several models, which are described in
 Choose a model for Copilot Cowork
@@ -117,7 +120,7 @@ Cowork Browsing
 tenant setting in the Microsoft 365 admin center turns the capability on or off for your organization.
 Which sites users can reach through Cowork
-: Cowork respects any allowlist, blocklist, and view-only policies your organization applies to web browsing in Microsoft Edge.
+: Cowork respects any allow list, block list, and view-only policies your organization applies to web browsing in Microsoft Edge.
 Audit visibility
 : Each browser task Cowork starts on behalf of a user is recorded in the unified audit log alongside other Cowork activity.
 Learn about
@@ -162,7 +165,7 @@ Microsoft Purview is available to secure and govern Cowork. Learn more in
 Use Microsoft Purview to manage data security & compliance for Microsoft Copilot Cowork
 and
-What is Copilot Managed Runtime (preview)
+What is Copilot Managed Runtime
 .
 Data residency
 Copilot Cowork follows the same data residency model as Copilot. Learn more in

```

---

### 6. Copilot Cowork available models

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
--- +++ @@ -40,7 +40,7 @@ , Cowork picks the model based on the models enabled by your organization.
 GPT 6.1 Sol
 Intelligent and efficient for hard work.
-Provided by OpenAI as a subprocessor. More information:
+Hosted by Microsoft. Tenants that turn off OpenAI as a subprocessor can still use it. More information:
 OpenAI as a subprocessor in Microsoft Online Services
 GPT 6 Astra
 Latest model for tough problems.
@@ -67,13 +67,12 @@ Anthropic subprocessor
 . Learn about data retention in
 Anthropic models in Microsoft Online Services
-.
 Grok 4.7
 Strong on long documents, coding, and multi-step tasks.
 Provided by xAI as an independent processor. More information:
 Connect to SpaceXAI models (as an independent processor)
 Note
-Model availability may vary based on tenant configuration. If your organization is within the
+Model availability might vary based on tenant configuration. If your organization is within the
 EU Data Boundary
 , only GPT models are supported.
 How model choice affects responses

```

---

### 7. Manage Copilot Cowork plugins

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
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
--- +++ @@ -1,5 +1,12 @@ Manage plugins for Copilot Cowork
 Microsoft Copilot Cowork supports plugins that add skills and connectors to extend what Cowork can do. As an IT administrator, you control which plugins are available in your organization, how they're deployed, and who can use them. This article covers plugin governance from an admin perspective.
+Manage plugins in
+Microsoft 365 admin center
+>
+Agents
+>
+Tools
+.
 Learn how users browse and use plugins in
 Use plugins with Cowork
 and
@@ -258,7 +265,7 @@ Only you
 to keep the plugin private to your account while you test.
 This approach gives you the fastest loop to confirm that your skills, connectors, and tool calls work end to end before you roll the plugin out to other users, groups, or your whole tenant. Learn more in
-Upload a plugin package
+Upload a skill or plugin
 .
 Testing in your tenant
 Before you publish a plugin to the Microsoft 365 App Store, you can distribute it within your own tenant to test it with a controlled audience. Admins upload the plugin package through

```

---

### 8. Copilot Cowork FAQ

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
--- +++ @@ -79,7 +79,7 @@ Yes. Cowork supports plugins from the Microsoft 365 App Store that add skills, connectors, or both. You can browse and install plugins from the
 Browse plugins
 menu. Once acquired, a plugin's included skills appear alongside the built-in skills, and included connectors become available for your conversations.
-Microsoft's role-based plugins include Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork. Learn about their capabilities and included skills in
+Microsoft's role-based plugins include Accounting for Cowork (Frontier), Finance for Cowork, Capital Markets for Cowork, HR Documents & Policies for Cowork, and more. Learn about their capabilities and included skills in
 Role-based and industry plugins
 .
 Get step-by-step instructions in
@@ -95,6 +95,12 @@ Can a plugin work with my files?
 Yes. Some plugin tools can act on files from your conversationâfor example, to convert a document, analyze an image, or attach a receipt to a record in another system. When a tool needs a file, Cowork sends the file you point to, and the plugin acts on it. Cowork asks for your approval before the tool runs. Learn more about building plugins in
 Accept files from the Cowork workspace
+.
+What happens to existing skills and plugins under the registry?
+The plugin registry is the common Microsoft Copilot infrastructure that lets a plugin be published once, discovered by users, made available to supported Copilot experiences, and centrally governed by admins.
+Existing skills and plugins generally remain available where they currently live. To gain full plugin registry discovery and cross-surface distribution, some owners need to package, validate, publish, or republish their assets. Microsoft still needs to publish product-specific migration and compatibility guidance for several existing sets of artifacts covered by this transition.
+Learn more in the
+Plugins hub
 .
 How do I start using Cowork?
 Getting started
```

---

### 9. What is Microsoft Copilot Managed Runtime (preview)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index
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
--- +++ @@ -1,102 +1,54 @@-What is Copilot Managed Runtime (preview)
-[This article is prerelease documentation and is subject to change.]
-Important
-This is a preview feature.
-These features are subject to
-supplemental terms of use
-, and are available before an official release so that customers can get early access and provide feedback.
-Copilot Managed Runtime hosts Microsoft 365 line-of-business applications that automatically inherit organizational governance, security, and compliance controls from the moment they're created. Whether you build an app through Copilot Cowork, Microsoft Copilot Studio, Copilot Code, or the Copilot Managed Runtime SDK, the resulting app runs in a Microsoft-hosted environment, uses Microsoft Entra authentication, follows tenant governance policies, and is visible to admins in the Microsoft 365 admin center for monitoring and management.
-Copilot Managed Runtime provides a unified experience for makers, developers, admins, and users. Organizations can accelerate app creation while maintaining centralized oversight, security, lifecycle management, and compliance controls.
-This article explains the entry points where you can
-create
-apps, the unified location where you can
-find and run
-apps already available to you, and further resources for Copilot Managed Runtime users, makers, developers, and administrators.
-Four ways to create an app
-Entry point
-Who it's for
-How it works
-Build apps in Cowork
-Business users who want to describe an app in a chat and keep working
-From a Cowork session, ask for an app (or use the
-App builder
-skill). Cowork builds the app, lets you preview it, and helps you publish and share it. Requires enrollment in the
-Frontier program
-.
-Create apps in Microsoft Copilot Studio
-Makers who want more control over the build, preview, and publish steps
-Sign in to Copilot Studio, turn on the
-Preview
-experience, and select
-Apps
-in the navigation. Describe the app in natural language or start from e
```

---

### 10. Learn about information barriers

**URL:** https://learn.microsoft.com/en-us/purview/information-barriers
**Section:** Information Barriers
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.4: Control 2.4: Information Barriers for Copilot (Chinese Wall)
  - File: `controls/pillar-2-security/2.4-information-barriers.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -119,6 +119,9 @@ . When you enable IB policies and enable hierarchical address book, all users not included in an IB segment see the
 hierarchical address book
 in Exchange Online.
+Information Barriers and Agent Builder experience
+Agent Builder provides an easy way to build Declarative agent in Microsoft 365. It offers an immediate, interactive AI development experience that suits quick and straightforward projects.
+Agent builder honors IB policies in the people picker experience. With IB support in Agent builder, when an IB user searches for other users in the people picker, they wonât see users theyâre restricted from communicating and collaborating with per IB policy. This restriction prevents users from conflicting segments to share an agent with each other. Users can continue to access agents that was previously shared with them. However, any new sharing experience via people picker will be allowed only with the users who can collaborate with each other per IB policy.
 Ready to get started?
 Get started with Information Barriers
 : Define segments and create your first IB policies.

```

---

### 11. Information barriers in Teams

**URL:** https://learn.microsoft.com/en-us/purview/information-barriers-teams
**Section:** Information Barriers
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 2.4: Control 2.4: Information Barriers for Copilot (Chinese Wall)
  - File: `controls/pillar-2-security/2.4-information-barriers.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -137,6 +137,8 @@ mode allows you to add all compatible users in the group.
 Owner Moderated
 : This mode is set on a team when you want to allow collaboration between incompatible segment users that the owner moderates. The team owner can add new members per their IB policy.
+Explicit
+: This mode is set on a team when you want to allow collaboration between the users who match with the segments associated with the Team and its connected resources - Microsoft 365 group and SharePoint site.
 Teams created before activating an IB policy in your tenant are automatically set to
 Open
 mode by default. When you activate IB policies on your tenant, you must update mode of your existing teams to
@@ -173,6 +175,21 @@ mode configuration on existing Teams-connected groups to meet compliance requirements for your organization, you need to
 update the IB modes
 for associated SharePoint sites connected to the Teams team.
+Explicit mode support for Teams and its connected Microsoft 365 group and SharePoint site (Preview)
+If you want to update a Teams-connected Microsoft 365 group from Implicit to Explicit mode, use the following PowerShell command:
+Set-UnifiedGroup <groupID> -InformationBarrierMode Explicit
+Once the Teams-connected Microsoft 365 group is updated from Implicit to Explicit mode,
+The segments on the group are automatically calculated based on the current members of the group and subsequently stamped on the group and the SharePoint site associated with it within 24 hours.
+The SharePoint site's access and sharing control will be based on the segments associated with the site.
+New users can be added to the Microsoft 365 group if they match the existing segments associated with the group.
+Managing segments from the explicit mode Team group
+:
+As an admin, you can remove existing segments from the explicit mode Microsoft 365 group. Once done, the users in the group who match with the removed segment will be automatically removed from the group members
```

---

### 12. Publish and deploy Copilot Studio agents

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Section:** Copilot Studio
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -6,10 +6,14 @@ Important
 This article includes information about
 Azure Bot Service skills
-, a code-based way to extend the capabilities of an agent in the standard harness. These skills shouldn't be confused with
-agentic skills
-in the Microsoft Copilot harness. Learn more about how to use agentic skills in
+, a code-based way to extend the capabilities of an agent in the standard harness. Azure Bot Service skills are different from:
+Agent skills
+, instruction-based skills that you add to agents powered by the GitHub Copilot or Customer Conversation harness. Learn more in
 Skills overview for agents
+.
+Plugin skills
+, a capability that a Microsoft 365 Copilot plugin can include. Learn more in
+Skills as plugin capabilities
 .
 By using Copilot Studio, you can publish agents that engage with your customers on multiple platforms or channels. For example, live websites, mobile apps, Microsoft Copilot, and messaging platforms like Teams and Facebook.
 Each time you update your agent, you can publish it again from within Copilot Studio. Publishing your agent applies to all the channels associated with your agent.

```

---

### 13. Microsoft Entra Agent ID documentation

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.17/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.17/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -44,8 +44,8 @@ Use an AI coding agent to automate the full Agent ID onboarding workflow.
 OAuth protocols for agents
 Understand how agents authenticate using OAuth 2.0 flows optimized for AI workloads.
-Configure third-party agents
-Integrate agents from platforms like AWS Bedrock and n8n with Agent ID.
+Choose an integration path
+Choose how to integrate an agent with Agent ID based on its platform and hosting model.
 Call Microsoft Graph API
 Access Microsoft 365 data and services from your agents.
 Microsoft Agent 365

```

---

### 14. Microsoft Entra Agent ID overview

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -30,6 +30,11 @@ Extending Microsoft Entra security features to agents requires Microsoft Agent 365. Agent 365 is included with Microsoft 365 E7 and is available as an add-on to Microsoft E5/A5/Business Premium (or Microsoft Defender Suite + Microsoft Purview Suite). See our latest
 Agent 365 product terms for more details
 .
+To build or connect an agent,
+choose an integration path
+. To administer an existing deployment, start with
+Manage agent identities
+and its owner, sponsor, and access controls.
 Related content
 Microsoft Entra security for AI overview
 What are agent identities?

```

---

### 15. Microsoft Sentinel overview

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/overview
**Section:** Microsoft Sentinel
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control index: Pillar 4: Operations & Monitoring
  - File: `controls/pillar-4-operations/index.md`
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,6 +19,17 @@ Collect data across all users, devices, applications, and infrastructure, both on-premises and in multiple clouds.
 Defender portal
 Azure portal
+To view Microsoft Sentinel data connectors, select
+Setup & configuration
+>
+Data management
+>
+Data & connectors
+, select the
+Connectors
+tab, and select
+Classic connectors - Microsoft Sentinel
+from the connector selector.
 This table highlights the key capabilities in Microsoft Sentinel for data collection.
 Capability
 Description

```

---

### 16. Microsoft Sentinel in the Microsoft Defender portal

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal
**Section:** Microsoft Sentinel
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -213,15 +213,9 @@ Logs
 Investigation & response
 >
-Hunting
->
 Advanced hunting
 News & guides
 Not available
-Search
-Microsoft Sentinel
->
-Search
 Threat management
 The following table lists the changes in navigation between the Azure and Defender portals for the
 Threat management
@@ -235,50 +229,23 @@ >
 Incidents
 Workbooks
-Microsoft Sentinel
->
-Threat management
+Dashboards & reports
 >
 Workbooks
 Hunting
-Microsoft Sentinel
->
-Threat management
->
-Hunting
+Investigation & response
+>
+Hunts
 Notebooks
-Microsoft Sentinel
->
-Threat management
+Investigation & response
 >
 Notebooks
-Entity behavior
-User entity page:
-Assets
->
-Identities
->
-{user}
->
-Sentinel events
-AND
-Device entity page:
-Assets
->
-Devices
->
-{device}
->
-Sentinel events
-Also, find the entity pages for the user, device, IP, and Azure resource entity types from incidents and alerts as they appear.
 Threat intelligence
 Threat intelligence
 >
-Intel management
+Intel explorer
 MITRE ATT&CK
-Microsoft Sentinel
->
-Threat management
+Threat intelligence
 >
 MITRE ATT&CK
 Content management
@@ -288,20 +255,14 @@ Azure portal
 Defender portal
 Content hub
-Microsoft Sentinel
->
 Content management
 >
 Content hub
 Repositories
-Microsoft Sentinel
->
 Content management
 >
 Repositories
 Community
-Microsoft Sentinel
->
 Content management
 >
 Community
@@ -309,42 +270,57 @@ The following table lists the changes in navigation between the Azure and Defender portals for the
 Configuration

```

---

### 17. Transition Microsoft Sentinel to the Defender portal

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender
**Section:** Microsoft Sentinel
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -427,13 +427,14 @@ table, accessible from the
 Advanced hunting
 page.
-Bookmarks aren't available in Advanced hunting, which provides a unified query experience across Microsoft Defender and Microsoft Sentinel data. However, bookmarks are still available in
-Microsoft Sentinel
->
-Threat management
->
-Hunting
-, which provides the Microsoft Sentinel-specific hunting experience. You can also use alternatives such as incident tags, saved queries, or custom hunting tables to preserve and track investigation context.
+Bookmarks aren't available in Advanced hunting, which provides a unified query experience across Microsoft Defender and Microsoft Sentinel data. However, bookmarks are still available in the Microsoft Sentinel-specific hunting experience:
+In Microsoft Sentinel:
+Microsoft Sentinel > Threat management > Hunting
+.
+In ISOC main navigation menu:
+Investigation & response > Hunts
+.
+You can also use alternatives such as incident tags, saved queries, or custom hunting tables to preserve and track investigation context.
 For more information, see
 Advanced hunting with Microsoft Sentinel data in Microsoft Defender
 , especially the list of

```

---

### 18. Manage data tiers and retention

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview
**Section:** Microsoft Sentinel
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -7,8 +7,14 @@ experience and explains how to use it to manage data in Microsoft Sentinel and Microsoft Defender XDR. For related tasks, see:
 Configure data connectors
 to send data to Microsoft Sentinel or Microsoft Defender XDR.
-Manage your existing tables and data
-.
+Manage tables, tiers, and retention in Sentinel
+.
+Manage tables, tiers, and retention in ISOC
+.
+Note
+If you use Integrated Security Operations Center (ISOC), see
+Data ingestion and billing for ISOC in Microsoft Defender
+for eligibility and included retention.
 Data & connectors in the Microsoft Defender portal (preview)
 Important
 The
@@ -96,93 +102,153 @@ Data you collect into Microsoft Sentinel and Microsoft Defender XDR is stored in tables. The
 Tables
 tab is where you view your tables, review their ingestion health, inspect their schema and transformations, and manage the retention period and storage costs associated with your data.
-Which tables can you manage in the Microsoft Defender portal?
-This section describes the table types you can manage in the Microsoft Defender portal.
-Table type
-Description
-Examples
-Is in Microsoft Sentinel workspace?
-Microsoft Sentinel
-Built-in tables, including:
-- Azure tables, such as AzureDiagnostics and SigninLogs.
-- Microsoft Sentinel tables.
--
-Microsoft Defender XDR integration with Microsoft Sentinel
-, which are created in your Microsoft Sentinel workspace when you increase the analytics retention period beyond 30 days. See the
-XDR
-table type for Defender XDR tables that are currently unsupported.
-- Azure tables:
-AzureDiagnostics
-,
-SigninLogs
-- Microsoft Sentinel tables:
-AWSCloudTrail
-,
-SecurityAlert
-- XDR tables:
-DeviceEvents
-,
-AlertInfo
-Yes
-Custom
-Tables you create manually or through jobs in your Microsoft Sentinel workspace, including summary rule and search job results tables, and custom data source tables.
-Tables with
-_CL
-or
-_SRCH
-suffixes.
-Yes
-XDR
-Tables in the XDR default tier, which have 30 d
```

---

### 19. Create workbooks

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/monitor-your-data
**Section:** Microsoft Sentinel
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -31,6 +31,8 @@ In Microsoft Sentinel, select
 Threat management > Workbooks
 .
+For ISOC customers: select
+Dashboards & Reports > Workbooks
 On the
 Workbooks
 page, select the

```

---

## HIGH: Control Review Recommended

### 1. Connect an existing MCP server to an agent

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
**Section:** Copilot Studio
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -10,8 +10,10 @@ (recommended)
 Create a custom connector to your server through Power Apps
 This article describes details for both of these methods.
-Alternatively, you can register your existing MCP server in Agents 365 using the Agents 365 CLI and Microsoft 365 Admin Center. Once the server is properly registered and approved, it becomes available for use in Copilot Studio. For more information, see
+Alternatively, you can register your existing MCP server with Microsoft Agent 365 (preview). You or a developer register the server by using the Agent 365 CLI. An admin then reviews and approves the request in the Microsoft 365 admin center and grants the required Microsoft Entra permissions. After approval and consent, the server can take up to 30 minutes to appear in your Copilot Studio environments. Learn more in
 Bring your own (BYO) MCP server
+and
+Review and approve MCP requests
 .
 If you don't yet have an MCP server set up, see
 Create a new MCP server
@@ -19,7 +21,7 @@ Supported transports
 In MCP,
 transports
-are the foundation for client-server communication. Transports handle the mechanics of sending and receiving messages. Currently, Copilot Studio supports the Streamable transport type.
+are the foundation for client-server communication. Transports handle the mechanics of sending and receiving messages. Copilot Studio supports the Streamable transport type.
 Note
 Given that SSE transport is
 deprecated
@@ -255,9 +257,14 @@ .
 Locate your connector file in the list of connectors and make the necessary updates using one of the available methods.
 MCP servers and data policies
-Access to MCP servers in Copilot Studio relies on Power Platform connectors for connectivity. This condition means that if a data policy regulates Power Platform connectors, it also regulates access to the MCP server and its tools for your agent. For more information, see
-configure a data policy
-.
+Access to MCP servers in Copilot Studio relies on Power Platform con
```

---

### 2. What's new in Microsoft Entra Agent ID

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,6 +1,24 @@ What's new in Microsoft Entra Agent ID
 Microsoft Entra Agent ID is now generally available. This release brings first-class identity and access management to AI agents, enabling organizations to authenticate, authorize, govern, and protect agent identities at enterprise scale. Microsoft Entra Agent ID extends Zero Trust principles to AI workloads with purpose-built identity constructs, specialized OAuth flows, and comprehensive security controls.
 This article summarizes the key capabilities and documentation currently available.
+Local agent authentication (preview)
+Microsoft Entra Agent ID now supports local agents as OAuth public clients. An agent running on an endpoint device can sign in a Microsoft Entra user and request delegated access to protected services by using the authorization code flow with PKCE, without storing or presenting a client credential.
+Authenticate a local agent with Microsoft Entra ID
+- Register a public-client Agent ID, configure MSAL, or use a CIMD URL as the client ID.
+Agent identity blueprint instance modes (preview)
+Agent identity blueprints can be configured for one Agent ID or multiple Agent IDs per tenant. A single-instance blueprint uses the same OAuth client ID for the blueprint and its one Agent ID in every tenant. A multi-instance blueprint can create a fleet of Agent IDs with distinct client IDs.
+Agent identity blueprint instance modes
+- Compare the two topologies and configure the immutable
+isSingleInstance
+setting.
+Client ID Metadata Document support (preview)
+Microsoft Entra ID now supports Client ID Metadata Documents (CIMD). CIMD lets an OAuth client use a public HTTPS metadata URL as its client ID. This model enables MCP clients to connect to Entra-protected MCP servers without requiring every client to be registered with Microsoft Entra ID in advance.
+Client ID Metadata Documents in Microsoft Entra ID
+- Learn how CIMD works, when to use it, and which limitations apply.
+Configure a
```

---

### 3. Manage Microsoft Entra agent identities

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin
**Section:** Agent Governance
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -96,7 +96,16 @@ View and manage agent identity blueprints in your tenant
 .
 Configure inheritable permissions for blueprints
-Inheritable permissions let agent identities automatically inherit OAuth 2.0 delegated permission scopes from their parent blueprint. When you configure inheritable permissions on a blueprint, newly created agent identities receive a base set of scopes without requiring interactive user or admin consent prompts.
+Inheritable permissions can make permissions granted to a blueprint principal available to its agent identities. The current Microsoft Graph beta reference documents delegated scope inheritance through
+inheritableScopes
+. The broader Agent ID permission model also describes application-role inheritance, but the public Graph reference doesn't define an application-role property or payload. Confirm Graph support before relying on application-role inheritance.
+Inheritance requires both a resource app to be configured as inheritable and the permission to be granted to the blueprint principal. Required resource access declares requested permissions for consent review; it doesn't grant access by itself. For static consent, include the permission in required resource access. For dynamic consent, explicitly request the permission. For details, see
+Inheritable permissions and required resource access
+and the
+Microsoft Graph
+inheritablePermission
+resource
+.
 Two inheritance patterns are supported per resource app:
 Pattern
 Description
@@ -105,10 +114,9 @@ All allowed scopes
 Inherit all available delegated scopes for the resource app. Newly granted scopes on the blueprint are automatically included.
 Start with enumerated scopes using only essential permissions, then expand as needed. This approach follows the principle of least privilege and makes it easier to audit which permissions agents actually use.
-Key limits:
-Maximum of 10 resource apps per blueprint.
-For enumerated scopes, maximum of 40 scopes per resource app
```

---

### 4. Microsoft Entra security for AI overview

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/security-for-ai-overview
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -5,7 +5,7 @@ Why AI systems need identity-based security
 Organizations are deploying AI agents for increasingly diverse tasks, and each deployment model presents distinct security challenges:
 Interactive agents
-Interactive agents perform specific tasks on demand on behalf of a signed-in user, often through a chat interface. Tasks include analyzing customer data for sales recommendations or answering support questions with escalation to human representatives. These agents are granted Microsoft Entra delegated permissions that allow them to act on behalf of users using the on-behalf-of (OBO) authentication flow. Common scenarios include customer support assistants, research helpers, and real-time collaboration agents.
+Interactive agents perform tasks on behalf of a signed-in user, often through a chat interface. Examples include analyzing customer data or answering support questions. Delegated permissions limit access to the permissions granted to the client and the user's own access. A local public client uses authorization code flow with PKCE. A hosted agent API receiving a user token uses the on-behalf-of (OBO) flow to call a downstream API as that user.
 Autonomous agents
 Autonomous agents operate independently using their own identity, not a human user's identity. These agents run in the background, making decisions and taking actions without human intervention, such as monitoring network logs for security operations, managing infrastructure deployments with autoscaling, or processing scheduled maintenance tasks. Autonomous agents authenticate directly with the Microsoft Entra ID platform using their agent identity and the client credentials flow.
 Agent's user account
@@ -60,9 +60,13 @@ Assign secure, scalable identities
 : The
 Microsoft Entra Agent identity platform
-enables you to assign identities to agents, autodiscover them across your organization, and manage all agent metadata in one place including capabilities, tasks, and protocols. It 
```

---

### 5. Microsoft Entra Agent identity platform

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -13,6 +13,11 @@ Extending Microsoft Entra security features to agents requires Microsoft Agent 365. Agent 365 is included with Microsoft 365 E7 and is available as an add-on to Microsoft E5/A5/Business Premium (or Microsoft Defender Suite + Microsoft Purview Suite). See our latest
 Agent 365 product terms for more details
 .
+To build or connect an agent,
+choose an integration path
+based on its platform and hosting environment. To administer existing identities, start with
+Manage agent identities
+.
 Platform architecture overview
 The Microsoft agent identity platform is built on several foundational technical components that work together to provide a complete identity and authorization solution for AI agents:
 Authentication service
@@ -20,7 +25,9 @@ SDKs
 : Software development kits that enable developers to integrate with the Microsoft agent identity platform. SDKs abstract the complexity of token acquisition and protocol handling, making it straightforward for platforms that build agents to incorporate identity management into their applications. Microsoft agent identity platform includes two SDKs: Microsoft Identity Web (.NET) and the Microsoft Entra ID Auth SDK (sidecar).
 Agent management
-: A comprehensive agent metadata store and administrative interface within the Microsoft Entra admin center that enables administrators to discover, view, configure, and manage agents. The platform provides the agent registry that is a centralized repository for registering and managing agents across an organization.
+: The Microsoft Entra admin center provides identity-management views for agent identities and blueprints. Microsoft Agent 365 provides the broader organizational agent registry. For which experience to use, see
+Agent registry convergence
+.
 These technical components work together with the identity constructs described in the following section to provide complete platform functionality.
 Authentication and authorization
 The Microsoft agent 
```

---

### 6. Microsoft Entra Agent ID sign-in and audit logs

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/sign-in-audit-logs-agents
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -188,7 +188,7 @@ Microsoft Entra Agent ID logs can be viewed and managed using Microsoft Graph on the
 /beta
 endpoint.
-To get started, follow these instructions to work with recommendations using Microsoft Graph in Graph Explorer.
+To get started, use Graph Explorer to query sign-in logs.
 Sign in to
 Graph Explorer
 .
@@ -199,9 +199,9 @@ beta
 .
 Retrieve agent identity sign-in events
-To retrieve only sign-in events where Microsoft Entra Agent ID was involved, you need to find events initiated by a service principal where the agent type is
+This request is limited to service principal sign-in events where the agent type is
 AgentIdentity
-. Use the following Microsoft Graph request:
+. It doesn't retrieve all agent-related sign-in types. The Microsoft Graph API documents separate event-type filters for sign-in categories, so use the filter that matches the sign-in flow you need to investigate. For example, use the following request for the service-principal category:
 GET https://graph.microsoft.com/beta/auditLogs/signIns?$filter=signInEventTypes/any(t: t eq 'servicePrincipal') and agent/agentType eq 'AgentIdentity'
 Was this page helpful?
 Yes

```

---

### 7. Microsoft Entra ID Governance for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,6 +1,9 @@-Governing Agent Identities
-Microsoft Entra allows you to ensure that the right people have the right access to the right apps and services at the right time. With the addition of the Microsoft agent identity platform, managing the access rights of agents in the same way is just as important in the governance lifecycle of your organization's identities. The Microsoft agent identity platform introduces the concept of Agent Identities (IDs). Agent identities are accounts within Microsoft Entra ID that provide unique identification, authentication and authorization capabilities for AI agents.
-This allows agent identities to be governed with Microsoft Entra features in the same style as you would govern human identities. With Agent identities, you can govern and manage the identity and access lifecycle of agents, ensuring the agents have a responsible person providing oversight throughout the agent lifecycle and agent's access does not persist longer than it is needed. This article provides an overview of how Microsoft Entra can be utilized to govern agent identities and access.
+Governing Agent identities and access
+Microsoft Entra allows you to ensure that the right people have the right access to the right apps and services at the right time. Microsoft Entra ID Governance features enable governing the identity and access lifecycle for employees and business guests. With the addition of the Microsoft agent identity platform, managing the access rights of agents in the same way is just as important in the governance lifecycle of your organization's identities. The Microsoft agent identity platform introduces the concept of Agent Identities (IDs). Agent identities are accounts within Microsoft Entra ID that provide unique identification, authentication and authorization capabilities for AI agents.
+This allows agent identities to be governed with Microsoft Entra features in the same style as you would govern human identities. With Agent identit
```

---

### 8. Microsoft Entra Agent ID best practices

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/best-practices-agent-id
**Section:** Agent Governance
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -4,28 +4,32 @@ What is Microsoft Entra Agent ID?
 and
 Key concepts
-.
+. To build an agent, start with
+Choose an integration path
+; you don't need to complete architecture planning before following a tutorial.
 Design agent identity blueprints
 Agent identity blueprints
-are templates that define the security posture for all agent instances of a common kind. Thoughtful blueprint design is the foundation of well-governed agent deployments.
+define authentication settings and the security posture for one or more agents. Thoughtful blueprint design is the foundation of well-governed agent deployments.
 Plan blueprints before deploying agents.
 Define required settings, permissions, and metadata in the blueprint up front rather than creating ad-hoc service principals. This ensures a consistent, governed rollout across all instances. For guidance on structuring your identity model, see
 Plan your agent identity architecture
 .
-Provision a unique identity per agent instance.
-Avoid sharing identities between different agents. Distinct identities improve traceability and let you disable or update one agent without impacting others. The blueprint model makes scaling with unique identities manageable because credentials live on the blueprint, not each instance. For instructions, see
+Give separately managed agents distinct identities.
+Separate identities when agents need independent access, accountability, or lifecycle controls. Multiple replicas, processes, or user sessions of the same logical agent don't by themselves require new identities. For fleet provisioning, see
 Create and delete agent identities
 .
 Assign a sponsor and an owner at creation time.
 Every blueprint and agent identity must have a
 sponsor
-; the person or group accountable for the agent's purpose. Assign an owner (technical admin) as well. Periodically verify that these assignments are current, especially when personnel changes occur.
+, the person or supported group accountable for t
```

---

### 9. Create analytics rules

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/create-analytics-rules
**Section:** Microsoft Sentinel
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -65,9 +65,9 @@ For Microsoft Sentinel in the
 Defender portal
 , select
-Microsoft Sentinel
+Investigation & response
 >
-Configuration
+Detection
 >
 Analytics
 . For Microsoft Sentinel in the

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. What's new in Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
**Classification:** MEDIUM (General content update)

---

### 2. Get started with Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Classification:** MEDIUM (General content update)

---

### 3. Sign-in risk-based policies
**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-sign-in
**Classification:** MEDIUM (General content update)

---

### 4. Learn about information barriers
**URL:** https://learn.microsoft.com/en-us/purview/information-barriers
**Classification:** MEDIUM (General content update)

---

### 5. Publish and deploy Copilot Studio agents
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Classification:** MEDIUM (General content update)

---

### 6. Microsoft Entra Agent ID documentation
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/
**Classification:** MEDIUM (General content update)

---

### 7. Microsoft Entra Agent ID overview
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
**Classification:** MEDIUM (General content update)

---

### 8. Microsoft Entra agent identity concepts
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities
**Classification:** MEDIUM (General content update)

---

### 9. Integrate third-party agents with Microsoft Entra Agent ID
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/configure-third-party-agents
**Classification:** CRITICAL (Deprecation notice)

---

### 10. Agent Registry convergence with Microsoft Agent 365
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence
**Classification:** MEDIUM (General content update)

---

### 11. Create workbooks
**URL:** https://learn.microsoft.com/en-us/azure/sentinel/monitor-your-data
**Classification:** MEDIUM (General content update)

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