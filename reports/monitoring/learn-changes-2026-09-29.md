# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-29
**Run Time:** 2026-09-29T16:14:45.852204+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 1 |
| HIGH Changes | 1 |
| MEDIUM Changes | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | agent-builder-build-agents | HIGH | None | Review and update |
| 2 | connected-platforms | CRITICAL | None | Monitor |
| 3 | data-connectors-reference | CRITICAL | 4.11, 3.1 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** CRITICAL (UI navigation steps changed)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -644,6 +644,143 @@ Data collection rule support:
 Not currently supported
 Setup Instructions:
+Airlock Digital (Poll - SaaS)
+Supported by:
+Airlock Digital
+The
+Airlock Digital
+SaaS
+connector periodically pulls execution history and server activity logs from the Airlock Digital SaaS API, authenticating with a user API key together with your directory and tenant identifiers. It is the polling connector for Airlock Digital's hosted SaaS offering, and it does not collect policy change logs. For self-hosted servers or Airlock Digital SaaS running v7.0 or higher, the
+Airlock Digital (Push)
+connector delivers events in near real time and also collects policy changes. For self-hosted servers older than v7.0, use the
+Airlock Digital (Poll)
+connector.
+NOTE:
+Use one connector per Airlock Digital server. If the same server is collected by more than one Airlock Digital connector, duplicate data is populated in the tables.
+Log Analytics table(s):
+Table
+DCR support
+Lake-only ingestion
+AirlockDigitalExecutionHistories_CL
+No
+No
+AirlockDigitalServerActivities_CL
+No
+No
+Data collection rule support:
+Not currently supported
+Prerequisites:
+Airlock Digital SaaS API credentials
+: A user API key, directory ID, and tenant ID for your Airlock Digital SaaS instance.
+Setup Instructions:
+Configure access to the Airlock Digital SaaS API
+Set up API access in your Airlock Digital SaaS tenant before connecting.
+Your server URL comes from your portal address: take
+https://portal.au.YourDomain.com/tenant/XYZ/dashboard
+and drop the
+portal.
+prefix and everything after the top-level domain, leaving
+https://au.YourDomain.com
+.
+The user API key, directory ID and tenant ID are in Airlock Digital under
+User Menu > My Profile
+.
+Logs are polled every five minutes.
+Connect Airlock Digital SaaS instances to Microsoft Sentinel
+This connector supports multiple simultaneous connections. Add one connection per Airlock Digital SaaS instance; each connection ingest
```

---

## HIGH: Control Review Recommended

### 1. Build agents with Agent Builder

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -47,11 +47,7 @@ Adds knowledge sources. For example: "Summarize my daily emails and include attachments." Agent Builder adds
 My emails
 as a knowledge source.
-Integrates capabilities. For example: "Create a PowerPoint presentation from this outline" or "Analyze this Excel data and generate a chart." Agent Builder configures your agent with
-code interpreter
-and
-image generator
-.
+Integrates capabilities. For example: "Create a PowerPoint presentation from this outline" or "Analyze this Excel data and generate a chart." Code interpreter and image generator capabilities are automatically available.
 You can also choose the plus sign (
 +
 ) in the chat box to select and add or search for knowledge sources.
@@ -123,12 +119,8 @@ Write effective instructions
 .
 Knowledge
-You can specify up to 20 knowledge sources (including SharePoint sites, folders, and files) or Copilot connectors. For details, see
+Add public websites, organizational and personal work content, embedded files, and Microsoft 365 Copilot connectors as knowledge sources. Availability and limits vary by source type. For details, see
 Add knowledge sources
-.
-Capabilities
-You can enhance the user experience of your declarative agent by adding capabilities. For details, see
-Add capabilities
 .
 Starter Prompts
 Starter prompts help other users understand commonly supported scenarios by your agent. Each starter prompt comes with a name and description. There's no minimum number of starter prompts.
@@ -138,7 +130,7 @@ Try it
 tab. You can continue to refine your agent's instructions, knowledge, and starter prompts.
 Build from a template
-Agent Builder in Microsoft 365 Copilot includes templates that you can use to build agents for specific use cases. The templates come preconfigured with a description, instructions, and prompts. Use the templates as-is or customize them for your specific needs, such as adding more knowledge sources and capabilities.
+Agent Builder in Microsoft 365 Copilot
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft Agent 365 registry sync
**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms
**Classification:** CRITICAL (Deprecation notice)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*