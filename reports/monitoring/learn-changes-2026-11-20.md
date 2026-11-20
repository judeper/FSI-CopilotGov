# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-20
**Run Time:** 2026-11-20T18:08:31.741452+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| MEDIUM Changes | 7 |
| Redirects | 44 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | dlp-policy-reference | MEDIUM | None | Review optional |
| 2 | ...t.com/en-us/microsoft-copilot-studio/ | HIGH | 2.14, 4.14 | Update portal-walkthrough |
| 3 | agent-extend-action-mcp | MEDIUM | None | Review optional |
| 4 | mcp-add-existing-server-to-agent | MEDIUM | None | Review optional |
| 5 | authoring-select-agent-model | MEDIUM | 1.16, 4.14 | Update portal-walkthrough |
| 6 | advanced-management | MEDIUM | 1.7, 2.5 | Update portal-walkthrough |
| 7 | ...opilot-sharepoint-advanced-management | CRITICAL | 1.13, 1.3 | Update portal-walkthrough |
| 8 | data-access-governance-reports | MEDIUM | 1.14, 1.1, 1.7, 1.15, 2.5 | Update portal-walkthrough |
| 9 | copilot-in-sharepoint-get-started | CRITICAL | None | Monitor |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft Copilot Studio documentation

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -96,7 +96,9 @@ Agents hub on Learn
 Explore Microsoft's agent ecosystem, learn key concepts, and find resources to plan, build, adopt, and continuously improve AI agents for your organization.
 Microsoft Copilot hub
-Explore resources for delivering Microsoft Copilot services, including find documentation for Copilot Cowork and Copilot Code (preview).
+Explore resources for delivering Microsoft Copilot services, including find documentation for Copilot Cowork, Copilot Code (Frontier), and Autopilot (Frontier).
+Microsoft Plugins hub
+Build and manage Microsoft Copilot plugins. Bring agents, skills, MCP servers, and connectors together to help get work done.
 Microsoft Copilot extensibility
 Customize Microsoft Copilot with agents and use actions and connectors to extend Copilot's skills and knowledge.
 Microsoft 365 Agents SDK

```

---

### 2. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -380,6 +380,9 @@ For Federal Risk and Authorization Management Program (FedRAMP) tenants and for environments outside the United States where cross-geo data movement is restricted, GPT-4.1 and GPT-5 will remain supported and won't retire as part of this migration. Learn more about availability and eligibility in
 Move data across regions for Copilots, AI agents, and generative AI features
 .
+If your agent uses the
+GPT Chat Latest
+alias, or is part of a managed solution whose model can't be edited, Copilot Studio automatically moves the agent's traffic to the alias's current underlying model or the environment's default model when a model retires. You don't need to republish the agent for this change to take effect.
 Limitations of experimental and preview models
 You can explore and test experimental and preview models, but don't use them for production:
 They might show variability in performance, response quality, latency, or message consumption, and might time out or be unavailable.

```

---

### 3. SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/advanced-management
**Section:** SharePoint Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`

**Affected Playbooks:**
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
--- +++ @@ -53,8 +53,8 @@ : Identify sites that might contain overshared or sensitive content. AI insights can be generated from DAG reports to highlight access risk patterns and recommend next steps. You can also initiate site access reviews from a DAG report. DAG reports include:
 Permission state reports for sites, OneDrive sites, and files
 : Use this report to get a snapshot of your organization's current permission structure across all SharePoint and OneDrive sites, helping you understand how broadly your data is exposed and identify potential oversharing risks.
-Site permissions for a given user report
-: Use this report to get a list of all the sites a user can access and how access is granted.
+Site permissions for users or groups report
+: Use this report to list all sites accessible to a user, Microsoft 365 group, or Microsoft Entra security group and review the extent of access.
 Sensitivity label snapshot report
 : Use this report to get a snapshot of sensitivity label distribution across all SharePoint and OneDrive sites.
 Sharing links activity reports

```

---

### 4. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,32 +1,268 @@-Secure and govern Microsoft Copilot: Foundational deployment guidance
-Microsoft Copilot can accelerate how people find information, summarize content, and get work done by grounding responses in the data users already have permission to access. To realize that value confidently, organizations require a foundation that is both secure and well-governed, with robust safeguards in place, including measures to protect interactions when using Copilot and meeting AI regulatory standards.
-How this blueprint can help you secure and govern Microsoft Copilot
-This deployment blueprint outlines the essential steps for establishing a secure and governed foundation for Copilot by remediating oversharing, implementing reliable guardrails, and fulfilling AI-related regulatory obligations, delivering a straightforward, approachable path to help every organization get started with confidence.
-This blueprint is organized into three pillars:
-Remediate oversharing
-Set up guardrails
-Meet regulations
-https://aka.ms/Copilot/SecureGovernBlueprintPDF
-What the blueprint covers
-The blueprint covers the following areas:
-A practical framework to reduce Copilot exposure quickly, then harden your environment with enforceable defaults
-Guidance powered by:
-Microsoft Purview
-, which enables a secure and governed Copilot deployment by providing tools to prevent data loss, mitigate insider risk, and ensure compliance with organizational and regulatory requirements, for both Copilot at runtime and Microsoft 365 data referenced by Copilot
+Get ready for Microsoft Copilot and agents with SharePoint Advanced Management
+Microsoft Copilot and agents work best for your organization when your content is up to date and well governed. Copilot and agents retrieve data from Microsoft Graph and respect existing permissions, sharing settings, and policies.
+This article describes how to prepare your environment for Copilot and agent usage by using capabilities in
 SharePoint 
```

---

### 5. Data access governance reports

**URL:** https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports
**Section:** SharePoint Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.14: Control 1.14: Item-Level Permission Scanning
  - File: `controls/pillar-1-readiness/1.14-item-level-permission-scanning.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
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
--- +++ @@ -20,6 +20,7 @@ Snapshot reports
 Site permissions across your organization
 (Recommended)
+Site permissions for users or groups
 Sensitivity label applied to files
 Activity reports
 Sharing links
@@ -33,8 +34,8 @@ Currently, three types of snapshot reports are available:
 Site permissions report
 : Provides a comprehensive snapshot of the permission structure across all SharePoint and OneDrive sites. It helps you identify sites with the broadest user access, such as sites with thousands of users, external guests, or "Everyone except external users" permissions.
-Site permissions for users report
-: Lists all sites a specified user can access. Admins can use this report to determine whether the user can access the entire site or specific sections, granted directly to the user or indirectly through groups.
+Site permissions for users or groups report
+: Lists all sites a specified user or group can access and the extent of that access. Each report contains either users or groups, not both.
 Sensitivity label for files report
 : Identifies SharePoint sites containing files with specific sensitivity labels applied. You can use this report to verify that appropriate security policies are in place for your most sensitive content.
 What are activity reports?
@@ -66,10 +67,11 @@ Learn how to create and use the
 site permissions for your organization report
 .
-What is the site permissions for users report?
-The site permissions for users report is the next snapshot report that provides a comprehensive view into permissions of the specified users across all SharePoint and OneDrive sites. This report lists all sites a user can access and allows admins to determine whether they can access the entire site or specific sections, granted directly to the user or indirectly through groups. This approach helps you quickly assess your overall security posture and identify sites that need immediate attention.
+What is the site permissions for users or groups report?
+The si
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. DLP policy reference
**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Classification:** MEDIUM (General content update)

---

### 2. Model Context Protocol in Copilot Studio
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
**Classification:** MEDIUM (General content update)

---

### 3. Connect an existing MCP server to an agent
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent
**Classification:** MEDIUM (General content update)

---

### 4. Select an agent model
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Classification:** MEDIUM (General content update)

---

### 5. SharePoint Advanced Management
**URL:** https://learn.microsoft.com/en-us/sharepoint/advanced-management
**Classification:** MEDIUM (General content update)

---

### 6. Data access governance reports
**URL:** https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports
**Classification:** MEDIUM (General content update)

---

### 7. Copilot in SharePoint (preview)
**URL:** https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-get-started
**Classification:** CRITICAL (Deprecation notice)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/copilot/plan/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access | https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/copilot/plan/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy | https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access | https://learn.microsoft.com/en-us/copilot/implement/copilot-ai-provider-user-sec-group-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences | https://learn.microsoft.com/en-us/copilot/implement/discovery-setting-ai-experiences |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits | https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/copilot-managed-runtime/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json | https://learn.microsoft.com/en-us/plugins/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent | https://learn.microsoft.com/en-us/plugins/overview-declarative-agent |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents | https://learn.microsoft.com/en-us/plugins/agent-builder-build-agents |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge | https://learn.microsoft.com/en-us/plugins/agent-builder-add-knowledge |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder | https://learn.microsoft.com/en-us/plugins/agent-builder |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/knowledge-sources | https://learn.microsoft.com/en-us/plugins/knowledge-sources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites#agent-capabilities-and-licensing-models | https://learn.microsoft.com/en-us/plugins/prerequisites#agent-capabilities-and-licensing-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/code-interpreter | https://learn.microsoft.com/en-us/plugins/code-interpreter |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/image-generator | https://learn.microsoft.com/en-us/plugins/image-generator |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide | https://learn.microsoft.com/en-us/copilot/manage/copilot-tuning-admin-guide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/plugins/overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security | https://learn.microsoft.com/en-us/plugins/data-privacy-security |
| https://learn.microsoft.com/en-us/entra/agent-id/configure-third-party-agents | https://learn.microsoft.com/en-us/entra/agent-id/choose-agent-integration-path |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/SharePoint/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*