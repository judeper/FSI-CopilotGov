# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-13
**Run Time:** 2026-11-13T17:25:37.844117+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| MEDIUM Changes | 2 |
| Redirects | 32 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | ...t.com/en-us/microsoft-copilot-studio/ | HIGH | 2.14, 4.14 | Update portal-walkthrough |
| 2 | ...ication-fundamentals-publish-channels | MEDIUM | 2.14, 4.14 | Update portal-walkthrough |
| 3 | overview | HIGH | 2.9, 2.3, 1.13 | Update portal-walkthrough |
| 4 | insider-risk-management-configure | CRITICAL | None | Monitor |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft Copilot Studio documentation

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -13,14 +13,14 @@ Get started
 Choose your harness before you build
 Build in Copilot Studio
-Create an automated solution using the GitHub Copilot harness (preview)
+Create an automated solution using the Microsoft Copilot harness (preview)
 Create and deploy an agent with the standard harness
-Agents (GitHub Copilot harness)
-About agents powered by GitHub Copilot
+Agents (Microsoft Copilot harness)
+About agents powered by the Microsoft Copilot harness
 Preview and test your agent
 Evaluate an agent
 Publish an agent
-Workflows (GitHub Copilot harness)
+Workflows (Microsoft Copilot harness)
 Workflows overview
 Edit and manage your workflow
 Add an agent node to a workflow
@@ -30,17 +30,12 @@ Create an app
 Publish and share an app
 Manage data in your app
-Build agents using the GitHub Copilot harness
+Build agents using the Microsoft Copilot harness
 Plan and build
-About agents powered by the GitHub Copilot harness
+About agents powered by the Microsoft Copilot harness
 Understand usage-based billing and Copilot Credits
 Build a new agent
-Configure your agent's details and instructions
-Add knowledge and tools
-Add knowledge to your agents
-Extend agents with tools
-Use skills with agents
-Build modular solutions with connected agents
+Upgrade agents to the GitHub Copilot harness (preview)
 Preview and test
 Debug your agents using activity trace
 Test your agents
@@ -53,17 +48,23 @@ Publish an agent
 Monitor your agent's performance
 Share an agent
+Build agents using the Customer Conversation harness (preview)
+Plan and build
+About agents powered by the Customer Conversation harness
+Understand usage-based billing and Copilot Credits
+Build a new agent
+Preview, test, and evaluate
+Preview and test an agent
+Evaluate an agent
+Deploy and monitor
+Deploy an agent
+Monitor an agent
 Build agents and agent flows using the standard harness
 Create agents
 Build an agent with generative AI from the ground up
 Create and delete agents
-Test your agent

```

---

### 2. Publish and deploy Copilot Studio agents

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
--- +++ @@ -8,7 +8,7 @@ Azure Bot Service skills
 , a code-based way to extend the capabilities of an agent in the standard harness. These skills shouldn't be confused with
 agentic skills
-in the GitHub Copilot harness. Learn more about how to use agentic skills in
+in the Microsoft Copilot harness. Learn more about how to use agentic skills in
 Skills overview for agents
 .
 By using Copilot Studio, you can publish agents that engage with your customers on multiple platforms or channels. For example, live websites, mobile apps, Microsoft Copilot, and messaging platforms like Teams and Facebook.

```

---

### 3. Microsoft Agent 365 overview

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/overview
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.9: Control 2.9: Defender for Cloud Apps — Copilot Session Controls
  - File: `controls/pillar-2-security/2.9-defender-cloud-apps.md`
- Control 2.3: Control 2.3: Conditional Access Policies for Copilot Workloads
  - File: `controls/pillar-2-security/2.3-conditional-access-policies.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.3/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.9/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.9/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.9/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.9/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,29 +1,54 @@ Overview of Microsoft Agent 365
-AI-powered agents are rapidly becoming ubiquitous across enterprises, driving a broad and accelerating transformation. Microsoft Agent 365 provides the ability to
-observe
+AI agents are quickly becoming part of everyday work. Microsoft Agent 365 is the observability platform for AI. It gives you one view of the agents in your organization, including agents from Microsoft and from other companies. Your IT, security, and business teams see the same information, each in the tools they already use.
+Agent 365 is built on four pillars:
+management
 ,
-govern
+governance
+,
+security
 , and
-secure
-the growing number of agents within organizations.
-Observe
-Microsoft Agent 365 gives organizations real-time visibility into their agentic environment, helping admins understand how agents are used, identify performance or risk signals early, and take action before issues impact the business. Admins can now view all their agents in a single, centralized registry providing a unified view of agent adoption, activity, and agent health. These insights help leaders and AI admins stay in control, operate efficiently, and maximize the value of their agent investments from a centralized AI admin experience. Role-specific oversight extends this visibility to security and business leaders, ensuring the right stakeholders have the tailored insights they need to manage risk and measure agent value within their domains. Learn more:
+business value
+.
+Management
+Management helps you see and run all your agents from one place.
+The agent registry in the Microsoft 365 admin center lists the agents in your organization. It includes agents from Microsoft, from partners, and from your own teams. For each agent, you can see who owns it, how much people use it, and whether it has any risks.
+You can also bring in agents that you built on other platforms. Agent Map shows your agents on a visual map, grouped by the platform you built th
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Publish and deploy Copilot Studio agents
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Classification:** MEDIUM (General content update)

---

### 2. Get started with insider risk management
**URL:** https://learn.microsoft.com/en-us/purview/insider-risk-management-configure
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