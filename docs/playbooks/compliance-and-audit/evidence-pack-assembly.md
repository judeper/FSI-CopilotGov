# Evidence Pack Assembly

How to collect and organize evidence for regulatory examinations and internal audits of M365 Copilot governance controls.

---

## Evidence Pack Structure

Organize evidence into the following categories aligned with the FSI Copilot Governance Framework pillars:

### Category 1: Governance Foundation

| Evidence Item | Source | Format | Collection Method |
|--------------|--------|--------|-------------------|
| Governance committee charter | Governance repository | PDF | Manual export |
| Committee meeting minutes | Governance repository | PDF | Manual export |
| Governance decisions log | STATE.md / governance log | PDF | Manual export |
| RACI matrix | Governance documentation | PDF | Manual export |
| Acceptable use policy | Policy repository | PDF | Manual export |

### Category 2: Pre-Deployment Controls (Pillar 1)

| Evidence Item | Source | Format | Collection Method |
|--------------|--------|--------|-------------------|
| Copilot readiness assessment | Admin Center dashboard | Screenshot/PDF | Manual capture |
| Oversharing assessment results | DSPM for AI report | CSV/PDF | Export from Purview |
| Permission audit report | PowerShell output | CSV | Script 1.6 |
| Sensitivity label taxonomy | PowerShell export | CSV | Script 1.5.1 |
| Label coverage metrics | Purview analytics | PDF | Export from Purview |
| RSS allowed list | PowerShell output | CSV | Script 1.3.3 |
| Vendor risk assessment | GRC platform | PDF | Manual export |
| License assignment records | Entra ID / Admin Center | CSV | Script 1.9.1 |
| Training completion records | LMS | CSV | LMS export |

### Category 3: Security Controls (Pillar 2)

| Evidence Item | Source | Format | Collection Method |
|--------------|--------|--------|-------------------|
| DLP policy configuration | PowerShell export | CSV/JSON | Script 2.1.2 |
| DLP incident reports | Purview | CSV | Script 2.1.3 |
| Conditional Access policies | PowerShell export | CSV | Script 2.3.1 |
| Information Barrier policies | PowerShell export | CSV | Script 2.4.3 |
| Web search configuration | Admin Center | Screenshot | Manual capture |
| Encryption status | PowerShell output | CSV | Script 2.8.1-2 |
| Insider risk policy config | Purview | Screenshot/PDF | Manual capture |
| External sharing settings | PowerShell output | CSV | Script 2.12.1 |

### Category 4: Verification Results

| Evidence Item | Source | Format | Collection Method |
|--------------|--------|--------|-------------------|
| Control test results | Test execution | PDF | From verification playbooks |
| DLP detection test | Test scenario | Screenshot/PDF | Manual test |
| Label inheritance test | Test scenario | Screenshot/PDF | Manual test |
| Barrier enforcement test | Test scenario | Screenshot/PDF | Manual test |
| Copilot scope validation | Test scenario | Screenshot/PDF | Manual test |

## Collection Procedures

### Step 1: Prepare Evidence Request List

Before collection, identify which evidence items are needed based on:
- The regulatory examination scope (FINRA, SEC, OCC, state regulators)
- The specific controls being examined
- The time period under examination
- Any specific examiner requests

### Step 2: Run Automated Collection

Execute the PowerShell scripts referenced in each control's playbook to generate current configuration exports and reports. Run all scripts within a 48-hour window to maintain data consistency.

### Step 3: Capture Manual Evidence

For items requiring manual capture:
- Take screenshots with timestamps visible
- Export reports as PDF with date ranges clearly shown
- Include the full navigation path in screenshot descriptions
- Capture the signed-in user information in each screenshot

### Step 4: Organize and Index

Organize evidence into folders matching the category structure above. Create an evidence index document listing:
- Each evidence item with its file name
- Collection date and collection method
- The control(s) it supports
- Any caveats or context notes

### Step 5: Quality Review

Before submitting the evidence pack:
- Verify all requested items are included
- Check screenshot quality and readability
- Confirm date ranges match the examination period
- Remove any sensitive data not relevant to the examination
- Have a second reviewer verify completeness

## Evidence Retention

| Category | Minimum Retention | Recommended Retention |
|----------|-------------------|----------------------|
| Governance documentation | 5 years | 7 years |
| Configuration exports | 5 years | 7 years |
| Test results | 5 years | 7 years |
| Audit logs | 5 years | 7 years |
| Incident records | 7 years | 10 years |
| Regulatory correspondence | 7 years | Permanent |

## Storage Requirements

- Store evidence in a tamper-evident repository
- Maintain access controls on evidence (compliance team access only)
- Enable version control to track any modifications
- Maintain backup copies in a separate secure location
- Document the chain of custody for all evidence

---

*Update this guide when new controls are added or regulatory requirements change.*
