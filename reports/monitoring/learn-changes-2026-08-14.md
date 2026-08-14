# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-14
**Run Time:** 2026-08-14T10:49:02.134215+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| HIGH Changes | 5 |
| MEDIUM Changes | 4 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | HIGH | 4.12 | Update portal-walkthrough |
| 2 | get-started | MEDIUM | None | Review optional |
| 3 | cowork-models | MEDIUM | 4.15 | Update portal-walkthrough |
| 4 | cowork-faq | HIGH | None | Review and update |
| 5 | ...-based-billing-manage-copilot-credits | HIGH | 4.15 | Update portal-walkthrough |
| 6 | what-is-microsoft-entra-agent-id | HIGH | None | Review and update |
| 7 | whats-new-agent-id | MEDIUM | None | Review optional |
| 8 | security-for-ai-overview | HIGH | None | Review and update |
| 9 | what-is-agent-id-platform | MEDIUM | None | Review optional |
| 10 | configure-third-party-agents | HIGH | None | Review and update |
| 11 | best-practices-agent-id | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -37,6 +37,16 @@ for data governance solutions.
 Roadmap
 for data security and risk and compliance solutions.
+August 2026
+Sensitivity labels
+Before enforcing an auto-labeling policy, run it in simulation mode to identify which items it would label without making any changes. Review the match results and source distribution to determine whether the policy is ready to enforce. For more information, see
+Review simulation results for auto-labeling policies in Microsoft Purview
+.
+The
+Insights
+tab in the policy details panel provides an at-a-glance view of an auto-labeling policy's performance. The information shown varies depending on whether the policy is running in simulation or enforcement mode, helping you understand how it identifies or labels content. For more information, see
+Use the Insights tab to analyze auto-labeling policies in Microsoft Purview
+.
 July 2026
 Data Loss Prevention
 In preview

```

---

### 2. Copilot Cowork available models

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
--- +++ @@ -99,6 +99,19 @@ Learn about organization-wide Cowork settings in
 Manage Cowork for your organization
 .
+Set the effort level to balance quality, speed, and cost
+Not every task needs the same level of power. Effort levels give you more control over how Cowork balances quality, speed, and cost.
+Medium
+is the default, which gives you a strong balance for everyday work. Select
+Light
+for lighter tasks. Select
+High
+or
+Extra High
+when you need deeper analysis, more complex reasoning, or a more thorough response. You can also select
+Max
+for your hardest work. Higher effort gives Cowork more room to work through the task, but takes longer and uses your limits faster.
+The model and effort controls are in the compose box, where your work begins. Choose your model, set the effort, and get working.
 Related content
 Use Cowork
 Manage Cowork for your organization

```

---

### 3. Manage Copilot Credits (usage-based billing)

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
--- +++ @@ -479,6 +479,7 @@ Usage-based billing overview for Copilot credits
 Discovery setting for AI experiences enabled by usage-based billing
 Cowork Usage report
+View Copilot Credit consumption in the Microsoft 365 admin center and on your Azure bill
 Feedback
 Was this page helpful?
 Yes

```

---

## HIGH: Control Review Recommended

### 1. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -338,11 +338,12 @@ Auto
 and Cowork chooses the model that fits your task. To pick a specific model, select
 Auto
-in the chat header and choose from the list that your organization makes available, which can include Claude Opus and Sonnet variants, Claude Fable 5 (Preview), the Sonnet+Opus Advisor pairing, and GPT 5.5. Claude Fable 5 (Preview) is off by default, so it appears only after an admin turns it on in the
+in the compose box and choose from the list that your organization makes available. The choices include GPT 5.5 and GPT 5.6 variants, Claude Opus, Claude Sonnet, and Claude Fable 5 (Preview). Claude Fable 5 (Preview) is off by default, so it appears only after an admin turns it on in the
 Microsoft 365 admin center
 under Copilot settings. Some models, such as Claude Fable 5, require data retention, and Cowork shows a note in the picker and a banner while the model is selected. Learn more in
 Choose a model for Cowork
 .
+You can also set the effort level that determines how Cowork balances quality, speed, and cost. Since your tasks might require different levels of power, you can choose the effort level next to the model picker. Medium is the default, giving you a strong balance for everyday work.
 Where are my files saved?
 Files that Cowork creates are saved to your
 OneDrive and SharePoint

```

---

### 2. Microsoft Entra Agent ID overview

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -29,10 +29,10 @@ Microsoft Entra Agent identity platform
 enables developers to create and manage
 agent identities
-, which are specialized identity constructs built for AI agents. Agent identity blueprints serve as templates for creating individual agent identities with parent-child relationships, enabling consistent security policies across large numbers of agents. The platform supports standard protocols such as OAuth 2.0, MCP, and A2A for authentication and agent-to-agent communication.
+, which are specialized identity constructs built for AI agents. Agent identity blueprints serve as templates for creating individual agent identities with parent-child relationships, enabling consistent security policies across large numbers of agents. The platform supports standard protocols such as OAuth 2.0, Model Context Protocol (MCP), and agent-to-agent (A2A) for authentication and agent-to-agent communication.
 Microsoft Entra Agent ID works with agents built on Microsoft and non-Microsoft platforms. Organizations can
 integrate third-party agents
-from platforms such as AWS Bedrock and n8n by using the Microsoft Entra Auth SDK (sidecar) or workload identity federation, giving every agent a governed identity regardless of where it was built.
+from platforms such as AWS Bedrock and n8n by using the Microsoft Entra ID Auth SDK (sidecar) or workload identity federation, giving every agent a governed identity regardless of where it was built.
 Security and governance for agents
 Microsoft Entra Agent ID extends existing Microsoft Entra security and governance capabilities to agent identities. Agents receive the same identity-driven protections as users and workloads, including adaptive access policies, real-time risk detection, lifecycle management, and network-level controls. All agent authentication and activity is logged for compliance and audit.
 For details on how these capabilities work for agents, see:

```

---

### 3. Microsoft Entra security for AI overview

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/security-for-ai-overview
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -83,7 +83,7 @@ Assign secure, scalable identities
 : The
 Microsoft Entra Agent identity platform
-enables you to assign identities to agents, autodiscover them across your organization, and manage all agent metadata in one place including capabilities, tasks, and protocols. It provides agent-to-agent discovery and authorization based on standard protocols such as MCP and A2A.
+enables you to assign identities to agents, autodiscover them across your organization, and manage all agent metadata in one place including capabilities, tasks, and protocols. It provides agent-to-agent discovery and authorization based on standard protocols such as Model Context Protocol (MCP) and agent-to-agent (A2A).
 Log and monitor agent activity
 : All authentication and actions performed by agents are logged in Microsoft Entra ID and viewable through the Microsoft Entra admin center for compliance and audit purposes.
 For more information about agent identities as identity constructs, including how they differ from application and user identities, see

```

---

### 4. Integrate third-party agents with Microsoft Entra Agent ID

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/configure-third-party-agents
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -22,7 +22,7 @@ Integrate third-party agents with Microsoft Entra Agent ID
 Feedback
 Summarize this article for me
-Microsoft Entra Agent ID enables AI agents from third-party platforms to authenticate and access your APIs securely without handling credentials directly. This article covers two integration patterns - the Microsoft Entra Auth SDK (sidecar) and federation - for platforms such as Amazon Web Service (AWS) Bedrock and n8n.
+Microsoft Entra Agent ID enables AI agents from third-party platforms to authenticate and access your APIs securely without handling credentials directly. This article covers two integration patterns - the Microsoft Entra ID Auth SDK (sidecar) and federation - for platforms such as Amazon Web Service (AWS) Bedrock and n8n.
 Prerequisites
 Before you start, make sure you have:
 Microsoft Entra tenant
@@ -58,13 +58,13 @@ Remove the need for agents to handle credentials directly.
 Use workload identity federation for agents running outside Azure.
 Support multiple authentication patterns, including client credentials, federated identity, and on-behalf-of.
-Integrate with third-party agent platforms by using the Microsoft Entra Auth SDK (sidecar).
+Integrate with third-party agent platforms by using the Microsoft Entra ID Auth SDK (sidecar).
 Integration patterns for third-party agents
 To integrate third-party agents with Microsoft Entra Agent ID, choose from the following patterns:
-Use the Microsoft Entra Auth SDK (sidecar)
+Use the Microsoft Entra ID Auth SDK (sidecar)
 The
 sidecar pattern
-runs the Microsoft Entra Auth SDK as a companion container alongside your agent. The agent calls the sidecar to request tokens for API calls. The agent never handles credentials directly; instead, it delegates token acquisition to the sidecar.
+runs the Microsoft Entra ID Auth SDK (sidecar) as a companion container alongside your agent. The agent calls the sidecar to request tokens for API calls. The agent never handles credentials direc
```

---

### 5. Microsoft Entra Agent ID best practices

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/best-practices-agent-id
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -58,6 +58,18 @@ Create agent's user accounts only when necessary.
 Agent's user accounts
 should only be created for scenarios that truly require a user object, such as an agent needing a mailbox or Teams presence. If your agent can operate with app credentials alone, avoid agent's user accounts because they add complexity with licenses, group memberships, and user-level policies.
+Guardrails for AI coding assistants
+AI coding assistants often default to creating a standard app registration when asked to build an agent, because that's the traditional workload identity pattern. Add the following to your repository's
+.github/copilot-instructions.md
+or
+AGENTS.md
+file so AI coding assistants use agent identities correctly:
+## Microsoft Entra Agent ID
+- To give an AI agent its own identity in Microsoft Entra, create an agent identity blueprint, then create agent identities from it.
+- Don't create or reuse a standard app registration or service principal to represent an agent. Never use `az ad app create`, `New-MgApplication`, `New-AzADApplication`, or `POST /applications` to create an agent identity.
+- In .NET, use the Microsoft.Identity.Web.AgentIdentities package: call builder.Services.AddAgentIdentities(), then acquire tokens with WithAgentIdentity(agentIdentity) (app-only) or WithAgentUserIdentity(agentIdentity, user) (on behalf of a user).
+- Requires the Agent ID Developer or Agent ID Administrator role and the AgentIdentityBlueprint.Create permission.
+- Reference: /entra/agent-id/how-to-plan-agent-identity-architecture
 Manage credentials securely
 Credential management is critical to preventing unauthorized access through agent identities. For detailed steps, see
 Create an agent identity blueprint
@@ -169,11 +181,11 @@ Copilot Studio, Graph APIs, or the Agent 365 CLI
 rather than manual Graph calls that might miss required properties. These tools handle blueprint creation, credential binding, and instance setup automatically.
 Establish a pr
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Get started with Copilot Cowork
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Classification:** MEDIUM (General content update)

---

### 2. Copilot Cowork available models
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
**Classification:** MEDIUM (General content update)

---

### 3. What's new in Microsoft Entra Agent ID
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
**Classification:** MEDIUM (General content update)

---

### 4. Microsoft Entra Agent identity platform
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform
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
| https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms |
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*