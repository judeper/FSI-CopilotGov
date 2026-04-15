# Control 1.1: Copilot Readiness Assessment and Data Hygiene — Troubleshooting

Common issues and resolution steps for Copilot readiness assessment and data hygiene procedures.

## Common Issues

### Issue 1: Optimization Assessment Shows Low Update Channel Compliance

- **Symptoms:** The Optimization Assessment reports that a high percentage of endpoints are on Semi-Annual Enterprise Channel or an unsupported Office update channel
- **Root Cause:** Semi-Annual Enterprise Channel does not receive Copilot feature updates. Endpoints on this channel may install the Copilot license but will not have access to the latest Copilot capabilities.
- **Resolution:**
  1. Use Microsoft Intune (Devices > Configuration profiles > Settings catalog > search for Update Channel under Microsoft Office 2016 (Machine) > Updates) to move endpoints from Semi-Annual Enterprise Channel to Current Channel or Monthly Enterprise Channel
  2. For Group Policy-managed environments, update the "Update Channel" policy to "Current Channel" (or "Monthly Enterprise Channel" for environments requiring monthly patch cycles)
  3. For a phased approach, move Copilot pilot users first, then expand as each group transitions channels
  4. Allow 1-7 days for channel transitions to complete after policy change
  5. Re-run the Optimization Assessment to confirm update channel compliance improves after the transition

### Issue 2: Copilot Readiness Dashboard Shows No Data

- **Symptoms:** Dashboard loads but displays "No data available" or shows stale information older than 7 days
- **Root Cause:** The readiness assessment requires specific licensing and tenant configuration to generate data. Data may not populate until Copilot licenses are assigned to at least one user or the assessment service has not completed its initial scan.
- **Resolution:**
  1. Verify at least one Microsoft 365 Copilot license exists in the tenant (even if unassigned)
  2. Check that the signed-in account has Global Administrator or Global Reader role
  3. Wait 48-72 hours after initial license provisioning for data to populate
  4. If data remains unavailable, open a Microsoft support ticket referencing the Copilot readiness service

### Issue 3: DSPM Oversharing Report Missing Sites

- **Symptoms:** The DSPM for AI report shows fewer sites than expected, or known sensitive sites are not appearing in the oversharing assessment
- **Root Cause:** DSPM scanning may not cover all site types by default. Personal OneDrive sites, Teams-connected sites with specific configurations, or recently created sites may be excluded from the initial scan scope.
- **Resolution:**
  1. Verify DSPM for AI is enabled in Microsoft Purview > Data Security Posture Management
  2. Check that the scan scope includes all relevant site templates
  3. Manually add missing sites to the DSPM assessment scope
  4. Allow 24-48 hours for newly added sites to appear in reports

### Issue 4: PowerShell Script Authentication Failures

- **Symptoms:** Scripts fail with "Access Denied", "Insufficient privileges", or "Connect-MgGraph: Interactive authentication is not supported"
- **Root Cause:** Graph API consent may not be granted, or the execution environment does not support interactive authentication (e.g., Azure Automation runbooks).
- **Resolution:**
  1. For interactive sessions: Run `Connect-MgGraph -Scopes "Sites.Read.All"` and consent to permissions
  2. For automated execution: Register an Entra ID app with certificate authentication and required API permissions
  3. Verify the app registration has admin consent for required Graph API scopes
  4. For SPO Management Shell: Confirm the account has SharePoint Administrator role

### Issue 5: Label Coverage Report Shows Unexpectedly Low Numbers

- **Symptoms:** Label analytics shows coverage well below expected levels despite active labeling policies
- **Root Cause:** Label analytics may have reporting delays of up to 7 days. Additionally, labels applied via client-side labeling (manual) may not be reflected until documents are next accessed or indexed.
- **Resolution:**
  1. Verify reporting timeframe in Label Analytics (default may be 7-day window)
  2. Check auto-labeling policy status — confirm policies are enabled and not in simulation mode
  3. Review label policy scoping — labels may not be published to all user groups
  4. Force a re-index of key SharePoint sites using PnP PowerShell (`Invoke-PnPSiteSearchReindex`) or the SharePoint site settings UI under Search and Offline Availability

### Issue 6: Stale Site Detection False Positives

- **Symptoms:** Sites actively used by teams are flagged as stale in the hygiene scan
- **Root Cause:** The `LastContentModifiedDate` property in SharePoint may not update for certain activity types such as viewing, commenting, or metadata-only changes
- **Resolution:**
  1. Cross-reference flagged sites with audit log activity using `Search-UnifiedAuditLog`
  2. Adjust the staleness threshold from 180 days to a value appropriate for your organization
  3. Exclude site templates known to have low write activity (e.g., communication sites used primarily for reading)
  4. Supplement with Microsoft 365 usage reports for a complete activity picture

## Diagnostic Steps

When encountering unexpected results from readiness assessments:

1. **Check service health:** Verify Microsoft 365 service health at admin.microsoft.com > Health > Service health for any active incidents affecting Purview or SharePoint
2. **Validate permissions:** Run `Get-MgContext` to confirm the current session has required scopes
3. **Review audit logs:** Check unified audit log for any relevant admin actions that may have affected results
4. **Test with a single site:** Isolate the issue by running assessment scripts against a single known site before running tenant-wide scans
5. **Compare data sources:** Cross-reference portal data with PowerShell output to identify discrepancies

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor data discrepancies in reports | IT Operations team for investigation |
| **Medium** | Readiness dashboard not populating after 72 hours | Microsoft Premier Support ticket |
| **High** | Assessment reveals critical oversharing of regulated data | CISO and Compliance Officer immediately |
| **Critical** | Assessment blocked — unable to evaluate readiness | Governance committee and Microsoft TAM |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Step-by-step configuration reference
- [PowerShell Setup](powershell-setup.md) — Script reference and parameters
- [Verification & Testing](verification-testing.md) — Test cases to validate resolution
- [Control 1.1: Copilot Readiness Assessment](../../../controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md) — Parent control
