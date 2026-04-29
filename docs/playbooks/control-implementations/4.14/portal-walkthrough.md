# Control 4.14: Copilot Studio Agent Lifecycle Governance - Portal Walkthrough

Step-by-step governance workflow for operating the five Copilot Studio agent lifecycle stages: authoring, testing, publishing, versioning, and deprecation. This playbook governs the lifecycle wrapper; intake (Control 1.10), tuning (Control 1.16), and embedded extensibility (Control 4.13) remain owned by their respective controls.

## Prerequisites

- [Control 1.10 Vendor Risk Management](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) intake gate has cleared the use case before authoring begins.
- [Control 4.13 Extensibility Governance](../../../controls/pillar-4-operations/4.13-extensibility-governance.md) covers connectors and plugins embedded in the agent.
- A documented agent register exists, with the inventory fields listed in [Control 4.14](../../../controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md).
- Approved Copilot Studio environments separated by lifecycle stage (e.g., dev, test, prod) are in place.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft Copilot Studio | Solutions > Agents | Authoring, testing, publishing, and versioning surface |
| Microsoft 365 Admin Center | Copilot > Agents | Tenant view of published agents and their audience scope |
| Microsoft Purview portal | Audit | Captures publishing, version, and lifecycle events |
| Governance evidence repository | Workspace of record | Stores the agent register and stage-by-stage evidence |

## Steps

### Step 1: Confirm intake clearance before authoring

Authoring begins only after the Control 1.10 intake decision is recorded. Capture the decision identifier in the agent register so each agent's lifecycle has a documented origin.

### Step 2: Operate testing as a gate, not a checkbox

Functional, prompt-injection, content-safety, and connector-boundary tests run in a non-production environment with a test plan and exit criteria. Tests passing is the entry condition for publishing — failing tests block the stage transition.

### Step 3: Run the publishing approval workflow

A named approver validates that testing exited cleanly, that an owner of record is named, that audience scope is appropriate, and that any embedded extensibility components are governed under [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md). The approval record enters the agent register.

### Step 4: Apply a versioning policy

Subsequent changes follow a documented versioning policy (recommended: semantic versioning). Each version produces a change-log entry, an approval entry, and a re-test result. Skipping the version record is a supervisory gap under FINRA Rule 3110.

### Step 5: Run a deprecation playbook at end of life

Agents reaching end of life follow a deprecation playbook covering user notice, migration guidance, impact assessment, and a final retirement record. Deprecated agents must be removed from runtime surfaces, not left dormant.

### Step 6: Periodic lifecycle attestation

Schedule a periodic attestation that every agent in the register has a current owner, a current lifecycle stage, and an in-period review record. Stale attestations are themselves an evidence gap.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Maintain an agent register and capture publishing approval per agent. |
| **Recommended** | Operate stage-separated environments, require versioned change logs, and run the deprecation playbook for retired agents. |
| **Regulated** | All Recommended controls plus: independent reviewer sign-off on publishing for high-impact agents, quarterly lifecycle attestation, and a tested deprecation drill. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to inventory agents and pull lifecycle audit evidence.
- Use [Verification & Testing](verification-testing.md) to validate stage transitions, approvals, and deprecation.
- Keep [Troubleshooting](troubleshooting.md) available for register, approval, and deprecation issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 4.14](../../../controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md)
