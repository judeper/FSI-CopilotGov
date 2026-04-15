# Control 2.8: Encryption (Data in Transit and at Rest) — Troubleshooting

Common issues and resolution steps for encryption controls.

## Common Issues

### Issue 1: Customer Key DEP in Error State

- **Symptoms:** `Get-DataEncryptionPolicy` shows DEP in "Error" or "PendingActivation" state
- **Root Cause:** Key vault access issues, expired keys, or network connectivity problems between Microsoft 365 and Azure Key Vault.
- **Resolution:**
  1. Verify both key vault URIs are accessible
  2. Check key vault access policies include the Microsoft 365 service principal
  3. Verify keys have not expired and have the correct permissions (wrap, unwrap)
  4. If keys were recently rotated, verify the new key URIs are updated in the DEP
  5. Contact Microsoft support if the DEP remains in error state after verification

### Issue 2: Copilot Cannot Access Encrypted Content

- **Symptoms:** Copilot responds with "I don't have access to that content" when asked about documents protected with encryption-enabled labels
- **Root Cause:** The user may not have the necessary RMS rights to decrypt the content, or the encryption configuration may not support Copilot access.
- **Resolution:**
  1. Verify the user has at least "View" rights on the encrypted document
  2. Check the label's encryption settings for the specific rights granted
  3. Verify the user can open the document directly (outside of Copilot)
  4. If the user can open it but Copilot cannot, this may be a service limitation — check Microsoft documentation for current encrypted content support in Copilot

### Issue 3: TLS Downgrade Attacks Detected

- **Symptoms:** Security monitoring detects connections using TLS versions below 1.2 to Microsoft 365 endpoints
- **Root Cause:** Legacy applications, outdated clients, or misconfigured proxy servers may negotiate lower TLS versions.
- **Resolution:**
  1. Identify the source of the lower TLS connections from monitoring logs
  2. Update legacy applications to support TLS 1.2
  3. Configure proxy servers to enforce TLS 1.2 minimum for outbound connections
  4. Microsoft 365 rejects connections below TLS 1.2 by default; the issue may be with on-premises infrastructure

### Issue 4: Key Rotation Disruption

- **Symptoms:** After rotating Customer Key vault keys, users experience temporary access issues with encrypted content
- **Root Cause:** Key rotation requires the new key to be available before the old key is decommissioned. If timing is incorrect, content may be temporarily inaccessible.
- **Resolution:**
  1. Follow Microsoft's documented key rotation procedure exactly
  2. Never decommission the old key until the new key is fully active in the DEP
  3. Test key rotation in a non-production environment first
  4. Schedule key rotation during low-activity periods

## Diagnostic Steps

1. **Check platform encryption:** Review Service Trust Portal SOC 2 report
2. **Verify TLS:** Run Script 1 to check connector configurations
3. **Check Customer Key:** Run Script 2 to verify DEP status
4. **Test encrypted access:** Open an encrypted document directly and via Copilot
5. **Review key health:** Check Azure Key Vault health in the Azure portal

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor encryption configuration questions | Security team |
| **Medium** | Customer Key DEP warnings | Security Operations and Microsoft support |
| **High** | TLS downgrade detected | Security Operations for investigation |
| **Critical** | Customer Key DEP in error state — potential data access disruption | CISO, Microsoft TAM, and IT Operations immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Encryption configuration
- [PowerShell Setup](powershell-setup.md) — Verification scripts
- [Verification & Testing](verification-testing.md) — Encryption validation
- Back to [Control 2.8](../../../controls/pillar-2-security/2.8-encryption.md)
