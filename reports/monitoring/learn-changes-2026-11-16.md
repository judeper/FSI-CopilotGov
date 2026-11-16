# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-16
**Run Time:** 2026-11-16T19:55:48.091529+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 9 |
| HIGH Changes | 3 |
| MEDIUM Changes | 8 |
| Redirects | 32 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 3 | .../microsoft-365/copilot/extensibility/ | MEDIUM | 2.16, 4.13 | Update portal-walkthrough |
| 4 | overview-copilot-connector | MEDIUM | None | Review optional |
| 5 | overview-declarative-agent | MEDIUM | 2.14, 1.13 | Update portal-walkthrough |
| 6 | agent-builder-build-agents | MEDIUM | 1.13, 2.14, 4.13 | Update portal-walkthrough |
| 7 | agent-builder | HIGH | None | Review and update |
| 8 | knowledge-sources | HIGH | 1.13, 2.14, 4.13 | Update portal-walkthrough |
| 9 | prerequisites | HIGH | None | Review and update |
| 10 | code-interpreter | MEDIUM | 1.13, 2.14, 4.13 | Update portal-walkthrough |
| 11 | image-generator | MEDIUM | 1.13, 2.14, 4.13 | Update portal-walkthrough |
| 12 | agent-registry | HIGH | 2.14, 4.13, 4.14, 1.13, 2.13 | Update portal-walkthrough |
| 13 | agents-are-apps | HIGH | None | Review and update |
| 14 | data-privacy-security | MEDIUM | None | Review optional |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (UI element names)

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
--- +++ @@ -19,12 +19,16 @@ Note
 The
 Home
-tab provides a unified starting point for Chat and Cowork in the Copilot app. Users can switch between Chat and Cowork from either the
-left navigation or the prompt box
-. Cowork and Code require a
-Microsoft 365 Copilot license
-and an
+tab provides a unified starting point for Chat and Cowork in the Copilot app. Users can switch between experiences from either the left navigation or the prompt box. Access to Cowork and Code capabilities depends on
+licensing
+, and
 assigned usage-based billing policy
+. If a usage-based experience requires a spending policy, the user is prompted to either
+Request access
+or
+Learn more
+, based on the organization's
+Access requests to usage-based billing policy
 .
 Compare Microsoft 365 Copilot licenses
 Note

```

---

### 2. What's new in Copilot Cowork

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
--- +++ @@ -13,6 +13,10 @@ OneNote support
 Read OneNote notebooks and, when editing is available, update pages with your approval.
 Work with OneNote notebooks
+Enhancements
+Added
+Plan and implement business processes with Copilot Cowork
+, guidance for choosing an implementation approach based on business outcomes, evidence, and controls and using a pilot to decide whether to expand.
 October 2026
 New features
 Feature

```

---

### 3. Copilot extensibility overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.16: Control 2.16: Federated Copilot Connector and Model Context Protocol (MCP) Governance
  - File: `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,22 +1,33 @@-Extending Microsoft 365 Copilot with plugins
-Create a plugin from existing capabilities with Work IQ Dev Tools, or follow the complete lifecycle to prepare, build, test, publish, govern, update, and retire a plugin.
-Get started with plugins
-Get started
+Extend Microsoft 365 Copilot with Plugins
+Build and manage plugins for Microsoft 365 Copilot, from planning through publishing and retirement.
+Prepare
+Overview
 What is a plugin?
-Quickstart: Create your first plugin with Work IQ Dev Tools
-Prepare to build your plugin
-Build and test plugins
+Compare plugins and Copilot-powered apps
+Browse the Copilot Plugin Catalog
 How-To Guide
+Plan your plugin
+Choose capabilities
+Choose development tools
+Build or reuse
+How-To Guide
+Quickstart: Package an existing declarative agent as a plugin with Work IQ Dev Tools
 Build or reuse capabilities
+Build a plugin with Work IQ Dev Tools
+Package & test
+How-To Guide
 Package and test
-Build a plugin with Work IQ Dev Tools (GitHub)
 Validate and test your plugin
-Publish and make plugins available
+Publish & distribute
 How-To Guide
 Publish or share
 Configure plugin CI/CD with Work IQ Dev Tools
-Make available and govern
-Monitor, update, and retire plugins
+Make available, govern & use
+How-To Guide
+Make your plugin available
+Govern plugin access and connections
+Use plugins with Copilot Cowork
+Monitor, update & retire
 How-To Guide
 Monitor your plugin
 Improve and update your plugin

```

---

### 4. Declarative agents for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`

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
--- +++ @@ -1,5 +1,8 @@ Declarative agents for Microsoft 365 Copilot
-Declarative agents provide a goal-directed conversational experience that's powered by Microsoft 365 Copilot. You define the agent's purpose, instructions, knowledge, and supported actions to address a business scenario. A plugin can include or reference an agent with other supported capabilities, such as skills, Copilot connectors, or MCP-based tools.
+Declarative agents provide a goal-directed conversational experience that's powered by Microsoft 365 Copilot. You define the agent's purpose, instructions, knowledge, and supported actions to address a business scenario.
+A declarative agent can be one component of a plugin. For how agents fit with skills, tools, and other capabilities, see
+Plugins for Microsoft 365 Copilot
+.
 Choose a declarative agent when users need a dedicated conversational experience with behavior and capabilities tailored to a specific outcome. You don't need to create an agent when an existing Microsoft experience or approved agent can use the selected skills, connectors, or tools.
 Note
 For information about the two approaches to building agents for Microsoft 365 Copilot, see
@@ -63,12 +66,11 @@ : Limited support - only pro-code agents built with Microsoft 365 Agents Toolkit are supported. Agent Builder isn't available for declarative agents in DoD.
 Related content
 Choose capabilities for your plugin
-Agent in-app experiences
 Declarative agent architecture
 Declarative agents FAQ
 Choose development tools for your plugin
 Build agents with Agent Builder
-Build agents with Microsoft 365 Agents Toolkit
+Build agents with Work IQ Dev Tools (recommended for supported pro-code scenarios)
 Responsible AI validation checks
 Was this page helpful?
 Yes

```

---

### 5. Build agents with Agent Builder

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -202,6 +202,11 @@ New chat
 to start a new conversation with the agent to view the suggested prompts again.
 Next step
+If you're including the agent in a plugin package, see
+Package your plugin
+. For direct sharing and other distribution options, see
+Choose how to publish and distribute your plugin
+. Not every sharing scenario requires a ZIP package.
 Share and manage agents built in Agent Builder
 Was this page helpful?
 Yes

```

---

### 6. Declarative agent knowledge sources

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/knowledge-sources
**Section:** Copilot Extensibility
**Classification:** HIGH (UI element names)

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
--- +++ @@ -1,4 +1,13 @@ Add knowledge sources to your declarative agent
+Tip
+Recommended:
+Start with
+Work IQ Dev Tools
+for supported pro-code declarative-agent and plugin scenarios. See the
+WIQD quickstart
+. Toolkit-based instructions remain available for existing projects and workflows that require them. Check
+capability and target-experience support
+before choosing a tool: WIQD doesn't target custom engine agents.
 You can enhance the user experience of your declarative agent by adding capabilities like
 code interpreter
 and
@@ -11,6 +20,9 @@ The following table lists the capabilities and knowledge sources you can configure by using Agent Builder in Microsoft 365 Copilot or
 Microsoft 365 Agents Toolkit
 and indicates whether users require a Microsoft 365 Copilot license or metered usage to access agents with that capability or knowledge source.
+This table describes the Agent Builder and Toolkit configuration paths, not WIQD feature coverage. For the recommended pro-code route, confirm the supported configuration in the
+WIQD documentation
+.
 Capability or knowledge source
 Agent Builder
 Agents Toolkit

```

---

### 7. Code interpreter capability

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -1,4 +1,13 @@ Add the code interpreter capability to your agent
+Tip
+Recommended:
+Start with
+Work IQ Dev Tools
+for supported pro-code declarative-agent and plugin scenarios. See the
+WIQD quickstart
+. Toolkit-based instructions remain available for existing projects and workflows that require them. Check
+capability and target-experience support
+before choosing a tool: WIQD doesn't target custom engine agents.
 You can enhance the user experience of your declarative agents for Microsoft 365 Copilot by adding the code interpreter capability. The
 capabilities
 element

```

---

### 8. Image generator capability

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/image-generator
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -1,4 +1,13 @@ Add the image generator capability to your agent
+Tip
+Recommended:
+Start with
+Work IQ Dev Tools
+for supported pro-code declarative-agent and plugin scenarios. See the
+WIQD quickstart
+. Toolkit-based instructions remain available for existing projects and workflows that require them. Check
+capability and target-experience support
+before choosing a tool: WIQD doesn't target custom engine agents.
 The image generator capability enables declarative agents for Microsoft 365 Copilot to generate images based on user prompts. Image generator uses the existing
 Designer
 functionality to create visually appealing and contextually relevant graphics, and includes the following features:

```

---

### 9. Agent registry in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
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
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -2,6 +2,19 @@ The agent registry in
 Microsoft 365 admin center
 provides a centralized view of all agents available for your organization. This list helps you monitor, manage, and govern agents for your organization.
+In this article,
+Registry
+refers to the agent inventory under
+Agents
+>
+All agents
+>
+Registry
+in the Microsoft 365 admin center. Use this inventory to manage agent records and their lifecycle. To manage plugins, skills, and MCP servers, use
+Agents
+>
+Tools
+.
 View agent registry
 Sign in to the
 Microsoft 365 admin center
@@ -113,7 +126,7 @@ Tip
 If you don't see the agents that you expect to see in the agent registry list, check to make sure you don't have an existing filter set.
 Certain columns allow you to sort the agent registry list. To sort the list, select the column title.
-Applying filters to the list of agents will not change the
+Applying filters to the list of agents doesn't change the
 Total agents
 count.
 Agent registry actions
@@ -145,7 +158,7 @@ Registry
 .
 Tip
-In addition to the above actions, you can change the view of the list from
+In addition to the preceding actions, you can change the view of the list from
 Normal list
 to
 Compact list
@@ -159,7 +172,7 @@ To help administrators manage these scenarios, the Microsoft 365 admin center enables you to identify and manage ownerless shared agents. The dashboard displays the total count of such agents, a one-click filter to quickly isolate them, and real-time updates that reflect user deletions. When administrators use these features, they can efficiently review and address ownership gaps by blocking or deleting affected agents.
 When you select the
 Agents without owners
-card, the agent list will be filtered to show the agents based on
+card, the agent list is filtered to show the agents based on
 Publisher type
 and
 Owner
@@ -220,7 +233,9 @@ Agents at risk tile
 The
 Agents at risk
-tile on the All agents page displays the total number of agents in the tena
```

---

## HIGH: Control Review Recommended

### 1. Agent Builder capabilities

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -22,6 +22,10 @@ . If your scenario requires a separate pro-code implementation, see
 Choose development tools for your plugin
 .
+Plan your plugin
+If your agent will be part of a plugin,
+choose the capabilities your plugin needs
+before you build.
 Licensing
 Access to Agent Builder, and the capabilities you can add to an agent, depend on the licenses assigned in your tenant. For details, see
 Agent capabilities and licensing models
@@ -45,8 +49,8 @@ Plan data, privacy, and security for Microsoft 365 Copilot extensibility
 .
 Admin controls
-Administrators can control whether Agent Builder is available to users in their organization. For information about agent admin controls, see
-Manage agents for Microsoft 365 Copilot in Integrated Apps
+Creating agents in Agent Builder is a core Copilot capability when agents are enabled. Administrators can't disable agent creation in Agent Builder separately while keeping agents enabled. They can control agent access, org-wide sharing, and approval for catalog publishing. For details, see
+Governance and admin controls
 . For the broader post-publishing model, see the
 Manage plugins with Microsoft Agent 365
 administration map.

```

---

### 2. Agent capabilities and licensing models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites#agent-capabilities-and-licensing-models
**Section:** Copilot Extensibility
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -1,7 +1,11 @@ Set up your development environment for your plugin
-Use the development plan from
+During
+Prepare
+, use the development plan from
 Choose development tools
-to prepare the environments, accounts, tools, identities, permissions, connections, and services required by your plugin components.
+to set up the environments, accounts, tools, identities, permissions, connections, and services required by your plugin components. You finish with verified access and tool prerequisites so you can return to
+Build or reuse
+.
 Complete this setup before you build, configure, extend, or reuse the components. You might need more than one environment or tool when the plugin combines agents, skills, connectors, and MCP-based capabilities.
 Start with the development plan
 For every component, confirm:
@@ -70,19 +74,28 @@ Some agent capabilities are only available to users in tenants with Copilot Studio pay-as-you-go billing enabled (consumed as Copilot Credits) or users with Microsoft 365 Copilot licenses. For example, if you want to build agents that are grounded in organizational data, you need to enable pay-as-you-go billing or purchase a Microsoft 365 Copilot license.
 Work IQ Dev Tools requirements
 Work IQ Dev Tools
-is a preview pro-code route for supported declarative-agent and plugin-package scenarios. Before you install it, confirm:
+is generally available and is the default professional-developer route for supported declarative-agent and plugin scenarios. First review
+Choose development tools for your plugin
+, then add Toolkit or another component-specific tool only when the scenario requires it. Confirm:
 Node.js 24.15 or later and npm on your
 PATH
 for CLI and installation-script execution. The installer doesn't install Node.js. These aren't required just to begin conversational or file-based authoring.
 PowerShell 7 or later on Windows.
 A Microsoft 365 account with access to Copilot.
-An Azure subscription when you provision agents.
+An A
```

---

### 3. Microsoft 365 Copilot agent governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,48 +1,123 @@ What is a Microsoft 365 Copilot plugin?
-A Microsoft 365 Copilot plugin is an installable package that brings together capabilities for a specific task. It can include supported agents and skills, along with configuration or references for connectors and remote MCP servers.
+A plugin is an installable package that adds new capabilities to Microsoft 365 Copilot and other Microsoft AI experiences. It brings together the skills, tools, and optional agents needed for a job in one unit that people can find, install, share, and manage.
 For example, a support plugin might use an agent to answer questions, a skill to guide troubleshooting, a connector to find support content, and an MCP server to provide tools.
-You build or reuse the capabilities, package and test the plugin, then publish or share it with the people who need it.
+A plugin can contain one capability or several; a single packaged skill is also a plugin. External services, such as remote MCP servers, can run separately from the package.
+Before building a new plugin, browse the
+Copilot Plugin Catalog
+, a public registry of available plugins.
 What can a plugin include?
 Choose what your plugin needs based on the task it should help users complete.
 Capability
 What it does
 Learn more
-Declarative agent
-Provides a focused assistant with instructions, knowledge, and tools.
+Skills
+Provide reusable instructions for a task, packaged in a directory that contains
+SKILL.md
+.
+Skills in declarative agents
+Tools
+Connect to apps and data, including supported Copilot connectors and remote MCP integrations.
+Copilot connectors
+and
+MCP servers
+Agents
+Provide specialized assistants for a role or workflow; today, these are declarative agents.
 Declarative agents overview
-Skill
-Provides reusable instructions or a workflow for a specific job.
-Skills as plugin capabilities
-Copilot connector
-Makes external organizational content available.
-Copilot connectors as plugin capabilities

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. What's new in Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
**Classification:** MEDIUM (General content update)

---

### 2. Copilot extensibility overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Classification:** MEDIUM (General content update)

---

### 3. Microsoft Graph connectors overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json
**Classification:** MEDIUM (General content update)

---

### 4. Declarative agents for Copilot
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
**Classification:** MEDIUM (General content update)

---

### 5. Build agents with Agent Builder
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
**Classification:** MEDIUM (General content update)

---

### 6. Code interpreter capability
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter
**Classification:** MEDIUM (General content update)

---

### 7. Image generator capability
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/image-generator
**Classification:** MEDIUM (General content update)

---

### 8. Copilot agent security and compliance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security
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
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide | https://learn.microsoft.com/en-us/copilot/manage/copilot-tuning-admin-guide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*