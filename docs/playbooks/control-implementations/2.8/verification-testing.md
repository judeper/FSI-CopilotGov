# Control 2.8: Encryption (Data in Transit and at Rest) — Verification & Testing

Test cases and evidence collection for validating encryption controls.

## Test Cases

### Test 1: Platform Encryption Verification

- **Objective:** Confirm Microsoft 365 platform encryption is active for all Copilot data
- **Steps:**
  1. Review Microsoft's service encryption documentation in the Service Trust Portal
  2. Verify BitLocker encryption status is referenced in the SOC 2 report
  3. Confirm service-level encryption keys are managed per Microsoft's documented process
- **Expected Result:** Platform encryption is active per Microsoft's documentation and audit reports
- **Evidence:** SOC 2 report excerpt and Service Trust Portal documentation

### Test 2: TLS Enforcement

- **Objective:** Verify TLS 1.2 or higher is enforced for all data in transit
- **Steps:**
  1. Run PowerShell Script 1 to check TLS connector settings
  2. Use a TLS testing tool to verify the TLS version on Microsoft 365 endpoints
  3. Confirm no connectors allow TLS below 1.2
- **Expected Result:** TLS 1.2 or higher enforced on all connections
- **Evidence:** TLS configuration export and test results

### Test 3: Customer Key Functionality (if deployed)

- **Objective:** Verify Customer Key encryption is operational
- **Steps:**
  1. Run PowerShell Script 2 to check DEP status
  2. Verify key vault accessibility for both key URIs
  3. Confirm the DEP is in "Active" state
  4. Test key availability by verifying access to a Customer Key-encrypted mailbox
- **Expected Result:** Customer Key DEP active with both keys accessible
- **Evidence:** DEP status report and key vault health check

### Test 4: Sensitivity Label Encryption with Copilot

- **Objective:** Verify Copilot correctly handles encrypted labeled content
- **Steps:**
  1. Create a document with an encryption-enabled sensitivity label
  2. As an authorized user, ask Copilot to summarize the encrypted document
  3. Verify Copilot can access and process the encrypted content
  4. As an unauthorized user, verify Copilot cannot access the document
- **Expected Result:** Copilot respects encryption access controls
- **Evidence:** Test results from authorized and unauthorized user perspectives

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| SOC 2 encryption reference | PDF | Compliance evidence repository | 7 years |
| TLS configuration export | CSV | Compliance evidence repository | 7 years |
| Customer Key status report | JSON | Compliance evidence repository | 7 years |
| Encryption label test results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| GLBA §501(b) | Encryption of customer data | Platform encryption supports compliance with data protection requirements |
| PCI DSS Req 4 | Encrypt transmission of cardholder data | TLS enforcement helps meet transmission encryption requirements |
| NIST SP 800-171 | Encryption at rest and in transit | Microsoft 365 encryption supports compliance with NIST encryption standards |
| FFIEC Handbook | Cryptographic controls | Encryption controls support compliance with FFIEC cryptographic requirements |
- Back to [Control 2.8](../../../controls/pillar-2-security/2.8-encryption.md)
