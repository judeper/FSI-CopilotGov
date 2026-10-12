# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-12
**Run Time:** 2026-10-12T19:30:25.457561+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| HIGH Changes | 1 |
| MEDIUM Changes | 4 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | ...soft-365-copilot-enablement-resources | HIGH | 1.11, 1.12 | Update portal-walkthrough |
| 2 | .../microsoft-365/copilot/extensibility/ | MEDIUM | 2.16, 4.13 | Update portal-walkthrough |
| 3 | agent-builder | MEDIUM | None | Review optional |
| 4 | agents-are-apps | HIGH | None | Review and update |
| 5 | data-privacy-security | MEDIUM | None | Review optional |
| 6 | restricted-content-discovery | MEDIUM | 1.13, 1.4, 1.7, 1.3, 1.2, 2.5 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot adoption guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.11: Control 1.11: Organizational Change Management and Adoption Planning
  - File: `controls/pillar-1-readiness/1.11-change-management-adoption.md`
- Control 1.12: Control 1.12: Training and Awareness Program
  - File: `controls/pillar-1-readiness/1.12-training-awareness.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.11/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -53,12 +53,24 @@ Set up Microsoft Copilot - Setup guide in the Microsoft 365 admin center
 Step 5 - Send a welcome email and enable feedback
 After your licenses are assigned, you can send a welcome email to your users. This email can include information about Microsoft Copilot, how to use it, and any training resources you have available.
-You can also enable feedback for Microsoft Copilot users. To learn more, see
-Welcome end users to Microsoft Copilot.
+You can also use the Copilot onboarding experience to help users get started with Copilot. Copilot onboarding is a guided, in-product experience that helps users build familiarity with Copilot and develop their prompting skills.
+As part of your onboarding rollout, you can:
+Add a link to your organization's AI usage policy for users to review.
+Share the Copilot onboarding experience by copying the onboarding link or downloading and customizing the email template.
+Use built-in notifications to let users know when Copilot onboarding is available.
+Monitor Copilot onboarding completion through Viva Learning reporting and follow up with users as needed.
+Allow feedback for Microsoft Copilot users.
+The onboarding experience can differ based on the user's Copilot license. For details about creating the onboarding experience, see
+Manage Microsoft Copilot onboarding
+.
+You can also continue supporting Copilot adoption by sharing learning resources and enabling feedback. To learn more, see
+Welcome end users to Microsoft Copilot
+.
 Related articles
 Copilot Prompt Gallery
 Configure a secure and governed data foundation for Microsoft Copilot
 Microsoft Copilot reports
+Manage Microsoft Copilot onboarding
 Was this page helpful?
 Yes
 No

```

---

### 2. Copilot extensibility overview

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
--- +++ @@ -1,17 +1,21 @@ Extending Microsoft 365 Copilot with plugins
-Package and share an existing declarative agent with Work IQ Dev Tools, or follow the complete lifecycle to prepare, build, test, publish, govern, update, and retire a plugin.
+Create a plugin from existing capabilities with Work IQ Dev Tools, or follow the complete lifecycle to prepare, build, test, publish, govern, update, and retire a plugin.
 Get started with plugins
 Get started
 What is a plugin?
-Quickstart: Share an existing agent
+Quickstart: Create your first plugin with Work IQ Dev Tools
 Prepare to build your plugin
 Build and test plugins
 How-To Guide
 Build or reuse capabilities
 Package and test
-â
-Publish, deploy, and manage plugins
+Validate and test your plugin
+Publish and make plugins available
 How-To Guide
-Publish and distribute
+Publish or share
 Make available and govern
-Monitor, update, and retire+Monitor, update, and retire plugins
+How-To Guide
+Monitor your plugin
+Improve and update your plugin
+Retire your plugin
```

---

### 3. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -28,7 +28,7 @@ Restricted Content Discovery is a site-level setting. When you turn on the setting, Microsoft 365 search systems propagate it so that content from the site doesn't appear in organization-wide discovery experiences.
 Even when Restricted Content Discovery is enabled:
 Site permissions stay the same.
-Users can still discover content they own or have recently interacted with.
+Users can continue to access content they already have permission to access.
 The feature doesn't remove content from the Microsoft 365 search index.
 Because the setting must propagate across indexing systems, updates can take time to become fully effective. The amount of time depends on site size, the number of files in each site, and the number of concurrent updates being processed.
 Prerequisites

```

---

## HIGH: Control Review Recommended

### 1. Microsoft 365 Copilot agent governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1,99 +1,74 @@ What is a Microsoft 365 Copilot plugin?
-A plugin brings supported capabilities together for use in Microsoft 365 Copilot experiences. For example, a solution might use a skill to guide a task, a Copilot connector to access organizational content, and an MCP server to provide tools. The plugin gives that solution a way to be packaged, published, and made available through supported Microsoft routes.
-You build each capability with the tools and guidance that apply to it. The plugin model connects those capabilities to a publishing and management lifecycle; it doesn't change how each capability runs.
-Important
-Supported components, packages, publishing routes, administration steps, and Microsoft experiences vary by product and rollout. Use the linked guidance for the capabilities and route you choose.
-Choose your path
-Choose the route that matches what you need to do:
-Package and share an existing agent:
-If you have the local source project for a supported declarative agent, follow the
-Work IQ Dev Tools quickstart
-to validate, provision, package, share, and test it without rebuilding the agent.
-Build new capabilities:
-If you need to build a new agent, skill, Copilot connector, or MCP server,
-plan your plugin
-and follow the complete lifecycle.
-Administer plugins and agents:
-Follow the
-administrator guidance
-to review, make available, govern, monitor, update, or retire them.
-Publish for customers:
-Follow the
-ISV and software publisher guidance
-for public distribution, certification, servicing, and support.
-Decide what your solution needs
-Start with the job the solution should help someone do, who will use it, and where they will use it. Then choose the capabilities that support that job.
+A Microsoft 365 Copilot plugin is an installable package that brings together capabilities for a specific task. It can include supported agents and skills, along with configuration or references for connectors and remote MCP servers.
+Fo
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot extensibility overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Classification:** MEDIUM (General content update)

---

### 2. Agent Builder capabilities
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder
**Classification:** MEDIUM (General content update)

---

### 3. Copilot agent security and compliance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security
**Classification:** MEDIUM (General content update)

---

### 4. Restricted Content Discovery
**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
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