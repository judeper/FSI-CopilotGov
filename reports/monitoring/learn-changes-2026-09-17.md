# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-17
**Run Time:** 2026-09-17T14:32:09.590164+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| HIGH Changes | 1 |
| MEDIUM Changes | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | HIGH | 4.12 | Update portal-walkthrough |
| 2 | dlp-learn-about-dlp | HIGH | 3.10 | Update portal-walkthrough |
| 3 | audit-log-activities | MEDIUM | 3.1, 2.2, 2.13, 1.15 | Update portal-walkthrough |
| 4 | connected-platforms | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
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
--- +++ @@ -37,6 +37,12 @@ for data governance solutions.
 Roadmap
 for data security and risk and compliance solutions.
+September 2026
+Data Loss Prevention
+General availability
+: Integrate Microsoft Entra Global Secure Access with Purview to protect text, files, and AI interactions at the network layer, enforce restrictive actions based on DLP policies, and detect risky user activity through Insider Risk Management. It helps prevent sensitive data from being shared with untrusted cloud applications through browsers, apps, APIs, and add-ins, including generative AI platforms, social media, and collaborative platforms. See
+Learn about Microsoft Purview Network Data Security
+.
 August 2026
 Data Governance
 Updated

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
--- +++ @@ -34,16 +34,17 @@ and
 Inline web traffic
 data. DLP policies act on a variety of locations, methods of data transmission, and types of user activities.
-DLP uses deep content analysisânot a simple text scan. It analyzes content:
+DLP uses deep content analysis - not a simple text scan. It analyzes content:
 For primary data matches to keywords
 By the evaluation of regular expressions
 By internal function validation
 By secondary data matches that are in proximity to the primary data match
-DLP also uses machine learning algorithms and other methods to detect content that matches your DLP policies
-Inline by
+Using machine learning algorithms and other methods to detect content that matches your DLP policies
+Inline through
 Microsoft Edge for business
-for Windows devices that haven't been onboarded into Microsoft Purview (preview) and
-Use Network Data Security to help prevent sharing sensitive information with unmanaged AI (preview)
+for Windows devices that haven't been onboarded into Microsoft Purview
+Microsoft Purview network data security
+via SASE and non-Microsoft secure enterprise browser integrations.
 Enterprise applications and devices
 DLP monitors and protects against oversharing in enterprise apps and on devices. It targets Microsoft 365 locations, like Exchange and SharePoint, and locations you add, like on-premises file shares, endpoint devices, and non-Microsoft cloud apps. These locations and sources include:
 Microsoft 365 services, like Exchange, SharePoint, OneDrive accounts, and Teams chat and channel messages.
@@ -63,10 +64,10 @@ collection policies
 , monitors and protects against oversharing to
 Unmanaged cloud apps
-by targeting data transmitted on your network and in Microsoft Edge for Business.
-Create policies that target Inline web traffic (preview)
-and
-Network activity (preview)
+by targeting data transmitted on your network and in Microsoft Edge for Business. Use
+Data Loss Prevention for Cloud Apps in Edge for Busi
```

---

### 3. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
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
--- +++ @@ -1394,6 +1394,9 @@ Get on-demand billing quota
 GetOnDemandBillingQuota
 Generated when the On-demand billing experience loads and the subscription-level on-demand billing quota usage and limits are retrieved.
+Get Capacity Overage Config. This can happen via Public API or using UX.
+GetCapacityOverageBillingConfiguration
+Get Capacity Overage Config. This can happen via Public API or using UX.
 Git connection settings updated
 GitConnectionSettingsUpdated
 Git connection settings updated.
@@ -1484,6 +1487,9 @@ Update on-demand billing limits
 UpdateOnDemandBillingLimits
 Generated when a capacity admin enables or disables a billing category, or changes its 24-hour compute limit, on a Fabric capacity. One audit event is emitted per billing category.
+Update Capacity Overage Config. This can happen via Public API or using UX.
+UpdateCapacityOverageBillingConfiguration
+Update Capacity Overage Config. This can happen via Public API or using UX.
 Updated a Fabric Copilot session
 FabricCopilotSessionUpdated
 A user updated a Fabric Copilot session.

```

---

## HIGH: Control Review Recommended

### 1. Microsoft Agent 365 registry sync

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms
**Section:** Agent Governance
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -93,6 +93,7 @@ Databricks Genie
 Anthropic Claude Managed Agents
 Oracle Generative AI Agents
+Snowflake Cortex
 Note
 Microsoft product teams are actively working to expand support to more platforms. Check back frequently to learn about new platform integrations.
 Authentication requirements
@@ -130,6 +131,8 @@ bedrock-agentcore:DeleteGateway
 bedrock-agentcore:DeleteGatewayTarget
 bedrock-agentcore:DeleteMemory
+bedrock-agentcore:DeleteWorkloadIdentity
+bedrock-agentcore:DeleteAgentRuntimeEndpoint
 Create a new access key.
 For more information about creating an access and secret key, see
 Amazon Bedrock
@@ -478,6 +481,19 @@ delete statements in Option B to make the account read-only.
 Note
 Only active OCI Generative AI agents are synced.
+Snowflake Cortex
+To set up a connection to Snowflake Cortex in Connected platforms, provide the following information:
+Account identifier
+: In the Snowflake app, select
+View Account Details
+in the lower-left corner to find the account identifier.
+Database and schema
+: Enter the database and schema where you created the agents. For more information about creating agents, see
+Snowflake Cortex Agents
+.
+Connected platforms uses RSA key-pair authentication to connect to Snowflake. Configure key-pair authentication for the Snowflake user before you create the connection. For more information, see
+Key-pair authentication and key-pair rotation
+.
 Feedback
 Was this page helpful?
 Yes

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*