# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-23
**Run Time:** 2026-09-23T14:32:29.444189+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| MEDIUM Changes | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | HIGH | 4.12 | Update portal-walkthrough |
| 2 | apply-sensitivity-label-automatically | HIGH | 2.2, 1.5 | Update portal-walkthrough |
| 3 | restricted-content-discovery | MEDIUM | 2.5, 1.2, 1.7, 1.13, 1.3, 1.4 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

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
--- +++ @@ -3433,7 +3433,7 @@ Makes interactions with multiple agents feel smoother.
 Additional Resources:
 Learn:
-Manage Connected Agents for Researcher in the Microsoft 365 admin center
+Manage Connected Agents in the Microsoft 365 admin center
 Connect to other agents from a declarative agent
 Microsoft Loop
 Generate PowerPoint grounded on a Copilot page
@@ -5152,7 +5152,7 @@ Makes interactions with multiple agents feel smoother.
 Additional Resources:
 Learn:
-Manage Connected Agents for Researcher in the Microsoft 365 admin center
+Manage Connected Agents in the Microsoft 365 admin center
 Connect to other agents from a declarative agent
 January 13, 2026
 Updates released between December 23, 2025, and January 13, 2026.
@@ -8237,7 +8237,7 @@ Makes interactions with multiple agents feel smoother.
 Additional Resources:
 Learn:
-Manage Connected Agents for Researcher in the Microsoft 365 admin center
+Manage Connected Agents in the Microsoft 365 admin center
 Connect to other agents from a declarative agent
 Microsoft Loop
 Generate PowerPoint grounded on a Copilot page

```

---

### 2. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`

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
--- +++ @@ -47,6 +47,10 @@ See
 Learn about simulation mode
 â the caveats cover the most common causes (12-hour completion window, single-policy scope, files modified after the run, and the sensitive info type created-after-modification rule).
+I turned on a policy after simulation and want to review coverage.
+See
+Review coverage by simulation context
+.
 A specific file wasn't labeled and I expected it to be.
 Open the policy's
 Labeled items
@@ -1101,6 +1105,58 @@ , which are transient infrastructure errors that are typically retried automatically. For the full list of failure reasons and recommended actions, see
 Resolve auto-labeling failures in SharePoint and OneDrive files
 .
+Review coverage by simulation context
+After you run an auto-labeling policy in simulation mode and then turn on the policy, use
+Coverage by simulation context
+to review labeling activity for that policy. The coverage report helps you see which files were labeled, pending, or not labeled, and whether those files were found in the latest simulation run.
+Use this report to:
+Review how labeling activity is distributed after the latest simulation run.
+Identify files that were found in simulation and then labeled during enforcement.
+Review files that are pending, not yet attempted, or failed to apply a label.
+Investigate files that don't have a match in the latest simulation run.
+Coverage is based on labeling activity after the latest simulation run and is available for 30 days. After 30 days,
+View coverage
+is unavailable for that simulation run. To view coverage again, run the policy in simulation mode again and then review the updated coverage report.
+The coverage report isn't an all-time policy total and isn't intended to be an exact reconciliation between simulation and enforcement. All-time labeled totals can include activity from before or after the coverage window, so they might not match the counts shown in the coverage report.
+To open the coverage report:
+In the Mic
```

---

### 3. Restricted Content Discovery

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
--- +++ @@ -29,7 +29,6 @@ When a site has a Restricted Content Discovery policy applied to it, a Restricted tag is visible, as shown in the following screenshot:
 Restricted Content Discovery is designed as a temporary governance control that gives organizations time to review and right-size access while continuing their Copilot deployment.
 Note
-You can apply Restricted Content Discovery to up to 20,000 sites.
 Restricted Content Discovery doesn't change existing permissions. Users who already have access to content can continue to access that content directly.
 You can only apply this feature to SharePoint sites. It's not supported for OneDrive sites.
 Restricted Content Discovery doesn't affect searches that originate from site context or other intelligent experiences such as Microsoft 365 Feed and Recommendations.

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Restricted Content Discovery
**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*