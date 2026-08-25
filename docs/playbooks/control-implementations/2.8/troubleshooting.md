# Control 2.8: Encryption (Data in Transit and at Rest) — Troubleshooting

Use this guide to diagnose scoped encryption evidence. Do not convert a connector setting, Microsoft Graph notification property, TCP test, or client protocol preference into a claim about every Microsoft 365 data flow.

## Common issues

### Issue 1: Customer Key onboarding validation fails

- **Symptoms:** The Customer Key Onboarding Service reports a failed `ValidationResult`, or `FailedValidations` contains subscription, recovery, key, or permission errors.
- **Likely causes:** The request reused one subscription, named a vault/HSM outside the declared subscription, used an ineligible subscription, lacks 90-day recovery/purge protection where required, has an expired/unsupported key, or lacks required Microsoft 365 application access.
- **Resolution:**
  1. Confirm two **distinct paid** Azure subscription IDs are supplied to the request.
  2. Select each subscription explicitly with `Set-AzContext` and verify the vault/HSM resides in that subscription.
  3. For Azure Key Vault, verify 90-day soft-delete retention and purge protection. For Managed HSM, verify purge protection and the applicable recovery settings.
  4. Verify the key is appropriate for the selected Customer Key configuration, is not expired, and permits required operations.
  5. Review `$request.FailedValidations`, remediate the stated item, and rerun `Validate`; do not use `Enable` until validation succeeds.

### Issue 2: DEP state is not healthy after onboarding

- **Symptoms:** `Get-DataEncryptionPolicy` reports an unexpected state or policy assignment does not match the approved workload.
- **Likely causes:** Key access, DEP assignment, key-expiry, workload-scenario, or rotation-process error.
- **Resolution:**
  1. Export the actual DEP state and key identifiers.
  2. Verify the onboarding scenario matches the workload. The Multiple Workloads DEP includes Microsoft 365 Copilot interactions; Exchange mailbox and SharePoint/OneDrive scenarios use their workload-specific processes.
  3. Verify both paired keys/vaults/HSMs remain accessible and have not expired.
  4. Review the change and key-rotation records before changing a policy.
  5. Escalate through Microsoft support if the service state remains unresolved after configuration review.

### Issue 3: Copilot does not summarize an encrypted item

- **Symptoms:** Copilot provides a link, an incomplete response, or a message indicating it cannot use an encrypted item.
- **Likely causes:** The requesting user has VIEW but not EXTRACT, the source is an unopened user-defined-permissions item, a label blocks connected experiences, the source/surface has a documented limitation, or the item is DKE-protected.
- **Resolution:**
  1. Check the requesting user’s effective EXTRACT (Copy) right, not just the label template.
  2. Remember that OWNER includes EXTRACT and that the person applying encryption is the Rights Management owner.
  3. Test whether the item is open in an Office app, directly referenced where supported, or protected with user-defined permissions.
  4. For Edge, check whether Edge DLP is deployed before assuming EXTRACT alone controls active-tab behavior.
  5. Identify whether the source is an external plugin or Graph connector; sensitivity labels/encryption for those external sources are not generally recognized by Microsoft 365 Copilot Chat.
  6. If the item is DKE-protected, treat the Copilot exclusion as expected behavior.

### Issue 4: A handshake shows TLS 1.2 instead of TLS 1.3

- **Symptoms:** The negotiated TLS evidence records TLS 1.2.
- **Likely causes:** TLS 1.3 is rolling out by Microsoft 365 application/service and is also client/network dependent. The observed endpoint or path may legitimately negotiate TLS 1.2.
- **Resolution:**
  1. Preserve the raw handshake output and endpoint/client/network scope.
  2. Confirm the result is TLS 1.2 or higher.
  3. Compare the endpoint to Microsoft’s current service-specific TLS documentation; do not claim TLS 1.3 is universal or unavailable based on one sample.
  4. Check managed client, proxy, TLS-inspection, and endpoint-inventory changes before escalating.

### Issue 5: A legacy TLS finding appears for SMTP AUTH

- **Symptoms:** `AllowLegacyTLSClients` is enabled or an SMTP AUTH client is configured for `smtp-legacy.office365.com`.
- **Likely causes:** A legacy device/application has an approved or unreviewed exception.
- **Resolution:**
  1. Inventory the mailbox, device/application, owner, and business reason.
  2. Confirm the exception is limited to SMTP AUTH and not presented as a general Microsoft 365 TLS posture.
  3. Upgrade or replace the client to support TLS 1.2+ and remove the opt-in setting when no longer needed.
  4. Note that the legacy endpoint is unavailable in GCC, GCC High, and DoD.

### Issue 6: Connector evidence conflicts with endpoint handshake evidence

- **Symptoms:** An Exchange connector is configured for forced/mutual TLS but a sampled HTTPS endpoint reports a different protocol/cipher expectation.
- **Likely causes:** The items cover different transports and scopes. Connector settings cover designated Exchange mail flow; an HTTPS handshake captures one client-to-service endpoint connection.
- **Resolution:**
  1. Keep the evidence records separate.
  2. Label each record with its path and scope.
  3. Correct only the relevant connector or endpoint configuration; do not use either item as a substitute for the other.

## Diagnostic checklist

1. Review the Microsoft 365 encryption service boundary and applicable Service Trust Portal artifact.
2. Run the negotiated TLS handshake procedure for the approved endpoint set.
3. Export Exchange connector and SMTP AUTH exception settings only when those paths exist.
4. Review Customer Key onboarding/DEP state and the paired Azure Key Vault/Managed HSM configuration when deployed.
5. Run the sensitivity-label/DKE test matrix with effective user rights and source/surface exceptions.

## Escalation

| Severity | Condition | Escalation path |
|---|---|---|
| **Low** | Documentation or scoped evidence question | Security/GRC owner |
| **Medium** | Missing handshake, connector, or sensitivity-label evidence | Security Operations and control owner |
| **High** | Unapproved SMTP AUTH legacy TLS exception or failed Customer Key validation | Security Operations, Exchange/Azure owner, and change authority |
| **Critical** | Customer Key/key-access issue that could disrupt protected data access | CISO, Microsoft support/TAM, and IT Operations |

## Related resources

- [Portal Walkthrough](portal-walkthrough.md) — scoped manual evidence.
- [PowerShell Setup](powershell-setup.md) — handshake, connector, and Customer Key procedures.
- [Verification & Testing](verification-testing.md) — expected outcomes and evidence matrix.
- Back to [Control 2.8](../../../controls/pillar-2-security/2.8-encryption.md).
