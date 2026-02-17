# Control 3.4: Communication Compliance Monitoring — Troubleshooting

Common issues and resolution steps for communication compliance monitoring of Copilot-assisted communications.

## Common Issues

### Issue 1: High False Positive Rate

- **Symptoms:** Review queue is flooded with benign communications flagged as potential violations, overwhelming reviewers.
- **Root Cause:** Policy conditions or trainable classifiers may be too broadly configured, or keyword lists may match common business terminology.
- **Resolution:**
  1. Review the top 20 false positive items to identify common patterns.
  2. Add exclusion conditions to filter benign patterns (e.g., standard disclaimers, templates).
  3. Retrain classifiers with additional false positive examples if using trainable classifiers.
  4. Adjust the review sampling percentage for lower-risk conditions while maintaining 100% for high-risk.

### Issue 2: Copilot Communications Not Being Captured

- **Symptoms:** Known Copilot-assisted communications do not appear in the monitoring scope or review queue.
- **Root Cause:** The Copilot interaction location may not be included in the policy, or the user is not in the supervised scope.
- **Resolution:**
  1. Edit the policy and verify "Copilot interactions" is enabled as a supervised location.
  2. Confirm the user is a member of the supervised user group.
  3. Check that the user has an active Copilot license.
  4. Wait 24 hours after policy changes for full propagation.

### Issue 3: Review Queue Backlog Growing

- **Symptoms:** Pending review items accumulate faster than the team can process them, risking SLA breaches.
- **Root Cause:** Insufficient reviewer capacity, overly broad policy conditions, or lack of automated resolution rules.
- **Resolution:**
  1. Add additional reviewers to the policy.
  2. Implement automated resolution rules for known low-risk patterns.
  3. Use the bulk resolution feature for categories of items that can be resolved together.
  4. Review policy conditions to narrow the scope of captured communications.
  5. Consider reducing the sampling percentage for lower-risk channels.

### Issue 4: Trainable Classifier Underperforming

- **Symptoms:** Classifier fails to detect known compliance violations or produces inconsistent results.
- **Root Cause:** Insufficient training data, domain-specific language not represented in training set, or classifier model not updated.
- **Resolution:**
  1. Review classifier performance metrics in the Communication compliance dashboard.
  2. Provide additional labeled training data — minimum 50 positive and 50 negative samples recommended.
  3. Retrain the classifier with updated samples.
  4. Consider using custom sensitive information types as a supplement to classifiers.

## Diagnostic Steps

1. **Check policy status:** Navigate to Communication compliance > Policies and verify status is "Active".
2. **Review recent matches:** Check the policy dashboard for match volume trends over the past 30 days.
3. **Verify reviewer access:** Confirm all assigned reviewers have the Communication Compliance Analyst or Investigator role.
4. **Test with known content:** Send a test message containing content that should trigger a match.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Policy completely non-functional — no communications being monitored | Compliance leadership + Microsoft Support |
| High | Significant detection gaps for high-risk content | Compliance team — policy tuning review |
| Medium | SLA breaches on review queue | Add reviewers and optimize policy conditions |
| Low | Minor classifier accuracy issues | Schedule retraining and add training samples |

## Related Resources

- [Control 3.5: FINRA Rule 2210 Compliance](../3.5/portal-walkthrough.md)
- [Control 3.6: Supervision and Oversight](../3.6/portal-walkthrough.md)
