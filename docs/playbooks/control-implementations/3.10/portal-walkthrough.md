# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Portal Walkthrough

Step-by-step portal configuration for implementing privacy controls that support compliance with SEC Regulation S-P when using Microsoft 365 Copilot with consumer financial information.

## Prerequisites

- **Role:** Compliance Administrator, Privacy Officer
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview compliance portal

## Steps

### Step 1: Configure Sensitive Information Types for Consumer Financial Data

**Portal:** Microsoft Purview Compliance Portal
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

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Data loss prevention > Policies > Create policy

1. Create a DLP policy named "FSI-RegSP-Copilot-Privacy-Protection".
2. Select the **U.S. Financial** regulatory template as a starting point.
3. Add locations: Exchange, SharePoint, OneDrive, Teams, and Copilot interactions.
4. Configure rules:
   - **Low volume (1-9 instances):** Notify user with policy tip
   - **High volume (10+ instances):** Block sharing and notify compliance team
5. Enable the policy for all Copilot-licensed users.

### Step 3: Configure Information Barriers for Privacy Segregation

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Information barriers > Segments and policies

1. Review existing information barrier segments.
2. Verify that segments prevent Copilot from surfacing consumer financial data across business unit boundaries where required by Reg S-P.
3. Create or update barrier policies to prevent cross-segment data access via Copilot grounding.

### Step 4: Enable Privacy Impact Assessment for Copilot Data Flows

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Data classification > Content explorer

1. Use Content Explorer to identify where consumer financial information resides.
2. Document the data flow from source systems through Copilot interactions.
3. Assess whether Copilot prompts and responses may expose nonpublic personal information (NPI).
4. Configure appropriate access controls to limit NPI exposure in Copilot responses.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| DLP for consumer financial data | Notify | Block external | Block all unauthorized |
| Information barriers | Optional | Business unit boundaries | Full segregation |
| NPI detection in Copilot | Audit only | Warn users | Block and log |
| Privacy impact assessment | Annual | Semi-annual | Annual + event-driven |

## Regulatory Alignment

- **SEC Reg S-P (Rule 30)** — Supports compliance with safeguarding requirements for customer records and information
- **GLBA Title V** — Helps meet financial privacy requirements for nonpublic personal information
- **FTC Safeguards Rule** — Supports information security program requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for privacy control automation
- See [Verification & Testing](verification-testing.md) to validate privacy protections
