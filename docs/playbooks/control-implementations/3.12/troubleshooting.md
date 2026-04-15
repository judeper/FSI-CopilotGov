# Control 3.12: Evidence Collection and Audit Attestation — Troubleshooting

Common issues and resolution steps for evidence collection and audit attestation procedures.

## Common Issues

### Issue 1: Evidence Pack Missing Critical Control Documentation

- **Symptoms:** Regulatory examiners identify gaps in the evidence pack during examination preparation.
- **Root Cause:** Evidence collection scripts may not cover all controls, or control owners have not uploaded evidence to Compliance Manager.
- **Resolution:**
  1. Run the evidence completeness check against the full control inventory.
  2. Identify missing controls and contact assigned owners for immediate evidence submission.
  3. Update automation scripts to cover the missing control areas.
  4. Implement a mandatory pre-examination review checklist.

### Issue 2: Stale Evidence Not Updated Before Examination

- **Symptoms:** Evidence freshness audit reveals items exceeding their maximum age at the time of examination.
- **Root Cause:** Evidence refresh schedule not adhered to, or responsible parties not notified of upcoming refresh deadlines.
- **Resolution:**
  1. Run the evidence freshness audit immediately and identify stale items.
  2. Regenerate stale evidence using automation scripts.
  3. Implement automated reminders for evidence refresh deadlines.
  4. Assign backup owners for each evidence category to prevent single-point-of-failure.

### Issue 3: Attestation Approver Unavailable

- **Symptoms:** Attestation workflows are stuck pending approval because the designated approver is unavailable.
- **Root Cause:** No backup approver is configured, or the approval workflow does not support delegation.
- **Resolution:**
  1. Configure backup approvers for all attestation workflows.
  2. Implement an escalation path that automatically redirects to backup after 48 hours.
  3. Ensure at least two people are assigned to each attestation approval role.
  4. Document the delegation of authority for attestation sign-offs.

### Issue 4: Compliance Manager Automated Assessments Showing Incorrect Status

- **Symptoms:** Compliance Manager shows a control as "Not implemented" when it has been configured correctly.
- **Root Cause:** Automated assessment may not detect all configuration methods (e.g., PowerShell-configured settings vs. portal settings).
- **Resolution:**
  1. Review the automated assessment criteria for the specific control.
  2. If the configuration was done via PowerShell, manually override the assessment status in Compliance Manager.
  3. Upload manual evidence (PowerShell output, screenshots) to support the override.
  4. Document the discrepancy for future reference.

## Diagnostic Steps

1. **Run evidence completeness check:** Review the evidence pack against the full control inventory.
2. **Check freshness audit:** Run Script 4 from PowerShell Setup to identify stale items.
3. **Verify attestation status:** Check Compliance Manager for pending or overdue attestations.
4. **Test evidence retrieval:** Simulate an examiner request and measure response time.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Examination underway with evidence gaps | Chief Compliance Officer + Legal |
| High | Multiple controls lacking evidence | Compliance team + Control owners |
| Medium | Evidence freshness issues | Assigned evidence owners |
| Low | Minor attestation workflow delays | IT support for workflow configuration |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 3.7: Regulatory Reporting](../3.7/portal-walkthrough.md)
- [Control 3.13: FFIEC Alignment](../3.13/portal-walkthrough.md)
- Back to [Control 3.12](../../../controls/pillar-3-compliance/3.12-evidence-collection.md)
