# Control 4.12: Change Management for Copilot Feature Rollouts — Portal Walkthrough

Step-by-step portal configuration for establishing change management processes governing the rollout of new Copilot features, updates, and configuration changes in financial services environments.

## Prerequisites

- **Role:** Global Administrator, Microsoft 365 Service Administrator
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center, Microsoft 365 Message Center

## Steps

### Step 1: Configure Microsoft 365 Message Center Monitoring

**Portal:** Microsoft 365 Admin Center
**Path:** Health > Message center > Preferences

1. Navigate to the Message center and configure notification preferences.
2. Set up alerts for Copilot-related updates:
   - Filter by service: Microsoft 365 Copilot
   - Include categories: Plan for Change, Stay Informed, Prevent or Fix Issues
3. Add notification recipients: IT operations, compliance team, governance committee.
4. Configure a weekly digest email summarizing upcoming Copilot changes.

### Step 2: Configure Targeted Release for Change Validation

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Org settings > Organization profile > Release preferences

1. Configure the release preferences:
   - **Targeted release for selected users** — recommended for FSI environments
   - Assign the pilot/validation group to receive new Copilot features first
2. This allows the governance team to evaluate new features before organization-wide rollout.
3. Document the validation period (minimum 2 weeks recommended before general release).

### Step 3: Establish Change Advisory Board Process

**Portal:** Internal governance documentation
**Path:** Change management procedures

1. Define the Change Advisory Board (CAB) composition for Copilot changes:
   - IT operations representative
   - Information security representative
   - Compliance representative
   - Business stakeholder representative
2. Establish a CAB review cadence (weekly during active rollout, monthly for steady state).
3. Define change categories and approval requirements:
   - **Standard changes** — Pre-approved, documented procedures (e.g., adding users to Copilot groups)
   - **Normal changes** — CAB review required (e.g., enabling new Copilot features)
   - **Emergency changes** — Expedited approval path (e.g., disabling a feature due to compliance concern)

### Step 4: Create Change Impact Assessment Template

**Portal:** Internal documentation
**Path:** Change management templates

1. Create a standard impact assessment template for Copilot changes:
   - Change description and business justification
   - Regulatory impact assessment (does this change affect any compliance controls?)
   - Security impact assessment (does this change affect data protection?)
   - User impact assessment (training requirements, workflow changes)
   - Rollback plan (how to revert if issues are discovered)
2. Require completion for all Normal and Emergency changes.
3. Archive completed assessments for audit evidence.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Release channel | Standard | Targeted release for validation group | Targeted release with CAB |
| Change review process | Ad hoc | Weekly CAB review | CAB review per change |
| Validation period | None | 2 weeks | 4 weeks |
| Impact assessment | Optional | Required for feature changes | Required for all changes |

## Regulatory Alignment

- **FFIEC Operations Booklet** — Supports compliance with change management requirements for IT systems
- **OCC Heightened Standards** — Helps meet expectations for controlled technology changes
- **SOX Section 404** — Supports change management controls for systems affecting financial reporting

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for change management automation
- See [Verification & Testing](verification-testing.md) to validate change management processes
