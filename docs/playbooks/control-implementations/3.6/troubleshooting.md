# Control 3.6: Supervision and Oversight (FINRA 3110 / SEC Reg BI) — Troubleshooting

Common issues and resolution steps for supervisory controls over Copilot-assisted activities.

## Common Issues

### Issue 1: Supervisory Review Backlog Exceeding SLA

- **Symptoms:** Review items are aging beyond the 24/48 hour SLA, supervisors report insufficient time for reviews.
- **Root Cause:** Supervisor-to-representative ratio too high, policy scope too broad, or supervisors lack training on review tools.
- **Resolution:**
  1. Check current supervisor ratios and redistribute if any supervisor exceeds 1:50.
  2. Implement automated resolution for low-risk, low-confidence policy matches.
  3. Provide refresher training on the Communication compliance review interface.
  4. Consider adding a deputy supervisor role for backup coverage.

### Issue 2: Pre-Send Hold Causing Business Disruption

- **Symptoms:** Time-sensitive client communications are delayed by pre-send supervisory holds, leading to complaints.
- **Root Cause:** Pre-send hold scope may be too broad, or supervisor response time is too slow for urgent communications.
- **Resolution:**
  1. Narrow pre-send hold to only high-risk communication types (investment recommendations, new account openings).
  2. Implement an expedited review path for time-sensitive items (4-hour SLA).
  3. Designate on-call supervisors for real-time review during business hours.
  4. Move lower-risk communications to post-send review with escalation triggers.

### Issue 3: Supervisory Hierarchy Not Reflecting Organizational Changes

- **Symptoms:** New representatives are not assigned to supervisors, or departed supervisors still have assigned users.
- **Root Cause:** Supervisory hierarchy is not synchronized with HR or registration systems.
- **Resolution:**
  1. Audit the current supervisory hierarchy against the firm's registration database.
  2. Update group memberships for any misaligned users.
  3. Implement a monthly reconciliation process between HR systems and supervisory groups.
  4. Configure Azure AD dynamic groups to auto-assign based on department and registration attributes.

### Issue 4: Reg BI Documentation Gaps in Copilot-Drafted Recommendations

- **Symptoms:** Supervisory reviewers find that Copilot-drafted recommendations lack required Reg BI elements.
- **Root Cause:** Copilot may not automatically include all required disclosure and documentation elements in its generated content.
- **Resolution:**
  1. Create Copilot prompt templates that include Reg BI required elements as placeholders.
  2. Train representatives to verify Reg BI completeness before submitting for review.
  3. Add a Reg BI checklist to the supervisory review workflow.
  4. Consider configuring Copilot declarative agents with instructions to include required disclosures.

## Diagnostic Steps

1. **Review supervisor assignments:** Verify all Copilot-enabled reps have an assigned supervisor.
2. **Check SLA metrics:** Run the SLA compliance script to identify systemic delays.
3. **Audit policy scope:** Confirm policies target the correct user groups and communication channels.
4. **Test the review workflow:** Process a test item through the complete supervisory review cycle.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Supervisory review system non-functional | Chief Compliance Officer + Microsoft Support |
| High | Systematic SLA breaches across multiple supervisors | Compliance leadership — capacity review |
| Medium | Individual supervisor backlog issues | Reassign representatives or add backup |
| Low | Minor workflow inefficiencies | Address in next quarterly process review |

## Related Resources

- [Control 3.4: Communication Compliance Monitoring](../3.4/portal-walkthrough.md)
- [Control 3.5: FINRA Rule 2210 Compliance](../3.5/portal-walkthrough.md)
- [Control 3.7: Regulatory Reporting](../3.7/portal-walkthrough.md)
