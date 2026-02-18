# Control 4.8: Cost Allocation and License Optimization — Troubleshooting

Common issues and resolution steps for Copilot cost allocation and license optimization.

## Common Issues

### Issue 1: PAYG Costs Not Appearing in Azure Billing

- **Symptoms:** PAYG Copilot Chat billing has been enabled, but no charges appear in Azure Cost Management or the Azure invoice for the current month.
- **Root Cause:** Azure billing for PAYG services typically has a 24–48 hour delay before charges appear in Cost Management. Alternatively, PAYG may not be correctly linked to the Azure subscription, or the Azure subscription and Microsoft 365 tenant may not be properly associated.
- **Resolution:**
  1. Allow 48 hours after the first known PAYG usage event before expecting charges to appear in Azure Cost Management.
  2. Verify the Azure subscription is linked to the correct Microsoft 365 tenant: in **Azure Portal > Subscriptions > [subscription] > Properties**, confirm the tenant ID matches your Microsoft 365 tenant.
  3. Confirm PAYG Copilot Chat is enabled: in **Microsoft 365 Admin Center > Billing > Your products**, verify Microsoft 365 Copilot Chat (pay-as-you-go) appears as an active product.
  4. Run Script 1 from the PowerShell Setup guide — if the Azure Commerce API returns no data, the subscription association or PAYG enablement is the root cause.
  5. If the issue persists after 48 hours, open a Microsoft billing support ticket referencing the Azure subscription ID and the PAYG product name.

### Issue 2: Budget Caps Not Enforcing for PAYG Spending

- **Symptoms:** Azure Cost Management budget caps have been configured, but alerts are not being triggered when spending approaches or exceeds the configured limits.
- **Root Cause:** Budget cap enforcement in Azure Cost Management sends alerts but does not automatically block spending — it is advisory only. Alternatively, the budget scope may not match the Azure resource scope where PAYG charges are being tracked.
- **Resolution:**
  1. Confirm the budget scope: in **Azure Portal > Cost Management > Budgets**, verify the budget is scoped to the correct subscription, resource group, or management group that contains PAYG Copilot Chat charges.
  2. Verify the alert recipient email addresses are correct and check spam/junk folders for missed alerts.
  3. Understand that Azure Cost Management budgets are alert-based, not enforcement-based — to prevent spending above the cap, additional Azure Policy controls or PAYG access revocation procedures are needed.
  4. For hard enforcement: establish a process to immediately disable PAYG access for a user group if its monthly budget is reached, pending management approval for reactivation.
  5. Run Script 2 from the PowerShell Setup guide to review the budget configuration and confirm thresholds are set correctly.

### Issue 3: PAYG Cost Allocation Tags Not Propagating

- **Symptoms:** Azure Cost Management cost analysis shows PAYG Copilot Chat charges as "Untagged" or attributed to the wrong cost center, despite tag policies being in place.
- **Root Cause:** Azure resource tags must be applied to the Azure subscription or resource group that receives the PAYG charges. If tags are applied at the wrong scope or tags are not inherited by the PAYG billing resource, costs appear untagged.
- **Resolution:**
  1. In **Azure Portal > Subscriptions > [subscription] > Tags**, verify that department and cost center tags are applied at the subscription level.
  2. Enable tag inheritance in **Azure Policy**: create an Azure Policy initiative that inherits subscription tags to all resources, including PAYG billing resources.
  3. In **Azure Cost Management > Cost analysis**, filter by "Untagged" and review the resource IDs to identify the untagged PAYG resources.
  4. Manually apply tags to identified resources and allow 24 hours for tag propagation to appear in cost analysis.
  5. For ongoing tag compliance, configure an Azure Policy assignment that audits or enforces required tags on all resources in the PAYG subscription.

### Issue 4: Group-Based Licensing Assignment Failures

- **Symptoms:** Users added to a license group do not receive the Copilot license, or errors appear in the group licensing status.
- **Root Cause:** Insufficient available licenses, conflicting service plans, or the user already has a direct license assignment.
- **Resolution:**
  1. Check group licensing status in Entra Admin Center: look for error indicators on the group.
  2. Verify sufficient Copilot licenses are available (not all consumed).
  3. Check for conflicting service plan assignments that prevent the Copilot license from being added.
  4. If the user has a direct assignment, remove it before adding via group-based licensing.

### Issue 5: Chargeback Allocations Do Not Match Finance Records

- **Symptoms:** Department chargeback totals from the license report do not match what finance has budgeted or invoiced.
- **Root Cause:** User department attributes in Entra ID may be outdated, or the chargeback calculation uses different rates.
- **Resolution:**
  1. Audit Entra ID department attributes against HR records.
  2. Update stale department assignments for users who have moved teams.
  3. Align the per-user cost rate with the contracted license price.
  4. Reconcile the total license count with the Microsoft invoice.

### Issue 6: Underutilization Report Flagging Active Users

- **Symptoms:** The underutilization report flags users as inactive who claim they are regularly using Copilot.
- **Root Cause:** Usage reporting data may have a 48-hour delay, or the user is using Copilot features that are not tracked in the standard usage report.
- **Resolution:**
  1. Allow 48 hours after the last activity before flagging as inactive.
  2. Cross-reference with the unified audit log for Copilot interaction events.
  3. Verify the user is using Copilot in tracked applications (not just Microsoft 365 Copilot Chat in browser).
  4. Implement a grace period before license reallocation (e.g., 60 days instead of 30).

### Issue 7: License Reallocation Disrupting Active Users

- **Symptoms:** A user who had their Copilot license removed reports they were actively using the service.
- **Root Cause:** The underutilization threshold may be too aggressive, or the user's activity pattern is intermittent but legitimate.
- **Resolution:**
  1. Immediately reassign the Copilot license to the affected user.
  2. Review the reallocation criteria and adjust thresholds (consider 60 or 90 day inactivity).
  3. Implement an approval workflow requiring manager confirmation before license removal.
  4. Add a notification step that warns users before license removal (e.g., 14-day notice).

## Diagnostic Steps

1. **Check license availability:** `Get-MgSubscribedSku | Where SkuPartNumber -like "*Copilot*"`
2. **Verify PAYG enabled:** Confirm in Microsoft 365 Admin Center > Billing > Your products that PAYG Copilot Chat is listed as active.
3. **Check Azure subscription link:** Confirm the Azure subscription is associated with the correct Microsoft 365 tenant (Azure Portal > Subscriptions > Properties > Directory).
4. **Review group licensing errors:** Check the group's licensing status in Entra Admin Center.
5. **Verify department data:** `Get-MgUser -UserId "user@contoso.com" -Property Department`
6. **Check PAYG billing delay:** PAYG charges have a 24–48 hour delay; cost tag propagation takes up to 24 hours.
7. **Test usage data freshness:** Compare the report date with the current date.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| High | PAYG budget cap breached without alert — possible overspend | IT Finance + Management — review and reauthorize |
| High | License reallocation disrupting active users | IT Admin — immediate reassignment |
| Medium | PAYG costs not appearing after 48 hours | IT Admin + Microsoft Billing Support — subscription association |
| Medium | Group licensing failures | IT Admin — investigate and resolve |
| Medium | Chargeback discrepancies with finance (per-seat or PAYG) | IT + Finance — reconciliation |
| Medium | PAYG tag propagation failures — untagged costs | IT Admin — Azure Policy enforcement |
| Low | Minor reporting delays | Monitor and report at next cycle |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.5: Copilot Usage Analytics](../4.5/portal-walkthrough.md)
