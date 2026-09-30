# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-28
**Run Time:** 2026-09-28T17:52:30.323139+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| MEDIUM Changes | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4 | Update portal-walkthrough |
| 2 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -129,6 +129,15 @@ bing.com/copilotsearch
 copilot.com
 copilot.ai
+Note
+The Microsoft 365 Copilot Chat app is now called Microsoft Copilot Chat
+. The primary URL for accessing the updated Copilot app is changing from
+m365.cloud.microsoft
+to
+copilot.cloud.microsoft
+. To help ensure users' connections aren't blocked, see
+recommended network configurations for Microsoft Copilot
+.
 Declarative agents that are grounded in instructions and public websites are included with Copilot Chat. Access to custom or other agents is pay-as-you-go only.
 To use organizational content with Copilot Chat:
 Copy and paste content, upload a file, or select a file when creating your prompt.
@@ -142,6 +151,15 @@ https://m365copilot.com/
 Microsoft 365 desktop app
 Microsoft 365 apps (Word, Excel, PowerPoint, and OneNote)
+Note
+The Microsoft 365 Copilot Chat app is now called Microsoft Copilot Chat
+. The primary URL for accessing the updated Copilot app is changing from
+m365.cloud.microsoft
+to
+copilot.cloud.microsoft
+. To help ensure users' connections aren't blocked, see
+recommended network configurations for Microsoft Copilot
+.
 In-app features you can use:
 Word: Draft, rewrite, and summarize documents
 Excel: Analyze data, generate insights, create formulas and visuals
@@ -214,6 +232,15 @@ https://m365copilot.com/
 Microsoft 365 desktop app
 Microsoft 365 apps (Word, Excel, PowerPoint, and OneNote)
+Note
+The Microsoft 365 Copilot app is now called Microsoft Copilot
+. The primary URL for accessing the updated Copilot app is changing from
+m365.cloud.microsoft
+to
+copilot.cloud.microsoft
+. To help ensure users' connections aren't blocked, see
+recommended network configurations for Microsoft Copilot
+.
 Other resources:
 Major services and features in Microsoft Graph
 Semantic indexing explained by Microsoft (YouTube video)

```

---

### 2. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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
--- +++ @@ -157,6 +157,7 @@ Set up Copilot Credits
 Estimate costs in the Cowork cost estimator
 Gain visibility into how users engage with Cowork in the Cowork Usage report
+Understand how Cowork is being used and where it provides value
 How to use the Consumption Dashboard in InsightsâCowork page
 Automated tasks
 Users can create automated tasks that run without a person present: scheduled prompts that run at a set time, and event-driven tasks that run when a matching email or Teams message arrives. Cowork applies the same governance to these tasks that it applies to interactive conversations, with additional safeguards:
@@ -173,6 +174,8 @@ Security and compliance
 Microsoft Purview is available to secure and govern Cowork. Learn more in
 Use Microsoft Purview to manage data security & compliance for Microsoft Copilot Cowork
+and
+What is Copilot Managed Runtime (preview)
 .
 Data residency
 Copilot Cowork follows the same data residency model as Copilot. Learn more in

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*