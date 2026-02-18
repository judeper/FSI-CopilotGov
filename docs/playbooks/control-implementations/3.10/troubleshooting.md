# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Troubleshooting

Common issues and resolution steps for privacy controls protecting consumer financial information in Copilot interactions, including incident response program and vendor notification issues.

## Common Issues

### Issue 1: DLP Not Detecting NPI in Copilot Responses

- **Symptoms:** Copilot generates responses containing SSNs, account numbers, or other NPI without triggering DLP.
- **Root Cause:** DLP policies may not cover Copilot interaction locations, or the sensitive information types do not match the data format in Copilot outputs.
- **Resolution:**
  1. Verify the DLP policy includes Copilot-relevant locations (Exchange, Teams, SharePoint).
  2. Test the sensitive information type against the specific data format appearing in Copilot responses.
  3. Update SIT patterns if Copilot formats data differently (e.g., partial masking, different separators).
  4. Enable DLP for the Copilot interaction workload if available in the tenant.

### Issue 2: Information Barriers Not Blocking Copilot Cross-Segment Access

- **Symptoms:** Users in one segment can access consumer financial data from another segment through Copilot prompts.
- **Root Cause:** Information barriers may not fully apply to Copilot's content grounding, or the barrier segments are misconfigured.
- **Resolution:**
  1. Verify information barrier policies are active: `Get-InformationBarrierPolicy | Select Name, State`
  2. Confirm segment assignments include all relevant users.
  3. Check that SharePoint sites containing NPI have correct segment associations.
  4. Test with Content Search to verify the same user cannot access cross-segment content through other search tools.

### Issue 3: Excessive DLP False Positives on Financial Data

- **Symptoms:** Legitimate financial communications are being blocked by DLP, disrupting business operations.
- **Root Cause:** Sensitive information type patterns may be matching non-NPI financial data (e.g., reference numbers, timestamps).
- **Resolution:**
  1. Review false positive incidents to identify pattern-matching issues.
  2. Add exclusion rules for known false positive patterns.
  3. Increase the confidence threshold for SIT detections.
  4. Implement context-based rules that require NPI to appear alongside other identifying information.

### Issue 4: NPI Exposure in Copilot Meeting Summaries

- **Symptoms:** Copilot meeting summaries in Teams capture verbally discussed NPI such as account numbers or SSNs.
- **Root Cause:** Copilot transcribes meeting audio and may include NPI spoken during the meeting in summaries.
- **Resolution:**
  1. Implement DLP policies on Teams meeting transcripts and summaries.
  2. Train users to avoid verbalizing full NPI during Copilot-enabled meetings.
  3. Configure Copilot meeting settings to restrict summary distribution.
  4. Apply sensitivity labels to meeting recordings and transcripts containing financial discussions.

### Issue 5: 72-Hour Vendor Notification Window — Calculation and Triggering

- **Symptoms:** Uncertainty about when the 72-hour clock starts under SEC Rule 248.30(a)(3), or the institution cannot determine whether the window has been met for a past incident.
- **Root Cause:** The rule requires notification within 72 hours of "detection," but "detection" is not precisely defined in the amended regulation. Institutions may not have a consistent definition, making clock-start determination inconsistent.
- **Resolution:**
  1. Define "detection" in writing in the incident response program: the 72-hour clock starts at the earliest of: (a) a DLP alert flagging NPI exposure through Copilot, (b) a user report of NPI exposure, or (c) any other event giving the institution reason to believe unauthorized access occurred. Document this definition in the IRP.
  2. Use the incident response timer script (Script 5 in the PowerShell Setup guide) to track the notification deadline from the moment of detection. Run it at detection, not at the end of investigation.
  3. Note that the 72-hour window is a notification deadline, not an investigation completion deadline — the notification to Microsoft can precede a completed investigation. The notification should describe the known facts and the status of the ongoing investigation.
  4. If a past incident is discovered to have missed the 72-hour window: document the gap, notify Microsoft as soon as possible, and consult legal counsel regarding voluntary self-disclosure to the SEC.

### Issue 6: Microsoft Notification Procedure for Copilot NPI Incidents

- **Symptoms:** When a Copilot NPI incident occurs, the compliance team cannot determine how to formally notify Microsoft as the service provider under Rule 248.30(a)(3).
- **Root Cause:** Microsoft's notification path for Reg S-P vendor notification is not the same as general support requests. The correct channel is not obvious from standard Microsoft 365 admin documentation.
- **Resolution:**
  1. **Primary channel — Microsoft Security Response Center (MSRC):** For security incidents involving unauthorized access to NPI through Copilot, report to MSRC at msrc.microsoft.com. This is Microsoft's designated security incident response team.
  2. **Secondary channel — Microsoft 365 admin portal:** For incidents reportable under the data processing terms in the Microsoft Online Subscription Agreement or Data Processing Agreement, use the admin portal (admin.microsoft.com > Support > New service request) and explicitly reference "Reg S-P Rule 248.30(a)(3) notification."
  3. **Microsoft account team:** Contact the Microsoft account team to confirm the correct notification path and to confirm that Microsoft acknowledges receipt of the notification — confirmation is important for documentation.
  4. Pre-stage the notification: draft a notification template before an incident occurs. The template should include: institution name and contact, incident description, NPI categories affected, estimated scope, containment status, and the regulatory citation (17 CFR 248.30(a)(3)).
  5. Document the Microsoft notification in the incident record: date/time, channel used, Microsoft confirmation of receipt, and any Microsoft response.

### Issue 7: Incident Response Program Not Meeting "Written" Requirement

- **Symptoms:** The institution has informal processes for handling NPI incidents but has not documented a formal written incident response program as required by Rule 248.30(a)(4).
- **Root Cause:** Incident response may have evolved organically without formal documentation, or the existing IRP does not explicitly cover Copilot scenarios or the amended Reg S-P notification requirements.
- **Resolution:**
  1. Draft or update the written IRP to explicitly address: (a) Copilot-related NPI incidents, (b) the 72-hour vendor notification procedure per Rule 248.30(a)(3), and (c) the 30-day customer notification timeline.
  2. Ensure the IRP is formally approved (signed by the designated individual responsible for the safeguards program) and version-controlled.
  3. The IRP does not need to be a standalone document — it can be a section of a broader information security program or privacy policy document. What matters is that it is written, approved, and accessible to those responsible for responding to incidents.
  4. Conduct a tabletop exercise after documentation is complete to verify that the written procedures are actionable.

## Diagnostic Steps

1. **Check DLP policy status:** `Get-DlpCompliancePolicy | Select Name, Enabled, Mode`
2. **Review SIT accuracy:** Test each sensitive information type against known NPI samples.
3. **Verify barrier status:** `Get-InformationBarrierPolicy | Select Name, State, Segments`
4. **Test Copilot responses:** Prompt Copilot with queries that might surface NPI from test data.
5. **Verify IRP exists and is written:** Confirm the incident response program is a documented, approved policy.
6. **Check 72-hour procedure:** Confirm the Microsoft notification path and contact are documented and accessible.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Confirmed NPI breach via Copilot interactions | Privacy Officer + Chief Compliance Officer + Legal |
| Critical | 72-hour Microsoft notification window at risk of being missed | Privacy Officer + Legal — execute notification immediately |
| High | Systematic DLP gaps allowing NPI exposure | IT Security + Compliance team |
| High | Written IRP does not meet Rule 248.30(a)(4) requirements | Chief Compliance Officer + Legal |
| Medium | Information barrier gaps for specific segments | IT + Compliance for barrier reconfiguration |
| Medium | 72-hour notification window calculation unclear | Compliance counsel for definition clarification |
| Low | False positive rate affecting operations | Compliance team for policy tuning |

## Related Resources

- [Control 3.4: Communication Compliance Monitoring](../3.4/portal-walkthrough.md)
- [Control 3.11: Record Keeping Compliance](../3.11/portal-walkthrough.md)
- [SEC Reg S-P Rule 248.30 (17 CFR 248.30)](https://www.ecfr.gov/current/title-17/chapter-II/part-248/section-248.30)
- [Microsoft Security Response Center (MSRC)](https://msrc.microsoft.com)
