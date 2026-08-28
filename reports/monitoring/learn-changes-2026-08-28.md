# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-28
**Run Time:** 2026-08-28T21:01:41.146370+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| HIGH Changes | 1 |
| MEDIUM Changes | 1 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4 | Update portal-walkthrough |
| 2 | whats-new | HIGH | 4.12 | Update portal-walkthrough |
| 3 | dlp-learn-about-dlp | HIGH | 3.10 | Update portal-walkthrough |
| 4 | dlp-policy-reference | HIGH | None | Review and update |
| 5 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 6 | whats-new | HIGH | 4.15 | Update portal-walkthrough |
| 7 | cowork-faq | CRITICAL | None | Monitor |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -23,217 +23,375 @@ Feedback
 Summarize this article for me
 Note
-Microsoft has onboarded OpenAI as a Microsoft subprocessor. For more information, see
-OpenAI as a subprocessor in Microsoft Online Services
-.
-Microsoft has onboarded Anthropic as a Microsoft subprocessor. For more information, see
+Microsoft Copilot is available in many regions worldwide. However, it might not be accessible in certain markets. Some organizations might gain access through an account support escalation process, but access is subject to approval. For more information, see
+International availability
+.
+Microsoft Copilot Chat and Microsoft Copilot responses and experiences differ by data grounding, integration depth, and licensing:
+However, all experiences are powered by:
+Large language models (LLMs)
+for natural language understanding and generation
+Grounding in web
+and/or
+organizational data
+(
+Microsoft Graph
+and
+Work IQ
+)
+Access scoped by user permissions (security and compliance enforced)
+Note
+Anthropic subprocessors are available only in applicable Microsoft 365 licensed experiences and aren't available to all users by default. Anthropic operates with
+Microsoft Enterprise data protections
+. For more information, see
 Anthropic as a subprocessor for Microsoft Online Services
 .
-Microsoft Copilot is an AI-powered tool that helps with your work tasks
-.
-Users enter a prompt in Copilot and Copilot responds with AI-generated information. The responses are in real-time and can include internet-based content and work content that users have permission to access.
-Users get content relevant to their work tasks, and in the context of the Microsoft 365 app they're using.
-The following video provides an overview of Microsoft Copilot. It's 1 minute and 49 seconds long.
-Using Microsoft Copilot
-Say, for example, you're an operations manager and are working with human resources to update job descriptions. By providing Copilot the basic job requirements, you can as
```

---

### 2. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -38,6 +38,11 @@ Roadmap
 for data security and risk and compliance solutions.
 August 2026
+Data Loss Prevention
+In preview
+:
+Use data loss prevention policies for non-Microsoft connected apps
+. Create DLP policies that protect sensitive data at rest in non-Microsoft connected applications, such as Box and Google Workspace. These policies use the existing Microsoft Defender for Cloud Apps connectors and support the same classification engine available for Microsoft 365 locations.
 Sensitivity labels
 New
 : Before enforcing an auto-labeling policy, run it in
@@ -49,6 +54,10 @@ Insights
 tab
 in the policy details panel provides an at-a-glance view of an auto-labeling policy's performance. The information shown varies depending on whether the policy is running in simulation or enforcement mode, helping you understand how it identifies or labels content.
+In preview
+:
+Sensitivity label policies for non-Microsoft connected apps
+. Create auto-labeling policies that protect sensitive data at rest in non-Microsoft connected apps, including Box and Google Workspace. These policies use the existing Microsoft Defender for Cloud Apps connectors and support the same classification engine available for Microsoft 365 locations.
 July 2026
 Data Governance
 Updated

```

---

### 3. Learn about DLP

**URL:** https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 3.10: Control 3.10: SEC Reg S-P -- Privacy of Consumer Financial Information
  - File: `controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/3.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.10/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -46,14 +46,15 @@ Use Network Data Security to help prevent sharing sensitive information with unmanaged AI (preview)
 Enterprise applications and devices
 DLP monitors and protects against oversharing in enterprise apps and on devices. It targets Microsoft 365 locations, like Exchange and SharePoint, and locations you add, like on-premises file shares, endpoint devices, and non-Microsoft cloud apps. These locations and sources include:
-Microsoft 365 services, like Exchange, SharePoint, OneDrive accounts, and Teams chat and channel messages
-Office applications, such as Word, Excel, and PowerPoint
-Devices running Windows 10, Windows 11, and the three most recent versions of macOS
-Non-Microsoft cloud apps
-On-premises file shares and on-premises SharePoint
-Microsoft Fabric and Power BI workspaces
-Microsoft 365 Copilot and Copilot chat (preview)
-Managed cloud apps
+Microsoft 365 services, like Exchange, SharePoint, OneDrive accounts, and Teams chat and channel messages.
+Office applications, such as Word, Excel, and PowerPoint.
+Devices running Windows 10, Windows 11, and the three most recent versions of macOS.
+Non-Microsoft cloud apps.
+Non-Microsoft connected apps (currently in preview), including Box, Dropbox, Google Workspace, and Salesforce.
+On-premises file shares and on-premises SharePoint.
+Microsoft Fabric and Power BI workspaces.
+Microsoft 365 Copilot and Copilot chat (preview).
+Managed cloud apps.
 Create DLP policies for
 Enterprise applications & devices
 to cover these locations.

```

---

### 4. Audit log activities

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
--- +++ @@ -2815,7 +2815,9 @@ Microsoft Purview permission activities
 The following table lists Microsoft Purview administration activities that the Microsoft 365 audit log records when an administrator manages role-based access control (RBAC) role groups and user assignments. For more information, see
 Permissions in the Microsoft Purview portal
-.
+. See
+Office 365 Management Activity API schema
+for the audit log schema.
 Friendly name
 Operation
 Description

```

---

### 5. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new
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
--- +++ @@ -25,7 +25,18 @@ This article lists recent features, improvements, and changes in Microsoft 365 Copilot Cowork. Get a full guide to Cowork's capabilities in
 Use Cowork
 .
-July 2026
+August 2026
+Enhancements
+Feature
+Description
+Learn more
+Workspace file input for plugin tools
+Plugin connector tools can now accept files from your session as input. Plugin authors declare a tool parameter with
+contentEncoding: base64
+, and Cowork resolves the workspace file to content before calling the toolâso a tool can convert a document, analyze an image, or attach a file to another system.
+Accept files from the Cowork workspace
+Local browser use
+This feature moved from Frontier to general availability to all Microsoft 365 Copilot tenants. Cowork can complete web tasks for you in Microsoft Edge on your device, using your existing sign-ins and your organization's policies. Requires that Edge is installed.
 New features
 Feature
 Description

```

---

## HIGH: Control Review Recommended

### 1. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -931,11 +931,17 @@ Workspaces
 data-in-use
 No
-Third-party apps
-None
-No
-No
-No
+Non-Microsoft connected apps (preview)
+No
+Cloud app instance
+data-at-rest
+-
+Use DLP and sensitivity label policies for non-Microsoft connected apps
+- Only available in the
+Custom
+policy template
+- Set up a
+Microsoft Defender for Cloud Apps connector
 Microsoft 365 Copilot (preview)
 No
 Account or Distribution group
@@ -1795,9 +1801,7 @@ patent
 , etc.
 Document name matches patterns:
-Detects documents where the file name matches specific patterns. The evaluation considers the entire path of the document, not just the documentâs name. The pattern is checked as a string match, meaning it can match any part of the document path. To define the patterns, use wild cards. For information on regex patterns, see the Regular Expression documentation
-here
-.
+Detects documents where the file name matches specific patterns. The evaluation considers the entire path of the document, not just the documentâs name. The pattern is checked as a string match, meaning it can match any part of the document path. To define the patterns, use wild cards.
 Note
 Due to potential performance issues, this condition will gradually be phased out from Purview Endpoint DLP. We recommend using the 'Document name contains words or phrases' condition instead.
 Document or attachment is password protected:

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Cowork FAQ
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Classification:** CRITICAL (Deprecation notice)

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