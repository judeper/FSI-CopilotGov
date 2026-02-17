# Control 1.4: Semantic Index Governance — Troubleshooting

Common issues and resolution steps for Semantic Index governance.

## Common Issues

### Issue 1: Semantic Index Not Processing Content

- **Symptoms:** Content recently added to SharePoint or OneDrive is not discoverable through Copilot even after several days, or the index status shows processing errors
- **Root Cause:** The Semantic Index requires time to process new content (typically 24-48 hours). Processing delays may occur during periods of high tenant activity or service-side throttling.
- **Resolution:**
  1. Check the Copilot readiness page for any index processing alerts
  2. Verify the content is in a supported format (Office documents, PDFs, text files)
  3. Confirm the site containing the content is not excluded from indexing
  4. If content remains unindexed after 72 hours, request a site re-index via `Request-SPOReIndex`

### Issue 2: Copilot Returning Content That Should Be Excluded

- **Symptoms:** Copilot responses reference content from sources that were supposed to be excluded from the semantic index
- **Root Cause:** Index exclusion settings may not have propagated fully, or the content was indexed before the exclusion was configured. Previously indexed content may remain in the index until it is purged.
- **Resolution:**
  1. Verify exclusion configuration is correctly set in Admin Center
  2. Check the timeline — if exclusion was recently configured, allow 48-72 hours for propagation
  3. For content indexed before exclusion, request a full re-crawl of the affected content source
  4. As an interim measure, use Restricted SharePoint Search (Control 1.3) to limit Copilot's scope

### Issue 3: Index Governance Settings Reset After Update

- **Symptoms:** Previously configured index governance settings revert to defaults after a service update or admin center change
- **Root Cause:** Microsoft 365 service updates may occasionally reset tenant-level preview settings. Admin center UI changes may also inadvertently modify related settings.
- **Resolution:**
  1. Document all governance settings in a configuration baseline document
  2. Implement weekly automated verification using PowerShell Script 1
  3. Set up alerts on configuration change audit events
  4. After any service update, immediately verify index governance settings

### Issue 4: Inconsistent Index Behavior Across Workloads

- **Symptoms:** Copilot returns content from Exchange or Teams that was expected to be excluded, while SharePoint exclusions work correctly
- **Root Cause:** Semantic Index governance controls may have different implementation timelines across workloads. SharePoint controls are typically the most mature, while Exchange and Teams controls may lag.
- **Resolution:**
  1. Verify governance settings for each workload independently
  2. Use workload-specific controls (e.g., Exchange retention policies, Teams data governance) as supplementary restrictions
  3. Document any workload-specific gaps in the governance decision record
  4. Monitor Microsoft 365 roadmap for updates to workload-specific index controls

### Issue 5: Performance Impact from Index Scope Changes

- **Symptoms:** After modifying index scope, users report slower Copilot response times or degraded search performance
- **Root Cause:** Significant index scope changes trigger re-processing that temporarily impacts query performance. Adding a large number of sites to the scope simultaneously can cause resource contention.
- **Resolution:**
  1. Make index scope changes incrementally rather than all at once
  2. Schedule major scope changes during off-peak hours
  3. Monitor service health metrics for 48 hours after scope changes
  4. If performance does not recover, contact Microsoft support

## Diagnostic Steps

1. **Check index health:** Review the Copilot readiness dashboard for index processing status
2. **Verify configuration:** Compare current settings against documented governance baseline
3. **Test with known content:** Search for content with a known location to confirm index behavior
4. **Review audit logs:** Check for recent admin changes to Copilot or search settings
5. **Cross-reference workloads:** Test index behavior across SharePoint, Exchange, and Teams independently

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Index processing delays under 72 hours | Monitor and retest |
| **Medium** | Governance settings found inconsistent with documented baseline | IT Operations for correction and investigation |
| **High** | Copilot surfacing content from excluded sources | Security Operations for immediate investigation |
| **Critical** | Index governance controls non-functional across workloads | CISO, Microsoft TAM, and governance committee |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Configuration reference
- [PowerShell Setup](powershell-setup.md) — Monitoring scripts
- [Verification & Testing](verification-testing.md) — Validation procedures
