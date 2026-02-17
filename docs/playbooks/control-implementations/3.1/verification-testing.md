# Control 3.1: Copilot Interaction Audit Logging — Verification & Testing

Test cases and evidence collection procedures to validate that Copilot interaction audit logging is fully operational and supports compliance with FSI regulatory requirements.

## Test Cases

### Test 1: Audit Log Capture Verification

- **Objective:** Confirm that Copilot interactions generate audit log entries
- **Steps:**
  1. Have a licensed test user initiate a Copilot interaction in Word, Excel, or Teams.
  2. Wait 15-30 minutes for log ingestion.
  3. Search the Unified Audit Log for `CopilotInteraction` events filtered to the test user.
- **Expected Result:** At least one `CopilotInteraction` record appears with the test user's UPN, timestamp, application context, and prompt metadata.
- **Evidence:** Screenshot of audit log search results showing the captured interaction with timestamps.

### Test 2: Retention Policy Application

- **Objective:** Verify that the 10-year retention policy is applied to Copilot audit records
- **Steps:**
  1. Run `Get-UnifiedAuditLogRetentionPolicy` and filter for Copilot-related policies.
  2. Confirm the policy shows `RetentionDuration: TenYears` and `RecordTypes: CopilotInteraction`.
  3. Verify the policy priority is higher than the default retention policy.
- **Expected Result:** FSI Copilot retention policy exists with correct duration, record types, and priority.
- **Evidence:** PowerShell output showing the retention policy configuration.

### Test 3: Cross-Application Coverage

- **Objective:** Validate that audit logs capture Copilot interactions across all M365 applications
- **Steps:**
  1. Initiate Copilot interactions in Word, Excel, PowerPoint, Teams Chat, Teams Meetings, and Outlook.
  2. Search audit logs for each application-specific event.
  3. Confirm each application generates distinct audit records.
- **Expected Result:** Audit records present for each M365 application where Copilot was used.
- **Evidence:** Consolidated report showing Copilot audit entries per application.

### Test 4: Alert Policy Validation

- **Objective:** Confirm alert policies trigger on high-volume Copilot activity
- **Steps:**
  1. Review alert policy configuration for Copilot-related thresholds.
  2. Simulate or review historical data for threshold-crossing events.
  3. Verify alert recipients received notification emails.
- **Expected Result:** Alert policies are configured and notification delivery is functional.
- **Evidence:** Screenshot of alert policy settings and sample alert email.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Audit log search results | Purview portal | CSV export | Per retention policy |
| Retention policy config | PowerShell output | Text/CSV | With control documentation |
| Alert policy settings | Purview portal | Screenshot | With control documentation |
| Cross-application test results | Audit log queries | CSV | Per retention policy |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC 17a-4 | Electronic record preservation | Supports compliance with record retention through 10-year audit log retention |
| FINRA 4511 | Books and records | Helps meet record-keeping requirements for AI-assisted activities |
| FFIEC IT Handbook | Audit trail requirements | Supports IT examination requirements for logging AI system interactions |
| SOX Section 802 | Record retention | Helps meet requirements for preserving records related to financial reporting |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for common audit logging issues
- Proceed to [Control 3.2](../3.2/portal-walkthrough.md) for data retention policy configuration
