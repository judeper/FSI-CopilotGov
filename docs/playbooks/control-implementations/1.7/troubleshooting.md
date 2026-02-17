# Control 1.7: SharePoint Advanced Management Readiness — Troubleshooting

Common issues and resolution steps for SharePoint Advanced Management configuration.

## Common Issues

### Issue 1: SAM Features Not Appearing After License Assignment

- **Symptoms:** SAM license is assigned but governance features like Restricted SharePoint Search or data access governance reports are not visible in the SharePoint Admin Center
- **Root Cause:** SAM feature provisioning can take 24-72 hours after license assignment. Additionally, the Admin Center may require a full page refresh or cache clear to display new features.
- **Resolution:**
  1. Verify the license is assigned at the tenant level in Admin Center > Billing
  2. Wait 72 hours for full feature provisioning
  3. Clear browser cache and sign out/in to the SharePoint Admin Center
  4. If features remain unavailable, verify the tenant region supports all SAM features
  5. Contact Microsoft support if features are not available after 72 hours

### Issue 2: Data Access Governance Reports Show Empty or Stale Data

- **Symptoms:** Reports load but show "No data available" or the data is significantly outdated
- **Root Cause:** Governance reports may require an initial processing period of up to 7 days to populate. Service-side processing delays or tenant configuration issues can also cause stale data.
- **Resolution:**
  1. Verify SAM license has been active for at least 7 days
  2. Check service health for any SharePoint-related processing delays
  3. Ensure the signed-in account has SharePoint Administrator role (lower roles may see limited data)
  4. If data remains unavailable after 7 days, open a Microsoft support ticket

### Issue 3: Lifecycle Policy Not Detecting Inactive Sites

- **Symptoms:** Sites known to be inactive are not flagged or site owners are not receiving notifications
- **Root Cause:** The `LastContentModifiedDate` property may update from system activities (e.g., flow operations, background jobs) even when no user activity occurs. Notifications may also be blocked by email filtering.
- **Resolution:**
  1. Verify the inactivity threshold is correctly set: `(Get-SPOTenant).InactivityThresholdDays`
  2. Check that notifications are enabled: `(Get-SPOTenant).InactivityNotificationEnabled`
  3. Verify site owner email addresses are valid and not blocked
  4. Cross-reference with Microsoft 365 usage reports for actual user activity
  5. Consider supplementing with custom PowerShell monitoring using audit log data

### Issue 4: Conditional Access Policy Conflicts

- **Symptoms:** SAM site-level conditional access policies conflict with tenant-level Entra ID conditional access policies, resulting in unexpected access behavior
- **Root Cause:** Multiple layers of conditional access (Entra ID tenant policy + SAM site policy) may create conflicting rules. The most restrictive policy typically wins.
- **Resolution:**
  1. Map all applicable conditional access policies for the affected site
  2. Verify the intended behavior when policies overlap
  3. Adjust SAM site-level policy to complement (not conflict with) Entra ID policies
  4. Test the combined policy effect from both managed and unmanaged devices
  5. Document the intended policy interaction for governance records

### Issue 5: Site Access Review Notifications Not Delivered

- **Symptoms:** Designated reviewers do not receive access review notifications, causing reviews to expire without completion
- **Root Cause:** Email notifications may be blocked by spam filters, the reviewer's mailbox may be full, or the notification configuration may be incorrect.
- **Resolution:**
  1. Check the reviewer's spam/junk folder for access review emails
  2. Verify the reviewer email address is correct in the review configuration
  3. Add Microsoft access review sender addresses to the organization's safe sender list
  4. Set up backup reviewers to handle cases where primary reviewers are unavailable
  5. Monitor review completion status and send manual reminders for overdue reviews

## Diagnostic Steps

1. **Verify licensing:** Confirm SAM license count and assignment in Admin Center
2. **Check feature status:** Run Script 1 to enumerate available SAM features
3. **Review configuration:** Compare current settings against documented baseline
4. **Test individual features:** Validate each SAM feature independently
5. **Check service health:** Review Microsoft 365 service health for SharePoint incidents

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Feature provisioning delays under 72 hours | Monitor and retest |
| **Medium** | Governance reports not populating after 7 days | Microsoft support ticket |
| **High** | Conditional access policies conflicting and causing access gaps | Security Operations and Identity team |
| **Critical** | SAM features non-functional affecting Copilot governance | Microsoft TAM and CISO |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — SAM configuration steps
- [PowerShell Setup](powershell-setup.md) — Automation scripts
- [Verification & Testing](verification-testing.md) — Validation procedures
