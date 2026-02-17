# Control 3.6: Supervision and Oversight (FINRA 3110 / SEC Reg BI) — Portal Walkthrough

Step-by-step portal configuration for establishing supervisory controls over Copilot-assisted activities that support compliance with FINRA Rule 3110 (Supervision) and SEC Regulation Best Interest requirements.

## Prerequisites

- **Role:** Compliance Administrator, Supervisory Principal
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview compliance portal, Microsoft 365 Admin Center

## Steps

### Step 1: Define Supervisory Hierarchy in Purview

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Communication compliance > Supervisory review settings

1. Map the supervisory hierarchy by assigning supervising principals to groups of registered representatives.
2. Create supervisor groups aligned with business units (wealth management, trading, advisory).
3. Each supervisor should be assigned no more than 50 supervised users to maintain effective review capacity.

### Step 2: Create Supervisory Review Policies

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Communication compliance > Policies > Create policy

1. Create a policy named "FSI-FINRA-3110-Supervision-Copilot".
2. Set supervised users to registered representatives using Copilot.
3. Set supervised locations to include all Copilot-enabled communication channels.
4. Under conditions, configure:
   - **All outbound communications** — 25% sampling for routine supervision
   - **Client-facing communications with financial recommendations** — 100% review
   - **Copilot-drafted investment advice** — 100% review with pre-send hold

### Step 3: Configure Reg BI Documentation Review

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Communication compliance > Policies

1. Create a second policy named "FSI-RegBI-Copilot-BestInterest-Review".
2. Target communications where Copilot assists in creating investment recommendations.
3. Add conditions to detect:
   - Recommendation language (buy, sell, hold, allocate)
   - Product-specific terms (mutual fund, ETF, annuity, structured product)
   - Cost and fee disclosures
4. Require 100% supervisory review for all matches.

### Step 4: Set Up Supervision Dashboards

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Communication compliance > Dashboard

1. Configure the dashboard to display key supervision metrics:
   - Outstanding review items by supervisor
   - Average review completion time
   - Policy match trend over 30/60/90 days
   - Escalation rate by policy
2. Set up weekly email digests for supervisory principals.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Routine communication sampling | 10% | 25% | 25% |
| Investment recommendation review | 25% | 100% | 100% |
| Pre-send hold for Copilot advice | Off | Recommended | Required |
| Supervisor-to-rep ratio | 1:100 | 1:50 | 1:25 |

## Regulatory Alignment

- **FINRA Rule 3110** — Supports compliance with supervisory system and written supervisory procedure requirements
- **SEC Reg BI** — Helps meet best-interest documentation, disclosure, and care obligations
- **FINRA Rule 3120** — Supports supervisory control system testing requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automation
- See [Verification & Testing](verification-testing.md) to validate supervisory controls
