# Microsoft Learn Documentation Changes

**Run Date:** 2026-06-13
**Run Time:** 2026-06-13T11:47:22.034575+00:00
**Total URLs Checked:** 152

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 12 |
| MEDIUM Changes | 3 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | CRITICAL | 4.12 | Monitor |
| 2 | connect-to-ai-subprocessor | HIGH | 3.8a, 2.7 | Review and update |
| 3 | dlp-policy-reference | HIGH | None | Review and update |
| 4 | ...osoft365-copilot-location-learn-about | HIGH | 2.1 | Review and update |
| 5 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Review and update |
| 6 | audit-log-activities | HIGH | 1.15 | Review and update |
| 7 | create-retention-policies | HIGH | 3.2 | Review and update |
| 8 | cowork-admin-governance | MEDIUM | None | Review optional |
| 9 | overview-copilot-connector | MEDIUM | 2.13 | Review optional |
| 10 | agent-365-overview | HIGH | 4.13, 4.5 | Review and update |
| 11 | agent-id | HIGH | 2.3, 2.17 | Review and update |
| 12 | ...opilot-sharepoint-advanced-management | HIGH | 1.13, 1.3 | Review and update |
| 13 | ai-in-sharepoint-get-started | HIGH | None | Review and update |
| 14 | content-governance-agent | HIGH | 1.7 | Review and update |
| 15 | archive-overview | HIGH | 3.2 | Review and update |

---

## HIGH: Control Review Recommended

### 1. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`

**What Changed:**
```diff
--- +++ @@ -19,29 +19,50 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Anthropic as a subprocessor for Microsoft Online Services
+Anthropic models in Microsoft Online Services
 Feedback
 Summarize this article for me
 Microsoft is introducing a new offering with Anthropic AI models as part of Microsoft Online Services, delivering enterprise-grade commitments and safeguards to ensure secure and responsible use of Anthropic models within your organization.
-To enable this change, Anthropic has onboarded as a Microsoft subprocessor. As part of this update, we're deprecating the previous option that allowed Microsoft tenant admins to opt in to use Anthropic models under Anthropic's separate commercial terms and data processing agreement. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework.
-As a subprocessor, Anthropic will operate with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. The Microsoft
-Product Terms
+To enable this change, Anthropic has onboarded as a Microsoft subprocessor. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered by the CCC, including Microsoft 365 Copilot and Copilot Studio.
+As a subprocessor, Anthropic will operate with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. Unless models are labeled "Preview models with Data Retention," the
+Microsoft Product Terms
 and
 Microsoft Data Protection Addendum (DPA)
 apply to use of Anthropic models through Microsoft's enterprise Online Services. Such use is also covered under our
 Enterprise Data Protection
-. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered b
```

---

### 2. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -1921,6 +1921,8 @@ Conditions Microsoft 365 Copilot supports
 This feature is in preview.
 Content contains (sensitivity labels)
+Content contains (sensitive information types)
+Email is received from (External users) (preview)
 Condition groups
 Sometimes you need a rule to identify only one thing, such as all content that contains a U.S. Social Security Number, which is defined by a single SIT. However, in many scenarios where the types of items you're trying to identify are more complex and therefore harder to define, more flexibility in defining conditions is required.
 For example, to identify content subject to the U.S. Health Insurance Act (HIPAA), you need to look for:
@@ -2761,7 +2763,7 @@ Content is shared from Microsoft 365
 - with people outside my organization
 Not configured
-User notification emails, policy tips, DLP alerts, and incident reports are sent only when a file is shared with a guest and a guest access the file.
+User notification emails, policy tips, DLP alerts, and incident reports are sent when a file is shared with a guest or when a guest accesses the file.
 Content is shared from Microsoft 365
 - only with people inside my organization
 Not configured
@@ -2800,7 +2802,7 @@ Block everyone
 - When the first user outside the organization access the document, the event causes the document to be blocked.
 - It's expected that for a short time, the document is accessible by guests who have the link to the file.
-- User notification emails, policy tips, DLP alerts, and incident reports are sent when a file is shared with an guest and an guest accesses that file.
+- User notification emails, policy tips, DLP alerts, and incident reports are sent when a file is shared with a guest or when a guest accesses that file.
 Content is shared from Microsoft 365
 - with people outside my organization
 -

```

---

### 3. DLP for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`

**What Changed:**
```diff
--- +++ @@ -22,13 +22,15 @@ Learn about using Microsoft Purview Data Loss Prevention to protect interactions with Microsoft 365 Copilot and Copilot Chat
 Feedback
 Summarize this article for me
-Microsoft Purview Data Loss Prevention (DLP) can help you protect interactions with Microsoft 365 Copilot and Copilot Chat in two ways:
-Restrict Microsoft 365 Copilot from using external web search when prompts contain sensitive data (preview)
-, you can use Microsoft Purview Data Loss Prevention (DLP) policies to prevent Microsoft 365 Copilot and Copilot Chat from sending sensitive information to external web services. When a prompt contains sensitive information types (SITs)âsuch as credit card numbers, passport numbers, Social Security numbers, or custom SITs defined by your organizationâCopilot automatically blocks the use of external web search as a grounding source for that prompt. Instead, Copilot continues to generate responses using permitted internal Microsoft 365 data sources, where applicable. This ensures that sensitive data remains protected and is not shared with external search providers.
-Restrict Microsoft 365 Copilot and Copilot Chat from processing sensitive prompts
-, you can create a DLP policy to help protect against the use of sensitive information types (SIT), such as credit card numbers, passport identification, or social security numbers in Microsoft Copilot 365 prompts. This includes Microsoft provided SITs and custom SITs that you create. This real-time control helps organizations mitigate data leakage and oversharing risks by preventing Microsoft 365 Copilot and Copilot Chat, including prebuilt agents in Microsoft 365 Copilot and Copilot Chat, from returning a response when prompts contain sensitive data and from using that sensitive data for both internal and external web searches.
-Restrict M365 Copilot and Copilot Chat processing sensitive files and emails (generally available)
-, you can create a DLP policy to help protect against the i
```

---

### 4. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

**What Changed:**
```diff
--- +++ @@ -754,6 +754,49 @@ However currently, restricted admins won't be able to see labeling activities for OneDrive in activity explorer.
 Tip
 You can also use content explorer to identify locations that have documents with sensitive information, but are unlabeled. Using this information, consider adding these locations to your auto-labeling policy, and include the identified sensitive information types as rules.
+Policy-level labeling activity for SharePoint and OneDrive
+For auto-labeling policies that are turned on and target SharePoint and OneDrive, you can monitor them right from the main
+Auto-labeling
+page and use the per-policy review pages. Use these pages to monitor day-to-day labeling activity, spot-check labeled files, and investigate labeling failures.
+To view the review pages, you need one of the following roles:
+Compliance Administrator
+Compliance Data Administrator
+Information Protection Admin
+Information Protection Analyst
+To see the matched text inside a file from the
+Contextual summary
+tab, you also need the
+Data Classification Content Viewer
+role.
+To open these pages, from
+Information Protection
+>
+Auto-labeling
+, select the name of an auto-labeling policy. Most data on the review pages reflects activity from the last 30 days.
+The policy
+Overview
+page shows labeled and failed file counts, a daily activity trend chart, the top labels applied, and the top sites where labeling occurred. A
+Labeling failures
+card surfaces the total failure count and the top three failure reasons so you can quickly identify whether the policy needs attention.
+From the
+Labeled items
+tab, you can toggle between a
+Labeled
+view (a sample of successfully labeled files) and a
+Failed
+view (files the policy couldn't label, grouped by failure reason). Select any item to open a details flyout pane that includes a file preview, file properties, and a
+Contextual summary
+tab that explains in plain language why the file matched or why labeling faile
```

---

### 5. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**What Changed:**
```diff
--- +++ @@ -1207,6 +1207,9 @@ Downloaded dataflow refresh logs
 DownloadedDataflowRefreshLogs
 Downloaded dataflow refresh logs.
+Edited Power BI semantic model options
+EditedSemanticModelOptions
+A user made a change to their semantic model options. This occurs when changes are made in the model options dialog.
 Export item definitions
 ExportItemDefinitions
 Export multiple item definitions from a workspace.

```

---

### 6. Create and configure retention policies

**URL:** https://learn.microsoft.com/en-us/purview/create-retention-policies
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.2: Control 3.2: Data Retention Policies for Copilot Interactions
  - File: `controls/pillar-3-compliance/3.2-data-retention-policies.md`

**What Changed:**
```diff
--- +++ @@ -100,7 +100,7 @@ . When you configure retention settings for the
 Teams channel message
 location, if a team has any shared channels, they inherit retention settings from their parent team.
-From late April 20206, retention policies also support newly created Teams call logs when you create the retention policies with PowerShell. For more information, see
+From late April 2026, retention policies also support newly created Teams call logs when you create the retention policies with PowerShell. For more information, see
 Retention policy for Teams call logs
 .
 Sign in to the Microsoft Purview portal
@@ -205,9 +205,7 @@ Retention policy for Teams call logs
 Teams call logs represent the collection of call-related data generated by Teams, including call data records (CDRs) and other call metadata. CDRs are also sometimes referred to as call detail records, or just call records.
 Prior to supporting the retention of Teams call logs in late April 2026, CDRs for Teams chat and Teams channels were included in retention policies for the Teams chat location. Going forward, new CDRs are supported only when you create a retention policy for Teams call logs. CDRs included in previous Teams chat retention policies continue to be managed by those same policies.
-This separate retention policy for call logs can be created only by using PowerShell, and has the following considerations:
-The policy is tenant-wide and can't be scoped to individual users.
-The policy doesn't support adaptive scopes or administrative units.
+This separate retention policy for call logs can be created and modified only by using PowerShell. It has the following considerations:
 The policy includes call logs for both Teams chat and Teams channels.
 The policy applies only to new call logs that are created after the policy is configured and active.
 After you create the retention policy for Teams call logs, it's displayed in
@@ -215,14 +213,13 @@ >
 Policies
 in the Microsoft Purview portal, wh
```

---

### 7. Agent management in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 4.5: Control 4.5: Copilot Usage Analytics and Adoption Reporting
  - File: `controls/pillar-4-operations/4.5-usage-analytics.md`

**What Changed:**
```diff
--- +++ @@ -53,15 +53,33 @@ The Microsoft Frontier program gives organizations early access to innovative and emerging AI capabilities in Microsoft 365 before those features reach general availability (GA). Frontier previews are subject to the existing preview terms of your customer agreements. For more information, see
 Get started with the Microsoft Frontier program
 .
-Prerequisites
+Prerequisites for agent management
 Before you can manage agents in the Microsoft 365 admin center, confirm the following requirements are met:
-Your organization has the required Microsoft 365 subscription and licenses for either Microsoft 365 Copilot or Microsoft Agent 365 capabilities.
-Users who create, publish, or use agents have the appropriate licenses assigned.
-Youâre assigned an administrator role that includes permissions to manage settings for either Microsoft 365 Copilot or Microsoft Agent 365 in the Microsoft 365 admin center.
+Your organization has the required subscription and licenses for either Microsoft 365, Microsoft 365 Copilot, or Microsoft Agent 365.
+Users at your organization that create, publish, or use agents have the appropriate licenses assigned.
+Youâre assigned an administrator role that includes permissions to manage settings for Microsoft 365, Microsoft 365 Copilot, or Microsoft Agent 365 in the Microsoft 365 admin center.
 For more information, see the following resources:
+Licensing for agent management
+Agent management roles and permissions
+Licensing for agent management
+The following licensing options include agents that can be managed in Microsoft 365 admin center:
+Microsoft 365 plans
+Microsoft 365 (All Suites) includes Copilot Chat. Copilot Chat provides web data agents.
+Microsoft 365 (E7) includes Microsoft 365 E5, Microsoft 365 Copilot, Microsoft Agent 365, and Microsoft Entra Suite.
+Microsoft 365 Copilot
+This license can be added to your Microsoft 365 license (E3, E5). It's included with your Microsoft 365 license (E7). This optio
```

---

### 8. Conditional Access for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.3: Control 2.3: Conditional Access Policies for Copilot Workloads
  - File: `controls/pillar-2-security/2.3-conditional-access-policies.md`
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**What Changed:**
```diff
--- +++ @@ -32,6 +32,7 @@ Guide to managing agent identities across your organization:
 Manage agent identities in your organization
 .
+How to target agent identities in Conditional Access
 Configure policies for autonomous agent access
 How Conditional Access evaluates agent access requests
 To access a corporate resource such as SharePoint file, MCP servers, or Open API services, a user or agent first requests an access token from Microsoft Entra ID.
@@ -77,25 +78,17 @@ Agents might access resources without a signed-in user. In this case the agent accesses the resource with its own identity. This flow is also known as client credentials flow, or app only access. All types of agents might use this flow. For more information about how agents authenticate with their own identity, see
 Agent OAuth flows: Autonomous apps
 .
-The following diagram shows the application only access authorization flow.
 This flow applies in the following common scenarios:
 Autonomous agents that operate independently
-:
-These agents run in the background, respond to events, or run on a schedule.
-For example, an agent that generates a daily report and sends the result to a group of employees. In this scenario, there's no user present, and the agent operates on its own.
+run in the background, respond to events, or run on a schedule.
+For example, an agent that generates a daily report and sends the result to a group of employees.
+In this scenario, there's no user present, and the agent operates on its own.
 Interactive agents that use their own identity
-:
-These agents don't always access resources on a user's behalf; sometimes they use their own identity.
+don't always access resources on a user's behalf; sometimes they use their own identity.
 For example, if an agent calls a backend SMS service that users don't have access to, the OBO flow doesn't apply, and the agent authenticates directly as itself.
 Agents published on the web for public use
-:
-These agents either don't authent
```

---

### 9. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`

**What Changed:**
```diff
--- +++ @@ -260,7 +260,9 @@ .
 In the SharePoint admin center, select the
 Copilot
-button.
+button, and then select the
+View prompts
+button in the lower corner of the Copilot pane.
 In Microsoft Teams, select
 Apps
 , and then search for

```

---

### 10. AI in SharePoint (preview)

**URL:** https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,81 +19,39 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Get started with AI in SharePoint (preview)
+Get started with Copilot in SharePoint (preview)
 Feedback
 Summarize this article for me
 Note
-This article applies to the preview version of AI capabilities in SharePoint (previously referred to as Knowledge Agent).
-AI in SharePoint isn't currently supported in Microsoft 365 GovernmentâGCC, GCC High, DoD, Office 365 air-gapped cloud environments, or Microsoft 365 operated by 21Vianet.
+This article applies to the preview version of Copilot in SharePoint (previously referred to as AI in SharePoint).
+Copilot in SharePoint isn't currently supported in Microsoft 365 GovernmentâGCC, GCC High, DoD, Office 365 air-gapped cloud environments, or Microsoft 365 operated by 21Vianet.
+Copilot in SharePoint helps you do more with your content. Ask questions, run workflows, and create SharePoint sites, pages, lists, libraries, interactive reports, and Office files using natural language. Starting in mid-June 2026, these capabilities roll out as an opt-out preview and become available automatically to all users with a Microsoft 365 Copilot license.
 Important
-AI in SharePoint capabilities require sites to be explicitly opted in to the AI in SharePoint public preview, or for the tenant to be opted in at the tenant level. Sites that are not opted in do not receive preview benefits.
+Copilot in SharePoint is changing from an opt-in preview to an opt-out preview. No administrator action is required to receive it. If you previously opted out your tenant or specific sites, those settings are honored.
 Prerequisites
-To use AI in SharePoint during Public Preview,
-all
-of the following requirements must be met.
+To use Copilot in SharePoint during the preview:
 Microsoft 365 Copilot license:
-Users must have an active Microsoft 365 Copilot license. AI in SharePoint is included with this license during Public Preview and at Ge
```

---

### 11. SharePoint Admin Agent (Content Governance Agent)

**URL:** https://learn.microsoft.com/en-us/sharepoint/content-governance-agent
**Section:** SharePoint Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -72,6 +72,12 @@ Microsoft 365 Backup
 , and
 version history
+Manage data residency compliance
+with
+Multi-Geo capabilities
+, such as cross-geography content move status reports (
+Preview
+)
 SharePoint Admin Agent prerequisites
 Your organization must have SharePoint Advanced Management. See
 SharePoint Advanced Management prerequisites
@@ -80,20 +86,23 @@ SharePoint Advanced Management Administrator
 role assigned in Microsoft Entra ID.
 Open the SharePoint Admin Agent
-Open the SharePoint Admin Agent in Microsoft 365 Copilot, the SharePoint admin center, or Microsoft Teams.
-SharePoint Admin Agent in Microsoft 365 Copilot
+Open the SharePoint Admin Agent by using any of the following methods:
+Open the SharePoint Admin Agent in the Microsoft 365 Copilot app
+Access content governance skills for Copilot in the SharePoint admin center
+Open the SharePoint Admin Agent in Microsoft Teams
+Open the SharePoint Admin Agent in Microsoft 365 Copilot
 In the Microsoft 365 Copilot app, expand
 Agents
 , and search for the SharePoint Admin Agent.
-After adding it, you can use the agent in the Copilot app.
-Prompts for Copilot in the SharePoint admin center
-In the SharePoint admin center, select the
+Use the agent in the Copilot app.
+Access content governance skills in Copilot in the SharePoint admin center
+Copilot in the SharePoint admin center includes content governance skills.
+Select the
 Copilot
-button.
-Select the
+button, and then select the
 View prompts
-button to view and use Governance skills.
-SharePoint Admin Agent in Microsoft Teams
+button to view and use governance skills.
+Open the SharePoint Admin Agent in Microsoft Teams
 In Microsoft Teams, select
 Apps
 , and then search for
@@ -101,20 +110,39 @@ .
 Get started with example prompts
 To help you get started, the SharePoint Admin Agent suggests prompts that you can try in your environment.
-Here are some more example prompts:
+As you submit a question, the SharePoint Admin Agent responds 
```

---

### 12. Microsoft 365 Archive overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide
**Section:** Microsoft 365 Archive
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 3.2: Control 3.2: Data Retention Policies for Copilot Interactions
  - File: `controls/pillar-3-compliance/3.2-data-retention-policies.md`

**What Changed:**
```diff
--- +++ @@ -74,7 +74,7 @@ Older versions of Office desktop apps that haven't had updates since March 1, 2026.
 Other apps such as Clipchamp and Power BI fail to load archived content when attempting to import.
 File-level archive is available only for SharePoint sites. When archived files are copied or moved, they retain their archived state. However, if an archived file is moved or copied into OneDrive, that archived state might not always be visually represented in the OneDrive user interface.
-Files that are reactivated cannot be archived again for 30 days.
+Files that are reactivated cannot be archived again for 120 days.
 Certain file types can't be archived, including OneNote, SharePoint pages, and SharePoint agents.
 The Site Assets library on SharePoint sites does not support file-level archive.
 Related articles

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. What's new in Microsoft Purview
**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Classification:** CRITICAL (Deprecation notice)

---

### 2. Copilot Cowork admin and governance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Classification:** MEDIUM (General content update)

---

### 3. Microsoft Graph connectors overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*