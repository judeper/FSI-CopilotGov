# Control 4.8: Cost Allocation and License Optimization — Portal Walkthrough

Step-by-step portal configuration for implementing cost allocation, chargeback, license optimization, and pay-as-you-go (PAYG) billing governance for Microsoft 365 Copilot across the organization.

## Prerequisites

- **Role:** AI Administrator, License Administrator, Billing Administrator, or Global Administrator as needed
- **License:** Microsoft 365 E5 with Copilot add-on; Azure subscription (for PAYG billing management)
- **Access:** Microsoft 365 Admin Center, Azure Portal (Cost Management + Billing), Azure Cost Management

## Steps

### Step 1: Establish License Inventory and Cost Baseline

**Portal:** Microsoft 365 Admin Center
**Path:** Billing > Licenses > Microsoft 365 Copilot

1. Navigate to the Copilot license inventory.
2. Document current license counts: total purchased, assigned, and available.
3. Calculate the per-user monthly cost based on your licensing agreement.
4. Establish a cost baseline for budget tracking and chargeback.

### Step 1b: Configure Pay-As-You-Go Billing Policies

**Portal:** Microsoft 365 Admin Center and Microsoft Cost Management
**Path:** Billing > Pay-as-you-go services / Cost Management

1. Open **Billing > Pay-as-you-go services** in the Microsoft 365 admin center.
2. Create or review the billing policy tied to the correct Azure subscription.
3. Add the approved users or groups to the billing policy and document the responsible cost owner.
4. Add a budget limit and notification routing to the billing policy.
5. Connect the billing policy to the approved service, such as Microsoft 365 Copilot Chat.
6. Open **Cost Management** to review usage and charges for the connected service.
7. Review **Settings > Org settings > Self-service trials and purchases** and document the per-product self-service state for Microsoft 365 Copilot and related products.

### Step 2: Configure Group-Based License Assignment

**Portal:** Microsoft Entra Admin Center
**Path:** Groups > All groups > Group-based licensing

1. Create or identify groups for license allocation by business unit:
   - "Copilot-Licensed-WealthManagement"
   - "Copilot-Licensed-Trading"
   - "Copilot-Licensed-Compliance"
   - "Copilot-Licensed-Operations"
2. Assign the Microsoft 365 Copilot license to each group.
3. Group membership changes automatically add or remove licenses.
4. Document the cost center mapping for each group.

### Step 3: Set Up Usage-Based Chargeback Reporting

**Portal:** Microsoft 365 Admin Center
**Path:** Reports > Usage > Microsoft 365 Copilot

1. Download the Copilot usage report and correlate with department data.
2. Create a chargeback model:
   - **Per-license chargeback** — charge each department for assigned licenses
   - **Usage-based chargeback** — charge based on active usage metrics
   - **Hybrid model** — base charge + usage premium
3. Document the chargeback methodology and distribute to finance stakeholders.

### Step 4: Identify License Optimization Opportunities

**Portal:** Microsoft 365 Admin Center
**Path:** Reports > Usage > Microsoft 365 Copilot

1. Review the usage report to identify underutilized licenses:
   - Users with licenses assigned but no activity in 30+ days
   - Users with very low interaction counts (fewer than 5 per month)
2. Create a reallocation plan for underutilized licenses.
3. Establish a quarterly license review cadence.
4. Set up automated alerts for license utilization dropping below threshold.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| License assignment method | Manual | Group-based | Group-based with approval |
| PAYG billing | Not enabled or not in scope | PAYG through documented billing policies for occasional users | PAYG limited to bounded scenarios with monthly billing-policy review |
| PAYG budget controls | N/A | Budget and notifications on each active billing policy | Budget and notifications plus documented escalation path |
| Chargeback model | None | Per-license | Hybrid model using seats plus PAYG cost review by billing policy |
| Utilization review | Annual | Quarterly | Monthly; PAYG anomaly review quarterly |
| Underutilization threshold | No threshold | 30 days inactive | 14 days inactive |

## Regulatory Alignment

- **SOX Section 404** (15 U.S.C. § 7262) — PAYG budget authorization controls serve as IT general controls over financial reporting; per-seat and PAYG costs should be reconciled to vendor billing and billing-policy records
- **FFIEC Management Booklet, Section II.D** — Cost-benefit analysis of per-seat versus PAYG model selection should be documented for examiner review; ongoing cost monitoring supports FFIEC expectations
- **OCC Heightened Standards** (12 CFR Part 30, Appendix D) — Billing-policy review, budgets, and anomaly investigation demonstrate responsible technology cost governance expected by OCC

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for license management automation
- See [Verification & Testing](verification-testing.md) to validate cost allocation
