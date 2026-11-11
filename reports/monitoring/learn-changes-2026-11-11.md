# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-11
**Run Time:** 2026-11-11T17:33:39.456062+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| HIGH Changes | 1 |
| Redirects | 32 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | ...-based-billing-manage-copilot-credits | HIGH | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 3 | prerequisites | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (Policy language)

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
--- +++ @@ -57,7 +57,9 @@ don't
 have the Microsoft 365 Copilot add-on license and
 don't
-have access to Copilot in Word, Excel, PowerPoint, and OneNote.
+have access to Copilot in Word, Excel, PowerPoint, and OneNote. Some features are subject to
+fair use limits
+.
 For more information, see
 Copilot Chat (Basic) license and experience
 .
@@ -65,7 +67,9 @@ don't
 have the Microsoft 365 Copilot add-on license but have
 standard access
-to Copilot in Word, Excel, PowerPoint, and OneNote.
+to Copilot in Word, Excel, PowerPoint, and OneNote. Some features are subject to
+fair use limits
+.
 For more information, see
 Microsoft 365 Copilot (Basic) license and experience
 .
@@ -131,7 +135,9 @@ Microsoft 365 Copilot (Premium) license and experience
 Usage-based billing capabilities
 Copilot Chat (Basic)
-is the standalone baseline experience included with eligible Microsoft 365 licenses. It provides a secure, enterprise-ready AI chat that primarily uses web data and has limited use of organizational content. Copilot Chat can use organizational content, but you must explicitly provide that content with your prompt.
+is the standalone baseline experience included with eligible Microsoft 365 licenses. It provides a secure, enterprise-ready AI chat that primarily uses web data and has limited use of organizational content. Copilot Chat can use organizational content, but you must explicitly provide that content with your prompt. Some features are subject to
+fair use limits
+.
 You can access Copilot Chat (Basic) through:
 copilot.cloud.microsoft
 Microsoft Copilot app (web, desktop, mobile)
@@ -165,7 +171,9 @@ Microsoft 365 Copilot (Basic)
 refers to users without the Copilot add-on license, but who still have
 standard access
-to Copilot capabilities inside apps (for example, Word or Excel). These experiences are more limited and might not include full chat integration or priority access. Standard access is subject to service capacity and might vary throughout the day.
+t
```

---

### 2. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.15: Control 4.15: Copilot Cowork Governance
  - File: `controls/pillar-4-operations/4.15-copilot-cowork-governance.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 4.8: Control 4.8: Cost Allocation and License Optimization
  - File: `controls/pillar-4-operations/4.8-cost-allocation.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.9/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.9/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.8/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.8/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.8/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.8/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -113,6 +113,47 @@ Select
 Next
 .
+Model templates
+Model templates are reusable sets of platforms and models that can be applied to spending policies with Cowork enabled.
+You can associate a model template with a spending policy to control which models Cowork can use for the users or groups covered by that policy.
+Note
+Model templates are currently available only for
+Copilot Cowork
+. The
+Model templates
+step appears only when you select
+Cowork
+in a spending policy.
+To associate a model template while creating a spending policy:
+Select the models Cowork can use.
+Select the model families the agents and services in this policy can consume credits against.
+In
+Model templates
+, select from one of the following options:
+Apply model selection automatically
+to allow Microsoft to pick the best available model for each request.
+Customize model selection
+to apply a reusable model template or create a new one to use here and in future spending policies.
+If you choose
+Customize model selection
+, select an existing template or select
++ Create new model template
+.
+When creating a model template:
+Enter a name for the template.
+Select the model providers and models to include in the template. You must select at least two models.
+Save the model template.
+Select
+Next
+.
+To create and manage model templates, go to
+Cost Management > Configuration
+tab. For more information, see
+Configure model templates
+.
+To understand more about model template considerations, see
+Model template considerations
+.
 Select billing method
 By default, the field selects the billing method tied to the default spending policy.
 If you're a Global administrator or a Billing administrator, you can override this selection and select how this policy should be billed. This feature enables you to do departmental billing and vary billing methods for each group, department, or set of users.

```

---

## HIGH: Control Review Recommended

### 1. Agent capabilities and licensing models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites#agent-capabilities-and-licensing-models
**Section:** Copilot Extensibility
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -54,7 +54,7 @@ By adding
 Teams message extensions
 and
-Copilot Studio actions
+Copilot Studio agents
 .
 By extending the knowledge in Copilot with
 Microsoft 365 Copilot connectors
@@ -71,16 +71,16 @@ Work IQ Dev Tools requirements
 Work IQ Dev Tools
 is a preview pro-code route for supported declarative-agent and plugin-package scenarios. Before you install it, confirm:
-Node.js 24 or later. The supported installer can install Node.js when required.
+Node.js 24.15 or later and npm on your
+PATH
+for CLI and installation-script execution. The installer doesn't install Node.js. These aren't required just to begin conversational or file-based authoring.
 PowerShell 7 or later on Windows.
 A Microsoft 365 account with access to Copilot.
 An Azure subscription when you provision agents.
 A development or test tenant that permits the required custom-app installation, sharing, or catalog actions.
-The default installer installs the WIQD CLI, its Visual Studio Code extension, and the
-wiqd:wiqd
-Copilot CLI agent. After installation, sign in interactively for local development and run
+The installation script installs the WIQD CLI, its Visual Studio Code extension, and the public WIQD coding-assistant plugin for detected supported hosts unless you skip those integrations. It doesn't install the host. You can instead install the coding-assistant plugin from its marketplace, but that doesn't install the WIQD CLI. After installation, start a new host session. Sign in interactively before tenant operations and run
 wiqd doctor
-to verify the environment. See
+to verify the CLI environment. See
 Install Work IQ Dev Tools
 and
 Work IQ Dev Tools authentication
@@ -121,8 +121,8 @@ Your Power Platform admin or Dynamics 365 admin must
 enable Generative AI features
 in Power Platform admin center.
-Your Microsoft 365 tenant admin must
-deploy the Copilot Studio app in the Microsoft 365 admin center
+For requirements to make your agent available in Teams and Microsoft 
```

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/copilot/plan/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access | https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/copilot/plan/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy | https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access | https://learn.microsoft.com/en-us/copilot/implement/copilot-ai-provider-user-sec-group-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences | https://learn.microsoft.com/en-us/copilot/implement/discovery-setting-ai-experiences |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits | https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide | https://learn.microsoft.com/en-us/copilot/manage/copilot-tuning-admin-guide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*