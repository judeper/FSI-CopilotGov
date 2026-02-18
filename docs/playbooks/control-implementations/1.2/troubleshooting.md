# Control 1.2: SharePoint Oversharing Detection (DSPM for AI) — Troubleshooting

Common issues and resolution steps for SharePoint oversharing detection using DSPM for AI.

## Common Issues

### Issue 1: PnP PowerShell "Application not registered" or Authentication Failure

- **Symptoms:** `Connect-PnPOnline -Interactive` fails with "Application is not registered" or "AADSTS700016: Application with identifier '31359c7f-...' was not found in the directory"
- **Root Cause:** The shared multi-tenant PnP Management Shell Entra ID app (App ID `31359c7f-...`) was retired September 9, 2024. Scripts written before this date that omit `-ClientId` will fail against this deleted app registration.
- **Resolution:**
  1. Run the one-time registration: `Register-PnPEntraIDAppForInteractiveLogin -ApplicationName "PnP Governance Shell - [YourOrg]" -Tenant "yourorg.onmicrosoft.com" -SharePointDelegated -GraphDelegated -Interactive`
  2. Save the returned Client ID
  3. Update all `Connect-PnPOnline` calls to include `-ClientId <your-app-id>`
  4. Verify the app registration in Microsoft Entra admin center under App registrations

### Issue 2: DSPM Not Available in Tenant

- **Symptoms:** The DSPM for AI option does not appear in Microsoft Purview navigation, or displays "This feature is not available for your organization"
- **Root Cause:** DSPM for AI requires Microsoft 365 E5 or E5 Compliance add-on licensing. The feature may also require tenant-level opt-in or may be in staged rollout.
- **Resolution:**
  1. Verify E5 or E5 Compliance licenses are assigned to administrator accounts
  2. Check the Microsoft 365 roadmap for DSPM for AI availability in your region
  3. Enable targeted release in Admin Center > Settings > Org settings > Release preferences
  4. If licensing is confirmed, open a support ticket with Microsoft to verify feature eligibility

### Issue 3: Oversharing Scan Returns Incomplete Results

- **Symptoms:** Known overshared sites do not appear in the DSPM assessment, or the total site count is significantly lower than expected
- **Root Cause:** DSPM scans are incremental and may not cover all sites in the initial scan. Sites created after the last scan cycle, or sites with specific template types, may be excluded.
- **Resolution:**
  1. Verify the scan scope in DSPM settings includes the expected site templates
  2. Check that recently created sites have had sufficient time to be indexed (allow 48 hours)
  3. Use the PowerShell oversharing detection script (Script 1) as a supplementary scan
  4. Compare DSPM results with manual PowerShell scan output to identify coverage gaps

### Issue 4: Remediation Actions Not Taking Effect

- **Symptoms:** After restricting sharing capability on a site, the site still appears as overshared in the next DSPM scan, or users can still access content they should not
- **Root Cause:** Sharing capability changes affect future sharing actions but do not automatically revoke existing shared links. Additionally, DSPM scan results may be cached.
- **Resolution:**
  1. After changing sharing capability, also remove existing sharing links using `Remove-PnPFileSharingLink`
  2. For organization-wide links, use the SharePoint Admin Center to review and revoke active links
  3. Wait for at least one full DSPM scan cycle (24-48 hours) before verifying
  4. Use `Get-SPOSite -Identity <url> -Detailed` to confirm the setting persisted

### Issue 5: High Volume of False Positives

- **Symptoms:** DSPM flags sites as overshared that have legitimate business reasons for broad access (e.g., company-wide communication sites, policy document libraries)
- **Root Cause:** DSPM applies generic sensitivity heuristics that may flag content as sensitive when it is intentionally shared broadly.
- **Resolution:**
  1. Review each flagged site and classify as true positive or false positive
  2. For legitimate broad-access sites, document the business justification
  3. Consider applying specific sensitivity labels to truly sensitive content rather than relying on heuristic detection
  4. Create DSPM policy exceptions for documented broad-access sites with governance approval

### Issue 6: PnP PowerShell Permission Scan Timeouts

- **Symptoms:** Script 2 (Site-Level Permission Analysis) times out or fails with "The operation has timed out" on large document libraries
- **Root Cause:** Large libraries with thousands of items with unique permissions cause excessive API calls that exceed timeout thresholds.
- **Resolution:**
  1. Add `-PageSize 100` parameter and process items in batches
  2. Filter to specific folders or content types rather than scanning entire libraries
  3. Increase the PowerShell session timeout: `$global:PnPConnection.Timeout = 600000`
  4. For very large libraries, use the SharePoint search API to first identify items with unique permissions

## Diagnostic Steps

1. **Verify DSPM service health:** Check Microsoft 365 service health dashboard for Purview-related incidents
2. **Validate scan status:** In Purview > DSPM > Overview, check the last scan timestamp and status
3. **Test with a known site:** Create a deliberately overshared test site and verify DSPM detects it
4. **Review audit logs:** Search unified audit log for "Set-SPOSite" events to confirm remediation actions were executed
5. **Check permission inheritance:** Use PnP PowerShell to verify whether permission changes have propagated to subsites and libraries

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | False positives in DSPM scan | SharePoint team for site classification review |
| **Medium** | DSPM scan coverage gaps | Microsoft support for scan scope configuration |
| **High** | Remediation not taking effect on sensitive sites | Security Operations and SharePoint Admin team |
| **Critical** | Active oversharing of regulated financial data detected | CISO, Compliance Officer, and governance committee within 4 hours |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — DSPM configuration steps
- [PowerShell Setup](powershell-setup.md) — Detection and remediation scripts
- [Verification & Testing](verification-testing.md) — Validation procedures
