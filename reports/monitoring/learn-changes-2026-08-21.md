# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-21
**Run Time:** 2026-08-21T10:19:39.353413+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| MEDIUM Changes | 3 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | MEDIUM | 1.9, 1.1, 2.15 | Update portal-walkthrough |
| 2 | whats-new | CRITICAL | 4.12 | Update portal-walkthrough |
| 3 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 4 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 5 | cowork-faq | MEDIUM | None | Review optional |
| 6 | agent-registry | HIGH | 2.14, 4.13, 4.14 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -151,7 +151,7 @@ ,
 *.cloud.microsoft
 and
-copilot.cloud.microsoft.com
+copilot.cloud.microsoft
 .
 Several Copilot integrations rely on WebSockets (WSS) to deliver a streamlined user experience. Some customer networks might not be configured to handle WSS connections properly, which can result in Copilot application failures. Typical network configurations that affect WSS include:
 The network perimeter blocks the WSS protocol

```

---

### 2. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -39,20 +39,71 @@ for data security and risk and compliance solutions.
 August 2026
 Sensitivity labels
-Before enforcing an auto-labeling policy, run it in simulation mode to identify which items it would label without making any changes. Review the match results and source distribution to determine whether the policy is ready to enforce. For more information, see
-Review simulation results for auto-labeling policies in Microsoft Purview
-.
+New
+: Before enforcing an auto-labeling policy, run it in
+simulation mode
+to identify which items it would label without making any changes. Review the match results and source distribution to determine whether the policy is ready to enforce.
+New
+:
 The
 Insights
-tab in the policy details panel provides an at-a-glance view of an auto-labeling policy's performance. The information shown varies depending on whether the policy is running in simulation or enforcement mode, helping you understand how it identifies or labels content. For more information, see
-Use the Insights tab to analyze auto-labeling policies in Microsoft Purview
-.
+tab
+in the policy details panel provides an at-a-glance view of an auto-labeling policy's performance. The information shown varies depending on whether the policy is running in simulation or enforcement mode, helping you understand how it identifies or labels content.
 July 2026
+Data Governance
+Updated
+: Microsoft Purview protection policies
+no longer support Azure SQL Database
+.
+New
+:
+Configure a manual business continuity and disaster recovery environment for Microsoft Purview Data Map
+. The guidance covers creating a secondary account, mirroring scans, validating the environment, and requesting account promotion during a regional outage.
 Data Loss Prevention
 In preview
 : Protect sensitive data in text and prompts by integrating with Microsoft Entra Global Secure Access (GSA). This integration enables organizations to intercept and inspect text and AI interactions at 
```

---

### 3. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new
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
--- +++ @@ -26,15 +26,6 @@ Use Cowork
 .
 July 2026
-Enhancements
-Feature
-Description
-Learn more
-Workspace file input for plugin tools
-Plugin connector tools can now accept files from your session as input. Plugin authors declare a tool parameter with
-contentEncoding: base64
-, and Cowork resolves the workspace file to content before calling the toolâso a tool can convert a document, analyze an image, or attach a file to another system.
-Accept files from the Cowork workspace
 New features
 Feature
 Description

```

---

### 4. Copilot Cowork available models

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -35,15 +35,19 @@ When to use Auto
 Use
 Auto
-for most work. Auto picks the model best suited to the task you describe, so you don't need to choose a model before every request.
+for most work. When you select
+Auto
+, Cowork picks the model based on the models enabled by your organization. You don't need to choose a model before every request.
 Available models
-The model picker can include the following models and model modes, depending on what your organization allows.
+The model picker can include the following models and model modes.
 Model
 Description
 Notes
 Auto
 For most day-to-day work.
-The default. Cowork picks the model best suited to the task you describe.
+The default. When you select
+Auto
+, Cowork picks the model based on the models enabled by your organization.
 GPT 5.5 (Frontier)
 Capable model for medium effort work.
 Hosted in Azure AI Foundry.

```

---

### 5. Agent registry in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

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
--- +++ @@ -426,7 +426,7 @@ Finish deployment
 .
 Note
-If your tentant uses unified agent and app management, all changes to org-wide tenant settings in Microsoft 365 admin center (MAC) are automatically synchronized in Teams admin center (TAC) and vice versa. For more information, see
+If your tenant uses unified agent and app management, all changes to org-wide tenant settings in Microsoft 365 admin center (MAC) are automatically synchronized in Teams admin center (TAC) and vice versa. For more information, see
 Unified agent and app management
 .
 Manage pinned agents

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot requirements
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Classification:** MEDIUM (General content update)

---

### 2. What's new in Copilot Cowork
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new
**Classification:** MEDIUM (General content update)

---

### 3. Copilot Cowork FAQ
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
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