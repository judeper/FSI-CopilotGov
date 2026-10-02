# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-02
**Run Time:** 2026-10-02T16:01:07.590598+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| MEDIUM Changes | 2 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | ...t.com/en-us/microsoft-copilot-studio/ | MEDIUM | 2.14, 4.14 | Update portal-walkthrough |
| 3 | ...ication-fundamentals-publish-channels | HIGH | 2.14, 4.14 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -82,8 +82,10 @@ licensing prerequisites
 ,
 Microsoft Copilot service descriptions
-and
+,
 Copilot license options
+, and
+Microsoft Copilot requirements
 .
 For more information about US government cloud, see
 Understand Microsoft US government cloud environments for Microsoft 365 and Microsoft Copilot
@@ -94,18 +96,12 @@ Copilot Chat (Basic)
 is the standalone baseline experience included with eligible Microsoft 365 licenses. It provides a secure, enterprise-ready AI chat that primarily uses web data and has limited use of organizational content. Copilot Chat can use organizational content, but you must explicitly provide that content with your prompt.
 You can access Copilot Chat (Basic) through:
-https://m365copilot.com/
-(
-Pin Copilot Chat
-)
-Copilot Chat in Microsoft Edge (select the Copilot icon in the upper-right corner of the Edge browser). Use Copilot Chat to summarize website content and
+copilot.cloud.microsoft
+Microsoft Copilot app (web, desktop, mobile)
+Copilot Chat in Edge (select the Copilot icon in the upper-right corner of the Edge browser). Use Copilot Chat to summarize website content and
 some document types
 displayed in Edge.
 Copilot Chat in Outlook and Teams
-bing.com/chat
-bing.com/copilotsearch
-copilot.com
-copilot.ai
 Note
 The Microsoft 365 Copilot Chat app is now called Microsoft Copilot Chat
 . The primary URL for accessing the updated Copilot app is changing from
@@ -125,8 +121,8 @@ standard access
 to Copilot capabilities inside apps (for example, Word or Excel). These experiences are more limited and might not include full chat integration or priority access. Standard access is subject to service capacity and might vary throughout the day.
 You can access Microsoft 365 Copilot (Basic) through:
-https://m365copilot.com/
-Microsoft 365 desktop app
+copilot.cloud.microsoft
+Microsoft Copilot app (web, desktop, mobile)
 Microsoft 365 apps (Word, Excel, PowerPoint, and OneNote)
 Note
 The Microsoft 365 Copilot Chat app i
```

---

### 2. Microsoft Copilot Studio documentation

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
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
--- +++ @@ -78,7 +78,7 @@ Key concepts - Publish and deploy your agent
 Publish an agent to SharePoint
 Publish an agent to a live or demo website
-Publish an agent to Teams and Microsoft 365 Copilot
+Publish an agent to Teams and Microsoft Copilot
 Monitor and administer
 Use analytics to improve your agent
 Configure data policies for agents
@@ -105,8 +105,8 @@ Browse reference architectures and solution ideas for Power Platform and Copilot Studio.
 Agents hub on Learn
 Explore Microsoft's agent ecosystem, learn key concepts, and find resources to plan, build, adopt, and continuously improve AI agents for your organization.
-Microsoft 365 Copilot extensibility
-Customize Microsoft 365 Copilot with agents and use actions and connectors to extend Copilot's skills and knowledge.
+Microsoft Copilot extensibility
+Customize Microsoft Copilot with agents and use actions and connectors to extend Copilot's skills and knowledge.
 Microsoft 365 Agents SDK
 Build agents deployable to channels of your choice, with scaffolding to handle the required communication.
 Microsoft Agent 365

```

---

### 3. Publish and deploy Copilot Studio agents

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
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
--- +++ @@ -3,7 +3,7 @@ This article describes features used in agents or agent flows powered by the
 standard harness
 .
-By using Copilot Studio, you can publish agents that engage with your customers on multiple platforms or channels. For example, live websites, mobile apps, Microsoft 365 Copilot, and messaging platforms like Teams and Facebook.
+By using Copilot Studio, you can publish agents that engage with your customers on multiple platforms or channels. For example, live websites, mobile apps, Microsoft Copilot, and messaging platforms like Teams and Facebook.
 Each time you update your agent, you can publish it again from within Copilot Studio. Publishing your agent applies to all the channels associated with your agent.
 You need to publish your agent before your customers can engage with it. You can publish your agent on multiple platforms, or
 channels
@@ -12,7 +12,7 @@ When you publish an agent, this agent updates on all connected channels. If you make changes to your agent but don't publish after doing so, your customers won't be engaging with the latest content.
 Agents have the
 Authenticate with Microsoft
-option turned on by default. With this option, agents automatically use Microsoft Entra ID authentication for Teams, Power Apps, and Microsoft 365 Copilot without requiring any manual setup.
+option turned on by default. With this option, agents automatically use Microsoft Entra ID authentication for Teams, Power Apps, and Microsoft Copilot without requiring any manual setup.
 If you want to allow anyone to chat with an agent, select
 No authentication
 .
@@ -48,7 +48,7 @@ in the current session. This command resets the conversation and starts a new session with the latest content you published. Otherwise, it might take one hour after you publish an update for the agent for its latest version to take effect. After this delay, users get the new version the next time they send a message to your agent.
 Test your agent
 Test your agent after you pub
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

### 2. Microsoft Copilot Studio documentation
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*