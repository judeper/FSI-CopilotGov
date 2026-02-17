# Control 1.9: License Planning and Assignment Strategy — Troubleshooting

Common issues and resolution steps for Copilot license management.

## Common Issues

### Issue 1: Group-Based License Assignment Errors

- **Symptoms:** Users in the deployment group do not receive Copilot licenses, or the group shows license assignment errors in Entra ID
- **Root Cause:** Insufficient available licenses, prerequisite license conflicts, or service plan dependency issues within the license bundle.
- **Resolution:**
  1. Navigate to Entra ID > Groups > [Group] > Licenses > check for errors
  2. Review the specific error message (common: "Not enough licenses", "Conflicting service plans")
  3. For insufficient licenses: Purchase additional licenses or reclaim from inactive users
  4. For service plan conflicts: Disable conflicting service plans in the license assignment
  5. Reprocess the group license assignment after resolving the error

### Issue 2: Copilot Not Available After License Assignment

- **Symptoms:** User has the Copilot license assigned but Copilot features do not appear in Office applications or Teams
- **Root Cause:** License propagation can take up to 24 hours. Additionally, the user may need to sign out and back in, or the Copilot feature may be restricted by a tenant-level toggle.
- **Resolution:**
  1. Verify the license is fully assigned (not in error state) in Entra ID
  2. Have the user sign out of all Office applications and sign back in
  3. Check that Copilot is enabled at the tenant level in Admin Center > Settings > Copilot
  4. Verify the user is not in the Copilot-Excluded-Users group
  5. Allow up to 24 hours for license propagation before escalating

### Issue 3: License Count Discrepancy Between Portal and PowerShell

- **Symptoms:** License counts from the Admin Center do not match PowerShell `Get-MgSubscribedSku` output
- **Root Cause:** Reporting data may have different refresh intervals. Grace period licenses or trial licenses may appear in one view but not the other.
- **Resolution:**
  1. Wait 24 hours and recheck — both sources should converge
  2. Filter out trial and grace period licenses from the comparison
  3. Use the PowerShell output as the authoritative source for automation
  4. If discrepancy persists, contact Microsoft billing support

### Issue 4: Users Losing Licenses Unexpectedly

- **Symptoms:** Users report Copilot features suddenly becoming unavailable; license checks show the license was removed
- **Root Cause:** The user may have been removed from the deployment group (manually or by a dynamic membership rule change), or a license reassignment script may have inadvertently removed the license.
- **Resolution:**
  1. Check the user's group membership history in Entra ID audit logs
  2. If using dynamic groups, verify the membership rule still matches the user
  3. Review recent PowerShell script execution logs for license modification commands
  4. Re-add the user to the appropriate deployment group
  5. Set up alerts on group membership changes for deployment groups

### Issue 5: Budget Tracking Challenges Across Departments

- **Symptoms:** Finance team cannot accurately allocate Copilot license costs to departments because license assignments are managed centrally
- **Root Cause:** Group-based license assignment does not inherently track departmental cost allocation.
- **Resolution:**
  1. Create department-specific deployment groups (e.g., Copilot-Finance, Copilot-Legal)
  2. Use PowerShell to generate department-level license utilization reports
  3. Cross-reference Copilot user lists with HR department data for cost allocation
  4. Implement a tagging system in the license management process for budget tracking

## Diagnostic Steps

1. **Check license status:** `Get-MgUser -UserId <upn> -Property AssignedLicenses`
2. **Verify group membership:** `Get-MgGroupMember -GroupId <id>` and confirm user is listed
3. **Review assignment errors:** Entra ID > Groups > [Group] > Licenses > error details
4. **Check tenant settings:** Admin Center > Settings > Microsoft 365 Copilot
5. **Review audit logs:** Search for license assignment events in Entra ID audit logs

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Individual user license delay under 24 hours | Monitor and retest |
| **Medium** | Group license assignment errors affecting multiple users | Identity and Access Management team |
| **High** | Widespread license loss affecting a deployment wave | IT Operations and License Administrator |
| **Critical** | License procurement or billing issues blocking deployment | Finance, IT leadership, and Microsoft account team |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — License management steps
- [PowerShell Setup](powershell-setup.md) — License automation scripts
- [Verification & Testing](verification-testing.md) — Validation procedures
