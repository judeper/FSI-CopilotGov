# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-14
**Run Time:** 2026-10-14T14:46:38.134457+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 6 |
| MEDIUM Changes | 3 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | dlp-policy-reference | MEDIUM | None | Review optional |
| 3 | create-sensitivity-labels | MEDIUM | 1.5, 2.2 | Update portal-walkthrough |
| 4 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 5 | ...-based-billing-manage-copilot-credits | HIGH | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 6 | authoring-select-agent-model | CRITICAL | 1.16, 4.14 | Update portal-walkthrough |
| 7 | cross-tenant-access-overview | HIGH | 2.12 | Update portal-walkthrough |

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
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.9/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.9/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -22,6 +22,7 @@ . For more information, see
 Anthropic models in Microsoft Online Services
 .
+Compare Microsoft 365 Copilot licenses
 Copilot Chat (Basic) license
 Microsoft 365 Copilot (Basic) license
 Microsoft 365 Copilot (Premium) license

```

---

### 2. Create and configure sensitivity labels

**URL:** https://learn.microsoft.com/en-us/purview/create-sensitivity-labels
**Section:** Information Protection (Sensitivity Labels)
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -233,7 +233,7 @@ (Get-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e).settings
 Publish sensitivity labels by creating a label policy
 As part of the label policy, you select users and groups to have sensitivity labels and label policy settings. For lower administrative maintenance, groups are recommended rather than individual users. However, if a user is removed from a group you specify, the label policy is automatically removed for that user.
-Groups supported: Email-enabled security groups, distribution groups, Microsoft 365 groups (that can have
+Groups supported: Email-enabled security groups, non-mail enabled security groups, distribution groups, Microsoft 365 groups (that can have
 dynamic membership
 ) in Microsoft Entra ID.
 Sign in to the Microsoft Purview portal

```

---

### 3. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -4608,6 +4608,9 @@ Detected impersonation attempt
 TeamsImpersonationDetected
 An external message sender is detected to have potential impersonation activity.
+Detected security risk in meeting
+SecurityRiskInMeetingDetected
+A security risk was detected in a Microsoft Teams meeting, such as brand, domain, or user impersonation by a meeting organizer or participant.
 Detected security risk in call
 SecurityRiskInCallDetected
 A security risk was detected during an incoming call in Microsoft Teams, such as brand, domain, or user impersonation.

```

---

### 4. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (Policy language)

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
--- +++ @@ -88,7 +88,13 @@ Auto-apply new services
 for any policy that shouldn't automatically govern future supported services or agents.
 Set limits and alerts
-Microsoft continuously evaluates customer usage patterns and industry trends to help define healthy spending policies for usage-based billing scenarios to support a high-quality user experience. We are actively learning and refining these guardrails to ensure customers can successfully use Copilot capabilities. As a result, recommendations and policy requirements may evolve over time, and administrators may see updated guidance over time in the product experience intended to maintain a quality user experience.
+Microsoft continuously evaluates customer usage patterns and industry trends to define healthy spending policies for usage-based billing scenarios. We're continuing to refine these guardrails so customers can successfully use Copilot capabilities. As a result, recommendations and policy requirements may evolve, and administrators may see updated guidance in the product experience.
+Monthly budget limit for users:
+Set at least 2,000 credits per user per month
+Monthly spending limit for policy:
+Set the monthly spending limit for policy at or above the required minimum for eligible users covered by the policy
+What if your limit is lower than recommended?
+To help ensure a good user experience, your policy must meet the minimum. If your budget meets that minimum but is below the recommended amount, you can still save your policy. We'll suggest a limit that may better support your users.
 For the users and groups that you selected for this policy, select the credit limits that apply to them, similar to what you did for the default spending policy.
 Select the monthly spending limit for this policy.
 Unlimited monthly budget

```

---

### 5. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -42,21 +42,21 @@ South Africa
 United Kingdom
 United States
-GPT-4o
-General
-Retired
-Retired
-Retired
-Retired
-Retired
-Retired
-Retired
-Retired
-Retired
-Retired
-Retired
-Retired
-Retired
+GPT Chat Latest
+General
+Default (cross-geo)
+Default
+Default (cross-geo)
+Default (cross-geo)
+Default
+Default (cross-geo)
+Default (cross-geo)
+Default (cross-geo)
+Default (cross-geo)
+Default (cross-geo)
+Default (cross-geo)
+Default
+Default
 GPT-4.1
 General
 GA (cross-geo)
@@ -119,6 +119,96 @@ Preview
 GPT-5.3 Chat
 General
+Preview (cross-geo)
+Preview (cross-geo)
+Preview (cross-geo)
+Preview (cross-geo)
+Preview
+Preview (cross-geo)
+Preview (cross-geo)
+Preview (cross-geo)
+Preview (cross-geo)
+Preview (cross-geo)
+Preview (cross-geo)
+Preview (cross-geo)
+Preview
+GPT-5.5 Chat
+General
+GA (cross-geo)
+GA
+GA (cross-geo)
+GA (cross-geo)
+GA
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA
+GA
+Claude Sonnet 4.6
+General
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA
+Claude Opus 4.6
+Deep
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)

```

---

### 6. Microsoft Entra Cross-Tenant Access Settings

**URL:** https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview
**Section:** Agent Governance
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 2.12: Control 2.12: External Sharing and Guest Access Governance
  - File: `controls/pillar-2-security/2.12-external-sharing-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -206,7 +206,7 @@ , or a
 custom role
 .
-To configure trust settings or apply access settings to specific users, groups, or applications, you need a Microsoft Entra ID P1 license. The license is required on the tenant that you configure. For B2B direct connect, where mutual trust relationship with another Microsoft Entra organization is required, you need a Microsoft Entra ID P1 license in both tenants.
+To configure trust settings, change the default redemption order, or apply access settings to specific users, groups, or applications, you need a Microsoft Entra ID P1 license. The license is required on the tenant that you configure. For B2B direct connect, where mutual trust relationship with another Microsoft Entra organization is required, you need a Microsoft Entra ID P1 license in both tenants.
 Cross-tenant access settings are used to manage B2B collaboration and B2B direct connect with other Microsoft Entra organizations. For B2B collaboration with non-Microsoft Microsoft Entra identities (for example, social identities or non-IT managed external accounts), use
 external collaboration settings
 . External collaboration settings include B2B collaboration options for restricting guest user access, specifying who can invite guests, and allowing or blocking domains.

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

### 2. DLP policy reference
**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Classification:** MEDIUM (General content update)

---

### 3. Create and configure sensitivity labels
**URL:** https://learn.microsoft.com/en-us/purview/create-sensitivity-labels
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