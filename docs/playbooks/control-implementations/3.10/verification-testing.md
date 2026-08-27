# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Verification & Testing

Test cases and evidence collection procedures to validate privacy controls for consumer financial information in Copilot interactions, including the incident response program requirements from the Reg S-P amendments proposed in 2023 and adopted by the SEC in May 2024 (Release No. 34-100155).

## Test Cases

### Test 1: DLP Detection of NPI in Copilot Prompts and Policy Configuration Verification

- **Objective:** Verify that DLP policies detect nonpublic personal information **entered as Copilot prompt text**, and that the exact expected policy is enabled on the Copilot location and enforcement plane with both expected rules and their alert configuration
- **Steps:**
  1. Using a test account, **type** test SSN and account number data directly into a Copilot prompt. Do not attach the test data as an uploaded file — uploaded file contents are not scanned by this control, so a file-based test proves nothing.
  2. Submit the prompt and observe whether Copilot processing is restricted.
  3. Verify that the DLP policy tip appears warning about NPI content. During the SIT-in-prompts preview, user messaging in Word, Excel, and PowerPoint may not clearly attribute the block to organizational policy; the prompt is still restricted.
  4. Run the fail-closed verification. Every check throws; the success line prints only if all checks pass:
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
             throw "Fail closed: '$Subject' does not expose a '$Name' property in this tenant. Verify '$Subject' manually in the Microsoft Purview portal (Data loss prevention > Policies) and record screenshots as the evidence."
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
  5. Confirm that high-volume NPI **in prompt text** triggers the documented Copilot content-processing restriction.
- **Expected Result:** DLP detects NPI typed into the prompt, displays policy tips or restricts Copilot processing, and the verification script prints its single success line with no exception raised.
- **Evidence:** Screenshots of DLP policy tips/content-processing restrictions; PowerShell transcript showing the verification success line; if any check stopped the script, the portal screenshots described in the throw message instead.

> **Documented Copilot DLP limitations (read before relying on this control):** In the **Microsoft 365 Copilot and Copilot Chat** location, sensitive information type (SIT) enforcement evaluates **the text a user types into the prompt**. The two documented SIT actions are **Prevent Copilot from processing content > Processing prompts** and **> Performing Web Searches**. Microsoft does not document a DLP action that inspects or blocks the text of a **generated Copilot response**; sensitive data in responses can be *observed* after the fact (DSPM / Activity explorer **AI activities**, Audit, eDiscovery) but is not blocked by this control. DLP also can't scan the contents of files uploaded directly into a prompt — only typed prompt text is checked. SIT-based prompt blocking is in preview and rolling out. The sensitivity label condition covers emails sent on or after January 1, 2025; calendar invites and Admin units are not supported. Policy updates can take up to four hours to take effect in the Copilot experience.

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

- **Objective:** Verify that NPI-related DLP rule matches produce the alert and email notification the control promises, and that the alert can be investigated end to end
- **Steps:**
  1. Confirm the alert is defined **on the rule**: in Microsoft Purview > Data loss prevention > Policies > FSI-RegSP-Copilot-Privacy-Protection, open each rule and confirm the **Incident reports** section shows the alert toggle on, the expected severity level (Medium / High), and the Privacy Officer plus compliance team as email alert recipients. The PowerShell equivalent is the `GenerateAlert`, `GenerateIncidentReport`, and `ReportSeverityLevel` check in Test 1.
  2. Trigger a DLP rule match by typing consumer financial test data into a Copilot prompt (test environment).
  3. Verify the alert appears on the DLP Alerts dashboard (Microsoft Purview > Data loss prevention > Alerts).
  4. Confirm the compliance team and Privacy Officer received the alert email generated by the rule.
  5. Cross-check the match in Activity explorer **AI activities** (Workload `Copilot`, activity `DLPRuleMatch` / `DLPRuleEnforce`) and confirm the `PolicyName` and `RuleName` match the expected rule.
  6. Walk through the incident investigation and resolution process in Purview.
- **Expected Result:** The rule's own alert configuration produces a dashboard alert and an email to the configured recipients; the match is visible in Activity explorer with the expected policy and rule names.
- **Evidence:** Screenshot of the rule's **Incident reports** configuration; DLP alert detail; notification email header (redacted); Activity explorer export row.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| DLP policy and rule configuration (including Incident reports) | Purview portal | Screenshot | With control documentation |
| Fail-closed policy verification output | Security & Compliance PowerShell transcript | Text | With control documentation |
| Copilot interaction audit records (metadata) | Unified audit log (`RecordType CopilotInteraction`) | CSV export | 7 years |
| Copilot DLP rule-match records | Activity explorer / DSPM **AI activities** (`Export-ActivityExplorerData`) | JSON or CSV export | 7 years |
| DLP alerts | Purview > Data loss prevention > Alerts | Screenshot / export | 7 years |
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
