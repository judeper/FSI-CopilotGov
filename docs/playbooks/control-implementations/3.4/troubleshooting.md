# Control 3.4: Communication Compliance Monitoring — Troubleshooting

Common issues and resolution steps for communication compliance monitoring of Copilot-assisted communications, including IRM integration issues.

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

### Issue 3: IRM Integration Not Showing CC Indicators

- **Symptoms:** CC policy matches are occurring, but no corresponding risk indicators appear in the IRM dashboard for affected users.
- **Root Cause:** Common causes include: IRM integration not enabled in CC Settings, propagation delay (up to 24 hours), licensing gap, or no active IRM policy targeting the affected users.
- **Resolution:**
  1. Verify IRM integration is enabled: navigate to **Communication compliance > Settings > Insider Risk Management integration** and confirm the toggle is On.
  2. Wait at least 24 hours after a CC match before expecting the IRM indicator to appear -- there is a propagation delay.
  3. Confirm the affected users are within the scope of at least one active IRM policy in Control 2.10.
  4. Verify that both CC and IRM require E5 or equivalent licensing -- confirm licenses are assigned to affected users.
  5. Run Script 4 from the PowerShell Setup playbook to check the audit log for CC-sourced IRM events.
  6. If indicators still do not appear after 48 hours, open a support ticket with Microsoft referencing the IRM-CC integration toggle.

### Issue 4: CC Policies Not Detecting Expanded Copilot Surfaces

- **Symptoms:** Known communications from Security Copilot or Copilot Studio interactions are not appearing in the CC review queue.
- **Root Cause:** This framework's configuration guidance covers Microsoft 365 Copilot and Copilot Chat only. Security Copilot, Fabric Copilot, and Copilot Studio are mentioned in this control for awareness -- their CC monitoring configuration is outside this framework's scope.
- **Resolution:**
  1. Confirm the surface in question is within scope for this framework (Microsoft 365 Copilot or Microsoft 365 Copilot Chat).
  2. For out-of-scope surfaces (Security Copilot, Fabric Copilot, Copilot Studio), consult Microsoft documentation specific to those products for CC monitoring configuration.
  3. For in-scope surfaces that are not being captured, verify "Copilot interactions" is enabled as a supervised location in the policy (see Issue 2).

### Issue 5: Review Queue Backlog Growing

- **Symptoms:** Pending review items accumulate faster than the team can process them, risking SLA breaches.
- **Root Cause:** Insufficient reviewer capacity, overly broad policy conditions, or lack of automated resolution rules.
- **Resolution:**
  1. Add additional reviewers to the policy.
  2. Implement automated resolution rules for known low-risk patterns.
  3. Use the bulk resolution feature for categories of items that can be resolved together.
  4. Review policy conditions to narrow the scope of captured communications.
  5. Consider reducing the sampling percentage for lower-risk channels.

### Issue 6: Trainable Classifier Underperforming

- **Symptoms:** Classifier fails to detect known compliance violations or produces inconsistent results.
- **Root Cause:** Insufficient training data, domain-specific language not represented in training set, or classifier model not updated.
- **Resolution:**
  1. Review classifier performance metrics in the Communication compliance dashboard.
  2. Provide additional labeled training data -- minimum 50 positive and 50 negative samples recommended.
  3. Retrain the classifier with updated samples.
  4. Consider using custom sensitive information types as a supplement to classifiers.

## Diagnostic Steps

1. **Check policy status:** Navigate to Communication compliance > Policies and verify status is "Active".
2. **Review recent matches:** Check the policy dashboard for match volume trends over the past 30 days.
3. **Verify IRM integration:** Navigate to Communication compliance > Settings > Insider Risk Management integration and confirm toggle is On.
4. **Run IRM audit check:** Use Script 4 from the PowerShell Setup playbook to check for CC-sourced IRM events.
5. **Verify reviewer access:** Confirm all assigned reviewers have the Communication Compliance Analyst or Investigator role.
6. **Test with known content:** Send a test message containing content that should trigger a match.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Policy completely non-functional -- no communications being monitored | Compliance leadership + Microsoft Support |
| High | IRM integration not producing indicators after 48 hours | Compliance team + Microsoft Support -- reference IRM-CC integration |
| High | Significant detection gaps for high-risk content | Compliance team -- policy tuning review |
| Medium | SLA breaches on review queue | Add reviewers and optimize policy conditions |
| Low | Minor classifier accuracy issues | Schedule retraining and add training samples |

## Related Resources

- [Control 2.10: Insider Risk Detection](../../pillar-2-security/2.10/portal-walkthrough.md)
- [Control 3.5: FINRA Rule 2210 Compliance](../3.5/portal-walkthrough.md)
- [Control 3.6: Supervision and Oversight](../3.6/portal-walkthrough.md)
