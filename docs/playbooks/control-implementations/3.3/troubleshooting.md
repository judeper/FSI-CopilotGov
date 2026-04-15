# Control 3.3: eDiscovery for Copilot-Generated Content — Troubleshooting

Common issues and resolution steps for eDiscovery operations involving Copilot-generated content. All navigation references use the unified eDiscovery experience in the Microsoft Purview portal (Microsoft Purview > eDiscovery > Cases).

## Common Issues

### Issue 1: Copilot Interactions Not Appearing in Search Results

- **Symptoms:** Compliance search with `kind:microsearch` returns zero results despite confirmed Copilot usage.
- **Root Cause:** Content indexing may not be complete (can take up to 24 hours), or the Copilot interaction location is not indexed for eDiscovery.
- **Resolution:**
  1. Verify that the user has an E5 or eDiscovery (Premium) license assigned.
  2. Wait at least 24 hours after the Copilot interaction for indexing to complete.
  3. Try broadening the search to include all Exchange content for the user to verify search functionality.
  4. Check if the Copilot interaction data source is available in your tenant region.

### Issue 2: Pre-Migration Cases Missing Copilot Content Locations

- **Symptoms:** An eDiscovery case created before May 2025 does not return Copilot content in searches, even though the custodian has Copilot interaction history.
- **Root Cause:** Cases created before the unified eDiscovery experience (May 2025 GA) may not automatically include the "Microsoft Copilot experiences" content location. Pre-migration cases retain their original data source configuration.
- **Resolution:**
  1. Open the case in **Microsoft Purview > eDiscovery > Cases**.
  2. Navigate to **Data sources** and check whether "Microsoft Copilot experiences" appears as an available location.
  3. If missing, add the Copilot content location to the case data sources.
  4. If the case has active holds, verify that the hold policy is updated to include the new Copilot content location.
  5. Re-run any affected searches after updating the data sources.

### Issue 3: Copilot Surface Filter Not Available

- **Symptoms:** The Copilot surface filter (filter by surface, agent name, or interaction type) is not visible in the unified search builder.
- **Root Cause:** The Copilot surface filter requires the Premium capability tier (E5 or E5 eDiscovery add-on license). It is not available for Standard-tier searches.
- **Resolution:**
  1. Verify that the case is configured for Premium eDiscovery capabilities.
  2. Confirm that E5 or E5 eDiscovery add-on licenses are assigned to the performing user.
  3. If operating at Standard tier, use KQL surface qualifiers (e.g., `kind:microsearch AND CopilotSurface:"Microsoft365Copilot"`) as an alternative.

### Issue 4: Hold Not Preserving Copilot Content

- **Symptoms:** Copilot-generated content is deleted despite an active eDiscovery hold on the custodian.
- **Root Cause:** The hold query may not cover Copilot-specific content types, or the hold is applied to the wrong data source.
- **Resolution:**
  1. Review the hold policy scope: `Get-CaseHoldPolicy -Identity "hold-name" | Format-List`
  2. Verify the hold includes Exchange and SharePoint locations for the custodian.
  3. Check if the hold rule query syntax correctly targets Copilot content (`kind:microsearch`).
  4. Consider using a broad hold (no query filter) for critical custodians to preserve all content.

### Issue 5: Large Collection Processing Timeout

- **Symptoms:** Collection estimates or commits fail or time out when targeting large volumes of Copilot data.
- **Root Cause:** High-volume Copilot usage generates significant interaction data that may exceed collection thresholds.
- **Resolution:**
  1. Narrow the date range to reduce collection volume.
  2. Split the collection by custodian or by workload location.
  3. Use the `SessionCommand` paging approach for PowerShell-based searches.
  4. Contact Microsoft Support if collection failures persist for Premium eDiscovery cases.

### Issue 6: Deprecated eDiscovery Export PowerShell Cmdlets

- **Symptoms:** PowerShell scripts using `New-ComplianceSearchAction -Export` or related export cmdlets fail with errors or return unsupported-operation messages.
- **Root Cause:** eDiscovery export PowerShell cmdlets were retired as part of the unified eDiscovery portal transition (May 2025). The cmdlets are no longer functional.
- **Resolution:**
  1. Replace PowerShell export workflows with the Purview portal export experience (eDiscovery > Cases > [case] > Review sets > Export).
  2. For programmatic export needs, migrate to the **Microsoft Graph eDiscovery APIs** (`POST /security/cases/ediscoveryCases/{id}/reviewSets/{id}/export`).
  3. Update any scheduled automation that relies on deprecated cmdlets.
  4. Case-management cmdlets (`New-ComplianceCase`, `New-ComplianceSearch`, `New-CaseHoldPolicy`) remain supported — only export cmdlets are affected.

### Issue 7: Missing Metadata in Exported Copilot Content

- **Symptoms:** Exported Copilot interaction records lack expected metadata fields such as application context or prompt text.
- **Root Cause:** Certain Copilot metadata fields may not be included in standard export formats, or the export format does not support the full schema. Additionally, organizations still using deprecated PowerShell export cmdlets may receive incomplete exports.
- **Resolution:**
  1. Use the native export format rather than PST to preserve maximum metadata.
  2. Export via the Purview portal or Microsoft Graph eDiscovery APIs (deprecated PowerShell export cmdlets may produce incomplete results — see Issue 6).
  3. Check that the review set includes all available Copilot-specific columns.
  4. Review Microsoft documentation for the current Copilot eDiscovery metadata schema.
  5. For critical fields, supplement eDiscovery exports with Audit Log data from Control 3.1.

## Diagnostic Steps

1. **Verify case status:** `Get-ComplianceCase | Select Name, Status, CaseType`
2. **Check search status:** `Get-ComplianceSearch -Identity "search-name" | Select Status, Items, Errors`
3. **Review hold status:** `Get-CaseHoldPolicy | Select Name, Enabled, DistributionStatus`
4. **Identify pre-migration cases:** `Get-ComplianceCase | Where-Object { $_.CreatedDateTime -lt [DateTime]"2025-05-01" } | Select Name, CreatedDateTime`
5. **Test basic search:** Run a simple search on a known custodian to confirm eDiscovery functionality.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Unable to meet court-ordered discovery deadline | Legal team + Microsoft Premier Support — Severity A |
| High | Hold failures risking data loss | Compliance team + Microsoft Support |
| High | Pre-migration cases missing Copilot locations affecting active holds | Compliance team -- immediate data source remediation |
| Medium | Search performance issues | Internal IT -- optimize queries and scope |
| Low | Metadata gaps in exports | Document gaps and supplement from other sources |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 3.2: Data Retention Policies](../3.2/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
- Back to [Control 3.3](../../../controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md)
