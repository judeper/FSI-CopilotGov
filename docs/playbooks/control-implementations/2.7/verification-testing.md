# Control 2.7: Data Residency and Cross-Border Data Flow — Verification & Testing

Test cases and evidence collection for validating data residency controls.

## Test Cases

### Test 1: Tenant Data Location Verification

- **Objective:** Confirm tenant data is stored in the expected geography
- **Steps:**
  1. Navigate to Admin Center > Settings > Org Settings > Data Location
  2. Document the data location for Exchange, SharePoint, and Teams
  3. Verify locations match the organization's data residency requirements
  4. Run PowerShell Script 1 to generate the automated report
- **Expected Result:** Data locations match regulatory requirements
- **Evidence:** Admin Center screenshot and PowerShell report

### Test 2: Copilot Processing Geography Confirmation

- **Objective:** Verify Copilot processes data within the expected geography
- **Steps:**
  1. Review Microsoft documentation on Copilot data processing locations
  2. Verify the tenant configuration for Copilot data processing
  3. Confirm processing location meets data residency obligations
  4. Document any exceptions or cross-border processing scenarios
- **Expected Result:** Copilot processing occurs within the required geography
- **Evidence:** Configuration documentation and Microsoft confirmation

### Test 3: Cross-Border Access Monitoring

- **Objective:** Verify cross-border access patterns are detected and documented
- **Steps:**
  1. Run PowerShell Script 3 to detect cross-border sign-ins
  2. Review any cross-border access events for compliance
  3. Verify legitimate cross-border access has legal basis documented
  4. Flag any unauthorized cross-border access for investigation
- **Expected Result:** All cross-border access is documented and authorized
- **Evidence:** Cross-border access report with authorization documentation

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Data location verification | Screenshot/PDF | Compliance evidence repository | 7 years |
| Copilot processing location | PDF | Compliance evidence repository | 7 years |
| Cross-border access reports | CSV | Compliance evidence repository | 7 years |
| Legal basis documentation | PDF | Legal document repository | Contract term + 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| GDPR Art. 44-49 | Cross-border transfer restrictions | Data residency controls support compliance with transfer requirements |
| State privacy laws | Data localization requirements | Residency verification helps meet state-level data localization rules |
| 12 CFR part 30, appendix D (OCC Heightened Standards) | Third-party data management | Understanding data locations supports compliance with third-party data requirements |
| NIST CSF | PR.DS-2 Data in transit protection | Residency controls complement data-in-transit protections |
- Back to [Control 2.7](../../../controls/pillar-2-security/2.7-data-residency.md)
