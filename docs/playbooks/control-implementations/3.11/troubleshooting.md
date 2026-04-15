# Control 3.11: Record Keeping and Books-and-Records Compliance — Troubleshooting

Common issues and resolution steps for records management of Copilot-generated content, including audit-trail alternative compliance, mobile Copilot access gaps, and off-channel risk assessment.

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
  1. Clarify with the user that regulatory records are intentionally immutable per SEC 17a-4. This immutability is what enables the audit-trail alternative under Rule 17a-4(f)(2)(ii)(A).
  2. If the user needs to create an updated version, instruct them to create a new document and apply the appropriate label to the new version.
  3. Review whether the regulatory record designation is appropriate for the content type -- not all content requires regulatory record status.
  4. Use retention labels without the regulatory record flag for working documents that may need updates; apply the regulatory record label only when the document is finalized.

### Issue 3: Preservation Lock Applied Prematurely or with Incorrect Settings

- **Symptoms:** A retention policy has Preservation Lock enabled, but the policy settings need modification (incorrect retention duration, missing locations, or wrong label assignments).
- **Root Cause:** Preservation Lock was enabled before the policy was fully validated, and it is irreversible.
- **Resolution:**
  1. Acknowledge that Preservation Lock cannot be removed — this is by design for SEC 17a-4(f) compliance (both WORM and audit-trail alternative paths require immutability of the governance framework itself).
  2. Create a new retention policy with the correct settings and deploy it alongside the locked policy. The locked policy will continue to apply its retention; the new policy will add additional retention or correct coverage gaps.
  3. The locked policy's retention duration cannot be shortened, but locations can be added. Use `Set-RetentionCompliancePolicy -Identity "policy-name" -AddSharePointLocation "new-site"` to add missing locations.
  4. Document the situation: update procedures to require formal written approval from the Records Management lead and Legal before enabling Preservation Lock in the future.
  5. If the locked policy has fundamentally incorrect settings (e.g., retention duration too short for 17a-4 requirements), consult with legal counsel — the locked policy may require disclosure to regulators if it creates a compliance gap.

### Issue 4: Disposition Review Backlog

- **Symptoms:** Records approaching their retention expiration date accumulate in the disposition review queue without timely processing.
- **Root Cause:** Disposition reviewers are not assigned, not trained, or the volume exceeds review capacity.
- **Resolution:**
  1. Verify disposition reviewers are assigned to each retention label.
  2. Set up automated notifications for pending disposition reviews.
  3. Establish a regular disposition review schedule (weekly or monthly).
  4. For high-volume categories, consider extending retention rather than deleting to reduce review burden.

### Issue 5: Mobile Copilot Interactions Not Appearing in Audit Log (Unmanaged Device)

- **Symptoms:** A user reports using Copilot on a personal mobile device or unmanaged browser. The compliance team cannot find corresponding audit log entries or confirm the interaction is covered by retention policies.
- **Root Cause:** If the user accessed Copilot through an unmanaged mobile browser (e.g., mobile web browser accessing office.com rather than the official Microsoft 365 apps), the interaction may not be captured by the firm's retention policies. This is the same off-channel gap that has generated regulatory penalties in the SEC/CFTC enforcement actions.
- **Resolution:**
  1. **Immediate:** Search the Purview audit log for CopilotInteraction events from the user during the relevant time period. If none are found, the interaction may genuinely not have been captured.
  2. **Assess the gap:** Document the unmanaged access event, the search conducted, and the absence of captured audit events. This documentation supports the firm's remediation record.
  3. **Remediate access controls:** Verify that Conditional Access policies requiring managed devices or compliant apps are in place for Copilot surfaces. If the user bypassed these controls, investigate the policy gap.
  4. **User remediation:** Inform the user that Copilot may only be accessed through managed Microsoft 365 apps on enrolled or compliant devices, per firm policy. Document the notification.
  5. **Long-term:** Review and strengthen Conditional Access policies (see Control 2.3) to ensure unmanaged mobile browser access to Copilot is blocked.

### Issue 6: Off-Channel Risk Assessment for Copilot — Scope Determination

- **Symptoms:** The compliance team is unsure whether a particular Copilot access channel (e.g., Copilot via SharePoint mobile, Copilot via third-party integration) is covered by the firm's recordkeeping policies, or whether it constitutes an "off-channel" access risk analogous to the personal messaging app enforcement cases.
- **Root Cause:** Copilot is accessible through multiple channels (desktop apps, web browsers, mobile apps, third-party integrations) and the recordkeeping coverage of each channel is not always obvious. The off-channel enforcement context -- $2B+ in SEC/CFTC fines since 2021 -- elevates the stakes for any unresolved channel coverage question.
- **Resolution:**
  1. **Audit channel coverage:** For each Copilot access channel in use, map to a retention policy and verify coverage:
     - Outlook (desktop, web, mobile via official app): Exchange retention ✓
     - Teams (desktop, web, mobile via official app): Teams retention ✓
     - SharePoint/OneDrive (desktop, web): SharePoint retention ✓
     - Mobile browser (office.com, teams.microsoft.com in browser): Coverage may depend on session type -- investigate and test
     - Third-party integrations (Graph API, custom applications): Typically NOT covered by default -- requires explicit connector or export
  2. **Close coverage gaps:** For channels where coverage is uncertain, either: (a) block access to Copilot through that channel via Conditional Access, or (b) implement a data connector or retention solution for the channel.
  3. **Conduct periodic channel review:** As Microsoft adds new Copilot surfaces and access paths, review channel coverage quarterly and update the recordkeeping channel map.
  4. **Consult the off-channel enforcement record:** The SEC and CFTC enforcement orders for off-channel communications (2021-present) consistently hold that firms are responsible for all channels where business communications occur, regardless of whether the firm affirmatively enabled the channel. The same principle applies to Copilot access channels.

### Issue 7: Audit Trail Alternative Coverage — Audit Log Retention Insufficient

- **Symptoms:** The firm is using the audit-trail alternative path under Rule 17a-4(f)(2)(ii)(A), but the Purview audit log retention period is shorter than the record retention period required for the retained records (e.g., audit log retained for 1 year, but records have 6-year retention).
- **Root Cause:** The Microsoft 365 default audit log retention (90 days to 1 year depending on license) may not match the SEC 17a-4 retention period for the regulated records. The audit-trail alternative requires the audit trail to cover the full retention period.
- **Resolution:**
  1. Check current audit log retention: Navigate to Purview > Audit > Audit retention policies > review policies.
  2. Create an audit retention policy covering the required retention period:
     - Navigate to Purview > Audit > Audit retention policies > Create policy
     - Select the relevant record types (CopilotInteraction, SharePointFileOperation, ExchangeItem, etc.)
     - Set retention duration to match or exceed the 17a-4 retention period (6 years for financial records, 3 years for communications)
     - Note: 10-year audit retention requires Microsoft 365 E5 or Audit (Premium) license
  3. Verify the audit retention policy is in effect and confirm its distribution status.
  4. If the license does not support the required audit retention period, consider: (a) upgrading to E5 or Audit (Premium), or (b) switching to Option B (third-party WORM archival) as the primary 17a-4(f) compliance path.

## Diagnostic Steps

1. **Check label deployment:** `Get-ComplianceTag | Select Name, RetentionDuration, IsRecordLabel, Regulatory`
2. **Verify auto-apply policies:** `Get-RetentionCompliancePolicy | Where IsAutoApply -eq $true`
3. **Review Preservation Lock:** `Get-RetentionCompliancePolicy | Select Name, RestrictiveRetention`
4. **Check audit trail coverage:** Run Script 5 to search for record-related audit events
5. **Verify mobile access controls:** Check Conditional Access sign-in logs for Entra ID > Monitoring > Sign-in logs > filter by Copilot app and device platform
6. **Check disposition queue:** Navigate to Purview > Records management > Disposition
7. **Verify audit log retention:** Purview > Audit > Audit retention policies

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Records deleted before retention period expires | Legal + Compliance + Microsoft Support |
| Critical | Mobile Copilot interactions confirmed unretained (off-channel gap) | Legal + Chief Compliance Officer |
| High | Preservation Lock misconfiguration | Records management lead + Legal |
| High | Audit log retention insufficient for audit-trail alternative path | Records management lead + IT + Legal |
| Medium | Auto-apply classification accuracy below 80% | Compliance team for policy tuning |
| Medium | Mobile Copilot access from unmanaged device (single instance) | Compliance team + user remediation |
| Medium | Off-channel risk gap identified for Copilot access channel | Compliance team for channel closure or coverage implementation |
| Low | Disposition review backlog | Assign additional reviewers |

## Related Resources

- [Control 3.2: Data Retention Policies](../3.2/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
- [Control 2.3: Conditional Access Policies](../2.3/portal-walkthrough.md)
- [SEC Rule 17a-4 (Records to Be Preserved)](https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4)
- [Microsoft Purview audit retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)
- Back to [Control 3.11](../../../controls/pillar-3-compliance/3.11-record-keeping.md)
