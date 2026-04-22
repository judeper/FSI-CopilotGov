# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Verification & Testing

Test cases and evidence collection procedures to validate privacy controls for consumer financial information in Copilot interactions, including the incident response program requirements under the 2023 Reg S-P amendments.

## Test Cases

### Test 1: DLP Detection of NPI in Copilot Interactions

- **Objective:** Verify that DLP policies detect nonpublic personal information in Copilot-assisted communications
- **Steps:**
  1. Using a test account, draft an email with Copilot that contains test SSN and account number data.
  2. Attempt to send the email to an external recipient.
  3. Verify that the DLP policy tip appears warning about NPI content.
  4. Confirm that high-volume NPI triggers blocking behavior.
- **Expected Result:** DLP detects NPI content, displays policy tips, and blocks high-volume transmissions.
- **Evidence:** Screenshots of DLP policy tips and block notifications.

### Test 2: Information Barrier Enforcement

- **Objective:** Confirm that information barriers prevent Copilot from surfacing NPI across business unit boundaries
- **Steps:**
  1. Create test documents containing consumer financial data in a restricted segment's SharePoint site.
  2. Have a user from a different segment use Copilot to search for or reference that content.
  3. Verify that Copilot does not surface the restricted content in its responses.
- **Expected Result:** Information barriers prevent cross-segment NPI exposure through Copilot.
- **Evidence:** Copilot response showing no restricted content surfaced.

### Test 3: Sensitivity Label Protection for NPI Documents

- **Objective:** Validate that documents containing NPI are protected with appropriate sensitivity labels
- **Steps:**
  1. Create a document containing consumer financial data.
  2. Apply or verify auto-application of the appropriate sensitivity label.
  3. Confirm the label enforces encryption and access restrictions.
  4. Test that Copilot interactions with the document respect label protections.
- **Expected Result:** NPI documents are labeled, encrypted, and Copilot respects label-based access controls.
- **Evidence:** Document properties showing label and encryption status.

### Test 4: Incident Response Program Verification (Rule 248.30(a)(4))

- **Objective:** Verify that the written incident response program covers Copilot-related NPI incidents and includes the required notification procedures
- **Steps:**
  1. Review the firm's written incident response program (IRP) for Copilot NPI coverage.
  2. Confirm the IRP is written (not informal) and includes: Copilot-specific incident scenarios, severity classification, escalation paths, containment steps, and notification procedures.
  3. Verify the 72-hour Microsoft notification procedure is documented (SEC Rule 248.30(a)(3)): confirm Microsoft notification channel, contact information, and notification template are accessible.
  4. Verify the 30-day customer notification timeline is documented.
  5. Confirm a named individual is responsible for executing the Microsoft notification within the 72-hour window.
- **Expected Result:** Written IRP exists, covers Copilot scenarios, and documents both the 72-hour vendor notification and 30-day customer notification procedures.
- **Evidence:** IRP document with Copilot section; 72-hour notification procedure documentation; responsible party assignment.

### Test 5: Incident Response Simulation — NPI Exposure via Copilot

- **Objective:** Simulate a Copilot NPI exposure event to test the incident response program and verify the 72-hour notification window is achievable
- **Steps:**
  1. Run a tabletop exercise scenario: "Copilot Chat surfaced client account numbers to a user without appropriate permissions due to a permission misconfiguration. The exposure was detected via a DLP alert."
  2. Walk through the IRP steps: detection confirmation → severity classification → internal escalation (4 hours) → executive notification (24 hours) → Microsoft notification preparation (72-hour deadline).
  3. Time the exercise — confirm that the 72-hour notification to Microsoft could be executed within the required window.
  4. Identify any gaps in the notification chain (e.g., unavailable contacts, missing notification templates).
  5. Document exercise outcomes and any remediation items.
- **Expected Result:** Tabletop exercise completed with documented outcome; notification chain is achievable within the 72-hour and 30-day windows; gaps identified and assigned for remediation.
- **Evidence:** Exercise facilitation notes and outcome documentation; gap remediation log.

### Test 6: Privacy Incident Response Alert Workflow

- **Objective:** Verify that NPI-related DLP incidents trigger the appropriate automated alert workflow
- **Steps:**
  1. Trigger a DLP incident involving consumer financial data (test environment).
  2. Verify the incident appears in the DLP incident report (Purview > Data loss prevention > Incidents).
  3. Confirm the compliance team and Privacy Officer receive notification via configured alert policy.
  4. Walk through the incident investigation and resolution process in Purview.
- **Expected Result:** DLP incidents trigger automated notifications, are logged for investigation, and can be resolved.
- **Evidence:** DLP incident report and notification confirmation.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| DLP policy configuration | Purview portal | Screenshot | With control documentation |
| DLP incident reports | Audit log | CSV export | 7 years |
| Information barrier test results | Copilot response | Screenshot | With control documentation |
| Privacy impact assessment | Assessment document | PDF | 7 years |
| Written IRP with Copilot section | IRP document | PDF | 7 years (updated annually) |
| 72-hour notification procedure | IRP or standalone document | PDF | 7 years |
| Tabletop exercise documentation | Exercise records | PDF | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Reg S-P Rule 248.30(a)(3) | 72-hour vendor notification for unauthorized NPI access | Test 4 and 5 verify documented procedure and achievable window |
| SEC Reg S-P Rule 248.30(a)(4) | Written incident response program | Test 4 verifies existence and completeness of written IRP |
| SEC Reg S-P Rule 30 | Safeguard customer records | Supports compliance with NPI safeguarding in AI interactions |
| GLBA Title V | Financial privacy | Helps meet privacy requirements for consumer financial information |
| GLBA §501(b) | Safeguards provision for NPI | Supports requirements for protecting customer information at banks and broker-dealers (statutory basis for SEC Reg S-P safeguards; the FTC Safeguards Rule is a separate implementing regulation outside SEC jurisdiction) |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for privacy control issues
- Proceed to [Control 3.11](../3.11/portal-walkthrough.md) for record keeping compliance
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
