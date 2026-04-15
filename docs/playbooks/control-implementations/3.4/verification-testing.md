# Control 3.4: Communication Compliance Monitoring — Verification & Testing

Test cases and evidence collection procedures to validate communication compliance monitoring for Copilot-assisted communications, including IRM integration verification.

## Test Cases

### Test 1: Policy Activation Verification

- **Objective:** Confirm communication compliance policies are active and targeting Copilot users
- **Steps:**
  1. Navigate to Communication compliance > Policies in the Purview portal.
  2. Verify the FSI Copilot policy shows status "Active".
  3. Confirm the supervised user scope includes all Copilot-licensed users.
  4. Verify all required locations (Exchange, Teams, Copilot interactions) are enabled.
- **Expected Result:** Policy is active, correctly scoped to Copilot users, and covers all communication channels.
- **Evidence:** Screenshot of policy configuration showing status, scope, and locations.

### Test 2: Copilot-Assisted Communication Detection

- **Objective:** Verify that Copilot-drafted communications trigger policy matches when containing flagged content
- **Steps:**
  1. Using a test account, ask Copilot to draft an email containing language that matches a detection rule (e.g., language suggesting guaranteed returns).
  2. Send the email to a monitored recipient.
  3. Wait up to 24 hours for policy processing.
  4. Check the Communication compliance dashboard for a new policy match.
- **Expected Result:** The Copilot-assisted communication is flagged and appears in the review queue.
- **Evidence:** Screenshot of the policy match in the review queue with communication details.

### Test 3: Reviewer Workflow Validation

- **Objective:** Confirm that reviewers can access, investigate, and resolve flagged communications
- **Steps:**
  1. Open a flagged communication in the review queue.
  2. Verify the full context is visible (original message, Copilot interaction data, recipient information).
  3. Apply a resolution action (Resolve, Escalate, or Tag as false positive).
  4. Verify the resolution is recorded in the audit trail.
- **Expected Result:** Reviewers can complete the full investigation and resolution workflow.
- **Evidence:** Screenshot of the review interface and resolution action confirmation.

### Test 4: IRM Integration Verification

- **Objective:** Confirm that CC policy matches generate IRM risk indicators for the affected user
- **Steps:**
  1. Confirm IRM integration is enabled: navigate to **Communication compliance > Settings > Insider Risk Management integration** and verify the toggle is On.
  2. Trigger a CC policy match using a test account (send a Copilot-drafted message with promissory language as in Test 2).
  3. Wait 24 hours after the CC match is logged in the review queue.
  4. Navigate to the IRM dashboard (Control 2.10) and search for risk events associated with the test account.
  5. Confirm a risk indicator sourced from Communication Compliance appears for the test user.
- **Expected Result:** Within 24 hours of a CC policy match, a corresponding IRM risk indicator appears for the user, demonstrating the cross-pillar governance loop is operational.
- **Evidence:** Screenshot of the IRM risk indicator for the test user, showing Communication Compliance as the source.

### Test 5: Trainable Classifier Accuracy

- **Objective:** Validate that trainable classifiers correctly identify FSI-specific compliance risks
- **Steps:**
  1. Submit a set of 10 test communications -- 5 containing genuine compliance risks and 5 benign messages.
  2. Review classifier results for accuracy.
  3. Calculate precision (true positives / total positives) and recall (true positives / actual positives).
  4. Document false positive rate for ongoing tuning.
- **Expected Result:** Classifier precision above 80% and recall above 70% for FSI-specific risk categories.
- **Evidence:** Accuracy report with precision, recall, and false positive metrics.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Policy configuration | Purview portal | Screenshot | With control documentation |
| Policy match samples | Review queue | Redacted screenshots | Per retention policy |
| Resolution audit trail | Purview audit log | CSV export | Per retention policy |
| IRM integration status | CC Settings | Screenshot | With control documentation |
| IRM indicator confirmation | IRM dashboard | Screenshot | Per retention policy |
| Classifier accuracy metrics | Test results | Spreadsheet | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3110(a) | Reasonably designed supervisory system | CC-to-IRM integration creates automated escalation strengthening the supervisory system |
| SEC Reg BI | Best interest communication standards | Helps meet review requirements for client-facing communications |
| FINRA 2210 | Communications with the public | Supports monitoring of AI-drafted public communications |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for communication compliance issues
- Proceed to [Control 3.5](../3.5/portal-walkthrough.md) for FINRA Rule 2210 compliance
- Back to [Control 3.4](../../../controls/pillar-3-compliance/3.4-communication-compliance.md)
