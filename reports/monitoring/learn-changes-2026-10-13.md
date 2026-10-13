# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-13
**Run Time:** 2026-10-13T17:14:49.903842+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 4 |
| MEDIUM Changes | 1 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 2 | audit-log-activities | MEDIUM | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 3 | manage-copilot-agents-integrated-apps | HIGH | 1.13, 2.13, 2.14, 2.17, 4.1, 4.13 | Update portal-walkthrough |
| 4 | agent-registry | HIGH | 2.14, 4.14, 4.13, 1.13, 2.13 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Portal references)

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
--- +++ @@ -578,13 +578,15 @@ Simulation is designed to evaluate and log matches without applying (or removing) labels. It is not a fully silent dry run. Before you run a simulation, know these behaviors that customers frequently misdiagnose as bugs:
 Simulation still generates activity alerts.
 If a Microsoft Purview alert policy is configured on auto-labeling or sensitive-information-type activity, matches surfaced during simulation trigger those alerts. To avoid mass alert email while validating a policy, temporarily scope or disable the alert policy for the simulation window.
-Policy management is greyed out for roughly 24 hours after a policy is created.
-During this window, the
+Policy actions depend on status and permissions.
+If
 Turn on policy
 ,
-, and
+, or
 Delete
-actions on a newly-created policy are unavailable while the backend finishes provisioning. This is normal â wait 24 hours, then refresh.
+is unavailable, check the current policy status and your permissions. For
+Turn on policy
+, also check the simulation status. Review any displayed error before retrying.
 A duplicated policy lands in simulation by default and doesn't notify you.
 Duplicating an existing policy creates a new policy in simulation regardless of the source policy's state. If you expect the duplicate to inherit the source's active state, it won't.
 Simulation and DLP share the same test-mode surface.
@@ -645,7 +647,16 @@ One or more SharePoint document libraries in your target sites have a default sensitivity label configured.
 You have permissions to create and manage auto-labeling policies.
 You have permission to read the SharePoint site and document library metadata required to identify libraries with default sensitivity labels. For the currently supported configuration path, use Compliance Administrator or an existing SharePoint or Microsoft Entra role with this access, such as SharePoint Administrator.
-When you create the policy, select the option to apply default sensi
```

---

### 2. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
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
--- +++ @@ -1497,6 +1497,9 @@ Updated connection role assignment by tenant admin
 UpdatedGatewayDatasourceByAdmin
 A tenant admin add or updates the connection role assignment.
+validate connection access for a given identity.
+ValidatedConnectionAccess
+validate connection access for a given identity.
 Updated git items selection
 GitItemsSelectionUpdated
 Updated git items selection.

```

---

### 3. Manage plugins for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide
**Section:** Copilot Extensibility
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`
- Control 4.1: Control 4.1: Copilot Admin Settings and Feature Management
  - File: `controls/pillar-4-operations/4.1-admin-settings-feature-management.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

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
- ⚠️ `playbooks/control-implementations/2.17/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.17/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -66,6 +66,15 @@ is enabled for Copilot Studio. You can also manage flows using the
 Power Platform admin center
 .
+Note
+The same Copilot Studio agent (declarative or custom engine) can appear more than once in the admin center with different publisher states, such as
+Shared by creator
+and
+Published by your organization
+. Depending on the publishing lifecycle and the actions that creators and admins take, these duplicate-looking entries can represent separate lifecycle and publisher records for the same underlying agent. They're expected and by design, not an error.
+For lifecycle details and available admin actions, see
+How one agent can appear as multiple entries
+.
 Get started
 To get started managing agents within Microsoft 365 admin center, see
 Agent management in Microsoft 365 admin center

```

---

### 4. Agent registry in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
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
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -27,6 +27,35 @@ Custom agents approved and published by your organization for broader use. These agents might be referred to as LOB (Line of Business) agents.
 Shared by creator
 Agents created and shared by individual users or developers at your organization. These agents are commonly referred to as Shared agents.
+Note
+The same Copilot Studio agent (declarative or custom engine) can appear more than once in the registry with different publisher types, such as
+Shared by creator
+and
+Published by your org
+. These duplicate-looking rows are expected and by design. They represent separate lifecycle and publisher records for the same underlying agent, not an inventory error.
+For lifecycle details and available admin actions, see
+How one agent can appear as multiple entries
+.
+How one agent can appear as multiple entries
+For a custom engine agent, how it appears in the registry depends on its publishing lifecycle and on the actions that creators and admins take:
+Publishing the agent in Copilot Studio alone might not make it visible in the admin center.
+Selecting
+See agent in Microsoft 365
+creates a
+Shared by creator
+entry, which creators often use to test the agent before sharing it more broadly.
+Choosing to show the agent to everyone in the organization and submitting it for admin approval, followed by an admin publishing it, creates a
+Published by your org
+entry.
+Available admin actions differ by agent type and publisher state. For example, some entries offer
+Delete
+, others offer
+Remove
+, and some offer only
+Block
+. Removing one entry doesn't remove the other. For more information, see
+Agent types you can manage
+.
 Agent registry summary
 The agent
 Registry

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
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