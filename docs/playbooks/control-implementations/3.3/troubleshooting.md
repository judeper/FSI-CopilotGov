# Control 3.3: eDiscovery for Copilot-Generated Content — Troubleshooting

Common issues and resolution steps for eDiscovery operations involving Copilot-generated content. All navigation references use the unified eDiscovery experience in the Microsoft Purview portal (Microsoft Purview > eDiscovery > Cases).

## Common Issues

### Issue 1: Copilot Interactions Not Appearing in Search Results

- **Symptoms:** eDiscovery search using the Copilot activity condition or Copilot item-class query returns zero results despite confirmed Copilot usage.
- **Root Cause:** Content indexing may not be complete (can take up to 24 hours), or the Copilot interaction location is not indexed for eDiscovery.
- **Resolution:**
  1. Verify that the user has an E5 or eDiscovery (Premium) license assigned.
  2. Wait at least 24 hours after the Copilot interaction for indexing to complete.
  3. Try broadening the search to include all Exchange content for the user to verify search functionality.
  4. Check if the Copilot interaction data source is available in your tenant region.

### Issue 2: Existing Cases Missing Copilot Sources or Conditions

- **Symptoms:** An existing eDiscovery case does not return Copilot content in searches, even though the custodian has Copilot interaction history.
- **Root Cause:** The case's selected data sources or search conditions may not cover Copilot activity, custodian mailboxes, or in-scope SharePoint, OneDrive, Teams, or SharePoint Embedded container locations.
- **Resolution:**
  1. Open the case in **Microsoft Purview > eDiscovery > Cases**.
  2. Navigate to **Data sources** and search conditions; check whether Copilot activity, custodian mailboxes, and in-scope container locations are covered.
  3. If missing, add the documented Copilot source, item-class condition, or container location to the case.
  4. If the case has active holds, verify that the hold policy is updated to include the corrected Copilot scope.
  5. Re-run any affected searches after updating the data sources.

### Issue 3: Copilot Item-Class Filtering Not Returning Expected Surface Scope

- **Symptoms:** A Copilot search returns broader or narrower results than expected for a specific surface (for example, BizChat, Teams, Outlook, or Word).
- **Root Cause:** The search condition may be using a broad Copilot activity selection without a documented item-class qualifier, or the tenant's current eDiscovery experience may expose different filtering fields than the playbook example.
- **Resolution:**
  1. Verify the current eDiscovery condition-builder fields available in the tenant.
  2. Compare the target surface against Microsoft Learn's current Copilot item-class table.
  3. If operating at Standard tier, use documented item-class KQL after tenant validation, such as `itemclass:IPM.SkypeTeams.Message.Copilot.*` or `itemclass:IPM.SkypeTeams.Message.Copilot.BizChat`, combined with supported custodian/date filters.

### Issue 4: Hold Not Preserving Copilot Content

- **Symptoms:** Copilot-generated content is deleted despite an active eDiscovery hold on the custodian.
- **Root Cause:** The hold query may not cover Copilot-specific content types, or the hold is applied to the wrong data source.
- **Resolution:**
  1. Review the hold policy scope: `Get-CaseHoldPolicy -Identity "hold-name" | Format-List`
  2. Verify the hold includes Exchange and SharePoint locations for the custodian.
  3. Check whether the hold scope correctly targets Copilot content using the condition-builder Copilot activity selection or documented item-class KQL such as `(itemclass:IPM.SkypeTeams.Message.Copilot.* OR itemclass:IPM.Contact)`.
  4. Consider using a broad hold (no query filter) for critical custodians to preserve all content.

### Issue 5: Large Collection Processing Timeout

- **Symptoms:** Collection estimates or commits fail or time out when targeting large volumes of Copilot data.
- **Root Cause:** High-volume Copilot usage generates significant interaction data that may exceed collection thresholds.
- **Resolution:**
  1. Narrow the date range to reduce collection volume.
  2. Split the collection by custodian or by workload location.
  3. Use the `SessionCommand` paging approach for PowerShell-based searches.
  4. Contact Microsoft Support if collection failures persist for Premium eDiscovery cases.

### Issue 6: Cloud Export Attempted with On-Premises-Only eDiscovery Export Cmdlet Pattern

- **Symptoms:** PowerShell scripts using `New-ComplianceSearchAction -Export` or related export cmdlets fail with errors or return unsupported-operation messages.
- **Root Cause:** Microsoft Learn documents `New-ComplianceSearchAction -Export` examples and several export parameters as functional only in on-premises Exchange; cloud tenants should use Microsoft-documented portal or API export workflows validated for the tenant.
- **Resolution:**
  1. Replace PowerShell export workflows with the Purview portal export experience (eDiscovery > Cases > [case] > Review sets > Export).
  2. For programmatic export needs, migrate to the **Microsoft Graph eDiscovery APIs** (`POST /security/cases/ediscoveryCases/{id}/reviewSets/{id}/export`).
  3. Update any scheduled automation that relies on deprecated cmdlets.
  4. Case-management cmdlets (`New-ComplianceCase`, `New-ComplianceSearch`, `New-CaseHoldPolicy`) remain supported for appropriate workflows; validate export through current Microsoft documentation before use.

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
4. **List active cases for source verification:** `Get-ComplianceCase | Where-Object { $_.Status -ne "Closed" } | Select Name, CreatedDateTime, CaseType`
5. **Test basic search:** Run a simple search on a known custodian to confirm eDiscovery functionality.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Unable to meet court-ordered discovery deadline | Legal team + Microsoft Premier Support — Severity A |
| High | Hold failures risking data loss | Compliance team + Microsoft Support |
| High | Existing cases missing Copilot sources or conditions affecting active holds | Compliance team -- immediate data source remediation |
| Medium | Search performance issues | Internal IT -- optimize queries and scope |
| Low | Metadata gaps in exports | Document gaps and supplement from other sources |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 3.2: Data Retention Policies](../3.2/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
- Back to [Control 3.3](../../../controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md)
