# Control 2.1: DLP Policies for M365 Copilot Interactions — Troubleshooting

Common issues and resolution steps for DLP policies governing Copilot interactions.

## Common Issues

### Issue 1: DLP Policy Not Detecting Sensitive Data in Copilot

- **Symptoms:** Copilot interactions involving known sensitive data do not trigger DLP policy matches or policy tips
- **Root Cause:** The DLP policy may not include the Copilot location, the sensitive information type definition may not match the data pattern, or the confidence level may be set too high.
- **Resolution:**
  1. Verify the policy scope includes Microsoft 365 Copilot as a monitored location
  2. Test the sensitive information type against the specific data pattern using Purview > Data Classification > Content Explorer
  3. Lower the confidence level threshold (try 75 instead of 85) and re-test
  4. Verify the policy is not in "off" mode — check both policy and rule enable status
  5. Allow 24 hours for policy propagation after any changes

### Issue 2: Excessive False Positives Disrupting Users

- **Symptoms:** Users frequently receive DLP policy tips for content that is not actually sensitive, causing frustration and reduced Copilot productivity
- **Root Cause:** Sensitive information type patterns may be too broad, confidence levels too low, or custom SIT definitions may match non-sensitive data patterns.
- **Resolution:**
  1. Increase the minimum confidence level (recommend 85+ for FSI)
  2. Increase the minimum instance count for common patterns (e.g., require 3+ credit card matches, not 1)
  3. Refine custom sensitive information type patterns to be more specific
  4. Use "except if" conditions to exclude known false positive sources
  5. Review false positive samples to identify pattern improvements

### Issue 3: DLP Policy Conflict with Other Policies

- **Symptoms:** Multiple DLP policies trigger simultaneously, resulting in confusing user notifications or unexpected blocking behavior
- **Root Cause:** Overlapping DLP policies with different actions create conflict scenarios. SharePoint DLP, Exchange DLP, and Copilot DLP policies may all evaluate the same content.
- **Resolution:**
  1. Review all DLP policies for scope overlap using `Get-DlpCompliancePolicy`
  2. Set explicit priority ordering so the most restrictive policy takes precedence
  3. Consolidate overlapping policies where possible
  4. Use policy conditions to differentiate scope (e.g., by location, content type, or label)
  5. Test the combined effect of all policies on sample content

### Issue 4: DLP Alerts Not Being Reviewed

- **Symptoms:** DLP incident queue grows without review, policy matches accumulate but no remediation occurs
- **Root Cause:** Alert fatigue from high volume, unclear ownership of DLP incident review, or missing escalation procedures.
- **Resolution:**
  1. Assign specific team members or roles as DLP alert reviewers
  2. Set up alert severity thresholds — high confidence matches generate high-severity alerts
  3. Configure alert aggregation to reduce volume (digest rather than individual)
  4. Implement a triage process: auto-close known false positives, escalate true positives
  5. Define SLAs for alert review (critical: 4 hours, high: 24 hours, medium: 72 hours)

### Issue 5: Policy Changes Not Taking Effect

- **Symptoms:** After modifying a DLP policy or rule, the changes do not appear to take effect in Copilot interactions
- **Root Cause:** DLP policy changes can take up to 24 hours to propagate across all workloads. Cached policy states on client applications may also delay enforcement.
- **Resolution:**
  1. Wait 24 hours after making policy changes before testing
  2. Verify the change was saved: `Get-DlpComplianceRule -Policy <name>` and check rule conditions
  3. Have test users sign out and back in to refresh policy cache
  4. If changes still do not take effect, deactivate and reactivate the policy

## Diagnostic Steps

1. **Verify policy status:** `Get-DlpCompliancePolicy | Select Name, Mode, Enabled`
2. **Check rule configuration:** `Get-DlpComplianceRule -Policy <name>`
3. **Review recent incidents:** Run Script 3 for the past 7 days
4. **Test with known data:** Create a test document with known sensitive patterns
5. **Check audit logs:** Search for DLP events in the unified audit log

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | False positive pattern identified | DLP policy tuning team |
| **Medium** | Policy not detecting known sensitive data | Information protection team |
| **High** | DLP bypassed — sensitive data exposed through Copilot | Security Operations and CISO |
| **Critical** | All DLP policies disabled or non-functional | Security Operations — incident response |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — DLP policy configuration
- [PowerShell Setup](powershell-setup.md) — DLP automation scripts
- [Verification & Testing](verification-testing.md) — DLP validation procedures
