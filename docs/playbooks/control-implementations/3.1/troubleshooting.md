# Control 3.1: Copilot Interaction Audit Logging — Troubleshooting

Common issues, diagnostic procedures, and resolution steps for Copilot interaction audit logging.

## Common Issues

### Issue 1: Copilot Interactions Not Appearing in Audit Logs

- **Symptoms:** Audit log searches for `CopilotInteraction` return no results despite confirmed Copilot usage.
- **Root Cause:** Unified Audit Log ingestion may be disabled, or insufficient time has elapsed for log propagation (up to 24 hours for some record types).
- **Resolution:**
  1. Verify audit logging is enabled: `Get-AdminAuditLogConfig | Select UnifiedAuditLogIngestionEnabled`
  2. If disabled, enable it: `Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true`
  3. Wait at least 24 hours after enabling before expecting complete Copilot interaction records.
  4. Confirm the user has a valid Copilot license assigned.

### Issue 2: Audit Retention Policy Not Applying

- **Symptoms:** Copilot audit records expire after default 90-day period despite a longer retention policy being configured.
- **Root Cause:** The retention policy priority may be lower than the default policy, or the record type filter may not match.
- **Resolution:**
  1. Review all retention policies: `Get-UnifiedAuditLogRetentionPolicy | Format-List`
  2. Verify the FSI policy has a higher priority number than the default policy.
  3. Confirm `RecordTypes` includes `CopilotInteraction`.
  4. If needed, update priority: `Set-UnifiedAuditLogRetentionPolicy -Name "FSI-Copilot-10Year-Retention" -Priority 100`

### Issue 3: Incomplete Audit Data Fields

- **Symptoms:** Copilot audit records are present but missing expected fields such as prompt text, application context, or referenced documents.
- **Root Cause:** Some Copilot audit fields require Audit (Premium) licensing. Standard audit captures fewer data points.
- **Resolution:**
  1. Verify the user has an E5 or E5 Compliance license for Audit (Premium).
  2. Check that the Audit (Premium) feature is provisioned in the tenant.
  3. Review Microsoft documentation for current Copilot audit schema fields.

### Issue 4: Search-UnifiedAuditLog Returns Maximum 5000 Results

- **Symptoms:** Audit log queries return exactly 5000 records, suggesting results are truncated.
- **Root Cause:** The `Search-UnifiedAuditLog` cmdlet has a built-in result size limit of 5000 per query.
- **Resolution:**
  1. Use the `SessionCommand` parameter with `ReturnLargeSet` to paginate results.
  2. Narrow the date range to reduce result volume per query.
  3. Use a session-based approach:
     ```powershell
     $sessionId = [Guid]::NewGuid().ToString()
     do {
         $batch = Search-UnifiedAuditLog -StartDate $start -EndDate $end `
             -RecordType CopilotInteraction -SessionId $sessionId `
             -SessionCommand ReturnLargeSet -ResultSize 5000
         $results += $batch
     } while ($batch.Count -eq 5000)
     ```

## Diagnostic Steps

1. **Check service health:** Verify Microsoft 365 audit service status in the Admin Center under Service Health.
2. **Verify licensing:** Confirm Copilot and E5 Compliance licenses are assigned to affected users.
3. **Test with known interaction:** Have a test user perform a Copilot action and check for the record after 30 minutes.
4. **Review admin audit log:** Check for any recent changes to audit configuration that may have disrupted logging.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Audit logging completely non-functional | Microsoft Premier Support — Severity A |
| High | Copilot events missing for multiple users | Internal compliance team + Microsoft Support |
| Medium | Individual user audit gaps | Internal IT support — verify licensing and configuration |
| Low | Minor field discrepancies | Document and monitor — review at next quarterly assessment |

## Related Resources

- [Microsoft Purview Audit documentation](https://learn.microsoft.com/purview/audit-solutions-overview)
- [Control 3.2: Data Retention Policies](../3.2/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
