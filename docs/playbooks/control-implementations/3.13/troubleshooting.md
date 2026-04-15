# Control 3.13: FFIEC IT Examination Handbook Alignment — Troubleshooting

Common issues and resolution steps for FFIEC IT Examination Handbook alignment and examination preparation.

## Common Issues

### Issue 1: Incomplete Control Mapping to FFIEC Booklets

- **Symptoms:** Examiner identifies Copilot governance areas that are not mapped to the applicable FFIEC booklet requirements.
- **Root Cause:** Initial mapping may not have covered all FFIEC booklet areas relevant to AI technology, or new booklet updates added requirements.
- **Resolution:**
  1. Review the latest FFIEC booklet revisions for new requirements.
  2. Conduct a gap analysis between current control mappings and booklet requirements.
  3. Create new improvement actions in Compliance Manager for unmapped areas.
  4. Assign owners and deadlines for gap remediation.

### Issue 2: Examiner Requesting Evidence Not Pre-Assembled

- **Symptoms:** During an examination, the examiner requests evidence that is not in the pre-assembled evidence pack.
- **Root Cause:** Pre-assembly may not have anticipated all possible examiner requests, or the examination scope includes areas not previously covered.
- **Resolution:**
  1. Use automation scripts to quickly generate the requested evidence from audit logs and configuration data.
  2. Document the gap for inclusion in the next pre-assembly cycle.
  3. Request reasonable time from the examiner to compile the evidence.
  4. Update the evidence pack template to include the newly identified evidence category.

### Issue 3: Compliance Manager Assessment Score Lower Than Expected

- **Symptoms:** The Compliance Manager compliance score for the FFIEC assessment is lower than the target, raising concerns before examination.
- **Root Cause:** Some improvement actions may be incomplete, or automated assessments may show false negatives for controls configured via PowerShell.
- **Resolution:**
  1. Review each incomplete improvement action and its blocking items.
  2. For automated assessments showing incorrect status, manually override with supporting evidence.
  3. Prioritize high-impact improvement actions that affect the most compliance score points.
  4. Document the score improvement plan and timeline.

### Issue 4: Cross-Pillar Evidence Coordination Failures

- **Symptoms:** Evidence for FFIEC alignment requires data from multiple Copilot governance pillars, and coordination across teams is delayed.
- **Root Cause:** FFIEC alignment spans all four governance pillars, requiring coordination across multiple control owners and teams.
- **Resolution:**
  1. Designate a single FFIEC examination coordinator to manage cross-pillar evidence requests.
  2. Create a shared evidence repository accessible to all control owners.
  3. Implement a weekly coordination meeting during examination preparation periods.
  4. Use the centralized evidence pack generator (Control 3.12) to consolidate cross-pillar evidence.

## Diagnostic Steps

1. **Review assessment status:** Open Compliance Manager and check the FFIEC assessment completion percentage.
2. **Check evidence freshness:** Run the evidence freshness audit from Control 3.12.
3. **Verify automation scripts:** Run each FFIEC evidence collection script to confirm they execute successfully.
4. **Test examiner response process:** Simulate an evidence request and measure end-to-end response time.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Active examination with significant evidence gaps | Chief Compliance Officer + Legal + examination coordinator |
| High | Assessment score below target threshold | Compliance leadership + Control owners |
| Medium | Evidence coordination delays | FFIEC examination coordinator |
| Low | Minor mapping or documentation gaps | Assigned improvement action owners |

## Related Resources

- [Control 3.12: Evidence Collection and Audit Attestation](../3.12/portal-walkthrough.md)
- [Control 3.7: Regulatory Reporting](../3.7/portal-walkthrough.md)
- [Control 3.8: Model Risk Management](../3.8/portal-walkthrough.md)
- Back to [Control 3.13](../../../controls/pillar-3-compliance/3.13-ffiec-alignment.md)
