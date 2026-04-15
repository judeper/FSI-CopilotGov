# Control 2.15: Network Security and Private Connectivity — Verification & Testing

Test cases and evidence collection for validating network security controls.

## Test Cases

### Test 1: Endpoint Connectivity Verification

- **Objective:** Confirm all Microsoft 365 Copilot endpoints are reachable from the corporate network
- **Steps:**
  1. Run PowerShell Script 1 from a corporate network workstation
  2. Verify all endpoints report "Reachable: True"
  3. Document latency values and compare against performance baselines
  4. Test from multiple network locations (headquarters, branches, VPN)
- **Expected Result:** All Copilot endpoints reachable with acceptable latency (<100ms)
- **Evidence:** Connectivity test results from multiple locations

### Test 2: Private Link Connectivity (if deployed)

- **Objective:** Verify Private Link endpoints are functioning correctly
- **Steps:**
  1. Run Script 2 to check Private Link status
  2. Resolve SharePoint URLs and verify they resolve to private IP addresses
  3. Test Copilot functionality through the Private Link connection
  4. Verify public endpoint access is blocked (if configured)
- **Expected Result:** Traffic routes through Private Link with correct DNS resolution
- **Evidence:** DNS resolution results and connectivity test

### Test 3: Firewall Rule Verification

- **Objective:** Confirm firewall rules allow required Copilot traffic
- **Steps:**
  1. Review firewall rules against Microsoft's published endpoint requirements
  2. Verify no rules block required Copilot service endpoints
  3. Test Copilot functionality from behind the firewall
  4. Verify SSL inspection exceptions are applied to M365 traffic
- **Expected Result:** All required traffic permitted through firewall
- **Evidence:** Firewall rule audit and functional test results

### Test 4: Network-Based Conditional Access

- **Objective:** Verify Conditional Access enforces network location restrictions
- **Steps:**
  1. Access Copilot from a trusted network location — verify access granted
  2. Access Copilot from an untrusted network — verify additional controls apply
  3. Verify location-based policies are logged in sign-in logs
- **Expected Result:** Network-based Conditional Access enforced correctly
- **Evidence:** Sign-in logs showing location-based policy evaluation

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Endpoint connectivity results | CSV | Compliance evidence repository | 7 years |
| Private Link configuration | PDF/CSV | Compliance evidence repository | 7 years |
| Firewall rule documentation | PDF | Compliance evidence repository | 7 years |
| Network architecture diagram | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FFIEC IT Handbook | Network security | Network controls support compliance with FFIEC network security requirements |
| PCI DSS Req 1 | Network segmentation | Network security controls help meet network segmentation requirements |
| NIST CSF | PR.AC-5 Network integrity | Private connectivity supports compliance with network integrity protection |
| SOX Section 404 | Network access controls | Network security documents internal controls for technology access |
- Back to [Control 2.15](../../../controls/pillar-2-security/2.15-network-security.md)
