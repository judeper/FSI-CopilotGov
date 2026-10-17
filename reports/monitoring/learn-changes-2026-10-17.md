# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-17
**Run Time:** 2026-10-17T13:21:04.998488+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 4 |
| MEDIUM Changes | 2 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | HIGH | 4.12 | Update portal-walkthrough |
| 2 | discovery-setting-ai-experiences | MEDIUM | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 3 | agent-extend-action-mcp | MEDIUM | None | Review optional |
| 4 | connected-platforms | HIGH | 1.13, 2.14, 4.13, 2.13 | Update portal-walkthrough |
| 5 | manage-federated-connectors | CRITICAL | 2.16 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

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
--- +++ @@ -14,6 +14,12 @@ for data governance solutions.
 Roadmap
 for data security and risk and compliance solutions.
+October 2026
+Data Loss Prevention
+General availability
+: Endpoint data loss prevention (DLP) can now monitor sensitive data transferred over FTP and SFTP from managed Windows devices. It can enforce restrictive actions to help prevent data exfiltration. Configure FTP and SFTP transfer activities in your Endpoint DLP policies to get started. See
+Protect FTP and SFTP transfers with Microsoft Purview Endpoint DLP
+.
 September 2026
 Data Loss Prevention
 General availability

```

---

### 2. Discovery setting for AI experiences enabled by usage-based billing

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences
**Section:** Copilot Cowork
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -3,6 +3,8 @@ The
 AI experiences enabled by usage-based billing
 setting is deprecated. This setting will be replaced by a new setting that allows admins to control whether users or groups can request access to experiences that require usage-based billing.
+For more information on the new setting, see
+Access requests to usage-based billing experiences
 The
 AI experiences enabled by usage-based billing
 setting controls whether users in your organization can see AI experiences that rely on usage-based billing.

```

---

### 3. Connected platforms in Microsoft Agent 365 (manual sync)

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms
**Section:** Agent Governance
**Classification:** HIGH (UI element names)

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
--- +++ @@ -90,6 +90,8 @@ Third-party
 agent observability (Frontier)
 .
+Note
+Databricks Genie observability is available through the Frontier program.
 Current limitations
 Manual synchronization only.
 Agent 365 doesn't currently sync on a

```

---

### 4. Manage federated connector availability

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
--- +++ @@ -1,111 +1,171 @@ Manage federated connector availability
-Important
-Work IQ Dev Tools (preview)
-- Work IQ Dev Tools (
-wiqd
-) are experimental, prerelease tools for building, validating, provisioning, packaging, publishing, evaluating, and monitoring Microsoft 365 Copilot declarative agents from the terminal. They're not production-ready or officially supported, and breaking changes are expected. For more information, see the
-Work IQ Dev Tools documentation
+Federated connectors for Microsoft 365 Copilot enable users to access information from external data sources directly within their Copilot experience. Microsoft provides default federated connectors that use the Model Context Protocol (MCP) to integrate with popular services and tools. While these connectors enhance Copilot's capabilities by extending its knowledge base, organizations might need to control their availability for security, compliance, or governance reasons.
+As an administrator, you manage federated connector availability in the Microsoft 365 admin center. Use Agent and plugin access to allow or block connectors in bulk by publisher type, User access to set which users can use connectors, and connector-level settings to enable, disable, or stage individual connectors.
+Manage federated connector availability for your organization
+Agent and plugin access lets you:
+Turn off all connectors of a publisher type (Microsoft, your organization, or external publishers) in a single step.
+Apply that choice automatically to future connectors of that type.
+Selectively turn on specific connectors while the bulk setting stays off.
+Re-select the option to restore default behavior.
+Prerequisites
+To manage federated connectors, you need one of the following administrator roles:
+Global Administrator
+Search Administrator
+Control connector availability with Agent and plugin access
+Agent and plugin access controls which types of agents and plugins, including connectors and MCP servers, are av
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Discovery setting for AI experiences enabled by usage-based billing
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences
**Classification:** MEDIUM (General content update)

---

### 2. Model Context Protocol in Copilot Studio
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
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