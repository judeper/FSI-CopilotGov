# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-16
**Run Time:** 2026-10-16T14:24:26.954817+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| MEDIUM Changes | 1 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 2 | index | HIGH | 4.15 | Update portal-walkthrough |
| 3 | connected-platforms | MEDIUM | 1.13, 2.14, 4.13, 2.13 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -613,6 +613,10 @@ .
 For Exchange, simulation evaluates email that's sent and received during the run, so email results aren't consistent unless the same messages are sent and received again.
 Workflow for an auto-labeling policy:
+Important
+Before you edit an auto-labeling policy or run simulation again, export any available results that you need for later comparison. See
+Preserve results before editing or rerunning
+.
 Create and configure an auto-labeling policy.
 Run the policy in simulation mode, which can take 12 hours to complete. The completed simulation triggers an email notification that's sent to the user configured to receive
 activity alerts
@@ -1055,7 +1059,11 @@ ). For policies in simulation mode, select the
 Items to review
 tab to see which emails or documents matched the rules that you specified.
-You can modify your policy directly from this interface:
+Before selecting
+Edit policy
+,
+preserve simulation results you need for comparison
+. You can modify your policy directly from this interface:
 For a policy in the
 Off
 section, select the
@@ -1366,6 +1374,9 @@ for exclusions) with
 New-AutoSensitivityLabelPolicy
 . An adaptive scope supports up to 50,000 SharePoint sites per policy. This doesn't increase the portal limit; instead, it replaces static site enumeration with dynamic adaptive-scope membership.
+Before rerunning simulation,
+preserve simulation results you need for comparison
+.
 Before you run the commands in PowerShell, you must first
 connect to Security & Compliance PowerShell
 . To use PowerShell to start or rerun an auto-labeling policy simulation, connect by using

```

---

### 2. What is Microsoft Copilot Managed Runtime (preview)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index
**Section:** Copilot Cowork
**Classification:** HIGH (Portal references)

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
--- +++ @@ -5,14 +5,14 @@ These features are subject to
 supplemental terms of use
 , and are available before an official release so that customers can get early access and provide feedback.
-Copilot Managed Runtime hosts Microsoft 365 line-of-business applications that automatically inherit organizational governance, security, and compliance controls from the moment they're created. Whether you build an app through Copilot Cowork, Microsoft Copilot Studio, or the Copilot Managed Runtime SDK, the resulting app runs in a Microsoft-hosted environment, uses Microsoft Entra authentication, follows tenant governance policies, and is visible to admins in the Microsoft 365 admin center for monitoring and management.
+Copilot Managed Runtime hosts Microsoft 365 line-of-business applications that automatically inherit organizational governance, security, and compliance controls from the moment they're created. Whether you build an app through Copilot Cowork, Microsoft Copilot Studio, Copilot Code, or the Copilot Managed Runtime SDK, the resulting app runs in a Microsoft-hosted environment, uses Microsoft Entra authentication, follows tenant governance policies, and is visible to admins in the Microsoft 365 admin center for monitoring and management.
 Copilot Managed Runtime provides a unified experience for makers, developers, admins, and users. Organizations can accelerate app creation while maintaining centralized oversight, security, lifecycle management, and compliance controls.
 This article explains the entry points where you can
 create
 apps, the unified location where you can
 find and run
 apps already available to you, and further resources for Copilot Managed Runtime users, makers, developers, and administrators.
-Three ways to create an app
+Four ways to create an app
 Entry point
 Who it's for
 How it works
@@ -32,6 +32,11 @@ in the navigation. Describe the app in natural language or start from existing data; Copilot Studio proposes a plan, generates a draft, 
```

---

### 3. Connected platforms in Microsoft Agent 365 (manual sync)

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -60,12 +60,12 @@ Salesforce Agentforce
 Agentforce
 Yes
-Coming soon
+Yes
 Connect Salesforce Agentforce
 Databricks Genie
 Genie
 Yes
-Coming soon
+Yes
 Connect Databricks Genie
 Anthropic Claude
 Managed Agents

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Connected platforms in Microsoft Agent 365 (manual sync)
**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*