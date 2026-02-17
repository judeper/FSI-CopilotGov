# Control 3.2: Data Retention Policies for Copilot Interactions — Troubleshooting

Common issues and resolution steps for Copilot data retention policy configuration and operation.

## Common Issues

### Issue 1: Retention Policy Distribution Fails

- **Symptoms:** Policy status shows `DistributionPending` or `DistributionFailed` in Purview portal or PowerShell output.
- **Root Cause:** Location scoping conflicts with existing policies, or service provisioning delays.
- **Resolution:**
  1. Check policy status: `Get-RetentionCompliancePolicy -Identity "FSI-Copilot-Interaction-Retention" | Select DistributionStatus`
  2. If `DistributionFailed`, review error details in the Purview portal under the policy's status page.
  3. Remove and re-add any conflicting locations.
  4. Allow up to 24 hours for distribution to complete after changes.

### Issue 2: Copilot Interaction Location Not Available

- **Symptoms:** The "Copilot for Microsoft 365 interactions" location does not appear when creating a retention policy.
- **Root Cause:** The tenant may not have the required Copilot licenses provisioned, or the location type is not yet available in the tenant region.
- **Resolution:**
  1. Verify at least one Copilot license is assigned in the tenant.
  2. Check the Microsoft 365 roadmap for regional availability of Copilot retention locations.
  3. As an interim measure, configure retention on Exchange, SharePoint, and OneDrive locations to cover Copilot-generated content.

### Issue 3: Retention Labels Not Applying to Copilot Content

- **Symptoms:** Auto-apply retention labels are not being applied to documents created with Copilot assistance.
- **Root Cause:** Auto-apply label policies may not detect Copilot-generated content characteristics, or the policy indexing is incomplete.
- **Resolution:**
  1. Verify the label policy is published to the correct locations.
  2. Confirm the auto-apply condition matches the content correctly (keyword, trainable classifier, or sensitive info type).
  3. Allow up to 7 days for auto-apply policies to fully index and apply.
  4. Consider using manual labeling or default labels as an interim approach.

### Issue 4: Conflict Between Retention and Deletion Policies

- **Symptoms:** Content is being deleted before the expected retention period ends, or content is not being deleted after the retention period.
- **Root Cause:** Multiple retention policies with conflicting actions may be applied to the same content. Retention always wins over deletion per Microsoft's conflict resolution.
- **Resolution:**
  1. Review all policies affecting the same locations: `Get-RetentionCompliancePolicy | Format-List Name, *Location*`
  2. Identify overlapping policies and review their retention rules.
  3. Follow the principle that the longest retention period and "retain" action take precedence.
  4. Consolidate overlapping policies where possible to reduce complexity.

## Diagnostic Steps

1. **Check policy sync status:** `Get-RetentionCompliancePolicy | Select Name, Enabled, DistributionStatus`
2. **Review rule configuration:** `Get-RetentionComplianceRule | Select PolicyName, RetentionDuration, RetentionComplianceAction`
3. **Verify Copilot licensing:** Confirm M365 Copilot licenses in the Microsoft 365 Admin Center.
4. **Test content search:** Use Purview Content Search to verify Copilot content is indexed and discoverable.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Retention policies failing to retain required records | Compliance team + Microsoft Premier Support |
| High | Policy distribution failures across tenant | Internal IT + Microsoft Support |
| Medium | Label application delays | Monitor and re-evaluate after 7 days |
| Low | Minor policy configuration adjustments | Internal compliance team |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 3.3: eDiscovery for Copilot Content](../3.3/portal-walkthrough.md)
