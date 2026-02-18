# Control 2.3: Conditional Access Policies for Copilot Workloads — Troubleshooting

Common issues and resolution steps for Conditional Access policies governing Copilot.

## Common Issues

### Issue 1: CA Policy Not Applying to Copilot Traffic

- **Symptoms:** Copilot access is not being evaluated by the expected CA policy; sign-in logs show Copilot traffic evaluated by the wrong policy or no policy
- **Root Cause:** The CA policy may be targeting an incorrect app ID. The wrong Enterprise Copilot Platform app ID (`fb8d773d-7ef4-4c2f-a801-2a5e1e8e1098`) is a known transcription error — if this appears in your policies, CA will not enforce against Copilot.
- **Resolution:**
  1. Verify the policy targets the correct app ID: `fb8d773d-7ef8-4ec0-a117-179f88add510`
  2. Run Script 1 (App ID Audit) from the PowerShell playbook to identify all affected policies
  3. Update the target app ID in any misconfigured policies
  4. Deploy updated policies in report-only mode first, then switch to enforcement
  5. Confirm Copilot sign-in events now show the correct policy being applied in sign-in logs

### Issue 2: Unexpected Enforcement After March 2026

- **Symptoms:** After March 27, 2026, users experience unexpected MFA prompts or blocks when accessing Copilot — particularly users who previously accessed without issue
- **Root Cause:** The March 2026 CA enforcement change removes the bypass path in "All resources + exclusion" policies. Users who were previously excluded from enforcement are now subject to MFA and device compliance requirements.
- **Resolution:**
  1. Check sign-in logs for the specific CA policy that is now enforcing
  2. Identify whether the user's Copilot access was previously relying on a resource exclusion
  3. If the enforcement is correct, assist the user in meeting the policy requirements (MFA setup, device enrollment)
  4. If the enforcement is unexpected, review whether the policy needs restructuring
  5. Refer to the March 2026 enforcement audit documentation to confirm the intended post-enforcement state

### Issue 3: Legitimate Users Blocked from Copilot

- **Symptoms:** Users with compliant devices and proper credentials are unable to access Copilot, receiving access denial errors
- **Root Cause:** Device compliance status may be stale, the user may be in a conflicting CA policy, or named location definitions may not include their current network.
- **Resolution:**
  1. Check the user's sign-in log: Microsoft Entra admin center > Users > [User] > Sign-in logs
  2. Review which CA policy was applied and the failure reason
  3. Verify device compliance status in Intune: Devices > [Device] > Compliance
  4. If device compliance is stale, trigger a sync from the device
  5. Verify the user's network IP is included in trusted named locations if required

### Issue 4: Report-Only Mode Not Showing Expected Results

- **Symptoms:** Conditional Access policy in report-only mode does not show any matches in the CA insights workbook
- **Root Cause:** Report-only evaluation requires sign-in events to trigger the policy. If no users matching the policy conditions have signed in, no results appear. The insights workbook may also have a reporting delay.
- **Resolution:**
  1. Verify the policy conditions match the intended user group
  2. Perform a test sign-in as a user in the policy scope to generate an evaluation
  3. Check the sign-in log details for the "Report-only" column
  4. Allow 24-48 hours for the insights workbook to populate

### Issue 5: MFA Prompts Too Frequent

- **Symptoms:** Users complain about being prompted for MFA multiple times per day when using Copilot
- **Root Cause:** Sign-in frequency settings may be too aggressive, or MFA token lifetime may be too short. Multiple CA policies may each trigger MFA independently.
- **Resolution:**
  1. Review the sign-in frequency setting — 8 hours is recommended for standard use
  2. Check if multiple CA policies are each requiring MFA (consolidate if possible)
  3. Enable "Remember multi-factor authentication" for trusted devices
  4. Verify MFA token lifetime in Entra ID authentication methods settings
  5. Balance security and usability based on organizational risk tolerance

### Issue 6: Conditional Access Not Applying to Specific Copilot Features

- **Symptoms:** CA policy applies to Office applications but does not appear to evaluate when users access Copilot-specific features within those applications
- **Root Cause:** Copilot features run within the context of the host Office application. CA evaluation occurs at the application sign-in level, not at the individual feature level.
- **Resolution:**
  1. This is expected behavior — CA policies apply to the application, not to individual features
  2. If granular feature-level control is needed, use Copilot enablement settings in the Microsoft 365 Admin Center
  3. Combine CA policies with DLP policies for content-level protection within Copilot
  4. Use Defender for Cloud Apps session controls for more granular session monitoring

### Issue 7: Adaptive Protection Not Triggering CA Enforcement

- **Symptoms:** A user has an elevated IRM risk level, but CA policies are not restricting their Copilot access
- **Root Cause:** The Adaptive Protection integration between IRM and CA requires both systems to be properly configured. The CA policy must be configured to evaluate IRM risk levels, not just standard Entra ID Protection risk.
- **Resolution:**
  1. Verify Adaptive Protection is enabled in Microsoft Purview > Insider Risk Management > Adaptive Protection settings
  2. Confirm the CA policy is configured to evaluate the IRM-sourced user risk signal (not only the standard Entra ID Protection risk)
  3. Check the evaluation interval — IRM risk level changes may take up to the configured evaluation window to propagate to CA
  4. Review sign-in logs for the affected user to confirm which risk signal was evaluated
  5. Test by manually reviewing the IRM risk dashboard to confirm the user's risk level shows as elevated

### Issue 8: Emergency Access Account Locked Out

- **Symptoms:** Emergency (break-glass) access account is blocked by the Copilot CA policy
- **Root Cause:** Emergency access accounts may not have been properly excluded from the CA policy.
- **Resolution:**
  1. Immediately verify emergency accounts are excluded from all CA policies
  2. Use emergency access account best practices: exclude from all CA policies, use FIDO2 or certificate auth
  3. Document the exclusion in the CA policy configuration record
  4. Test emergency account access quarterly to verify it remains functional

## Diagnostic Steps

1. **Review sign-in logs:** Microsoft Entra admin center > Sign-in logs > filter by user and application
2. **Check policy evaluation:** Sign-in log > [Entry] > Conditional Access tab shows applied policies
3. **Verify app ID:** Run Script 1 to confirm correct Enterprise Copilot Platform app ID in all policies
4. **Verify device compliance:** Intune > Devices > [Device] > Compliance status
5. **Test from different conditions:** Try different devices, networks, and MFA states
6. **Review policy conflicts:** Export all CA policies and check for conflicting conditions

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Individual user access issues with known resolution | IT Help Desk |
| **Medium** | Multiple users blocked by policy misconfiguration | Identity and Access Management team |
| **High** | Emergency access account locked out | Security Operations immediately |
| **Critical** | CA policies non-functional or bypassed | Security incident response team |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — CA policy configuration
- [PowerShell Setup](powershell-setup.md) — CA policy management scripts
- [Verification & Testing](verification-testing.md) — CA validation procedures
