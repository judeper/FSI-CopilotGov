# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-15
**Run Time:** 2026-08-15T10:12:37.430168+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| MEDIUM Changes | 2 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | audit-log-activities | MEDIUM | 1.15, 2.13, 3.1 | Update portal-walkthrough |
| 2 | cowork-admin-governance | MEDIUM | 4.15 | Update portal-walkthrough |
| 3 | manage-federated-connectors | CRITICAL | 2.16 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
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
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -521,6 +521,9 @@ Listed role assignments
 ListedRoleAssignments
 Role assignments were listed.
+Listed role definitions
+ListedRoleDefinitions
+An administrator listed the available role definitions.
 Listed settings
 ListedSettings
 Configuration settings were listed.
@@ -599,6 +602,9 @@ Viewed role assignment
 ViewedRoleAssignment
 A role assignment was viewed.
+Viewed role definition
+ViewedRoleDefinition
+An administrator viewed a role definition.
 Viewed setting
 ViewedSetting
 A setting value was viewed.
@@ -1295,6 +1301,9 @@ Friendly name
 Operation
 Description
+Assign Warehouse Server Alias
+AssignWarehouseServerAlias
+A workspace administrator assigned a server alias to a Fabric Warehouse workspace.
 Automatically bound user credentials to Git
 AutoBoundGitCredentials
 Automatically bound user credentials to Git.
@@ -1352,6 +1361,9 @@ Edited Power BI semantic model options
 EditedSemanticModelOptions
 A user made a change to their semantic model options. This occurs when changes are made in the model options dialog.
+Executed a tenant relocation
+TenantRelocationExecuted
+Executed tenant relocation.
 Export item definitions
 ExportItemDefinitions
 Export multiple item definitions from a workspace.
@@ -1364,6 +1376,9 @@ Git connection settings updated
 GitConnectionSettingsUpdated
 Git connection settings updated.
+Granted consent to tenant relocation
+TenantRelocationConsentGranted
+Tenant relocation consent granted.
 Import item definitions
 ImportItemDefinitions
 Import multiple item definitions into a workspace.
@@ -1403,12 +1418,24 @@ Retrieved artifact's Logical Id
 ArtifactLogicalIdRetrieved
 Retrieved artifact's Logical Id.
+Revoked consent to tenant relocation
+TenantRelocationConsentRevoked
+Tenant relocation consent revoked.
 Sent a Digital Operations Ontology Agent message
 DigitalOperationsOntologyAgentMessageSent
 A user sent a message in a Digital Operations Ontology Agent conversation.
 Sent a Fabric Copilot message
 FabricCopilot
```

---

### 2. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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
--- +++ @@ -102,7 +102,7 @@ Runs with the user's permissions
 âEach automated task runs as the user who created it. It sees only the data that user can see and acts only through the same governed, enterprise-compliant tools available in an interactive conversation.
 Approval before shared actions
-âBy default, when a task would send an email, post a message, or change a shared system, Cowork prepares the action and asks the user for approval before it happens. For a more seamless experience that requires no user intervention for the task to be triggered, you can pre-authorize Cowork to complete the task for you.
+âBy default, when a task would send an email, post a message, or change a shared system, Cowork prepares the action and asks the user for approval before it happens. For a more seamless experience that requires no user intervention for the task to be triggered, you can pre-authorize Cowork to complete the task for you. This pre-authorization is given to that current chat session, and doesn't pre-authorize Cowork to complete actions in any net new chat sessions that require approval. If a scheduled or event triggered task starts a new chat session, it inherits permissions given in the initial creation.
 Rate limits and loop protection
 âAutomated tasks have limits on how often they can run, and Cowork guards against tasks that trigger themselves in a loop.
 Audit visibility

```

---

### 3. Manage federated connector availability

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/manage-federated-connectors
**Section:** Agent Governance
**Classification:** CRITICAL (Breaking changes)

**Affected Controls:**
- Control 2.16: Control 2.16: Federated Copilot Connector and Model Context Protocol (MCP) Governance
  - File: `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -22,12 +22,21 @@ Manage federated connector availability
 Feedback
 Summarize this article for me
+Important
+Work IQ Dev Tools (preview)
+- Work IQ Dev Tools (
+wiqd
+) are experimental, prerelease tools for building, validating, provisioning, packaging, publishing, evaluating, and monitoring Microsoft 365 Copilot declarative agents from the terminal. They're not production-ready or officially supported, and breaking changes are expected. For more information, see the
+Work IQ Dev Tools documentation
+.
 Federated connectors for Microsoft 365 Copilot enable users to access information from external data sources directly within their Copilot experience. Microsoft provides default federated connectors that use the Model Context Protocol (MCP) to integrate with popular services and tools. While these connectors enhance Copilot's capabilities by extending its knowledge base, organizations might need to control their availability for security, compliance, or governance reasons.
 As an administrator, you can use PowerShell to manage the availability of all default federated connectors across your tenant. This centralized management approach allows you to quickly disable or enable connectors organization-wide while maintaining visibility and control over individual connector settings.
 Important
 Microsoft is retiring the command-line (CLI) toggle for setFederatedConnectors by
 August 20, 2026
-. The CLI is being deprecated so that connector and agent settings are honored from the same global tenant settings, giving you one consistent place to govern both. Going forward, you can manage the same intent through the 'Allowed agent types' setting in Agent 365. For more information, see
+. The CLI is being deprecated so that connector and agent settings are honored from the same global tenant settings, giving you one consistent place to govern both. Going forward, you can manage the same intent through the
+Allowed agent types
+setting in Agent 365. For more informa
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

### 2. Copilot Cowork admin and governance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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