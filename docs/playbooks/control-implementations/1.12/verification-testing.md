# Control 1.12: Training and Awareness Program — Verification & Testing

Test cases and evidence collection for validating the training and awareness program.

## Test Cases

### Test 1: Training Content Completeness

- **Objective:** Verify training content covers all required governance topics
- **Steps:**
  1. Review all training module content against the governance requirements checklist
  2. Verify modules cover: acceptable use, data governance, sensitive data handling, reporting obligations
  3. Confirm FSI-specific content addresses supervisory requirements and regulatory context
  4. Check that content is current with latest Copilot features and governance policies
- **Expected Result:** Training content covers all required governance topics
- **Evidence:** Content review checklist with sign-off from compliance team

### Test 2: Training Completion Rates

- **Objective:** Verify training completion meets target thresholds before each deployment wave
- **Steps:**
  1. Run PowerShell Script 1 to generate compliance report
  2. Verify completion rate exceeds 95% for the current deployment wave
  3. Identify any departments below the threshold
  4. Confirm non-compliant users have not yet been granted Copilot access
- **Expected Result:** 95% or higher completion rate for active deployment waves
- **Evidence:** Training compliance report with department breakdown

### Test 3: Knowledge Retention Verification

- **Objective:** Validate that training effectively transfers governance knowledge
- **Steps:**
  1. Administer a brief post-training assessment to a sample of 20 users
  2. Include questions on acceptable use, data governance, and reporting procedures
  3. Verify average score exceeds 80%
  4. Identify common knowledge gaps for targeted reinforcement
- **Expected Result:** Average assessment score of 80% or higher
- **Evidence:** Assessment results and analysis

### Test 4: Awareness Communication Delivery

- **Objective:** Confirm ongoing awareness communications are delivered and read
- **Steps:**
  1. Review the awareness communication calendar for the past quarter
  2. Verify all planned communications were sent on schedule
  3. Check email open rates or Teams message engagement metrics
  4. Survey a sample of users to verify they recall recent awareness content
- **Expected Result:** All planned communications delivered; engagement rate above 50%
- **Evidence:** Communication delivery records and engagement metrics

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Training content review checklist | PDF | Compliance evidence repository | 7 years |
| Training completion reports | CSV | Compliance evidence repository | 7 years |
| Post-training assessment results | PDF | Compliance evidence repository | 7 years |
| Communication delivery records | PDF/CSV | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory systems and WSPs | Copilot governance training supports compliance with supervisory training obligations |
| SEC Regulation S-P | Employee awareness | Security awareness training helps meet employee awareness requirements |
| GLBA §501(b) | Employee training | Data governance training supports compliance with safeguards training requirements |
| NIST AI RMF | GOVERN 4.2 — AI training | AI-specific training supports compliance with AI governance training requirements |
- Back to [Control 1.12](../../../controls/pillar-1-readiness/1.12-training-awareness.md)
