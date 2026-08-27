# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Troubleshooting

Common issues and resolution steps for privacy controls protecting consumer financial information in Copilot interactions, including incident response program and vendor notification issues.

## Common Issues

### Issue 1: NPI Appears in Copilot Responses and No DLP Block Occurs

- **Symptoms:** Copilot generates responses containing SSNs, account numbers, or other NPI, and no DLP block or policy tip appears.
- **Root Cause:** Most often this is expected behavior rather than a misconfiguration. In the **Microsoft 365 Copilot and Copilot Chat** DLP location, SIT-based enforcement evaluates **the text typed into the prompt** — there is no documented DLP action that inspects or blocks the text of a generated response. The secondary causes are: the policy isn't actually enabled on the Copilot location/enforcement plane, the test data was uploaded as a file rather than typed, or the SIT doesn't match the data format.
- **Resolution:**
  1. Reset the expectation first: this control restricts **prompts** and **web grounding**, and can exclude labeled files and emails from grounding. It does not scan response text. What limits NPI in a response is what Copilot is allowed to ground on — user permissions, sensitivity labels with the `Prevent Copilot from processing content` action, and information barriers.
  2. For response-side visibility, use DSPM / Activity explorer **AI activities** (SIT detections in prompts and responses), the unified audit log for interaction metadata, and eDiscovery (**Type > Contains any of > Copilot activity**) for the interaction content. These are observation surfaces, not enforcement.
  3. Run the fail-closed diagnostic in the next section to confirm the expected policy is `Mode=Enable` on the Copilot location and enforcement plane with both expected rules and their actions and alerts. Policy updates can take up to four hours to take effect.
  4. For prompt tests, **type** the test data as prompt text rather than attaching a file; DLP can't scan the contents of files uploaded directly into prompts. SIT-based prompt blocking is also in preview and rolling out, so confirm rollout has reached the tenant.
  5. Test the sensitive information type against the specific data format in use, and update SIT patterns if the data is formatted differently (partial masking, different separators).
  6. Add or verify a sensitivity label rule (`Content contains > Sensitivity labels` with `Prevent Copilot from processing content`) so labeled NPI files and emails are excluded from grounding. Items may still appear in response citations even when their content is excluded.

> **Documented Copilot DLP limitations (read before relying on this control):** In the **Microsoft 365 Copilot and Copilot Chat** location, sensitive information type (SIT) enforcement evaluates **the text a user types into the prompt**. The two documented SIT actions are **Prevent Copilot from processing content > Processing prompts** and **> Performing Web Searches**. Microsoft does not document a DLP action that inspects or blocks the text of a **generated Copilot response**; sensitive data in responses can be *observed* after the fact (DSPM / Activity explorer **AI activities**, Audit, eDiscovery) but is not blocked by this control. DLP also can't scan the contents of files uploaded directly into a prompt — only typed prompt text is checked. SIT-based prompt blocking is in preview and rolling out. The sensitivity label condition covers emails sent on or after January 1, 2025; calendar invites and Admin units are not supported. Policy updates can take up to four hours to take effect in the Copilot experience.

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

1. **Check the Copilot DLP policy (fail closed).** Run this in Security & Compliance PowerShell. It stops on the first failed check; the success line prints only when everything passes. If a check reports that a property is not exposed, verify that item by hand in **Microsoft Purview portal > Data loss prevention > Policies** rather than assuming it passed.

    ```powershell
    $ErrorActionPreference = 'Stop'
    Connect-IPPSSession -ErrorAction Stop

    $policyName          = "FSI-RegSP-Copilot-Privacy-Protection"
    $copilotLocationGuid = "470f2276-e011-4e9d-a6ec-20768be3a4b0"
    $expectedRules       = @{
        "RegSP-LowVolume-NPI-Warn"   = @{ Restrict = $false; Severity = "Medium" }
        "RegSP-HighVolume-NPI-Block" = @{ Restrict = $true;  Severity = "High"   }
    }

    function Assert-ExposedProperty {
        param($InputObject, [string]$Name, [string]$Subject)
        if (-not $InputObject.PSObject.Properties[$Name]) {
            throw "Fail closed: '$Subject' does not expose a '$Name' property in this tenant. Verify '$Subject' manually in the Microsoft Purview portal (Data loss prevention > Policies)."
        }
    }

    $policy = Get-DlpCompliancePolicy -Identity $policyName -ErrorAction Stop
    if (-not $policy) { throw "Fail closed: DLP policy '$policyName' was not found." }

    Assert-ExposedProperty $policy 'Mode' $policyName
    if ("$($policy.Mode)" -ne 'Enable') { throw "Fail closed: '$policyName' is Mode=$($policy.Mode); expected Mode=Enable." }

    Assert-ExposedProperty $policy 'Locations' $policyName
    if ((ConvertTo-Json -InputObject $policy.Locations -Depth 10 -Compress) -notmatch [regex]::Escape($copilotLocationGuid)) {
        throw "Fail closed: '$policyName' does not target Copilot location GUID $copilotLocationGuid."
    }

    Assert-ExposedProperty $policy 'EnforcementPlanes' $policyName
    if (-not (@($policy.EnforcementPlanes) -contains 'CopilotExperiences')) {
        throw "Fail closed: '$policyName' does not set EnforcementPlanes=CopilotExperiences."
    }

    $rules = @(Get-DlpComplianceRule -Policy $policyName -ErrorAction Stop)
    foreach ($ruleName in $expectedRules.Keys) {
        $rule = $rules | Where-Object { $_.Name -eq $ruleName }
        if (-not $rule) { throw "Fail closed: expected rule '$ruleName' is missing from '$policyName'." }

        Assert-ExposedProperty $rule 'Disabled' $ruleName
        if ($rule.Disabled) { throw "Fail closed: rule '$ruleName' is disabled." }

        Assert-ExposedProperty $rule 'GenerateAlert' $ruleName
        if (-not @($rule.GenerateAlert)) { throw "Fail closed: rule '$ruleName' has no alert recipients, so no notification is produced." }

        Assert-ExposedProperty $rule 'ReportSeverityLevel' $ruleName
        if ("$($rule.ReportSeverityLevel)" -ne $expectedRules[$ruleName].Severity) {
            throw "Fail closed: rule '$ruleName' has ReportSeverityLevel=$($rule.ReportSeverityLevel); expected $($expectedRules[$ruleName].Severity)."
        }

        if ($expectedRules[$ruleName].Restrict) {
            Assert-ExposedProperty $rule 'RestrictAccess' $ruleName
            if ((ConvertTo-Json -InputObject $rule.RestrictAccess -Depth 10 -Compress) -notmatch 'ExcludeContentProcessing') {
                throw "Fail closed: rule '$ruleName' does not carry the ExcludeContentProcessing restriction."
            }
            Assert-ExposedProperty $rule 'RestrictWebGrounding' $ruleName
            if (-not $rule.RestrictWebGrounding) { throw "Fail closed: rule '$ruleName' does not set RestrictWebGrounding." }
        }
    }

    Write-Host "Verified: '$policyName' Mode=Enable, Copilot location $copilotLocationGuid, EnforcementPlanes=CopilotExperiences, rules $($expectedRules.Keys -join ', ') present with expected restriction and alert configuration." -ForegroundColor Green
    ```

2. **Review SIT accuracy:** Test each sensitive information type against known NPI samples, entered as prompt text.
3. **Verify barrier status:** `Get-InformationBarrierPolicy | Select Name, State, Segments`
4. **Check DLP matches and alerts:** Microsoft Purview > **Data loss prevention > Alerts** for triage, and Activity explorer **AI activities** (Workload `Copilot`, activity `DLPRuleMatch` / `DLPRuleEnforce`) for the underlying records.
5. **Test Copilot prompts:** Prompt Copilot with queries that might surface NPI from test data, and record the result. Response content is observed through DSPM / Activity explorer and eDiscovery, not blocked by this control.
6. **Verify IRP exists and is written:** Confirm the incident response program is a documented, approved policy.
7. **Check 72-hour procedure:** Confirm the Microsoft notification path and contact are documented and accessible.

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
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
