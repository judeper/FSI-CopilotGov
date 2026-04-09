# Control 2.1: DLP Policies for M365 Copilot Interactions — Troubleshooting

Common issues and resolution steps for DLP policies governing Copilot interactions. Control 2.1 uses two distinct DLP policy types — troubleshooting guidance distinguishes between label-based response blocking (Type 1) and SIT-based prompt blocking (Type 2) issues.

## Common Issues

### Issue 1: Attempting to Combine Both Policy Types in a Single Policy

- **Symptoms:** Administrator creates one DLP policy intending to cover both label-based response blocking and SIT-based prompt blocking, but only one mechanism appears to work (or neither does correctly)
- **Root Cause:** Label-based response blocking and SIT-based prompt blocking are architecturally distinct enforcement mechanisms that operate at different points in the Copilot interaction chain. They cannot be combined within a single DLP rule because they target different enforcement points: Type 1 blocks at the grounding/response phase, Type 2 blocks at the user prompt phase. However, they may exist as separate rules within the same policy.
- **Resolution:**
  1. Create two separate DLP rules (they may exist within the same policy or as separate policies):
     - Rule 1 (Type 1 — Label-Based): conditions use "Content contains sensitivity label" — blocks Copilot from including labeled content in responses
     - Rule 2 (Type 2 — SIT-Based): conditions use "Content contains sensitive information types" — blocks Copilot from processing prompts containing sensitive data
  2. Each rule must be independently configured, tested in simulation mode, and transitioned to enforcement separately
  3. Verify both policies appear in Purview > DLP > Policies as distinct entries

### Issue 2: DLP Policy Not Detecting Sensitive Data in Copilot

- **Symptoms:** Copilot interactions involving known sensitive data do not trigger DLP policy matches or policy tips
- **Root Cause (Type 1):** The label-based policy may not include the Copilot location, or the sensitivity label on the source document may not match the label specified in the policy condition.
- **Root Cause (Type 2):** The SIT-based prompt blocking policy may not include the Copilot location, the SIT definition may not match the data pattern typed in the prompt, or the confidence level may be set too high.
- **Resolution:**
  1. Verify both policies include Microsoft 365 Copilot as a monitored location (in Purview DLP policy scope)
  2. For Type 1: test the sensitivity label condition by opening the labeled document in Office apps and confirming the label is applied correctly
  3. For Type 2: test the SIT against the specific data pattern using Purview > Data Classification > Content Explorer
  4. Lower the confidence level threshold (try 75 instead of 85) and re-test
  5. Verify each policy is not in "off" mode — check both policy and rule enable status
  6. Allow 24 hours for policy propagation after any changes

### Issue 3: Default Copilot DLP Policy Not Visible

- **Symptoms:** The Microsoft-deployed default Copilot DLP policy does not appear in Purview > DLP > Policies, or match data is not populating in simulation mode
- **Root Cause:** The default policy (GA January 2026, MC1182689) should auto-appear for tenants with appropriate licenses. If it does not appear, the policy may not have been provisioned for the tenant, or the admin may lack visibility permissions.
- **Resolution:**
  1. Verify access via MAC > Copilot > Overview > Security tab (an alternative access point for the default policy)
  2. Confirm the tenant has Microsoft 365 E5 or E5 Compliance licenses (required for Copilot DLP)
  3. Wait 48-72 hours after license assignment for the default policy to provision
  4. If the policy does not appear, open a Microsoft support ticket referencing MC1182689
  5. In the interim, create a manual SIT-based prompt blocking policy (Type 2) covering the same SITs as the default policy

### Issue 4: Excessive False Positives Disrupting Users

- **Symptoms:** Users frequently receive DLP policy tips for content that is not actually sensitive, causing frustration and reduced Copilot productivity
- **Root Cause:** Sensitive information type patterns may be too broad, confidence levels too low, or custom SIT definitions may match non-sensitive data patterns.
- **Resolution:**
  1. Increase the minimum confidence level (recommend 85+ for FSI)
  2. Increase the minimum instance count for common patterns (e.g., require 3+ credit card matches, not 1)
  3. Refine custom sensitive information type patterns to be more specific
  4. Use "except if" conditions to exclude known false positive sources
  5. Review false positive samples to identify pattern improvements
  6. For Type 2 prompt blocking specifically: use the default policy simulation mode data to tune before enforcing

### Issue 5: DLP Policy Conflict with Other Policies

- **Symptoms:** Multiple DLP policies trigger simultaneously, resulting in confusing user notifications or unexpected blocking behavior
- **Root Cause:** Overlapping DLP policies with different actions create conflict scenarios. SharePoint DLP, Exchange DLP, and Copilot DLP policies may all evaluate the same content.
- **Resolution:**
  1. Review all DLP policies for scope overlap using `Get-DlpCompliancePolicy`
  2. Set explicit priority ordering so the most restrictive policy takes precedence
  3. Consolidate overlapping policies where possible (but do NOT consolidate Type 1 and Type 2 — keep them as separate policies)
  4. Use policy conditions to differentiate scope (e.g., by location, content type, or label)
  5. Test the combined effect of all policies on sample content

### Issue 6: DLP Alerts Not Being Reviewed

- **Symptoms:** DLP incident queue grows without review, policy matches accumulate but no remediation occurs
- **Root Cause:** Alert fatigue from high volume, unclear ownership of DLP incident review, or missing escalation procedures.
- **Resolution:**
  1. Assign specific team members or roles as DLP alert reviewers
  2. Set up alert severity thresholds — high confidence matches generate high-severity alerts
  3. Configure alert aggregation to reduce volume (digest rather than individual)
  4. Implement a triage process: auto-close known false positives, escalate true positives
  5. Define SLAs for alert review (critical: 4 hours, high: 24 hours, medium: 72 hours)

### Issue 7: Edge Browser DLP Not Applying to Copilot

- **Symptoms:** Copilot interactions accessed through Microsoft Edge browser do not trigger DLP policies that work correctly in native M365 apps
- **Root Cause:** Edge browser DLP requires Endpoint DLP configuration and a supported Edge browser version. If Edge is not configured as a monitored browser in Endpoint DLP settings, browser-based Copilot interactions will not be covered.
- **Resolution:**
  1. Navigate to Purview > Data loss prevention > Endpoint DLP settings
  2. Verify Microsoft Edge is listed as a monitored browser and the setting is enabled
  3. Confirm Edge browser version meets minimum requirements (check Purview documentation for supported versions)
  4. Verify endpoint devices have the Purview client extension installed (required for browser-based DLP)
  5. Allow 24 hours for Endpoint DLP policy changes to propagate to managed devices

### Issue 8: Policy Changes Not Taking Effect

- **Symptoms:** After modifying a DLP policy or rule, the changes do not appear to take effect in Copilot interactions
- **Root Cause:** DLP policy changes can take up to 24 hours to propagate across all workloads. Cached policy states on client applications may also delay enforcement.
- **Resolution:**
  1. Wait 24 hours after making policy changes before testing
  2. Verify the change was saved: `Get-DlpComplianceRule -Policy <name>` and check rule conditions
  3. Have test users sign out and back in to refresh policy cache
  4. If changes still do not take effect, deactivate and reactivate the policy

## Diagnostic Steps

1. **Verify both policy types exist:** `Get-DlpCompliancePolicy | Where-Object { $_.Name -match "Copilot" } | Select Name, Mode, Enabled`
2. **Check rule configuration for each policy type:** `Get-DlpComplianceRule -Policy <name>`
3. **Review recent incidents by policy type:** Run Script 4 for the past 7 days and filter by policy name
4. **Locate default policy:** Check MAC > Copilot > Overview > Security tab for the Microsoft-deployed default policy
5. **Test with known data:** Create a test prompt with known SIT patterns; create a test document with a known label
6. **Check audit logs:** Search for DLP events in the unified audit log
7. **Use Security Copilot policy explanations:** In the Purview DLP console, use AI-powered policy explanations to review complex rule logic and verify both policy types are configured as intended

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | False positive pattern identified in either policy type | DLP policy tuning team |
| **Medium** | Policy type not detecting known sensitive data | Information protection team |
| **High** | DLP bypassed — sensitive data exposed through Copilot prompt or response | Security Operations and CISO |
| **Critical** | All DLP policies disabled or non-functional | Security Operations — incident response |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — DLP policy configuration for both policy types
- [PowerShell Setup](powershell-setup.md) — DLP automation scripts for both policy types
- [Verification & Testing](verification-testing.md) — DLP validation procedures
