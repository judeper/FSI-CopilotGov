# Control 1.4: Semantic Index Governance — Troubleshooting

Common issues and resolution steps for Semantic Index governance.

## Common Issues

### Issue 1: Semantic Index Not Processing Content

- **Symptoms:** Content recently added to SharePoint or OneDrive is not discoverable through Copilot even after several days, or the index status shows processing errors
- **Root Cause:** Semantic indexing and Copilot retrieval are not instantaneous, and the timing varies by workload and change type. Microsoft documents daily indexing for newly added eligible SharePoint documents, separate propagation for scope controls such as RCD, and different behavior for mailbox/user-context retrieval.
- **Resolution:**
  1. Check the Copilot readiness page for any index processing alerts
  2. Verify the content is in a supported format (Office documents, PDFs, text files)
  3. Confirm the SharePoint site remains searchable and is not intentionally limited by RCD or RSS
  4. If the problem persists after the documented service timeline, request a site re-index via PnP PowerShell (`Request-PnPReindexWeb`) or the SharePoint site settings UI and collect evidence before escalating

### Issue 2: Copilot Returning Content That Should Be Excluded

- **Symptoms:** Copilot responses reference content from sources that were supposed to be excluded from the semantic index
- **Root Cause:** The wrong control may have been used for the intended outcome. RCD excludes SharePoint content from Copilot discovery but does not remove it from the Microsoft 365 search index, while turning off site searchability removes the site from both Microsoft Search and semantic indexing. RSS, where still enabled, scopes retrieval differently from RCD.
- **Resolution:**
  1. Verify whether the intended control is RCD, RSS, or site searchability and confirm that the current setting matches the governance decision
  2. Check the change timeline and allow for documented propagation
  3. If the content must leave both Microsoft Search and semantic indexing, turn off site-level searchability rather than relying on RCD alone
  4. As an interim measure, use RSS only if it is already enabled in the tenant and the retirement plan is documented

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
- **Root Cause:** SharePoint discoverability controls do not replace workload-specific governance for Exchange, Teams, or other Microsoft Graph content. The Semantic Index, Microsoft Graph, and workload-native permissions are separate parts of the grounding path.
- **Resolution:**
  1. Verify SharePoint searchability, RCD/RSS state, and workload-specific controls independently
  2. Use Exchange, Teams, Purview, and information-barrier controls as the primary governance levers for non-SharePoint content
  3. Document which control governs each workload in the decision record
  4. Re-test with representative users to confirm that the issue is discovery scope rather than permissions or retention behavior

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
5. **Cross-reference controls:** Test SharePoint searchability, RCD/RSS state, and workload-specific controls independently

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
