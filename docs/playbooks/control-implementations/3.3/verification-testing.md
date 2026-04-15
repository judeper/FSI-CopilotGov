# Control 3.3: eDiscovery for Copilot-Generated Content — Verification & Testing

Test cases and evidence collection procedures to validate eDiscovery capabilities for Copilot-generated content and interaction history. All test procedures use the unified eDiscovery experience in the Microsoft Purview portal (Microsoft Purview > eDiscovery > Cases).

## Test Cases

### Test 1: Copilot Content Discoverability

- **Objective:** Confirm that Copilot interactions are searchable via the unified eDiscovery search builder
- **Steps:**
  1. Have a test user perform several Copilot interactions in different applications (Word, Teams, Outlook).
  2. Wait 24 hours for content indexing.
  3. In the unified eDiscovery experience, create a search with the query `kind:microsearch AND participants:[test-user@firm.com]`.
  4. Use the Copilot surface filter to confirm results are filterable by surface type (e.g., Teams Copilot, Outlook Copilot).
  5. Review search results for completeness.
- **Expected Result:** All Copilot interactions from the test user are returned in search results with full metadata. Surface filter is available for Premium-tier searches.
- **Evidence:** Search results export showing Copilot interaction records with timestamps and content.

### Test 2: Custodian Hold Preservation

- **Objective:** Verify that eDiscovery holds preserve Copilot content from deletion
- **Steps:**
  1. Place a test custodian on hold with a Copilot content query (`kind:microsearch`).
  2. Have the custodian delete a Copilot-generated document.
  3. Search for the deleted document using eDiscovery.
  4. Confirm the document is still discoverable in the Recoverable Items folder.
- **Expected Result:** Deleted Copilot content remains preserved and discoverable under the hold.
- **Evidence:** Search results showing the preserved document with hold metadata.

### Test 3: Cross-Workload Collection

- **Objective:** Validate that eDiscovery searches capture Copilot content across all M365 workloads
- **Steps:**
  1. Create a search targeting Exchange, SharePoint, OneDrive, and Teams custodian locations.
  2. Filter by Copilot-specific content types using the unified search builder.
  3. Review search estimates for each workload.
  4. Commit the results to a review set.
- **Expected Result:** Copilot content from all targeted workloads appears in the review set.
- **Evidence:** Search statistics showing items per workload and review set contents.

### Test 4: Pre-Migration Case Verification

- **Objective:** Confirm that cases created before May 2025 include the Copilot content location
- **Steps:**
  1. Open each eDiscovery case created before May 2025.
  2. Navigate to **Data sources** within the case.
  3. Verify that "Microsoft Copilot experiences" appears as a data source or custodian location option.
  4. If missing, add the Copilot content location and confirm inclusion in any active holds.
- **Expected Result:** All active cases, including pre-migration cases, cover the Copilot content location.
- **Evidence:** Screenshot of Data sources panel for each reviewed case, showing the Copilot content location.

### Test 5: Export and Production Readiness

- **Objective:** Confirm Copilot content can be exported in standard litigation formats using the unified portal or Graph APIs
- **Steps:**
  1. Select items from the review set containing Copilot content.
  2. Export using the **Purview portal export experience** or **Microsoft Graph eDiscovery APIs** (deprecated PowerShell export cmdlets are no longer supported — see Troubleshooting Issue 6).
  3. Export in the required format (PST, EML, or native format).
  4. Verify exported items retain metadata including Copilot attribution.
  5. Confirm the export load file contains correct field mappings.
- **Expected Result:** Copilot content exports successfully with preserved metadata and standard load file format.
- **Evidence:** Export manifest and sample exported items with Copilot metadata intact.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Search results summary | Purview eDiscovery | CSV | Case duration |
| Hold confirmation | PowerShell | Text export | Case duration |
| Pre-migration case audit | Purview portal | Screenshot | Ongoing |
| Search statistics | Purview eDiscovery | Screenshot | Case duration |
| Export manifest | Export tool | CSV | Case duration |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FRCP Rule 26(b)(1) | Proportional ESI preservation and production | Unified search builder enables targeted, proportional discovery of Copilot content |
| FINRA Rule 8210 | Record production for examinations | Supports timely production of Copilot interaction records |
| SEC 17a-4(j) | Record accessibility and production | Supports requirements for accessible and producible electronic records |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for eDiscovery issues with Copilot content
- Proceed to [Control 3.4](../3.4/portal-walkthrough.md) for communication compliance monitoring
- Back to [Control 3.3](../../../controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md)
