# Control 3.1: Copilot Interaction Audit Logging — Troubleshooting

Common issues, diagnostic procedures, and resolution steps for Copilot interaction audit logging.

## Common Issues

### Issue 1: Copilot Interactions Not Appearing in Audit Logs

- **Symptoms:** Audit log searches for `CopilotInteraction` return no results despite confirmed Copilot usage.
- **Root Cause:** Unified Audit Log ingestion may be disabled, or insufficient time has elapsed for normal audit ingestion. Microsoft doesn't guarantee a specific SLA; core services are typically available within 60 to 90 minutes after an event occurs, while other services may take longer.
- **Resolution:**
  1. Verify audit logging is enabled: `Get-AdminAuditLogConfig | Select UnifiedAuditLogIngestionEnabled`
  2. If disabled, enable it: `Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true`
  3. Allow for the normal audit-ingestion window before treating missing results as a failure; core services are typically available within 60 to 90 minutes, while other services may take longer.
  4. Confirm the user has a valid Copilot license assigned.

### Issue 2: Audit Retention Policy Not Applying

- **Symptoms:** Copilot audit records expire after default 180-day period (all license tiers) despite a longer retention policy being configured.
- **Root Cause:** A conflicting custom policy with a lower numeric priority value may be taking precedence, the policy may reuse a duplicate priority value, or the record type filter may not match.
- **Resolution:**
  1. Review all retention policies: `Get-UnifiedAuditLogRetentionPolicy | Format-List`
  2. Verify the FSI policy uses a unique priority value and that its intended precedence is correct. Lower numbers take precedence over higher numbers among custom policies, and custom policies take precedence over the default policy.
  3. Confirm `RecordTypes` includes `CopilotInteraction`.
  4. If needed, update the existing policy with a complete command: `Set-UnifiedAuditLogRetentionPolicy -Identity "FSI-Copilot-10Year-Retention" -RetentionDuration TenYears -Priority 100`. Keep priorities unique — for example, use `110` for `FSI-AgentAdmin-10Year-Retention`.

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

### Issue 5: Agent Events Not Appearing (CopilotAgentManagement Latency)

- **Symptoms:** An administrator creates or modifies a Copilot agent, but no `CopilotAgentManagement` event appears in the Unified Audit Log when searching immediately after.
- **Root Cause:** Microsoft doesn't guarantee a specific audit-ingestion SLA. Core services are typically available within 60 to 90 minutes after an event occurs, while other services may take longer. Delayed Copilot agent records aren't by themselves proof of a configuration failure.
- **Resolution:**
  1. Allow for normal audit ingestion; core services typically appear within 60 to 90 minutes, while other services may take longer.
  2. Search with a broader date range to account for potential timestamp alignment issues: `Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-2) -EndDate (Get-Date) -RecordType CopilotAgentManagement`
  3. Confirm the `CopilotAgentManagement` record type is available in your tenant by checking the Microsoft 365 Admin Center under Service features.
  4. If records still don't appear after allowing additional time and broadening the search, verify the administrator performing the change had sufficient permissions for the action to be logged.

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
3. **Test with known interaction:** Have a test user perform a Copilot action and check for the record after the normal audit-ingestion window (typically 60 to 90 minutes for core services; other services may take longer).
4. **Review admin audit log:** Check for any recent changes to audit configuration that may have disrupted logging.
5. **Check agent event latency:** For CopilotAgentManagement events, allow for the normal audit-ingestion window first and broaden the search before diagnosing a missing event.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Audit logging completely non-functional | Microsoft Premier Support — Severity A |
| High | Copilot events missing for multiple users | Internal compliance team + Microsoft Support |
| High | JailbreakDetected event with no legitimate business explanation | Security incident response team — escalate per FFIEC incident response procedures |
| Medium | CopilotAgentManagement events still missing after repeated checks beyond the normal audit-ingestion window | Internal IT support — verify permissions and record type availability |
| Medium | Individual user audit gaps | Internal IT support — verify licensing and configuration |
| Medium | PAYG billing spike | Finance + IT — review event volume and evaluate E5 vs PAYG cost comparison |
| Low | Minor field discrepancies | Document and monitor — review at next quarterly assessment |

## Related Resources

- [Microsoft Purview Audit documentation](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)
- [Control 3.2: Data Retention Policies](../3.2/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
- Back to [Control 3.1](../../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md)
