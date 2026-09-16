# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-16
**Run Time:** 2026-09-16T14:27:51.247466+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| MEDIUM Changes | 2 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | CRITICAL | 4.12 | Update portal-walkthrough |
| 2 | ...t.com/en-us/microsoft-copilot-studio/ | MEDIUM | None | Review optional |
| 3 | restricted-content-discovery | MEDIUM | 2.5, 1.2, 1.7, 1.13, 1.3, 1.4 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. What's new in Microsoft Purview

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
--- +++ @@ -38,11 +38,61 @@ Roadmap
 for data security and risk and compliance solutions.
 August 2026
+Data Governance
+Updated
+:
+Data Quality capability
+requires the Microsoft Purview account and its data sources to be in the same Azure region.
 Data Loss Prevention
 In preview
 :
 Use data loss prevention policies for non-Microsoft connected apps
 . Create DLP policies that protect sensitive data at rest in non-Microsoft connected applications, such as Box and Google Workspace. These policies use the existing Microsoft Defender for Cloud Apps connectors and support the same classification engine available for Microsoft 365 locations.
+Updated
+: The
+Endpoint DLP capability comparison
+now clarifies that policies for access by apps not included in a restricted apps list or restricted app group are supported on Windows but not on macOS.
+Updated
+: If an Exchange DLP policy uses sensitivity labels as a condition and policy tips while mandatory labeling is enabled, selecting a label from the mandatory-labeling prompt
+doesn't reevaluate the policy tip
+. The configured DLP action is still enforced.
+Updated
+: In cross-tenant Microsoft Teams chats and channels,
+DLP policy enforcement follows the tenant that initiated the conversation
+. A user's home-tenant DLP policies don't automatically apply when another tenant hosts the chat or thread.
+In preview
+: Prepare Endpoint DLP for
+permission changes in macOS 27
+. Deploy client version 101.26072 or later, configure protection modes, monitor permission status, and notify users if they disable the required
+Device Control and Data Access
+permission.
+Updated
+: Guidance for
+DLP policies in Microsoft Edge for Business
+now explains policy sync status, where to investigate managed and unmanaged app activity, and coverage limitations caused by duplicate app catalog entries, encoded traffic, dynamic endpoints, and shared consumer and enterprise URLs.
+Data lifecycle management
+Updated
+: When you remove the last h
```

---

### 2. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -67,7 +67,7 @@ Microsoft Copilot license
 . Restricted Content Discovery is intended for Microsoft Copilot deployment and governance scenarios.
 Review your organization's existing categories, and if necessary, add categories. See
-Catalog mangement
+Catalog management
 .
 Enable Restricted Content Discovery for a site
 You can enable Restricted Content Discovery from the SharePoint admin center or by using PowerShell.
@@ -94,11 +94,6 @@ Remove Restricted Content Discovery from a site
 To disable Restricted Content Discovery for a site, open PowerShell as an administrator and run the following command:
 Set-SPOSite -Identity <site-url> -RestrictContentOrgWideSearch $false
-Enable or disable Restricted Content Discovery for multiple sites
-You can enable Restricted Content Discovery for multiple sites by using groups in catalog management.
-See
-Use catalog groups with Restricted Content Discovery
-.
 Delegate management to site administrators
 By default, only SharePoint administrators can manage Restricted Content Discovery.
 If you want site administrators to manage the setting for their own sites, enable delegation by using the following PowerShell command:

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft Copilot Studio documentation
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Classification:** MEDIUM (General content update)

---

### 2. Restricted Content Discovery
**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*