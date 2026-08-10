# Control 2.12: External Sharing and Guest Access Governance — Troubleshooting

Common issues and resolution steps for external sharing and guest access controls.

## Common Issues

### Issue 1: Site-Level Sharing Overriding Tenant Policy

- **Symptoms:** External sharing is possible on certain sites despite tenant-level restrictions
- **Root Cause:** Site-level sharing can be more restrictive but not more permissive than tenant settings. If a site appears more permissive, the tenant setting may not be as restrictive as expected.
- **Resolution:**
  1. Verify tenant-level sharing: `(Get-SPOTenant).SharingCapability`
  2. Verify site-level sharing: `(Get-SPOSite -Identity <url>).SharingCapability`
  3. Set tenant to the desired restriction level
  4. Override permissive site settings: `Set-SPOSite -Identity <url> -SharingCapability Disabled`

### Issue 2: Guest Access Reviews Not Removing Denied Access

- **Symptoms:** Access reviews complete but denied guest users retain access
- **Root Cause:** Auto-apply may not be configured, the review may target the wrong resource, there may be a processing delay, or the guest may retain access through another Microsoft 365 group, security group, Team, application, direct permission, or sharing link. The all-Microsoft-365-groups review mode cannot delete guest accounts.
- **Resolution:**
  1. Verify auto-apply is enabled on the access review
  2. Wait 24-48 hours after review completion for processing
  3. Manually apply results if auto-apply is not configured
  4. Verify the denied user's membership has been removed from the reviewed resource, then reconcile every other group, Team, application, direct permission, and sharing-link access path
  5. If a tenant-wide account block or deletion is required, start a separate dedicated guest-lifecycle review; verify all direct, group, Teams, SharePoint, application, and other engagements are obsolete and obtain the tenant's required approvals before taking the account-level action

### Issue 3: Legitimate External Collaboration Blocked

- **Symptoms:** Business teams cannot collaborate with approved external partners due to sharing restrictions
- **Root Cause:** Overly restrictive policies may block legitimate collaboration scenarios.
- **Resolution:**
  1. Create approved external domains in Entra ID external collaboration settings
  2. Use specific site collections with controlled external sharing for collaboration
  3. Keep Copilot-scoped sites restricted while allowing sharing on dedicated collaboration sites
  4. Document exceptions with governance approval

### Issue 4: Guest Accounts Accumulating Without Review

- **Symptoms:** Large numbers of guest accounts exist without recent activity or review
- **Root Cause:** No automated lifecycle management for guest accounts.
- **Resolution:**
  1. Configure SharePoint/OneDrive guest-access expiration for eligible sharing-link access and direct site permissions granted after enablement; this does not alter or delete the Entra guest account
  2. Reconcile pre-existing access and access through Microsoft 365 groups, security groups, and Teams because those paths can survive SharePoint expiration
  3. Run the guest inventory script to identify stale account candidates
  4. Establish a monthly guest access review process
  5. If an account-level action is required, use a separate dedicated guest-lifecycle review after confirming every access path and active engagement is obsolete; do not elevate a resource-review denial into a tenant-wide decision

### Issue 5: Guest Still Has Access After SharePoint Expiration

- **Symptoms:** A guest has passed the SharePoint expiration date but can still open a group-connected site, Team, or related content
- **Root Cause:** Microsoft's guest-expiration policy applies only to sharing-link access and direct site permissions granted after the policy is enabled. Pre-existing permissions and access inherited through Microsoft 365 groups, security groups, or Teams can remain.
- **Resolution:**
  1. Confirm when the expiration policy was enabled and when the direct or sharing-link permission was granted
  2. Export the guest's direct and transitive group memberships and identify Microsoft 365 groups and security groups
  3. Review Teams membership and connected-site access
  4. Remove or renew each access path according to the approved engagement, then retest the site and Team

## Diagnostic Steps

1. **Check tenant sharing:** `(Get-SPOTenant).SharingCapability`
2. **Audit sites:** Run Script 1 for site-level sharing status
3. **Check resource expiration:** Review `ExternalUserExpirationRequired`, `ExternalUserExpireInDays`, the policy enablement date, and site overrides
4. **Review guests:** Run Script 3 for guest account inventory
5. **Check surviving access paths:** Review direct permissions, sharing links, Microsoft 365 groups, security groups, Teams, and applications
6. **Check reviews:** Verify Entra ID access-review scope and post-review actions
7. **Test sharing:** Attempt external sharing on key sites

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Guest account cleanup needed | IT Operations |
| **Medium** | Sharing restrictions blocking legitimate collaboration | Governance committee |
| **High** | Unauthorized external sharing detected on sensitive sites | Security Operations |
| **Critical** | Regulated data shared externally via Copilot-accessible sites | CISO and Compliance Officer |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Sharing configuration
- [PowerShell Setup](powershell-setup.md) — Guest management scripts
- [Verification & Testing](verification-testing.md) — Sharing control validation
- Back to [Control 2.12](../../../controls/pillar-2-security/2.12-external-sharing-governance.md)
