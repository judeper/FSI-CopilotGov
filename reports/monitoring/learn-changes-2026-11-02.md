# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-02
**Run Time:** 2026-11-02T19:53:30.294711+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 1 |
| MEDIUM Changes | 1 |
| Redirects | 23 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | mcp-add-existing-server-to-agent | MEDIUM | None | Review optional |
| 2 | move-to-defender | HIGH | 4.11 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Transition Microsoft Sentinel to the Defender portal

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender
**Section:** Microsoft Sentinel
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -87,6 +87,14 @@ For more information about CMK, see
 Set up Microsoft Sentinel customer-managed key
 .
+Private Link support
+Azure Monitor Private Link Scope (AMPLS) provides private connectivity to Azure Monitor resources, including Log Analytics workspaces. For more information about configuring and using Private Link with Azure Monitor, see
+Use Azure Private Link to connect networks to Azure Monitor
+For Microsoft Sentinel in the Defender portal, AMPLS supports private data ingestion, but it doesn't support querying Sentinel data through Defender portal experiences or Microsoft Defender APIs when Log Analytics query access is restricted to private endpoints.
+Specifically:
+Supported: Microsoft Sentinel data ingestion into the Log Analytics workspace through AMPLS.
+Not supported: Querying that Sentinel data through Microsoft Defender portal experiences, such as Advanced Hunting, when Log Analytics query access is restricted to AMPLS/private endpoints.
+Customer impact: If public Log Analytics query access is disabled, Sentinel data in the Log Analytics workspace won't be available to Defender portal experiences that query Sentinel workspace data, including Advanced Hunting.
 Configure multi-workspace and multitenant management
 Defender supports one or more workspaces across multiple tenants through the
 Microsoft Defender multitenant portal

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Connect an existing MCP server to an agent
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot | https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*