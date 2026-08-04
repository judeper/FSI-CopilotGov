# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-04
**Run Time:** 2026-08-04T11:55:47.221816+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| HIGH Changes | 1 |
| MEDIUM Changes | 6 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | audit-log-activities | HIGH | 3.1, 1.15 | Update portal-walkthrough |
| 2 | ...t.com/en-us/microsoft-copilot-studio/ | HIGH | None | Review and update |
| 3 | ...ication-fundamentals-publish-channels | MEDIUM | None | Review optional |
| 4 | authoring-ask-a-question | MEDIUM | None | Review optional |
| 5 | agent-extend-action-mcp | MEDIUM | None | Review optional |
| 6 | mcp-add-existing-server-to-agent | MEDIUM | None | Review optional |
| 7 | authoring-select-agent-model | MEDIUM | 4.14, 1.16 | Update portal-walkthrough |
| 8 | manage-federated-connectors | MEDIUM | 2.16 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (UI element names)

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
--- +++ @@ -2167,6 +2167,55 @@ Executed a scheduled prompt
 ScheduledPromptExecute
 Logged at the start of each scheduled run. It doesn't confirm the prompt was completed.
+Microsoft Defender for Cloud activities
+The following table lists Microsoft Defender for Cloud activities that are logged in the Microsoft 365 audit log. For more information, see
+What is Microsoft Defender for Cloud?
+.
+Friendly name
+Operation
+Description
+Connector created
+ConnectorCreated
+A user created a cloud environment connector for AWS, Azure, Google Cloud Platform (GCP), GitHub, JFrog, or Azure DevOps.
+Connector deleted
+ConnectorDeleted
+A user deleted a cloud environment connector.
+Connector modified
+ConnectorModified
+A user updated the configuration of an existing cloud environment connector.
+Enablement rule collection created
+EnablementRuleCollectionCreated
+A user created an enablement rule collection to configure Defender plans and extensions for an environment.
+Enablement rule collection deleted
+EnablementRuleCollectionDeleted
+A user deleted an enablement rule collection.
+Enablement rule collection modified
+EnablementRuleCollectionModified
+A user modified an enablement rule collection to change Defender plan or extension settings.
+Global setting modified
+GlobalSettingModified
+A user modified a global setting.
+Rule collection created
+RuleCollectionCreated
+A user created a rule collection.
+Rule collection deleted
+RuleCollectionDeleted
+A user deleted a rule collection and its associated rules.
+Rule collection disabled
+RuleCollectionDisabled
+A user disabled an active rule collection without deleting it.
+Rule collection enabled
+RuleCollectionEnabled
+A user enabled a previously disabled rule collection.
+Rule collection modified
+RuleCollectionModified
+A user modified a rule collection.
+Rule created
+RuleCreated
+A user created a rule.
+Rule deleted
+RuleDeleted
+A user deleted a rule.
 Microsoft Defender for Endpoint general settings activities
 The 
```

---

### 2. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -22,6 +22,14 @@ Select a primary AI model for your agent
 Feedback
 Summarize this article for me
+Note
+Features in this article are powered by the
+standard harness
+, which uses the billing options described in
+Licensing for agents powered by the standard harness
+. Learn how to access standard features in
+Access standard agents and agent flows
+.
 AI capabilities evolve rapidly, and each generative model brings distinct strengths, whether it's faster responses, higher-quality outputs, or improved cost efficiency. By using Copilot Studio, you can choose the best model for your agent's orchestration by using a simple dropdown menu.
 Want to try out cutting-edge models before they're production-ready? Access the latest experimental models to evaluate them early. However, they might have limited testing, availability, and functionality.
 This article describes how to select an AI model for your agent's generative orchestration. Separate settings exist for changing models for
@@ -302,7 +310,7 @@ Experimental (cross-geo)
 Experimental (cross-geo)
 * Claude Sonnet 5 is available only in
-new experience agents
+agents powered by the GitHub Copilot harness
 .
 Note
 Models marked as

```

---

### 3. Manage federated connector availability

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/manage-federated-connectors
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.16: Control 2.16: Federated Copilot Connector and Model Context Protocol (MCP) Governance
  - File: `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -39,7 +39,7 @@ Prerequisites
 The federated connector management capability requires the following prerequisites:
 Administrator role
-: Global Administrator or AI Administrator permissions
+: Global Administrator or Search Administrator permissions
 PowerShell access
 : Ability to run PowerShell as an administrator
 Connector.Cmd module
@@ -59,7 +59,7 @@ cmdlet to enable or disable federated connectors across your tenant.
 In PowerShell, run the following command:
 Set-FederatedConnectorToggle
-When prompted, authenticate with your Global Administrator or AI Administrator credentials.
+When prompted, authenticate with your Global Administrator or Search Administrator credentials.
 Approve the requested permissions.
 The cmdlet displays the current state of the federated connector toggle and prompts you to choose an action:
 Select

```

---

## HIGH: Control Review Recommended

### 1. Microsoft Copilot Studio documentation

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,6 +1,6 @@ Microsoft Copilot Studio documentation
-Discover how to build AI-driven agents and workflows easily with Microsoft Copilot Studio with online training courses, docs, and videos. Learn how to quickly and simply integrate chat into your website.
-Get started
+Discover how to build AI-driven agents and workflows with Microsoft Copilot Studio. Access documentation, implementation guidance, online training, and other resources.
+Overview
 What is Microsoft Copilot Studio?
 What's new
 What's new in Microsoft Copilot Studio?
@@ -11,81 +11,79 @@ Create
 Create agents and workflows in Microsoft Copilot Studio.
 Get started
-NEW! Try the new agent experience (preview)
-Buy license
-Use generative AI to build agents fast
+Choose your harness before you build
+Build in Copilot Studio
+Create an automated solution using the GitHub Copilot harness (preview)
+Create and deploy an agent with the standard harness
+Agents (GitHub Copilot harness)
+Build an agent
+Preview and test your agent
+Evaluate an agent
+Publish an agent
+Workflows (GitHub Copilot harness)
+Workflows overview
+Edit and manage your workflow
+Add an agent node to a workflow
+Add a Microsoft 365 Copilot node to a workflow
+Build agents using the GitHub Copilot harness
+Plan and build
+About agents powered by the GitHub Copilot harness
+Understand usage-based billing and Copilot Credits
+Build a new agent
+Configure your agent's details and instructions
+Add knowledge and tools
+Add knowledge to your agents
+Extend agents with tools
+Use skills with agents
+Build modular solutions with connected agents
+Preview and test
+Debug your agents using activity trace
+Test your agents
+View conversation history
+Evaluate
+Create a test set
+Run an evaluation
+View evaluation results
+Publish, monitor, and share
+Publish an agent
+Monitor your agent's performance
+Share an agent
+Build agents and agent flows using the standard harness
+Create agents
 Build an agent with generative AI from the ground
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Publish and deploy Copilot Studio agents
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Classification:** MEDIUM (General content update)

---

### 2. Adaptive cards in Copilot Studio topics
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-ask-a-question#add-an-adaptive-card
**Classification:** MEDIUM (General content update)

---

### 3. Model Context Protocol in Copilot Studio
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
**Classification:** MEDIUM (General content update)

---

### 4. Connect an existing MCP server to an agent
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
**Classification:** MEDIUM (General content update)

---

### 5. Select an agent model
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Classification:** MEDIUM (General content update)

---

### 6. Manage federated connector availability
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/manage-federated-connectors
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