# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-12
**Run Time:** 2026-09-12T13:15:01.159829+00:00
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
| 1 | connect-to-ai-models | HIGH | 3.8a, 2.7, 1.10 | Update portal-walkthrough |
| 2 | cowork-admin-governance | MEDIUM | 4.15 | Update portal-walkthrough |
| 3 | restricted-content-discovery | HIGH | 2.5, 1.2, 1.7, 1.13, 1.3, 1.4 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Connect to xAI models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Section:** Copilot Administration
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`

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
--- +++ @@ -37,16 +37,6 @@ and the
 xAI Data Processing Addendum
 .
-Important
-Microsoft's safety and responsible AI evaluations found Grok-4.1 Fast (Non-Reasoning) to be less aligned than other models evaluated resulting in (i) higher risks that the model will produce potentially harmful content and (ii) lower scores on safety and jailbreak benchmarks. Grok-4.1 Fast (Non-Reasoning) may be capable of producing explicit content, and may do so with a higher propensity than other models. Customers must comply with both the
-Microsoft Enterprise AI Services Code of Conduct
-and the
-xAI Enterprise Terms of Service
-, including the
-xAI Acceptable Use Policy
-. Additionally, there may be categories of harm this model can produce that are not covered by Microsoft's content safety systems. Accordingly, as with all Experimental models, Grok-4.1 Fast (Non-Reasoning) is not recommended for production use and customers should review
-Limitations of experimental and preview models
-and conduct their own evaluations before choosing Grok-4.1 Fast (Non-Reasoning).
 Before you begin
 Before users in your organization can use SpaceXAI, they need to be assigned a
 Microsoft Copilot license

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
--- +++ @@ -153,6 +153,7 @@ Set up Copilot Credits
 Estimate costs in the Cowork cost estimator
 Gain visibility into how users engage with Cowork in the Cowork Usage report
+How to use the Consumption Dashboard in InsightsâCowork page
 Automated tasks
 Users can create automated tasks that run without a person present: scheduled prompts that run at a set time, and event-driven tasks that run when a matching email or Teams message arrives. Cowork applies the same governance to these tasks that it applies to interactive conversations, with additional safeguards:
 Runs with the user's permissions

```

---

### 3. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -22,15 +22,16 @@ Restrict discovery of SharePoint sites and content
 Feedback
 Summarize this article for me
-Organizations preparing for Microsoft Copilot often need time to review SharePoint sites, validate permissions, and implement governance controls before making content broadly discoverable. Restricted Content Discovery (RCD) helps you limit discovery of content from specific SharePoint sites, including recently interacted files, in organization-wide search results and Microsoft Copilot responses while those reviews are taking place.
-RCD also removes AI-powered entry points from these SharePoint sites. Users don't see entry points such as the Copilot button, AI actions menus (including creating agents), or
+Organizations preparing for Microsoft Copilot often need time to review SharePoint sites, validate permissions, and implement governance controls before making content broadly discoverable. Restricted Content Discovery helps you limit discovery of content from specific SharePoint sites, including recently interacted files, in organization-wide search results and Microsoft Copilot responses while those reviews are taking place.
+Restricted Content Discovery also removes AI-powered entry points from these SharePoint sites. Users don't see entry points such as the Copilot button, AI actions menus (including creating agents), or
 Create pages with AI
 . This restriction helps reduce the likelihood of accidental discovery of content while permissions and governance controls are being evaluated.
 When a site has a Restricted Content Discovery policy applied to it, a Restricted tag is visible, as shown in the following screenshot:
 Restricted Content Discovery is designed as a temporary governance control that gives organizations time to review and right-size access while continuing their Copilot deployment.
 Note
+You can apply Restricted Content Discovery to up to 20,000 sites.
 Restricted Content Discovery doesn't change existing permissions. Users
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Cowork admin and governance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*