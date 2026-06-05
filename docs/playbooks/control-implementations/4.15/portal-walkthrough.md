# Control 4.15: Copilot Cowork Governance - Portal Walkthrough

Step-by-step admin-center workflow for governing Microsoft 365 Copilot Cowork while it is a Frontier preview feature: confirming Frontier enrollment, scoping availability, governing deployment and pinning, controlling plugins, and confirming supervision coverage. This playbook governs the Cowork agent wrapper; broader admin settings (Control 4.1) and extensibility (Control 4.13) remain owned by their respective controls.

## Prerequisites

- [Control 4.1 Admin Settings and Feature Management](../../../controls/pillar-4-operations/4.1-admin-settings-feature-management.md) baseline is documented.
- [Control 4.13 Extensibility Governance](../../../controls/pillar-4-operations/4.13-extensibility-governance.md) governs plugins and connectors that extend Cowork.
- An approved pilot security group exists for phased rollout.
- A documented agent register and evidence repository are in place, per [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md).

> **Important:** Cowork is a Frontier preview feature. Preview capabilities and admin surfaces may change. Re-verify each step against current Microsoft documentation before relying on it in production governance.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft 365 Copilot settings | Copilot > Settings > Frontier | Confirms tenant and admin Frontier enrollment that gates Cowork visibility |
| Microsoft 365 Admin Center | Copilot > Agents > All agents > Cowork | Sets availability, deployment, and plugin controls for Cowork |
| Microsoft 365 Admin Center | Copilot > Agents > Manage pinned agents | Controls whether Cowork is pinned in the Copilot rail |
| Microsoft Purview portal | Audit | Captures Cowork-related agent install, deployment, and usage events |
| Governance evidence repository | Workspace of record | Stores availability decisions, plugin inventory, and approvals |

## Steps

### Step 1: Confirm Frontier enrollment

Navigate to **Copilot > Settings > Frontier** and record whether the tenant and the administering accounts are enrolled. If Cowork is not visible in Agent management, verify that the admin account is enrolled in Frontier. Capture the enrollment decision and approver in the register.

### Step 2: Scope availability deliberately

In **Copilot > Agents > All agents**, select **Cowork** and set availability to **Available to specific users or groups** scoped to the approved pilot group, rather than leaving the Microsoft default of **Available to all users**. Use security groups to represent geographic or organizational segments — country/region scoping is not supported.

### Step 3: Govern deployment and pinning

Decide whether Cowork is user-installed or pre-installed. If deploying, use **Deploy to** scoped to approved groups, recognizing that deployment accepts users' permissions on their behalf. If pinning, use **Manage pinned agents**. Record an approval for each deployment or pinning decision.

### Step 4: Govern plugins

Review the plugins available to Cowork through the admin plugin controls. Maintain an approved-plugin inventory, confirm connector authentication for any Dynamics 365 / Agent 365 integrations, and restrict plugin availability to approved populations under [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md).

### Step 5: Confirm supervision and audit coverage

Confirm that Cowork activity is visible to existing Purview audit, retention, and supervision tooling. Document any coverage gaps and the remediation owner. Define a review cadence for availability, plugin inventory, and preview-feature changes.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Document Frontier enrollment, set availability deliberately, and maintain a plugin inventory. |
| **Recommended** | Use group-scoped availability and deployment under a change register, separate approval from implementation, and confirm audit coverage. |
| **Regulated** | All Recommended controls plus: dual technology + compliance approval before any regulated population is enabled, supervisory review of agentic outputs per FINRA Rule 3110 where applicable, and examination-ready evidence retention. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to inventory Cowork availability and pull audit evidence.
- Use [Verification & Testing](verification-testing.md) to validate availability scoping, plugin controls, and audit coverage.
- Keep [Troubleshooting](troubleshooting.md) available for visibility, availability, and plugin issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)
