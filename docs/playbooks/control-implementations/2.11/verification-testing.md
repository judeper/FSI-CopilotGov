# Control 2.11: Copilot Pages Security and Sharing Controls — Verification & Testing

Test cases and evidence collection for validating Copilot Pages security.

## Test Cases

### Test 1: Sharing Restriction Enforcement

- **Objective:** Confirm Pages sharing is restricted to "Specific people" and external sharing is blocked
- **Steps:**
  1. Create a Copilot Page through a Copilot interaction
  2. Attempt to share the Page using "Anyone with the link" — verify it is blocked
  3. Attempt to share with an external user — verify it is blocked
  4. Share with an internal specific user — verify it succeeds
- **Expected Result:** Only "Specific people" internal sharing is permitted
- **Evidence:** Screenshots of sharing attempts and their outcomes

### Test 2: Sensitivity Label Application

- **Objective:** Verify sensitivity labels are applied to Copilot Pages
- **Steps:**
  1. Create a Copilot Page from a source document with a "Confidential" label
  2. Check the sensitivity label on the resulting Page
  3. Verify label inheritance is working
- **Expected Result:** Pages inherit sensitivity labels from source content
- **Evidence:** Page properties showing applied sensitivity label

### Test 3: Retention Policy Coverage

- **Objective:** Confirm retention policies apply to Copilot Pages
- **Steps:**
  1. Verify the retention policy scope includes Copilot Pages storage
  2. Create a test Page and verify it is subject to retention
  3. Attempt to delete a Page under retention hold — verify it is preserved
- **Expected Result:** Retention policies apply to Pages content
- **Evidence:** Retention policy configuration and preservation test results

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Sharing configuration | Screenshot | Compliance evidence repository | 7 years |
| Sharing test results | PDF | Compliance evidence repository | 7 years |
| Label application verification | Screenshot | Compliance evidence repository | 7 years |
| Retention coverage confirmation | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Communication supervision | Pages sharing controls support compliance with AI-generated content oversight |
| SEC Rule 17a-4 | Records retention | Retention on Pages helps meet records preservation requirements |
| GLBA Safeguards Rule | Information sharing controls | Sharing restrictions help prevent unauthorized distribution of AI-generated content |
