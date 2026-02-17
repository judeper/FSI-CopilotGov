# Control 4.4: Copilot in Viva Suite Governance — Troubleshooting

Common issues and resolution steps for Copilot governance across the Viva suite.

## Common Issues

### Issue 1: Viva Engage Posts Not Captured by Communication Compliance

- **Symptoms:** Copilot-assisted Viva Engage posts are not appearing in the communication compliance review queue despite active policies.
- **Root Cause:** Communication compliance policy may not include Viva Engage / Yammer as a monitored location.
- **Resolution:**
  1. Verify the communication compliance policy includes "Yammer" or "Viva Engage" as a supervised location.
  2. Confirm the user is in the supervised user scope.
  3. Allow up to 24 hours for new policy locations to propagate.
  4. Test with a known policy-triggering phrase to verify detection.

### Issue 2: Copilot Surfacing Sensitive Content in Viva Connections

- **Symptoms:** Copilot surfaces confidential or highly sensitive content on the Viva Connections dashboard.
- **Root Cause:** Sensitivity labels may not be properly restricting Copilot's content grounding for the Viva Connections surface.
- **Resolution:**
  1. Verify sensitivity labels are applied to the sensitive content.
  2. Check that the label configuration includes access restrictions.
  3. Review SharePoint site permissions for the content source.
  4. Consider using Restricted SharePoint Search to limit Copilot's content scope.

### Issue 3: Viva Learning AI Recommendations Conflicting with Compliance Training

- **Symptoms:** Copilot recommends alternative courses when users search for mandatory compliance training.
- **Root Cause:** AI recommendations may prioritize relevance or engagement metrics over compliance mandates.
- **Resolution:**
  1. Ensure mandatory compliance training is marked as required in Viva Learning.
  2. Configure learning paths that enforce sequential completion of mandatory training.
  3. Communicate to users that Copilot recommendations supplement but do not replace required training.
  4. Work with the Viva Learning team to pin mandatory training in the user experience.

### Issue 4: Viva Goals Copilot Providing Inaccurate Progress Insights

- **Symptoms:** Copilot-generated progress analysis in Viva Goals does not match actual goal completion data.
- **Root Cause:** Copilot may be generating insights from incomplete or stale data, or data integration between systems is delayed.
- **Resolution:**
  1. Verify goal data integration sources are current and accurately synced.
  2. Cross-reference Copilot progress insights with the actual goal data in Viva Goals.
  3. Report inaccurate insights through the feedback mechanism for model improvement.
  4. Advise users to verify Copilot insights against actual data before making decisions.

## Diagnostic Steps

1. **Check Viva licensing:** Verify Viva suite and Copilot licenses are properly assigned.
2. **Review compliance policies:** Confirm Engage/Yammer is included in communication compliance scope.
3. **Test sensitivity labels:** Verify labels are applied and enforced in Viva Connections content.
4. **Verify data integrations:** Check that Viva Goals data sources are current and synced.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Sensitive content exposed via Viva Connections | IT Security + Compliance |
| High | Communication compliance gap for Engage | Compliance team — policy update |
| Medium | AI recommendation conflicts with compliance training | HR + Compliance + IT |
| Low | Minor Viva Goals insight inaccuracies | Document and report to Microsoft |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.5: Copilot Usage Analytics](../4.5/portal-walkthrough.md)
