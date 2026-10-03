# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-03
**Run Time:** 2026-10-03T14:27:47.493582+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| MEDIUM Changes | 2 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | CRITICAL | 4.12 | Update portal-walkthrough |
| 2 | apply-sensitivity-label-automatically | CRITICAL | 1.5, 2.2 | Update portal-walkthrough |
| 3 | audit-log-activities | MEDIUM | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 4 | discovery-setting-ai-experiences | MEDIUM | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 5 | ...-based-billing-manage-copilot-credits | HIGH | 4.15, 1.9, 4.8 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -20,6 +20,11 @@ : Integrate Microsoft Entra Global Secure Access with Purview to protect text, files, and AI interactions at the network layer, enforce restrictive actions based on DLP policies, and detect risky user activity through Insider Risk Management. It helps prevent sensitive data from being shared with untrusted cloud applications through browsers, apps, APIs, and add-ins, including generative AI platforms, social media, and collaborative platforms. See
 Learn about Microsoft Purview Network Data Security
 .
+Information Barriers
+New
+:
+Create an Information Barriers policy compliance report
+to identify SharePoint sites, OneDrive accounts, and user-owned SharePoint Embedded containers that no longer comply after Information Barriers policy changes.
 August 2026
 Data Governance
 Updated

```

---

### 2. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -33,11 +33,11 @@ Apply default sensitivity labels from SharePoint document libraries to existing files
 .
 A specific file wasn't labeled and I expected it to be.
-Open the policy's
-Labeled items
-tab and switch to the
-Failed
-view to see the failure reason. For the full list of reasons and fixes, see
+Select the policy, then
+View details
+in the policy details panel. In the newer review experience, open
+Labeling failures
+to investigate the file. For failure navigation, reasons, and fixes, see
 Resolve auto-labeling failures in SharePoint and OneDrive files
 .
 My active policy has stopped matching Exchange email.
@@ -608,6 +608,15 @@ Deploy in production.
 The simulated deployment runs like the WhatIf parameter for PowerShell, for a specific point in time. You see results reported as if the auto-labeling policy had applied your selected label, using the rules that you defined. You can then refine your rules for accuracy if needed, and rerun the simulation. However, because auto-labeling for Exchange applies to emails that are sent and received, rather than emails stored in mailboxes, don't expect results for email in a simulation to be consistent unless you can send and receive the exact same email messages.
 Simulation mode also lets you gradually increase the scope of your auto-labeling policy before deployment. For example, you might start with a single location, such as a SharePoint site, with a single document library. Then, with iterative changes, increase the scope to multiple sites, and then to another location, such as OneDrive.
+For details about the newer simulation overview, see
+Review simulation results for auto-labeling policies
+.
+Sample items
+, when displayed, shows the sampled item count.
+Contextual summary
+is available in supported portal experiences; viewing matched content requires the
+Data Classification Content Viewer
+role.
 Finally, you can use simulation mode to provide an approximation of the time needed to run your a
```

---

### 3. Audit log activities

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
--- +++ @@ -1320,6 +1320,9 @@ Created a Fabric Copilot session
 FabricCopilotSessionCreated
 A user created a Fabric Copilot session.
+Create a Microsoft Fabric free trial
+CreatedFabricTrial
+A new Microsoft Fabric free trial capacity was started.
 Created MirroredStorage
 CreatedMirroredStorage
 Generated when a user or service principal creates a Fabric MirroredStorage item, linking an external storage source to a workspace as OneLake shortcuts.

```

---

### 4. Discovery setting for AI experiences enabled by usage-based billing

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
--- +++ @@ -13,7 +13,7 @@ To use these experiences, administrators must complete setup in
 Copilot > Cost management
 , including configuring billing and spending policies. For more information, see
-Managing AI experiences enabled by usage-based billing
+Set up usage-based billing for Copilot Credits
 .
 After the setting is not selected:
 Usage-based AI experiences remain hidden from users, unless you set up usage-based billing for the user.
@@ -38,7 +38,7 @@ Allow users to discover and use AI experiences enabled by usage-based billing in Microsoft Copilot
 .
 Related articles
-Managing AI experiences enabled by usage-based billing
+Set up usage-based billing for Copilot Credits
 Usage-Based Billing and Cost Management for Copilot Credits
 Cowork Usage report
 Was this page helpful?

```

---

### 5. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (Portal references)

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
--- +++ @@ -1,15 +1,16 @@ Managing AI experiences enabled by usage-based billing
-Microsoft uses a usage-based billing model that uses Copilot Credits to provide flexible payment options alongside fixed licensing. This model enables organizations to manage and optimize AI service expenses effectively through centralized tools like the Cost management dashboard in the Microsoft 365 admin center.
-The Cost Management dashboard in the Microsoft 365 admin center helps organizations control, monitor, and optimize Copilot Credit spending for AI experiences enabled by usage-based billing.
+Use spending policies in the Cost Management dashboard to control access and Copilot Credit spending for AI experiences enabled by usage-based billing.
 Administrators can:
 Create spending policies that control access to supported agents and services.
 Automatically apply existing spending policies to future supported services and agents.
 Configure organizational and user-level spending limits.
 Configure threshold notifications for administrators and users.
-Use Capacity packs, pay-as-you-go billing, Copilot Credit Pre-purchase plans (P3), or supported combinations of these billing methods.
-Configure custom approval routing for credit requests.
-Monitor consumption by spending policy, group, user, agent, service, and funding source.
-These controls help organizations understand cost drivers, apply spending safeguards, and manage Copilot Credit consumption at scale.
+Assign model profiles and billing methods.
+For initial configuration and billing options, see
+Set up usage-based billing for Copilot Credits
+. To review consumption, see
+Monitor Copilot Credit spending
+.
 Important
 For a list of services managed by usage-based billing method, see
 Services managed by usage-based billing
@@ -17,11 +18,6 @@ To learn more about discovery settings for AI experiences enabled by usage-based billing, see
 Discovery setting for AI experiences enabled by usage-based billing
 .
-When a spendi
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

### 2. Discovery setting for AI experiences enabled by usage-based billing
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences
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