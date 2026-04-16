# Control 3.12: Evidence Collection and Audit Attestation — Verification & Testing

Test cases and evidence collection procedures to validate audit evidence completeness and attestation workflows.

## Test Cases

### Test 1: Evidence Pack Completeness

- **Objective:** Verify that the evidence pack contains documentation for all Copilot governance controls
- **Steps:**
  1. Generate the evidence pack using the automated script.
  2. Review the pack against the evidence requirements checklist for each control (3.1-3.13).
  3. Confirm each control has: configuration evidence, test results, and attestation sign-off.
  4. Identify any gaps and assign remediation owners.
- **Expected Result:** Evidence pack contains complete documentation for all 13 Pillar 3 controls.
- **Evidence:** Evidence pack inventory checklist with completeness status per control.

### Test 2: Evidence Freshness Validation

- **Objective:** Confirm that all evidence items are within their maximum age thresholds
- **Steps:**
  1. Run the evidence freshness audit script.
  2. Review the freshness report for any "STALE" items.
  3. Verify that critical evidence (audit logs, policy configurations) is no older than 90 days.
  4. Verify that dynamic evidence (review logs, incident reports) is no older than 30 days.
- **Expected Result:** All evidence items are within their defined freshness thresholds.
- **Evidence:** Freshness audit report showing all items as "Current".

### Test 3: Attestation Workflow Functionality

- **Objective:** Validate that the attestation workflow correctly captures approvals and sign-offs
- **Steps:**
  1. Initiate a test attestation for one control.
  2. Submit the attestation for approval.
  3. Have the designated approver review and sign off.
  4. Verify the attestation is recorded with timestamp, approver identity, and comments.
- **Expected Result:** Attestation workflow completes with full audit trail of approval.
- **Evidence:** Attestation record showing submission, review, and approval with timestamps.

### Test 4: Regulatory Production Readiness

- **Objective:** Confirm that evidence can be assembled and produced in response to a regulatory examination request
- **Steps:**
  1. Simulate a regulatory examination request for Copilot governance documentation.
  2. Assemble the evidence pack within the target response time (48 hours).
  3. Verify the pack includes all requested categories: policies, configurations, test results, attestations.
  4. Confirm the evidence is in a format acceptable for regulatory review.
- **Expected Result:** Evidence pack is assembled within 48 hours and meets regulatory production requirements.
- **Evidence:** Assembled evidence pack with production cover letter and index.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Evidence pack inventory | Automated scripts | Text/CSV | With assessment |
| Freshness audit report | PowerShell | CSV | With assessment |
| Attestation records | Compliance Manager | PDF | 7 years |
| Production readiness test | Simulation results | Documentation | With control docs |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3120 | Annual supervisory control report with evidence | Supports compliance with evidence-based supervisory attestation |
| Sarbanes-Oxley §404 | Internal controls attestation | Helps meet attestation requirements for financial reporting controls |
| FFIEC IT Handbook | Examination evidence production | Supports timely production of IT governance evidence |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for evidence collection issues
- Proceed to [Control 3.13](../3.13/portal-walkthrough.md) for FFIEC alignment
- Back to [Control 3.12](../../../controls/pillar-3-compliance/3.12-evidence-collection.md)
