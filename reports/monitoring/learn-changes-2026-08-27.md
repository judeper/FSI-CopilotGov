# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-27
**Run Time:** 2026-08-27T20:03:37.107489+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 6 |
| MEDIUM Changes | 8 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | HIGH | 1.9, 1.1, 2.15 | Update portal-walkthrough |
| 2 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 3 | cowork-models | MEDIUM | 4.15 | Update portal-walkthrough |
| 4 | ...t.com/en-us/microsoft-copilot-studio/ | MEDIUM | None | Review optional |
| 5 | ...ication-fundamentals-publish-channels | MEDIUM | None | Review optional |
| 6 | authoring-ask-a-question | MEDIUM | None | Review optional |
| 7 | agent-extend-action-mcp | MEDIUM | None | Review optional |
| 8 | mcp-add-existing-server-to-agent | MEDIUM | None | Review optional |
| 9 | authoring-select-agent-model | MEDIUM | 1.16, 4.14 | Update portal-walkthrough |
| 10 | agent-registry | MEDIUM | 2.14, 4.13, 4.14 | Update portal-walkthrough |
| 11 | manage-federated-connectors | CRITICAL | 2.16 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
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
--- +++ @@ -39,22 +39,22 @@ .
 Users must have
 Microsoft Entra ID
-accounts. You can add or sync users using the
+accounts. You can add or sync users by using the
 onboarding wizard in the Microsoft 365 admin center
 .
-Microsoft Copilot is only supported on primary mailboxes that are hosted on Exchange Online.
+Microsoft Copilot supports only primary mailboxes that are hosted on Exchange Online.
 Note
-Chat experiences in Word, Excel, PowerPoint vary depending on your tenant configuration and license. Learn more in
+Chat experiences in Word, Excel, and PowerPoint vary depending on your tenant configuration and license. Learn more in
 Microsoft Copilot overview
 .
-If you'd like to enable users with priority access to these capabilities, learn more about
+To enable users with priority access to these capabilities, learn more about
 Microsoft Copilot
 .
 App requirements
 Microsoft 365 Apps
-- The apps must be deployed. You can use the
+- You must deploy the apps. Use the
 Microsoft 365 Apps setup guide in the Microsoft 365 admin center
-to deploy to your users.
+to deploy the apps to your users.
 Note
 For Copilot to work in Word Online, Excel Online, and PowerPoint Online, you must enable third-party cookies.
 Review your privacy settings for Microsoft 365 Apps. These settings might affect the availability of Microsoft Copilot features. For more information, see
@@ -64,7 +64,7 @@ Microsoft OneDrive
 - Some features in Microsoft Copilot, such as file restore and OneDrive management, require that users have a
 OneDrive account
-. You can use the
+. Use the
 OneDrive setup guide in the Microsoft 365 admin center
 to enable OneDrive for your users.
 Microsoft Outlook
@@ -78,7 +78,7 @@ Important
 Microsoft Copilot is only supported on primary mailboxes that are hosted on Exchange Online. It isn't available on a user's archive mailbox, group mailboxes, or shared and delegate mailboxes that they have access to.
 Microsoft Teams
-- You can use the
+- Use the
 Microsoft Te
```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
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
--- +++ @@ -1379,6 +1379,9 @@ Get Items Sizes
 GetItemsSize
 Retrieved cached item sizes for the OneLake item-size report.
+Get OneLake file soft-delete settings
+GetFileSoftDelete
+Generated when a user reads the workspace's OneLake file soft-delete status and retention period.
 Get connection by tenant admin
 GetGatewayClusterDatasourceAsAdmin
 A tenant admin retrieved the connection details.
@@ -1421,6 +1424,9 @@ Modified OneLake default tier
 ModifiedDefaultTier
 Modified OneLake default tier.
+Modified OneLake file soft-delete settings
+ModifiedOneLakeFileSoftDeleteSettings
+Generated when a workspace admin enables or disables OneLake file soft delete, or changes the retention period (1â365 days).
 Planning session upgraded
 PlanningSessionUpgraded
 Session type is upgraded in planning workload.

```

---

### 3. Copilot Cowork available models

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
--- +++ @@ -105,9 +105,9 @@ Manage Cowork for your organization
 .
 Set the effort level to balance quality, speed, and cost
-Not every task needs the same level of power. Effort levels give you more control over how Cowork balances quality, speed, and cost.
+Not every task needs the same level of power. Effort levels give you more control over how Cowork balances quality, speed, and cost. The effort level you select persists across future Cowork tasks until you change it.
 Medium
-is the default, which gives you a strong balance for everyday work. Select
+is the default, which gives you a strong balance for everyday work. The default can vary across models to meet the Cowork quality bar. Select
 Light
 for lighter tasks. Select
 High
@@ -115,8 +115,10 @@ Extra High
 when you need deeper analysis, more complex reasoning, or a more thorough response. You can also select
 Max
-for your hardest work. Higher effort gives Cowork more room to work through the task, but takes longer and uses your limits faster.
-The model and effort controls are in the compose box, where your work begins. Choose your model, set the effort, and get working.
+for your hardest work.
+Effort levels are available in Copilot Cowork for web, Windows, and macOS.
+Note
+Higher effort is more thorough, but is slower and uses more credits. Usage is based on factors such as model choice, context volume, orchestration, and tools used.
 Related content
 Use Cowork
 Manage Cowork for your organization

```

---

### 4. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

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
--- +++ @@ -23,12 +23,8 @@ Feedback
 Summarize this article for me
 Note
-Features in this article are powered by the
+This article describes features used in agents or agent flows powered by the
 standard harness
-, which uses the billing options described in
-Licensing for agents powered by the standard harness
-. Learn how to access standard features in
-Access standard agents and agent flows
 .
 AI capabilities evolve rapidly, and each generative model brings distinct strengths, whether it's faster responses, higher-quality outputs, or improved cost efficiency. By using Copilot Studio, you can choose the best model for your agent's orchestration by using a simple dropdown menu.
 Want to try out cutting-edge models before they're production-ready? Access the latest experimental models to evaluate them early. However, they might have limited testing, availability, and functionality.

```

---

### 5. Agent registry in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
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
--- +++ @@ -569,20 +569,20 @@ For more information, see
 Agent and app Package Management API overview (preview)
 .
-Export to Excel
-Export the list of shared agents to an Excel file. You can set the scope of the exported list to be
-All agents
-or only the currently
+Export to Excel for users and agents
+You can export the list of agents to an Excel file. Set the export scope to
+All agents
+or
 Filtered agents
-. This feature is essential for detailed analysis and reporting.
-The exported file includes comprehensive information about each shared agent, such as:
+for analysis and reporting.
+The export can include agent details such as:
 Name
 Status
 Channel
 Date created
-Last Modified
+Last modified
 Publisher
-Publisher Type
+Publisher type
 Version
 Owner
 Description
@@ -591,6 +591,12 @@ Tip
 There are over 30 different items for each agent that can be included in the exported list.
 With this information, you can efficiently manage and review the shared agents within your organization, ensuring compliance and optimizing resource allocation.
+Export the list of active users for the last 30 days to an Excel file. This feature is essential for detailed analysis and reporting.
+The exported file includes comprehensive information about each active user, such as:
+User Principal Name
+Total Agents Used
+Total Sessions
+Last Activity Date
 Additional information
 Important
 Non-Microsoft tools including third-party MCP servers available in [catalog/registry/offering name] ("Third-Party Tools") are Non-Microsoft Products under your agreement governing use of the corresponding Microsoft Product. When you connect to a Third-Party Tool, you do so at your own risk. You are responsible for any terms and charges associated with use of Third-Party Tools. Microsoft has no responsibility to you or others in relation to your use of Third-Party Tools. We recommend that you carefully review and track the Third-Party Tools you add to your MCP client.

```

---

### 6. Manage federated connector availability

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/manage-federated-connectors
**Section:** Agent Governance
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -33,7 +33,7 @@ As an administrator, you can use PowerShell to manage the availability of all default federated connectors across your tenant. This centralized management approach allows you to quickly disable or enable connectors organization-wide while maintaining visibility and control over individual connector settings.
 Important
 Microsoft is retiring the command-line (CLI) toggle for setFederatedConnectors by
-August 20, 2026
+August 25, 2026
 . The CLI is being deprecated so that connector and agent settings are honored from the same global tenant settings, giving you one consistent place to govern both. Going forward, you can manage the same intent through the
 Allowed agent types
 setting in Agent 365. For more information, see
@@ -45,8 +45,6 @@ in a single operation.
 Automatically apply the setting to future default connectors
 that Microsoft releases.
-Maintain connector visibility
-in the Microsoft 365 admin center for awareness and selective management.
 Selectively enable specific connectors
 while keeping the global disable setting active.
 Reenable all connectors
@@ -56,10 +54,23 @@ Administrator role
 : Global Administrator or Search Administrator permissions
 PowerShell access
-: Ability to run PowerShell as an administrator
+: Ability to run PowerShell as an administrator (CLI will be deprecated by August 25, 2026)
 Connector.Cmd module
-: Version 2.1 or later (installed in the following steps)
-Install the PowerShell module
+: Version 2.1 or later (installed in the following steps) (CLI will be deprecated by August 25, 2026)
+Disable the agent type used by Copilot connectors
+The
+Allowed agent types
+setting provides a tenant-wide control for governing Microsoft 365 Copilot agents and connectors from a single location in the Microsoft 365 admin center. When an administrator disables the agent type used by Copilot connectors, Microsoft 365 Copilot connectors are no longer available to end users. Existing connectors remain visible to a
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Cowork available models
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
**Classification:** MEDIUM (General content update)

---

### 2. Microsoft Copilot Studio documentation
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Classification:** MEDIUM (General content update)

---

### 3. Publish and deploy Copilot Studio agents
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Classification:** MEDIUM (General content update)

---

### 4. Adaptive cards in Copilot Studio topics
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-ask-a-question#add-an-adaptive-card
**Classification:** MEDIUM (General content update)

---

### 5. Model Context Protocol in Copilot Studio
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
**Classification:** MEDIUM (General content update)

---

### 6. Connect an existing MCP server to an agent
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
**Classification:** MEDIUM (General content update)

---

### 7. Select an agent model
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Classification:** MEDIUM (General content update)

---

### 8. Agent registry in Microsoft 365 admin center
**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
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