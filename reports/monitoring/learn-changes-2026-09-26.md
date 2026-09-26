# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-26
**Run Time:** 2026-09-26T13:57:50.752698+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 2 | discovery-setting-ai-experiences | CRITICAL | 4.15 | Update portal-walkthrough |
| 3 | ...-based-billing-manage-copilot-credits | HIGH | 4.15 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Apply sensitivity labels automatically

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
--- +++ @@ -50,6 +50,10 @@ I turned on a policy after simulation and want to review coverage.
 See
 Review coverage by simulation context
+.
+I want SharePoint default library labels to apply to existing files.
+See
+Apply default sensitivity labels from SharePoint document libraries to existing files
 .
 A specific file wasn't labeled and I expected it to be.
 Open the policy's
@@ -117,6 +121,9 @@ When the label applies encryption, the
 Rights Management issuer and Rights Management owner
 is the account that last modified the file.
+To apply default sensitivity labels from SharePoint document libraries to existing files, see
+Apply default sensitivity labels from SharePoint document libraries to existing files
+.
 Auto-labeling for Exchange
 PDF attachments and Office attachments are scanned for the conditions you specify in your auto-labeling policy. When there's a match, the email is labeled but not the attachment.
 For PDF files, if the label applies encryption, these files are encrypted by using
@@ -625,6 +632,39 @@ Finally, you can use simulation mode to provide an approximation of the time needed to run your auto-labeling policy, to help you plan and schedule when to run it without simulation mode.
 Note
 If the simulation results don't include files that you expect, based on your configured auto-policy conditions and the current file contents, it might be because the files were updated after the simulation ran. Check if the files were updated and run simulation again to confirm they will be labeled.
+Apply default sensitivity labels from SharePoint document libraries to existing files
+SharePoint document libraries can be configured with a default sensitivity label. SharePoint applies this label to new files and to files that users edit in the library. Files that already existed in the library before the default label was configured might remain unlabeled.
+To extend your default library label deployment to existing files, create an auto-labeling policy tha
```

---

### 2. Managing AI experiences enabled by usage-based billing

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences
**Section:** Copilot Cowork
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -22,6 +22,10 @@ Discovery setting for AI experiences enabled by usage-based billing
 Feedback
 Summarize this article for me
+Important
+The
+AI experiences enabled by usage-based billing
+setting is deprecated. This setting will be replaced by a new setting that allows admins to control whether users or groups can request access to experiences that require usage-based billing.
 The
 AI experiences enabled by usage-based billing
 setting controls whether users in your organization can see AI experiences that rely on usage-based billing.

```

---

### 3. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

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
--- +++ @@ -29,7 +29,7 @@ Automatically apply existing spending policies to future supported services and agents.
 Configure organizational and user-level spending limits.
 Configure threshold notifications for administrators and users.
-Use prepaid credits, pay-as-you-go billing, or supported combinations of these billing methods.
+Use Capacity packs, pay-as-you-go billing, Copilot Credit Pre-purchase plans (P3), or supported combinations of these billing methods.
 Configure custom approval routing for credit requests.
 Monitor consumption by spending policy, group, user, agent, service, and funding source.
 These controls help organizations understand cost drivers, apply spending safeguards, and manage Copilot Credit consumption at scale.
@@ -58,7 +58,7 @@ .
 Role requirements
 Global administrator and Billing administrator roles can add, select, and change billing methods, and set billing methods in policies.
-AI administrator and License administrator roles can create spending policies and manage limits and alerts. They can't set or modify the billing method.
+AI administrator and License administrator roles can edit spending policies, manage limits and alerts, and billing methods. However, they can't create spending policies.
 AI Reader, Global Reader, License Administrator, and other supported reader-based roles can view consumption dashboards and reports. These roles provide read-only access to consumption information and don't allow administrators to create or change spending policies, limits, alerts, request policies, or billing methods.
 Note
 Review existing role assignments. Assign a supported reader-based role to users who need to review consumption and spending information but don't need configuration permissions.
@@ -125,21 +125,24 @@ Manage Configuration
 . The
 Configuration
-tab within the Cost management page is displayed. Copilot consumptive services are now available. You can configure more policies to scope access to specific groups, users, or 
```

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*