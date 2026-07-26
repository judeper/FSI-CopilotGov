# Control 2.15: Network Security and Private Connectivity — Portal Walkthrough

Step-by-step portal configuration for implementing network security controls for M365 Copilot workloads, plus correct scoping of private connectivity (Azure Private Link) for adjacent Azure resources.

## Prerequisites

- Azure Network Administrator or Entra Global Admin role
- Azure subscription (only if configuring Private Link for adjacent Azure resources an internal Copilot Studio agent calls — not for M365 Copilot)
- Network architecture documentation
- Understanding of Microsoft 365 network connectivity requirements

## Steps

### Step 1: Review Microsoft 365 Network Connectivity

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Health > Network Connectivity

Review the network connectivity assessment for your organization. Verify:
- Network paths to Microsoft 365 endpoints are optimal
- No proxy or inspection devices are degrading Copilot performance
- DNS resolution is correctly configured for Microsoft 365 services

### Step 2: Scope Azure Private Link Correctly (Adjacent Azure Resources Only)

**Portal:** Azure Portal
**Path:** Azure Portal > Private Link Center > Private Endpoints

Azure Private Link does **not** apply to Microsoft 365 Copilot. Microsoft 365 (SharePoint Online, Exchange Online, Teams, and Copilot surfaces) is delivered as SaaS over the public internet, and Microsoft offers **no** customer-managed private endpoints for these services. Do not attempt to route M365 or Copilot traffic through Private Link — treat it as internet-facing SaaS and govern it with Conditional Access, Global Secure Access, and tenant restrictions (Steps 3–4).

Use Private Link **only** for *adjacent Azure resources* an internal Copilot Studio agent calls — for example, an Azure-hosted API, Azure SQL, or Storage account behind the agent:
- Create a Private Endpoint on the Azure resource itself (not on M365)
- Configure Azure Private DNS so the agent's Azure backend resolves privately
- Verify the agent's backend connectivity through the private endpoint
- Confirm this protects the adjacent Azure resource — it does not create a private path to the M365 Copilot service

### Step 3: Review Firewall and Proxy Configuration

**Portal:** Network management console (organization-specific)

Review firewall and proxy rules for Microsoft 365 Copilot endpoints:
- Allow required Copilot endpoints per Microsoft's published endpoint list
- Configure SSL inspection exceptions for Microsoft 365 traffic (if applicable)
- Verify no content inspection is degrading Copilot response quality
- Document all network path configurations for compliance

### Step 4: Configure Network Location in Conditional Access

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Protection > Conditional Access > Named Locations

Define trusted network locations for Conditional Access policies:
- Corporate network IP ranges
- VPN exit point IP addresses
- Branch office IP ranges
- Configure country-based blocking if required (see Control 2.7)

### Step 5: Document Network Security Architecture

Create a network security document for Copilot connectivity:
- Network topology for Microsoft 365 access
- Firewall rules and exceptions for Copilot endpoints
- Private Link configuration for adjacent Azure resources (if applicable — not for M365 Copilot itself)
- Monitoring and alerting for network security events
- Performance baselines for Copilot connectivity

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Verify Microsoft 365 endpoint access; configure trusted locations in Conditional Access |
| **Recommended** | Optimize network paths; SSL inspection exceptions for M365; network monitoring for Copilot traffic |
| **Regulated** | Global Secure Access (Entra Internet Access) + universal tenant restrictions for Copilot; Private Link only for adjacent Azure resources an internal agent calls; network segmentation for Copilot traffic; continuous network monitoring with SIEM integration |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for network verification automation
- See [Verification & Testing](verification-testing.md) to validate network controls
- Review Control 2.3 for Conditional Access integration with network controls
- Back to [Control 2.15](../../../controls/pillar-2-security/2.15-network-security.md)
