# Control 2.2: Sensitivity Labels and Copilot Content Classification — Troubleshooting

Common issues and resolution steps for sensitivity label enforcement with Copilot.

## Common Issues

### Issue 1: Copilot Content Not Inheriting Source Labels

- **Symptoms:** Documents created by Copilot from labeled source documents do not inherit the source label, instead receiving the default label or no label
- **Root Cause:** Label inheritance for Copilot-generated content may depend on the specific Copilot feature and Office application version. Some features may not support automatic inheritance.
- **Resolution:**
  1. Verify the label policy has inheritance settings configured correctly
  2. Update Office applications to the latest version (label inheritance requires recent builds)
  3. If automatic inheritance is not supported, configure mandatory labeling so users must select a label
  4. Document the expected behavior for each Copilot feature and communicate to users

### Issue 2: Users Bypassing Mandatory Labeling

- **Symptoms:** Documents found in SharePoint without sensitivity labels despite mandatory labeling policy being enabled
- **Root Cause:** Mandatory labeling is enforced client-side and may not apply to all document creation paths. Files uploaded via sync client, migrated from other systems, or created by automated processes may bypass labeling.
- **Resolution:**
  1. Enable auto-labeling policies as a safety net for unlabeled content
  2. Configure a default label at the site level for documents without labels
  3. Run the unlabeled content detection script (Script 3) weekly to catch gaps
  4. Review upload paths and ensure all channels enforce labeling

### Issue 3: Label Conflicts with Multiple Source Documents

- **Symptoms:** When Copilot references multiple source documents with different sensitivity labels, the resulting content label is inconsistent or unexpected
- **Root Cause:** When multiple sources with different labels are combined, the inheritance behavior may default to the highest label or may be unpredictable depending on the Copilot feature.
- **Resolution:**
  1. Document the expected behavior: most restrictive label should win
  2. Test multi-source scenarios with different label combinations
  3. If behavior is inconsistent, configure mandatory labeling as the backup
  4. Train users to verify the label on Copilot-generated content that references multiple sources

### Issue 4: Encrypted Label Blocking Copilot Access

- **Symptoms:** Copilot reports it cannot access content or returns incomplete responses when source documents have encryption-enabled labels
- **Root Cause:** Labels with encryption restrict access to authorized users only. Copilot accesses content as the current user, so if the user has decryption rights, Copilot should work. If not, Copilot is correctly blocked.
- **Resolution:**
  1. Verify the user has the required rights for the encrypted content
  2. If the user should have access, check the encryption configuration and add the user to the authorized list
  3. If Copilot should not access the encrypted content, this is expected behavior — document it
  4. Consider using labels without encryption but with other protections (content marking, DLP) if Copilot access is required

### Issue 5: Label Analytics Showing Incomplete Data

- **Symptoms:** Label analytics reports in Purview show lower label counts than expected or data appears to be delayed
- **Root Cause:** Label analytics data has a reporting lag of up to 7 days. Additionally, label events from all workloads may not be aggregated in real-time.
- **Resolution:**
  1. Allow 7 days for data to fully populate in label analytics
  2. Cross-reference with audit log data for more current information
  3. Use PowerShell Script 2 for near-real-time label event monitoring
  4. Check service health for any Purview reporting delays

## Diagnostic Steps

1. **Check label policies:** Run Script 1 to verify policy configuration
2. **Review label events:** Run Script 2 for recent labeling activity
3. **Scan for unlabeled content:** Run Script 3 on key sites
4. **Test inheritance:** Create test scenarios with known source labels
5. **Verify client version:** Check Office client version supports label inheritance

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Label analytics reporting delays | Monitor and recheck after 7 days |
| **Medium** | Inconsistent label inheritance behavior | Information protection team |
| **High** | Mandatory labeling bypassed for sensitive content | Security Operations |
| **Critical** | Encrypted content accessible through Copilot without authorization | Security incident response |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Label configuration for Copilot
- [PowerShell Setup](powershell-setup.md) — Label management scripts
- [Verification & Testing](verification-testing.md) — Label validation procedures
