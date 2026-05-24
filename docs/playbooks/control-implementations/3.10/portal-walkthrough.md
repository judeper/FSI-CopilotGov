<!-- Educational reference only — not legal advice. Verify all citations against current regulations. -->

# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Portal Walkthrough

Step-by-step portal configuration for implementing privacy controls that support compliance with SEC Regulation S-P (including the 2023 amendments) when using Microsoft 365 Copilot with consumer financial information.

## Prerequisites

- **Role:** Purview Compliance Admin, Privacy Officer
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal

## Steps

### Step 1: Configure Sensitive Information Types for Consumer Financial Data

**Portal:** Microsoft Purview portal
**Path:** Solutions > Data classification > Sensitive info types

1. Review built-in sensitive information types relevant to Reg S-P:
   - U.S. Social Security Number (SSN)
   - Credit Card Number
   - U.S. Bank Account Number
   - U.S. Individual Taxpayer Identification Number (ITIN)
2. Create custom sensitive information types for firm-specific financial data:
   - Account numbers matching your firm's format
   - Client identifiers and portfolio numbers
3. Test each SIT against sample data to verify accuracy.

### Step 2: Create DLP Policies for Consumer Financial Information in Copilot

**Portal:** Microsoft Purview portal
**Path:** Solutions > Data loss prevention > Policies > Create policy

1. Create a DLP policy named "FSI-RegSP-Copilot-Privacy-Protection".
2. Select the **U.S. Financial** regulatory template as a starting point.
3. Add locations: Exchange, SharePoint, OneDrive, Teams, and Copilot interactions.
4. Configure rules:
   - **Low volume (1-9 instances):** Notify user with policy tip
   - **High volume (10+ instances):** Block sharing and notify compliance team
5. Enable the policy for all Copilot-licensed users.

### Step 3: Configure Information Barriers for Privacy Segregation

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information barriers > Segments and policies

1. Review existing information barrier segments.
2. Verify that segments prevent Copilot from surfacing consumer financial data across business unit boundaries where required by Reg S-P.
3. Create or update barrier policies to prevent cross-segment data access via Copilot grounding.

### Step 4: Enable Privacy Impact Assessment for Copilot Data Flows

**Portal:** Microsoft Purview portal
**Path:** Solutions > Data classification > Content explorer

1. Use Content Explorer to identify where consumer financial information resides.
2. Document the data flow from source systems through Copilot interactions.
3. Assess whether Copilot prompts and responses may expose nonpublic personal information (NPI).
4. Configure appropriate access controls to limit NPI exposure in Copilot responses.

### Step 5: Configure the Incident Response Program for Copilot NPI Events (Reg S-P Rule 248.30(a)(4))

**Portal:** Microsoft Purview portal / Internal incident response documentation
**Path:** Microsoft Purview > Audit > Alert policies; Internal IRP documentation system

The amended Reg S-P requires a written incident response program addressing unauthorized access to or use of customer information. Configure the following for Copilot NPI incident coverage:

1. **Document Copilot NPI scenarios in the written IRP:**
   - Scenario: Copilot surfaces client NPI to unauthorized user (oversharing or permission misconfiguration)
   - Scenario: Copilot-drafted communication contains NPI that should not have been disclosed
   - Scenario: Copilot Chat response aggregates NPI from multiple sources into a single response accessible to an unauthorized party
   For each scenario, document: detection method, severity classification, escalation path, containment steps, and notification workflow.

2. **Configure alert policies for Copilot NPI events:**
   - Navigate to **Microsoft Purview > Audit > Alert policies**
   - Create or verify an alert policy that triggers on DLP policy matches involving Copilot interactions
   - Set alert severity to High for SSN/account credential exposure; Medium for other NPI types
   - Configure alerts to route to the designated Privacy Officer and Compliance team

3. **Verify service provider notification arrangements (Reg S-P Rule 248.30(a)(3)):**
   - Verify that service provider agreements require Microsoft to notify the institution within 72 hours of becoming aware of unauthorized access to customer information
   - Document the institution's process for receiving and acting on service provider notifications

4. **Set up the incident response notification timeline:**
   - Internal escalation: Per the institution's incident response procedures
   - Customer notification: Per amended Reg S-P requirements

### Step 6: Test the Incident Response Program Configuration

1. Conduct a tabletop exercise simulating a Copilot NPI incident.
2. Walk through each stage of the incident response procedures per the institution's written program.
3. Verify that service provider notification arrangements are documented and tested.
4. Document the exercise outcomes and any gaps identified.
5. Update the IRP based on exercise findings.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| DLP for consumer financial data | Notify | Block external | Block all unauthorized |
| Information barriers | Optional | Business unit boundaries | Full segregation |
| NPI detection in Copilot | Audit only | Warn users | Block and log |
| Privacy impact assessment | Annual | Semi-annual | Annual + event-driven |
| Written incident response program | Required (Rule 248.30(a)(4)) | With Copilot scenarios | With tabletop exercise documentation |
| Service provider notification requirement | Verify agreements | Test in tabletop | Quarterly drill |

## Regulatory Alignment

- **SEC Reg S-P Rule 248.30(a)(3)** — Requires institutions to adopt policies requiring service providers to notify the institution within 72 hours of unauthorized access to customer information
- **SEC Reg S-P Rule 248.30(a)(4)** — Mandatory written incident response program; Copilot-specific scenarios must be included
- **SEC Reg S-P (Rule 30)** — Supports compliance with safeguarding requirements for customer records and information
- **GLBA Title V** — Helps meet financial privacy requirements for nonpublic personal information
- **GLBA §501(b)** — Helps meet safeguards provisions for nonpublic personal information at banks and broker-dealers (the statutory authority for SEC Reg S-P safeguards for SEC-regulated entities; the FTC Safeguards Rule is a separate implementing regulation that applies to FTC-jurisdiction institutions, not to SEC-regulated broker-dealers)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for privacy control automation
- See [Verification & Testing](verification-testing.md) to validate privacy protections
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
