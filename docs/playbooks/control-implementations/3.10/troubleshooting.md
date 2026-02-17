# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Troubleshooting

Common issues and resolution steps for privacy controls protecting consumer financial information in Copilot interactions.

## Common Issues

### Issue 1: DLP Not Detecting NPI in Copilot Responses

- **Symptoms:** Copilot generates responses containing SSNs, account numbers, or other NPI without triggering DLP.
- **Root Cause:** DLP policies may not cover Copilot interaction locations, or the sensitive information types do not match the data format in Copilot outputs.
- **Resolution:**
  1. Verify the DLP policy includes Copilot-relevant locations (Exchange, Teams, SharePoint).
  2. Test the sensitive information type against the specific data format appearing in Copilot responses.
  3. Update SIT patterns if Copilot formats data differently (e.g., partial masking, different separators).
  4. Enable DLP for the Copilot interaction workload if available in the tenant.

### Issue 2: Information Barriers Not Blocking Copilot Cross-Segment Access

- **Symptoms:** Users in one segment can access consumer financial data from another segment through Copilot prompts.
- **Root Cause:** Information barriers may not fully apply to Copilot's content grounding, or the barrier segments are misconfigured.
- **Resolution:**
  1. Verify information barrier policies are active: `Get-InformationBarrierPolicy | Select Name, State`
  2. Confirm segment assignments include all relevant users.
  3. Check that SharePoint sites containing NPI have correct segment associations.
  4. Test with Content Search to verify the same user cannot access cross-segment content through other search tools.

### Issue 3: Excessive DLP False Positives on Financial Data

- **Symptoms:** Legitimate financial communications are being blocked by DLP, disrupting business operations.
- **Root Cause:** Sensitive information type patterns may be matching non-NPI financial data (e.g., reference numbers, timestamps).
- **Resolution:**
  1. Review false positive incidents to identify pattern-matching issues.
  2. Add exclusion rules for known false positive patterns.
  3. Increase the confidence threshold for SIT detections.
  4. Implement context-based rules that require NPI to appear alongside other identifying information.

### Issue 4: NPI Exposure in Copilot Meeting Summaries

- **Symptoms:** Copilot meeting summaries in Teams capture verbally discussed NPI such as account numbers or SSNs.
- **Root Cause:** Copilot transcribes meeting audio and may include NPI spoken during the meeting in summaries.
- **Resolution:**
  1. Implement DLP policies on Teams meeting transcripts and summaries.
  2. Train users to avoid verbalizing full NPI during Copilot-enabled meetings.
  3. Configure Copilot meeting settings to restrict summary distribution.
  4. Apply sensitivity labels to meeting recordings and transcripts containing financial discussions.

## Diagnostic Steps

1. **Check DLP policy status:** `Get-DlpCompliancePolicy | Select Name, Enabled, Mode`
2. **Review SIT accuracy:** Test each sensitive information type against known NPI samples.
3. **Verify barrier status:** `Get-InformationBarrierPolicy | Select Name, State, Segments`
4. **Test Copilot responses:** Prompt Copilot with queries that might surface NPI from test data.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Confirmed NPI breach via Copilot interactions | Privacy Officer + Chief Compliance Officer + Legal |
| High | Systematic DLP gaps allowing NPI exposure | IT Security + Compliance team |
| Medium | Information barrier gaps for specific segments | IT + Compliance for barrier reconfiguration |
| Low | False positive rate affecting operations | Compliance team for policy tuning |

## Related Resources

- [Control 3.4: Communication Compliance Monitoring](../3.4/portal-walkthrough.md)
- [Control 3.11: Record Keeping Compliance](../3.11/portal-walkthrough.md)
