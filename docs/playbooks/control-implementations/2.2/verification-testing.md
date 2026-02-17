# Control 2.2: Sensitivity Labels and Copilot Content Classification — Verification & Testing

Test cases and evidence collection for validating sensitivity label enforcement with Copilot.

## Test Cases

### Test 1: Label Inheritance from Source Documents

- **Objective:** Verify Copilot-generated content inherits the appropriate sensitivity label from source documents
- **Steps:**
  1. Create a test document labeled "Confidential" in SharePoint
  2. Use Copilot to create a summary of the Confidential document
  3. Check the sensitivity label on the Copilot-generated summary
  4. Verify it inherits the "Confidential" label (or higher)
- **Expected Result:** Generated content inherits the source document's sensitivity label
- **Evidence:** Screenshots showing source label and generated content label

### Test 2: Default Label Application

- **Objective:** Confirm default labels are applied to new Copilot-created content
- **Steps:**
  1. Use Copilot to draft a new document from scratch (no source documents)
  2. Check the sensitivity label on the new document
  3. Verify the default label ("General" or configured default) is applied
  4. Repeat across Word, Excel, and PowerPoint
- **Expected Result:** Default sensitivity label applied to all new Copilot content
- **Evidence:** Screenshots of new documents with default labels

### Test 3: Mandatory Labeling Enforcement

- **Objective:** Verify users cannot save Copilot content without a label
- **Steps:**
  1. Have Copilot generate a document
  2. Attempt to remove the sensitivity label
  3. Attempt to save the document without a label
  4. Verify the system prevents saving and prompts for label selection
- **Expected Result:** System prevents saving unlabeled content
- **Evidence:** Screenshot of mandatory labeling prompt

### Test 4: Label Downgrade Justification

- **Objective:** Confirm label downgrades require justification and are audited
- **Steps:**
  1. Open a document labeled "Confidential" that was created by Copilot
  2. Attempt to change the label to "General" (downgrade)
  3. Verify a justification prompt appears
  4. Enter a justification and complete the downgrade
  5. Verify the justification is recorded in the audit log
- **Expected Result:** Downgrades require justification; justification is audited
- **Evidence:** Justification prompt screenshot and audit log entry

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Label inheritance test results | PDF with screenshots | Compliance evidence repository | 7 years |
| Default label verification | Screenshots | Compliance evidence repository | 7 years |
| Mandatory labeling test | Screenshots | Compliance evidence repository | 7 years |
| Label event audit logs | CSV | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Information classification | Label enforcement supports compliance with content classification requirements |
| SEC Regulation S-P | Customer information protection | Labels help classify and protect AI-generated content containing NPI |
| GLBA Safeguards Rule | Data classification controls | Sensitivity labels provide systematic data classification for AI outputs |
| NIST CSF | PR.DS-1 Data at rest protection | Labels enforce protection policies on stored Copilot content |
