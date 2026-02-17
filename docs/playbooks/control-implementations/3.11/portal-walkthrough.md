# Control 3.11: Record Keeping and Books-and-Records Compliance — Portal Walkthrough

Step-by-step portal configuration for implementing record keeping controls that support compliance with SEC Rule 17a-4, FINRA Rule 4511, and other books-and-records requirements for Copilot-generated content.

## Prerequisites

- **Role:** Compliance Administrator, Records Management Administrator
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview compliance portal

## Steps

### Step 1: Configure Records Management for Copilot Content

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Records management > File plan

1. Navigate to the Records management solution.
2. Create file plan categories aligned with SEC/FINRA record types:
   - **Business Communications** — Copilot-drafted emails, Teams messages
   - **Client Correspondence** — Copilot-assisted client communications
   - **Investment Recommendations** — AI-assisted advisory content
   - **Marketing Materials** — Copilot-generated marketing content
3. Assign retention periods per category (minimum 3 years for general communications, 6 years for client records).

### Step 2: Create Retention Labels with Regulatory Record Status

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Records management > File plan > Create a label

1. Create retention labels for each record category:
   - "SEC-17a4-Business-Communication-6yr" — 6-year retention, regulatory record
   - "FINRA-4511-Client-Record-7yr" — 7-year retention, regulatory record
   - "Investment-Recommendation-Record-7yr" — 7-year retention, regulatory record
2. Mark labels as **Regulatory records** where required (immutable, cannot be relabeled or deleted).
3. Configure disposition review for records approaching expiration.

### Step 3: Configure Auto-Apply Retention Labels

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Records management > Label policies > Auto-apply a label

1. Create auto-apply policies for each retention label:
   - Apply "Business Communication" labels based on Copilot interaction metadata
   - Apply "Client Correspondence" labels based on external recipient detection
   - Apply "Investment Recommendation" labels using trainable classifiers for advisory content
2. Target locations: Exchange, SharePoint, OneDrive, Teams.
3. Set each policy to run continuously.

### Step 4: Configure WORM-Compliant Storage (If Required)

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Records management > Disposition

1. For SEC Rule 17a-4(f) compliance, verify that regulatory records are stored in write-once-read-many (WORM) format.
2. Configure Preservation Lock on retention policies governing regulatory records.
3. Once Preservation Lock is enabled, the retention policy cannot be shortened or disabled.
4. Document the Preservation Lock configuration for regulatory examination.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Record classification | Manual | Auto-apply labels | Auto-apply with manual override |
| Regulatory record status | Optional | Key categories | All client-facing content |
| Preservation Lock | Not applied | Applied to critical records | Required for 17a-4 |
| Disposition review | Automatic | Review before disposition | Committee review |

## Regulatory Alignment

- **SEC Rule 17a-4** — Supports compliance with electronic record retention and WORM storage requirements
- **FINRA Rule 4511** — Helps meet books-and-records retention obligations
- **SEC Rule 17a-3** — Supports record-making requirements for broker-dealer operations

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for records management automation
- See [Verification & Testing](verification-testing.md) to validate record keeping controls
