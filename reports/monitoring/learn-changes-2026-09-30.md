# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-30
**Run Time:** 2026-09-30T16:09:47.800975+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 7 |
| HIGH Changes | 4 |
| MEDIUM Changes | 1 |
| Redirects | 3 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 2 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | 4.15 | Update portal-walkthrough |
| 3 | cowork-faq | MEDIUM | 4.15 | Update portal-walkthrough |
| 4 | .../microsoft-365/copilot/extensibility/ | HIGH | 2.16, 4.13 | Update portal-walkthrough |
| 5 | overview-copilot-connector | HIGH | None | Review and update |
| 6 | overview-declarative-agent | HIGH | 1.13, 2.14 | Update portal-walkthrough |
| 7 | agent-builder-build-agents | HIGH | 1.13, 2.14, 4.13 | Update portal-walkthrough |
| 8 | agent-builder | HIGH | None | Review and update |
| 9 | agent-settings | HIGH | 1.13, 2.16, 2.13, 2.14, 4.13 | Update portal-walkthrough |
| 10 | agents-are-apps | HIGH | None | Review and update |
| 11 | data-privacy-security | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -5359,6 +5359,9 @@ Friendly name
 Operation
 Description
+Added agentic policy
+PolicyAdded
+An agentic policy was added.
 Added Company Admin
 AddCompanyAdmin
 A user was added to the Company Admin role.
@@ -5377,18 +5380,39 @@ Company Admin Logged Out
 AdminLogout
 A Company Admin user logged out of Viva Glint.
+Completed agentic campaign
+CampaignCompleted
+An agentic campaign was completed.
+Created agentic campaign
+CampaignCreated
+An agentic campaign was created.
 Created User Role
 RoleCreated
 Glint User Role creation activity.
+Deleted agentic campaign
+CampaignDeleted
+An agentic campaign was deleted.
+Deleted agentic policy
+PolicyDeleted
+An agentic policy was deleted.
+Deleted retained agentic campaign data
+CampaignRetentionDeleted
+Retained agentic campaign data was deleted.
 Deleted Support Access
 GlintSupportAccessDeleted
 A user was removed from the Support User role.
 Deleted System
 GlintSystemDeleted
 The Viva Glint system was deleted.
+Deleted tenant data for a DSR request
+DsrTenantDeleted
+Tenant data was deleted for a data subject rights (DSR) request.
 Deleted User
 GlintUserDeleted
 Viva Glint user deletion activity.
+Deleted user data for a DSR request
+DsrUserDeleted
+User data was deleted for a data subject rights (DSR) request.
 Disabled Advanced Configuration Access
 UserAdvConfigDisabled
 A Company Admin user disabled Advanced Configuration access in Viva Glint.
@@ -5440,6 +5464,9 @@ Exported User Data
 UserDataExport
 Employee data export activity.
+Generated agentic campaign report
+ReportGenerated
+An agentic campaign report was generated.
 Imported Glint 360 Feedback
 GlintFeedbackProgramImport
 360 Feedback program data import activity.
@@ -5452,21 +5479,39 @@ Imported Glint User Role
 GlintRoleImport
 User Role employee data activity.
+Launched agentic campaign
+CampaignLaunched
+An agentic campaign was launched.
 Removed Company Admin
 RemoveCompanyAdmin
 A user was removed from the Company Admin role.
 Reopened S
```

---

### 2. Copilot Cowork overview

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
--- +++ @@ -22,6 +22,8 @@ : Drafts stakeholder communications such as status updates and announcements.
 Schedules prompts
 : Runs prompts on a schedule so recurring tasks happen automatically.
+Allows faculty and staff in the education industry to complete multi-step work across Microsoft 365
+: Prepares course materials, coordinates research and grant work, prepares materials for department or curriculum meetings, and other tasks.
 Create apps (Frontier)
 : Use the App skill to build lightweight, interactive apps from a description. There's no coding required. You can refine the app in chat, open, publish, and share it with your stakeholders.
 Cowork shows each step in your session, so you can follow along as it works.
@@ -81,7 +83,7 @@ . Cowork discovers your custom skills automatically at the start of each session. You can create up to 50 custom skills.
 As Cowork loads skills during a session, the side panel updates to show which skills are active.
 Extend with plugins
-Cowork supports plugins from the Microsoft 365 App Store that add new skills and connectors. Plugins can give Cowork specialized expertise-such as financial analysis or legal research-or connect it to external data sources and services. Your organization's admin can also deploy plugins for everyone in your organization.
+Cowork supports plugins from the Microsoft 365 App Store that add new skills and connectors. Plugins can give Cowork specialized expertiseâsuch as financial analysis or legal researchâor connect it to external data sources and services. Your organization's admin can also deploy plugins for everyone in your organization.
 Learn more about browsing, installing, and managing plugins in
 Use plugins with Cowork
 .
@@ -108,7 +110,7 @@ Watch Cowork work
 : Cowork breaks your request into steps and works through them one by one. You can follow along as each step appears in the session.
 Interrupt, steer, or pause the session
-: At any point, you can interrupt Cowork to give it addi
```

---

### 3. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
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
--- +++ @@ -1,19 +1,19 @@ Copilot Cowork common questions
 Find answers to common questions about Microsoft Copilot Cowork.
 What is Cowork?
-Cowork is available in Microsoft Copilot. It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multi-step tasks across your Microsoft 365 environment.
+Cowork is available in Microsoft Copilot. It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multistep tasks across your Microsoft 365 environment.
 What can Cowork do for me?
 Cowork can send emails, schedule meetings, create documents (Word, Excel, PowerPoint, PDF), post in Teams, manage your calendar, prepare daily briefings, search across your organization, conduct deep research, and draft stakeholder communications. You can also schedule prompts to run automatically.
 Get a full breakdown by category in
 What can Cowork do for you?
 How is Cowork different from Copilot Chat?
-Cowork completes multi-step work across Microsoft 365 by taking action on your behalf, while Copilot Chat helps you generate content and insights within a single session.
+Cowork completes multistep work across Microsoft 365 by taking action on your behalf, while Copilot Chat helps you generate content and insights within a single session.
 Feature
 Copilot Chat
 Cowork
 What it is
 Always-on AI for drafting, summarizing, answering questions
-Agentic AI that completes multi-step work across Microsoft 365
+Agentic AI that completes multistep work across Microsoft 365
 Best for
 Fast, focused, single-task support
 End-to-end work across multiple apps
@@ -22,7 +22,7 @@ Minutes to hours (autonomous execution)
 Task complexity
 Single-step, single-session
-Multi-step workflows across tasks and sources
+Multistep workflows across tasks and sources
 Use when...
 You need a quick draft, answer, or insight
 You need Copilot to take action across apps,
```

---

### 4. Copilot extensibility overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -1,29 +1,17 @@-Microsoft 365 Copilot extensibility documentation
-Learn how to build custom Copilot experiences by using Microsoft 365 extensibility options including agents, connectors, and Copilot APIs.
-Get started with Copilot extensibility
+Extending Microsoft 365 Copilot with plugins
+Package and share an existing declarative agent with Work IQ Dev Tools, or follow the complete lifecycle to prepare, build, test, publish, govern, update, and retire a plugin.
+Get started with plugins
 Get started
-Overview
-Planning guide
-Licensing and cost considerations
-Choose your development tool
-Create and manage agents
+What is a plugin?
+Quickstart: Share an existing agent
+Prepare to build your plugin
+Build and test plugins
 How-To Guide
-Agents overview
-Build a declarative agent
-Build a custom engine agent
-Evaluate agents
-Use Insights Agent (preview)
-Manage agents in the Microsoft 365 admin center
-Extend with plugins and connectors
+Build or reuse capabilities
+Package and test
+â
+Publish, deploy, and manage plugins
 How-To Guide
-Add plugins to declarative agents
-Use Copilot connectors
-Build a custom Copilot connector
-Use developer tools and APIs
-Reference
-Microsoft 365 Agents Toolkit
-Microsoft 365 Agents SDK
-Work IQ API
-Microsoft 365 Copilot APIs
-Interactive Demo
-Microsoft Agent 365+Publish and distribute
+Make available and govern
+Monitor, update, and retire
```

---

### 5. Declarative agents for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -1,54 +1,55 @@ Declarative agents for Microsoft 365 Copilot
-Declarative agents enable you to customize Microsoft 365 Copilot to help you meet the unique business needs of your users. When you build a declarative agent, you provide the instructions, actions, and knowledge to tailor Copilot for your business scenarios. Declarative agents run on the same orchestrator, foundation models, and trusted AI services that power Microsoft 365 Copilot. By building declarative agents, you can optimize collaboration, increase productivity, and streamline workflows in your organization.
-With declarative agents, you can establish consistent, personalized experiences and automate intricate processes, ranging from team onboarding to efficient resolution of customer issues. You can also add capabilities to your agent to unlock more functionality for your users.
+Declarative agents provide a goal-directed conversational experience that is powered by Microsoft 365 Copilot. You define the agent's purpose, instructions, knowledge, and supported actions to address a business scenario. A plugin can include or reference an agent with other supported capabilities, such as skills, Copilot connectors, or MCP-based tools.
+Choose a declarative agent when users need a dedicated conversational experience with behavior and capabilities tailored to a specific outcome. You don't need to create an agent when an existing Microsoft experience or approved agent can use the selected skills, connectors, or tools.
 Note
 For information about the two approaches to building agents for Microsoft 365 Copilot, see
 Agents for Microsoft 365 Copilot
 .
-Tailor declarative agents for your scenario
-Declarative agents are powered by Microsoft 365 Copilot. They use the same scalable infrastructure and platform but are scoped to meet your specific business needs. The following examples illustrate possible use cases for your agents:
-Employee IT self-help with enhanced knowledge
-- Your employees can reso
```

---

### 6. Build agents with Agent Builder

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
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
--- +++ @@ -1,5 +1,5 @@-Build agents by using Agent Builder in Microsoft 365 Copilot
-The Agent Builder feature in Microsoft 365 Copilot provides a simple interface that you can use to quickly build declarative agents by using natural language. This article describes how to use Agent Builder to build an agent for Copilot.
+Build agents in Agent Builder
+Agent Builder provides a simple interface that you can use to quickly build declarative agents by using natural language. This article describes how to use Agent Builder to build an agent for Microsoft 365 Copilot.
 When you choose
 New agent
 in Microsoft 365 Copilot, you can:
@@ -12,7 +12,7 @@ template
 to create an agent for a specific use case.
 Use natural language to describe your agent (recommended)
-You can use Agent Builder in Microsoft 365 Copilot to create an agent by using natural language. As you provide information conversationally, the agentâs name, description, and instructions update automatically to refine its behavior. This approach:
+You can use Agent Builder to create an agent by using natural language. As you provide information conversationally, the agent's name, description, and instructions update automatically to refine its behavior. This approach:
 Understands a user's intent through natural language.
 Provides suggestions, guidance, and next-best prompts.
 Generates optimized agent instructions to build accurate, high-quality agents.
@@ -40,7 +40,7 @@ test it
 on the
 Try it
-tab. You can continue to refine it by using natural language. If you want to change the starter prompts or intent, just say it in natural language - for example: "Update the agent to summarize Teams chats instead of emails."
+tab. You can continue to refine it by using natural language. If you want to change the suggested prompts or intent, just say it in natural language - for example: "Update the agent to summarize Teams chats instead of emails."
 Note
 The natural language experience is only available when you se
```

---

### 7. Agent settings in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.16: Control 2.16: Federated Copilot Connector and Model Context Protocol (MCP) Governance
  - File: `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -10,14 +10,14 @@ page includes the following configuration options:
 Agent management rules
 - Set and run rules to manage or perform actions on agents.
-Allowed agent types
-- Specify which categories of AI agents are permitted for use within the organization.
+Agent and plugin access
+- Specify which categories of AI agents and plugins are permitted for use within the organization.
 Security templates
 - Create preset policies, rules, and allow lists for new AI agents to ensure consistency and compliance.
 Sharing
 - Manage who can share AI agents within your organization and define the methods they can use to share them.
 User access
-- Control which users or groups can interact with AI agents, aligning access with organizational roles and permissions.
+- Control which users or groups can interact with AI agents and plugins, aligning access with organizational roles and permissions.
 Agent feedback sharing
 - Control whether agent usage feedback is shared with agent developers to help improve agent quality and reliability.
 Tags
@@ -86,19 +86,19 @@ action is a one-time bulk operation. It isn't a scheduled rule.
 Reject agent publish requests older than a specified number of days
 Admins can create a custom rule to reject multiple agent publish requests that are older than a specified number of days.
-Allowed agent types
-The
-Allowed agent types
-setting controls which types of agents users can view and install from the agent catalog. Select from the following options:
-Allow apps and agents built by Microsoft
-- Enables users to install agents created by Microsoft.
-Allow apps and agents built by your organization
-- Enables users to install custom agents developed within your tenant.
-Allow apps and agents built by external publishers
-- Enables users to install non-Microsoft agents built by external developers.
+Agent and plugin access
+The
+Agent and plugin access
+setting controls which types of agents and plugins users can view and install from t
```

---

## HIGH: Control Review Recommended

### 1. Microsoft Graph connectors overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json
**Section:** Copilot Extensibility
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -4,6 +4,9 @@ ingest and index external content into Microsoft Graph.
 Federated connectors
 retrieve content in real time by using Model Context Protocol (MCP) without indexing data into Microsoft Graph.
+A Copilot connector can provide external data access as a capability of a Microsoft 365 Copilot plugin. Connector implementation, authentication, packaging, and availability depend on the connector model and target Microsoft experience. For help deciding whether your plugin needs a connector, see
+Connectors as plugin capabilities
+.
 Synced and federated connectors power Microsoft 365 Copilot and other Microsoft 365 intelligent experiences, such as Microsoft Search, Copilot in Excel, and the Researcher agent.
 Note
 Copilot connectors are available in commercial environments and in Microsoft 365 Government Community Cloud (GCC), Government Community Cloud High (GCCH), and Department of Defense (DoD) environments.
@@ -35,6 +38,10 @@ Availability
 Global, GCC, GCCH, DoD
 Varies by federated connector availability
+Important
+Authentication requirements differ between synced connectors, federated connectors, MCP plugins, and agent connectors. The authentication guidance for
+MCP and API plugins
+doesn't automatically apply to Copilot connectors. Follow the product-specific guidance for the connector model you choose.
 For more information about federated connectors, see
 Federated connectors overview
 .
@@ -72,6 +79,11 @@ The
 Copilot connectors gallery
 includes descriptions of Microsoft and partner connectors with links to partner sites. With more than 100 connectors available, you can connect to Azure services, Box, Confluence, Google services, MediaWiki, Salesforce, ServiceNow, and more.
+Prerequisites
+Before you implement a connector, prepare the development environment, target Microsoft experience, required licenses, administrator roles, identities, permissions, data source, and test users. For the general readiness checklist, see
+Set up your devel
```

---

### 2. Agent Builder capabilities

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,37 +1,54 @@-Agent Builder in Microsoft 365 Copilot
-Agent Builder in Microsoft 365 Copilot provides an easy way to build
+Agent Builder overview
+Agent Builder provides an easy way to build
 declarative agents
-for Microsoft 365. Agent Builder offers an immediate, interactive AI development experience that's perfect for quick and straightforward projects.
-Use Microsoft 365 Copilot to create and customize agents that you can implement for scenario-specific use cases, such as:
+for Microsoft 365. Agent Builder offers an immediate, interactive AI development experience that suits quick and straightforward projects.
+Use Agent Builder to create and customize agents for scenario-specific use cases, such as:
 An agent that provides writing or presentation coaching tailored to organizational standards
 A team onboarding agent that responds with specific information about the user's new team and helps them complete onboarding tasks
-You can specify dedicated knowledge sources, including content on SharePoint and information provided by Microsoft 365 Copilot connectors. You can also test the agent before deploying it for use in your conversations with Microsoft 365 Copilot or sharing it with others in your organization.
+You can specify dedicated knowledge sources, including content on SharePoint and information provided by
+Copilot connectors
+. You can also test the agent before you use, share, or publish it.
+Agent Builder also lets you add skills to an agent you build in Agent Builder, either by providing a skill or by creating one through natural language. Skills in Agent Builder are in preview and available only to organizations enrolled in the Microsoft Frontier Program. For more information, see
+Add custom skills to your declarative agent in Agent Builder (preview)
+.
 You can build agents from the following apps and sites:
 microsoft365.com/chat
 office.com/chat
-Microsoft Teams Desktop and web client
+Microsoft Teams desktop and web client
 Agent Bu
```

---

### 3. Microsoft 365 Copilot agent governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,173 +1,99 @@-Agents are apps for Microsoft 365
-When you build an agent, you're also building an app for Microsoft 365. Apps for Microsoft 365 share a common manifest schema and packaging format, and unified distribution and management processes and tools. The end result is that your apps and agents reach the widest possible audience and appear contextually within the workflow of your users.
-This article describes the key parts of the Microsoft 365 app model that apply to agent development.
+What is a Microsoft 365 Copilot plugin?
+A plugin brings supported capabilities together for use in Microsoft 365 Copilot experiences. For example, a solution might use a skill to guide a task, a Copilot connector to access organizational content, and an MCP server to provide tools. The plugin gives that solution a way to be packaged, published, and made available through supported Microsoft routes.
+You build each capability with the tools and guidance that apply to it. The plugin model connects those capabilities to a publishing and management lifecycle; it doesn't change how each capability runs.
 Important
-API plugins are currently only supported as actions within
-declarative agents
-. They aren't enabled in Microsoft 365 Copilot. For an example that shows how to add an API plugin to a declarative agent, see
-Add an API plugin as a custom action to the agent
-.
-The capability is enabled by default in all Microsoft 365 Copilot-licensed tenants. Admins can disable this functionality on a user and group basis and control how individual plugins are approved for use, and which plugins are enabled. For more information, see
-Manage Agents in Integrated Apps
-.
-App package
-The app package for Microsoft 365, including agents, is a zip file that contains one or more configuration (manifest) files and your app icons. Your app logic and data storage are hosted elsewhere and accessed by the Microsoft 365 host application via HTTPS. You'll submit the app package to yo
```

---

### 4. Copilot agent security and compliance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,117 +1,101 @@-Data, privacy, and security considerations for extending Microsoft 365 Copilot
-When you extend Microsoft 365 Copilot with agents, the agent can use queries based on your prompts, conversation history, and Microsoft 365 data to generate a response or complete a command. When you extend Microsoft 365 Copilot with synced Microsoft 365 Copilot connectors, your external data is ingested into Microsoft Graph and remains in your tenant. This article outlines data privacy and security considerations for developing different Copilot extensibility solutions, both in-house and as a commercial developer.
-Agents and actions
-Agents in Microsoft 365 Copilot are individually governed by their terms of use and privacy policies. As a developer of agents and actions (API plugins), you're responsible for securing your customer's data within the bounds of your service and providing information on your policies regarding users' personal information. Admins and users can then view your
-privacy policy
-and
-terms of use
-in the app store before choosing to add or use your agent.
-When you integrate your business workflows as agents for Copilot, your external data stays within your app; it
-doesn't
-flow into Microsoft Graph and it isn't used to train Microsoft 365 Copilot LLMs. Copilot does, however, generate a search query to send to your agent on the user's behalf based on their prompt and conversation history with Copilot and data the user has access to in Microsoft 365. For more info, see
-Data stored about user interactions with Microsoft 365 Copilot
-in the Microsoft 365 Copilot admin documentation.
+Plan data, privacy, and security
+Use this article while you
+plan your plugin
+. Identify the applicable requirements now, and confirm the component-specific implementation after you choose capabilities and development tools.
+Map data and action flows
+Document how information enters, moves through, and leaves the solution. Include prompts, conversation 
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Cowork FAQ
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*