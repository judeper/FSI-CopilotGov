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

- **Objective:** Verify that the 6-year retention policy is applied to Copilot audit records
- **Steps:**
  1. Run `Get-UnifiedAuditLogRetentionPolicy` and filter for Copilot-related policies.
  2. Confirm the policy shows `RetentionDuration: SixYears` and `RecordTypes: CopilotInteraction`.
  3. Verify the policy priority is higher than the default retention policy.
- **Expected Result:** FSI Copilot retention policy exists with correct duration, record types, and priority. Minimum 6 years per SEC Rule 17a-4(a).
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

### Test 5: Agent Audit Event Capture

- **Objective:** Verify that agent creation and modification events generate AgentAdminActivity records
- **Steps:**
  1. In a test environment, have an authorized administrator create a new declarative Copilot agent or modify an existing agent (e.g., add a knowledge source or change agent instructions).
  2. Wait 15-30 minutes for log ingestion.
  3. Search the Unified Audit Log using `-RecordType AgentAdminActivity` filtered to the test administrator's UPN.
  4. Verify the event record contains `AgentId` and `AgentName` fields in the AuditData JSON.
  5. Repeat for an agent settings change using `-RecordType AgentSettingsAdminActivity`.
- **Expected Result:** At least one `AgentAdminActivity` event and one `AgentSettingsAdminActivity` event appear with the administrator's UPN, the affected agent's ID and name, and a timestamp corresponding to the test action.
- **Evidence:** PowerShell output showing the agent audit records with AgentId field populated.

### Test 6: JailbreakDetected Field Verification

- **Objective:** Confirm that JailbreakDetected events are captured and identifiable in audit logs
- **Steps:**
  1. Review existing CopilotInteraction audit records for the past 30 days.
  2. Parse AuditData JSON for each record and check for the `JailbreakDetected` field.
  3. Verify that the daily JailbreakDetected scan script (Script 5 in the PowerShell Setup playbook) executes successfully and produces output.
- **Expected Result:** The scan script runs without errors and correctly identifies the presence or absence of JailbreakDetected events. If events exist, they are exported to a separate CSV for investigation.
- **Evidence:** PowerShell output from Script 5 showing scan completion, plus exported CSV if events were found.

### Test 7: PAYG Billing Verification (Regulated — if PAYG configured)

- **Objective:** Confirm that PAYG audit billing controls are active and within budget
- **Steps:**
  1. Navigate to Azure portal > Cost Management > Budgets.
  2. Verify a budget exists for Purview audit spend with an alert threshold.
  3. Confirm the budget has notification recipients configured for the compliance team.
  4. Review the current month's spend to verify it is within the approved limit.
- **Expected Result:** PAYG billing budget exists with active alert. Current spend is within approved limit. No unexpected cost spikes from audit event accumulation.
- **Evidence:** Screenshot of Azure Cost Management budget configuration and current spend.

### Test 8: AgentAdminActivity Retention Policy

- **Objective:** Verify that agent-specific record types are covered by a retention policy
- **Steps:**
  1. Run `Get-UnifiedAuditLogRetentionPolicy | Where-Object { $_.RecordTypes -like "*AgentAdminActivity*" }`.
  2. Confirm the policy exists with a minimum 6-year duration.
  3. Verify the policy priority is appropriately set.
- **Expected Result:** A retention policy covering `AgentAdminActivity` and `AgentSettingsAdminActivity` exists with 6-year duration — supporting SOX Section 404 IT general controls audit trail requirements.
- **Evidence:** PowerShell output showing the agent record type retention policy configuration.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Audit log search results | Purview portal | CSV export | Per retention policy |
| Retention policy config | PowerShell output | Text/CSV | With control documentation |
| Alert policy settings | Purview portal | Screenshot | With control documentation |
| Cross-application test results | Audit log queries | CSV | Per retention policy |
| Agent audit event capture | PowerShell output | CSV | Per retention policy |
| JailbreakDetected scan results | PowerShell output | CSV | Per retention policy |
| PAYG billing controls | Azure Cost Management | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Rule 17a-4(a) | Electronic record preservation — six-year retention minimum | Supports compliance through 6-year audit log retention for CopilotInteraction and agent record types |
| FINRA Rule 4511 | Books and records | Helps meet record-keeping requirements for AI-assisted activities |
| FINRA Rule 3110 | Supervisory procedures for registered representatives | AgentId/AgentName fields enable supervisory mapping of agent usage to approved workflows |
| SOX Section 404 | IT general controls audit trail | AgentAdminActivity and AgentSettingsAdminActivity record types provide change management evidence |
| FFIEC IT Handbook | Audit trail and incident response requirements | JailbreakDetected scan provides the detection capability required for AI incident response |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for common audit logging issues
- Proceed to [Control 3.2](../3.2/portal-walkthrough.md) for data retention policy configuration
