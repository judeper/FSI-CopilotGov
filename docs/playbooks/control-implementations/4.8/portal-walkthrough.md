# Control 4.8: Cost Allocation and License Optimization — Portal Walkthrough

Step-by-step portal configuration for implementing cost allocation, chargeback, license optimization, and pay-as-you-go (PAYG) billing governance for Microsoft 365 Copilot across the organization.

## Prerequisites

- **Role:** Global Administrator, License Administrator, Billing Administrator
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

### Step 1b: Configure Pay-As-You-Go Billing Monitoring in Azure Commerce

**Portal:** Azure Portal
**Path:** Cost Management + Billing > Billing accounts > [Your account] > Products and services

1. Navigate to the Azure Portal at `portal.azure.com` and sign in with Global Administrator or Billing Administrator credentials.
2. Navigate to **Cost Management + Billing** in the left navigation.
3. Select **Billing accounts** and choose the billing account associated with your Microsoft 365 tenant.
4. Under **Products and services**, search for **Microsoft 365 Copilot Chat** to view PAYG billing details and current metered usage.
5. Configure budget caps for PAYG spending by department:
   - In the **Azure Portal**, navigate to **Cost Management > Budgets**
   - Select **+ Add** to create a new budget
   - Set the **Scope** to the subscription or resource group associated with PAYG Copilot Chat
   - Set the **Budget amount** to the approved monthly spend limit for the scope
   - Under **Alert conditions**, add alerts at 80% and 100% of budget
   - Set **Alert recipients** to the department head and IT finance owner
   - Confirm and save the budget
6. Configure Azure cost management tags for PAYG cost allocation:
   - Navigate to **Cost Management > Cost analysis**
   - Filter by service name containing "Copilot" to isolate PAYG charges
   - Group costs by department tag to verify cost routing
   - If costs are not routing correctly, update the tag assignment in **Azure Portal > Subscriptions > [subscription] > Resource tags**
7. Review monthly PAYG usage in **Azure Portal > Cost Management > Cost analysis**:
   - Set date range to the current billing month
   - Filter by meter name to isolate Copilot Chat metered charges
   - Export the cost analysis report for monthly reconciliation with internal finance records

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
| PAYG billing | Not enabled (per-seat only) | Per-seat for heavy users + PAYG with budget caps for occasional users | Per-seat for regulated users + PAYG with strict budget caps, department cost allocation, quarterly review |
| PAYG budget cap | N/A | Per-department monthly cap | Per-department cap + per-user group sub-limits |
| Chargeback model | None | Per-license | Usage-based hybrid including PAYG metered costs |
| Utilization review | Annual | Quarterly | Monthly; PAYG anomaly review quarterly |
| Underutilization threshold | No threshold | 30 days inactive | 14 days inactive |

## Regulatory Alignment

- **SOX Section 404** (15 U.S.C. § 7262) — PAYG budget authorization controls serve as IT general controls over financial reporting; per-seat and PAYG costs must be reconciled to vendor billing
- **FFIEC Management Booklet, Section II.D** — Cost-benefit analysis of per-seat vs. PAYG model selection should be documented for examiner review; ongoing cost monitoring supports FFIEC expectations
- **OCC Heightened Standards** (12 CFR Part 30, Appendix D) — Budget caps and anomaly detection for PAYG demonstrate responsible technology cost governance expected by OCC

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for license management automation
- See [Verification & Testing](verification-testing.md) to validate cost allocation
