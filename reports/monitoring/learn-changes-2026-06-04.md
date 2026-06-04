# Microsoft Learn Documentation Changes

**Run Date:** 2026-06-04
**Run Time:** 2026-06-04T12:38:27.157618+00:00
**Total URLs Checked:** 154

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 22 |
| MEDIUM Changes | 10 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-privacy | MEDIUM | 1.10, 1.4, 2.6, 2.7, 3.10, 3.8, 3.8a | Review optional |
| 2 | copilot-teams-transcription | MEDIUM | 4.2 | Review and update |
| 3 | release-notes | HIGH | 4.12 | Review and update |
| 4 | whats-new | CRITICAL | 4.12 | Monitor |
| 5 | dlp-policy-reference | HIGH | None | Review and update |
| 6 | create-sensitivity-labels | HIGH | None | Review and update |
| 7 | sensitivity-labels-office-apps | HIGH | None | Review and update |
| 8 | audit-search | MEDIUM | 3.1, 3.14 | Review optional |
| 9 | audit-log-activities | CRITICAL | 1.15 | Monitor |
| 10 | retention | MEDIUM | 4.2, 3.2, 3.11, 3.14 | Review optional |
| 11 | create-retention-policies | HIGH | 3.2 | Review and update |
| 12 | retention-policies-teams | HIGH | 4.2 | Review and update |
| 13 | cowork-faq | MEDIUM | None | Review optional |
| 14 | plan-conditional-access | HIGH | 2.3 | Review and update |
| 15 | information-barriers-teams | HIGH | 2.4 | Review and update |
| 16 | communication-compliance-policies | CRITICAL | 3.5, 3.4 | Review and update |
| 17 | ai-microsoft-purview | MEDIUM | 1.2, 1.1, index, 2.1 | Review optional |
| 18 | ...curity-posture-management-learn-about | HIGH | 1.14, 3.10 | Review and update |
| 19 | .../microsoft-365/copilot/extensibility/ | HIGH | 4.13, 1.13, 2.13, 2.17, 2.16, 2.14 | Review and update |
| 20 | agent-builder-build-agents | HIGH | None | Review and update |
| 21 | mcp-add-existing-server-to-agent | HIGH | None | Review and update |
| 22 | authoring-select-agent-model | HIGH | None | Review and update |
| 23 | overview | HIGH | None | Review and update |
| 24 | agent-365-overview | HIGH | 4.5, 4.13 | Review and update |
| 25 | agent-registry | HIGH | 4.13, 2.14 | Review and update |
| 26 | agent-id | HIGH | 2.17 | Review and update |
| 27 | concept-risky-agents | HIGH | None | Review and update |
| 28 | data-connectors-reference | CRITICAL | 4.11, 3.1 | Monitor |
| 29 | ai-in-sharepoint-get-started | MEDIUM | None | Review optional |
| 30 | content-governance-agent | HIGH | 1.7 | Review and update |
| 31 | overview | HIGH | None | Review and update |

---

## HIGH: Control Review Recommended

### 1. Copilot in Teams meetings

**URL:** https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 4.2: Control 4.2: Copilot in Teams Meetings Governance
  - File: `controls/pillar-4-operations/4.2-teams-meetings-governance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.2/powershell-setup.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,7 +19,7 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Manage Microsoft 365 Copilot in Teams meetings and events
+Manage Teams meeting transcription
 Feedback
 Summarize this article for me
 APPLIES TO:

```

---

### 2. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**What Changed:**
```diff
--- +++ @@ -30,6 +30,168 @@ Android
 iOS
 Mac
+June 2, 2026
+Updates released between May 19, 2026, June 2, 2026
+Microsoft 365 admin center
+Organizational Messages Usageâbased targeting is now generally available in the Microsoft 365 admin center!
+[Web]
+Organizational Messages now supports usageâbased targeting in addition to existing groupâbased targeting capabilities. This enables admins to deliver Organizational Messages based on real user behavior and engagement patterns rather than static group membership.
+Roadmap ID:
+503563
+Details:
+What changed:
+Admins can now target Organizational Messages using dynamic usage behaviors through Usageâbased targeting. This allows IT admins to drive Microsoft 365 Copilot adoption by reaching users based on actual product usage instead of relying only on preâconfigured groups or distribution lists.
+By leveraging dynamic, preâdefined usage segments, admins can deliver timely and relevant guidance to the right users to improve awareness, engagement, and value realization from Copilot investments.
+The initial release includes two Action Segments focused on Copilot adoption:
+Inactive Copilot Users for the past 28 days
+Inactive Copilot Users in Teams for the past 30 days
+Why this matters:
+Business impact:
+Enables more precise and effective Copilot adoption campaigns by targeting users based on actual behavior, helping organizations improve engagement and maximize value from Copilot investments.
+Personal impact:
+Users receive more relevant and timely communications tailored to their usage patterns, helping them better discover and adopt Microsoft 365 Copilot capabilities.
+Organizational Messages now supports Email messages
+[Web]
+Organizational Messages in the Microsoft 365 Admin Center now supports email delivery in addition to other surfaces like the Windows Taskbar, Windows Spotlight, Windows Notification Center, and Teams Popovers. This gives admins another familiar communication channel while keepi
```

---

### 3. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -2178,8 +2178,48 @@ .
 Supported actions: SharePoint
 Restrict access or encrypt the content in Microsoft 365 locations
+Block everyone
+Block only people from outside your organization
+Block access for specific external domains or users (in public preview)
+The
+Block access for specific external domains or users
+sub-option lets you block external access by domain (for example,
+partner.com
+) or by user SMTP (for example,
+user@example.com
+). You can also specify allow lists by using
+Domain IS NOT
+or
+User IS NOT
+. Internal users and domains can't be blocked with this sub-option; continue to use
+Block everyone
+for internal users.
+Note
+When you use
+Block access for specific external domains or users
+: if a user or domain appears in both allow and block lists, the block takes effect (most restrictive wins). If a file matches both an allow rule and a block rule, evaluation is across all matching rules â allowed users and domains are permitted, blocked users and domains are denied, and users in neither list are blocked by default.
 Supported actions: OneDrive
 Restrict access or encrypt the content in Microsoft 365 locations
+Block everyone
+Block only people from outside your organization
+Block access for specific external domains or users (in public preview)
+The
+Block access for specific external domains or users
+sub-option lets you block external access by domain (for example,
+partner.com
+) or by user SMTP (for example,
+user@example.com
+). You can also specify allow lists by using
+Domain IS NOT
+or
+User IS NOT
+. Internal users and domains can't be blocked with this sub-option; continue to use
+Block everyone
+for internal users.
+Note
+When you use
+Block access for specific external domains or users
+: if a user or domain appears in both allow and block lists, the block takes effect (most restrictive wins). If a file matches both an allow rule and a block rule, evaluation is per rule â allowed users and domains are permitted, 
```

---

### 4. Create and configure sensitivity labels

**URL:** https://learn.microsoft.com/en-us/purview/create-sensitivity-labels
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -275,6 +275,11 @@ Create policy
 configuration. For example, from the Microsoft Purview portal:
 Note
+For more information about the
+Export policies
+option that can capture detailed information about these policies and all sensitivity labels in your tenant, see
+Export policy configuration in Microsoft Purview
+.
 If you had default sensitivity labels created for you, you also have a
 default label publishing policy
 , which you can modify or supplement with additional policies.

```

---

### 5. Mandatory labeling

**URL:** https://learn.microsoft.com/en-us/purview/sensitivity-labels-office-apps#require-users-to-apply-a-label
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -26,22 +26,23 @@ When you have
 published
 sensitivity labels from the Microsoft Purview portal, they start to appear in Office apps for users to classify and protect data as it's created or edited.
-Use the information in this article to help you successfully manage sensitivity labels in Office apps. For example, additional configuration information for specific labeling features.
+This article helps you successfully manage sensitivity labels in Office apps. For example, you can find additional configuration information for specific labeling features.
 Sensitivity labeling support in apps
 To use sensitivity labels in Office apps, you must use a subscription edition of Office. Use the licensing link at the top of this page to identify eligible plans. Sensitivity labels aren't supported for standalone editions of Office, sometimes called "Office Perpetual".
-For Outlook (Windows, macOS, iOS, Android, and on the web), the mailbox must be hosted in Exchange Online. Sensitivity labels aren't supported for mailboxes that are hosted on-premises. This also applies to shared mailboxes, even if the users accessing them have mailboxes in Exchange Online.
+For Outlook (Windows, macOS, iOS, Android, and on the web), the mailbox must be hosted in Exchange Online. Sensitivity labels aren't supported for mailboxes that are hosted on-premises. This on-premises limitation also applies to shared mailboxes, even if the users accessing them have mailboxes in Exchange Online.
 Support for sensitivity label capabilities in apps
 Use the tables in
 Minimum versions for sensitivity labels in Office apps
-to identify the minimum Office version that introduced specific capabilities for sensitivity labels in Office apps. Or, if the label capability is in public preview.
+to identify the minimum Office version that introduced specific capabilities for sensitivity labels in Office apps, or whether the label capability is in public preview.
 In addition to listing the minimum version
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
--- +++ @@ -75,6 +75,7 @@ (applicable
 pre-migration
 only)
+Teams call logs
 Microsoft Copilot experiences
 Enterprise AI apps
 Other AI apps
@@ -99,11 +100,9 @@ . When you configure retention settings for the
 Teams channel message
 location, if a team has any shared channels, they inherit retention settings from their parent team.
-Retention policies also support newly created call data records, which are system-generated messages that contain
-metadata for meetings and calls
-. All call data records are always included with the
-Teams chats
-location, even call data records for Teams channel messages and Teams private channel messages.
+From late April 20206, retention policies also support newly created Teams call logs when you create the retention policies with PowerShell. For more information, see
+Retention policy for Teams call logs
+.
 Sign in to the Microsoft Purview portal
 >
 Solutions
@@ -202,15 +201,34 @@ When you select
 Edit
 for the Teams chats location, you might see guests and non-mailbox users. Retention policies aren't designed for these users, so don't select them.
-To include newly created call data records for Teams channel messages and Teams private channel messages, you must select the
-Teams chats
-location, instead of the
-Teams channel messages
-and
-Teams private channel messages
-locations.
-Additional retention policy needed to support Teams
-Teams is more than just chats and channel messages. If you have teams that were created from a Microsoft 365 group (formerly Office 365 group), you should additionally configure a retention policy that includes that Microsoft 365 group by using the
+Before late April 2026: Teams call data records (CDRs) for Teams chat and channel messages were included in Teams chat retention policies. Now, CDRs are included only in a retention policy for Teams call logs, as documented in the next section.
+Retention policy for Teams call logs
+Teams call logs represent the collection of call-related data genera
```

---

### 7. Retention for Teams

**URL:** https://learn.microsoft.com/en-us/purview/retention-policies-teams
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 4.2: Control 4.2: Copilot in Teams Meetings Governance
  - File: `controls/pillar-4-operations/4.2-teams-meetings-governance.md`

**What Changed:**
```diff
--- +++ @@ -24,14 +24,13 @@ Summarize this article for me
 Microsoft Purview service description
 Note
-If you are seeing a message in Teams that your chats or messages have been deleted by a retention policy, see
+If you're seeing a message in Teams that your chats or messages have been deleted by a retention policy, see
 Teams messages about retention policies
 .
 The information on this page is for IT administrators who manage these retention policies.
-Microsoft Purview Data Lifecycle Management (DLM) now supports retention and deletion for Microsoft Teams call logs, replacing the previous default of indefinite retention. General Availability begins rolling out in late April 2026.
 The information in this article supplements
 Learn about retention
-because it has information that's specific to Microsoft Teams messages.
+because it has information that's specific to Microsoft Teams messages and call logs.
 For other workloads, see:
 Learn about retention for SharePoint and OneDrive
 Learn about retention for Viva Engage
@@ -42,9 +41,6 @@ Retention policies support
 shared channels
 . Any shared channels inherit retention settings from the parent team.
-Retention policies also support messages posted with the
-chat with yourself
-feature.
 Teams chats messages and
 Facilitator interactions in meetings
 , channel messages, and private channel messages can be deleted by using retention policies for Teams. In addition to the text in the messages, the following items from these interactions can be retained for compliance reasons:
@@ -53,13 +49,15 @@ card content
 .
 These chat messages and private channel messages include all the names of the people in the conversation, and channel messages include the team name and the message title (if supplied).
-Code snippets, recorded voice memos from the Teams mobile client, thumbnails, announcement images, and reactions from others in the form of emoticons aren't retained when you use retention policies for Teams.
-Call data re
```

---

### 8. Plan a Conditional Access deployment

**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access
**Section:** Conditional Access
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.3: Control 2.3: Conditional Access Policies for Copilot Workloads
  - File: `controls/pillar-2-security/2.3-conditional-access-policies.md`

**What Changed:**
```diff
--- +++ @@ -175,6 +175,48 @@ .
 Use filter for applications to include or exclude applications instead of individually specifying them
 .
+Govern and manage policies at scale
+As your organization grows, managing Conditional Access policies at scale requires deliberate governance practices. Conditional Access has a hard limit of 240 policies per tenant across all policy states (see
+Minimize the number of Conditional Access policies
+and
+Microsoft Entra service limits and restrictions
+), so scaling effectively means
+consolidating
+policies, not adding more. Consider these strategies to maintain control over a large policy set:
+Establish naming and ownership conventions.
+Adopt a consistent
+naming convention
+that identifies each policy's purpose, target, and scope at a glance. Because Conditional Access policies don't have a built-in owner attribute, encode ownership in the policy name (for example, a team prefix) and maintain an out-of-band registry that maps each policy to a responsible admin or team.
+Audit and consolidate regularly.
+Review your policies periodically to remove redundant or conflicting rules. Where it's enabled in your tenant, the
+Conditional Access Optimization Agent
+with Microsoft Security Copilot can analyze your existing policies, identify gaps in coverage, and suggest consolidation opportunities. The agent requires Microsoft Security Copilot with provisioned security compute units (SCUs) and Microsoft Entra ID P1, so it isn't available in every tenant; for details, see the agent
+prerequisites
+.
+Monitor impact with reporting tools.
+Use the
+Conditional Access Insights and Reporting workbook
+to visualize policy impact across your tenant. Stream sign-in logs to a Log Analytics workspace so you can query trends, identify policy conflicts, and track coverage over time. The workbook requires Microsoft Entra ID P1 and a Log Analytics workspace that's receiving sign-in logs; for details, see the workbook
+prerequisites
+.
+Troubleshoot e
```

---

### 9. Information barriers in Teams

**URL:** https://learn.microsoft.com/en-us/purview/information-barriers-teams
**Section:** Information Barriers
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.4: Control 2.4: Information Barriers for Copilot (Chinese Wall)
  - File: `controls/pillar-2-security/2.4-information-barriers.md`

**What Changed:**
```diff
--- +++ @@ -215,8 +215,8 @@ for a smoother experience.
 Users can't join channel meetings
 : If you enable IB policies, users can't join channel meetings if they're not a member of the team. The root cause is that IB checks rely on whether users can be added to a meeting chat roster, and only when they can be added to the roster are they allowed to join the meeting. The chat thread in a channel meeting is available to Team/Channel members only, and non-members can't see or access the chat thread. If you enable IB for the organization and a non-team member attempts to join a channel meeting, that user isn't allowed to join the meeting. However, if you don't enable IB for the organization and a nonteam member attempts to join a channel meeting, the user is allowed to join the meeting but they don't see the chat option in the meeting.
-IB policies don't work for federated users
-: If you allow federation with external organizations, the users of those organizations aren't restricted by IB policies. If users of your organization join a chat or meeting organized by external federated users, then IB policies also don't restrict communication between users of your organization.
+IB policies are supported in federated communication
+: If you allow federation with external organizations, the users of those organizations aren't restricted by IB policies. If users of your organization join a group chat, meeting chat, or a call organized by external federated users, IB policies continue to restrict communication between users of your organization.
 Next steps
 Use Information Barriers with SharePoint
 : Enable IB on SharePoint sites connected to Teams.

```

---

### 10. Create communication compliance policies

**URL:** https://learn.microsoft.com/en-us/purview/communication-compliance-policies
**Section:** Communication Compliance
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 3.5: Control 3.5: FINRA Rule 2210 Compliance for Copilot-Drafted Communications
  - File: `controls/pillar-3-compliance/3.5-finra-2210-compliance.md`
- Control 3.4: Control 3.4: Communication Compliance Monitoring
  - File: `controls/pillar-3-compliance/3.4-communication-compliance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.4/powershell-setup.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -26,13 +26,16 @@ Microsoft Purview Communication Compliance
 provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.
 Policies
+Create Communication Compliance policies for Microsoft 365 organizations in the Microsoft Purview portal. Communication Compliance policies define which communications and users are subject to review in your organization, set custom conditions the communications must meet, and specify who should do reviews.
+Users assigned the
+Communication Compliance Admins
+role can set up policies and access the
+Communication Compliance
+page and global settings in Microsoft Purview.
+You can export the modification history to a .csv file that includes the status of alerts pending review, escalated items, and resolved items.
+You can't rename policies, but you can delete them when no longer needed.
 Important
 PowerShell isn't supported for creating and managing Communication Compliance policies. To create and manage these policies, use the policy management controls in the Communication Compliance solution.
-Create Communication Compliance policies for Microsoft 365 organizations in the Microsoft Purview portal. Communication Compliance policies define which communications and users are subject to review in your organization, set custom conditions the communications must meet, and specify who should do reviews. Users assigned the
-Communication Compliance Admins
-role can set up policies. Anyone with this role can access the
-Communication Compliance
-page and global settings in Microsoft Purview. If needed, you can expo
```

---

### 11. Learn about DSPM

**URL:** https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
**Section:** DSPM (Data Security Posture Management) and DSPM for AI (classic)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.14: Control 1.14: Item-Level Permission Scanning
  - File: `controls/pillar-1-readiness/1.14-item-level-permission-scanning.md`
- Control 3.10: Control 3.10: SEC Reg S-P -- Privacy of Consumer Financial Information
  - File: `controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md`

**What Changed:**
```diff
--- +++ @@ -58,6 +58,11 @@ Outcome
 card displays key metrics, such as the percentage of data covered by policies, number of risky sharing incidents, or improvements over time. This information lets you quickly see your current security posture and track progress as you remediate risks.
 Within each outcome, you see suggested prioritized actions, such as applying sensitivity labels, configuring DLP policies, or investigating alerts, all tailored to your organzation's data. You can take action directly from the workflow, such as remediating oversharing, configuring one-click policies, or launching investigations into suspicious activity. Reporting and analytics are also organized by outcome, making it easier to identify and report improvements, compliance, and risk reduction.
+The
+Prevent exfiltration to risky destinations
+objective also supports
+proactive AI insights powered by Data Security Investigations
+. When enabled, Data Security Investigations automatically creates and refreshes an investigation that continuously analyzes recently exfiltrated sensitive data across five risk categories.
 Operational insights are surfaced throughout Data Security Posture Management, including:
 Impact prediction visuals and progress tracking for remediation steps
 Role-based access controls to provide granular access to features and AI content for delegated administration and compliance
@@ -70,6 +75,9 @@ . Use the
 View agent activity
 options throughout the data security objectives for easy access to the agents' activity.
+For example, the
+proactive AI insights
+feature uses Data Security Investigations to automatically analyze exfiltrated data and surface risk counts by category on the exfiltration objective card, without requiring manual investigation creation.
 These AI capabilities from Data Security Posture Management help ensure that sensitive data is governed, labeled, and monitored, with streamlined management. For more information:
 How AI is used within Data Sec
```

---

### 12. Copilot extensibility overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`
- Control 2.16: Control 2.16: Federated Copilot Connector and Model Context Protocol (MCP) Governance
  - File: `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`

**What Changed:**
```diff
--- +++ @@ -27,4 +27,5 @@ Microsoft 365 Agents SDK
 Work IQ API (preview)
 Microsoft 365 Copilot APIs
+Interactive Demo (preview)
 Microsoft Agent 365
```

---

### 13. Build agents with Agent Builder

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
**Section:** Copilot Extensibility
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -110,6 +110,10 @@ For more information about icons, see
 Design icons for agent acquisition and management
 .
+Model
+You can specify the default response mode for your agent. Users can always override this when using the agent. For details, see
+Set the default response mode
+.
 Description
 The description helps the Large Language Model (LLM) identify and use your agent for a specific task or situation. Make it as short, precise, and simple as possible. It's also displayed in the app file for use in the app catalog. Character limit of 1,000 characters.
 Instructions
@@ -187,6 +191,26 @@ - Generates images based on user prompts. To add this capability, select the toggle next to
 Create images
 .
+Set the default response mode
+In the
+Model
+section of the
+Configure
+tab, set the default response mode for your agent. The response mode controls how the agent approaches each question, whether it prioritizes speed or takes more time for in-depth analysis. Users can always override this setting by using the model selector when using the agent.
+The following response modes are available:
+Mode
+Description
+Auto
+(default)
+The agent automatically chooses the best approach based on each question, balancing speed and depth of analysis.
+Quick response
+The agent replies quickly, keeping responses concise. This mode is best for straightforward questions that don't require in-depth analysis.
+Think deeper
+The agent takes more time to carefully analyze the question before responding. This mode works best for complex tasks that benefit from a more thorough answer.
+Note
+The default response mode isn't applied when the agent is invoked via
+@mention
+from the main Copilot experience. This is a known issue.
 Test your agent
 The
 Try it

```

---

### 14. Connect an existing MCP server to an agent

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
**Section:** Copilot Studio
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -23,11 +23,15 @@ Feedback
 Summarize this article for me
 If you already set up a Model Context Protocol (MCP) server, you can connect the MCP server to your agent.
-You can connect your agent to an MCP server in Copilot Studio in two ways:
+There are two ways to connect your agent to an MCP server in Copilot Studio:
 Add the MCP server in Copilot Studio by using the
 MCP onboarding wizard
 (recommended)
 Create a custom connector to your server through Power Apps
+This article describes details for both of these methods.
+Alternatively, you can register your existing MCP server in Agents 365 using the Agents 365 CLI and Microsoft 365 Admin Center. Once the server is properly registered and approved, it becomes available for use in Copilot Studio. For more information, see
+Bring your own (BYO) MCP server
+.
 If you don't yet have an MCP server set up, see
 Create a new MCP server
 for information on how to get started.

```

---

### 15. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -256,6 +256,21 @@ -
 -
 Experimental (early access environment)
+Mistral Medium 3.5
+General
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental (cross-geo)
+Experimental (cross-geo)
 Note
 Models marked as
 cross-geo
@@ -382,8 +397,9 @@ Admins control whether makers can add external models to agents. To grant access to external models, admins must complete the following actions:
 Turn on external models
 in Power Platform admin center for the environment or the environment group.
-Allow access to each external model in the Microsoft 365 admin center. Learn more in the Microsoft 365 admin center documentation:
+Allow access to each external model provider in the Microsoft 365 admin center. Learn more in the Microsoft 365 admin center documentation:
 Connect to Anthropic LLM
+Connect to Mistral
 Connect to xAI
 Preview models and external models are two different sets that can overlap but aren't the same, and their settings are separate. For example:
 Admins can block external models but allow preview or experimental models. In this case, makers can't use external models but can use preview, experimental, and generally available internal models.

```

---

### 16. Microsoft Agent 365 overview

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/overview
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -53,7 +53,7 @@ . At launch, a set of
 pre-integrated ecosystem partner agents
 are available to deploy directly from the Microsoft 365 admin center.
-Microsoft Agent 365 does not require specific product prerequisites to enable; however, it is recommended that customers have Entra P1, Entra P2, or Entra Suite in addition to Purview Data Loss Prevention to make full use of the benefits. At least one user must be licensed with a
+Microsoft Agent 365 works best when using Microsoft E5 as a pre-requisite. At least one user must be licensed with a
 qualifying Microsoft Agent 365 license
 to enable Agent 365.
 Plans and licensing
@@ -64,7 +64,7 @@ Microsoft Agent 365 Licensing FAQs
 .
 Next step
-Onboard to Microsoft Agent 365
+Why does an enterprise need Agent 365?
 Feedback
 Was this page helpful?
 Yes

```

---

### 17. Agent management in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.5: Control 4.5: Copilot Usage Analytics and Adoption Reporting
  - File: `controls/pillar-4-operations/4.5-usage-analytics.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**What Changed:**
```diff
--- +++ @@ -53,6 +53,15 @@ The Microsoft Frontier program gives organizations early access to innovative and emerging AI capabilities in Microsoft 365 before those features reach general availability (GA). Frontier previews are subject to the existing preview terms of your customer agreements. For more information, see
 Get started with the Microsoft Frontier program
 .
+Prerequisites
+Before you can manage agents in the Microsoft 365 admin center, confirm the following requirements are met:
+Your organization has the required Microsoft 365 subscription and licenses for either Microsoft 365 Copilot or Microsoft Agent 365 capabilities.
+Users who create, publish, or use agents have the appropriate licenses assigned.
+Youâre assigned an administrator role that includes permissions to manage settings for either Microsoft 365 Copilot or Microsoft Agent 365 in the Microsoft 365 admin center.
+For more information, see the following resources:
+Plans and licensing for Microsoft Agent 365
+License options for Microsoft 365 Copilot
+Agent management roles and permissions
 View the Agent overview
 You can access and view the
 Agent overview

```

---

### 18. Agent registry in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`

**What Changed:**
```diff
--- +++ @@ -418,6 +418,10 @@ Review and finished. Select
 Finish deployment
 .
+Note
+If your tentant uses unified agent and app management, all changes to org-wide tenant settings in Microsoft 365 admin center (MAC) are automatically synchronized in Teams admin center (TAC) and vice versa. For more information, see
+Unified agent and app management
+.
 Manage pinned agents
 As an administrator, you can choose to pin a deployed agent to the
 Agents

```

---

### 19. Conditional Access for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**What Changed:**
```diff
--- +++ @@ -19,132 +19,64 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Conditional Access for agent identities
+Conditional Access for agents
 Feedback
 Summarize this article for me
-Conditional Access is an intelligent policy engine that helps organizations control how users and agent identities access corporate resources. It brings together real-time signals such as user's context, device, location, and session risk information to determine when to allow, block, or limit access, or require more verification steps.
-Learn about Conditional Access and agent identities:
+Conditional Access is an intelligent policy engine that helps organizations control how users and agents access corporate resources. It brings together real-time signals such as user's and agent's context, device, location, and session risk information to determine when to allow, block, or limit access, or require more verification steps.
+Conditional Access for agents requires Microsoft Entra ID P1 or P2 and a Microsoft Agent 365 license for each user. Enforcement of Agent 365 licensing is coming soon. Network controls for agents require Microsoft Entra Internet Access. For more information, see
+What is Microsoft Entra Agent ID
+.
+Learn about Conditional Access for agents:
 High-level overview of Conditional Access:
 What is Conditional Access?
 Guide to managing agent identities across your organization:
 Manage agent identities in your organization
 .
-Policy templates:
-Block high-risk agent identities
-Configure policy for autonomous agent access
-Configure policy for on-behalf-of agent access
-Attribute-driven Conditional Access
-As the number of agent identities grows, individually adding each agent identity across every Conditional Access policy becomes operationally unsustainable. Before you start creating Conditional Access policies, it's important to organize the agent identities, enabling consistent, scalable access control enforcement.
-Custom s
```

---

### 20. Identity Protection for agents

**URL:** https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -22,9 +22,9 @@ ID Protection for agents (Preview)
 Feedback
 Summarize this article for me
-As organizations adopt, build, and deploy autonomous AI agents, the need to monitor and protect those agents becomes critical. Microsoft Entra ID Protection helps protect your organization by automatically detecting and responding to identity-based risks on agents that use the
+As organizations adopt, build, and deploy autonomous AI agents, the need to monitor and protect those agents becomes critical. Microsoft Entra ID Protection helps protect your organization by automatically detecting and responding to identity-based risks on agents that have agent identities provided by
 Microsoft Entra Agent ID
-platform.
+.
 Prerequisites
 Roles
 To use our Risky Agent reports, you must have one of the following administrator roles assigned.
@@ -57,7 +57,7 @@ What is Global Secure Access
 .
 How it works
-Because agents can operate autonomously and on behalf of a user, they can display unique sign-in behavior. Agents can take initiative, interact with sensitive data, and operate at scale. Microsoft Entra ID Protection for agents is designed to identify and mitigate risks associated with these capabilities. The system determines a baseline for an agent's normal activity and then continuously monitors it for anomalies in Microsoft Entra ID. Once an agent exhibits suspicious behavior, ID Protection flags the activity and marks it as risky.
+Because agents can operate autonomously and on behalf of (OBO) a user, they can display unique sign-in behavior. Agents can take initiative, interact with sensitive data, and operate at scale. Microsoft Entra ID Protection for agents is designed to identify and mitigate risks associated with these capabilities. The system determines a baseline for an agent's normal activity and then continuously monitors it for anomalies in Microsoft Entra ID. Once an agent exhibits suspicious behavior, ID Protection flags the activity and marks it as risky
```

---

### 21. SharePoint Admin Agent (Content Governance Agent)

**URL:** https://learn.microsoft.com/en-us/sharepoint/content-governance-agent
**Section:** SharePoint Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -81,18 +81,19 @@ role assigned in Microsoft Entra ID.
 Open the SharePoint Admin Agent
 Open the SharePoint Admin Agent in Microsoft 365 Copilot, the SharePoint admin center, or Microsoft Teams.
-SharePoint Admin Agent in Agents in Microsoft 365 Copilot
-:
+SharePoint Admin Agent in Microsoft 365 Copilot
 In the Microsoft 365 Copilot app, expand
 Agents
 , and search for the SharePoint Admin Agent.
-Copilot in the SharePoint admin center
-:
+After adding it, you can use the agent in the Copilot app.
+Prompts for Copilot in the SharePoint admin center
 In the SharePoint admin center, select the
 Copilot
 button.
+Select the
+View prompts
+button to view and use Governance skills.
 SharePoint Admin Agent in Microsoft Teams
-:
 In Microsoft Teams, select
 Apps
 , and then search for

```

---

### 22. Zero Trust deployment guide

**URL:** https://learn.microsoft.com/en-us/security/zero-trust/deploy/overview
**Section:** Zero Trust and Security Architecture
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,88 +19,66 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Zero Trust deployment for technology pillars
+Overview - Technology pillars
 Feedback
 Summarize this article for me
-Because your organization might already have elements of Zero Trust protections already in place, this documentation set provides conceptual information to get you started and deployment plans and implementation recommendations for end-to-end adherence to Zero Trust principles. Each article acts as a checklist of deployment objectives with steps and links to more information.
-You deploy Zero Trust principles across your IT infrastructure by implementing Zero Trust controls and technologies across seven technology pillars. Six of these pillars are signal sources, a control plane for enforcement, and a critical resource to be defended. The seventh pillar is the pillar that collects signals from the first six pillars and provides visibility for security incidents and automation and orchestration for responding to and mitigating cybersecurity threats.
-The following articles provide conceptual information and deployment objectives for these seven technology pillars. Use these articles to assess your readiness and build a deployment plan to apply
-Zero Trust principles
+This article summarizes technology pillars in our
+Zero Trust adoption model
 .
+Technology pillars represent the core areas of your security architecture. They group related capabilities and controls into logical domains such as identity, endpoints, data, apps, infrastructure, networks, and security operations.
+Each pillar answers the same fundamental question:
+How do we apply Zero Trust principles to this part of the environment?
+Instead of thinking in terms of individual products or features, pillars provide a stable way to organize security design and implementation across your environment.
+Technology pillars in the adoption model
+Our structured adoption model focuses on 
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Data, privacy, and security for Microsoft 365 Copilot
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
**Classification:** MEDIUM (General content update)

---

### 2. Copilot in Teams meetings
**URL:** https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription
**Classification:** MEDIUM (General content update)

---

### 3. What's new in Microsoft Purview
**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Classification:** CRITICAL (Deprecation notice)

---

### 4. Search the audit log
**URL:** https://learn.microsoft.com/en-us/purview/audit-search
**Classification:** MEDIUM (General content update)

---

### 5. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** CRITICAL (Deprecation notice)

---

### 6. Learn about retention policies
**URL:** https://learn.microsoft.com/en-us/purview/retention
**Classification:** MEDIUM (General content update)

---

### 7. Copilot Cowork FAQ
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Classification:** MEDIUM (General content update)

---

### 8. DSPM for AI (classic) overview
**URL:** https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
**Classification:** MEDIUM (General content update)

---

### 9. Connect Microsoft 365 data
**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Classification:** CRITICAL (UI navigation steps changed)

---

### 10. AI in SharePoint (preview)
**URL:** https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*