# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-08
**Run Time:** 2026-10-08T17:04:48.122807+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| MEDIUM Changes | 2 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 3 | agent-id | MEDIUM | 2.3, 2.14, 2.17 | Update portal-walkthrough |

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
--- +++ @@ -104,11 +104,20 @@ Copilot Chat in Outlook and Teams
 Note
 The Microsoft 365 Copilot Chat app is now called Microsoft Copilot Chat
-. The primary URL for accessing the updated Copilot app is changing from
-m365.cloud.microsoft
-to
-copilot.cloud.microsoft
-. To help ensure users' connections aren't blocked, see
+. The primary URL for accessing the updated Copilot app is changing to
+copilot.cloud.microsoft
+. To help ensure users' connections aren't blocked, make sure to:
+Allow
+*.cloud.microsoft
+.
+Allow the Microsoft Copilot endpoints.
+Verify that proxies, firewalls, Conditional Access, tenant restrictions, and app-control policies don't block the Copilot app.
+Do not block
+copilot.cloud.microsoft
+to prevent personal account access. Instead, use
+tenant restrictions
+to control personal Microsoft-account sign.
+For more information, see
 Network requirements for Microsoft Copilot
 .
 Declarative agents that are grounded in instructions and public websites are included with Copilot Chat. Access to custom or other agents is pay-as-you-go only.
@@ -126,11 +135,20 @@ Microsoft 365 apps (Word, Excel, PowerPoint, and OneNote)
 Note
 The Microsoft 365 Copilot Chat app is now called Microsoft Copilot Chat
-. The primary URL for accessing the updated Copilot app is changing from
-m365.cloud.microsoft
-to
-copilot.cloud.microsoft
-. To help ensure users' connections aren't blocked, see
+. The primary URL for accessing the updated Copilot app is changing to
+copilot.cloud.microsoft
+. To help ensure users' connections aren't blocked, make sure to:
+Allow
+*.cloud.microsoft
+.
+Allow the Microsoft Copilot endpoints.
+Verify that proxies, firewalls, Conditional Access, tenant restrictions, and app-control policies don't block the Copilot app.
+Do not block
+copilot.cloud.microsoft
+to prevent personal account access. Instead, use
+tenant restrictions
+to control personal Microsoft-account sign.
+For more information, see
 Network requirements for Microsoft Cop
```

---

### 2. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Policy language)

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
--- +++ @@ -90,6 +90,12 @@ and Office files for Word (.docx), PowerPoint (.pptx), and Excel (.xlsx) are supported.
 These files can be auto-labeled at rest before or after the auto-labeling policies are created. Files can't be auto-labeled if they're part of an open session (the file is open).
 Currently, attachments to list items aren't supported and won't be auto-labeled.
+Important
+PDF labeling must be enabled for your tenant before an auto-labeling policy can process PDFs in SharePoint and OneDrive. Enable it by selecting the
+Protect PDFs with Auto-labeling
+banner in the Microsoft Purview portal, or by using PowerShell. If PDF labeling isn't enabled, PDFs are skipped entirely: PDFs aren't evaluated or sent for labeling, and no label is applied. For instructions, see
+Adding support for PDF
+.
 Maximum of 500,000 automatically labeled files in your tenant per day.
 Maximum of 100 auto-labeling policies per tenant. In the portal, each policy can target up to 1,000 explicitly included or excluded SharePoint sites, or up to 100 explicitly included or excluded OneDrive individual users or groups. If you keep the default configuration of
 All
@@ -502,6 +508,9 @@ You have
 enabled sensitivity labels for Office files in SharePoint and OneDrive
 .
+If you want the policy to process PDFs, you have
+enabled PDF support
+by using the portal banner or PowerShell. Otherwise, PDFs are skipped without being evaluated or sent for labeling.
 For OneDrive, the OneDrive account must be associated with the corresponding user account. A OneDrive account that isn't associated with its user account (sometimes called a detached OneDrive account) isn't supported for auto-labeling or simulation. Use a properly associated OneDrive account, or move the content to a supported SharePoint or OneDrive location, and then rerun simulation.
 At the time the auto-labeling policy runs, the file mustn't be open by another process or user. A file that's checked out for editing falls into this categ
```

---

### 3. Conditional Access for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.3: Control 2.3: Conditional Access Policies for Copilot Workloads
  - File: `controls/pillar-2-security/2.3-conditional-access-policies.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.17/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.17/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.3/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -67,9 +67,9 @@ Note
 The on-behalf-of flow is also known as delegated access. "On-behalf-of" describes the authentication flow, not the type of agent. These interactive agents involve a user interface for human interaction. Any agent can use this flow when a signed-in user is present and the agent needs to access resources with that user's identity and permissions.
 In this flow, the agent can't reuse the user's original token because it was issued for a different audience. Instead, the agent uses the OBO flow to exchange tokens with Microsoft Entra ID, obtaining a new token scoped to the target resource. This token exchange is also evaluated by Conditional Access, letting admins enforce granular controls over which resources agents can access on behalf of the user.
-Because the user is the subject in this flow, Conditional Access policies target
-users and groups
-, not agent identities.
+Because the signed-in user is the token subject in this flow, Conditional Access evaluates policies assigned to that
+user
+, whether the user is targeted directly, through a group, or through another supported user-targeting mechanism. Selecting an agent identity as the policy subject doesn't cover agent requests made on behalf of the user.
 Agents that act as applications
 Agents might access resources without a signed-in user. In this case the agent accesses the resource with its own identity. This flow is also known as client credentials flow, or app only access. All types of agents might use this flow. For more information about how agents authenticate with their own identity, see
 Agent OAuth flows: Autonomous apps
@@ -135,10 +135,17 @@ are enabled.
 Conditional Access only protects resources secured by Microsoft Entra ID. For example, if an agent accesses resources using an API key, it bypasses the Microsoft Entra ID authentication and token issuance pipeline entirely and Conditional Access policies won't apply to them.
 The following configurations aren't curren
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

### 2. Conditional Access for agent identities
**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id
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