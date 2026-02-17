# Control 4.8: Cost Allocation and License Optimization — Troubleshooting

Common issues and resolution steps for Copilot cost allocation and license optimization.

## Common Issues

### Issue 1: Group-Based Licensing Assignment Failures

- **Symptoms:** Users added to a license group do not receive the Copilot license, or errors appear in the group licensing status.
- **Root Cause:** Insufficient available licenses, conflicting service plans, or the user already has a direct license assignment.
- **Resolution:**
  1. Check group licensing status in Entra Admin Center: look for error indicators on the group.
  2. Verify sufficient Copilot licenses are available (not all consumed).
  3. Check for conflicting service plan assignments that prevent the Copilot license from being added.
  4. If the user has a direct assignment, remove it before adding via group-based licensing.

### Issue 2: Chargeback Allocations Do Not Match Finance Records

- **Symptoms:** Department chargeback totals from the license report do not match what finance has budgeted or invoiced.
- **Root Cause:** User department attributes in Azure AD may be outdated, or the chargeback calculation uses different rates.
- **Resolution:**
  1. Audit Azure AD department attributes against HR records.
  2. Update stale department assignments for users who have moved teams.
  3. Align the per-user cost rate with the contracted license price.
  4. Reconcile the total license count with the Microsoft invoice.

### Issue 3: Underutilization Report Flagging Active Users

- **Symptoms:** The underutilization report flags users as inactive who claim they are regularly using Copilot.
- **Root Cause:** Usage reporting data may have a 48-hour delay, or the user is using Copilot features that are not tracked in the standard usage report.
- **Resolution:**
  1. Allow 48 hours after the last activity before flagging as inactive.
  2. Cross-reference with the unified audit log for Copilot interaction events.
  3. Verify the user is using Copilot in tracked applications (not just Copilot Chat in browser).
  4. Implement a grace period before license reallocation (e.g., 60 days instead of 30).

### Issue 4: License Reallocation Disrupting Active Users

- **Symptoms:** A user who had their Copilot license removed reports they were actively using the service.
- **Root Cause:** The underutilization threshold may be too aggressive, or the user's activity pattern is intermittent but legitimate.
- **Resolution:**
  1. Immediately reassign the Copilot license to the affected user.
  2. Review the reallocation criteria and adjust thresholds (consider 60 or 90 day inactivity).
  3. Implement an approval workflow requiring manager confirmation before license removal.
  4. Add a notification step that warns users before license removal (e.g., 14-day notice).

## Diagnostic Steps

1. **Check license availability:** `Get-MgSubscribedSku | Where SkuPartNumber -like "*Copilot*"`
2. **Review group licensing errors:** Check the group's licensing status in Entra Admin Center.
3. **Verify department data:** `Get-MgUser -UserId "user@contoso.com" -Property Department`
4. **Test usage data freshness:** Compare the report date with the current date.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| High | License reallocation disrupting active users | IT Admin — immediate reassignment |
| Medium | Group licensing failures | IT Admin — investigate and resolve |
| Medium | Chargeback discrepancies with finance | IT + Finance — reconciliation |
| Low | Minor reporting delays | Monitor and report at next cycle |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.5: Copilot Usage Analytics](../4.5/portal-walkthrough.md)
