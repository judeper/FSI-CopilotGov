# Control 4.4: Copilot in Viva Suite Governance — Troubleshooting

Common issues and resolution steps for Copilot governance across the Viva suite.

## Common Issues

### Issue 1: Copilot Chat Insights Not Populating in Viva Insights

- **Symptoms:** The Copilot Chat analytics dashboard in Viva Insights shows no data, or all department adoption rates appear as zero despite known Copilot Chat activity.
- **Root Cause:** Data delay (Copilot Chat usage data takes 48–72 hours to appear in Viva Insights analytics), licensing gap (Viva Insights P2 or Viva Suite license required), or analytics not enabled in the Viva Insights Admin portal.
- **Resolution:**
  1. Verify the Viva Insights P2 or Viva Suite license is assigned to users whose data should appear in analytics.
  2. Confirm Copilot Chat analytics is enabled: navigate to the Viva Insights Admin portal (`insights.viva.office.com` > Admin > Advanced Insights settings) and verify the Copilot analytics toggle is **On**.
  3. Allow up to 72 hours for Copilot Chat usage data to populate in the analytics dashboard — check again after the data propagation period.
  4. If data still does not appear after 72 hours, verify that users have the Microsoft 365 Copilot license assigned (Copilot Chat usage data requires an active Copilot license).
  5. Run Script 2 from the PowerShell Setup guide to confirm the usage report API returns data — if it fails, the license or settings configuration is the root cause.

### Issue 2: Engage Content Not Captured by Teams Compliance Policies After Engage-to-Teams Integration

- **Symptoms:** Viva Engage community content surfacing in Teams channels is not appearing in Teams-scoped eDiscovery searches or Communication Compliance review queues.
- **Root Cause:** The Engage-to-Teams integration is active for display purposes but the compliance policies were not updated to include the Teams channel locations receiving Engage content; or the Engage content is treated as Yammer-origin only and requires Yammer-scoped policy search.
- **Resolution:**
  1. Verify which Teams channels receive surfaced Engage content by checking the Viva Engage Admin Center > Communities > [Community] > Connected Teams channels.
  2. In Microsoft Purview > Data Lifecycle Management, confirm that the relevant Teams retention policy explicitly includes the Teams channels receiving Engage content.
  3. For eDiscovery searches, use both Yammer/Viva Engage and Teams locations in the same search to capture all instances of Engage content regardless of where it was viewed.
  4. In Microsoft Purview > Communication Compliance, update the policy scope to include both Yammer messages and Teams channel messages — this dual-location coverage ensures Engage content is captured regardless of which interface the employee used.
  5. Allow up to 24 hours for updated policy scopes to propagate before re-testing.

### Issue 3: Viva Engage Posts Not Captured by Communication Compliance

- **Symptoms:** Copilot-assisted Viva Engage posts are not appearing in the communication compliance review queue despite active policies.
- **Root Cause:** Communication compliance policy may not include Viva Engage / Yammer as a monitored location.
- **Resolution:**
  1. Verify the communication compliance policy includes "Yammer" or "Viva Engage" as a supervised location.
  2. Confirm the user is in the supervised user scope.
  3. Allow up to 24 hours for new policy locations to propagate.
  4. Test with a known policy-triggering phrase to verify detection.

### Issue 4: Copilot Surfacing Sensitive Content in Viva Connections

- **Symptoms:** Copilot surfaces confidential or highly sensitive content on the Viva Connections dashboard.
- **Root Cause:** Sensitivity labels may not be properly restricting Copilot's content grounding for the Viva Connections surface.
- **Resolution:**
  1. Verify sensitivity labels are applied to the sensitive content.
  2. Check that the label configuration includes access restrictions.
  3. Review SharePoint site permissions for the content source.
  4. Consider using Restricted SharePoint Search to limit Copilot's content scope.

### Issue 5: Viva Learning AI Recommendations Conflicting with Compliance Training

- **Symptoms:** Copilot recommends alternative courses when users search for mandatory compliance training.
- **Root Cause:** AI recommendations may prioritize relevance or engagement metrics over compliance mandates.
- **Resolution:**
  1. Ensure mandatory compliance training is marked as required in Viva Learning.
  2. Configure learning paths that enforce sequential completion of mandatory training.
  3. Communicate to users that Copilot recommendations supplement but do not replace required training.
  4. Work with the Viva Learning team to pin mandatory training in the user experience.

### Issue 6: Viva Goals Copilot Providing Inaccurate Progress Insights

!!! warning "Retired"
    Viva Goals was retired December 31, 2025. This troubleshooting entry is no longer applicable.

- **Symptoms:** Copilot-generated progress analysis in Viva Goals does not match actual goal completion data.
- **Root Cause:** Copilot may be generating insights from incomplete or stale data, or data integration between systems is delayed.
- **Resolution:**
  1. Verify goal data integration sources are current and accurately synced.
  2. Cross-reference Copilot progress insights with the actual goal data in Viva Goals.
  3. Report inaccurate insights through the feedback mechanism for model improvement.
  4. Advise users to verify Copilot insights against actual data before making decisions.

## Diagnostic Steps

1. **Check Viva licensing:** Verify Viva suite and Copilot licenses are properly assigned. Viva Insights P2 or Viva Suite is required for Copilot Chat analytics.
2. **Verify Copilot Chat analytics enabled:** Confirm in Viva Insights Admin portal > Advanced Insights settings that Copilot analytics is toggled On.
3. **Review compliance policies:** Confirm Engage/Yammer is included in communication compliance scope and that Teams channel locations are added for Engage-to-Teams integration coverage.
4. **Test sensitivity labels:** Verify labels are applied and enforced in Viva Connections content.
5. **Verify data integrations:** Check that Viva Goals data sources are current and synced.
6. **Allow data propagation:** Copilot Chat usage data in Viva Insights has a 48–72 hour delay; retention policy scope changes propagate within 24 hours.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Sensitive content exposed via Viva Connections | IT Security + Compliance |
| High | Communication compliance gap for Engage — including Engage-to-Teams integration | Compliance team — policy update |
| High | Copilot Chat analytics showing individual-level data (privacy violation) | IT Admin + Privacy Officer — verify minimum group size configuration |
| Medium | AI recommendation conflicts with compliance training | HR + Compliance + IT |
| Low | Minor Viva Goals insight inaccuracies | Document and report to Microsoft |
| Low | Copilot Chat insights data delay | Monitor — allow 72 hours for data population |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.5: Copilot Usage Analytics](../4.5/portal-walkthrough.md)
- Back to [Control 4.4](../../../controls/pillar-4-operations/4.4-viva-suite-governance.md)
