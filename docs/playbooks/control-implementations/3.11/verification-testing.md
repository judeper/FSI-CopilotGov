# Control 3.11: Record Keeping and Books-and-Records Compliance — Verification & Testing

Test cases and evidence collection procedures to validate records management controls for Copilot-generated content.

## Test Cases

### Test 1: Regulatory Record Label Application

- **Objective:** Confirm retention labels correctly classify Copilot-generated content as regulatory records
- **Steps:**
  1. Create a Copilot-drafted business communication and apply the "SEC-17a4-Business-Communication-6yr" label.
  2. Verify the label metadata shows regulatory record status.
  3. Attempt to delete the labeled item and confirm deletion is blocked.
  4. Attempt to change or remove the label and confirm the action is blocked for regulatory records.
- **Expected Result:** Regulatory record label prevents deletion and relabeling, preserving content immutability.
- **Evidence:** Screenshot showing label application and blocked deletion attempt.

### Test 2: Auto-Apply Label Accuracy

- **Objective:** Verify that auto-apply policies correctly classify Copilot-generated content
- **Steps:**
  1. Generate various types of Copilot content: business emails, client correspondence, investment recommendations.
  2. Wait for auto-apply processing (up to 7 days for initial policy deployment).
  3. Check that each content type received the appropriate retention label.
  4. Document any misclassifications or unlabeled content.
- **Expected Result:** Auto-apply labels correctly classify at least 85% of Copilot-generated content.
- **Evidence:** Classification accuracy report showing auto-apply results.

### Test 3: Preservation Lock Verification

- **Objective:** Confirm that Preservation Lock prevents policy modification
- **Steps:**
  1. Verify that Preservation Lock is enabled: `Get-RetentionCompliancePolicy -Identity "policy-name" | Select RestrictiveRetention`
  2. Attempt to reduce the retention duration on the locked policy.
  3. Confirm the modification is rejected.
  4. Document the lock status for examination evidence.
- **Expected Result:** Preservation Lock prevents any reduction in retention duration or disabling of the policy.
- **Evidence:** PowerShell output showing lock status and rejected modification attempt.

### Test 4: Record Retrieval and Production

- **Objective:** Validate that retained Copilot records can be searched, retrieved, and produced for examination
- **Steps:**
  1. Use Content Search to locate retained Copilot-generated records.
  2. Verify search results include records from all categories (communications, client records, recommendations).
  3. Export a sample set in a format suitable for regulatory production.
  4. Confirm exported records retain all original metadata and content integrity.
- **Expected Result:** Records are searchable, retrievable, and exportable with full metadata integrity.
- **Evidence:** Content search results and sample export with metadata verification.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Label configuration | Purview portal | Screenshot | With control documentation |
| Auto-apply accuracy results | Classification report | Spreadsheet | With control documentation |
| Preservation Lock status | PowerShell | Text export | Permanent |
| Record retrieval test results | Content search | CSV/Export | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC 17a-4 | Electronic record preservation in WORM format | Supports compliance with immutable record storage requirements |
| FINRA 4511 | Books-and-records retention | Helps meet retention obligations for AI-generated business records |
| SEC 17a-3 | Record-making requirements | Supports creation and classification of required records |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for records management issues
- Proceed to [Control 3.12](../3.12/portal-walkthrough.md) for evidence collection
