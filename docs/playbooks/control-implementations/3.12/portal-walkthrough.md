# Control 3.12: Evidence Collection and Audit Attestation — Portal Walkthrough

Step-by-step portal configuration for establishing evidence collection and audit attestation procedures that demonstrate Copilot governance control effectiveness to regulators and auditors.

## Prerequisites

- **Role:** Compliance Administrator, Audit Manager
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal, Compliance Manager

## Steps

### Step 1: Configure Compliance Manager Evidence Repository

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Assessments

1. Open or create an assessment for your primary regulatory framework.
2. For each improvement action related to Copilot governance (Controls 3.1-3.13), click **Manage evidence**.
3. Upload supporting evidence documents:
   - Policy configuration screenshots
   - PowerShell output confirming settings
   - Test results from verification procedures
   - Signed attestation documents
4. Set evidence review dates to align with your audit cycle.

### Step 2: Create Evidence Collection Templates

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Templates

1. Create or customize an assessment template for "FSI Copilot Governance Evidence Pack".
2. Map each Copilot control to its evidence requirements:
   - Control 3.1 (Audit Logging) — Audit log configuration, retention policy, sample log export
   - Control 3.4 (Communication Compliance) — Policy settings, review statistics, sample reviews
   - Control 3.6 (Supervision) — Supervisory hierarchy, review logs, SLA metrics
3. Define evidence freshness requirements (maximum age per evidence type).

### Step 3: Set Up Automated Evidence Gathering

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Assessments > Improvement actions

1. For each improvement action, configure automated testing where available:
   - Compliance Manager automatically assesses certain Microsoft 365 configurations.
   - Review the auto-assessed controls and validate accuracy.
2. For manually assessed controls, document the assessment procedure and frequency.
3. Assign owners responsible for periodic evidence updates.

### Step 4: Configure Attestation Workflow

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Assessments > Attestations

1. Define attestation frequency for each control area:
   - Technical controls: Quarterly attestation
   - Process controls: Semi-annual attestation
   - Governance controls: Annual attestation
2. Assign attestation approvers (compliance officers, control owners).
3. Configure attestation reminders 30 days before due dates.
4. Establish a sign-off workflow requiring dual approval for high-risk controls.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Evidence collection frequency | Annual | Quarterly | Continuous |
| Attestation frequency | Annual | Semi-annual | Quarterly |
| Automated assessments | None | Where available | Maximum automation |
| Evidence freshness | 12 months | 6 months | 3 months |

## Regulatory Alignment

- **FINRA Rule 3120** — Supports compliance with supervisory control system testing and attestation
- **SOX Section 404** — Helps meet internal controls over financial reporting attestation requirements
- **FFIEC IT Handbook** — Supports IT examination evidence production requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated evidence collection
- See [Verification & Testing](verification-testing.md) to validate evidence completeness
