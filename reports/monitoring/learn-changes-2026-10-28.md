# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-28
**Run Time:** 2026-10-28T16:21:46.971137+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 4 |
| HIGH Changes | 2 |
| MEDIUM Changes | 1 |
| Redirects | 21 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | HIGH | 4.12, 3.8a | Update portal-walkthrough |
| 2 | dlp-policy-reference | HIGH | None | Review and update |
| 3 | ...osoft365-copilot-location-learn-about | HIGH | 1.5, 2.1, 2.6 | Update portal-walkthrough |
| 4 | overview-declarative-agent | MEDIUM | 1.13, 2.14 | Update portal-walkthrough |
| 5 | agent-builder-build-agents | HIGH | 1.13, 2.14, 4.13 | Update portal-walkthrough |
| 6 | agent-builder | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -7,6 +7,304 @@ Android
 iOS
 Mac
+October 27, 2026
+Updates released between October 13, 2026, and October 27, 2026.
+Microsoft 365 Copilot
+Learning Agent in Microsoft 365 Copilot
+[Windows]
+The Learning agent helps employees build skills through personalized microlearning and structured learning experiences.
+Roadmap ID:
+490154
+Details:
+What changed:
+Microsoft 365 Copilot now includes a Learning agent that helps employees discover personalized learning opportunities. The experience supports both microlearning content and structured learning paths, making it easier to find skill-building resources within the flow of work and upskill on Copilot.
+Why:
+Learning Agent makes continuous upskilling part of everyday work by delivering personalized, role- and task-relevant learning directly in Copilot. It helps employees discover what to learn, learn through real work, practice skills, identify gaps, and follow structured learning plans, enabling organizations to build AI fluency and role-based skills at scale.
+Try this:
+Open
+https://aka.ms/LearningAgent/add
+Click on any cards present on the home page or ask anything to learn/upskill
+Why this matters:
+Personalized learning guidance helps employees discover relevant training without extensive searching.
+Business impact:
+Organizations can support workforce skill development by helping employees find relevant learning resources more efficiently.
+Personal impact:
+Users can identify useful learning opportunities faster and spend more time building skills.
+Learn
+Learning Agent
+Overview of Learning agent
+Insights - New Copilot Metrics Available
+[Web]
+We are bringing a set of new Copilot metrics including actions taken in Microsoft 365 Copilot app, Edge and OneNote, and more key use cases across Outlook, Word, Excel, and PowerPoint including suggested reply, translate, coach, clean data and more. This will empower customers to more deeply understand the key Copilot adoption cases in Copilot Dashboa
```

---

### 2. DLP for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.6/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.6/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -251,9 +251,46 @@ Updates to a DLP policy can take up to four hours to reflect in Microsoft 365 Copilot and Copilot Chat experience.
 Admin units
 The
-Microsoft 365 Copilot and Copilot Chat
-policy location doesn't support
+Microsoft Copilot and Chat
+policy location supports
+administrative units
+. You can scope a Copilot DLP policy to a region or department and delegate policy management to administrators assigned to those units, without granting tenant-wide policy management permissions.
+Note
+Administrative unit support for this location is rolling out. The option might not yet be available in your tenant.
+Tip
+Use administrative units when regional or departmental administrators need to manage Copilot DLP policies for their own users.
+Before you create a scoped policy,
+configure administrative units
+in Microsoft Entra ID and assign them to the appropriate Microsoft Purview role group members. Administrators still need the DLP permissions required to create and manage policies.
+To scope a Copilot DLP policy:
+In the
+Microsoft Purview portal
+, go to
+Data Loss Prevention
+>
+Policies
+and select
++ Create policy
+.
+Select the
+Custom
+template, then
+Custom policy
+, and enter a name and description.
+On the
 Admin units
+page, select the administrative units for the policy.
+Select the
+Microsoft Copilot and Chat
+location and choose the users and groups to include or exclude within the selected administrative units.
+Configure the rule conditions and actions, review the settings, and save the policy.
+An administrative unit restricted administrator can select only their assigned units and manage policies within that scope. An unrestricted administrator can scope policies to administrative units or keep
+Full directory
+to apply a policy across the organization. Existing tenant-wide policies continue to apply; using administrative units is optional.
+Important
+Copilot DLP policy scoping is based on the user who submits the prompt, not the 
```

---

### 3. Declarative agents for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
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
--- +++ @@ -1,5 +1,5 @@ Declarative agents for Microsoft 365 Copilot
-Declarative agents provide a goal-directed conversational experience that is powered by Microsoft 365 Copilot. You define the agent's purpose, instructions, knowledge, and supported actions to address a business scenario. A plugin can include or reference an agent with other supported capabilities, such as skills, Copilot connectors, or MCP-based tools.
+Declarative agents provide a goal-directed conversational experience that's powered by Microsoft 365 Copilot. You define the agent's purpose, instructions, knowledge, and supported actions to address a business scenario. A plugin can include or reference an agent with other supported capabilities, such as skills, Copilot connectors, or MCP-based tools.
 Choose a declarative agent when users need a dedicated conversational experience with behavior and capabilities tailored to a specific outcome. You don't need to create an agent when an existing Microsoft experience or approved agent can use the selected skills, connectors, or tools.
 Note
 For information about the two approaches to building agents for Microsoft 365 Copilot, see
@@ -23,7 +23,7 @@ Declarative agent architecture
 .
 Understand what the agent contributes
-A declarative agent is defined by configuration that describes:
+You define a declarative agent by configuration that describes:
 Identity and behavior
 : The agent's name, purpose, instructions, conversation starters, constraints, and visual representation.
 Knowledge
@@ -36,7 +36,7 @@ Decide whether to build or reuse
 Before you build an agent:
 Review agents that are already approved for the target users and experiences.
-Determine whether an existing agent can be reused, copied, configured, or extended.
+Determine whether you can reuse, copy, configure, or extend an existing agent.
 Confirm who owns the agent instructions, knowledge, connections, and support.
 Identify any gaps that require a new agent.
 If you reuse an agent, c
```

---

### 4. Build agents with Agent Builder

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
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
--- +++ @@ -163,9 +163,9 @@ . If your scenario requires a separate pro-code implementation, see
 Choose development tools for your plugin
 .
-Skills (preview)
-You can add skills to an agent built in Agent Builder, either by providing a skill package or by describing the skill in natural language. Skills in Agent Builder are in preview and are available only to organizations enrolled in the Microsoft Frontier Program. For more information, see
-Add custom skills to your declarative agent in Agent Builder (preview)
+Skills
+You can add skills to an agent built in Agent Builder, either by providing a skill package or by describing the skill in natural language. For more information, see
+Add skills to your declarative agent in Agent Builder
 .
 Set the default response mode
 In the

```

---

## HIGH: Control Review Recommended

### 1. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -919,8 +919,8 @@ policy template
 - Set up a
 Microsoft Defender for Cloud Apps connector
-Microsoft 365 Copilot (preview)
-No
+Microsoft Copilot and Chat (preview)
+Yes (rolling out)
 Account or Distribution group
 data-at-rest
 data-in-use

```

---

### 2. Agent Builder capabilities

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -8,8 +8,8 @@ You can specify dedicated knowledge sources, including content on SharePoint and information provided by
 Copilot connectors
 . You can also test the agent before you use, share, or publish it.
-Agent Builder also lets you add skills to an agent you build in Agent Builder, either by providing a skill or by creating one through natural language. Skills in Agent Builder are in preview and available only to organizations enrolled in the Microsoft Frontier Program. For more information, see
-Add custom skills to your declarative agent in Agent Builder (preview)
+Agent Builder also lets you add skills to an agent you build in Agent Builder, either by providing a skill or by creating one through natural language. For more information, see
+Add skills to your declarative agent in Agent Builder
 .
 You can build agents from the following apps and sites:
 microsoft365.com/chat
@@ -129,7 +129,7 @@ Build your first agent
 Build agents in Agent Builder
 Agent Builder templates
-Add custom skills to your declarative agent in Agent Builder (preview)
+Add skills to your declarative agent in Agent Builder
 Share and manage agents built in Agent Builder
 Agent Builder regional availability and language support
 Copy an agent from Agent Builder to Copilot Studio

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Declarative agents for Copilot
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
**Classification:** MEDIUM (General content update)

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