# Control 4.8: Cost Allocation and License Optimization — Portal Walkthrough

Step-by-step portal configuration for implementing cost allocation, chargeback, and license optimization for Microsoft 365 Copilot across the organization.

## Prerequisites

- **Role:** Global Administrator, License Administrator, Billing Administrator
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center, Azure Cost Management (if applicable)

## Steps

### Step 1: Establish License Inventory and Cost Baseline

**Portal:** Microsoft 365 Admin Center
**Path:** Billing > Licenses > Microsoft 365 Copilot

1. Navigate to the Copilot license inventory.
2. Document current license counts: total purchased, assigned, and available.
3. Calculate the per-user monthly cost based on your licensing agreement.
4. Establish a cost baseline for budget tracking and chargeback.

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
| Chargeback model | None | Per-license | Usage-based hybrid |
| Utilization review | Annual | Quarterly | Monthly |
| Underutilization threshold | No threshold | 30 days inactive | 14 days inactive |

## Regulatory Alignment

- **SOX Section 404** — Supports compliance with IT asset management and cost controls
- **FFIEC Management Booklet** — Helps meet IT investment governance requirements
- **OCC Heightened Standards** — Supports technology cost governance expectations

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for license management automation
- See [Verification & Testing](verification-testing.md) to validate cost allocation
