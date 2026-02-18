# Control 2.9: Defender for Cloud Apps — Copilot Session Controls — Troubleshooting

Common issues and resolution steps for Defender for Cloud Apps session controls.

## Common Issues

### Issue 1: Copilot Activities Not Appearing in Activity Log

- **Symptoms:** Copilot interactions are not visible in the Defender for Cloud Apps activity log despite session policies being configured
- **Root Cause:** Conditional Access App Control may not be fully configured for Microsoft 365, or the session routing may not be active for the specific Copilot workload.
- **Resolution:**
  1. Verify Conditional Access App Control is enabled for Microsoft 365 in Defender settings
  2. Check the Conditional Access policy routes traffic through Defender for Cloud Apps
  3. Verify the user's session was proxied (check for the MCAS proxy indicator in the browser)
  4. Allow 24 hours for activity data to appear in the log

### Issue 2: Session Control Causing Performance Issues

- **Symptoms:** Users report slower Copilot responses or Office application performance degradation when session controls are active
- **Root Cause:** Proxying sessions through Defender for Cloud Apps adds latency. Content inspection adds additional processing time.
- **Resolution:**
  1. Review session policy scope — limit content inspection to specific conditions rather than all traffic
  2. Optimize content inspection rules to target only high-risk activities
  3. Consider monitoring-only policies (no blocking) for general use and blocking policies for specific conditions
  4. Work with Microsoft support to optimize proxy routing if latency is significant

### Issue 3: False Positive Alerts Overwhelming Security Team

- **Symptoms:** High volume of alerts for normal Copilot usage patterns, creating alert fatigue
- **Root Cause:** Alert thresholds may be too sensitive, or alert conditions may match normal business activity.
- **Resolution:**
  1. Review alert patterns and identify the most common false positive types
  2. Adjust alert thresholds to reduce noise (e.g., increase the activity count threshold)
  3. Create suppression rules for known-good activity patterns
  4. Use alert aggregation to group related alerts into single incidents
  5. Implement a tiered alerting approach (informational vs. actionable)

### Issue 4: Content Inspection Missing Sensitive Data

- **Symptoms:** Known sensitive data passes through Copilot sessions without triggering content inspection alerts
- **Root Cause:** Content inspection patterns may not match the specific data format, or inspection may not be configured for the specific Copilot interaction type.
- **Resolution:**
  1. Review content inspection sensitive information type definitions
  2. Test with known data patterns to verify detection capability
  3. Verify the session policy applies to the specific interaction type where data was missed
  4. Add custom inspection rules for organization-specific data patterns

### Issue 5: Agent Threat Detection Alerts Not Appearing

- **Symptoms:** Copilot agents are deployed but no agent-related alerts appear in Defender XDR; the Incidents & alerts view shows no agent incidents despite agent activity
- **Root Cause:** Agent threat detection may require specific licensing (Defender for Office 365 P2 or Microsoft 365 Defender) and may need to be explicitly enabled for agent workloads. Agent coverage was added in September 2025 and may require feature updates in older tenants.
- **Resolution:**
  1. Verify the tenant has the required Defender XDR license tier for agent threat detection (included in M365 E5 Security or Defender for Office 365 P2)
  2. Navigate to Defender portal > Settings > Microsoft Defender XDR and confirm unified XDR is enabled
  3. Check that the agents are registered in Agent Registry (MAC > Copilot > Agents) — unregistered agents may not have threat detection coverage
  4. Verify no filter is hiding agent incidents: in Incidents & alerts, clear all filters and search for recent agent-related events
  5. Allow 24-48 hours after enabling detection — initial alert generation may be delayed
  6. If alerts still do not appear after enabling: open a Microsoft support ticket referencing Defender XDR agent threat detection

### Issue 6: Generative AI App Catalog Not Showing Discovered Apps

- **Symptoms:** The Cloud app catalog Generative AI filter shows apps but no "discovered" usage data, or the catalog shows fewer apps than expected
- **Root Cause:** Discovery data requires traffic analysis either through Microsoft Defender for Endpoint integration or manual log upload. Without endpoint agents or log upload configured, only the catalog (not discovery) will be visible.
- **Resolution:**
  1. Navigate to Defender portal > Cloud Apps > Settings > Cloud Discovery to check discovery configuration
  2. If Microsoft Defender for Endpoint is deployed: verify the "Defender for Endpoint integration" toggle is enabled in Cloud Discovery settings — this enables automatic traffic analysis for discovery
  3. If Defender for Endpoint is not deployed: configure manual log upload from proxy or firewall logs to enable discovery
  4. Allow 24-48 hours after enabling discovery for initial data to appear
  5. Verify the correct data source is connected: Defender portal > Cloud Apps > Cloud Discovery > Data sources

## Diagnostic Steps

1. **Verify proxy routing:** Check browser URL for MCAS proxy indicators during Copilot use
2. **Check policy status:** Defender > Policies > verify all session policies are "Enabled"
3. **Review activity log:** Search for any Copilot-related activities in the last 24 hours
4. **Test detection:** Use a test document with known sensitive data patterns
5. **Check CA integration:** Verify the Conditional Access policy references Defender for Cloud Apps

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor logging gaps | Security Operations |
| **Medium** | Session controls causing user-impacting latency | Security Operations and Microsoft support |
| **High** | Content inspection failing to detect sensitive data | Security Operations and Information Protection team |
| **Critical** | Session controls non-functional — no monitoring on Copilot | CISO and Security Operations immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Session control configuration
- [PowerShell Setup](powershell-setup.md) — Monitoring scripts
- [Verification & Testing](verification-testing.md) — Session control validation
