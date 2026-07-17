# Control 4.5: Copilot Usage Analytics and Adoption Reporting — Verification & Testing

Conservative tests that validate whether usage-detail reporting is accessible and produces records in a live tenant.

## Non-Claims (Scope Guardrails)

Passing these tests does **not** prove:

- dashboard interpretation quality
- adoption quality or business impact
- regulatory sufficiency on its own
- complete user coverage across licensed and unlicensed populations

## Test Cases

### Test 1: Permission and Role Gate

- **Objective:** Confirm the caller is authorized to query Copilot usage-detail APIs.
- **Steps:**
  1. Connect with `Connect-MgGraph -Scopes "Reports.Read.All"`.
  2. Run `Get-MgContext | Select-Object Scopes`.
  3. Validate the identity is assigned a supported delegated admin role (if using delegated auth), or app-only consent exists for `Reports.Read.All`.
- **Expected Result:** `Reports.Read.All` is present and authorization requirements are met.
- **Fail Closed:** Missing scope, missing role, or consent errors.

### Test 2: Beta Endpoint/Cmdlet Reachability

- **Objective:** Confirm the documented beta API path is reachable from the tenant.
- **Steps:**
  1. Run `Get-MgBetaReportMicrosoft365CopilotUsageUserDetail -Period D7 -Format application/json -OutFile .\copilot-usage-d7.json`.
  2. Parse the file with `Get-Content -Raw .\copilot-usage-d7.json | ConvertFrom-Json`.
- **Expected Result:** Command succeeds and returns structured JSON payload.
- **Fail Closed:** HTTP/auth errors, malformed output, or missing file.

### Test 3: Record Presence Validation

- **Objective:** Validate that the export contains usage-detail records.
- **Steps:**
  1. Count records in `.value`.
  2. Capture `reportRefreshDate`, `userPrincipalName`, and at least one activity-date field from a sample row.
- **Expected Result:** Record count is `>= 1`.
- **Fail Closed:** Zero records returned.

### Test 4: Response and Export Behavior Validation

- **Objective:** Confirm expected Microsoft Graph response/export behavior for the selected mode.
- **Steps:**
  1. JSON path: verify `200 OK` semantics and JSON payload in output file.
  2. Optional CSV path: call legacy beta endpoint with `$format=text/csv` and capture redirect response details.
- **Expected Result:** JSON mode returns data; CSV mode shows documented redirect/download behavior.
- **Fail Closed:** Response mode differs from docs without documented explanation.

### Test 5: Throttling and Retry Controls

- **Objective:** Validate handling of Graph throttling events.
- **Steps:**
  1. On `429 Too Many Requests`, inspect `Retry-After`.
  2. Re-run after the required wait time.
  3. Log retry count and final outcome.
- **Expected Result:** Process follows `Retry-After` guidance and logs retries.
- **Fail Closed:** Repeated throttling with no successful retrieval in the approved execution window.

### Test 6: Caveat and Coverage Documentation

- **Objective:** Confirm that known API limitations are documented with evidence.
- **Steps:**
  1. Record that the control uses a beta API surface.
  2. Record that availability is global-service-only per docs.
  3. Record that unlicensed Copilot Chat usage is excluded from this API.
- **Expected Result:** Verification packet includes explicit caveat statements.
- **Fail Closed:** Caveats omitted from evidence package.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Beta cmdlet execution transcript | PowerShell session | Text log | Quarterly archive |
| Usage-detail export artifact | Microsoft Graph beta API | JSON/CSV | Quarterly archive |
| Authorization proof | Entra app consent + role assignment | Screenshot/export | With control record |
| Throttling/retry log | Execution transcript | Text log | With control record |
| Caveat statement | Control runbook record | Markdown/PDF | With committee packet |

## Operational Decision Rule

- **Pass:** authorization valid, export succeeds, and at least one record is present.
- **Fail:** missing permissions, unreachable endpoint, unresolved throttling, or empty result set.
- **Manual follow-up required:** pass/fail result must be reviewed with reporting cadence evidence before final control attestation.

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for failure triage.
- Coordinate with [Control 4.6](../4.6/portal-walkthrough.md) for impact analytics that are outside this verification scope.
- Back to [Control 4.5](../../../controls/pillar-4-operations/4.5-usage-analytics.md).
