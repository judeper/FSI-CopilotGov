# Control 4.7: Copilot Feedback and Telemetry Data Governance — Portal Walkthrough

Step-by-step portal configuration for governing the collection, storage, and use of Copilot feedback and telemetry data in financial services environments.

## Prerequisites

- **Role:** Entra Global Admin, Privacy Administrator
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center, Microsoft Purview

## Steps

### Step 1: Configure Copilot Feedback Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Cloud Policy service / Group Policy feedback and survey policies; M365 Admin Center feedback surfaces where present

1. Navigate to Cloud Policy service for Microsoft 365 or the equivalent Group Policy settings.
2. Configure feedback collection options:
   - **User feedback (thumbs up/down)** — Enable or disable per organizational policy
   - **Screenshots, attachments, logs, and content samples** — Disable for regulated populations unless approved
   - **Microsoft follow-up contact** — Disable unless approved
   - **In-product surveys** — Configure per organizational policy
3. For FSI environments, limit feedback data to the minimum necessary.

### Step 2: Configure Diagnostic Data Levels

**Portal:** Microsoft 365 Admin Center
**Path:** Cloud Policy service or Group Policy > Microsoft Office 2016 > Privacy > Trust Center

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
| User feedback collection | Firm-defined | Firm-defined with metadata limits | Firm-defined with screenshots/logs/content samples disabled unless approved |
| Diagnostic data level | Required unless justified | Required unless justified | Required unless justified |
| Connected experiences | Selective | Minimum necessary | Minimum necessary |
| Telemetry retention | Default | Defined policy | Defined with data minimization |

## Regulatory Alignment

- **GLBA** — Supports compliance with data handling requirements for financial information
- **CCPA/CPRA** — Can support firm-defined controls for consumer data privacy requirements (where applicable)
- **GDPR** — Supports data minimization and processing transparency requirements (for global operations)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for telemetry configuration automation
- See [Verification & Testing](verification-testing.md) to validate data governance
- Back to [Control 4.7](../../../controls/pillar-4-operations/4.7-feedback-telemetry.md)
