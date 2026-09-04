# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-03
**Run Time:** 2026-09-03T13:59:25.015433+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| HIGH Changes | 1 |
| MEDIUM Changes | 1 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | connect-to-ai-subprocessor | HIGH | 1.10, 2.7, 3.8a | Update portal-walkthrough |
| 2 | dlp-learn-about-dlp | HIGH | 3.10 | Update portal-walkthrough |
| 3 | dlp-policy-reference | HIGH | None | Review and update |
| 4 | apply-sensitivity-label-automatically | MEDIUM | 1.5, 2.2 | Update portal-walkthrough |
| 5 | cowork-admin-governance | CRITICAL | 4.15 | Update portal-walkthrough |
| 6 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -116,7 +116,7 @@ Some features are only available when Anthropic models are enabled. If you turn off Anthropic as a subprocessor, certain features may no longer be accessible.
 Anthropic Fable-class models
 Certain Anthropic models, such as Fable 5.0 and Fable 5.1, may be made available to your organization with different or additional terms (âFable-class modelsâ).
-Depending on your organizationâs eligibility, some Fable-class models may be available to your organization with Anthropic acting as a subprocessor. For example, for certain organizations, Fable 5.1 is available with Anthropic acting as a subprocessor and Microsoft's Product Terms and Data Protection Addendum (DPA) apply. For these organizations, no additional terms apply and, as long as your organization has enabled Anthropic models under the
+Depending on your organizationâs eligibility, some Fable-class models may be available to your organization with Anthropic acting as a subprocessor. For example, for certain organizations, Fable 5.1 is available with Anthropic acting as a subprocessor and Microsoft's Product Terms and Data Protection Addendum (DPA) apply. For these organizations, no additional terms apply, and Anthropic doesn't retain customer content (including prompts and responses). As long as your organization has enabled Anthropic models under the
 AI providers operating as Microsoft subprocessors
 setting in the Microsoft 365 admin center, no other opt-in is required. Contact your account team if you have questions about your organizationâs eligibility.
 Other Fable-class models may be provided as âAnthropic models with Data Retentionâ and require your organization to agree to Anthropicâs terms as described in the next section.

```

---

### 2. Learn about DLP

**URL:** https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.10: Control 3.10: SEC Reg S-P -- Privacy of Consumer Financial Information
  - File: `controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/3.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.10/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -306,7 +306,7 @@ Alerts in DLP policies
 : Describes alerts in the context of a DLP policy.
 Get started with data loss prevention alerts
-: Covers the necessary liscensing, permissions, and prerequisites for DLP alerts and alert reference details.
+: Covers the necessary licensing, permissions, and prerequisites for DLP alerts and alert reference details.
 Create and deploy data loss prevention policies
 : Includes guidance on alert configuration in the context of creating a DLP policy.
 Learn about investigating data loss prevention alerts

```

---

### 3. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
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
--- +++ @@ -1037,6 +1037,21 @@ above.
 Monitoring your auto-labeling policy
 After your auto-labeling policy is turned on, you can view the labeling progress for files in your chosen SharePoint and OneDrive locations. Emails aren't included in the labeling progress because they're automatically labeled as they're sent.
+Note
+Exchange email isn't included in policy-level labeling progress,
+Insights
+enforcement metrics, or the
+Labeled items
+view. These views report on files in SharePoint and OneDrive.
+To verify labeling for an Exchange email, use
+Activity explorer
+and filter for the
+Sensitivity label applied
+activity. Narrow the results by date, sensitivity label, location, and item details, and review
+How applied
+to verify that the label was applied automatically. Allow
+60 to 90 minutes for the activity to appear
+. Activity explorer identifies the resulting label and how it was applied, but doesn't identify the specific auto-labeling policy or rule that applied the label to an Exchange message.
 The labeling progress includes the files to be labeled or unlabeled by the policy, the affected files for the last seven days, and the total files affected. Because of the maximum of labeling 100,000 files a day, this information provides you with visibility into the current labeling progress for your policy and how many files are still to be labeled.
 When you first turn on your policy, you initially see a value of 0 for files to be labeled until the latest data is retrieved. This progress information updates every 48 hours, so you can expect to see the most current data about every other day. When you select an auto-labeling policy, you can see more details about the policy in a flyout pane, which includes the labeling progress by the top 10 sites. The information on this flyout pane might be more current than the aggregated policy information displayed on the
 Auto-labeling
@@ -1054,6 +1069,7 @@ and
 Information Protection Investigators
 role groups let you s
```

---

### 4. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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
--- +++ @@ -24,11 +24,6 @@ Summarize this article for me
 Learn how to manage plugins, models, browser use, security and compliance, and usage-based billing in Copilot Cowork.
 Note
-Copilot Cowork is now generally available and is no longer managed in the Microsoft 365 admin center by selecting
-All Agents
->
-Cowork
-in the left navigation menu. The agent-based access control that was available in the Preview version isn't used to manage user access.
 Cowork is now an
 agentic system
 (different from an
@@ -42,6 +37,58 @@ from the dropdown menu to the right.
 Allow access to Cowork
 To allow users to access Cowork, admins must enable usage-based billing. To learn how to set up and enable usage-based billing, see
+Managing AI experiences enabled by usage-based billing
+.
+Important
+A spending policy is an access control, not only a budget. Any user in the scope of a spending policy that selects Cowork can use Cowork, regardless of how small the credit limit is. A policy with a limit of one credit still grants access. A very low limit doesn't prevent access; users can still open Cowork and start work until the limit is reached. To keep a user out of Cowork, don't include them in any spending policy that selects Cowork, rather than lowering their limit. For how access is determined across policies, discovery, and model settings, see
+How access to Copilot Cowork is determined
+.
+Important
+The agent-based access control from the Frontier and Preview versions is deprecated for access control. Copilot Cowork is generally available and is no longer managed by selecting
+All Agents
+>
+Cowork
+in the Microsoft 365 admin center. The
+Cowork
+agent entry is still visible under
+Agents
+>
+All Agents
+, but any configuration on it has no effect on who can use Cowork. Access is granted only through a spending policy that selects Cowork.
+Migrating from Frontier or Preview access control
+If you managed Cowork access during the Frontier or Preview program, the control you u
```

---

### 5. Copilot Cowork available models

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
**Section:** Copilot Cowork
**Classification:** HIGH (Portal references)

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
--- +++ @@ -69,17 +69,21 @@ Anthropic subprocessor
 Claude Fable 5 (Preview)
 For your toughest, most demanding challenges.
-In preview and off by default. An admin must turn it on in the Microsoft 365 admin center under Copilot settings before it appears in your picker. Requires data retention. When you select Fable 5, your prompts and responses are retained by the model provider, and Cowork shows a banner while it's selected. More information:
+In preview and off by default. An admin must turn it on in the Microsoft 365 admin center under Copilot settings before it appears in your picker. Requires data retention. When you select Fable 5, the model provider retains your prompts and responses, and Cowork shows a banner while it's selected. More information:
 Data retention
 and
 Anthropic subprocessor
+1
+The models in your picker reflect what your organization makes available to you. State which populations the GPT 5.5 (Frontier) model is available to before publishing. If it's available only to Copilot Cowork Frontier program tenants, say so.
+Note
+Confirm the GPT 5.5 (Frontier) availability statement and the definition of the "(Frontier)" qualifier before this page is published.
 How model choice affects responses
 Changing the model can affect response speed, response depth, and output style. Some models are optimized for faster drafting, while others spend more time on reasoning and review.
 Cowork shows a model badge in the conversation so you can see which model produced a response.
 Data retention
 Some models, such as
 Claude Fable 5 (Preview)
-(off by default), require data retention. When you select a model that requires data retention, your prompts and responses for that model are retained by the model provider rather than following Cowork's default no-retention posture. Cowork indicates this in two ways:
+(off by default), require data retention. When you select a model that requires data retention, the model provider retains your prompts and responses
```

---

## HIGH: Control Review Recommended

### 1. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**What Changed:**
```diff
--- +++ @@ -2944,7 +2944,7 @@ Alerts in DLP policies
 : Describes alerts in the context of a DLP policy.
 Get started with data loss prevention alerts
-: Covers the necessary liscensing, permissions, and prerequisites for DLP alerts and alert reference details.
+: Covers the necessary licensing, permissions, and prerequisites for DLP alerts and alert reference details.
 Create and deploy data loss prevention policies
 : Includes guidance on alert configuration in the context of creating a DLP policy.
 Learn about investigating data loss prevention alerts

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Apply sensitivity labels automatically
**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
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