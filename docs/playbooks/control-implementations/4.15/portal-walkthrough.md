# Control 4.15: Copilot Cowork Governance - Portal Walkthrough

Step-by-step admin-center workflow for governing Microsoft 365 Copilot Cowork after its June 2026 general availability: scoping access through spending policies, controlling the discovery setting, governing model controls and provider-retention review, reviewing the local browser-use toggle, governing plugins and the Customize page (skills and uploaded plugin packages), setting consumption limits, and confirming Purview and audit coverage. This playbook governs Cowork's tenant configuration surfaces; broader admin settings (Control 4.1) and extensibility (Control 4.13) remain owned by their respective controls.

## Prerequisites

- [Control 4.1 Admin Settings and Feature Management](../../../controls/pillar-4-operations/4.1-admin-settings-feature-management.md) baseline is documented.
- [Control 4.13 Extensibility Governance](../../../controls/pillar-4-operations/4.13-extensibility-governance.md) governs plugins, connectors, and uploaded plugin packages that extend Cowork.
- An approved pilot security group exists for phased rollout.
- The tenant's usage-based billing (Copilot Credits) posture has been approved by finance, and a spending policy is in place.
- A documented governance register and evidence repository are in place, per [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md).

> **Important:** Cowork is generally available as of June 2026. Microsoft Learn now states that local browser use moved from Frontier to general availability in August 2026, while other features and model names continue to change quickly. Re-verify each step against current Microsoft documentation before relying on it in production governance.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft 365 admin center | Copilot > Cost management > Configuration | Configures usage-based billing scope, spending policies, and per-user or per-group consumption limits for Cowork |
| Microsoft 365 admin center | Copilot > Settings > AI experiences enabled by usage-based billing | Toggles tenant-wide discovery for usage-based experiences including Cowork |
| Microsoft 365 admin center | Copilot settings > Anthropic model family and current model controls | Governs third-party model availability and provider data-retention review |
| Microsoft 365 admin center | Copilot > Settings > View All > Cowork settings > Allow browser access | Governs the **Cowork Browsing** tenant toggle for local Microsoft Edge browser use |
| Microsoft 365 admin center | Integrated apps / plugin availability controls | Governs Microsoft and partner plugin availability, deployment, and connector authentication |
| Cowork (web) | Customize > Plugins and Customize > Skills | Governs uploaded plugin packages, user-created and uploaded custom skills, and sharing scope |
| Microsoft Purview portal | Copilot governance surfaces per the Purview for Cowork guidance | Provides the capabilities currently documented for Cowork AI interactions, including audit, sensitivity labels, insider risk, communication compliance, eDiscovery, and data lifecycle management; verify DLP rollout separately |
| Microsoft Purview portal | Audit | Captures unified-audit-log events including Cowork browser tasks |
| Governance evidence repository | Workspace of record | Stores access-posture decisions, model-toggle decisions, browser-toggle decisions, plugin/skill inventory, consumption limits, and approvals |

## Steps

### Step 1: Confirm the access posture (billing + discovery)

In **M365 Admin Center > Copilot > Cost management > Configuration**, record which users or groups have a spending policy that selects Cowork and confirm the spending policy. Then in **M365 Admin Center > Copilot > Settings > AI experiences enabled by usage-based billing**, record whether discovery is on. The recommended pilot posture is a Cowork-selecting spending policy scoped only to the approved pilot group with tenant-wide discovery **off**, so Cowork is not surfaced to users outside the pilot. Capture the decision, approver, and pilot scope in the register.

### Step 2: Handle access requests deliberately

If discovery is on and a user does not have billing enabled, the user can submit an access request in the app. Establish a documented workflow so that requests are reviewed against policy, cost, and compliance before an admin enables billing for the requester. Record the reviewer and outcome for each request.

### Step 3: Govern model toggles

In **M365 Admin Center > Copilot settings**, record the current state and scope of the **Anthropic model family** control and any model-specific controls visible in the tenant. Current Microsoft Learn model names include Claude Fable 5.1 and direct admins to Anthropic data-retention guidance; do not rely on stale model names or assume the same defaults in every tenant. Leave any model with provider-retention implications disabled for regulated data unless legal, privacy, and compliance have reviewed the retention terms and approved the use. If the Anthropic family is disabled per policy, coordinate with the pilot on which models remain available for their tasks.

### Step 4: Govern the Cowork Browsing tenant toggle

Navigate to **M365 Admin Center > Copilot > Settings > View All > Cowork settings > Allow browser access**. Leave "Allow Cowork to use the Microsoft Edge browser to perform tasks on behalf of users" unchecked until browser use is reviewed. Because browser tasks run in the user's local Microsoft Edge and inherit Conditional Access, Microsoft Purview DLP, browser management policy, and site allow/block/view-only rules, confirm those policies are in the intended state before enabling the toggle. Microsoft Learn states local browser use moved from Frontier to general availability in August 2026; still verify tenant toggle, Edge policy, Conditional Access, DLP, and audit behavior before regulated use.

### Step 5: Govern plugins and the Customize page

Review the plugins available to Cowork through the admin plugin controls, including Microsoft plugins (for example, Dynamics 365 Customer Service, Sales, ERP, Fabric IQ) and partner connectors (for example, Jira, Salesforce, ServiceNow, SAP ERP, Workday HCM, Zendesk). Coordinate with Control 4.13 on the Cowork **Customize** page: govern uploaded plugin packages, user-created and uploaded custom skills (`.md`, `.zip`, `.skill`), and the sharing scope for each. Maintain an approved inventory and confirm connector authentication for any Dynamics 365 / Agent 365 integrations.

### Step 6: Set consumption limits and monitor spend

In **Copilot > Cost management > Configuration**, set per-user or per-group consumption limits sized to the pilot's approved budget. Cowork consumption includes model responses, tool/skill calls, image generation, and browser tasks — reflect all four in the review. Establish a review cadence so consumption growth is visible before month-end and before threshold breaches.

### Step 7: Confirm Purview, audit, and supervision coverage

Confirm Cowork is included in the tenant's Purview posture per the [Use Microsoft Purview to manage data security & compliance for Copilot Cowork](https://learn.microsoft.com/en-us/purview/ai-copilot-cowork) guidance (the capabilities currently listed for Cowork AI interactions, including audit, sensitivity labels, insider risk, communication compliance, eDiscovery, and data lifecycle management). Confirm that browser task events appear in the unified audit log. Document any coverage gaps with a remediation owner and cadence.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Scope Cowork-selecting spending policies to a pilot group with tenant-wide discovery off; keep the Cowork Browsing toggle off until browser governance is reviewed; keep models with provider-retention implications disabled for regulated data until approved; maintain a plugin and custom-skill inventory; set an initial consumption limit. |
| **Recommended** | Manage billing scope, discovery, model toggles, browser toggle, plugin/skill/uploaded-package inventory, and consumption limits through a documented change register with separation of approval and implementation; route access requests through a formal review; confirm Purview and audit coverage. |
| **Regulated** | All Recommended controls plus: dual technology + compliance approval before enabling spending-policy access, discovery, browser use, or Anthropic/model controls for any regulated population; supervisory review of agentic outputs per FINRA Rule 3110 where applicable; prohibition or explicit documented approval of any model that requires provider data retention for regulated data; examination-ready evidence retention for billing, discovery, model, browser, plugin/skill, and consumption decisions. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for evidence-collection scripts that pull unified-audit-log activity and package portal exports.
- Use [Verification & Testing](verification-testing.md) to validate access posture, model toggles, browser toggle, plugin/skill inventory, consumption limits, and Purview/audit coverage.
- Keep [Troubleshooting](troubleshooting.md) available for access, billing, discovery, model-toggle, browser-use, and plugin issues.

*FSI Copilot Governance Framework v1.8.0 - July 2026*
- Back to [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)
