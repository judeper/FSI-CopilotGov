# Control 2.4: Information Barriers for Copilot (Chinese Wall) — Troubleshooting

Common issues and resolution steps for Information Barriers.

## Common Issues

### Issue 1: Policy Application Fails or Stalls

- **Symptoms:** `Get-InformationBarrierPoliciesApplicationStatus` shows "Failed" or has been "InProgress" for more than 48 hours
- **Root Cause:** Conflicting policies, invalid segment definitions, or user attributes that do not match segment filters can prevent successful policy application.
- **Resolution:**
  1. Check application status details for specific error messages
  2. Verify segment definitions reference valid Entra ID attributes
  3. Check for policy conflicts (e.g., circular blocking rules)
  4. Verify all users in segments have the required attributes populated
  5. Remove conflicting policies, re-apply, then re-add corrected policies

### Issue 2: Users Assigned to Wrong Segments

- **Symptoms:** Users can or cannot communicate with segments they should or should not be blocked from
- **Root Cause:** User attributes in Entra ID (department, custom attributes) may not match the segment filter definitions, or recent job changes may not have been reflected.
- **Resolution:**
  1. Verify the user's Entra ID attributes: `Get-MgUser -UserId <upn> -Property Department`
  2. Compare against the segment filter: `Get-OrganizationSegment -Identity <segment>`
  3. Update user attributes in Entra ID to match the correct segment
  4. Re-apply barrier policies after attribute corrections

### Issue 3: Copilot Not Respecting Barrier Boundaries

- **Symptoms:** Copilot returns content from a segment the user should be blocked from accessing
- **Root Cause:** Information Barriers may not have fully propagated to the Copilot service, or the content may be in a shared location that both segments can access (e.g., a company-wide site).
- **Resolution:**
  1. Verify the barrier policy is in "Active" state and has been applied
  2. Check that the content is not in a location accessible to both segments
  3. Verify the site or content container has segment-appropriate permissions
  4. Allow 48 hours after policy application for full propagation to Copilot
  5. If the issue persists, open a Microsoft support ticket referencing IB and Copilot integration

### Issue 4: Barrier Exceptions Not Working

- **Symptoms:** Users configured with barrier exceptions still cannot access cross-segment content
- **Root Cause:** Exceptions may not be configured correctly, or the exception policy may not have been applied after creation.
- **Resolution:**
  1. Verify the exception configuration: check for "Allow" policies
  2. Re-apply barrier policies after creating exceptions
  3. Allow 24-48 hours for propagation
  4. Verify the user is in the correct segment for the exception to apply

### Issue 5: Performance Impact from Barrier Evaluation

- **Symptoms:** Copilot responses are noticeably slower for users in barriered segments, or Teams search takes longer than expected
- **Root Cause:** Barrier evaluation adds processing overhead to content access decisions. Complex barrier configurations with many segments may increase evaluation time.
- **Resolution:**
  1. This may be expected behavior for complex barrier configurations
  2. Simplify segment definitions where possible
  3. Monitor response times and establish performance baselines
  4. Contact Microsoft support if performance degradation is severe

### Issue 6: Channel Agent Surfaces Cross-Barrier Content

- **Symptoms:** Users report that a Channel Agent in Teams is returning content that should be restricted by Information Barriers; compliance team identifies Channel Agent responses that appear to include content from barrier-separated segments
- **Root Cause:** This is a **documented platform limitation**: Information Barriers are not supported for Channel Agent in Teams. Channel Agent does not enforce IB policies and may return content from across barrier boundaries. This is not a misconfiguration — it is the expected behavior of Channel Agent.
- **Resolution:**
  1. **Do not attempt to resolve this through IB policy adjustments** — IB enforcement for Channel Agent is not currently supported and policy changes will not fix this behavior
  2. **Immediately review the channel's membership** to determine whether IB-separated users are present in the channel where Channel Agent is deployed
  3. If IB-separated users are present in the channel: **remove the Channel Agent from that channel** — it cannot be safely deployed in channels with mixed IB-segment membership
  4. Redeploy Channel Agent only in channels with homogeneous IB-segment membership after auditing member segments
  5. **Document this incident** in the firm's supervisory procedures and escalate to Compliance per SEC Rule 10b-5 and FINRA Rules 5280, 2241, 2242 requirements if cross-barrier content was accessed
  6. As a compensating control: apply sensitivity labels to content in the channel to prevent Channel Agent from processing labeled materials; configure DSPM for AI monitoring to detect future cross-segment surfacing

### Issue 7: Uncertainty About Which Copilot Surfaces Enforce IB

- **Symptoms:** Compliance team is uncertain whether a specific Copilot surface (e.g., SharePoint Copilot, Loop Copilot) enforces Information Barriers, and functional testing results are ambiguous
- **Root Cause:** IB enforcement scope across Copilot surfaces can be difficult to verify through testing alone, particularly when both segments have access to the same public/shared content.
- **Resolution:**
  1. Use test content that is exclusively accessible within one segment (e.g., a file stored in a segment-specific SharePoint library with no sharing outside the segment)
  2. Test as a user from the barrier-separated segment and verify whether the content appears in Copilot responses
  3. Consult the Microsoft Learn page "Information Barriers and Microsoft 365 Copilot" for the current authoritative surface coverage matrix
  4. For Channel Agent specifically: IB enforcement is confirmed NOT supported — do not test hoping for enforcement; instead apply compensating controls as documented
  5. If testing reveals a surface that should enforce IB is not doing so (and the surface is not Channel Agent): verify barrier policies are in Active/Applied state, allow 48 hours for propagation, then open a Microsoft support case referencing IB and the specific Copilot surface

## Diagnostic Steps

1. **Check barrier status:** `Get-InformationBarrierPoliciesApplicationStatus`
2. **Verify segments:** `Get-OrganizationSegment | Format-Table Name, UserGroupFilter`
3. **Check user segment:** Verify user attributes match segment definitions
4. **Test communication:** Attempt cross-barrier Teams chat to verify enforcement
5. **Review audit logs:** Search for barrier-related events in unified audit log

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor segment assignment corrections needed | IT Operations |
| **Medium** | Barrier policy application delays | Microsoft support |
| **High** | Barriers not enforced for Copilot — cross-segment content accessible | Security Operations and Compliance |
| **Critical** | Chinese Wall breach detected via Copilot | Compliance Officer, Legal, and CISO immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Barrier configuration
- [PowerShell Setup](powershell-setup.md) — Barrier management scripts
- [Verification & Testing](verification-testing.md) — Barrier validation
- Back to [Control 2.4](../../../controls/pillar-2-security/2.4-information-barriers.md)
