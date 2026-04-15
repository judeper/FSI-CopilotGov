# Control 1.6: Permission Model Audit — Troubleshooting

Common issues and resolution steps for permission model auditing.

## Common Issues

### Issue 1: Permission Audit Script Timeouts on Large Tenants

- **Symptoms:** Script 1 fails or times out when processing tenants with thousands of SharePoint sites
- **Root Cause:** Iterating through all sites with detailed permission checks exceeds default timeout thresholds. API throttling may also slow execution.
- **Resolution:**
  1. Process sites in batches of 100-200 using `-Top` and skip parameters
  2. Add `Start-Sleep -Seconds 2` between site checks to avoid throttling
  3. Run the script during off-peak hours (weekends or after business hours)
  4. Use Azure Automation with extended timeout configurations for tenant-wide scans

### Issue 2: Access Reviews Not Auto-Applying Denials

- **Symptoms:** Access review completes but denied users still have access to resources
- **Root Cause:** The access review may not have "Auto-apply results" enabled, or there may be a delay in applying denial results to underlying group memberships.
- **Resolution:**
  1. Verify the access review configuration has "Auto-apply results to resource" enabled
  2. Check that "If reviewers don't respond" action is set to an appropriate default
  3. Allow 24-48 hours after review completion for changes to propagate
  4. Manually apply results if auto-apply is not configured: Access Reviews > [Review] > Apply results

### Issue 3: Inherited Permissions Masking Direct Grants

- **Symptoms:** Permission audit shows clean results at the site level, but users report accessing content they should not have access to
- **Root Cause:** Unique permissions set at the library, folder, or item level may grant access that is not visible in site-level scans. SharePoint permission inheritance breaks are not captured by basic site-level audits.
- **Resolution:**
  1. Use PnP PowerShell to scan for items with broken inheritance: `Get-PnPListItem -List "Documents" | Where-Object { $_.HasUniqueRoleAssignments }`
  2. Run Script 3 (Sharing Links Inventory) on the affected site
  3. For critical sites, perform a deep permission scan at the item level
  4. Consider resetting permissions to inherit from parent and re-applying access intentionally

### Issue 4: Dynamic Group Membership Rule Producing Incorrect Results

- **Symptoms:** Dynamic security groups include or exclude users unexpectedly, causing permission anomalies
- **Root Cause:** Dynamic membership rules may reference user attributes that are not consistently maintained in Entra ID (e.g., department, job title, location).
- **Resolution:**
  1. Review the dynamic rule: `Get-MgGroup -GroupId <id> -Property MembershipRule`
  2. Validate the user attributes the rule depends on are populated correctly in Entra ID
  3. Test the rule with specific users using the "Validate rules" feature in Entra ID
  4. Correct user attribute data or adjust the dynamic rule to match actual attribute values

### Issue 5: Guest Users Retained After Project Completion

- **Symptoms:** External guest users still have access to SharePoint sites and Teams after the business engagement has ended
- **Root Cause:** Guest access is typically not automatically revoked when a project ends. Without regular access reviews, guest accounts persist indefinitely.
- **Resolution:**
  1. Configure guest access reviews in Entra ID Identity Governance
  2. Set guest access expiration policies using `Set-MgPolicyAuthorizationPolicy`
  3. Run a guest user audit: `Get-MgUser -Filter "userType eq 'Guest'"` and review against active engagements
  4. Remove stale guest access and block sign-in for departed external collaborators

### Issue 6: PnP PowerShell Connection Failures

- **Symptoms:** `Connect-PnPOnline` fails with "Application not found" or "AADSTS700016" errors
- **Root Cause:** The shared multi-tenant PnP Management Shell app was deleted on September 9, 2024. Scripts that do not specify `-ClientId` with a tenant-specific app registration will fail.
- **Resolution:**
  1. Complete the one-time app registration described in the PowerShell Setup Prerequisites: `Register-PnPEntraIDAppForInteractiveLogin`
  2. Add `-ClientId <your-app-id>` to all `Connect-PnPOnline` calls
  3. Verify the app registration exists: Microsoft Entra admin center > App registrations > All applications > search for "PnP Governance Shell"
  4. If the app registration was accidentally deleted, re-run `Register-PnPEntraIDAppForInteractiveLogin` to create a new one

### Issue 7: DSPM Role Not Visible in Purview Portal

- **Symptoms:** "Purview Data Security AI Viewer" or "Purview Data Security AI Content Viewer" role groups do not appear in Purview portal > Settings > Roles and scopes
- **Root Cause:** These roles require Microsoft Purview with DSPM for AI enabled. The roles may not be visible if the tenant does not have an appropriate Purview license, or if DSPM for AI has not been activated.
- **Resolution:**
  1. Verify the tenant has Microsoft Purview enabled with appropriate licensing (E5 Compliance or Microsoft 365 E5)
  2. Navigate to Microsoft Purview portal > Data Security Posture Management to verify DSPM for AI is accessible
  3. If DSPM for AI is not yet enabled, work with your Microsoft account team to enable it
  4. Note: The AI Administrator role is an Entra ID role (not a Purview role) and is managed separately in Microsoft Entra admin center > Roles and administrators

## Diagnostic Steps

1. **Quick permission check:** Use the SharePoint Admin Center "Check access" feature for individual sites
2. **Compare methods:** Cross-reference portal permission display with PowerShell output for accuracy
3. **Review audit trail:** Search for permission changes in the unified audit log
4. **Test as affected user:** Use a non-admin account to verify actual access matches expected access
5. **Check nested groups:** Trace group membership chains to identify indirect access paths

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor permission discrepancies on non-sensitive sites | IT Operations for review |
| **Medium** | Access review non-completion or delayed auto-apply | Identity and Access Management team |
| **High** | Unauthorized access to sensitive content discovered | Security Operations for investigation |
| **High** | Unauthorized assignment to AI Content Viewer role discovered | Information Security and Compliance team — this role grants access to Copilot prompt/response content |
| **Critical** | Widespread permission model failure across sensitive sites | CISO and governance committee immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Audit procedure reference
- [PowerShell Setup](powershell-setup.md) — Audit automation scripts
- [Verification & Testing](verification-testing.md) — Validation procedures
- Back to [Control 1.6: Permission Model Audit](../../../controls/pillar-1-readiness/1.6-permission-model-audit.md)
