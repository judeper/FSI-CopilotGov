# Control 2.15: Network Security and Private Connectivity — Portal Walkthrough

Step-by-step portal configuration for implementing network security controls and private connectivity for M365 Copilot workloads.

## Prerequisites

- Azure Network Administrator or Global Administrator role
- Azure subscription for Private Link configuration
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

### Step 2: Configure Azure Private Link for SharePoint (Optional)

**Portal:** Azure Portal
**Path:** Azure Portal > Private Link Center > Private Endpoints > Create

For organizations requiring private network connectivity to Microsoft 365 content:
- Create Private Endpoints for SharePoint Online
- Configure DNS to resolve SharePoint URLs to private IP addresses
- Verify connectivity from corporate network through private endpoints
- Test Copilot functionality over the private connection

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
- Private Link configuration (if applicable)
- Monitoring and alerting for network security events
- Performance baselines for Copilot connectivity

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Verify Microsoft 365 endpoint access; configure trusted locations in Conditional Access |
| **Recommended** | Optimize network paths; SSL inspection exceptions for M365; network monitoring for Copilot traffic |
| **Regulated** | Azure Private Link for SharePoint; network segmentation for Copilot traffic; continuous network monitoring with SIEM integration |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for network verification automation
- See [Verification & Testing](verification-testing.md) to validate network controls
- Review Control 2.3 for Conditional Access integration with network controls
