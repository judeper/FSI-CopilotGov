# Control 2.2: Sensitivity Labels and Copilot Content Classification — Verification & Testing

Test cases and evidence collection for validating sensitivity label enforcement with Copilot. This playbook covers verification for label groups, Copilot Studio agent label inheritance, and nested auto-labeling conditions.

## Test Cases

### Test 1: Label Taxonomy Structure Verification (Label Groups)

- **Objective:** Confirm the label taxonomy has been migrated to or is configured correctly with label groups (GA January 2026)
- **Steps:**
  1. Run Script 5 (Label Groups Migration Status Check) to inventory current label structure
  2. Verify all labels are organized within the expected label groups (Public, Internal, Confidential, Highly Confidential)
  3. If parent/child hierarchy is still in use, confirm migration is scheduled and document the timeline
  4. After migration: confirm all DLP policies that referenced parent label names continue to function by testing with labeled content
- **Expected Result:** Label taxonomy is organized in label groups; DLP policies verified to function correctly with new structure
- **Evidence:** Label taxonomy export (Script 5 output) and DLP policy test results post-migration

### Test 2: Label Inheritance from Source Documents

- **Objective:** Verify Copilot-generated content inherits the appropriate sensitivity label from source documents
- **Steps:**
  1. Create a test document labeled "Confidential — Standard" in SharePoint
  2. Use Copilot to create a summary of the Confidential document
  3. Check the sensitivity label on the Copilot-generated summary
  4. Verify it inherits the "Confidential" label (or higher)
- **Expected Result:** Generated content inherits the source document's sensitivity label
- **Evidence:** Screenshots showing source label and generated content label

### Test 3: Copilot Studio Agent Label Inheritance Verification

- **Objective:** Confirm Copilot Studio agents inherit the highest sensitivity label from their knowledge sources
- **Steps:**
  1. Identify a deployed Copilot Studio agent with knowledge sources carrying different sensitivity labels
  2. Document the labels on each knowledge source (e.g., "Confidential — Standard" and "Internal — General")
  3. Interact with the agent and confirm DLP monitoring triggers at the appropriate label tier (Confidential in this example)
  4. Verify the agent deployment record documents the inherited label
  5. For a new agent with an unlabeled knowledge source: add a labeled document to the knowledge base and verify the inherited label updates
- **Expected Result:** Agent's effective inherited label matches the highest label across all knowledge sources; DLP policies respond at the appropriate tier
- **Evidence:** Agent knowledge source label inventory and DLP monitoring evidence

### Test 4: Auto-Labeling with Nested Conditions

- **Objective:** Verify nested AND/OR/NOT auto-labeling conditions apply labels correctly to FSI financial content, including the ability to override manually applied labels on files
- **Steps:**
  1. Create a test document that matches a nested condition (e.g., contains both a CUSIP pattern AND an earnings context keyword)
  2. Upload the document to a SharePoint site covered by the auto-labeling policy
  3. Verify the policy applies the expected label (Confidential — MNPI per the nested rule)
  4. Create a second test document matching only part of the nested condition (e.g., CUSIP pattern only, no earnings keyword) and verify the label is NOT applied
  5. Create a third test document that would match conditions but is in an excluded folder (NOT condition) and verify the label is NOT applied
  6. **Override test:** Manually apply a lower-sensitivity label (e.g., "Internal — General") to a file that matches auto-labeling conditions. Verify the auto-labeling policy overrides the manual label and applies the correct higher-sensitivity label.
- **Expected Result:** Nested auto-labeling conditions correctly apply and withhold labels based on combined condition logic; auto-labeling overrides manually applied labels on files when configured
- **Evidence:** Screenshots of labeled and unlabeled test documents with condition logic documentation, including override scenario

### Test 4a: Default Labeling for Teams Meetings

- **Objective:** Verify default sensitivity labels are applied to Teams meetings for regulated user groups
- **Steps:**
  1. Confirm that a Teams meeting label policy is configured with a default label for regulated user groups.
  2. Create a new Teams meeting as a user in the regulated group.
  3. Verify the default sensitivity label is automatically applied to the meeting.
  4. Confirm that meeting artifacts (transcripts, notes, recordings) inherit the meeting's sensitivity label.
  5. Verify Copilot-generated meeting summaries respect the meeting label classification.
- **Expected Result:** Default label is applied to Teams meetings; meeting artifacts inherit the label.
- **Evidence:** Meeting properties showing applied label; Copilot summary with inherited label.

### Test 5: Default Label Application

- **Objective:** Confirm default labels are applied to new Copilot-created content
- **Steps:**
  1. Use Copilot to draft a new document from scratch (no source documents)
  2. Check the sensitivity label on the new document
  3. Verify the default label ("Internal — General" or configured default) is applied
  4. Repeat across Word, Excel, and PowerPoint
- **Expected Result:** Default sensitivity label applied to all new Copilot content
- **Evidence:** Screenshots of new documents with default labels

### Test 6: Mandatory Labeling Enforcement

- **Objective:** Verify users cannot save Copilot content without a label
- **Steps:**
  1. Have Copilot generate a document
  2. Attempt to remove the sensitivity label
  3. Attempt to save the document without a label
  4. Verify the system prevents saving and prompts for label selection
- **Expected Result:** System prevents saving unlabeled content
- **Evidence:** Screenshot of mandatory labeling prompt

### Test 7: Label Downgrade Justification

- **Objective:** Confirm label downgrades require justification and are audited
- **Steps:**
  1. Open a document labeled "Confidential — Standard" that was created by Copilot
  2. Attempt to change the label to "Internal — General" (downgrade)
  3. Verify a justification prompt appears
  4. Enter a justification and complete the downgrade
  5. Verify the justification is recorded in the audit log (run Script 2 to confirm)
- **Expected Result:** Downgrades require justification; justification is audited
- **Evidence:** Justification prompt screenshot and audit log entry

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Label taxonomy export (label groups migration status) | CSV | Compliance evidence repository | 7 years |
| Label inheritance test results | PDF with screenshots | Compliance evidence repository | 7 years |
| Agent label inheritance inventory | PDF | Compliance evidence repository | 7 years |
| Nested auto-labeling condition test results | PDF with screenshots | Compliance evidence repository | 7 years |
| Default label verification | Screenshots | Compliance evidence repository | 7 years |
| Mandatory labeling test | Screenshots | Compliance evidence repository | 7 years |
| Label event audit logs | CSV | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Information classification | Label enforcement supports compliance with content classification requirements; agent label inheritance extends classification to AI-generated content |
| SEC Regulation S-P | Customer information protection | Labels help classify and protect AI-generated content containing NPI; nested auto-labeling enables precise classification of complex financial data |
| GLBA §501(b) | Data classification controls | Sensitivity labels and label groups provide systematic data classification for AI outputs and Copilot interactions |
| NIST CSF | PR.DS-1 Data at rest protection | Labels enforce protection policies on stored Copilot content; agent inherited labels extend protection to agent interactions |
- Back to [Control 2.2](../../../controls/pillar-2-security/2.2-sensitivity-labels-classification.md)
