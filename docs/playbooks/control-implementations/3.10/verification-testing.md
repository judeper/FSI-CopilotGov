# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Verification & Testing

Test cases and evidence collection procedures to validate privacy controls for consumer financial information in Copilot interactions, including the incident response program requirements from the Reg S-P amendments proposed in 2023 and adopted by the SEC in May 2024 (Release No. 34-100155).

## Test Cases

### Test 1: Copilot DLP Policy Plane Verification

- **Objective:** Verify that the policy targets the documented Copilot location and enforcement plane.
- **Steps:**
  1. Run:
     ```powershell
     Connect-IPPSSession
     $locationId = "470f2276-e011-4e9d-a6ec-20768be3a4b0"
     $matches = @(Get-DlpCompliancePolicy | Where-Object {
         $_.EnforcementPlanes -contains "CopilotExperiences" -and
         [string]$_.Locations -match [regex]::Escape($locationId)
     })
     if (-not $matches) {
         throw "No policy targets the Microsoft 365 Copilot and Copilot Chat location."
     }
     $matches | Format-List Name, Enabled, Mode, Locations, EnforcementPlanes
     ```
  2. In **Purview > Data Loss Prevention > Policies**, confirm that each matching policy uses the **Microsoft 365 Copilot and Copilot Chat** location.
  3. Confirm that the policy was created from the **Custom** template and that other locations are disabled.
- **Expected Result:** At least one policy includes location GUID `470f2276-e011-4e9d-a6ec-20768be3a4b0` and `CopilotExperiences`.
- **Evidence:** Policy screenshot and PowerShell output showing `Mode`, `Locations`, and `EnforcementPlanes`. Don't require a top-level `Workload` property; `Workload: "Applications"` is inside the locations JSON.

### Test 2: Sensitivity-Label Exclusion

- **Objective:** Validate the supported Copilot action for labeled source files and emails.
- **Steps:**
  1. Create a synthetic test file or an email sent on or after January 1, 2025, apply a sensitivity label targeted by the Copilot DLP rule, and give the test user permission to access it. Don't use a calendar invite, which isn't supported.
  2. Ask Copilot to summarize or use that item.
  3. Allow up to four hours after a policy change before testing.
  4. Review **Purview > Data Loss Prevention > Alerts** and **Purview > Audit > Copilot activities**.
- **Expected Result:** Copilot doesn't use the labeled item's content in the response. The item can still appear as a citation.
- **Evidence:** Source label, Copilot result, applicable DLP alert, and `CopilotInteraction` audit record.

### Test 3: Typed-Prompt, Web-Search, and External-Email Actions

- **Objective:** Validate each configured SIT action and document the direct-upload limitation.
- **Steps:**
  1. Type synthetic NPI directly into a Copilot prompt. Where **Processing prompts** has reached the tenant, verify that Copilot doesn't return a response.
  2. In a separate test of **Performing Web Searches**, type synthetic NPI and request current web information. Verify that external web search is blocked while permitted internal grounding can continue.
  3. If the preview **Email is received from > External users** rule is configured, send a synthetic message from a domain outside the tenant's accepted domains. Verify Copilot excludes the email from grounding, summarization, and citation; the condition evaluates sender metadata rather than the body.
  4. Upload an **unlabeled** synthetic file that contains a test SIT while typing a neutral prompt that doesn't contain the SIT.
  5. Confirm that the SIT prompt rule doesn't inspect the uploaded file's contents. Delete the test artifacts.
- **Expected Result:** Tenant-available typed-prompt, web-search, and external-email actions behave as configured. The direct-upload test demonstrates the documented coverage gap rather than being recorded as a policy failure.
- **Evidence:** Screenshots of each result, policy/rule configuration, alert evidence where configured, and the documented direct-upload exception.

### Test 4: Information Barrier Enforcement

- **Objective:** Confirm that information barriers prevent Copilot from surfacing NPI across business unit boundaries
- **Steps:**
  1. Create test documents containing consumer financial data in a restricted segment's SharePoint site.
  2. Have a user from a different segment use Copilot to search for or reference that content.
  3. Verify that Copilot does not surface the restricted content in its responses.
  4. Separately document that Information Barriers don't support the SharePoint Embedded content used by Copilot Pages and Copilot Notebooks.
- **Expected Result:** Information barriers prevent cross-segment NPI exposure through supported SharePoint sources. Pages and Notebooks are governed through their available admin policies when the SharePoint Embedded limitation isn't acceptable.
- **Evidence:** Copilot result for the supported source and the documented Pages/Notebooks disposition.

### Test 5: Sensitivity Label Protection for NPI Documents

- **Objective:** Validate that documents containing NPI are protected with appropriate sensitivity labels
- **Steps:**
  1. Create a document containing consumer financial data.
  2. Apply or verify auto-application of the appropriate sensitivity label.
  3. Confirm the label enforces encryption and access restrictions.
  4. Test that Copilot interactions with the document respect label protections.
- **Expected Result:** NPI documents are labeled, encrypted, and Copilot respects label-based access controls.
- **Evidence:** Document properties showing label and encryption status.

### Test 6: Incident Response Program Verification (Rule 248.30(a)(4))

- **Objective:** Verify that the written incident response program covers Copilot-related NPI incidents and includes the required notification procedures
- **Steps:**
  1. Review the firm's written incident response program (IRP) for Copilot NPI coverage.
  2. Confirm the IRP is written (not informal) and includes: Copilot-specific incident scenarios, severity classification, escalation paths, containment steps, and notification procedures.
  3. Verify the service provider notification receipt and escalation procedure is documented (SEC Rule 248.30(a)(3)). For Microsoft-determined service incidents, confirm designated tenant administrator contacts are current and Microsoft 365 Service health is monitored.
  4. Verify the 30-day customer notification timeline is documented.
  5. Confirm a named individual is responsible for receiving, assessing, and escalating service provider notifications.
- **Expected Result:** Written IRP exists, covers Copilot scenarios, and documents both the 72-hour vendor notification and 30-day customer notification procedures.
- **Evidence:** IRP document with Copilot section; service provider notification intake procedure; tenant contact and Service health monitoring evidence; responsible party assignment.

### Test 7: Incident Response Simulation — NPI Exposure via Copilot

- **Objective:** Simulate a Copilot NPI exposure event to test the incident response program and verify the 72-hour notification window is achievable
- **Steps:**
  1. Run a tabletop exercise scenario: "Copilot Chat surfaced client account numbers to a user without appropriate permissions due to a permission misconfiguration. The exposure was detected via a DLP alert."
  2. Walk through the IRP steps: detection confirmation → severity classification → internal escalation → service provider notification intake and assessment → customer notification decision workflow.
  3. Time the exercise and test the institution's documented service provider notification and customer notification procedures.
  4. Identify any gaps in the notification chain (for example, stale tenant administrator contacts or an unmonitored Service health dashboard).
  5. Document exercise outcomes and any remediation items.
- **Expected Result:** Tabletop exercise completed with documented outcome; notification chain is achievable within the 72-hour and 30-day windows; gaps identified and assigned for remediation.
- **Evidence:** Exercise facilitation notes and outcome documentation; gap remediation log.

### Test 8: Privacy Incident Response Alert Workflow

- **Objective:** Verify that NPI-related DLP incidents trigger the appropriate automated alert workflow
- **Steps:**
  1. Trigger a DLP incident involving consumer financial data (test environment).
  2. Verify the alert appears under **Purview > Data Loss Prevention > Alerts**.
  3. Confirm the compliance team and Privacy Officer receive the configured notification.
  4. Walk through the incident investigation and resolution process in Purview.
- **Expected Result:** DLP incidents trigger automated notifications, are logged for investigation, and can be resolved.
- **Evidence:** DLP alert record and notification confirmation.

### Test 9: Copilot Pages and Notebooks Controls

- **Objective:** Verify the controls and documented limitations for SharePoint Embedded content.
- **Steps:**
  1. Create synthetic content in a Copilot Page and a Copilot Notebook under a test account.
  2. Confirm both artifacts are stored in the user's SharePoint Embedded container.
  3. Verify DLP and policy-tip behavior for the test content.
  4. Verify that the Copilot Page can use a sensitivity label and record that Copilot Notebooks don't have a container sensitivity label.
  5. Record that Information Barriers don't support SharePoint Embedded content and verify the organization's admin-policy disposition.
- **Expected Result:** Supported DLP and Page-label behavior is evidenced; the Notebook label and Information Barriers limitations are explicitly accepted or creation is disabled for the affected users.
- **Evidence:** SharePoint Embedded container evidence, Page label, DLP result, and admin-policy screenshot.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| DLP policy configuration | Purview portal | Screenshot | With control documentation |
| DLP alert records | Purview > Data Loss Prevention > Alerts | CSV export or screenshot | 7 years |
| Copilot interaction events | Purview > Audit > Copilot activities | CSV export | 7 years |
| Sensitive AI activity review | Purview > Solutions > DSPM > Discover > Activity explorer | Export or screenshot | With control documentation |
| Direct-upload limitation test | Copilot test session | Screenshot | With control documentation |
| Information barrier test results | Copilot response | Screenshot | With control documentation |
| Pages and Notebooks limitation review | SharePoint Embedded and admin policy evidence | Screenshot | With control documentation |
| Privacy impact assessment | Assessment document | PDF | 7 years |
| Written IRP with Copilot section | IRP document | PDF | 7 years (updated annually) |
| 72-hour notification procedure | IRP or standalone document | PDF | 7 years |
| Tabletop exercise documentation | Exercise records | PDF | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Reg S-P Rule 248.30(a)(3) | 72-hour vendor notification for unauthorized NPI access | Test 6 and 7 verify documented procedure and achievable window |
| SEC Reg S-P Rule 248.30(a)(4) | Written incident response program | Test 6 verifies existence and completeness of written IRP |
| SEC Reg S-P Rule 30 | Safeguard customer records | Supports compliance with NPI safeguarding in AI interactions |
| GLBA Title V | Financial privacy | Helps meet privacy requirements for consumer financial information |
| GLBA §501(b) | Safeguards provision for NPI | Supports requirements for protecting customer information at banks and broker-dealers (statutory basis for SEC Reg S-P safeguards; the FTC Safeguards Rule is a separate implementing regulation outside SEC jurisdiction) |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for privacy control issues
- Proceed to [Control 3.11](../3.11/portal-walkthrough.md) for record keeping compliance
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
