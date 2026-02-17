# Control 1.10: Vendor Risk Management for Microsoft AI Services — Verification & Testing

Test cases and evidence collection for validating vendor risk management processes.

## Test Cases

### Test 1: Vendor Risk Assessment Completeness

- **Objective:** Verify the vendor risk assessment covers all required domains for FSI AI services
- **Steps:**
  1. Review the completed vendor risk questionnaire
  2. Verify all sections are completed: data security, privacy, resilience, governance, contractual
  3. Confirm risk ratings are assigned for each identified risk
  4. Verify governance committee has reviewed and approved the assessment
- **Expected Result:** Complete vendor risk assessment with all domains evaluated and approved
- **Evidence:** Signed vendor risk assessment document

### Test 2: Microsoft Compliance Documentation Currency

- **Objective:** Confirm referenced Microsoft compliance documents are current
- **Steps:**
  1. Verify SOC 2 Type II report is from the current or most recent audit period
  2. Confirm ISO 27001 certificate is not expired
  3. Check that the DPA references the current product terms
  4. Verify AI transparency documentation references current Copilot capabilities
- **Expected Result:** All compliance documentation is current and valid
- **Evidence:** Document inventory with validity dates

### Test 3: Ongoing Monitoring Process Validation

- **Objective:** Verify vendor monitoring processes are active and functioning
- **Steps:**
  1. Run PowerShell Script 2 to check for recent AI-related Message Center posts
  2. Verify the monitoring team has reviewed recent posts and taken appropriate action
  3. Confirm vendor risk register is updated with any new findings
  4. Verify the next scheduled reassessment is calendared
- **Expected Result:** Active monitoring with documented review of recent service changes
- **Evidence:** Monitoring log showing review dates and actions taken

### Test 4: Contractual Protection Verification

- **Objective:** Confirm contractual protections are in place for AI data processing
- **Steps:**
  1. Verify a current Data Processing Agreement is executed
  2. Confirm the agreement covers AI processing activities
  3. Review SLA terms for Copilot service availability
  4. Verify indemnification and liability provisions are adequate per legal counsel
- **Expected Result:** Contractual protections are current and cover AI-specific processing
- **Evidence:** Executed DPA and legal review memo

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Vendor risk assessment | PDF | Vendor risk management repository | 7 years |
| Microsoft compliance certificates | PDF | Compliance evidence repository | 7 years |
| Data Processing Agreement | PDF | Legal document repository | Contract term + 7 years |
| Monitoring review logs | CSV | Compliance evidence repository | 7 years |
| Governance committee approval | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| OCC Third-Party Risk Guidance | Third-party risk management | Formal vendor assessment supports compliance with OCC third-party risk requirements |
| FFIEC IT Examination Handbook | Vendor management | Documented vendor assessment helps meet FFIEC examination expectations |
| SEC Regulation S-P | Safeguards for service providers | Vendor risk review supports compliance with service provider oversight obligations |
| NIST AI RMF | GOVERN 5 — Third-party AI governance | Vendor risk assessment supports compliance with AI third-party governance |
