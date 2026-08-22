# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-22
**Run Time:** 2026-08-22T10:12:50.447362+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 9 |
| MEDIUM Changes | 1 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 2 | overview | HIGH | 4.16 | Update portal-walkthrough |
| 3 | get-started | HIGH | 4.16 | Update portal-walkthrough |
| 4 | admin-access-overview | HIGH | 4.16 | Update portal-walkthrough |
| 5 | manage-group-policy | MEDIUM | 4.16 | Update portal-walkthrough |
| 6 | use-microsoft-scout | HIGH | 4.16 | Update portal-walkthrough |
| 7 | faq | HIGH | 4.16 | Update portal-walkthrough |
| 8 | microsoft-scout-responsible-ai-overview | HIGH | 4.16 | Update portal-walkthrough |
| 9 | microsoft-scout-responsible-ai-faq | HIGH | 2.13, 4.16 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (UI element names)

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
--- +++ @@ -1376,9 +1376,6 @@ Edited Power BI semantic model options
 EditedSemanticModelOptions
 A user made a change to their semantic model options. This occurs when changes are made in the model options dialog.
-Executed a PostgreSQL database query
-QueryExecuted
-Generated when a user executes a SQL query against a Fabric Native PostgreSQL database. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact.
 Executed a tenant relocation
 TenantRelocationExecuted
 Executed tenant relocation.

```

---

### 2. Microsoft Scout (Frontier) overview

**URL:** https://learn.microsoft.com/microsoft-scout/overview
**Section:** Microsoft Scout (Frontier preview)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -35,7 +35,6 @@ Microsoft Product Terms
 .
 Microsoft Scout is a desktop AI application for Windows and macOS that takes action on your behalf. It reads and writes files, runs shell commands, controls a browser, queries your Microsoft 365 data, and works autonomously in the background. You describe what you need in a chat conversation, and Microsoft Scout carries out the work - with your approval before sensitive actions.
-Watch a quick overview video introducing Microsoft Scout:
 What can Microsoft Scout do?
 Microsoft Scout combines local and cloud capabilities in a single desktop application:
 Acts on your files
@@ -43,9 +42,11 @@ Runs commands
 : Executes shell commands, builds, tests, and scripts with a tiered permission system.
 Automates browsers
-: Navigates web pages, fills forms, and interacts with web applications by using Playwright.
+: Navigates web pages, fills forms, and interacts with web applications.
 Connects to Microsoft 365
-: Manages your email, calendar, Teams messages, OneDrive files, and meetings.
+: Works with Outlook mail and calendar, Teams meetings and messages, SharePoint Lists, and files in OneDrive, SharePoint, and Teams. For more information, see
+Work with Microsoft 365 in Microsoft Scout
+.
 Works autonomously
 : Runs in the background on schedules or triggers you define.
 Delegates work
@@ -62,6 +63,9 @@ Key features
 Local and cloud integration
 Microsoft Scout runs on your desktop with permissioned access to your approved file system and shell, while also connecting to your Microsoft 365 account. This means it can edit code in your workspace, run a build, send the results in an email, and schedule a follow-up meeting â all in one conversation.
+Microsoft Scout can also retrieve available Teams meeting transcripts, book meeting rooms, work with SharePoint Lists and Outlook inbox rules, and help manage file sharing and access. For more information, see
+Work with Microsoft 365 in Microsoft Scout
+.
 Granular permission
```

---

### 3. Get started with Microsoft Scout

**URL:** https://learn.microsoft.com/microsoft-scout/get-started
**Section:** Microsoft Scout (Frontier preview)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -69,11 +69,15 @@ .
 Authenticate with your organizational Microsoft 365 credentials.
 Grant the requested permissions when prompted.
+If your organization uses GitHub Enterprise Cloud, turn on
+Use a GitHub Enterprise host
+and enter your enterprise host (for example,
+your-org.ghe.com
+). Leave this off to sign in on github.com.
 Select
 Sign in to GitHub
-.
-Sign in with a GitHub account with a Business or Enterprise GitHub Copilot license.
-Microsoft Scout uses Microsoft Authentication Library (MSAL) with Web Account Manager (WAM) on Windows for secure authentication. Your organization's identity provider manages your credentials.
+and sign in with a GitHub account that has a Business or Enterprise GitHub Copilot license. Complete the sign-in in your browser when prompted.
+Microsoft Scout signs you in securely using your organization's Microsoft 365 identity. Your organization's identity provider manages your credentials.
 Configure your workspace
 After signing in, Microsoft Scout asks you to set a workspace directory. This folder is where Microsoft Scout reads and writes files.
 Select a workspace directory or accept the default location.
@@ -106,7 +110,7 @@ or select
 Send
 .
-Microsoft Scout begins working and shows progress in the conversation, including tool calls, permission prompts, created files, and final results.
+Microsoft Scout begins working and shows progress in the conversation, including actions, permission prompts, created files, and final results.
 Tip
 Be specific about what you want. Instead of "Help me with email," try "Draft a reply to Sarah's email about the budget review, thanking her and confirming I'll attend the Thursday meeting."
 Review default settings
@@ -151,15 +155,19 @@ Explore settings
 Open
 Settings
-to configure Microsoft Scout:
+to configure Microsoft Scout. Settings is a single, grouped window with a search box at the top, so you can find an option by typing its name. Key groups include:
 Appearance
 : Theme (l
```

---

### 4. Microsoft Scout admin access overview

**URL:** https://learn.microsoft.com/microsoft-scout/admin-access-overview
**Section:** Microsoft Scout (Frontier preview)
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -91,6 +91,66 @@ For more information, see:
 Setting up GitHub Copilot for your organization
 Granting access to GitHub Copilot for members of your organization
+Troubleshoot GitHub Copilot access
+Microsoft Scout uses the GitHub Copilot app. For a user to sign in and run a task, two GitHub-side conditions must both be true:
+The user has a GitHub Copilot
+Business
+or
+Enterprise
+seat assigned.
+Your organization or enterprise policy allows the GitHub Copilot app for that user.
+An assigned seat by itself isn't sufficient. If the policy that governs the Copilot app is turned off, a licensed user is still blocked.
+Important
+A user can have an active, assigned Copilot Business or Enterprise seat and still be blocked if the GitHub Copilot app policy (or, for app versions before 1.1, the Copilot CLI policy) is disabled. Check the policy before concluding it's a licensing problem.
+Symptoms and fixes
+Use the message the user sees in Microsoft Scout to identify the cause.
+What the user sees
+Likely cause
+Admin fix
+A message that GitHub Copilot access is required (for example, "GitHub Copilot access required" or "GitHub Copilot Business or Enterprise required"), or that the account "doesn't have a â¦ license"
+No Copilot Business or Enterprise seat is assigned, or the user signed in with a personal GitHub account that only has an individual plan
+Assign a Business or Enterprise seat to the user, and have the user sign in with the GitHub account that carries that seat.
+"You are not authorized to use this Copilot feature" (an HTTP 403), or the access message above even though a seat is assigned
+The organization or enterprise policy for the GitHub Copilot app (or
+Copilot in the CLI
+for app versions before 1.1) is disabled for the user
+Enable the policy at the enterprise and organization level. See
+Enable the GitHub Copilot app policy
+.
+Sign-in is blocked before any GitHub prompt appears
+A Microsoft Scout admin gate (Frontier access, or the Intune p
```

---

### 5. Manage admin controls in Intune for Microsoft Scout

**URL:** https://learn.microsoft.com/microsoft-scout/manage-group-policy
**Section:** Microsoft Scout (Frontier preview)
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -40,7 +40,7 @@ Available admin controls
 Administrators can use these policies to manage Microsoft Scout features and capabilities, including:
 Requiring approval for tool actions
-Blocking specific MCP servers
+Blocking specific tool servers
 Restricting permission types
 Disabling AI models or providers
 Disabling Heartbeat and Automations
@@ -57,10 +57,10 @@ PolicyVersion
 REG_DWORD
 Stores the policy schema version for diagnostics and future migrations.
-Disabled MCP servers
+Disabled tool servers
 DisabledServers
 REG_SZ
-Comma-separated list of MCP server keys to block, such as
+Comma-separated list of tool server keys to block, such as
 filesystem
 ,
 playwright
@@ -112,7 +112,7 @@ Blocked browser egress origins
 BrowserEgressBlockedOrigins
 REG_SZ
-Comma-separated list of HTTP or HTTPS origins that are blocked from Playwright browser traffic.
+Comma-separated list of HTTP or HTTPS origins that are blocked from browser automation traffic.
 Related content
 Admin access overview for Microsoft Scout
 Set up Microsoft Scout with Intune

```

---

### 6. Use Microsoft Scout

**URL:** https://learn.microsoft.com/microsoft-scout/use-microsoft-scout
**Section:** Microsoft Scout (Frontier preview)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -49,11 +49,35 @@ Send follow-up messages
 You can send additional messages while Microsoft Scout is still working. Messages are queued and processed in order. If your follow-up changes direction, Microsoft Scout adjusts its approach.
 Answer questions from Microsoft Scout
-When Microsoft Scout needs more information, it presents a set of choices. Select an option and confirm. If you don't want to answer, select
+When Microsoft Scout needs more information, it presents a set of choices. Select an option and confirm. When a question is open-ended, you can type your own answer instead of choosing a preset option. If you don't want to answer, select
 Skip
 - Microsoft Scout continues with what it knows.
+Shorten a long conversation
+Long conversations can reach the model's context limit. To free up room while keeping the important details, compact the conversation on demand. Microsoft Scout summarizes the earlier turns and continues from the shortened history, so you can keep working in the same conversation.
+Choose a model and reasoning effort
+Microsoft Scout lets you control which model runs and how much it reasons.
+Switch models per message
+: Use the model selector in the compose box to change the model for your next message, without starting a new conversation.
+Set a default reasoning effort
+: In
+Settings
+, choose the default reasoning effort Microsoft Scout uses. Higher effort takes more time but handles more complex tasks.
+Choose a context window size
+: Select how much conversation history the model keeps in context, up to a
+Max
+option for the largest supported window.
+Organize your chats
+The left navigation lists your conversations and automations. To keep them organized:
+Filter the list
+: Show all items, only chats, or only automations.
+Pin and reorder
+: Pin important conversations and drag them into the order you want.
+Open chat actions
+: Right-click a conversation to rename, pin, delete, or mark it as unread.
+Mark as unread
+: F
```

---

### 7. Microsoft Scout FAQ

**URL:** https://learn.microsoft.com/microsoft-scout/faq
**Section:** Microsoft Scout (Frontier preview)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -43,9 +43,9 @@ Run shell commands, builds, tests, and scripts on your machine.
 Explore codebases, apply patches, run linters, and debug failures using git, gh, curl, and PowerShell.
 Automate browser interactions - navigate pages, fill forms, take snapshots, and inspect network traffic.
-Search your workspace with fast pattern-matching tools (glob and ripgrep).
+Search your workspace with fast pattern-matching tools.
 Search the internet for real-time information.
-Read and manage your email, calendar, Teams chats, OneDrive files, and meetings.
+Read and manage your email, calendar, Teams chats and channels, OneDrive files, To Do tasks, and meetings.
 Query across Microsoft 365 services using WorkIQ for complex questions.
 Create and edit Word documents, Excel spreadsheets, PowerPoint presentations, and diagrams.
 Run autonomously in the background on a schedule (heartbeat mode).
@@ -56,7 +56,7 @@ What is Microsoft Scout?
 Is Microsoft Scout secure?
 Yes. Microsoft Scout operates within your Microsoft 365 security boundaries:
-Authentication uses MSAL (Microsoft Authentication Library) with WAM (Web Account Manager) on Windows.
+Authentication uses your organization's Microsoft 365 credentials on Windows.
 Microsoft Scout accesses only services and data your account is permitted to use.
 Shell commands are gated by a permission system that you control.
 You can mark sensitive paths to require explicit approval before access.
@@ -80,7 +80,7 @@ Yes (with three-tier permissions)
 Browser control
 No
-Yes (Playwright automation)
+Yes (browser automation)
 Autonomous modes
 No
 Yes (heartbeat and automations)
@@ -390,28 +390,28 @@ If Microsoft Scout loses connection to its backend, work in progress pauses. When the connection is restored, Microsoft Scout resumes automatically. Work done before the disconnection is preserved.
 Where are my files saved?
 Files that Microsoft Scout creates are saved to your workspace directory (the folder you configured during s
```

---

### 8. Responsible AI overview for Microsoft Scout

**URL:** https://learn.microsoft.com/microsoft-scout/microsoft-scout-responsible-ai-overview
**Section:** Microsoft Scout (Frontier preview)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -45,7 +45,7 @@ Shell command execution
 - Runs commands and scripts on your machine with a three-tier permission system (auto-approve, prompt, deny).
 Browser automation
-- Controls a browser using Playwright to navigate pages, fill forms, take snapshots, and inspect network traffic.
+- Controls a browser to navigate pages, fill forms, take snapshots, and inspect network traffic.
 Code and CLI
 - Explores codebases, applies patches, runs builds and tests, and debugs failures using git, gh, curl, and PowerShell.
 Microsoft 365 integration

```

---

### 9. Responsible AI FAQ for Microsoft Scout

**URL:** https://learn.microsoft.com/microsoft-scout/microsoft-scout-responsible-ai-faq
**Section:** Microsoft Scout (Frontier preview)
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 4.16: Control 4.16: Microsoft Scout Governance
  - File: `controls/pillar-4-operations/4.16-microsoft-scout-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -43,7 +43,7 @@ Run shell commands, builds, tests, and scripts by using a three-tier permission system (auto-approve, prompt, deny).
 Explore codebases, apply patches, run linters, and debug failures using git, gh, curl, and PowerShell.
 Automate browser interactions â navigate pages, fill forms, take snapshots, inspect console logs and network requests, and upload files.
-Search your workspace with fast pattern-matching tools (glob and ripgrep).
+Search your workspace with fast pattern-matching tools.
 Search the internet for real-time information.
 Launch specialized research agents for parallel investigations with detailed findings and citations.
 Read and manage your email, calendar, Teams chats, OneDrive files, and meetings.
@@ -102,7 +102,7 @@ How does Microsoft Scout handle my data?
 Microsoft Scout operates within the security and compliance boundaries of Microsoft 365 and your local machine, and (in certain cases) external AI services, based on your instructions, permissions, and configuration.
 Authentication and access controls
-: Microsoft Scout uses your existing Microsoft 365 credentials (MSAL with WAM on Windows) and operates with the same permissions and access controls that apply to your account. It accesses only services and data that your account is permitted to use.
+: Microsoft Scout uses your existing Microsoft 365 credentials and operates with the same permissions and access controls that apply to your account. It accesses only services and data that your account is permitted to use.
 Tenant isolation
 : Your Microsoft 365 data is isolated to your organization's tenant, subject to your organization's existing security, compliance and governance controls.
 External AI processing (GitHub Copilot)
@@ -114,7 +114,7 @@ Data subject rights
 : Access, deletion, rectification, and portability requests are supported in accordance with Microsoft's privacy standards.
 File storage and memory
-: Files that Microsoft Scout creates are stored in
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Manage admin controls in Intune for Microsoft Scout
**URL:** https://learn.microsoft.com/microsoft-scout/manage-group-policy
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