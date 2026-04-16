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

- **Symptoms:** Copilot audit records expire after default 180-day period (all license tiers) despite a longer retention policy being configured.
- **Root Cause:** The retention policy priority may be lower than the default policy, or the record type filter may not match.
- **Resolution:**
  1. Review all retention policies: `Get-UnifiedAuditLogRetentionPolicy | Format-List`
  2. Verify the FSI policy has a higher priority number than the default policy.
  3. Confirm `RecordTypes` includes `CopilotInteraction`.
  4. If needed, update priority: `Set-UnifiedAuditLogRetentionPolicy -Name "FSI-Copilot-6Year-Retention" -Priority 100`

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

### Issue 5: Agent Events Not Appearing (AgentAdminActivity Latency)

- **Symptoms:** An administrator creates or modifies a Copilot agent, but no `AgentAdminActivity` event appears in the Unified Audit Log when searching immediately after.
- **Root Cause:** Agent administrative events may have longer ingestion latency than standard CopilotInteraction events — typically 30 minutes to 4 hours depending on tenant load and event pipeline. This is expected behavior, not a configuration error.
- **Resolution:**
  1. Wait at least 4 hours after the agent configuration change before searching for the event.
  2. If no event appears after 24 hours, verify the administrator performing the change has sufficient permissions for the action to be logged.
  3. Search with a broader date range to account for potential timestamp alignment issues: `Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-2) -EndDate (Get-Date) -RecordType AgentAdminActivity`
  4. Confirm the `AgentAdminActivity` record type is available in your tenant by checking the Microsoft 365 Admin Center under Service features.

### Issue 6: PAYG Billing Unexpected Cost Spike

- **Symptoms:** Azure Cost Management shows a significantly higher-than-expected charge for Purview audit billing in a given month.
- **Root Cause:** High-volume Copilot usage periods (e.g., during a regulatory examination when administrators are running repeated audit searches and exports) generate significantly more audit events than baseline operations. PAYG billing at $0.01 per event accumulates rapidly at scale.
- **Resolution:**
  1. Review Azure Cost Management to identify which audit event types are driving the spike: filter by Purview resource and review the event type breakdown.
  2. Check whether any automated scripts or API subscriptions are generating duplicate event ingestion.
  3. Evaluate whether E5 Audit Premium licensing would be more cost-effective than PAYG for the current event volume — if monthly PAYG costs consistently exceed the per-user cost of E5 Compliance for the same user population, consider switching to E5 licensing.
  4. Set a budget alert in Azure Cost Management at 75% of your approved monthly audit spend limit to provide early warning before costs become unmanageable.

### Issue 7: JailbreakDetected False Positives

- **Symptoms:** The JailbreakDetected field is populated as `true` on audit records for interactions that appear to be legitimate business queries, not actual jailbreak attempts.
- **Root Cause:** Microsoft's jailbreak detection model uses heuristics that may trigger on certain complex prompting patterns, especially when users employ detailed structured prompts (e.g., asking Copilot to "ignore previous instructions and focus only on...") even in legitimate workflow contexts.
- **Resolution:**
  1. Do not dismiss JailbreakDetected events without review — treat each event as requiring investigation before clearing.
  2. Review the full audit record including the prompt metadata and accessed resources to assess whether the interaction was consistent with the user's normal business activities.
  3. If the user's role and context clearly explain the prompt pattern, document the investigation outcome and retain the documentation with the audit record.
  4. If JailbreakDetected false positives are frequent for a specific user or team, consider whether their workflow patterns can be modified to avoid triggering the detection model.
  5. Report persistent false positive patterns to Microsoft Support to assist with model calibration — include sanitized examples without customer data.

## Diagnostic Steps

1. **Check service health:** Verify Microsoft 365 audit service status in the Admin Center under Service Health.
2. **Verify licensing:** Confirm Copilot and E5 Compliance licenses are assigned to affected users.
3. **Test with known interaction:** Have a test user perform a Copilot action and check for the record after 30 minutes.
4. **Review admin audit log:** Check for any recent changes to audit configuration that may have disrupted logging.
5. **Check agent event latency:** For AgentAdminActivity events, allow up to 4 hours before diagnosing a missing event.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Audit logging completely non-functional | Microsoft Premier Support — Severity A |
| High | Copilot events missing for multiple users | Internal compliance team + Microsoft Support |
| High | JailbreakDetected event with no legitimate business explanation | Security incident response team — escalate per FFIEC incident response procedures |
| Medium | AgentAdminActivity events missing after 24 hours | Internal IT support — verify permissions and record type availability |
| Medium | Individual user audit gaps | Internal IT support — verify licensing and configuration |
| Medium | PAYG billing spike | Finance + IT — review event volume and evaluate E5 vs PAYG cost comparison |
| Low | Minor field discrepancies | Document and monitor — review at next quarterly assessment |

## Related Resources

- [Microsoft Purview Audit documentation](https://learn.microsoft.com/purview/audit-solutions-overview)
- [Control 3.2: Data Retention Policies](../3.2/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
- Back to [Control 3.1](../../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md)
