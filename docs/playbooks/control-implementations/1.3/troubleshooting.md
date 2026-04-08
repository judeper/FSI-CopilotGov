# Control 1.3: Restricted SharePoint Search and Restricted Content Discovery — Troubleshooting

Common issues and resolution steps for Restricted SharePoint Search (RSS) and Restricted Content Discovery (RCD) configuration.

## Common Issues

### Issue 1: RSS or RCD Not Available in SharePoint Admin Center

- **Symptoms:** The Restricted SharePoint Search option does not appear under Settings > Search, or `Set-SPOSite -RestrictContentOrgWideSearch` returns "unrecognized parameter" or "property not found"
- **Root Cause:** Both RSS and RCD require SharePoint Advanced Management (SAM) licensing. SAM is included with Microsoft 365 Copilot licenses at no additional cost; tenants without Copilot licenses need the standalone SAM add-on. Older versions of the SPO Management Shell may not include RCD or RSS cmdlets.
- **Resolution:**
  1. Verify SharePoint Advanced Management is licensed and activated in the tenant (check Microsoft 365 Admin Center > Billing > Licenses)
  2. Update the SharePoint Online Management Shell to the latest version: `Update-Module Microsoft.Online.SharePoint.PowerShell`
  3. If SAM is licensed but features are not visible, check your tenant's release ring and allow 24-48 hours for feature propagation
  4. Contact Microsoft support if the feature remains unavailable after licensing and module updates

### Issue 1b: RCD-Enabled Site Content Still Appearing in Copilot

- **Symptoms:** After enabling `RestrictContentOrgWideSearch` on a site, Copilot still surfaces content from that site
- **Root Cause:** RCD configuration changes require time to propagate through the search index, similar to RSS changes. Additionally, content may be cached in Copilot's retrieval layer.
- **Resolution:**
  1. Wait 24 hours after enabling RCD before testing — changes may take up to 24 hours to propagate
  2. Verify the setting was saved: `(Get-SPOSite -Identity <url>).RestrictContentOrgWideSearch` should return `True`
  3. Clear the user's browser cache and sign out/in to Microsoft 365 before retesting
  4. Note: RCD does not affect content already in Copilot's active context window — test with a fresh Copilot session
  5. If RCD is not working after 48 hours, check service health for search indexing delays

### Issue 2: Allowed List Changes Not Reflected in Search Results

- **Symptoms:** After adding or removing sites from the allowed list, search results do not immediately reflect the changes
- **Root Cause:** RSS allowed list changes require time to propagate through the search index. Changes may take up to 24 hours to take full effect across all search endpoints and Copilot grounding.
- **Resolution:**
  1. Wait 24 hours after making allowed list changes before testing
  2. Verify the change was saved by running `Get-SPOTenantRestrictedSearchAllowedList`
  3. Clear the user's browser cache and sign out/in to Microsoft 365
  4. If changes are not reflected after 24 hours, check service health for search indexing delays

### Issue 3: 100-Site Allowed List Limit Reached

- **Symptoms:** Attempting to add a site to the allowed list fails with a limit error, or the `Add-SPOTenantRestrictedSearchAllowedList` cmdlet returns an error about maximum capacity
- **Root Cause:** RSS initially supports a maximum of 100 sites in the allowed list. Organizations with more than 100 sites that need Copilot access will hit this limit.
- **Resolution:**
  1. Review the current allowed list and remove sites that are no longer needed
  2. Consolidate content into fewer sites where feasible
  3. Prioritize sites based on business need and governance risk assessment
  4. Check Microsoft documentation for updated limits as this cap may increase
  5. Consider using DSPM for AI and granular permissions instead of RSS if the limit is too restrictive

### Issue 4: Users Report Missing Search Results from Allowed Sites

- **Symptoms:** Users cannot find content from sites that are on the allowed list
- **Root Cause:** RSS controls search scope at the tenant level, but individual user permissions still apply. Users without access to an allowed site will not see its content in search results.
- **Resolution:**
  1. Verify the user has at least read access to the site in question
  2. Check that the content has been indexed by searching directly within the site
  3. Verify the site URL in the allowed list matches exactly (no trailing slashes or variations)
  4. Request a re-index of the site if content was recently added: `Request-SPOReIndex -Identity <siteUrl>`

### Issue 5: RSS Accidentally Disabled

- **Symptoms:** Users suddenly report seeing search results from sites that were previously restricted
- **Root Cause:** An administrator may have toggled RSS off via the admin center or PowerShell, or a service update may have reset the setting.
- **Resolution:**
  1. Immediately re-enable RSS: `Set-SPOTenantRestrictedSearchMode -Mode Enabled`
  2. Verify the allowed list is intact: `Get-SPOTenantRestrictedSearchAllowedList`
  3. Review the audit log for who changed the setting: `Search-UnifiedAuditLog -Operations "Set-SPOTenantRestrictedSearchMode"`
  4. Implement alerting on RSS configuration changes to detect future unauthorized modifications

## Diagnostic Steps

1. **Check RSS mode:** `Get-SPOTenantRestrictedSearchMode` should return "Restricted"
2. **Verify allowed list:** `Get-SPOTenantRestrictedSearchAllowedList` returns expected sites
3. **Test as specific user:** Use a non-admin account to test search behavior
4. **Review audit logs:** Search for RSS-related admin operations in unified audit log
5. **Check search health:** Verify the SharePoint search service is healthy in the admin dashboard

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Propagation delay on allowed list changes | Monitor and retest after 24 hours |
| **Medium** | Site limit reached, blocking approved additions | Governance committee for prioritization |
| **High** | RSS found disabled without authorization | Security Operations for investigation |
| **Critical** | Copilot returning content from non-allowed sites | Security Operations and CISO immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Configuration reference
- [PowerShell Setup](powershell-setup.md) — Allowed list management scripts
- [Verification & Testing](verification-testing.md) — Validation procedures
