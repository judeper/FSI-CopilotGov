# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-04
**Run Time:** 2026-09-04T13:52:34.132527+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | HIGH | 4.12 | Update portal-walkthrough |
| 2 | agent-settings | HIGH | 4.13, 2.13, 2.14, 1.13 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

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
--- +++ @@ -689,13 +689,13 @@ Copilot now displays rich images from files and meetings directly within responses to improve comprehension.
 Details:
 What changed:
-Previously, Copilot responses included text only. Now, it surfaces relevant images inline from files and meetings to provide visual context. This enhancement supports richer content formats while maintaining data security and compliance with Microsoft 365 policies.
+Previously, Copilot responses included text only. Now, it surfaces relevant images inline from files and meetings to provide visual context. This enhancement supports richer content formats while maintaining data security and compliance with Microsoft 365 policies. This applies to Microsoft 365 Copilot licenses only.
 Why:
 Visual information helps users understand complex content faster and reduces the need to switch between apps or documents.
 Try this:
 Ask Copilot a question related to your meeting notes or documents.
 Review the inline images that appear alongside the text response.
-Click images to open the source file or meeting contenvt for more details.
+Click images to open the source file or meeting content for more details.
 Why this matters:
 Including images directly in responses helps users grasp information quickly and reduces context switching.
 Business impact:
@@ -4093,13 +4093,13 @@ Copilot now displays rich images from files and meetings directly within responses to improve comprehension.
 Details:
 What changed:
-Previously, Copilot responses included text only. Now, it surfaces relevant images inline from files and meetings to provide visual context. This enhancement supports richer content formats while maintaining data security and compliance with Microsoft 365 policies.
+Previously, Copilot responses included text only. Now, it surfaces relevant images inline from files and meetings to provide visual context. This enhancement supports richer content formats while maintaining data security and compliance with Microsof
```

---

### 2. Agent settings in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -53,11 +53,12 @@ Review impacted agents before running the rule
 Apply governance actions across affected agents in bulk
 This experience helps organizations maintain compliance, ownership accountability, and deployment consistency across agents while keeping administrators in the control loop.
-Supported Rule-Based Bulk Actions
+Supported rule-based bulk actions
 Agent management rules currently support the following governance scenarios:
 Install Microsoft agents
 Reassign ownerless agents created with Agent Builder to manager
 Block ownerless agents without usage
+Apply a template to agents
 Reject agent publish requests older than a specified number of days
 Install Microsoft agents
 Microsoft first-party (1P) agents are consistently among the most installed and widely used agents. However, administrators currently lack a scalable way to install these agents proactively across their tenant.
@@ -80,6 +81,32 @@ Transfer ownership by using a bulk reassignment action to the manager of the previous owner based on Microsoft Entra ID hierarchy
 Block ownerless agents without usage
 Admins can create a custom rule to block multiple ownerless agents that have no usage.
+Apply a template
+Use the
+Apply template
+action in an agent management rule to apply security policies to existing agents. This action helps you apply policies at scale after agents are published instead of applying policies to each agent individually.
+When you create the rule, define conditions that identify the agent instances you want to manage. The rule evaluates agents in the registry that have an agent identity. It doesn't apply to agent blueprints or AI teammates.
+To apply a template:
+In the Microsoft 365 admin center, go to
+Agents
+>
+Settings
+>
+Agent management rules
+, and then select
+Add rule
+.
+Select
+Apply template
+as the rule action.
+Define the applicable criteria that determine which agent instances the rule applies to.
+Choose a preexisting template, or select polic
```

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