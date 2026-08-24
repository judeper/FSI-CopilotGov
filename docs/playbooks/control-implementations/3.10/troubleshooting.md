# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Troubleshooting

Common issues and resolution steps for privacy controls protecting consumer financial information in Copilot interactions, including the distinct response-program, affected-individual notification, and service-provider oversight requirements in the Reg S-P amendments.

## Common Issues

### Issue 1: A Copilot DLP Rule Doesn't Trigger

- **Symptoms:** A labeled source is processed, a typed prompt containing an SIT isn't blocked, external web search still runs, or a configured external-email exclusion doesn't act.
- **Root Cause:** The policy might use an unsupported condition/action pair, target the wrong location, still be propagating, or test a path the feature doesn't cover.
- **Resolution:**
  1. Verify that the policy was created from the **Custom** template and uses location GUID `470f2276-e011-4e9d-a6ec-20768be3a4b0` with enforcement plane `CopilotExperiences`.
  2. Verify the supported condition/action pair: sensitivity label > prevent content processing; SIT > process prompts; SIT > perform web searches; or external email > prevent content processing. Put label and SIT conditions in separate rules.
  3. Allow up to four hours for a policy update to appear in Copilot experiences.
  4. For prompt blocking and external-email exclusion, confirm that the preview feature has reached the tenant.
  5. Confirm that the SIT appears in text typed directly into the prompt. DLP doesn't scan the contents of files uploaded directly into prompts.
  6. Don't expect these rules to act as a general SIT scanner over generated responses.
  7. For label rules, use a supported stored/open file or an email sent on or after January 1, 2025; calendar invites aren't supported. For external-email rules, validate the sender against the tenant's accepted domains because only sender metadata is evaluated.

### Issue 2: Information Barriers Not Blocking Copilot Cross-Segment Access

- **Symptoms:** Users in one segment can access consumer financial data from another segment through Copilot prompts.
- **Root Cause:** Information barriers may not fully apply to Copilot's content grounding, or the barrier segments are misconfigured.
- **Resolution:**
  1. Verify information barrier policies are active: `Get-InformationBarrierPolicy | Select Name, State`
  2. Confirm segment assignments include all relevant users.
  3. Check that SharePoint sites containing NPI have correct segment associations.
  4. Test with Content Search to verify the same user cannot access cross-segment content through other search tools.
  5. If the test uses Copilot Pages or Copilot Notebooks, stop treating it as an Information Barriers failure. Their SharePoint Embedded content doesn't support Information Barriers; use the available admin policies where this gap isn't acceptable.

### Issue 3: Excessive DLP False Positives on Financial Data

- **Symptoms:** Legitimate financial communications are being blocked by DLP, disrupting business operations.
- **Root Cause:** Sensitive information type patterns may be matching non-NPI financial data (e.g., reference numbers, timestamps).
- **Resolution:**
  1. Review false positive incidents to identify pattern-matching issues.
  2. Add exclusion rules for known false positive patterns.
  3. Increase the confidence threshold for SIT detections.
  4. If context is needed, refine or create a custom SIT that incorporates the required evidence rather than adding an unsupported Copilot policy condition.

### Issue 4: NPI Exposure in Copilot Meeting Summaries

- **Symptoms:** Copilot meeting summaries in Teams capture verbally discussed NPI such as account numbers or SSNs.
- **Root Cause:** Copilot transcribes meeting audio and may include NPI spoken during the meeting in summaries.
- **Resolution:**
  1. Apply source permissions, sensitivity labels, retention, and supported DLP controls to recordings and transcripts stored in OneDrive or SharePoint.
  2. Train users to avoid verbalizing full NPI during Copilot-enabled meetings.
  3. Use Teams meeting policies, meeting templates, sensitivity labels, and organizer options to control Copilot, recording, transcription, and who can access the recording and transcript. Some options require Teams Premium or a Microsoft Copilot license.
  4. Verify the resulting OneDrive/SharePoint permissions and lifecycle rather than assuming a separate Copilot summary distribution control exists.

### Issue 5: Service-Provider Notification Intake Isn't Operationalized

- **Symptoms:** The institution can't evidence how it receives, timestamps, evaluates, and escalates a service provider notification under its approved Rule 248.30(a)(5) procedure.
- **Root Cause:** Tenant contacts, Service health monitoring, provider awareness records, and the institution's incident system might not be mapped into one tested process.
- **Resolution:**
  1. Use the institution's legal-approved process to record the provider's awareness time, institution receipt time, provider-reported scope, and 72-hour timing evaluation. The Rule 248.30(a)(5) clock starts with provider awareness of a qualifying breach in a provider-maintained customer-information system, not with the institution's detection time.
  2. On receipt, initiate the Rule 248.30(a)(3) response program and retain the response and recovery evidence.
  3. Keep designated Microsoft online-services tenant administrator contacts accurate and monitor Microsoft 365 Service health and the institution's documented provider-notification channels.
  4. Keep the Rule 248.30(a)(4) affected-individual determination and any 30-day notification clock separate from the provider timing evaluation.
  5. Do not invent a general written-contract requirement. Rule 248.30(a)(5) requires written oversight policies and procedures; it permits a written agreement for a provider to notify affected individuals on the institution's behalf.
  6. Treat Script 5 in the PowerShell guide as a local evidence tracker only, not a Microsoft notification integration or legal deadline calculator.

### Issue 6: Microsoft Service Incident Notification Isn't Reaching the Team

- **Symptoms:** The privacy team doesn't receive or can't locate notification of a Microsoft-determined service incident.
- **Root Cause:** Designated tenant contacts might be stale, Service health isn't monitored, or the internal routing process doesn't include privacy and compliance stakeholders.
- **Resolution:**
  1. Microsoft documents delivery of security-incident notifications to designated administrators of the affected online-services tenant and, depending on the incident, through Microsoft 365 Service health.
  2. Verify tenant administrator contact information and the organization's Service health monitoring.
  3. Map those channels into the approved incident response and service-provider oversight procedures.
  4. Don't use MSRC vulnerability reporting as a substitute for the institution's Reg S-P workflow; Microsoft doesn't document it as that customer notification channel.

### Issue 7: Response Program Not Meeting the Written Requirement

- **Symptoms:** The institution has informal processes for handling NPI incidents but has not documented the formal written response program required by Rule 248.30(a)(3).
- **Root Cause:** Incident response may have evolved organically without formal documentation, or the existing IRP does not explicitly cover Copilot scenarios or the amended Reg S-P notification requirements.
- **Resolution:**
  1. Draft or update the written response program to explicitly address: (a) Copilot-related NPI incidents, (b) detection, response, recovery, scope assessment, and containment under Rule 248.30(a)(3), (c) the Rule 248.30(a)(4) affected-individual notification determination and timing, and (d) Rule 248.30(a)(5) provider oversight and provider-to-institution intake.
  2. Ensure the IRP is formally approved (signed by the designated individual responsible for the safeguards program) and version-controlled.
  3. The IRP does not need to be a standalone document — it can be a section of a broader information security program or privacy policy document. What matters is that it is written, approved, and accessible to those responsible for responding to incidents.
  4. Conduct a tabletop exercise after documentation is complete to verify that the written procedures are actionable.

### Issue 8: DSPM Doesn't Show Expected Copilot Details

- **Symptoms:** AI activity is absent, or the reviewer can see an event but not its prompt and response.
- **Root Cause:** The reviewer may be using **DSPM for AI (classic)**, initial setup might still be populating, or the account lacks the additional content-viewer permissions.
- **Resolution:**
  1. Use **Purview > Solutions > DSPM**, not **DSPM for AI (classic)**.
  2. Review **Discover > Activity explorer > AI activities** and allow approximately a day after first-time DSPM setup for tenant data to appear.
  3. Assign DSPM view permissions according to least privilege.
  4. To view prompt and response bodies, use the additional Content Explorer Content Viewer and Microsoft Purview Data Security AI Content Viewer permissions documented by Microsoft.

### Issue 9: Copilot Pages or Notebooks Controls Differ from OneDrive

- **Symptoms:** The expected OneDrive container, Notebook sensitivity label, or Information Barriers behavior isn't present.
- **Root Cause:** Copilot Pages and Copilot Notebooks are stored together in a user-owned SharePoint Embedded container, not OneDrive. Pages support sensitivity labels, but Notebooks don't have a container sensitivity label, and Information Barriers don't support SharePoint Embedded content.
- **Resolution:**
  1. Manage the content as SharePoint Embedded and verify that storage counts against the organization's SharePoint quota.
  2. Validate DLP and policy-tip behavior; apply sensitivity labels to Copilot Pages where appropriate.
  3. Document the Notebook label and Information Barriers limitations.
  4. Use the available admin policies to disable creation where those limitations aren't acceptable.

## Diagnostic Steps

1. **Check DLP policy status (fail closed):** `Connect-IPPSSession; $id = '470f2276-e011-4e9d-a6ec-20768be3a4b0'; $m = @(Get-DlpCompliancePolicy | Where-Object { $_.EnforcementPlanes -contains 'CopilotExperiences' -and [string]$_.Locations -match [regex]::Escape($id) }); if(-not $m){ throw 'Fail closed: no policy targets the Microsoft 365 Copilot and Copilot Chat location.' }; $m | Select-Object Name, Enabled, Mode, EnforcementPlanes, Locations`
2. **Review SIT accuracy:** Test each sensitive information type against known NPI samples.
3. **Verify barrier status:** `Get-InformationBarrierPolicy | Select Name, State, Segments`
4. **Test supported Copilot actions:** Separately test labeled source exclusion, typed-prompt blocking where available, web-search restriction, and external-email exclusion where available. Include the direct-upload limitation test.
5. **Verify IRP exists and is written:** Confirm the incident response program is a documented, approved policy.
6. **Check service-provider notification procedure:** Confirm tenant contacts, Service health monitoring, internal routing, and the legal-approved procedure are documented and accessible.
7. **Check DLP alerts:** Review **Purview > Data Loss Prevention > Alerts**.
8. **Check Copilot audit:** Review **Purview > Audit > Copilot activities** for `CopilotInteraction` records.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Confirmed NPI breach via Copilot interactions | Privacy Officer + Chief Compliance Officer + Legal |
| Critical | Rule 248.30(a)(5) provider-to-institution notification process at risk of missing an applicable deadline | Privacy Officer + Legal — execute the approved procedure immediately |
| High | Systematic DLP gaps allowing NPI exposure | IT Security + Compliance team |
| High | Written response program does not meet Rule 248.30(a)(3) requirements | Chief Compliance Officer + Legal |
| Medium | Information barrier gaps for specific segments | IT + Compliance for barrier reconfiguration |
| Medium | Service-provider notification deadline calculation unclear | Compliance counsel for definition clarification |
| Low | False positive rate affecting operations | Compliance team for policy tuning |

## Related Resources

- [Control 3.4: Communication Compliance Monitoring](../3.4/portal-walkthrough.md)
- [Control 3.11: Record Keeping Compliance](../3.11/portal-walkthrough.md)
- [SEC Reg S-P Rule 248.30 (17 CFR 248.30)](https://www.ecfr.gov/current/title-17/chapter-II/part-248/section-248.30)
- [SEC Final Rule — Regulation S-P Amendments (Release No. 34-100155)](https://www.sec.gov/files/rules/final/2024/34-100155.pdf)
- [Federal Register — Regulation S-P, 89 FR 47688 (June 3, 2024), document 2024-11116](https://www.federalregister.gov/documents/2024/06/03/2024-11116/regulation-s-p-privacy-of-consumer-financial-information-and-safeguarding-customer-information)
- [Microsoft Purview DLP for Microsoft 365 Copilot and Copilot Chat](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)
- [Microsoft security incident management: customer notification](https://learn.microsoft.com/en-us/compliance/assurance/assurance-sim-containment-eradication-recovery#customer-notification-of-security-incident)
- [Copilot Pages and Notebooks compliance summary](https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide)
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
