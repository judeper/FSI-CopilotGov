# Control 2.15: Network Security and Private Connectivity — Troubleshooting

Common issues and resolution steps for network security controls.

## Common Issues

### Issue 1: Copilot Slow or Unresponsive

- **Symptoms:** Copilot responses are significantly delayed or time out, particularly from specific network locations
- **Root Cause:** Network latency, proxy interference, SSL inspection overhead, or firewall blocking of required endpoints.
- **Resolution:**
  1. Run Script 1 to test endpoint connectivity and latency
  2. Compare latency against baselines — anything above 200ms may impact experience
  3. Check if a proxy server is inspecting Microsoft 365 traffic (recommended: bypass proxy for M365)
  4. Verify SSL inspection exceptions are configured for Microsoft 365 endpoints
  5. Review firewall logs for blocked connections to Copilot service endpoints

### Issue 2: Private Link DNS Resolution Failures

- **Symptoms:** SharePoint or other M365 services resolve to public IP addresses instead of private endpoints, or DNS resolution fails entirely
- **Root Cause:** Private DNS zones may not be correctly configured, or DNS forwarding rules may not cover all required domains.
- **Resolution:**
  1. Verify Azure Private DNS zones are created for all required M365 domains
  2. Check DNS forwarding configuration on corporate DNS servers
  3. Test DNS resolution using `nslookup <tenant>.sharepoint.com` from within the corporate network
  4. Verify the Private DNS zone is linked to the correct virtual network

### Issue 3: Firewall Blocking Required Copilot Endpoints

- **Symptoms:** Copilot features fail or are unavailable; endpoint connectivity test shows failures
- **Root Cause:** Firewall rules may not include recently added Microsoft 365 endpoints, or endpoint categories may have changed.
- **Resolution:**
  1. Download the current Microsoft 365 endpoint list from Microsoft's web service
  2. Compare against current firewall rules to identify missing entries
  3. Add missing endpoints and categories to the firewall allowlist
  4. Subscribe to endpoint change notifications to stay current

### Issue 4: SSL Inspection Degrading Copilot Performance

- **Symptoms:** Copilot works but is noticeably slower than expected, or certificate errors appear intermittently
- **Root Cause:** SSL/TLS inspection devices add latency and may interfere with certificate pinning used by Microsoft 365 services.
- **Resolution:**
  1. Configure SSL inspection bypass for all Microsoft 365 endpoint categories
  2. Verify the bypass is effective by checking the certificate presented by M365 endpoints (should be Microsoft-issued, not the proxy's CA)
  3. Test Copilot performance before and after bypass to quantify the improvement
  4. Document the bypass in the network security architecture

### Issue 5: Branch Office Connectivity Issues

- **Symptoms:** Copilot performance varies significantly between headquarters and branch offices
- **Root Cause:** Branch offices may route M365 traffic through a central hub (backhauling) instead of using local internet egress, adding latency.
- **Resolution:**
  1. Evaluate local internet breakout for Microsoft 365 traffic at branch offices
  2. Implement SD-WAN policies to route M365 traffic directly from branches
  3. Configure split-tunnel VPN for remote workers to avoid backhauling M365 traffic
  4. Monitor connectivity from each branch using Script 1

## Diagnostic Steps

1. **Test connectivity:** Run Script 1 from the affected network location
2. **Check DNS resolution:** Verify M365 domains resolve correctly
3. **Review firewall logs:** Check for blocked connections to M365 endpoints
4. **Test without proxy:** Temporarily bypass proxy to isolate the issue
5. **Compare locations:** Test from multiple network locations to identify location-specific issues

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor latency variations between locations | Network Operations |
| **Medium** | Endpoint connectivity failures from specific locations | Network Operations and ISP |
| **High** | Private Link non-functional | Azure team and Network Operations |
| **Critical** | All Copilot endpoints unreachable | Network Operations and Microsoft support immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Network configuration
- [PowerShell Setup](powershell-setup.md) — Connectivity scripts
- [Verification & Testing](verification-testing.md) — Network validation
- Back to [Control 2.15](../../../controls/pillar-2-security/2.15-network-security.md)
