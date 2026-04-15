# Control 3.5: FINRA Rule 2210 Compliance for Copilot-Drafted Communications — Verification & Testing

Test cases and evidence collection to validate that Copilot-drafted communications are monitored for FINRA Rule 2210 compliance.

## Test Cases

### Test 1: Prohibited Language Detection

- **Objective:** Verify that Copilot-drafted communications containing prohibited language are flagged
- **Steps:**
  1. Using a test account, ask Copilot to draft an email containing "guaranteed returns" or "risk-free investment".
  2. Send the email to a monitored test recipient.
  3. Wait up to 24 hours for policy processing.
  4. Check the Communication compliance review queue for the flagged item.
- **Expected Result:** The email is flagged with a FINRA 2210 policy match identifying the prohibited language.
- **Evidence:** Screenshot of the flagged item in the review queue with highlighted prohibited language.

### Test 2: Retail Communication Classification

- **Objective:** Confirm Copilot-assisted communications are correctly categorized by FINRA communication type
- **Steps:**
  1. Draft and send test communications to varying recipient counts (fewer than 25 and more than 25).
  2. Verify that communications to more than 25 retail recipients are classified as "Retail Communication".
  3. Verify that communications to fewer than 25 recipients are classified as "Correspondence".
- **Expected Result:** Communications are categorized correctly based on recipient count and type.
- **Evidence:** Review queue entries showing correct FINRA category classification.

### Test 3: Pre-Send Review Enforcement

- **Objective:** Validate that high-risk Copilot-drafted communications require supervisory approval before delivery
- **Steps:**
  1. Configure a test policy with pre-send review enabled for retail communications.
  2. Draft a retail communication using Copilot that contains flagged content.
  3. Verify the communication is held for supervisory review before delivery.
  4. Approve or reject the communication and verify the action is logged.
- **Expected Result:** Flagged retail communications are held pending supervisory review and approval.
- **Evidence:** Audit log showing the hold, review, and approval/rejection actions.

### Test 4: False Positive Rate Assessment

- **Objective:** Measure the false positive rate of FINRA 2210 detection rules
- **Steps:**
  1. Prepare a test set of 20 communications — 10 with genuine FINRA 2210 issues and 10 compliant.
  2. Route all through the communication compliance policy.
  3. Record which items were flagged and which were not.
  4. Calculate the false positive rate and false negative rate.
- **Expected Result:** False positive rate below 20% and false negative rate below 10% for critical violations.
- **Evidence:** Test matrix with detection results, precision, and recall calculations.

### Test 5: AI Washing Detection (FINRA 2210(d)(1)(A) / SEC v. Delphia Precedent)

- **Objective:** Verify that Communication Compliance policies catch promissory AI capability claims in Copilot-drafted communications
- **Regulatory basis:** FINRA Rule 2210(d)(1)(A) prohibits material misstatements; the SEC v. Delphia Inc. and Global Predictions Inc. enforcement action (March 2024) established that overstating AI capabilities violates the Investment Advisers Act Section 206 antifraud provisions
- **Steps:**
  1. Using a test account, ask Copilot to draft a client newsletter section containing phrases such as: "Our AI-powered platform guarantees superior returns" or "Our AI algorithms eliminate investment risk."
  2. Send the draft to a monitored test recipient.
  3. Wait up to 24 hours for policy processing.
  4. Verify the communication is flagged in the review queue with the AI washing keyword match identified.
  5. Confirm the reviewer can see which specific language triggered the match.
- **Expected Result:** The communication is flagged for containing unsubstantiated AI capability claims. The match correctly identifies the triggering language (e.g., "guarantees superior returns", "eliminate investment risk").
- **Evidence:** Screenshot of the flagged item in the review queue; keyword match detail showing the specific AI washing language detected.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Policy match examples | Purview review queue | Redacted screenshots | Per retention policy |
| Detection accuracy metrics | Test results | Spreadsheet | With control documentation |
| Supervisory review logs | Audit log | CSV export | 7 years |
| Policy configuration | Purview portal | Screenshot | With control documentation |
| AI washing detection results | Test 5 results | Redacted screenshots | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 2210(b) | Content standards for fair and balanced communications | Supports detection of misleading or promissory language in AI-drafted content |
| FINRA 2210(c) | Supervisory review and filing requirements | Helps meet pre-use approval requirements for retail communications |
| FINRA 2210(d) | Institutional communication standards | Supports categorization and appropriate review levels |
| FINRA 2210(d)(1)(A) | Prohibition on misleading statements, including about AI capabilities | AI washing keyword detection catches unsubstantiated capability claims |
| Investment Advisers Act Section 206 | Antifraud provisions — no false or misleading statements about AI | Detection policies aligned to SEC v. Delphia enforcement precedent |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for detection tuning
- Proceed to [Control 3.6](../3.6/portal-walkthrough.md) for supervision and oversight
- Back to [Control 3.5](../../../controls/pillar-3-compliance/3.5-finra-2210-compliance.md)
