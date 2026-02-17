# Control 3.3: eDiscovery for Copilot-Generated Content — Troubleshooting

Common issues and resolution steps for eDiscovery operations involving Copilot-generated content.

## Common Issues

### Issue 1: Copilot Interactions Not Appearing in Search Results

- **Symptoms:** Compliance search with `kind:microsoftcopilot` returns zero results despite confirmed Copilot usage.
- **Root Cause:** Content indexing may not be complete (can take up to 24 hours), or the Copilot interaction location is not indexed for eDiscovery.
- **Resolution:**
  1. Verify that the user has an E5 or eDiscovery (Premium) license assigned.
  2. Wait at least 24 hours after the Copilot interaction for indexing to complete.
  3. Try broadening the search to include all Exchange content for the user to verify search functionality.
  4. Check if the Copilot interaction data source is available in your tenant region.

### Issue 2: Hold Not Preserving Copilot Content

- **Symptoms:** Copilot-generated content is deleted despite an active eDiscovery hold on the custodian.
- **Root Cause:** The hold query may not cover Copilot-specific content types, or the hold is applied to the wrong data source.
- **Resolution:**
  1. Review the hold policy scope: `Get-CaseHoldPolicy -Identity "hold-name" | Format-List`
  2. Verify the hold includes Exchange and SharePoint locations for the custodian.
  3. Check if the hold rule query syntax correctly targets Copilot content.
  4. Consider using a broad hold (no query filter) for critical custodians to preserve all content.

### Issue 3: Large Collection Processing Timeout

- **Symptoms:** Collection estimates or commits fail or time out when targeting large volumes of Copilot data.
- **Root Cause:** High-volume Copilot usage generates significant interaction data that may exceed collection thresholds.
- **Resolution:**
  1. Narrow the date range to reduce collection volume.
  2. Split the collection by custodian or by workload location.
  3. Use the `SessionCommand` paging approach for PowerShell-based searches.
  4. Contact Microsoft Support if collection failures persist for Premium eDiscovery cases.

### Issue 4: Missing Metadata in Exported Copilot Content

- **Symptoms:** Exported Copilot interaction records lack expected metadata fields such as application context or prompt text.
- **Root Cause:** Certain Copilot metadata fields may not be included in standard export formats, or the export format does not support the full schema.
- **Resolution:**
  1. Use the native export format rather than PST to preserve maximum metadata.
  2. Check that the review set includes all available Copilot-specific columns.
  3. Review Microsoft documentation for the current Copilot eDiscovery metadata schema.
  4. For critical fields, supplement eDiscovery exports with Audit Log data from Control 3.1.

## Diagnostic Steps

1. **Verify case status:** `Get-ComplianceCase | Select Name, Status, CaseType`
2. **Check search status:** `Get-ComplianceSearch -Identity "search-name" | Select Status, Items, Errors`
3. **Review hold status:** `Get-CaseHoldPolicy | Select Name, Enabled, DistributionStatus`
4. **Test basic search:** Run a simple search on a known custodian to confirm eDiscovery functionality.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Unable to meet court-ordered discovery deadline | Legal team + Microsoft Premier Support — Severity A |
| High | Hold failures risking data loss | Compliance team + Microsoft Support |
| Medium | Search performance issues | Internal IT — optimize queries and scope |
| Low | Metadata gaps in exports | Document gaps and supplement from other sources |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 3.2: Data Retention Policies](../3.2/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
