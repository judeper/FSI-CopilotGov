# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-10
**Run Time:** 2026-10-10T15:37:58.211098+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | connect-to-ai-models | HIGH | 1.10, 2.7, 3.8a | Update portal-walkthrough |
| 2 | content-governance-agent | HIGH | 1.7 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Connect to xAI models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,11 +1,11 @@ Connect to SpaceXAI models (as an independent processor)
-You can now use SpaceXAI models within your Microsoft products. These models are hosted by SpaceXAI outside of Microsoft. You can elect to use SpaceXAI models with Copilot Studio in Microsoft 365.
+You can now use SpaceXAI models within your Microsoft products. These models are hosted by SpaceXAI outside of Microsoft. You can elect to use SpaceXAI models with Copilot Studio and with Copilot Cowork in Microsoft 365.
 SpaceXAI models can help people in your organization with some of the following:
 Summarize complex information
 Answer questions using source material
 Synthesize across multiple sources
 Idea generation, drafting and editing
-When your organization chooses to use a SpaceXAI model, your organization is choosing to share your data with SpaceXAI to power Copilot Studio features. This data is processed outside all Microsoft managed environments and audit controls, therefore Microsoft's customer agreements, including the
+When your organization chooses to use a SpaceXAI model, your organization is choosing to share your data with SpaceXAI to power Copilot Studio and Copilot Cowork features. This data is processed outside all Microsoft managed environments and audit controls, therefore Microsoft's customer agreements, including the
 Product Terms
 and
 Data Processing Addendum

```

---

### 2. SharePoint Admin Agent (Content Governance Agent)

**URL:** https://learn.microsoft.com/en-us/sharepoint/content-governance-agent
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -107,18 +107,18 @@ Is Baseline Security Mode enabled in my tenant?
 Recovery options
 What recovery options are available for my SharePoint and OneDrive sites?
-OneDrive libraries to move to another geo (preview)
-(This feature is currently in preview for
+OneDrive libraries to move to another geo
+(This feature is available for
 multi-geo organizations
 .)
 Show me users whose OneDrive libraries need to be moved to another location
-Cross-geo moves that failed (preview)
-(This feature is currently in preview for
+Cross-geo moves that failed
+(This feature is available for
 multi-geo organizations
 .)
 Show me cross geo moves that have failed
-Status of cross-geo moves (preview)
-(This feature is currently in preview for
+Status of cross-geo moves
+(This feature is available for
 multi-geo organizations
 .)
 Show me the status of all cross geo moves initiated in past 7 days

```

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