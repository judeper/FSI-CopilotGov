# Control 1.7: SharePoint Advanced Management Readiness — Troubleshooting

Common issues and resolution steps for SharePoint Advanced Management configuration.

## Common Issues

### Issue 1: SAM Features Not Appearing After License Assignment

- **Symptoms:** SAM governance features like Restricted Content Discovery, Restricted Access Control, or data access governance reports are not visible in the SharePoint admin center
- **Root Cause:** SAM feature provisioning can take 24-72 hours after license assignment or Copilot license activation. The Admin Center may require a full page refresh or cache clear to display new features.
- **Resolution:**
  1. **For Microsoft 365 Copilot license holders:** Verify the Copilot license is fully provisioned in Admin Center > Billing > Licenses. SAM is included with Copilot licenses — no additional purchase is required.
  2. **For standalone SAM add-on users:** Verify the license is assigned at the tenant level in Admin Center > Billing
  3. Wait 72 hours for full feature provisioning
  4. Clear browser cache and sign out/in to the SharePoint admin center
  5. If features remain unavailable, verify the tenant region supports all SAM features
  6. Contact Microsoft support if features are not available after 72 hours

### Issue 2: Data Access Governance Reports Show Empty or Stale Data

- **Symptoms:** Reports load but show "No data available" or the data is significantly outdated
- **Root Cause:** Governance reports may require an initial processing period of up to 7 days to populate. Service-side processing delays or tenant configuration issues can also cause stale data.
- **Resolution:**
  1. Verify SAM license has been active for at least 7 days
  2. Check service health for any SharePoint-related processing delays
  3. Ensure the signed-in account has SharePoint Admin role (lower roles may see limited data)
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

### Issue 6: Restricted Access Control Not Blocking Users with Sharing Links

- **Symptoms:** A user who holds a sharing link to a RAC-enabled site can still access the site content, despite not being in the designated security group
- **Root Cause:** RAC may not have been fully applied, or the security group configuration was incorrect during RAC setup. There may also be a propagation delay after RAC is enabled.
- **Resolution:**
  1. Verify RAC is enabled on the site: navigate to SharePoint admin center > Active Sites > [site] > Settings and confirm Restricted Access Control shows the correct security group
  2. Check that the designated security group contains the correct members and no broader groups that would inadvertently include the user
  3. Allow up to 30 minutes for RAC changes to propagate across SharePoint infrastructure
  4. If the issue persists, re-apply the RAC configuration: `Set-SPOSite -Identity <siteUrl> -RestrictedAccessControl $true -RestrictedAccessControlGroups <groupId>`
  5. Test access again after propagation delay

### Issue 7: RAC Breaking Legitimate Access Patterns

- **Symptoms:** After enabling RAC, users who should have access to the site are being blocked (e.g., site contributors, guest collaborators)
- **Root Cause:** RAC replaces all other access methods with the security group boundary. Users who previously had access through direct permissions, sharing links, or group memberships will lose access if they are not members of the RAC security group.
- **Resolution:**
  1. Review the membership of the designated security group and add any users or groups who should retain access
  2. For guest collaborators: Guests cannot typically be added to standard security groups -- use Entra ID external user groups or SharePoint site membership instead
  3. Communicate RAC changes to site owners in advance of enabling, allowing them to nominate security group members
  4. Consider a phased rollout: enable RAC in read-only mode or on a test copy of the site before applying to production

## Diagnostic Steps

1. **Verify licensing:** Confirm SAM license availability -- for Copilot organizations, confirm Copilot license is provisioned; for non-Copilot organizations, confirm standalone SAM add-on
2. **Check feature status:** Run Script 1 to enumerate available SAM features
3. **Review configuration:** Compare current settings against documented baseline
4. **Test individual features:** Validate each SAM feature independently (RCD, RAC, lifecycle, access reviews)
5. **Check service health:** Review Microsoft 365 service health for SharePoint incidents

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Feature provisioning delays under 72 hours | Monitor and retest |
| **Medium** | Governance reports not populating after 7 days | Microsoft support ticket |
| **Medium** | RAC propagation delay exceeding 2 hours | Verify configuration, wait, then Microsoft support if persistent |
| **High** | Conditional access policies conflicting and causing access gaps | Security Operations and Identity team |
| **High** | RAC misconfiguration exposing NPI or MNPI to unauthorized users | Information Security team -- treat as data exposure incident |
| **Critical** | SAM features non-functional affecting Copilot governance | Microsoft TAM and CISO |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — SAM configuration steps including RCD and RAC
- [PowerShell Setup](powershell-setup.md) — Automation scripts including RAC bulk configuration
- [Verification & Testing](verification-testing.md) — Validation procedures for all SAM features
