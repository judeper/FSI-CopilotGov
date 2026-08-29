# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-29
**Run Time:** 2026-08-29T14:48:22.047311+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| MEDIUM Changes | 1 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | copilot-teams-transcription | MEDIUM | 4.2 | Update portal-walkthrough |
| 2 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Copilot in Teams meetings

**URL:** https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 4.2: Control 4.2: Copilot in Teams Meetings Governance
  - File: `controls/pillar-4-operations/4.2-teams-meetings-governance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.2/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -63,7 +63,7 @@ .
 Important
 Microsoft Copilot in Teams meetings and events isn't available in end-to-end encrypted meetings. For more information on end-to-end encryption, see
-Require end-to-end encryption for sensitive Teams meetings
+Manage end-to-end encryption for Microsoft Teams meetings and one-to-one calls
 .
 Note
 Microsoft Copilot in Teams isn't currently available for GCC High.

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
--- +++ @@ -34,6 +34,10 @@ Prerequisites for auto-labeling policies
 first, then follow
 Creating an auto-labeling policy
+.
+I want to label Exchange email based on the subject, sender, or recipient.
+See
+Example: Apply a label to Exchange email based on the subject
 .
 I'm deciding between labeling in Office apps and an auto-labeling policy.
 See
@@ -932,6 +936,49 @@ For the
 Summary
 page: Review the configuration of your auto-labeling policy and make any changes that you need, and complete the configuration.
+Example: Apply a label to Exchange email based on the subject
+In this example, an auto-labeling policy applies the
+High Confidence
+sensitivity label when an email subject matches the fictional project codename
+Project Atlas
+.
+Make sure the
+High Confidence
+sensitivity label is published to at least one user and its scope includes
+Emails
+.
+Follow the preceding steps to create a policy that automatically applies a label. Select
+Custom
+>
+Custom policy
+, and then select the
+High Confidence
+label.
+On the
+Choose locations where you want to apply the label
+page, select
+Exchange
+. Keep the default of
+All
+included and
+None
+excluded if the policy must evaluate incoming email from outside your organization.
+On the
+Set up common or advanced rules
+page, select
+Advanced rules
+. Create a rule for Exchange, add the
+Subject matches patterns
+condition, and enter a regular expression that matches
+Project Atlas
+in the subject. For information about regular expressions for this condition, see
+SubjectMatchesPatterns
+.
+Run the policy in simulation mode and send representative test messages while simulation is running. Review the matching messages on the
+Items to review
+tab, and then turn on the policy.
+Note
+You don't need an Exchange mail flow rule or a data loss prevention (DLP) policy for this configuration. Exchange auto-labeling policies evaluate messages in transit as they're sent or received; they don't evaluate existing messages st
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot in Teams meetings
**URL:** https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new |
| https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models |
| https://learn.microsoft.com/microsoft-365/copilot/discovery-setting-ai-experiences | https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences |
| https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits | https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits |
| https://learn.microsoft.com/microsoft-scout/overview | https://learn.microsoft.com/en-us/microsoft-scout/overview |
| https://learn.microsoft.com/microsoft-scout/get-started | https://learn.microsoft.com/en-us/microsoft-scout/get-started |
| https://learn.microsoft.com/microsoft-scout/admin-access-overview | https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview |
| https://learn.microsoft.com/microsoft-scout/admin-intune-setup | https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup |
| https://learn.microsoft.com/microsoft-scout/manage-group-policy | https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy |
| https://learn.microsoft.com/microsoft-scout/use-microsoft-scout | https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout |
| https://learn.microsoft.com/microsoft-scout/faq | https://learn.microsoft.com/en-us/microsoft-scout/faq |
| https://learn.microsoft.com/microsoft-scout/microsoft-scout-responsible-ai-overview | https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview |
| https://learn.microsoft.com/microsoft-scout/microsoft-scout-responsible-ai-faq | https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq |
| https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms |
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*