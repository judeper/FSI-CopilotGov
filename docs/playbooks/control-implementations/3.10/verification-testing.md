# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Verification & Testing

Test cases and evidence collection procedures to validate privacy controls for consumer financial information in Copilot interactions.

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

### Test 4: Privacy Incident Response Workflow

- **Objective:** Verify that NPI-related DLP incidents trigger the appropriate response workflow
- **Steps:**
  1. Trigger a DLP incident involving consumer financial data.
  2. Verify the incident appears in the DLP incident report.
  3. Confirm the compliance team receives notification.
  4. Walk through the incident investigation and resolution process.
- **Expected Result:** DLP incidents trigger notifications, are logged for investigation, and can be resolved.
- **Evidence:** DLP incident report and notification email.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| DLP policy configuration | Purview portal | Screenshot | With control documentation |
| DLP incident reports | Audit log | CSV export | 7 years |
| Information barrier test results | Copilot response | Screenshot | With control documentation |
| Privacy impact assessment | Assessment document | PDF | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Reg S-P Rule 30 | Safeguard customer records | Supports compliance with NPI safeguarding in AI interactions |
| GLBA Title V | Financial privacy | Helps meet privacy requirements for consumer financial information |
| FTC Safeguards Rule | Information security program | Supports requirements for protecting customer information |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for privacy control issues
- Proceed to [Control 3.11](../3.11/portal-walkthrough.md) for record keeping compliance
