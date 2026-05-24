# Microsoft Learn Documentation Changes

**Run Date:** 2026-05-14
**Run Time:** 2026-05-14T11:44:30.554076+00:00
**Total URLs Checked:** 154

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 17 |
| MEDIUM Changes | 1 |
| Redirects | 6 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | None | Review and update |
| 2 | manage-public-web-access | HIGH | None | Review and update |
| 3 | microsoft-365-copilot-privacy | HIGH | 2.7 | Review and update |
| 4 | whats-new | HIGH | None | Review and update |
| 5 | endpoint-dlp-learn-about | HIGH | None | Review and update |
| 6 | audit-search | HIGH | 3.1 | Review and update |
| 7 | audit-log-activities | HIGH | 1.15 | Review and update |
| 8 | cpcn-compliance-summary | HIGH | 2.11 | Review and update |
| 9 | cpcn-loop-purview-management | HIGH | None | Review and update |
| 10 | ...t.com/en-us/microsoft-copilot-studio/ | HIGH | 4.14 | Review and update |
| 11 | agent-registry | MEDIUM | None | Review optional |
| 12 | advanced-management | HIGH | 1.7 | Review and update |
| 13 | data-access-governance-reports | HIGH | 1.15, 1.1, 1.14, 1.7 | Review and update |
| 14 | insights-on-sharepoint-agents | HIGH | None | Review and update |
| 15 | content-management-assessment | HIGH | 1.7 | Review and update |
| 16 | site-lifecycle-management | HIGH | 1.7 | Review and update |
| 17 | restricted-content-discovery | HIGH | 1.7 | Review and update |
| 18 | content-governance-agent | HIGH | 1.7 | Review and update |

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

### 4. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -125,9 +125,19 @@ Updated
 : Restructured the
 just-in-time (JIT) protection
-documentation. The
+documentation.
+Updated
+: The
 Get started with just-in-time protection
 article now focuses on deployment and configuration steps.
+In preview
+:
+Unsaved file protection
+extends just-in-time (JIT) protection to files that haven't been saved yet, including brand-new files and files with unsaved modifications. For more information, see
+Get started with just-in-time protection
+and
+Learn about unsaved file protection
+.
 New
 : A new conceptual article,
 Learn about just-in-time protection

```

---

### 5. Endpoint DLP

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

### 6. Search the audit log

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

### 7. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**What Changed:**
```diff
--- +++ @@ -1223,7 +1223,9 @@ Are there scenarios where a user previewing a document generates FileAccessed events?
 Both the FilePreviewed and FileAccessed events indicate that a user's call led to a read of the file (or a read of a thumbnail rendering of the file). While these events are intended to align with preview versus access intention, the event distinction isn't a guarantee of the user's intent.
 What causes FileAccessed audit events in Insider Risk Management scenarios?
-Creating a case in Insider Risk Management and enabling Content Explorer generates and records a FileAccessed event in the audit log. In this scenario, the event is generated by the Insider Risk Management/Content Explorer workflow rather than by a direct user file-open action, and the same ApplicationId value is used for these events. This is important for administrators because it helps distinguish these system-generated FileAccessed events from other FileAccessed activity during an investigation. You can use the ApplicationId field as one of the properties to help identify or filter these specific events when reviewing audit log results.
+Creating a case in Insider Risk Management and enabling Content Explorer generates and records a FileAccessed event in the audit log. In this scenario, the event is generated by the Insider Risk Management/Content Explorer workflow rather than by a direct user file-open action, and the same ApplicationId value,
+92876b03-76a3-4da8-ad6a-0511ffdf8647
+, is used for these events. This is important for administrators because it helps distinguish these system-generated FileAccessed events from other FileAccessed activity during an investigation. You can use the ApplicationId field as one of the properties to help identify or filter these specific events when reviewing audit log results.
 The app@sharepoint user in audit records
 In audit records for some file activities (and other SharePoint-related activities), you might notice the user who performed the 
```

---

### 8. Copilot Pages and Notebooks compliance summary

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.11: Control 2.11: Copilot Pages Security and Sharing Controls
  - File: `controls/pillar-2-security/2.11-copilot-pages-security.md`

**What Changed:**
```diff
--- +++ @@ -114,9 +114,11 @@ Data Lifecycle
 Tip
 Scenario: User leaves the organization
-Copilot Pages and Copilot Notebooks container follows OneDrive cleanup schedule (30 days active â 93 days to permanent deletion)
-Unlike OneDrive, there's no manager workflow to retain content
-To preserve content before departure, export using Purview or Graph API or add the container to a retention policy
+Copilot Pages and Copilot Notebooks container follows OneDrive cleanup schedule (30 days active â 93 days to permanent deletion).
+To add owners and preserve content before deletion, see
+Grant access to containers
+.
+To preserve content before departure, export using Purview or Graph API or add the container to a retention policy.
 Storage
 : Copilot Pages and Copilot Notebooks are stored together in a single user-owned SharePoint Embedded container that is also used by Loop My workspace. In admin tools, the owning application is shown as Loop. Storage counts against your organization's SharePoint quota. See
 Managing SharePoint Embedded containers
@@ -125,9 +127,8 @@ : There's no admin control to set limits on individual containers.
 Admin control note
 : This single user-owned container can be created when either the Loop policy or the Copilot Pages and Copilot Notebooks policy allows creation for the user. To prevent creation, disable both policies for the same user.
-Limitation
-: Unlike OneDrive, there's no user workflow for content after departure. The container is deleted on the same schedule as OneDrive defaults. See
-Storage management after user departure
+Unlike OneDrive, there's no automatic manager access workflow. IT admins must manually add owners. See
+Grant access to containers
 .
 Multi-Geo
 :
@@ -183,6 +184,7 @@ from Microsoft Purview Data Lifecycle Management configured for all SharePoint sites are enforced for all Copilot Pages and Copilot Notebooks.
 For more information on how to configure specific Copilot Notebooks, see
 Purview and SharePoint 
```

---

### 9. Purview management for SharePoint Embedded containers

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-loop-purview-management?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -55,8 +55,10 @@ tab.
 Copy the container URL.
 Note
-The container URL doesn't provide access to the container and doesn't function as a shareable link. Use the container URL only within Purview to target that container for various Purview features. A separate Application Redirect URL is the clickable link for end users with access to open the container in the Loop app. The Application Redirect URL isn't yet available, it's part of the launch of
-Roadmap ID 421612
+The container URL doesn't provide access to the container and doesn't function as a shareable link. Use the container URL only within Purview to target that container for various Purview features. A separate Container Redirect URL is the clickable link for end users with access to open the container in the Loop app. The Container Redirect URL is
+rolling out
+and may not yet be available in the SharePoint admin center. For more information on using the Container Redirect URL, see
+Grant access to containers
 .
 Searching the Audit Logs
 Loop application IDs:

```

---

### 10. Microsoft Copilot Studio documentation

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

### 11. SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/advanced-management
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -88,7 +88,7 @@ Initiate site access reviews
 : Initiate site access reviews to delegate the process of reviewing DAG reports to site owners of overshared sites.
 Manage permissions and access
-SAM provides layered controls to detect oversharing, delegate remediation, and enforce leastâprivilege access across SharePoint and OneDrive.
+SAM provides layered controls to manage permissions and access, and enforce leastâprivilege access across SharePoint and OneDrive.
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
-by purchasing a standalone Sh
```

---

### 12. Data access governance reports

**URL:** https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.14: Control 1.14: Item-Level Permission Scanning
  - File: `controls/pillar-1-readiness/1.14-item-level-permission-scanning.md`
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

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

### 13. Agent insights report in SharePoint

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

### 14. SAM Content Management Assessment

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

### 15. SharePoint site lifecycle management

**URL:** https://learn.microsoft.com/en-us/sharepoint/site-lifecycle-management
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -27,28 +27,8 @@ help you improve site governance by automating the process of detecting inactive sites and notifying site owners by email. Site owners can then review and confirm whether their sites are still active.
 You can configure an inactive sites policy in the SharePoint admin center. This article describes how to set up an inactive site policy with notifications and enforcement actions.
 What do you need to create an inactive site policy?
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
 How do inactive site policies work?
 Scope of inactive site policies

```

---

### 16. Restricted Content Discovery

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

### 17. SharePoint Admin Agent (Content Governance Agent)

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

### 1. Microsoft Agent 365 registry sync
**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry
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

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*