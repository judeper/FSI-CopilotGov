# Microsoft Learn Documentation Changes

**Run Date:** 2026-05-21
**Run Time:** 2026-05-21T12:39:37.586756+00:00
**Total URLs Checked:** 154

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 33 |
| MEDIUM Changes | 12 |
| Redirects | 7 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | None | Review and update |
| 2 | microsoft-365-copilot-setup | MEDIUM | None | Review optional |
| 3 | manage-public-web-access | HIGH | None | Review and update |
| 4 | microsoft-365-copilot-privacy | HIGH | 2.7 | Review and update |
| 5 | microsoft-365-copilot-usage | HIGH | None | Review and update |
| 6 | release-notes | CRITICAL | None | Monitor |
| 7 | whats-new | CRITICAL | None | Monitor |
| 8 | ai-m365-copilot | HIGH | None | Review and update |
| 9 | endpoint-dlp-learn-about | HIGH | None | Review and update |
| 10 | audit-solutions-overview | HIGH | 3.1 | Review and update |
| 11 | audit-search | HIGH | 3.1 | Review and update |
| 12 | audit-log-activities | HIGH | 1.15 | Review and update |
| 13 | cpcn-admin-configuration | HIGH | 2.11 | Review and update |
| 14 | cpcn-compliance-summary | HIGH | 2.11 | Review and update |
| 15 | cpcn-loop-purview-management | HIGH | None | Review and update |
| 16 | cowork-admin-governance | HIGH | None | Review and update |
| 17 | concept-conditional-access-policy-common | MEDIUM | None | Review optional |
| 18 | ai-microsoft-purview | HIGH | 1.1, 1.2 | Review and update |
| 19 | .../microsoft-365/copilot/extensibility/ | HIGH | 2.14, 1.13 | Review and update |
| 20 | manage-copilot-agents-integrated-apps | HIGH | 2.13, 2.14, 1.13, 4.1, 4.13 | Review and update |
| 21 | overview-copilot-connector | HIGH | None | Review and update |
| 22 | overview-declarative-agent | HIGH | 2.14, 1.13 | Review and update |
| 23 | ...t.com/en-us/microsoft-copilot-studio/ | HIGH | 4.14 | Review and update |
| 24 | mcp-add-existing-server-to-agent | HIGH | None | Review and update |
| 25 | agent-365-overview | HIGH | 4.5, 4.13 | Review and update |
| 26 | agent-registry | HIGH | 2.14, 4.13 | Review and update |
| 27 | agent-settings | HIGH | 2.13, 2.14, 4.13 | Review and update |
| 28 | agent-registry | HIGH | None | Review and update |
| 29 | agents-are-apps | HIGH | None | Review and update |
| 30 | data-privacy-security | MEDIUM | None | Review optional |
| 31 | what-is-microsoft-entra-agent-id | MEDIUM | 2.17 | Review optional |
| 32 | what-are-agent-identities | MEDIUM | None | Review optional |
| 33 | whats-new-agent-id | MEDIUM | None | Review optional |
| 34 | what-is-agent-id-platform | MEDIUM | None | Review optional |
| 35 | agent-id | HIGH | 2.17 | Review and update |
| 36 | concept-risky-agents | MEDIUM | None | Review optional |
| 37 | agent-id-governance-overview | MEDIUM | None | Review optional |
| 38 | concept-secure-web-ai-gateway-agents | MEDIUM | None | Review optional |
| 39 | advanced-management | HIGH | 1.7 | Review and update |
| 40 | data-access-governance-reports | HIGH | 1.1, 1.7, 1.15, 1.14 | Review and update |
| 41 | insights-on-sharepoint-agents | HIGH | None | Review and update |
| 42 | content-management-assessment | HIGH | 1.7 | Review and update |
| 43 | site-lifecycle-management | HIGH | 1.7 | Review and update |
| 44 | restricted-content-discovery | HIGH | 1.7 | Review and update |
| 45 | content-governance-agent | HIGH | 1.7 | Review and update |

---

## HIGH: Control Review Recommended

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -132,50 +132,50 @@ Feature
 Word
 Draft
-âGenerate text with and without formatting in new or existing documents. Word files can also be used for grounding data.
+-Generate text with and without formatting in new or existing documents. Word files can also be used for grounding data.
 Chat
-âCreate content, summarize, ask questions about your document, and do light commanding.
+-Create content, summarize, ask questions about your document, and do light commanding.
 PowerPoint
 Draft
-âCreate a new presentation from a prompt or Word file using enterprise templates. PowerPoint files can also be used for grounding data.
+-Create a new presentation from a prompt or Word file using enterprise templates. PowerPoint files can also be used for grounding data.
 Chat
-âSummary and Q&A
+-Summary and Q&A
 Light commanding
-âAdd slides, pictures, or make deck-wide formatting changes.
+-Add slides, pictures, or make deck-wide formatting changes.
 Excel
 Draft
-âGet suggestions for formulas, chart types, and insights about data in your spreadsheet.
+-Get suggestions for formulas, chart types, and insights about data in your spreadsheet.
 Loop
 Collaborative content creation
-âCreate content that can be collaboratively improved through direct editing.
+-Create content that can be collaboratively improved through direct editing.
 Outlook
 Coaching tips
-âGet coaching tips and suggestions on clarity, sentiment, and tone, and an overall message assessment and suggestions for improvement.
+-Get coaching tips and suggestions on clarity, sentiment, and tone, and an overall message assessment and suggestions for improvement.
 Summarize
-âSummarize an email thread to quickly understand the discussion.
-Draft
-âPull from other emails or content across Microsoft 365 that the user already has access to.
+-Summarize an email thread to quickly understand the discussion.
+Draft
+-Pull from other emails or content across Microsoft 365 that the user already has access
```

---

### 2. Manage Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/copilot/microsoft-365/manage-public-web-access
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -34,7 +34,7 @@ Researcher
 and
 Analyst
-in Microsoft 365 Copilot. While web search isn't a prerequisite for using Researcher and Analyst, enabling web search is recommended to get the most value out of using them. The only difference is that Researcher and Analyst donât have a
+in Microsoft 365 Copilot. While web search isn't a prerequisite for using Researcher and Analyst, enabling web search is recommended to get the most value out of using them. The only difference is that Researcher and Analyst don't have a
 Web content
 toggle for users.
 Web search
@@ -44,8 +44,8 @@ manage whether web search is enabled
 in your environment.
 How web search works
-When web search is enabled, Microsoft 365 Copilot and Microsoft 365 Copilot Chat parse the userâs prompt and identifies terms where information from the web would improve the quality of the response. Based on these terms, Copilot generates a search query that it sends to the Bing search service asking for more information.
-This generated search query is different from the userâs original promptâit consists of a few words informed by the userâs prompt. The following information isn't included in the generated search query sent to the Bing search service:
+When web search is enabled, Microsoft 365 Copilot and Microsoft 365 Copilot Chat parse the user's prompt and identifies terms where information from the web would improve the quality of the response. Based on these terms, Copilot generates a search query that it sends to the Bing search service asking for more information.
+This generated search query is different from the user's original prompt-it consists of a few words informed by the user's prompt. The following information isn't included in the generated search query sent to the Bing search service:
 The user's entire prompt, unless the prompt is very short (for example, "local weather")
 Entire Microsoft 365 files (for example, emails or documents) or files uploaded into Copilot
 Entire we
```

---

### 3. Data, privacy, and security for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`

**What Changed:**
```diff
--- +++ @@ -62,20 +62,20 @@ Microsoft 365 Copilot community
 on the Microsoft Tech Community.
 How does Microsoft 365 Copilot use your proprietary organizational data?
-Microsoft 365 Copilot provides value by connecting LLMs to your organizational data. Microsoft 365 Copilot accesses content and context through Microsoft Graph. It can generate responses anchored in your organizational data, such as user documents, emails, calendar, chats, meetings, and contacts. Microsoft 365 Copilot combines this content with the userâs working context, such as the meeting a user is in now, the email exchanges the user had on a topic, or the chat conversations the user had last week. Microsoft 365 Copilot uses this combination of content and context to help provide accurate, relevant, and contextual responses.
+Microsoft 365 Copilot provides value by connecting LLMs to your organizational data. Microsoft 365 Copilot accesses content and context through Microsoft Graph. It can generate responses anchored in your organizational data, such as user documents, emails, calendar, chats, meetings, and contacts. Microsoft 365 Copilot combines this content with the user's working context, such as the meeting a user is in now, the email exchanges the user had on a topic, or the chat conversations the user had last week. Microsoft 365 Copilot uses this combination of content and context to help provide accurate, relevant, and contextual responses.
 Important
 Prompts, responses, and data accessed through Microsoft Graph aren't used to train foundation LLMs, including those used by Microsoft 365 Copilot.
 Microsoft 365 Copilot only surfaces organizational data to which individual users have at least view permissions. It's important that you're using the permission models available in Microsoft 365 services, such as SharePoint, to help ensure the right users or groups have the right access to the right content within your organization. This includes permissions you give to users outside your o
```

---

### 4. Copilot usage reports

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage?view=o365-worldwide
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -19,17 +19,16 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Microsoft 365 Copilot usage report - Microsoft 365 admin center
+Microsoft 365 Copilot usage report
 Feedback
 Summarize this article for me
 The Microsoft 365 Copilot usage report provides a summary of how users adopt, retain, and engage with Microsoft 365 Copilot and its associated enabled apps, including agent usage. For Copilot activity on a given day, the report typically becomes available within 72 hours of the end of that day (in UTC).
-For general information about Microsoft 365 Usage reports and to see a list of all available reports, see
+For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see
 Microsoft 365 admin center usage reports overview
 .
 View the Microsoft 365 Copilot usage report
-For information about the roles needed to view usage reports, see
+For information about the roles needed to view usage reports, see "Before you begin" in
 Microsoft 365 admin center usage reports overview
-.
 Go to the
 Microsoft 365 admin center
 .
@@ -58,7 +57,6 @@ Usage
 tab to view adoption and usage metrics.
 Interpret the Microsoft 365 Copilot usage report
-Use the Microsoft 365 Copilot usage report to see the usage of Microsoft 365 Copilot in your organization.
 At the top, you can filter by different timeframes. You can view the Microsoft 365 Copilot report over the last 7, 30, 90, or 180 days.
 You can view several numbers for Microsoft 365 Copilot usage, which highlight the enablement number and the adoption of the enablement:
 Enabled Users
@@ -148,7 +146,7 @@ , type a prompt in Copilot box, and submit. (User experience is slightly different among web, Windows, Mac, or mobile.)
 Draft an email message with Copilot in Outlook - Microsoft Support
 Coach
-Select Copilot icon in the email message, choose
+Select the Copilot icon in the email message, and then select
 Coaching by Copi
```

---

### 5. Use Purview for Copilot data security

**URL:** https://learn.microsoft.com/en-us/purview/ai-m365-copilot
**Section:** Copilot Administration
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -104,9 +104,9 @@ . Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.
 These events flow into
 activity explorer
-in DSPM for AI and the
+in the
 AI activities
-tab in activity explorer from the preview version of DSPM, where the data from prompts and responses can be displayed. You can also use the
+tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the
 Audit
 solution from the
 Microsoft Purview portal
@@ -212,7 +212,7 @@ policy location to restrict the processing of prompts that contain sensitive information types, or processing files and emails that have specific sensitivity labels applied. For more information, see
 Learn about using Microsoft Purview Data Loss Prevention to protect interactions with Microsoft 365 Copilot and Copilot Chat
 .
-Microsoft 365 Copilot Chat supports the following Endpoint DLP capabilities only:
+Microsoft 365 Copilot Chat (web version only) supports the following Endpoint DLP capabilities:
 Block paste of sensitive content
 Block files based on a specified sensitivity label
 Insider Risk Management and AI interactions

```

---

### 6. Endpoint DLP

**URL:** https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -565,7 +565,10 @@ Just-in-time protection blocks egress activities on these monitored files until policy evaluation completes successfully:
 Items that have never been evaluated.
 Items on which the evaluation has gone stale. These are previously evaluated items that haven't been reevaluated by the current, updated cloud versions of the policies.
-For more information on how just-in-time protection works, see
+Unsaved files (preview) â brand-new files that have never been saved, or existing files with unsaved modifications, including the window before autosave completes. For more information, see
+Unsaved file protection
+.
+For more information on how just-in-time protection works,see
 Learn about just-in-time protection
 , and
 Get started with Microsoft Purview Data Loss Prevention just-in-time protection

```

---

### 7. Microsoft Purview Audit overview

**URL:** https://learn.microsoft.com/en-us/purview/audit-solutions-overview
**Section:** Audit and Retention
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**What Changed:**
```diff
--- +++ @@ -46,7 +46,7 @@ 1
 Audit (Premium) includes higher bandwidth access to the Office 365 Management Activity API, which provides faster access to audit data.
 2
-In addition to the required licensing for Audit (Premium) (described in the next section), a user must be assigned a 10-Year Audit Log Retention add-on license to retain their audit records for 10 years.
+In addition to the required licensing for Audit (Premium) (described in the next section), a user must be assigned a 10-Year Audit Log Retention add-on license to retain their audit records for 10 years. Audit records generated by non-user entities (such as service principal actions, system events, and application activities) are retained for a fixed period of one year. This retention period isn't configurable and custom audit log retention policies don't apply to these records.
 Audit (Standard)
 Microsoft Purview Audit (Standard) enables you to log and search for audited activities to support your forensic, IT, compliance, and legal investigations.
 Enabled by default

```

---

### 8. Search the audit log

**URL:** https://learn.microsoft.com/en-us/purview/audit-search
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**What Changed:**
```diff
--- +++ @@ -249,7 +249,7 @@ : Additional details about the activity.
 You can sort the search job items by using the column headers or create a custom filter by using the filter pane. Use the filter to filter the search job items for specific values for any of the dashboard column criteria. To export all search job items to a .csv file, select
 Export
-on the command bar. Export supports results up to 50 KB for Audit (Standard) and up to 500 KB (500,000 rows) for Audit (Premium).
+on the command bar. Export supports results up to 50,000 rows for Audit (Standard) and up to 1,000,000 rows for Audit (Premium).
 Select a specific activity to see more details about the activity in a fly-out window. The fly-out window displays the additional information about the activity.
 Scoping access to audit logs using administrative units
 Access to search the audit log is based on the

```

---

### 9. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**What Changed:**
```diff
--- +++ @@ -1008,6 +1008,9 @@ Checked out Git branch
 GitCheckedOutBranch
 Checked out Git branch.
+Compute Items Sizes
+ComputeItemsSize
+Calculated current size of all items for the OneLake item-size report.
 Create the cross tenant auth mapping
 CreateCrossTenantAuthMapping
 Create a user mapping for the cross tenant auth feature.
@@ -1026,6 +1029,9 @@ Export item definitions
 ExportItemDefinitions
 Export multiple item definitions from a workspace.
+Get Items Sizes
+GetItemsSize
+Retrieved cached item sizes for the OneLake item-size report.
 Git connection settings updated
 GitConnectionSettingsUpdated
 Git connection settings updated.
@@ -1062,6 +1068,9 @@ Retrieved artifact's Logical Id
 ArtifactLogicalIdRetrieved
 Retrieved artifact's Logical Id.
+Set Warehouse Hardware Acceleration
+SetWarehouseHardwarePlatform
+Changed the current hardware acceleration settings for warehouses in a workspace.
 Soft delete an artifact
 ArtifactSoftDeleted
 A user soft deleted an artifact, such as a gateway or gateway cluster member, marking it for deletion while allowing recovery within a retention period.
@@ -1071,6 +1080,9 @@ Updated artifact's Logical Id
 ArtifactLogicalIdUpdated
 Updated artifact's Logical Id.
+Updated authorization setting in GraphQL
+UpdatedAuthorizationSettingGraphQL
+Updated authorization setting in GraphQL.
 Updated git items selection
 GitItemsSelectionUpdated
 Updated git items selection.
@@ -1223,7 +1235,9 @@ Are there scenarios where a user previewing a document generates FileAccessed events?
 Both the FilePreviewed and FileAccessed events indicate that a user's call led to a read of the file (or a read of a thumbnail rendering of the file). While these events are intended to align with preview versus access intention, the event distinction isn't a guarantee of the user's intent.
 What causes FileAccessed audit events in Insider Risk Management scenarios?
-Creating a case in Insider Risk Management and enabling Content Explorer generates and reco
```

---

### 10. Manage Copilot Pages and Notebooks

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-admin-configuration?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.11: Control 2.11: Copilot Pages Security and Sharing Controls
  - File: `controls/pillar-2-security/2.11-copilot-pages-security.md`

**What Changed:**
```diff
--- +++ @@ -24,9 +24,11 @@ Summarize this article for me
 Copilot Pages (
 .page
-files) and Copilot Notebooks are stored in the same user-owned SharePoint Embedded container used by Loop My workspace. Storage for these files counts toward your organization's overall SharePoint quota. For details, see
+files) and Copilot Notebooks are stored in the same user-owned SharePoint Embedded container used by Loop My workspace. In the SharePoint admin center, PowerShell, and Purview audit data, this container always appears with an application name of
+Loop
+â there's no separate Copilot Pages or Copilot Notebooks application filter. Storage counts toward your organization's overall SharePoint quota. For full details, see
 storage and lifecycle
-. IT administrators can control the creation and use of Copilot Pages and Copilot Notebooks through Cloud Policy settings.
+. IT administrators can control creation and use of Copilot Pages and Copilot Notebooks through Cloud Policy settings.
 At a glance
 What you want to control
 Where to configure
@@ -69,20 +71,19 @@ Create dynamic groups in Microsoft Entra ID
 . If you apply the policy to all users in the tenant, group setup isn't required.
 Relationship to Loop components
-Copilot Pages and Copilot Notebooks are independent of Loop. You can enable or disable them separately from Loop in your organization.
-Copilot Pages, Copilot Notebooks, and Loop My workspace use one single user-owned SharePoint Embedded container per user. For more information, see
+Copilot Pages and Copilot Notebooks are independent of Loop. You can enable or disable them separately. They do share a single user-owned SharePoint Embedded container with Loop My workspace, which has implications for the
+Create and view Copilot Pages and Copilot Notebooks
+policy:
+The shared container is created when
+either
+the Copilot Pages and Copilot Notebooks policy
+or
+the Loop
+Create Loop workspaces in Loop
+policy allows creation for the user. To prevent the cont
```

---

### 11. Copilot Pages and Notebooks compliance summary

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.11: Control 2.11: Copilot Pages Security and Sharing Controls
  - File: `controls/pillar-2-security/2.11-copilot-pages-security.md`

**What Changed:**
```diff
--- +++ @@ -112,23 +112,24 @@ Set
 guest app permissions.
 Data Lifecycle
-Tip
-Scenario: User leaves the organization
-Copilot Pages and Copilot Notebooks container follows OneDrive cleanup schedule (30 days active â 93 days to permanent deletion)
-Unlike OneDrive, there's no manager workflow to retain content
-To preserve content before departure, export using Purview or Graph API or add the container to a retention policy
+Scenario: user leaves the organization.
+The Copilot Pages and Copilot Notebooks container follows the OneDrive cleanup schedule (30 days active, then 93 days to permanent deletion). To add owners and preserve content before deletion, see
+Grant access to containers
+. To preserve content before departure, export it using Purview or the Graph API, or add the container to a retention policy.
 Storage
-: Copilot Pages and Copilot Notebooks are stored together in a single user-owned SharePoint Embedded container that is also used by Loop My workspace. In admin tools, the owning application is shown as Loop. Storage counts against your organization's SharePoint quota. See
+: Copilot Pages and Copilot Notebooks are stored together in a single user-owned SharePoint Embedded container, which is also shared by Loop My workspace. Storage counts against your organization's SharePoint quota. See
+storage
+for the full explanation of the shared container,
 Managing SharePoint Embedded containers
-.
-Limitation
-: There's no admin control to set limits on individual containers.
+for admin tooling, and
+Grant access to containers
+for the manual access workflow at user departure.
+Limitation
+: There's no admin control to set quota limits on individual containers.
 Admin control note
-: This single user-owned container can be created when either the Loop policy or the Copilot Pages and Copilot Notebooks policy allows creation for the user. To prevent creation, disable both policies for the same user.
-Limitation
-: Unlike OneDrive, there's no user workflow
```

---

### 12. Purview management for SharePoint Embedded containers

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-loop-purview-management?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -54,9 +54,16 @@ General
 tab.
 Copy the container URL.
+The container URL doesn't provide access to the container and doesn't function as a shareable link. Use it only within Purview to target the container for Purview features. To give end users a clickable link that opens the container in the Loop app, use the separate
+Container Redirect URL
+instead. For more information, see
+Grant access to containers
+.
 Note
-The container URL doesn't provide access to the container and doesn't function as a shareable link. Use the container URL only within Purview to target that container for various Purview features. A separate Application Redirect URL is the clickable link for end users with access to open the container in the Loop app. The Application Redirect URL isn't yet available, it's part of the launch of
-Roadmap ID 421612
+The
+Container Redirect URL
+field may not yet be available in the SharePoint admin center. This capability is still rolling out. Track the rollout status on the
+Microsoft 365 public roadmap
 .
 Searching the Audit Logs
 Loop application IDs:
@@ -65,6 +72,7 @@ Loop Mobile Application ID:
 0922ef46-e1b9-4f7e-9134-9ad00547eb41
 The personal user-owned container shared by Copilot Pages, Copilot Notebooks, and Loop My workspace is identified using the Loop Application IDs.
+Because these workloads share an application identity, audit events for Copilot Pages and Copilot Notebooks also appear under the Loop application IDs â there's no separate Copilot Pages or Copilot Notebooks identity to filter on in audit logs or eDiscovery.
 Search and Export
 To search and export Microsoft 365 service events for all file related activity:
 In the

```

---

### 13. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Section:** Copilot Cowork
**Classification:** HIGH (Compliance features)

**What Changed:**
```diff
--- +++ @@ -111,6 +111,9 @@ Get a full walkthrough of these controls in
 Manage agents in the Microsoft 365 admin center
 .
+Learn more about requirements in
+Cowork network endpoints
+.
 Pre-install Cowork for your users
 Instead of waiting for users to install Cowork themselves, admins can deploy it on behalf of all users or a specific group. Deploying an agent automatically installs it, and users don't need to take any other action.
 To deploy Cowork:
@@ -172,21 +175,15 @@ Note
 Agent 365 connectivity requires that users have appropriate Dynamics 365 licenses and permissions in the target environment.
 Security and compliance
-Microsoft 365 Copilot applies the same security and compliance controls to Cowork as it does to all agents.
-Data loss prevention
-Microsoft Purview DLP policies apply to Copilot agent interactions. Copilot agents, including Cowork, block sensitive information from being processed. This sensitive information includes content that matches DLP rules or documents with sensitivity labels. Learn more in
-Learn about the Microsoft 365 Copilot location for DLP
-.
-Audit logs
-Microsoft Purview audit logs capture all interactions with Cowork under
-Copilot activities
-. Log entries include the agent name, agent ID, and version. Audit Standard provides these logs at no extra cost. Learn more in
-Audit log activities for Microsoft 365 Copilot
-.
+The following security and compliance feature is available while Cowork is in Frontier preview. This list will be updated as more capabilities are released:
+Purview sensitivity label: Displays the sensitivity label for items listed in the response and citations. Using the sensitivity label's
+priority number
+defined in the
+Microsoft Purview portal
+, the latest response in Cowork displays the highest priority sensitivity label from the data used for that Copilot chat.
+Although compliance admins define a sensitivity label's priority, a higher priority number usually denotes higher sensitivity of the conte
```

---

### 14. DSPM for AI (classic) overview

**URL:** https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
**Section:** DSPM (Data Security Posture Management) and DSPM for AI (classic)
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`

**What Changed:**
```diff
--- +++ @@ -146,9 +146,9 @@ . Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.
 These events flow into
 activity explorer
-in DSPM for AI and the
+in the
 AI activities
-tab in activity explorer from the preview version of DSPM, where the data from prompts and responses can be displayed. You can also use the
+tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the
 Audit
 solution from the
 Microsoft Purview portal

```

---

### 15. Copilot extensibility overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`

**What Changed:**
```diff
--- +++ @@ -8,6 +8,7 @@ Overview
 Planning guide
 Licensing and cost considerations
+Choose your development tool
 Create and manage agents
 How-To Guide
 Agents overview
@@ -24,6 +25,6 @@ Reference
 Microsoft 365 Agents Toolkit
 Microsoft 365 Agents SDK
-Work IQ APIs (preview)
+Work IQ API (preview)
 Microsoft 365 Copilot APIs
 Microsoft Agent 365
```

---

### 16. Manage plugins for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide
**Section:** Copilot Extensibility
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 4.1: Control 4.1: Copilot Admin Settings and Feature Management
  - File: `controls/pillar-4-operations/4.1-admin-settings-feature-management.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**What Changed:**
```diff
--- +++ @@ -43,17 +43,24 @@ Microsoft Agent 365 documentation
 .
 Overview
-Agents enhance the functionality of Copilot by adding search capabilities, custom actions, connectors, and APIs. Agents are custom versions of Microsoft 365 Copilot that combine instructions, knowledge, and skills to perform specific tasks or scenarios. For more information, see
-Get started with agents for Microsoft 365 Copilot
+Agents enhance the functionality of Copilot by adding search capabilities, custom actions, connectors, and APIs. Agents are custom versions of Microsoft 365 Copilot that combine instructions, knowledge, and skills to perform specific tasks or scenarios. For more information about using agents with Copilot, see
+Get started with agents in the Microsoft 365 Copilot app
 .
-However, before users can access these agents, the agents must undergo a streamlined process of submission and approval. To learn more, see
-Publish agents
-.
-The hub Copilot experience shows the list of agents that are available and deployed for the user. Users can toggle it on or off to restrict access of Copilot to any specific agents during the interaction. Users can also add or remove agents in their Copilot experience by right-clicking on the agents and selecting the appropriate option. Users can only access the agents that the admin allows and that they install or are assigned to.
+The members of your organization can find and add agents from the
+Agent Store
+within the Microsoft 365 Copilot app. However, before users can access these agents, each agent must undergo a streamlined process of submission and approval. Agents are managed in the
+Agent Registry
+of Microsoft 365 admin center. As part of agent management, you can review
+agent requests
+and determine whether to publish the agent to the store or reject the agent submission. For more information, see
+Agent management in Microsoft 365 admin center
+. Members of your organization can only access the agents that you have allowed.
 Ag
```

---

### 17. Microsoft Graph connectors overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -22,11 +22,11 @@ Microsoft 365 Copilot connectors overview
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot connectors allow you to bring external, line-of-business data into Microsoft 365 Copilot so your users can search, reason over, and act on more of your enterprise content. The platform supports two connector models:
+Microsoft 365 Copilot connectors bring external, line-of-business data into Microsoft 365 Copilot so your users can search, reason over, and act on more of your enterprise content. The platform supports two connector models:
 Synced connectors
 ingest and index external content into Microsoft Graph.
 Federated connectors
-retrieve content in real time using Model Context Protocol (MCP) without indexing data into Microsoft Graph.
+retrieve content in real time by using Model Context Protocol (MCP) without indexing data into Microsoft Graph.
 Both connector types power Microsoft 365 Copilot and other Microsoft 365 intelligent experiences, such as Microsoft Search, Context IQ, and Microsoft 365 Copilot.
 Note
 Copilot connectors are available in commercial environments and in Microsoft 365 Government Community Cloud (GCC) and Government Community Cloud High (GCCH). They aren't available in Department of Defense (DoD) environments.
@@ -135,6 +135,26 @@ Administrators must also ensure that synced connectors are enabled for
 inline results
 .
+Microsoft 365 Copilot connector samples
+The following samples implement Microsoft 365 Copilot connectors that extend Microsoft 365 Copilot.
+Sample
+Description
+TypeScript policies connector
+This sample contains a Copilot connector that shows how to ingest local policies into Microsoft 365. For each file, it extracts the metadata from front matter, maps it to the external connection's schema, and ingests the content, retaining the content and metadata. The ingested content is set to be visible to everyone in the organization.
+.NET docs connector
+This sample .NET project shows you how
```

---

### 18. Declarative agents for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`

**What Changed:**
```diff
--- +++ @@ -31,38 +31,42 @@ Tailor declarative agents for your scenario
 Declarative agents are powered by Microsoft 365 Copilot. They use the same scalable infrastructure and platform but are scoped to meet your specific business needs. The following examples illustrate possible use cases for your agents:
 Employee IT self-help with enhanced knowledge
-- Imagine a world where your employees can resolve their technical issues without relying on the internal IT help desk. You can streamline and simplify IT workflows by building a declarative agent to expedite resolution of common issues. This specialized agent draws from internal knowledge stored in SharePoint sites to provide employees fast and effective assistance, while reducing costs for the organization.
+- Your employees can resolve their technical issues without relying on the internal IT help desk. You can streamline and simplify IT workflows by building a declarative agent to expedite resolution of common issues. This specialized agent draws from internal knowledge stored in SharePoint sites to provide employees fast and effective assistance, while reducing costs for the organization.
 Real-time customer support with seamless system integrations
-- Assume having a support team dedicated to providing customer support while also monitoring customers' live order status. You can increase the support team's productivity by enhancing your existing process with a declarative agent that seamlessly integrates with a plugin for the order management system to access and provide real-time order updates to customers.
+- Increase your customer support team's productivity by enhancing your existing process with a declarative agent that seamlessly integrates with a plugin for the order management system to access and provide real-time order updates to customers.
 Explore the benefits of declarative agents
 Some of the core benefits of using declarative agents as part of your business processes include:
 Familiar UI
 - Decla
```

---

### 19. Microsoft Copilot Studio documentation

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**What Changed:**
```diff
--- +++ @@ -27,7 +27,7 @@ Extend agents with tools
 Add tools to custom agents
 Use connectors
-Add computer use (preview)
+Add computer use
 Create and use prompts
 Create prompts with Copilot
 Create a custom prompt

```

---

### 20. Connect an existing MCP server to an agent

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
**Section:** Copilot Studio
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -267,6 +267,10 @@ Custom connectors
 .
 Locate your connector file in the list of connectors and make the necessary updates using one of the available methods.
+MCP servers and data policies
+Access to MCP servers in Copilot Studio relies on Power Platform connectors for connectivity. This condition means that if a data policy regulates Power Platform connectors, it also regulates access to the MCP server and its tools for your agent. For more information, see
+configure a data policy
+.
 Feedback
 Was this page helpful?
 Yes

```

---

### 21. Agent management in Microsoft 365 admin center

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
--- +++ @@ -69,7 +69,7 @@ Agent overview
 pane is displayed.
 Important
-Certain features are available within Microsoft 365 admin center based on services licensed in your subscription. Based on your subscription, you may see Agent 365 branding and additional agent related features and details. To view your licensed subscriptions in the
+Certain features are available within Microsoft 365 admin center based on services licensed in your subscription. To view your licensed subscriptions in the
 Microsoft 365 admin center
 , select
 Billing
@@ -77,6 +77,8 @@ Licenses
 >
 Subscriptions
+. For more information, see
+Plans and licensing
 .
 Agent overview summary
 Administrators use the Agent overview to identify and act on critical governance tasks required to maintain compliance, mitigate risk, and ensure agents are properly managed across the organization. These actions are surfaced through actionable insights in the dashboard and provide direct pathways to resolve governance gaps.
@@ -150,6 +152,7 @@ Data & tools by agent type
 .
 Agent card details
+The agents overview provides a dashboard view with cards containing specific information and status related to agents.
 Hero metrics for agent impact
 Hero metrics provide a high-level summary of the most critical indicators of agent scale and engagement.
 Agent registry

```

---

### 22. Agent registry in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**What Changed:**
```diff
--- +++ @@ -143,7 +143,18 @@ box.
 Agents without owners
 Shared agents can become ownerless when you delete the user who created them from the organization.
-To help administrators manage these scenarios, the Microsoft 365 admin center now enables you to identify and manage ownerless shared agents. The dashboard displays the total count of such agents, a one-click filter to quickly isolate them, and real-time updates that reflect user deletions. When administrators use these features, they can efficiently review and address ownership gaps by blocking or deleting affected agents.
+To help administrators manage these scenarios, the Microsoft 365 admin center enables you to identify and manage ownerless shared agents. The dashboard displays the total count of such agents, a one-click filter to quickly isolate them, and real-time updates that reflect user deletions. When administrators use these features, they can efficiently review and address ownership gaps by blocking or deleting affected agents.
+When you select the
+Agents without owners
+card, the agent list will be filtered to show the agents based on
+Publisher type
+and
+Owner
+. You can review the list of agents without owners and take appropriate actions for each agent, such as
+blocking
+or
+deleting
+the agent.
 Key features
 Ownerless agent count
 - Administrators can view the total number of agents without a valid owner directly from the dashboard. For example, the dashboard shows 20 ownerless agents, which indicates that users who left the organization created these agents.
@@ -151,52 +162,185 @@ - Selecting the dashboard pane instantly filters the agent list to display only shared agents missing an owner. This feature allows for quick triage and action.
 Real-time updates
 - The ownerless agent count automatically updates when you hard delete a user from the organization. This feature ensures that the dashboard reflects the current state without requiring manual refreshes.
-Steps to view and manage own
```

---

### 23. Agent settings in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**What Changed:**
```diff
--- +++ @@ -89,14 +89,14 @@ Sharing
 allows defining who can share agents within your organization and how sharing works.
 Options include:
-Allow all users to share with anyone in the organization
+All users
 - All users can share their agents with others in your tenant.
-No users can share with anyone in the organization
+No users
 - Sharing is disabled at the org level, but users can still share directly with specific individuals.
-Allow specific groups of users to share with anyone in the organization
+Specific users
 - Restrict broad sharing permissions to designated groups.
 Only agents built with
-Agent Builder
+Microsoft 365 Copilot Agent Builder
 are governed by sharing control.
 User access
 User access

```

---

### 24. Microsoft Agent 365 registry sync

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -27,18 +27,18 @@ Preview features aren't meant for production use and might have restricted functionality. These features are subject to
 supplemental terms of use
 , and are available before an official release so that customers can get early access and provide feedback.
-Registry sync in Microsoft Agent 365 agent registry, in the Microsoft 365 admin center, enables administrators to securely connect external AI agent environments and synchronize agents into the Agent 365 agent registry for centralized visibility and governance.
-Organizations often deploy AI agents across multiple environments such as Amazon Bedrock and Google Vertex AI. Without a centralized agent registry, administrators must manually track agents across disconnected platforms.
-By using the registry sync, administrators can:
+Registry sync in Microsoft Agent 365 agent registry, in the Microsoft 365 admin center, enables you, as an administrator, to securely connect external AI agent environments and synchronize agents into the Agent 365 agent registry for centralized visibility and governance.
+AI agents are often deployed across multiple environments such as Amazon Bedrock, Google Vertex AI, Salesforce, and Databricks. Without a centralized agent registry, you must manually track agents across disconnected platforms.
+By using the registry sync, you can:
 Connect supported thirdâparty AI platforms.
 Authenticate once per environment.
 Synchronize agents from external environments into Microsoft Agent 365 agent registry.
 Perform agent management actions supported by the AI platform APIs.
 Manage external platform connections
-Administrators can create and manage external platform connections from the
+You can create and manage external platform connections from the
 Registry sync
 page in the Microsoft 365 admin center.
-From this page, administrators can:
+From this page, you can:
 Create new platform connections.
 View connection sync status.
 Monitor last sync activity.
@@ -78,
```

---

### 25. Microsoft 365 Copilot agent governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -45,7 +45,7 @@ large color icon
 (
 color.png
-), a full-color 92x92 icon to display your agent in the Microsoft 365 Copilot UI and store
+), a full-color 192x192 icon to display your agent in the Microsoft 365 Copilot UI and store
 A
 small outline icon
 (
@@ -88,9 +88,7 @@ semver
 standard).
 id
-The unique generated identifier for this app from Microsoft Application Registration Portal (
-apps.dev.microsoft.com
-), in GUID form.
+The unique identifier for this app, in GUID form.
 developer
 Information about the developer, including name, website, and links to privacy policy and terms of use. For apps submitted to AppSource, values must match the value provided in the Partner Center app submission form.
 name
@@ -124,8 +122,8 @@  "developer": {
  "name": "Northwind Traders",
  "websiteUrl": "https://www.example.com",
- "privacyUrl": "https://www.example.com/termofuse",
- "termsOfUseUrl": "https://www.example.com/privacy"
+ "privacyUrl": "https://www.example.com/privacy",
+ "termsOfUseUrl": "https://www.example.com/termsofuse"
  },
  "icons": {
  "color": "Northwind-Logo-196.png",

```

---

### 26. Conditional Access for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**What Changed:**
```diff
--- +++ @@ -23,11 +23,16 @@ Feedback
 Summarize this article for me
 Conditional Access is an intelligent policy engine that helps organizations control how users and agent identities access corporate resources. It brings together real-time signals such as user's context, device, location, and session risk information to determine when to allow, block, or limit access, or require more verification steps.
-For a high-level overview of Conditional Access, see
+Learn about Conditional Access and agent identities:
+High-level overview of Conditional Access:
 What is Conditional Access?
-. For a high-level guide to managing agent identities across your organization, see
+Guide to managing agent identities across your organization:
 Manage agent identities in your organization
 .
+Policy templates:
+Block high-risk agent identities
+Configure policy for autonomous agent access
+Configure policy for on-behalf-of agent access
 Attribute-driven Conditional Access
 As the number of agent identities grows, individually adding each agent identity across every Conditional Access policy becomes operationally unsustainable. Before you start creating Conditional Access policies, it's important to organize the agent identities, enabling consistent, scalable access control enforcement.
 Custom security attributes in Microsoft Entra ID are a convenient way to organize agent identities at scale. Custom security attributes are business-specific key-value attributes that you can define and assign to Microsoft Entra objects, including users, agent identities, and enterprise applications (service principals). These attributes let you store meaningful information about each agent identity, like the sensitivity level of the data the agent handles.
@@ -52,17 +57,19 @@ What are custom security attributes in Microsoft Entra ID
 .
 Agent identity blueprints
-Another way to apply a Conditional Access policy to multiple agent identities at once is by targeting their parent agent identity blueprint
```

---

### 27. SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/advanced-management
**Section:** SharePoint Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -34,7 +34,7 @@ SAM capabilities are helpful as organizations
 prepare for Microsoft 365 Copilot and agents
 .
-SAM is managed primarily through the SharePoint admin center and is designed for SharePoint and Microsoft 365 administrators who are responsible for governance, risk reduction, and audit readiness. You can also use the
+Administrators primarily manage SAM through the SharePoint admin center. It's designed for SharePoint and Microsoft 365 administrators who are responsible for governance, risk reduction, and audit readiness. You can also use the
 SharePoint Admin Agent
 to make your SharePoint administration more productive and efficient.
 Manage content sprawl
@@ -88,7 +88,7 @@ Initiate site access reviews
 : Initiate site access reviews to delegate the process of reviewing DAG reports to site owners of overshared sites.
 Manage permissions and access
-SAM provides layered controls to detect oversharing, delegate remediation, and enforce leastâprivilege access across SharePoint and OneDrive.
+SAM provides layered controls to manage permissions and access, and enforce least-privilege access across SharePoint and OneDrive.
 Use Conditional Access policies
 : Use authentication contexts to connect a Microsoft Entra Conditional Access policy to a SharePoint site.
 Use site policy comparison reports
@@ -104,28 +104,8 @@ Restrict OneDrive and SharePoint site creation
 : Using PowerShell, you can designate who can create OneDrive or SharePoint sites by using security groups in Microsoft Entra ID.
 SAM prerequisites
-License requirements
-Your organization needs to have the right
-licenses
-and meet certain administrative permissions or roles to use the feature described in this article.
-First, your organization must have one of the following base licenses:
-Office 365 E3, E5, or A5
-Microsoft 365 E1, E3, E5, or A5
-Additionally, you need at least one of these licenses:
-Microsoft 365 Copilot license:
-At least one user in your organization must be as
```

---

### 28. Data access governance reports

**URL:** https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 1.14: Control 1.14: Item-Level Permission Scanning
  - File: `controls/pillar-1-readiness/1.14-item-level-permission-scanning.md`

**What Changed:**
```diff
--- +++ @@ -24,28 +24,8 @@ Summarize this article for me
 As sprawl and oversharing of SharePoint sites increase with exponential data growth, organizations need help with governing their data. Data access governance reports can help you govern access to SharePoint data. The reports let you discover sites that contain potentially overshared or sensitive content. You can use these reports to assess and apply the appropriate security and compliance policies.
 What you need to create a data access governance report
-License requirements
-Your organization needs to have the right
-licenses
-and meet certain administrative permissions or roles to use the feature described in this article.
-First, your organization must have one of the following base licenses:
-Office 365 E3, E5, or A5
-Microsoft 365 E1, E3, E5, or A5
-Additionally, you need at least one of these licenses:
-Microsoft 365 Copilot license:
-At least one user in your organization must be assigned a Copilot license (this user doesn't need to be a SharePoint administrator).
-Microsoft SharePoint Advanced Management license:
-Available as a standalone purchase.
-Administrator requirements
-You must be a
-SharePoint administrator
-or have equivalent permissions.
-Additional information
-If your organization has a Copilot license and at least one person in your organization is assigned a Copilot license, SharePoint administrators automatically gain access to the
-SharePoint Advanced Management features needed for Copilot deployment
-.
-For organizations without a Copilot license, you can use SharePoint Advanced Management features
-by purchasing a standalone SharePoint Advanced Management license
+See
+Prerequisites for SharePoint Advanced Management
 .
 The reports are currently unavailable for Gallatin, even if you have the required licenses.
 How to access the Data access governance reports in the SharePoint admin center

```

---

### 29. Agent insights report in SharePoint

**URL:** https://learn.microsoft.com/en-us/sharepoint/insights-on-sharepoint-agents
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -22,29 +22,15 @@ Insights report on agents in SharePoint
 Feedback
 Summarize this article for me
-Insights report on agents in SharePoint provides SharePoint Administrators with rich information on the recently created agents across all SharePoint sites and OneDrive sites within their organization. This report provides admins with the ability to learn about the sites with the highest number of agents created. Using this report, SharePoint admins can further govern and maintain the integrity of the content used by agents as grounding data.
-The insights report is based on the Microsoft audit data logged for the agents, created in SharePoint, through the FileCreated and FileRenamed events.
-You can generate and manage agent insights report in SharePoint Admin Center or with SharePoint Online Management Shell.
-What do you need to access agent insights report
-License requirements
-Your organization needs to have the right
-licenses
-and meet certain administrative permissions or roles to use the feature described in this article.
-First, your organization must have one of the following licenses:
-Office 365 E3, E5, or A5
-Microsoft 365 E1, E3, E5, or A5
-Additionally, you need to have a Microsoft 365 Copilot license.
-Note
-At least one user in your organization must be assigned a Copilot license (this user doesn't need to be a SharePoint administrator).
-If your organization has a Copilot license and at least one person in your organization is assigned a Copilot license, SharePoint administrators automatically gain access to the
-SharePoint Advanced Management features needed for Copilot deployment
+The insights report on agents in SharePoint provides SharePoint administrators with rich information on the recently created agents across all SharePoint sites and OneDrive sites within their organization. This report helps admins learn about the sites with the highest number of agents created. By using this report, SharePoint admins can further govern and mai
```

---

### 30. SAM Content Management Assessment

**URL:** https://learn.microsoft.com/en-us/sharepoint/content-management-assessment
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -64,28 +64,8 @@ On-demand reassessment
 : Allow administrators to rerun the assessment monthly to ensure continuous improvement and compliance.
 What do you need to access Content Management Assessment?
-License requirements
-Your organization needs to have the right
-licenses
-and meet certain administrative permissions or roles to use the feature described in this article.
-First, your organization must have one of the following base licenses:
-Office 365 E3, E5, or A5
-Microsoft 365 E1, E3, E5, or A5
-Additionally, you need at least one of these licenses:
-Microsoft 365 Copilot license:
-At least one user in your organization must be assigned a Copilot license (this user doesn't need to be a SharePoint administrator).
-Microsoft SharePoint Advanced Management license:
-Available as a standalone purchase.
-Administrator requirements
-You must be a
-SharePoint administrator
-or have equivalent permissions.
-Additional information
-If your organization has a Copilot license and at least one person in your organization is assigned a Copilot license, SharePoint administrators automatically gain access to the
-SharePoint Advanced Management features needed for Copilot deployment
-.
-For organizations without a Copilot license, you can use SharePoint Advanced Management features
-by purchasing a standalone SharePoint Advanced Management license
+See
+SharePoint Advanced Management prerequisites
 .
 Where to find Content Management Assessment
 You can access Content Management Assessment in the SharePoint Admin Center:

```

---

### 31. SharePoint site lifecycle management

**URL:** https://learn.microsoft.com/en-us/sharepoint/site-lifecycle-management
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -26,31 +26,10 @@ Microsoft SharePoint Advanced Management
 help you improve site governance by automating the process of detecting inactive sites and notifying site owners by email. Site owners can then review and confirm whether their sites are still active.
 You can configure an inactive sites policy in the SharePoint admin center. This article describes how to set up an inactive site policy with notifications and enforcement actions.
-What do you need to create an inactive site policy?
-License requirements
-Your organization needs to have the right
-licenses
-and meet certain administrative permissions or roles to use the feature described in this article.
-First, your organization must have one of the following base licenses:
-Office 365 E3, E5, or A5
-Microsoft 365 E1, E3, E5, or A5
-Additionally, you need at least one of these licenses:
-Microsoft 365 Copilot license:
-At least one user in your organization must be assigned a Copilot license (this user doesn't need to be a SharePoint administrator).
-Microsoft SharePoint Advanced Management license:
-Available as a standalone purchase.
-Administrator requirements
-You must be a
-SharePoint administrator
-or have equivalent permissions.
-Additional information
-If your organization has a Copilot license and at least one person in your organization is assigned a Copilot license, SharePoint administrators automatically gain access to the
-SharePoint Advanced Management features needed for Copilot deployment
-.
-For organizations without a Copilot license, you can use SharePoint Advanced Management features
-by purchasing a standalone SharePoint Advanced Management license
-.
-How do inactive site policies work?
+Prerequisites for an inactive site policy
+See
+SharePoint Advanced Management prerequisites
+.
 Scope of inactive site policies
 You can configure parameters for an inactive site policy, such as inactive time period, template type, site creation source, sensitivity labels, and exclusion of up
```

---

### 32. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -40,30 +40,10 @@ Active sites
 tab to first compile a selective list of targeted sites.
 What you need to restrict a specific SharePoint access?
-License requirements
-Your organization needs to have the right
-licenses
-and meet certain administrative permissions or roles to use the feature described in this article.
-First, your organization must have one of the following base licenses:
-Office 365 E3, E5, or A5
-Microsoft 365 E1, E3, E5, or A5
-Additionally, you need at least one of these licenses:
-Microsoft 365 Copilot license:
-At least one user in your organization must be assigned a Copilot license (this user doesn't need to be a SharePoint administrator).
-Microsoft SharePoint Advanced Management license:
-Available as a standalone purchase.
-Administrator requirements
-You must be a
-SharePoint administrator
-or have equivalent permissions.
-Additional information
-If your organization has a Copilot license and at least one person in your organization is assigned a Copilot license, SharePoint administrators automatically gain access to the
-SharePoint Advanced Management features needed for Copilot deployment
+See
+SharePoint Advanced Management prerequisites
 .
-For organizations without a Copilot license, you can use SharePoint Advanced Management features
-by purchasing a standalone SharePoint Advanced Management license
-.
-In addition to preceding information, you also need the latest version of
+Also download the latest version of
 Microsoft SharePoint Online Management Shell
 .
 Configure Restricted Content Discovery

```

---

### 33. SharePoint Admin Agent (Content Governance Agent)

**URL:** https://learn.microsoft.com/en-us/sharepoint/content-governance-agent
**Section:** SharePoint Administration
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -72,7 +72,14 @@ Microsoft 365 Backup
 , and
 version history
-How to open the SharePoint Admin Agent
+SharePoint Admin Agent prerequisites
+Your organization must have SharePoint Advanced Management. See
+SharePoint Advanced Management prerequisites
+.
+To use the SharePoint Admin Agent, you must have the
+SharePoint Advanced Management Administrator
+role assigned in Microsoft Entra ID.
+Open the SharePoint Admin Agent
 Open the SharePoint Admin Agent in Microsoft 365 Copilot, the SharePoint admin center, or Microsoft Teams.
 SharePoint Admin Agent in Agents in Microsoft 365 Copilot
 :
@@ -107,34 +114,9 @@ multi-geo organization
 )
 As you submit a question, the SharePoint Admin Agent responds by gathering the relevant data and reports, offering analysis and recommendations, and suggesting other prompts. You can choose appropriate next steps from there.
-SharePoint Admin Agent prerequisites
-SAM capabilities
-Make sure SAM capabilities, including
-catalog management
-, are set up and configured. See
-Get ready for Microsoft 365 Copilot and Agents with SharePoint Advanced Management
-.
-License requirements
-Your organization needs to have the right
-licenses
-and meet certain administrative permissions or roles to use the feature described in this article.
-First, your organization must have one of the following licenses:
-Office 365 E3, E5, or A5
-Microsoft 365 E1, E3, E5, or A5
-Additionally, you need to have a Microsoft 365 Copilot license.
-Note
-At least one user in your organization must be assigned a Copilot license (this user doesn't need to be a SharePoint administrator).
-If your organization has a Copilot license and at least one person in your organization is assigned a Copilot license, SharePoint administrators automatically gain access to the
-SharePoint Advanced Management features needed for Copilot deployment
-.
-Administrator requirements
-You must be a
-SharePoint administrator
-or have equivalent permissions.
-SharePoint Advanced Mana
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot setup guide
**URL:** https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-setup
**Classification:** MEDIUM (General content update)

---

### 2. Microsoft 365 Copilot release notes
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Classification:** CRITICAL (Deprecation notice)

---

### 3. What's new in Microsoft Purview
**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Classification:** CRITICAL (Deprecation notice)

---

### 4. Common Conditional Access policies
**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common
**Classification:** MEDIUM (General content update)

---

### 5. Copilot agent security and compliance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security
**Classification:** MEDIUM (General content update)

---

### 6. Microsoft Entra Agent ID overview
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
**Classification:** MEDIUM (General content update)

---

### 7. Microsoft Entra agent identity concepts
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities
**Classification:** MEDIUM (General content update)

---

### 8. What's new in Microsoft Entra Agent ID
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
**Classification:** MEDIUM (General content update)

---

### 9. Microsoft Entra Agent identity platform
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform
**Classification:** MEDIUM (General content update)

---

### 10. Identity Protection for agents
**URL:** https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents
**Classification:** MEDIUM (General content update)

---

### 11. Microsoft Entra ID Governance for agent identities
**URL:** https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
**Classification:** MEDIUM (General content update)

---

### 12. Network controls for Copilot Studio agents
**URL:** https://learn.microsoft.com/en-us/entra/global-secure-access/concept-secure-web-ai-gateway-agents
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/manage-public-web-access | https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-loop-purview-management?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-365/loop/purview-management?view=o365-worldwide |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*