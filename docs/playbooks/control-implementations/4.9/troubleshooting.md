# Control 4.9: Incident Reporting and Root Cause Analysis — Troubleshooting

Common issues and resolution steps for Copilot incident reporting and root cause analysis.

## Common Issues

### Issue 1: Alert Policies Not Triggering

- **Symptoms:** Known Copilot incidents occur without triggering configured alert policies.
- **Root Cause:** Alert thresholds may be set too high, the alert policy may not be active, or the event type may not match the alert condition.
- **Resolution:**
  1. Verify alert policies are enabled in the Purview portal.
  2. Review threshold settings and lower them if incidents are being missed.
  3. Check that the alert conditions match the actual event record types in the audit log.
  4. Test with a simulated event to confirm the alert pipeline is functional.

### Issue 2: Incomplete Root Cause Analysis

- **Symptoms:** RCA reports lack sufficient detail to identify the true root cause or prevent recurrence.
- **Root Cause:** Insufficient audit log data, lack of RCA training, or time pressure leading to surface-level analysis.
- **Resolution:**
  1. Ensure audit logging captures sufficient detail for Copilot interactions (Control 3.1).
  2. Provide RCA methodology training (5 Whys, fishbone diagrams) to the incident response team.
  3. Allow adequate time for thorough RCA rather than rushing to closure.
  4. Implement a peer review process for RCA quality assurance.

### Issue 3: Delayed Regulatory Notification Assessment

- **Symptoms:** Regulatory notification decisions are delayed, risking missed notification deadlines.
- **Root Cause:** The assessment workflow lacks clear ownership, or the CCO is unavailable for timely approval.
- **Resolution:**
  1. Designate a deputy CCO for regulatory notification decisions when the CCO is unavailable.
  2. Implement a time-bound escalation path (e.g., auto-escalate after 4 hours without a decision).
  3. Pre-define notification criteria that can be assessed quickly based on incident category and impact.
  4. Maintain a current contact list for regulatory notification recipients at each regulator.

### Issue 4: Incident Classification Disagreements

- **Symptoms:** Teams disagree on the severity level or category of a Copilot incident, delaying response.
- **Root Cause:** Incident classification criteria are ambiguous or do not address Copilot-specific scenarios.
- **Resolution:**
  1. Review and update the incident classification criteria with Copilot-specific examples.
  2. Establish a tie-breaking authority (e.g., CISO for security incidents, CCO for compliance incidents).
  3. Create a decision matrix that maps incident characteristics to severity levels.
  4. Conduct tabletop exercises to calibrate the team's classification consistency.

## Diagnostic Steps

1. **Check alert policy status:** Navigate to Purview > Policies > Alert policies and verify status.
2. **Review recent alerts:** Check the Alerts dashboard for recent Copilot-related alerts.
3. **Verify audit log coverage:** Confirm Copilot events are present in the audit log.
4. **Test notification delivery:** Send a test alert to verify email notification delivery.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Active Copilot data breach | CISO + CCO + Legal — immediate response |
| High | Regulatory notification deadline at risk | CCO + Legal — immediate assessment |
| Medium | Alert system failures | IT Security — investigate and restore |
| Low | RCA quality issues | Incident response team lead — process improvement |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 4.10: Business Continuity and Disaster Recovery](../4.10/portal-walkthrough.md)
- [Control 4.11: Microsoft Sentinel Integration](../4.11/portal-walkthrough.md)
- Back to [Control 4.9](../../../controls/pillar-4-operations/4.9-incident-reporting.md)
