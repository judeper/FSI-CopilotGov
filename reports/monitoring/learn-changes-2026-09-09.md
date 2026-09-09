# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-09
**Run Time:** 2026-09-09T14:01:57.745375+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| HIGH Changes | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | HIGH | 2.15, 1.1, 1.9 | Update portal-walkthrough |
| 2 | audit-get-started | HIGH | None | Review and update |
| 3 | audit-log-activities | HIGH | 3.1, 2.2, 2.13, 1.15 | Update portal-walkthrough |
| 4 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | None | Review and update |
| 5 | whats-new | HIGH | 4.15 | Update portal-walkthrough |
| 6 | get-started | HIGH | None | Review and update |
| 7 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 8 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 9 | cowork-faq | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`

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
--- +++ @@ -42,7 +42,7 @@ accounts. You can add or sync users by using the
 onboarding wizard in the Microsoft 365 admin center
 .
-Microsoft Copilot supports only primary mailboxes that are hosted on Exchange Online.
+Microsoft Copilot supports primary mailboxes that are hosted on Exchange Online. It is also available on users' archive mailboxes and shared and delegate mailboxes that they have access to.
 Note
 Chat experiences in Word, Excel, and PowerPoint vary depending on your tenant configuration and license. Learn more in
 Microsoft Copilot overview
@@ -76,7 +76,7 @@ Try the new Outlook
 in their existing Outlook client.
 Important
-Microsoft Copilot is only supported on primary mailboxes that are hosted on Exchange Online. It isn't available on a user's archive mailbox, group mailboxes, or shared and delegate mailboxes that they have access to.
+Microsoft Copilot isn't available on group mailboxes.
 Microsoft Teams
 - Use the
 Microsoft Teams setup guide in the Microsoft 365 admin center
@@ -103,8 +103,7 @@ Customization
 |
 Policy Management
-.
-To learn more, see:
+. To learn more, see:
 Manage Loop workspaces in Syntex repository services
 Learn how to enable the Microsoft Loop app
 .

```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
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
--- +++ @@ -1302,7 +1302,7 @@ Operation
 Description
 Applied a PostgreSQL database schema
-PgSchemaApplied
+ApplyPostgreSQLDatabaseSchema
 Generated when a user applies (plans and executes) a PostgreSQL database schema through the custom PG schema service (pgschema-based ALM flow). The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
 Assign Warehouse Server Alias
 AssignWarehouseServerAlias
@@ -1320,7 +1320,7 @@ GitBranchedOut
 Branched out to a workspace in Git.
 Browsed PostgreSQL database objects
-PgSQLDbObjectExplorered
+PgSQLDbObjectExplorer
 Generated when a user browses PostgreSQL database schema objects through Object Explorer. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
 Cancelled a Digital Operations Ontology Agent conversation
 DigitalOperationsOntologyAgentConversationCancelled
@@ -1374,7 +1374,7 @@ ExportItemDefinitions
 Export multiple item definitions from a workspace.
 Exported a PostgreSQL database schema
-PgSchemaExported
+ExportPostgreSQLDatabaseSchema
 Generated when a user dumps a PostgreSQL database schema through the custom PG schema service (pgschema-based ALM flow). The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
 Get Items Sizes
 GetItemsSize
@@ -1398,7 +1398,7 @@ ImportedLifecyclePolicy
 Imported OneLake Lifecycle policy.
 Imported PostgreSQL sample data
-ImportedSampleData
+ImportSampleDataToPostgreSQLDatabase
 Generated when a user imports supported sample data into a Fabric Native PostgreSQL database. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
 Initialized connection to Git
 GitConnectionInitialized
@@ -1437,7 +1437,7 @@ ArtifactLogicalIdRetrieved
 Retrieved artifact's Logical Id.
 Retrieved PostgreSQL SQL audit policy
-SqlAuditPolicyRetrieved
+GetSqlAuditPolicyOnDatabase
 Generated when a user retrieves the SQ
```

---

### 3. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -25,6 +25,27 @@ This article lists recent features, improvements, and changes in Microsoft 365 Copilot Cowork. Get a full guide to Cowork's capabilities in
 Use Cowork
 .
+September 2026
+New features
+Feature
+Description
+Learn more
+App skill (Frontier)
+Create lightweight, interactive apps from a description without writing code. Refine your app in chat, open it, publish it, and share it with people in your organization.
+Build apps with the App skill
+Claude Fable 5.1 model
+Fable 5.1 is now available in the model selector as the most advanced model for ambitious work, replacing Fable 5.
+Choose a model for Cowork
+GPT 6 Astra model
+GPT 6 Astra is now available in the model selector as the latest model for tough problems.
+Choose a model for Cowork
+Plugins on the mobile app
+Plugins are discoverable and configurable on the mobile app. To find them, select the attach menu (
++
+) >
+Skills
+.
+Cowork common questions
 August 2026
 Enhancements
 Feature

```

---

### 4. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -104,10 +104,8 @@ Manage plugins in Microsoft 365 admin center
 .
 Manage models
-Cowork ships with several models: Claude Opus and Sonnet variants from Anthropic, Claude Fable 5 (Preview), the Sonnet+Opus Advisor pairing, GPT 5.5, and ChatGPT Images 2.0 for image generation. Claude Fable 5 (Preview) is off by default; turn it on in the
-Microsoft 365 admin center
-under Copilot settings if you want to make it available. Some models, such as Claude Fable 5, require data retention, which means a user's prompts and responses for that model are retained by the model provider. Learn about preview models, including their limitations, in
-Manage preview AI models in Microsoft Online Services
+Cowork ships with several models: Claude Fable, Opus and Sonnet variants from Anthropic, the Sonnet+Opus Advisor pairing, GPT 5.5, and ChatGPT Images 2.0 for image generation. For information on data retention, see
+Anthropic models in Microsoft Online Services
 .
 As an admin, you can turn off the Anthropic model family in the
 Microsoft 365 admin center

```

---

### 5. Copilot Cowork available models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -59,6 +59,10 @@ Balanced effort for common tasksâ.
 Provided by OpenAI as a subprocessor. More information:
 OpenAI as a subprocessor in Microsoft Online Services
+GPT 6 Astra
+Latest model for tough problems.
+Provided by OpenAI as a subprocessor. More information:
+OpenAI as a subprocessor in Microsoft Online Services
 Opus 5
 For complex, high stakes work.
 More information:
@@ -67,35 +71,19 @@ For everyday tasks and fast responses such as drafting, quick lookups, and day-to-day work.
 Use when you want a shorter response cycle for common tasks. More information:
 Anthropic subprocessor
-Claude Fable 5 (Preview)
-For your toughest, most demanding challenges.
-In preview and off by default. An admin must turn it on in the Microsoft 365 admin center under Copilot settings before it appears in your picker. Requires data retention. When you select Fable 5, the model provider retains your prompts and responses, and Cowork shows a banner while it's selected. More information:
-Data retention
-and
+Claude Fable 5.1
+Most advanced model for ambitious work.
+More information:
 Anthropic subprocessor
-1
-The models in your picker reflect what your organization makes available to you. State which populations the GPT 5.5 (Frontier) model is available to before publishing. If it's available only to Copilot Cowork Frontier program tenants, say so.
-Note
-Confirm the GPT 5.5 (Frontier) availability statement and the definition of the "(Frontier)" qualifier before this page is published.
+. For information on data retention, see
+Anthropic models in Microsoft Online Services
+.
 How model choice affects responses
 Changing the model can affect response speed, response depth, and output style. Some models are optimized for faster drafting, while others spend more time on reasoning and review.
 Cowork shows a model badge in the conversation so you can see which model produced a response.
 Data retention
-Some models, such as
-Claude Fable 5 (Preview)
-(off by default)
```

---

## HIGH: Control Review Recommended

### 1. Audit (Standard)

**URL:** https://learn.microsoft.com/en-us/purview/audit-get-started
**Section:** Audit and Retention
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -92,27 +92,28 @@ role group can only search and export the audit log. They can't enable or disable audit logging. This role group grants the
 View-Only Audit Logs
 role to the user.
-Step 3: Enable SearchQueryInitiated events
-You must explicitly enable two events (
+Step 3: Enable/Disable SearchQueryInitiatedExchange/SearchQueryInitiatedSharePoint events
 SearchQueryInitiatedExchange
-and
+must be enabled explicitly for logging when users perform searches in Exchange Online.
 SearchQueryInitiatedSharePoint
-) for logging when users perform searches in Exchange Online and SharePoint.
-To enable these two events to be audited for users, run the following cmdlet (for each user) in
+is by default enabled for logging when users perform searches in SharePoint.
+To enable Exchange Online and SharePoint events to be audited for users, run the following cmdlet (for each user) in
 Exchange Online PowerShell
 :
-Set-Mailbox <user> -AuditOwner @{Add="SearchQueryInitiated"}
+Set-Mailbox <user> -AuditOwner @{Add="SearchQueryInitiated"} // For Exchange Online
+
+Set-Mailbox <user> -AuditOwner @{Add="SharepointSearchQueryInitiated"} // For SharePoint. Enabled by default.
 In a multi-geo environment, you must run the
 Set-Mailbox
 command in the forest where the user's mailbox is located. To identify the user's mailbox location, run the following cmdlet:
 Get-Mailbox <user identity> | FL MailboxLocations
 If you previously ran the cmdlet to enable auditing of search queries in a forest that's different than the forest where the user's mailbox is located, remove the
-SearchQueryInitiated
+SearchQueryInitiated/SharepointSearchQueryInitiated
 value from the user's mailbox. To remove the value, run
-Set-Mailbox -AuditOwner @{Remove="SearchQueryInitiated"}
+Set-Mailbox -AuditOwner @{Remove="SearchQueryInitiated"} for Exchange Online and Set-Mailbox -AuditOwner @{Remove="SharepointSearchQueryInitiated"}
 . Then, add it to the user's mailbox in the forest where the user's mailb
```

---

### 2. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Section:** Copilot Cowork
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -45,6 +45,8 @@ : Drafts stakeholder communications such as status updates and announcements.
 Schedules prompts
 : Runs prompts on a schedule so recurring tasks happen automatically.
+Create apps (Frontier)
+: Use the App skill to build lightweight, interactive apps from a description. There's no coding required. You can refine the app in chat, open, publish, and share it with your stakeholders.
 Cowork shows each step in your session, so you can follow along as it works.
 Note
 Cowork is available for
@@ -90,7 +92,7 @@ .
 Skills
 Cowork uses specialized skills as it works. When Cowork loads a new skill during your session, the skill shows up in the side panel. Each skill corresponds to a specific type of task.
-Cowork has built-in skills, including Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, and Adaptive Cards. You can also create your own custom skills.
+Cowork has built-in skills, including Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, Adaptive Cards, and App (Frontier). You can also create your own custom skills.
 Learn more about each skill in
 Cowork skills
 .
@@ -103,6 +105,22 @@ Learn more about browsing, installing, and managing plugins in
 Use plugins with Cowork
 .
+Build apps with the App skill (Frontier)
+Describe the app or visualization you want, and Cowork invokes the built-in App skill to start building it. Use the App skill to:
+Prototype ideas quickly.
+Create interactive visuals from complex data.
+Build secure productivity tools for yourself or your team.
+Refine app features in Cowork.
+Share and deploy apps to support productivity and collaboration.
+Use enterprise data from documents, spreadsheets, and other sources to generate secure, functional apps.
+Important
+This is a preview feature provided under
+Microsoft Product Terms
+.
+
```

---

### 3. Get started with Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Section:** Copilot Cowork
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -22,7 +22,7 @@ Get started with Copilot Cowork
 Feedback
 Summarize this article for me
-Microsoft Copilot Cowork allows you to describe what you needâdraft an email, build a spreadsheet, schedule a meetingâand Cowork handles it. This article walks you through your first conversation, from sending a request to reviewing the result.
+Microsoft Copilot Cowork allows you to describe what you needâdraft an email, build a spreadsheet, schedule a meeting, build an appâand Cowork handles it. This article walks you through your first conversation, from sending a request to reviewing the result.
 Prerequisites
 Before you begin, make sure you have:
 Microsoft Copilot access
@@ -33,6 +33,8 @@ : Cowork is enabled in your Microsoft Copilot environment.
 Usage-based billing
 : Usage-based and Cowork billing has been enabled.
+Access to create apps
+: You must be part of the Frontier program to use the built-in App skill in Cowork.
 Cowork can optionally use Anthropic models as a subprocessor. Integration details can be found at
 Anthropic as a subprocessor for Microsoft Online Services
 .
@@ -116,12 +118,17 @@ Skip
 if you'd rather not answer.
 Review your results
-When Cowork finishes, any files it created appear in the side panel on the right. From there you can:
+When Cowork finishes, any files it creates appear in the side panel on the right. From there, you can:
 Download individual files to your device, or select
 Download All
 to download every file as a single zip archive.
 Preview files directly in the browser. Supported formats include PDF, Microsoft 365 documents (Word, Excel, PowerPoint), Markdown, code files, images, CSV, HTML, and email.
 Open files in OneDrive and directly in the online version of PowerPoint.
+When an app is ready, open it to verify the user experience, and then select
+Publish
+to make the latest version available to users. The App skill is available only to users in the Frontier program. For more information, see
+Build apps w
```

---

### 4. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -54,7 +54,7 @@ Inbox and calendar clean-up, project launches, or meeting preparation.
 Copilot Chat helps you think through your work, supports fast, single-step inputs, and generates output for you to act on. Cowork helps you get work done by completing complex, coordinated actions across your apps, files, and data.
 What skills does Cowork have?
-Cowork has built-in skills: Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, and Adaptive Cards. You can also create your own custom skills by placing a
+Cowork has built-in skills: Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, Adaptive Cards, and App (Frontier). The App skill lets you build lightweight, interactive apps in Cowork without writing code. You can also create your own custom skills by placing a
 SKILL.md
 file in a subfolder of your OneDrive
 /Documents/Cowork/skills/
@@ -105,11 +105,16 @@ Send your message. Cowork begins processing your request.
 Does Cowork work on mobile devices?
 Yes. You can access Cowork in the following ways:
-In the Microsoft Copilot mobile app for iPhone and Android
-In your browser at
+On the Microsoft Copilot mobile app for iPhone and Android
+Plugins are discoverable and configurable on the mobile app. To find them, select the attach menu (
++
+) >
+Skills
+. Plugins are also accessible in the Cowork mobile app if you set it up on your desktop.
+From your browser at
 m365.cloud.microsoft
 (desktop)
-In the Microsoft Copilot desktop app for Windows and Mac
+On the Microsoft Copilot desktop app for Windows and macOS
 What file types does Cowork support?
 You can attach a wide variety of files to your sessions. Cowork supports the following categories:
 Word
@@ -338,7 +343,7 @@ Auto
 and Cowork chooses the model that fits your task. To pick a specific model, select
 Auto
-in the 
```

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*