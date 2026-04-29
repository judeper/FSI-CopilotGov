# Control 1.16: Copilot Tuning Governance - Portal Walkthrough

Step-by-step governance workflow for evaluating Copilot Tuning eligibility, configuring tenant-level enablement, scoping data sources, and operationalizing the request and approval flow for fine-tuned agents.

## Prerequisites

- Tenant has 5,000+ Microsoft 365 Copilot licenses (Tuning eligibility threshold).
- [Control 1.10 Vendor Risk Management](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) has assessed Microsoft as the AI platform vendor.
- [Control 2.2 Sensitivity Labels](../../../controls/pillar-2-security/2.2-sensitivity-labels-classification.md) is in place so candidate SharePoint tuning sources are labeled.
- A documented model risk management framework aligned to OCC Bulletin 2011-12 / SR 11-7 principles.
- Named tuning approver(s), output supervisor(s), and an evidence retention path.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft 365 Admin Center | Settings > Copilot > Copilot Tuning | Tenant-level enablement, scoping, request flow |
| Microsoft Entra admin center | Groups | Manages the security group authorized to request tuning |
| Microsoft Purview portal | Audit | Captures tuning job, snapshot, and approval events |
| Governance evidence repository | Workspace of record | Retains approval rationale, model cards, and supervision results |

## Steps

### Step 1: Confirm eligibility and policy posture

Verify the 5,000-license eligibility threshold and record the organization's policy decision (enabled / disabled / under evaluation). Capture the rationale even when the decision is to leave Tuning disabled — examiners commonly ask for the documented stance.

### Step 2: Establish the approval model before enabling

Decide who approves tuning requests, who supervises tuned-agent outputs, and how denials are recorded. Tuned agents are customized models and should be governed under the firm's model risk management framework before any tuning job runs.

### Step 3: Scope candidate data sources

Walk SharePoint sites considered for tuning input against the firm's data classification scheme. Exclude sites containing customer non-public personal information, MNPI, regulated communications, or content the firm has not approved as training material. Document the inclusion list and the exclusion rationale.

### Step 4: Configure tenant enablement

In the M365 Admin Center, enable Copilot Tuning at the tenant level only after Steps 1–3 are complete. Restrict access using a dedicated Entra security group rather than enabling for all users. Configure whether external open-source base models are permitted in line with the firm's third-party AI policy.

### Step 5: Operationalize the request, approval, and supervision flow

Define the standing review cadence (recommended weekly) for tuning requests. Each request should produce an evidence record covering business justification, data sources, intended use, approver decision, and the supervisor named for ongoing output review.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Keep Copilot Tuning disabled by default and record the policy decision in the governance evidence workspace. |
| **Recommended** | Enable Tuning only for a named Entra group, require business-justification on every request, and treat each tuned agent as a model under the firm's MRM framework. |
| **Regulated** | All Recommended controls plus: pre-publication independent review of tuning data scope, signed model card per tuned agent, and quarterly attestation of supervision results. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to capture configuration evidence and audit-log queries.
- Use [Verification & Testing](verification-testing.md) to validate scoping, approval, and supervision controls.
- Keep [Troubleshooting](troubleshooting.md) available for enablement, scoping, and approval-flow issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 1.16](../../../controls/pillar-1-readiness/1.16-copilot-tuning-governance.md)
