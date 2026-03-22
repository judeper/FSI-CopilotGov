# Control 4.8: Cost Allocation and License Optimization — Troubleshooting

Common issues and resolution steps for Copilot cost allocation and license optimization.

## Common Issues

### Issue 1: PAYG Costs Not Appearing in Azure Billing

- **Symptoms:** PAYG Copilot Chat billing has been enabled, but no charges appear in Azure Cost Management or the Azure invoice for the current month.
- **Root Cause:** PAYG might not be correctly connected through a billing policy, the wrong users or groups may be covered, or the Azure subscription and Microsoft 365 tenant might not be properly associated.
- **Resolution:**
  1. Allow for normal billing-report refresh if usage began recently.
  2. Verify the Azure subscription is linked to the correct Microsoft 365 tenant: in **Azure Portal > Subscriptions > [subscription] > Properties**, confirm the tenant ID matches your Microsoft 365 tenant.
  3. Confirm the billing policy is connected to the intended service in **Microsoft 365 Admin Center > Billing > Pay-as-you-go services**.
  4. Verify the intended users or groups are covered by the billing policy.
  5. Run Script 1 from the PowerShell Setup guide — if the Azure Commerce API returns no data, the subscription association or billing-policy setup is the likely root cause.
  6. If the issue persists after the expected billing refresh, open a Microsoft billing support ticket referencing the Azure subscription ID and the PAYG product name.

### Issue 2: Budget Notifications Not Triggering as Expected

- **Symptoms:** PAYG budgets exist, but business or finance owners aren't receiving the expected notifications.
- **Root Cause:** Notification recipients might be incorrect, the wrong billing policy might be under review, or the budget wasn't configured on the active billing policy.
- **Resolution:**
  1. Review the active billing policy in **Billing > Pay-as-you-go services**.
  2. Confirm the budget and notification recipients are configured for that policy.
  3. Verify the finance and business-owner addresses are current.
  4. Confirm the policy is tied to the expected Azure subscription and service.
  5. Run Script 2 from the PowerShell Setup guide to review existing budget objects.

### Issue 3: Costs Can't Be Mapped to the Correct Cost Owner

- **Symptoms:** PAYG charges appear in Cost Management, but finance can't determine which department or approved population should own them.
- **Root Cause:** Billing policy ownership was not documented clearly, or users and groups were added to the wrong billing policy.
- **Resolution:**
  1. Review **Microsoft 365 Admin Center > Billing > Pay-as-you-go services**.
  2. Confirm the billing policy owner, covered users or groups, and connected service.
  3. Compare policy coverage with the current finance cost center mapping.
  4. Move users or groups to the correct billing policy if needed and document the change.
  5. Retain the corrected mapping in the governance register.

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
- **Root Cause:** User department attributes in Entra ID may be outdated, the chargeback calculation uses different rates, or PAYG policy ownership is mapped incorrectly.
- **Resolution:**
  1. Audit Entra ID department attributes against HR records.
  2. Update stale department assignments for users who have moved teams.
  3. Align the per-user cost rate with the contracted license price.
  4. Reconcile the total license count with the Microsoft invoice.
  5. Reconcile PAYG charges with the documented billing policy owner.

### Issue 6: Underutilization Report Flagging Active Users

- **Symptoms:** The underutilization report flags users as inactive who claim they are regularly using Copilot.
- **Root Cause:** Usage reporting data may have a delay, or the user is using Copilot features that aren't fully reflected in the standard report.
- **Resolution:**
  1. Allow 48 hours after the last activity before flagging as inactive.
  2. Cross-reference with the unified audit log for Copilot interaction events.
  3. Verify the user is using Copilot in tracked applications.
  4. Implement a grace period before license reallocation (for example, 60 days instead of 30).

### Issue 7: License Reallocation Disrupting Active Users

- **Symptoms:** A user who had their Copilot license removed reports they were actively using the service.
- **Root Cause:** The underutilization threshold may be too aggressive, or the user's activity pattern is intermittent but legitimate.
- **Resolution:**
  1. Immediately reassign the Copilot license to the affected user.
  2. Review the reallocation criteria and adjust thresholds.
  3. Implement an approval workflow requiring manager confirmation before license removal.
  4. Add a notification step that warns users before license removal.

## Diagnostic Steps

1. **Check license availability:** `Get-MgSubscribedSku | Where SkuPartNumber -like "*Copilot*"`
2. **Verify PAYG enabled:** Confirm in Microsoft 365 Admin Center > Billing > Pay-as-you-go services that the billing policy is connected to the intended service.
3. **Check Azure subscription link:** Confirm the Azure subscription is associated with the correct Microsoft 365 tenant (Azure Portal > Subscriptions > Properties > Directory).
4. **Review group licensing errors:** Check the group's licensing status in Entra Admin Center.
5. **Verify department data:** `Get-MgUser -UserId "user@contoso.com" -Property Department`
6. **Check PAYG billing timing:** Allow for normal billing-report refresh and confirm policy coverage before escalating.
7. **Test usage data freshness:** Compare the report date with the current date.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| High | PAYG spend exceeds approved expectation without notification | IT Finance + Management — review billing policy and reauthorize if needed |
| High | License reallocation disrupting active users | IT Admin — immediate reassignment |
| Medium | PAYG costs not appearing after expected billing refresh | IT Admin + Microsoft Billing Support — subscription association |
| Medium | Group licensing failures | IT Admin — investigate and resolve |
| Medium | Chargeback discrepancies with finance (per-seat or PAYG) | IT + Finance — reconciliation |
| Medium | PAYG costs can't be mapped to approved cost owner | IT Admin + Finance — review billing policy mapping |
| Low | Minor reporting delays | Monitor and report at next cycle |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.5: Copilot Usage Analytics](../4.5/portal-walkthrough.md)
