# Control 3.11: Record Keeping and Books-and-Records Compliance — Verification & Testing

Test cases and evidence collection procedures to validate records management controls for Copilot-generated content, including the SEC Rule 17a-4(f)(2)(ii)(A) audit-trail alternative and mobile Copilot recordkeeping verification.

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

- **Objective:** Confirm that Preservation Lock prevents policy modification (required for audit-trail alternative path under SEC Rule 17a-4(f)(2)(ii)(A))
- **Steps:**
  1. Verify that Preservation Lock is enabled: `Get-RetentionCompliancePolicy -Identity "FSI-Regulatory-Record-Labels" | Select Name, RestrictiveRetention`
  2. Attempt to reduce the retention duration on the locked policy.
  3. Confirm the modification is rejected with an error.
  4. Run Script 4 (Preservation Lock Status) to generate a compliance report.
  5. Document the lock status for examination evidence.
- **Expected Result:** Preservation Lock prevents any reduction in retention duration or disabling of the policy; report shows LOCKED status.
- **Evidence:** PowerShell output showing lock status; Script 4 CSV export; rejected modification attempt screenshot.

### Test 4: Audit-Trail Alternative Compliance Verification (Rule 17a-4(f)(2)(ii)(A))

- **Objective:** Verify that the Purview audit trail captures all required events for the Rule 17a-4(f)(2)(ii)(A) audit-trail alternative compliance path
- **Steps:**
  1. Apply a regulatory record label to a test Copilot-generated document.
  2. Attempt to modify the labeled item — the modification should be blocked.
  3. Attempt to delete the labeled item — the deletion should be blocked.
  4. Run Script 5 (Audit Trail Coverage) to search the audit log for RecordStatusChanged, ComplianceRecordChanged events.
  5. Confirm that the label application, modification block, and deletion block are all captured in the Purview audit log.
  6. Export the audit log entries as evidence.
  7. Verify that the audit log retention policy covers the full record retention period for the labeled items.
- **Expected Result:** Audit trail captures all required events (label application, modification blocks, deletion blocks) throughout the retention period; this demonstrates that the audit-trail alternative under Rule 17a-4(f)(2)(ii)(A) is functional.
- **Evidence:** Audit log export showing record status changes, blocked modifications, and blocked deletions; audit log retention policy screenshot showing coverage period.

### Test 5: Mobile Copilot Recordkeeping Verification — Managed Device

- **Objective:** Verify that Copilot interactions via managed mobile devices are captured by existing retention policies
- **Steps:**
  1. Using a managed mobile device (Intune-enrolled, Microsoft 365 app installed), generate a Copilot interaction in Teams mobile and Outlook mobile.
  2. Within 24 hours, search the Purview audit log for CopilotInteraction events associated with the test user.
  3. Confirm that the mobile-generated Copilot interaction appears in the audit log.
  4. Verify that the interaction is subject to the relevant retention policy (Teams retention for Teams mobile, Exchange retention for Outlook mobile).
  5. Check that the CopilotInteraction audit event includes the expected metadata (timestamp, user, app, content references).
- **Expected Result:** Mobile Copilot interactions on managed devices are captured in the audit log and covered by retention policies — identical coverage to desktop interactions.
- **Evidence:** Audit log export showing CopilotInteraction events from mobile app usage; retention policy coverage confirmation.

### Test 6: Mobile Copilot Recordkeeping Verification — Unmanaged Device (Expected Failure)

- **Objective:** Confirm that Conditional Access blocks Copilot access from unmanaged mobile devices, preventing the off-channel recordkeeping gap
- **Steps:**
  1. Attempt to access M365 Copilot from an unmanaged mobile browser or personal device (using a test account).
  2. Verify that Conditional Access blocks access or requires enrollment in Intune.
  3. If access is blocked: document the Conditional Access block as evidence that the off-channel recordkeeping gap is prevented.
  4. If access is NOT blocked: this is a compliance gap — unmanaged mobile Copilot access may not be captured by retention policies. Escalate for Conditional Access policy remediation.
- **Expected Result:** Unmanaged mobile browser access to Copilot is blocked by Conditional Access; the Conditional Access block is logged and evidence is preserved.
- **Evidence:** Conditional Access sign-in log showing blocked access from unmanaged device; policy configuration screenshot.

### Test 7: Record Retrieval and Production

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
| Preservation Lock status | PowerShell (Script 4) | CSV + Text export | Permanent |
| Audit trail events for regulatory records | Purview audit + Script 5 | CSV export | Full record retention period |
| Conditional Access mobile block evidence | Entra sign-in logs | Export | With control documentation |
| Mobile audit log entries (managed device) | Purview audit log | Export | Full record retention period |
| Record retrieval test results | Content search | CSV/Export | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Rule 17a-4(f)(2)(ii)(A) | Audit-trail alternative to WORM storage | Tests 3 and 4 verify Preservation Lock and audit trail coverage for the alternative compliance path |
| SEC 17a-4 | Electronic record preservation in WORM format | Supports compliance with immutable record storage requirements (WORM or audit-trail alternative) |
| FINRA 4511 | Books-and-records retention | Helps meet retention obligations for AI-generated business records |
| SEC 17a-3 | Record-making requirements | Supports creation and classification of required records |
| Off-channel enforcement | All business communications must be captured | Tests 5 and 6 verify mobile Copilot recordkeeping coverage and access controls |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for records management issues
- Proceed to [Control 3.12](../3.12/portal-walkthrough.md) for evidence collection
