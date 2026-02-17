# Control 3.3: eDiscovery for Copilot-Generated Content — Verification & Testing

Test cases and evidence collection procedures to validate eDiscovery capabilities for Copilot-generated content and interaction history.

## Test Cases

### Test 1: Copilot Content Discoverability

- **Objective:** Confirm that Copilot interactions are searchable via eDiscovery tools
- **Steps:**
  1. Have a test user perform several Copilot interactions in different applications (Word, Teams, Outlook).
  2. Wait 24 hours for content indexing.
  3. Create a compliance search with the query `kind:microsoftcopilot AND UserPrincipalName:[test-user]`.
  4. Review search results for completeness.
- **Expected Result:** All Copilot interactions from the test user are returned in search results with full metadata.
- **Evidence:** Search results export showing Copilot interaction records with timestamps and content.

### Test 2: Custodian Hold Preservation

- **Objective:** Verify that eDiscovery holds preserve Copilot content from deletion
- **Steps:**
  1. Place a test custodian on hold with a Copilot content query.
  2. Have the custodian delete a Copilot-generated document.
  3. Search for the deleted document using eDiscovery.
  4. Confirm the document is still discoverable in the Recoverable Items folder.
- **Expected Result:** Deleted Copilot content remains preserved and discoverable under the hold.
- **Evidence:** Search results showing the preserved document with hold metadata.

### Test 3: Cross-Workload Collection

- **Objective:** Validate that eDiscovery collections capture Copilot content across all M365 workloads
- **Steps:**
  1. Create a collection targeting Exchange, SharePoint, OneDrive, and Teams.
  2. Filter by Copilot-specific content types.
  3. Review collection estimates for each workload.
  4. Commit the collection to a review set.
- **Expected Result:** Copilot content from all targeted workloads appears in the review set.
- **Evidence:** Collection statistics showing items per workload and review set contents.

### Test 4: Export and Production Readiness

- **Objective:** Confirm Copilot content can be exported in standard litigation formats
- **Steps:**
  1. Select items from the review set containing Copilot content.
  2. Export in the required format (PST, EML, or native format).
  3. Verify exported items retain metadata including Copilot attribution.
  4. Confirm the export load file contains correct field mappings.
- **Expected Result:** Copilot content exports successfully with preserved metadata and standard load file format.
- **Evidence:** Export manifest and sample exported items with Copilot metadata intact.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Search results summary | Purview eDiscovery | CSV | Case duration |
| Hold confirmation | PowerShell | Text export | Case duration |
| Collection statistics | Purview eDiscovery | Screenshot | Case duration |
| Export manifest | Export tool | CSV | Case duration |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FRCP Rule 26 | ESI preservation and production | Supports compliance with discovery obligations for AI-generated content |
| FINRA Rule 8210 | Record production for examinations | Helps meet timely production of Copilot interaction records |
| SEC 17a-4 | Record accessibility | Supports requirements for accessible and searchable electronic records |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for eDiscovery issues with Copilot content
- Proceed to [Control 3.4](../3.4/portal-walkthrough.md) for communication compliance monitoring
