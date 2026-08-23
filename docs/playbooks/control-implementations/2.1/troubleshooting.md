# Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions — Troubleshooting

Common issues and resolution steps for the supported Microsoft 365 Copilot and Copilot Chat DLP condition/action patterns.

## Common Issues

### Issue 1: Sensitivity-Label and SIT Conditions Combined in One Rule

- **Symptoms:** Only one intended action appears or the rule can't be saved.
- **Root Cause:** Sensitivity-label and sensitive-information-type conditions can't be combined within one Copilot DLP rule.
- **Resolution:**
  1. Use a separate sensitivity-label rule with **Prevent Copilot from processing content**.
  2. Use separate SIT rules for **Processing prompts** and **Performing Web Searches**, as applicable.
  3. The rules can be in one Custom policy, but the policy must use only the **Microsoft 365 Copilot and Copilot Chat** location.
  4. Test each rule in simulation mode before enforcement.

### Issue 2: Policy Has Unsupported Locations or Scope

- **Symptoms:** The policy can't be created, a Copilot location error appears, or enforcement doesn't match the design.
- **Root Cause:** The Copilot location can't be combined with other DLP policy locations, and it doesn't support administrative units.
- **Resolution:**
  1. Confirm `Locations` contains `470f2276-e011-4e9d-a6ec-20768be3a4b0`.
  2. Confirm all other policy locations are disabled.
  3. Confirm `EnforcementPlanes` contains `CopilotExperiences`.
  4. Use the supported tenant or user/group inclusion model rather than an administrative unit.

### Issue 3: Label-Based Rule Doesn't Exclude Source Content

- **Symptoms:** Copilot uses content from a file or email carrying a matching sensitivity label.
- **Root Cause:** The source label doesn't match the rule, the user isn't in scope, the policy/rule isn't enabled, or the update hasn't propagated.
- **Resolution:**
  1. Confirm the label on the source item and the label GUID in the rule.
  2. Confirm the policy and rule modes and the user's scope.
  3. Allow up to four hours for Copilot policy changes to apply.
  4. Retest in a new Copilot interaction.
  5. Don't treat a remaining citation as failed enforcement; Microsoft documents that the item can remain visible as a citation while its content isn't processed.

### Issue 4: Typed-Prompt Rule Doesn't Appear or Trigger

- **Symptoms:** The **Processing prompts** action isn't present or a matching typed prompt isn't blocked.
- **Root Cause:** Prompt blocking is in preview and rolling out, or the SIT/confidence configuration doesn't match the typed text.
- **Resolution:**
  1. Confirm the feature has reached the tenant.
  2. Test the exact synthetic value with `Get-DlpSensitiveInformationType` and the relevant Purview classifier tools.
  3. Confirm the value is typed directly into the prompt.
  4. Review the rule's SIT, confidence, scope, and mode.
  5. Allow up to four hours after a policy change before retesting.

### Issue 5: Uploaded File Content Doesn't Trigger an SIT Prompt/Web Rule

- **Symptoms:** A directly uploaded file contains a configured SIT, but the prompt or web-search rule doesn't trigger.
- **Root Cause:** This is a documented limitation. Copilot DLP doesn't scan the contents of files uploaded directly into prompts; it evaluates typed prompt text.
- **Resolution:**
  1. Don't represent prompt/web SIT rules as upload-content inspection.
  2. Validate source permissions and sensitivity-label source exclusion.
  3. Evaluate separately documented Endpoint/browser DLP controls for the approved upload activity, device, browser, and file type.
  4. Record the limitation and compensating controls in test evidence.

### Issue 6: Web-Search Rule Appears Ineffective

- **Symptoms:** The expected difference between benign and matching prompts isn't visible.
- **Root Cause:** Web search might already be disabled by Cloud Policy, the prompt might not match the SIT, or the tester might be looking for a full response block rather than only a web-search restriction.
- **Resolution:**
  1. Check **Allow web search in Copilot** in the Microsoft 365 Apps admin center (`config.office.com`).
  2. Use an approved benign prompt to confirm the test user can receive web citations.
  3. Retest with an approved synthetic SIT value typed into the prompt.
  4. Confirm the matching prompt has no external web search or web citation.
  5. Internal Microsoft 365 grounding can continue; don't classify an internal answer as failed web-search enforcement.

### Issue 6a: External-Email Rule Doesn't Exclude a Message

- **Symptoms:** A configured external-email rule is present, but Copilot still uses the message.
- **Root Cause:** The preview might not have reached the tenant, the sender domain might be in the tenant's accepted domains, or the test expects email-body SIT scanning.
- **Resolution:**
  1. Confirm preview availability.
  2. Compare the sender domain with the tenant's accepted domains.
  3. Confirm the rule uses **Email is received from > External users** with **Prevent Copilot from processing content**.
  4. Retest after up to four hours.
  5. Expect matching email to be excluded from grounding, summarization, and citation. The condition evaluates sender metadata, not body content.

### Issue 7: Alerts or Detailed AI Activity Aren't Visible

- **Symptoms:** A tested rule acts, but the reviewer can't find the alert or detailed interaction.
- **Root Cause:** The reviewer may be using the wrong portal view, the alert isn't configured, or required content-viewer permissions are missing.
- **Resolution:**
  1. Review **Purview > Data Loss Prevention > Alerts**.
  2. Review **Purview > Solutions > DSPM > Discover > Activity explorer > AI activities**.
  3. Confirm the rule's alert configuration.
  4. Assign only the Microsoft-documented roles required for the view. Prompt/response bodies require additional Content Explorer Content Viewer and Data Security AI Content Viewer permissions.

### Issue 8: Policy Changes Haven't Taken Effect

- **Symptoms:** A saved Copilot policy or rule change isn't reflected in testing.
- **Root Cause:** Copilot DLP policy updates can take up to four hours to apply.
- **Resolution:**
  1. Verify the saved policy with `Get-DlpCompliancePolicy -Identity <name>`.
  2. Verify rules with `Get-DlpComplianceRule -Policy <name>`.
  3. Wait up to four hours and retest in a new interaction.
  4. If the documented window has elapsed, gather policy/rule output and open a Microsoft support case.

## Diagnostic Steps

1. **Check the policy:** `Get-DlpCompliancePolicy -Identity <name> | Format-List Name,Mode,Enabled,Locations,EnforcementPlanes`
2. **Check rules:** `Get-DlpComplianceRule -Policy <name> | Format-Table Name,Disabled,Priority`
3. **Check the Copilot location:** Search the string form of `Locations` for `470f2276-e011-4e9d-a6ec-20768be3a4b0`
4. **Check SITs:** Use `Get-DlpSensitiveInformationType`; don't substitute `Get-DlpSensitiveInformationTypeRulePackage`, which returns packages
5. **Check DLP evidence:** Review DLP Alerts and DSPM AI activities
6. **Test each documented enforcement path:** Labeled source content, typed-prompt blocking if available, web-search restriction, external-email exclusion if available, and the direct-upload limitation

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | False-positive pattern identified | DLP policy tuning team |
| **Medium** | A tenant-available supported action doesn't match its test case after propagation | Information protection team |
| **High** | Sensitive data path bypasses the documented and approved controls | Security Operations and CISO |
| **Critical** | Applicable DLP policies are disabled or non-functional | Security Operations — incident response |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — supported DLP configuration
- [PowerShell Setup](powershell-setup.md) — documented policy and label-rule automation
- [Verification & Testing](verification-testing.md) — supported-action test procedures
- Back to [Control 2.1](../../../controls/pillar-2-security/2.1-dlp-policies-for-copilot.md)
