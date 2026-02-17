# Control 3.11: Record Keeping and Books-and-Records Compliance — Troubleshooting

Common issues and resolution steps for records management of Copilot-generated content.

## Common Issues

### Issue 1: Auto-Apply Labels Not Classifying Copilot Content

- **Symptoms:** Copilot-generated documents and communications remain unlabeled after the auto-apply policy is deployed.
- **Root Cause:** Auto-apply conditions may not match Copilot content characteristics, or policy indexing is incomplete.
- **Resolution:**
  1. Verify auto-apply policy status: check for `DistributionStatus: Success`.
  2. Allow up to 7 days for initial policy deployment and indexing.
  3. Review the auto-apply conditions (keywords, SIT, trainable classifier) against actual Copilot output.
  4. Test conditions against sample Copilot content using the Content Explorer.
  5. As an interim measure, assign default retention labels to sites with Copilot-generated content.

### Issue 2: Regulatory Record Label Preventing Legitimate Updates

- **Symptoms:** Users cannot update or modify documents that have been marked as regulatory records.
- **Root Cause:** Regulatory record labels enforce strict immutability, preventing any modification to the content.
- **Resolution:**
  1. Clarify with the user that regulatory records are intentionally immutable per SEC 17a-4.
  2. If the user needs to create an updated version, instruct them to create a new document and apply the appropriate label.
  3. Review whether the regulatory record designation is appropriate for the content type — not all content requires regulatory record status.
  4. Use retention labels without the regulatory record flag for content that may need updates.

### Issue 3: Preservation Lock Applied Prematurely

- **Symptoms:** A retention policy has Preservation Lock enabled, but the policy settings need modification (incorrect retention duration or scope).
- **Root Cause:** Preservation Lock was enabled before the policy was fully validated, and it is irreversible.
- **Resolution:**
  1. Acknowledge that Preservation Lock cannot be removed — this is by design for SEC 17a-4(f) compliance.
  2. Create a new retention policy with the correct settings and deploy it alongside the locked policy.
  3. The locked policy will continue to apply its retention; the new policy will add additional retention as needed.
  4. Document the situation and update procedures to require formal approval before enabling Preservation Lock.

### Issue 4: Disposition Review Backlog

- **Symptoms:** Records approaching their retention expiration date accumulate in the disposition review queue without timely processing.
- **Root Cause:** Disposition reviewers are not assigned, not trained, or the volume exceeds review capacity.
- **Resolution:**
  1. Verify disposition reviewers are assigned to each retention label.
  2. Set up automated notifications for pending disposition reviews.
  3. Establish a regular disposition review schedule (weekly or monthly).
  4. For high-volume categories, consider extending retention rather than deleting to reduce review burden.

## Diagnostic Steps

1. **Check label deployment:** `Get-ComplianceTag | Select Name, RetentionDuration, IsRecordLabel, Regulatory`
2. **Verify auto-apply policies:** `Get-RetentionCompliancePolicy | Where IsAutoApply -eq $true`
3. **Review Preservation Lock:** `Get-RetentionCompliancePolicy | Select Name, RestrictiveRetention`
4. **Check disposition queue:** Navigate to Purview > Records management > Disposition.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Records deleted before retention period expires | Legal + Compliance + Microsoft Support |
| High | Preservation Lock misconfiguration | Records management lead + Legal |
| Medium | Auto-apply classification accuracy below 80% | Compliance team for policy tuning |
| Low | Disposition review backlog | Assign additional reviewers |

## Related Resources

- [Control 3.2: Data Retention Policies](../3.2/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
