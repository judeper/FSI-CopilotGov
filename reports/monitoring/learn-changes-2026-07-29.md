# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-29
**Run Time:** 2026-07-29T11:54:07.501356+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | audit-log-activities | HIGH | 3.1, 1.15 | Update portal-walkthrough |
| 2 | cowork-manage-plugins | HIGH | 4.15 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -461,6 +461,9 @@ Deleted data export configuration
 DeletedDataExportConfig
 A data export configuration was deleted.
+Deleted device connector
+DeletedDeviceConnector
+A device connector under an EHR connector was deleted.
 Deleted EHR instance
 DeletedEhrInstance
 An EHR integration instance was removed.
@@ -485,9 +488,18 @@ Deprovisioned product
 DeprovisionedProduct
 A product was deprovisioned from an environment.
+Installed device connector
+InstalledDeviceConnector
+A device connector was installed or upgraded under an EHR connector from a published package.
+Installed device connector from package
+InstalledDeviceConnectorFromPackage
+A device connector was installed or upgraded under an EHR connector from a sideloaded device package.
 Listed billing plans
 ListedBillingPlans
 Billing plans were listed.
+Listed device connectors
+ListedDeviceConnectors
+Device connectors installed under an EHR connector were listed.
 Listed EHR instances
 ListedEhrInstances
 EHR instances were listed.
@@ -518,12 +530,18 @@ Removed group member
 RemovedGroupMember
 A user was removed from a group.
+Set device connector state
+SetDeviceConnectorState
+A device connector under an EHR connector was enabled or disabled.
 Updated billing plan
 UpdatedBillingPlan
 Billing plan properties were modified.
 Updated data export configuration
 UpdatedDataExportConfig
 A data export configuration was modified.
+Updated device connector configuration
+UpdatedDeviceConnectorConfiguration
+The configuration of a device connector under an EHR connector was updated.
 Updated EHR connector
 UpdatedEhrConnector
 An EHR connector was modified.
@@ -545,12 +563,18 @@ Updated setting
 UpdatedSetting
 A configuration setting was changed.
+Verified device connector package
+VerifiedDeviceConnectorPackage
+A sideloaded device package was verified against an EHR connector without being installed.
 Viewed billing plan
 ViewedBillingPlan
 Billing plan details were viewed.
 Viewed data export co
```

---

### 2. Manage Copilot Cowork plugins

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
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
--- +++ @@ -168,7 +168,6 @@  "$schema": "https://developer.microsoft.com/en/json-schemas/teams/vDevPreview/MicrosoftTeams.schema.json",
  "manifestVersion": "devPreview",
  "version": "1.0.0",
- "packageName": "com.cowork.plugin.contoso",
  "name": {
  "short": "Contoso Analytics",
  "full": "Contoso Analytics"
@@ -188,6 +187,9 @@  "toolSource": {
  "remoteMcpServer": {
  "mcpServerUrl": "https://api.contoso.com/mcp",
+ "mcpToolDescription": {
+ "file": "./tools/contoso.json"
+ },
  "authorization": {
  "type": "OAuthPluginVault",
  "referenceId": "Y29udG9zby1tY3Atc2VydmVyLWF1dGg="
@@ -212,17 +214,44 @@ For the full list of validation rules, see
 Validation rules
 in the plugin development guide.
-Sideloaded plugins
-For testing purposes, users with appropriate permissions can sideload plugin packages through
+Testing as the plugin author
+As the plugin author, test the package yourself first, before you distribute it more widely. You can install your own package directly in Cowork without going through the Microsoft 365 admin center:
+In Cowork, open the
+Customize
+page and select the
+Plugins
+tab.
+Select
+Add plugin
+and choose your
+.zip
+package.
+When the
+Share
+dialog opens, choose
+Only you
+to keep the plugin private to your account while you test.
+This gives you the fastest loop to confirm that your skills, connectors, and tool calls work end to end before you roll the plugin out to other users, groups, or your whole tenant. For details, see
+Upload a plugin package
+.
+Testing in your tenant
+Before you publish a plugin to the Microsoft 365 App Store, you can distribute it within your own tenant to test it with a controlled audience. Admins upload the plugin package through
 M365 admin center
 >
-Manage Apps
+Manage apps
 >
 Upload custom app
-. Sideloaded plugins bypass store validation, so use this option only for development and testing. Control who can sideload apps by using your existing
+, then choose who the package is available to:
+Specific u
```

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
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*