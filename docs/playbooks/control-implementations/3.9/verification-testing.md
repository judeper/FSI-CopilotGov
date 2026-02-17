# Control 3.9: AI Disclosure, Transparency, and SEC Marketing Rule — Verification & Testing

Test cases and evidence collection procedures to validate AI disclosure and transparency controls for Copilot-generated content.

## Test Cases

### Test 1: Sensitivity Label Application

- **Objective:** Verify that the AI-Assisted Content sensitivity label can be applied to Copilot-generated documents
- **Steps:**
  1. Create a document using Copilot in Word.
  2. Apply the "AI-Assisted Content" sensitivity label.
  3. Verify the header and footer content markings appear on the document.
  4. Save and reopen the document to confirm label persistence.
- **Expected Result:** Label is applied, content markings (header/footer) are visible, and the label persists after save/reopen.
- **Evidence:** Screenshot of labeled document showing header and footer AI disclosure markings.

### Test 2: DLP Enforcement for External Communications

- **Objective:** Confirm that DLP blocks undisclosed AI-assisted content sent to external recipients
- **Steps:**
  1. Draft an email using Copilot assistance.
  2. Attempt to send the email to an external recipient without including AI disclosure language.
  3. Verify that DLP blocks or warns the sender.
  4. Add the required AI disclosure text and resend successfully.
- **Expected Result:** DLP blocks the email without disclosure and allows it after disclosure is added.
- **Evidence:** DLP policy tip screenshot and message trace showing block and subsequent delivery.

### Test 3: Marketing Material Review Workflow

- **Objective:** Validate that Copilot-assisted marketing materials go through SEC Marketing Rule review
- **Steps:**
  1. Use Copilot to draft a marketing brochure containing performance data.
  2. Route the document through the communication compliance review process.
  3. Verify the reviewer can assess SEC Marketing Rule compliance elements.
  4. Complete the review and confirm the audit trail captures the assessment.
- **Expected Result:** Marketing material is captured, reviewed for SEC compliance, and the review is logged.
- **Evidence:** Review queue entry and completed review record.

### Test 4: AI Disclosure Template Availability

- **Objective:** Confirm that AI disclosure templates are accessible to all Copilot users
- **Steps:**
  1. Log in as a Copilot-licensed user.
  2. Verify the AI disclosure templates are available in Outlook and Word.
  3. Test inserting a disclosure template into an email and a document.
  4. Confirm the template text matches the approved disclosure language.
- **Expected Result:** Templates are accessible and contain the correct, approved disclosure language.
- **Evidence:** Screenshots showing template access and content in Outlook and Word.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Label configuration | Purview portal | Screenshot | With control documentation |
| DLP policy test results | Message trace | CSV | 7 years |
| Marketing review records | Communication compliance | Redacted screenshots | 7 years |
| Disclosure template samples | Email/Document | PDF copies | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Marketing Rule | Advertising disclosure requirements | Supports compliance with AI-assisted content disclosure in marketing materials |
| SEC Reg BI | Client communication transparency | Helps meet disclosure obligations for AI-assisted recommendations |
| FINRA 2210 | Fair and balanced communication | Supports transparency in AI-generated public communications |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for disclosure enforcement issues
- Proceed to [Control 3.10](../3.10/portal-walkthrough.md) for SEC Reg S-P privacy controls
