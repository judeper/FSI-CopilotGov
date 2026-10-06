# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-06
**Run Time:** 2026-10-06T16:23:43.531942+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| HIGH Changes | 1 |
| MEDIUM Changes | 1 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | MEDIUM | 1.1, 1.9, 2.15, 1.4 | Update portal-walkthrough |
| 2 | dlp-policy-reference | HIGH | None | Review and update |
| 3 | ...osoft365-copilot-location-learn-about | HIGH | 1.5, 2.6, 2.1 | Update portal-walkthrough |
| 4 | audit-log-activities | HIGH | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

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
--- +++ @@ -155,7 +155,7 @@ Copilot integrations can fail when a network perimeter blocks WSS, a network device performs Transport Layer Security inspection that interferes with the connection, or a proxy enforces aggressive connection timeouts.
 Work with the teams that manage network security, proxies, firewalls, secure web gateways, or SSE/SASE services to allow the required traffic. You can test connectivity to the
 *.cloud.microsoft
-domain by using either the
+domain by using the
 connectivity test for the Copilot app
 . You can also use the
 Microsoft 365 connectivity test tool

```

---

### 2. DLP for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.6/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.6/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -172,6 +172,72 @@ When a user prompts Copilot to summarize their inbox or reason over recent email, external emails are excluded from grounding. Copilot returns a response based on internal email and other permitted Microsoft 365 sources, and the user sees a message that some content was excluded by an organizational policy.
 Files uploaded in prompts
 You can upload files when you craft a prompt for Microsoft 365 Copilot to analyze. DLP can't scan the contents of files that you upload directly into prompts, so evaluation of the uploaded file for sensitive data doesn't occur. DLP only checks the text you type into the prompt itself.
+Supported conditions and actions
+The
+Microsoft 365 Copilot and Copilot Chat
+policy location supports the following conditions and actions:
+Conditions
+Supported policy actions
+Description
+Content contains
+>
+Sensitivity labels
+Prevent Copilot from processing content
+Detects when a file or an email in Exchange has a chosen sensitivity label. Copilot and Cowork don't process the content of the item or use it in the response summary, but the item could be available in the citations of the response.
+Content contains
+>
+Sensitive information types
+Prevent Copilot from processing content
+>
+Processing prompts
+Detects when the text entered directly into a Copilot or Cowork prompt contains chosen sensitive information types. The experience doesn't respond to the prompt. The prompt isn't used for internal or web searches.
+Content contains
+>
+Sensitive information types
+Prevent Copilot from processing content
+>
+Performing Web Searches
+Detects when the text entered directly into a Copilot or Cowork prompt contains chosen sensitive information types. The experience blocks the use of external web search as a grounding source for that prompt.
+Email is received from
+>
+External users
+Prevent Copilot from processing content
+Detects when an email was received from a sender outside your organization's accepted domains. 
```

---

### 3. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (UI element names)

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
--- +++ @@ -1311,6 +1311,9 @@ Create the cross tenant auth mapping
 CreateCrossTenantAuthMapping
 Create a user mapping for the cross tenant auth feature.
+Created Artifact Definition
+CreatedArtifactDefinition
+Created Artifact Definition is a Fabric External Sources activity which is generated when an External Sources artifact definition is created. Shared across item types: for MirroredStorage it carries SourceType and ConnectionId; for AWS Databricks Catalog it carries CatalogName, WorkspaceConnectionId, and MirroringMode.
 Created AWS Databricks Catalog
 CreatedAWSDatabricksCatalog
 Created AWS Databricks Catalog is an AWSDatabricksCatalog activity which is generated when a Fabric AWS Databricks Catalog item is created, capturing the bound AWS Databricks workspace ConnectionId and the initial MirroredScope (catalogs/schemas/tables selected for mirroring).
@@ -1479,6 +1482,9 @@ Updated authorization setting in GraphQL
 UpdatedAuthorizationSettingGraphQL
 Updated authorization setting in GraphQL.
+Updated Artifact Definition
+UpdatedArtifactDefinition
+Updated Artifact Definition is a Fabric External Sources activity which is generated when an External Sources artifact definition is updated via the update-item-definition API. Shared across item types (e.g. MirroredStorage, AWS Databricks Catalog); the properties carried depend on the item type.
 Updated AWS Databricks Catalog Definition
 UpdatedAWSDatabricksCatalogDefinition
 Updated AWS Databricks Catalog definition is an AWSDatabricksCatalog activity which is generated when the item's Databricks workspace connection or mirrored scope (catalogs/schemas/tables) is updated via the update-item-definition API.

```

---

## HIGH: Control Review Recommended

### 1. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**What Changed:**
```diff
--- +++ @@ -2809,17 +2809,21 @@ Block everyone
 to block internal users.
 Learn more URL
-Users may want to learn why their activity is being blocked. You can configure a site or a page that explains more about your policies. When you select
-Provide a compliance URL for the end user to learn more about your organization's policies (only available for Exchange)
-, and the user receives a policy tip notification in Outlook Win32, the
+Users may want to learn why their activity is being blocked. You can configure a site or a page that explains more about your policies. In the rule's user notification settings, select
+Provide a compliance URL for the end user to learn more about your organization's policies
+, and then enter the URL.
+For Outlook Win32, the
 Learn more
-link points to the site URL that you provide. This URL has priority over the global compliance URL configured with
-Set-PolicyConfig -ComplainceURL
+link in the policy tip points to the site URL that you provide. This URL has priority over the global compliance URL configured with
+Set-PolicyConfig -ComplianceURL
+.
+For Microsoft Copilot and Copilot Chat, the
+Learn about access restrictions
+link in the standard block message points to the URL that you provide. Only the link destination changes; the message text and enforcement action remain unchanged. For more information, see
+Customize the link in Copilot policy tips
 .
 Important
-You must configure the site or page that
-Learn more
-points to from scratch. Microsoft Purview doesn't provide this functionality out of the box.
+You must configure the site or page that the link points to from scratch. Microsoft Purview doesn't provide this functionality out of the box.
 User overrides
 The intent of
 User overrides

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot requirements
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
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