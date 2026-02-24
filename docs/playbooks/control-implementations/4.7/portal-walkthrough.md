# Control 4.7: Copilot Feedback and Telemetry Data Governance — Portal Walkthrough

Step-by-step portal configuration for governing the collection, storage, and use of Copilot feedback and telemetry data in financial services environments.

## Prerequisites

- **Role:** Global Administrator, Privacy Administrator
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center, Microsoft Purview

## Steps

### Step 1: Configure Copilot Feedback Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Copilot > Feedback

1. Navigate to Copilot feedback settings.
2. Configure feedback collection options:
   - **User feedback (thumbs up/down)** — Enable or disable per organizational policy
   - **Optional diagnostic data** — Configure the level of telemetry shared with Microsoft
   - **Connected experiences** — Control data sharing for service improvement
3. For FSI environments, limit feedback data to the minimum necessary.

### Step 2: Configure Diagnostic Data Levels

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Org settings > Services > Microsoft 365 Apps

1. Navigate to the Microsoft 365 Apps settings.
2. Set diagnostic data level:
   - **Required diagnostic data** — Minimum data for service operation (recommended for FSI)
   - **Optional diagnostic data** — Additional data for service improvement (not recommended for regulated environments)
3. Review and disable optional connected experiences if data sharing is restricted.

### Step 3: Configure Telemetry Data Retention

**Portal:** Microsoft Purview portal
**Path:** Solutions > Data lifecycle management

1. Create a retention policy for Copilot telemetry and feedback data.
2. Define retention periods aligned with regulatory requirements.
3. Configure automatic purging of telemetry data beyond the retention period.
4. Ensure telemetry data is not retained longer than necessary per data minimization principles.

### Step 4: Review Microsoft Data Processing Terms

**Portal:** Microsoft Service Trust Portal / Licensing documentation
**Path:** Data Protection Addendum

1. Review Microsoft's Data Processing Addendum (DPA) for Copilot data handling.
2. Verify that Copilot feedback and telemetry data processing aligns with organizational privacy policies.
3. Document the data flow: user feedback/telemetry -> Microsoft processing -> data retention.
4. Maintain a record of the DPA version and review date for audit purposes.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| User feedback collection | Enabled | Enabled (internal use) | Enabled with controls |
| Diagnostic data level | Optional | Required only | Required only |
| Connected experiences | Enabled | Selective | Minimum necessary |
| Telemetry retention | Default | Defined policy | Defined with data minimization |

## Regulatory Alignment

- **GLBA** — Supports compliance with data handling requirements for financial information
- **CCPA/CPRA** — Helps meet consumer data privacy requirements (where applicable)
- **GDPR** — Supports data minimization and processing transparency requirements (for global operations)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for telemetry configuration automation
- See [Verification & Testing](verification-testing.md) to validate data governance
