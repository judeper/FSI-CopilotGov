# Control 2.3: Conditional Access Policies for Copilot Workloads — Troubleshooting

Common issues and resolution steps for Conditional Access policies governing Copilot.

## Common Issues

### Issue 1: Legitimate Users Blocked from Copilot

- **Symptoms:** Users with compliant devices and proper credentials are unable to access Copilot, receiving access denial errors
- **Root Cause:** Device compliance status may be stale, the user may be in a conflicting CA policy, or named location definitions may not include their current network.
- **Resolution:**
  1. Check the user's sign-in log: Entra ID > Users > [User] > Sign-in logs
  2. Review which CA policy was applied and the failure reason
  3. Verify device compliance status in Intune: Devices > [Device] > Compliance
  4. If device compliance is stale, trigger a sync from the device
  5. Verify the user's network IP is included in trusted named locations if required

### Issue 2: Report-Only Mode Not Showing Expected Results

- **Symptoms:** Conditional Access policy in report-only mode does not show any matches in the CA insights workbook
- **Root Cause:** Report-only evaluation requires sign-in events to trigger the policy. If no users matching the policy conditions have signed in, no results appear. The insights workbook may also have a reporting delay.
- **Resolution:**
  1. Verify the policy conditions match the intended user group
  2. Perform a test sign-in as a user in the policy scope to generate an evaluation
  3. Check the sign-in log details for the "Report-only" column
  4. Allow 24-48 hours for the insights workbook to populate

### Issue 3: MFA Prompts Too Frequent

- **Symptoms:** Users complain about being prompted for MFA multiple times per day when using Copilot
- **Root Cause:** Sign-in frequency settings may be too aggressive, or MFA token lifetime may be too short. Multiple CA policies may each trigger MFA independently.
- **Resolution:**
  1. Review the sign-in frequency setting — 8 hours is recommended for standard use
  2. Check if multiple CA policies are each requiring MFA (consolidate if possible)
  3. Enable "Remember multi-factor authentication" for trusted devices
  4. Verify MFA token lifetime in Entra ID authentication methods settings
  5. Balance security and usability based on organizational risk tolerance

### Issue 4: Conditional Access Not Applying to Specific Copilot Features

- **Symptoms:** CA policy applies to Office applications but does not appear to evaluate when users access Copilot-specific features within those applications
- **Root Cause:** Copilot features run within the context of the host Office application. CA evaluation occurs at the application sign-in level, not at the individual feature level.
- **Resolution:**
  1. This is expected behavior — CA policies apply to the application, not to individual features
  2. If granular feature-level control is needed, use Copilot enablement settings (Admin Center > Copilot)
  3. Combine CA policies with DLP policies for content-level protection within Copilot
  4. Use Defender for Cloud Apps session controls for more granular session monitoring

### Issue 5: Emergency Access Account Locked Out

- **Symptoms:** Emergency (break-glass) access account is blocked by the Copilot CA policy
- **Root Cause:** Emergency access accounts may not have been properly excluded from the CA policy.
- **Resolution:**
  1. Immediately verify emergency accounts are excluded from all CA policies
  2. Use emergency access account best practices: exclude from all CA policies, use FIDO2 or certificate auth
  3. Document the exclusion in the CA policy configuration record
  4. Test emergency account access quarterly to verify it remains functional

## Diagnostic Steps

1. **Review sign-in logs:** Entra ID > Sign-in logs > filter by user and application
2. **Check policy evaluation:** Sign-in log > [Entry] > Conditional Access tab shows applied policies
3. **Verify device compliance:** Intune > Devices > [Device] > Compliance status
4. **Test from different conditions:** Try different devices, networks, and MFA states
5. **Review policy conflicts:** Export all CA policies and check for conflicting conditions

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
