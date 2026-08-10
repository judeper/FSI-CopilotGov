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
- **Root Cause:** Auto-apply may not be configured, the review may target the wrong resource, or there may be a processing delay. The all-Microsoft-365-groups review mode cannot delete guest accounts.
- **Resolution:**
  1. Verify auto-apply is enabled on the access review
  2. Wait 24-48 hours after review completion for processing
  3. Manually apply results if auto-apply is not configured
  4. Verify the denied user's group membership has been removed
  5. If tenant-account deletion is required, verify the review uses **Select Teams + groups**, **If reviewers don't respond** is **Remove access**, and **Action to apply on denied guest users** is **Block user from signing-in for 30 days, then remove user from the tenant**

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
  1. Configure SharePoint/OneDrive guest-access expiration for resource access; this does not alter or delete the Entra guest account
  2. Run the guest inventory script to identify stale account candidates
  3. Establish a monthly guest access review process
  4. If account deletion is required, use the specifically configured **Select Teams + groups** review described above; do not rely on the all-groups review mode

## Diagnostic Steps

1. **Check tenant sharing:** `(Get-SPOTenant).SharingCapability`
2. **Audit sites:** Run Script 1 for site-level sharing status
3. **Check resource expiration:** Review `ExternalUserExpirationRequired` and `ExternalUserExpireInDays`
4. **Review guests:** Run Script 3 for guest account inventory
5. **Check reviews:** Verify Entra ID access-review scope and post-review actions
6. **Test sharing:** Attempt external sharing on key sites

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
