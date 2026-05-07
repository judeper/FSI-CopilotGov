# Microsoft Learn Documentation Changes

**Run Date:** 2026-05-07
**Run Time:** 2026-05-07T11:42:39.387805+00:00
**Total URLs Checked:** 114

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 14 |
| MEDIUM Changes | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4 | Review and update |
| 2 | manage-public-web-access | HIGH | None | Review and update |
| 3 | microsoft-365-copilot-privacy | HIGH | 3.8a, 3.10, 3.8, 1.4, 1.10 | Review and update |
| 4 | microsoft-365-copilot-usage | HIGH | None | Review and update |
| 5 | release-notes | CRITICAL | None | Monitor |
| 6 | whats-new | MEDIUM | None | Review optional |
| 7 | ...ilot-foundational-deployment-guidance | MEDIUM | 1.2 | Review optional |
| 8 | ...data-foundation-microsoft-365-copilot | HIGH | 1.2, 1.7 | Review and update |
| 9 | dlp-policy-reference | HIGH | None | Review and update |
| 10 | encryption-sensitivity-labels | HIGH | None | Review and update |
| 11 | audit-log-activities | HIGH | 1.15 | Review and update |
| 12 | .../microsoft-365/copilot/extensibility/ | HIGH | 1.13, 2.14 | Review and update |
| 13 | manage-copilot-agents-integrated-apps | HIGH | 1.13, 4.1, 4.13, 2.14, 2.13 | Review and update |
| 14 | copilot-tuning-admin-guide | CRITICAL | 1.16 | Monitor |
| 15 | m365-agents-admin-guide | HIGH | None | Review and update |
| 16 | data-connectors-reference | HIGH | None | Review and update |
| 17 | content-management-assessment | HIGH | 1.7 | Review and update |
| 18 | site-lifecycle-management | HIGH | 1.7 | Review and update |

---

## HIGH: Control Review Recommended

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

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

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
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

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 3.10: Control 3.10: SEC Reg S-P -- Privacy of Consumer Financial Information
  - File: `controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md`
- Control 3.8: Control 3.8: Model Risk Management Alignment (SR 26-2 / OCC Bulletin 2026-13, applying SR 11-7 / OCC 2011-12 principles to generative AI)
  - File: `controls/pillar-3-compliance/3.8-model-risk-management.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`

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
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -33,7 +33,7 @@ Go to the
 Microsoft 365 admin center
 .
-In the navigation menu, selectâ¯
+In the navigation menu, select
 Reports
 . If you don't see
 Reports
@@ -73,7 +73,7 @@ Microsoft Copilot Dashboard
 , where you can deliver insights to your IT leaders to explore Copilot readiness, adoption, and impact in Viva Insights.
 Active agent users
-shows the total number of unique Microsoft 365 Copilot users in your org who used agents built by your org (including admin-approved agents and agents created via agent builderâ¯and shared with users in your org).
+shows the total number of unique Microsoft 365 Copilot users in your org who used agents built by your org (including admin-approved agents and agents created via agent builder and shared with users in your org).
 Note
 Agent usage is available starting November 1, 2024, and is currently limited to agents built by your org. Usage of agents built by Microsoft and Microsoft Partners will be introduced in the coming months.
 Total prompts submitted
@@ -229,7 +229,7 @@ Welcome to Copilot in OneNote - Microsoft Support
 .
 Loop
-All Copilot in Loop features are automatically included in the Microsoft 365 Copilot usage report. Usage of any Copilot in Loop feature counts towards the Active users metric and is indicated in the per-user Last activity date (UTC). User views of Loop documents generated by the Facilitator feature in Teams meetings are included in active usage for the Loop app and all up Microsoft 365 Copilot usage, effective December 11, 2025.
+All Copilot in Loop features are automatically included in the Microsoft 365 Copilot usage report. Usage of any Copilot in Loop feature counts towards the Active users metric and is indicated in the per-user Last activity date (UTC). User views of Loop documents generated by the Facilitator feature in Teams meetings are included in active usage for the Loop app and all up Microsoft 365 Copilot usage, effective December 11, 2025.
 To learn more about Copil
```

---

### 5. Configure secure and governed Copilot foundation

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -25,7 +25,9 @@ Applies to: Microsoft 365 Copilot, Microsoft Purview, and SharePoint Advanced Management
 Microsoft 365 Copilot
 uses Work IQ to enhance responses to user prompts using data that the user already has permission to access. When your organization's data is well governed, current, and appropriately shared, Copilot can deliver accurate, relevant, and secure responses.
-This article guides you through preparing, securing, and managing Microsoft 365 Copilot using the process depicted in the following diagram:
+This article walks through the steps of preparing, securing, and managing Microsoft 365 Copilot using the process described in the
+Foundational deployment blueprint
+.
 By following these steps, you can help Copilot deliver accurate and relevant results while supporting your organization's security, compliance, and regulatory requirements.
 This guidance is intended for IT administrators and security administrators who are either preparing their organization for Microsoft 365 Copilot or making necessary adjustments to security and governance controls after Copilot is enabled.
 What this article helps you achieve
@@ -87,7 +89,7 @@ For sites you identify as high risk, use Microsoft Purview and SAM recommendations to remove excessive access, correct broken inheritance, and ensure accountable ownership.
 Review
 Microsoft Purview DSPM Data Risk Assessment
-recommendations for sites flagged as highârisk and take the following actions:
+recommendations for sites flagged as high-risk and take the following actions:
 Apply
 site sensitivity labels
 to reflect data sensitivity and restrict oversharing
@@ -110,7 +112,7 @@ .)
 Remove interim Copilot protections once access and permissions are remediated
 Step 2: Set up guardrails
-In this step, you establish secure defaults and durable guardrails with Microsoft Purview and SAM so new sites and content are protected at creationâand continuously enforce and optimize these controls over time.
+In th
```

---

### 6. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -19,31 +19,9 @@ Access to this page requires authorization. You can try
 changing directories
 .
+Data Loss Prevention policy reference
 Feedback
 Summarize this article for me
-title: "Data Loss Prevention policy reference"
-f1.keywords: CSH
-ms.author: chrfox
-author: chrfox
-manager: laurawi
-ms.date: [DATE]
-audience: Admin
-ms.topic: reference
-ms.service: purview
-ms.subservice: purview-data-loss-prevention
-search.appverid:
-SPO160
-MET150
-ms.assetid: 6501b5ef-6bf7-43df-b60d-f65781847d6c
-ms.collection:
-highpri
-purview-compliance
-SPO_Content
-recommendations: false
-description: "DLP policy component and configuration reference. This article provides a detailed anatomy of a DLP policy."
-ms.custom: seo-marvel-apr2021
-ai-usage: ai-assisted
-Data Loss Prevention policy reference
 Microsoft Purview Data Loss Prevention (DLP) policies have many components to configure. To create an effective policy, you need to understand what the purpose of each component is and how its configuration alters the behavior of the policy. This article provides a detailed anatomy of a DLP policy.
 Tip
 Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about

```

---

### 7. Encryption with sensitivity labels

**URL:** https://learn.microsoft.com/en-us/purview/encryption-sensitivity-labels
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -48,8 +48,8 @@ Understand how the encryption works
 Unless you're using
 S/MIME for Outlook
-, encryption that's applied by sensitivity labels to documents, emails, and meeting invites all use the Azure Rights Management service (Azure RMS) from Microsoft Purview Information Protection. This protection solution uses encryption, identity, and authorization policies. To learn more, see
-What is Azure Rights Management?
+, encryption that's applied by sensitivity labels to documents, emails, and meeting invites all use the Azure Rights Management service from Microsoft Purview Information Protection. This protection solution uses encryption, identity, and authorization policies. To learn more, see
+Learn about the Azure Rights Management encryption service
 .
 When you use this encryption solution, the
 super user
@@ -76,8 +76,8 @@ There are some Microsoft Entra configurations that can prevent authorized access to encrypted content. For example, cross-tenant access settings and Conditional Access policies. For more information, see
 Microsoft Entra configuration for encrypted content
 .
-Configure Exchange for Azure Rights Management
-Exchange doesn't have to be configured for Azure Rights Management before users can apply labels in Outlook to encrypt their emails. However, until Exchange is configured for Azure Rights Management, you don't get the full functionality of encryption with rights management.
+Configure Exchange for the Azure Rights Management service
+Exchange doesn't have to be configured for the Azure Rights Management service before users can apply labels in Outlook to encrypt their emails. However, until Exchange is configured for the Azure Rights Management service, you don't get the full functionality of encryption with rights management.
 For example, users can't view encrypted emails or encrypted meeting invites on mobile phones or with Outlook on the web, encrypted emails can't be indexed for search, and you can't configure Exchange Onl
```

---

### 8. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**What Changed:**
```diff
--- +++ @@ -993,6 +993,9 @@ Friendly name
 Operation
 Description
+Analyzed dataflow refresh logs
+AnalyzedDataflowRefreshLogs
+Analyzed dataflow refresh logs.
 Automatically bound user credentials to Git
 AutoBoundGitCredentials
 Automatically bound user credentials to Git.
@@ -1056,9 +1059,15 @@ Planning session upgraded
 PlanningSessionUpgraded
 Session type is upgraded in planning workload.
+Recover an artifact
+ArtifactRecovered
+A user recovered a previously soft-deleted artifact, such as a gateway or gateway cluster member, restoring it to active state.
 Retrieved artifact's Logical Id
 ArtifactLogicalIdRetrieved
 Retrieved artifact's Logical Id.
+Soft delete an artifact
+ArtifactSoftDeleted
+A user soft deleted an artifact, such as a gateway or gateway cluster member, marking it for deletion while allowing recovery within a retention period.
 Switched Git branch
 GitSwitchedBranch
 Switched Git branch for workspace.

```

---

### 9. Copilot extensibility overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`

**What Changed:**
```diff
--- +++ @@ -13,6 +13,7 @@ Agents overview
 Build a declarative agent
 Build a custom engine agent
+Evaluate agents
 Manage agents in the Microsoft 365 admin center
 Extend with plugins and connectors
 How-To Guide
@@ -23,6 +24,6 @@ Reference
 Microsoft 365 Agents Toolkit
 Microsoft 365 Agents SDK
+Work IQ APIs (preview)
 Microsoft 365 Copilot APIs
-Copilot Studio documentation
 Microsoft Agent 365
```

---

### 10. Manage plugins for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide
**Section:** Copilot Extensibility
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 4.1: Control 4.1: Copilot Admin Settings and Feature Management
  - File: `controls/pillar-4-operations/4.1-admin-settings-feature-management.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`

**What Changed:**
```diff
--- +++ @@ -53,11 +53,11 @@ Agent types you can manage
 You can manage several types of agents in Microsoft 365 Copilot, each serving different purposes:
 Published by your organization
-:â¯Built with predefined instructions and actions. These agents follow structured logic and are best for predictable, rule-based tasks. Before agents become available to users, these agents go through an admin approval and publishing process to ensure compliance and readiness.
+: Built with predefined instructions and actions. These agents follow structured logic and are best for predictable, rule-based tasks. Before agents become available to users, these agents go through an admin approval and publishing process to ensure compliance and readiness.
 Note
 Publishing agents to the organization is supported in Microsoft 365 Government Community Cloud High (GCCH) and Government Community Cloud Moderate (GCCM) environments.
 Shared by creator
-:â¯Shared agents are custom versions of Microsoft 365 Copilot that combine instructions, knowledge, and skills to perform specific tasks or scenarios. Creators can create and share these agents through multiple channels, such as Microsoft 365 Copilot Studio, Microsoft 365 Copilot Agent Builder, and more. Shared agents enhance the functionality of Copilot by adding search capabilities, custom actions, connectors, and APIs. For more information, see
+: Shared agents are custom versions of Microsoft 365 Copilot that combine instructions, knowledge, and skills to perform specific tasks or scenarios. Creators can create and share these agents through multiple channels, such as Microsoft 365 Copilot Studio, Microsoft 365 Copilot Agent Builder, and more. Shared agents enhance the functionality of Copilot by adding search capabilities, custom actions, connectors, and APIs. For more information, see
 Share agents with other users
 .
 As an admin, you can view shared agents on the
@@ -65,11 +65,11 @@ page in the Microsoft 365 admin center. You can see a 
```

---

### 11. M365 Agents admin guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -24,8 +24,8 @@ Summarize this article for me
 When you add
 Microsoft 365 Copilot
-to your qualifying Microsoft 365 for business subscription, you provide generative AI capabilities to your organization. With these capabilities, you help enhance your organizationâs productivity, improve accuracy, and provide personalized assistance.
-In addition to the generative AI capabilities provided by Microsoft 365 Copilot, you can extend your AI implementation to include agents. Agents allow you to customize your Copilot experience. You can connect agents to your organizationâs knowledge and data sources to help members of your organization answer questions, automate tasks, and run business processes. These AI-driven agents can perform various tasks, working alongside you to offer suggestions, automate repetitive tasks, and provide insights to help you and your organization make more informed decisions.
+to your qualifying Microsoft 365 for business subscription, you provide generative AI capabilities to your organization. With these capabilities, you help enhance your organization's productivity, improve accuracy, and provide personalized assistance.
+In addition to the generative AI capabilities provided by Microsoft 365 Copilot, you can extend your AI implementation to include agents. Agents allow you to customize your Copilot experience. You can connect agents to your organization's knowledge and data sources to help members of your organization answer questions, automate tasks, and run business processes. These AI-driven agents can perform various tasks, working alongside you to offer suggestions, automate repetitive tasks, and provide insights to help you and your organization make more informed decisions.
 This guide:
 Helps you determine which Copilot agent capabilities your organization needs
 Helps you understand where members of your organization view agents
@@ -39,7 +39,7 @@ .
 Identify your Copilot licensing scenario
 Organizations typically deploy
```

---

### 12. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -61,8 +61,8 @@ Cloud feature availability for US Government customers
 .
 Data connector prerequisites
-Each data connector has its own set of prerequisites. Prerequisites might include that you must have specific permissions on your Azure workspace, subscription, or policy. Or, you must meet other requirements for the partner data source you're connecting to.
-Prerequisites for each data connector are listed on the relevant data connector page in Microsoft Sentinel.
+Each data connector has its own set of prerequisites. Prerequisites might include having specific permissions on your Azure workspace, subscription, or policy. You might also need to meet other requirements for the partner data source you're connecting to.
+Prerequisites for each data connector are listed in this article and on the relevant data connector page in Microsoft Sentinel.
 Azure Monitor agent (AMA) based data connectors require an internet connection from the system where the agent is installed. Enable port 443 outbound to allow a connection between the system where the agent is installed and Microsoft Sentinel.
 Syslog and Common Event Format (CEF) connectors
 Log collection from many security appliances and devices are supported by the data connectors

```

---

### 13. SAM Content Management Assessment

**URL:** https://learn.microsoft.com/en-us/sharepoint/content-management-assessment
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -32,23 +32,23 @@ Ensure compliance and maintain data integrity
 Receive actionable recommendations for remediation
 Track progress over time with recurring assessments
-The assessment uses the SharePoint Advanced Management (SAM) toolkit, running a suite of essential reports to surface key findings and categorize sites that might require attention. It's intended to make content governance accessible and actionable, even for admins who might not have deep technical expertise.
+The assessment uses the SharePoint Advanced Management (SAM) toolkit, running a suite of essential reports to surface key findings and categorize sites that might require attention. It makes content governance accessible and actionable, even for admins who might not have deep technical expertise.
 Included reports
 Currently, the Content Management Assessment includes the following reports:
-Inactive sites
-- Identifies sites with no activity in the past 180 days
-Site ownership
-- Detects sites without owners or with only one owner
-Broken inheritance
-- Finds sites where permission inheritance has been broken
-Unrestricted internal sharing via EEEU (Everyone Except External Users)
-- Locates content shared with all internal users
+Inactive sites report
+: Identifies sites with no activity in the past 180 days.
+Site ownership report
+: Detects sites without owners or with only one owner.
+Broken inheritance report
+: Finds sites where permission inheritance is broken.
+Unrestricted internal sharing via EEEU (Everyone Except External Users) report
+: Locates content shared with all internal users.
 Unrestricted sharing via sharing links
-- Discovers content shared through overly permissive sharing links
+: Discovers content shared through overly permissive sharing links.
 Note
-Reports may take between 2 hour â 72 hours to run, depending on the size of the tenant.
-Reports run on all sites across the organization, and don't take any action without the admin's consent.
-Why Use Con
```

---

### 14. SharePoint site lifecycle management

**URL:** https://learn.microsoft.com/en-us/sharepoint/site-lifecycle-management
**Section:** SharePoint Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -22,11 +22,10 @@ Manage inactive sites by using inactive site policies
 Feedback
 Summarize this article for me
-The site lifecycle management features from
+Site lifecycle management capabilities in
 Microsoft SharePoint Advanced Management
-help you improve site governance by automating policy configuration in the
-SharePoint admin center
-. Inactive site policies, part of SharePoint's site lifecycle management features, help you automate this process. You can set up an inactive site policy to automatically detect inactive sites and notify site owners by email. Owners can then confirm if the site is still active.
+help you improve site governance by automating the process of detecting inactive sites and notifying site owners by email. Site owners can then review and confirm whether their sites are still active.
+You can configure an inactive sites policy in the SharePoint admin center. This article describes how to set up an inactive site policy with notifications and enforcement actions.
 What do you need to create an inactive site policy?
 License requirements
 Your organization needs to have the right

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot release notes
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Classification:** CRITICAL (Deprecation notice)

---

### 2. What's new in Microsoft Purview
**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Classification:** MEDIUM (General content update)

---

### 3. Secure and Govern Copilot blueprint
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance
**Classification:** MEDIUM (General content update)

---

### 4. Copilot Tuning admin guide
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide
**Classification:** CRITICAL (Deprecation notice)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*