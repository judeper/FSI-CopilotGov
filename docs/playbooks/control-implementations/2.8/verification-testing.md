# Control 2.8: Encryption (Data in Transit and at Rest) — Verification & Testing

Control 2.8 requires a manual evidence pack. The tests below deliberately separate evidence that proves an individual negotiated connection from evidence that proves a configured connector, Customer Key deployment, or Microsoft-managed service boundary.

## Test cases

### Test 1: Microsoft 365 service-encryption review

- **Objective:** Record the Microsoft-managed service encryption boundary without inventing a tenant-wide portal setting.
- **Steps:**
  1. Review the current [Microsoft 365 encryption documentation](https://learn.microsoft.com/en-us/microsoft-365/compliance/encryption).
  2. Review the current [technical encryption reference](https://learn.microsoft.com/en-us/microsoft-365/compliance/technical-reference-details-about-encryption).
  3. Obtain the applicable Service Trust Portal report through the organization’s approved process.
  4. Record source version/date, workload scope, reviewer, and limitation.
- **Expected result:** The evidence pack identifies Microsoft-managed service assurances and clearly distinguishes them from tenant-configurable evidence.
- **Evidence:** Documentation review record and approved Service Trust Portal artifact.

### Test 2: Actual TLS handshake

- **Objective:** Capture the protocol and cipher suite actually negotiated with representative approved Microsoft 365 endpoints.
- **Steps:**
  1. Run [Script 1](powershell-setup.md#script-1-capture-actual-negotiated-tls-handshakes) from a representative managed client/network location.
  2. Retain the raw JSON output, endpoint inventory reference, timestamp, protocol, cipher suite, and certificate data.
  3. Verify that each recorded negotiation is TLS 1.2 or TLS 1.3.
  4. If TLS 1.3 is not negotiated, record that it is service- and client-dependent rather than declaring it unavailable across Microsoft 365.
- **Expected result:** Each sampled endpoint has timestamped TLS 1.2+ negotiated-handshake evidence.
- **Evidence:** Raw handshake output and approved endpoint inventory reference.

!!! note "What this test does not prove"
    A successful sample does not prove every Microsoft 365 endpoint, client, proxy path, or service-to-service flow. It is a scoped observation that must be paired with Microsoft service documentation and the organization’s endpoint inventory.

### Test 3: Exchange connector and legacy SMTP AUTH exception

- **Objective:** Review forced-TLS or mutual-TLS settings only where the tenant uses those Exchange mail-flow paths.
- **Steps:**
  1. Run [Script 2](powershell-setup.md#script-2-export-narrowly-scoped-exchange-connector-and-smtp-auth-evidence).
  2. For each relevant connector, review TLS requirement, certificate identity, partner domain, and smart-host configuration.
  3. Review `AllowLegacyTLSClients` only for SMTP AUTH use.
  4. If the legacy SMTP AUTH endpoint is enabled, document the exception owner, affected devices, compensating controls, and retirement plan.
- **Expected result:** Connector evidence matches approved connector design, and any SMTP AUTH legacy TLS exception is explicitly governed.
- **Evidence:** Connector export, approval/change record, and legacy-exception record where applicable.

### Test 4: Multi-workload Customer Key DEP, configuration, and onboarding validation

- **Objective:** Verify the tenant-level multi-workload Customer Key DEP (`MDEP`) and its assignment without accepting Exchange-mailbox evidence or a single-subscription design as Copilot coverage.
- **Steps:**
  1. Run `Get-M365DataAtRestEncryptionPolicy` and `Get-M365DataAtRestEncryptionPolicyAssignment` after connecting to Exchange Online. Preserve every returned property and the property names, using [Script 3](powershell-setup.md#script-3-review-the-multi-workload-customer-key-dep-and-assignment).
  2. Confirm both a tenant-level multi-workload DEP policy and its tenant assignment are present and match the approved Copilot scenario. `Get-DataEncryptionPolicy` is Exchange-mailbox DEP evidence only and cannot satisfy this test.
  3. Record two **different paid** Azure subscription IDs in the Customer Key scenario evidence.
  4. Verify one Azure Key Vault Premium vault or Managed HSM instance in each subscription for the scenario.
  5. For Azure Key Vault, verify 90-day soft-delete retention and purge protection; for Managed HSM, verify purge protection and applicable recovery configuration.
  6. Verify production keys are HSM-protected where that design is required.
  7. Run the Customer Key Onboarding Service in `Validate` mode and retain the property-preserving onboarding request output.
  8. Before enabling, confirm `ValidationResult` is successful. Retain enablement evidence only after approved enablement completes.
- **Expected result:** The multi-workload DEP policy and tenant assignment are both present; the onboarding record verifies two unique subscriptions and the correct recovery/key configuration; it reports no unresolved validation failure.
- **Evidence:** Multi-workload DEP policy/assignment export, subscription/vault/HSM export, onboarding request output, and change approval. Exchange-mailbox DEP output cannot replace the multi-workload evidence.

### Test 5: Sensitivity-label encryption and Copilot behavior

- **Objective:** Verify documented EXTRACT behavior and exceptions rather than asserting that encrypted content is categorically inaccessible.
- **Steps:**
  1. Test a requesting user with VIEW but no EXTRACT. Confirm Copilot does not summarize the encrypted item and can reference it with a link.
  2. Test an OWNER user. Confirm that OWNER includes EXTRACT and record the expected outcome.
  3. Test an unopened SharePoint/OneDrive item encrypted with user-defined permissions, a direct `/` reference where supported, and the same item open in an Office app.
  4. If Edge DLP is not deployed, test the active encrypted browser-tab exception and record the result.
  5. Test each external plugin or Graph connector source separately; do not assume sensitivity labels/encryption applied to external data are recognized by Microsoft 365 Copilot Chat.
  6. Test a DKE-protected item separately. Confirm that it is not returned by Copilot/agents and that Copilot cannot be used in the app while the DKE item is open.
- **Expected result:** Outcomes match the documented user, source, and surface boundary; deviations have an owner and escalation path.
- **Evidence:** Test matrix with user role/rights, source, surface, expected result, actual result, date, and tester.

### Test 6: Current HSM validation evidence

- **Objective:** Confirm the organization has current evidence for the HSM assurance level it requires.
- **Steps:**
  1. Record the actual key type and service configuration.
  2. For Azure Key Vault Premium or Managed HSM, review the current [firmware validation notice](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/firmware-update).
  3. Record the current validation reference and review date; recheck after firmware or certification changes.
- **Expected result:** The evidence names the actual HSM-backed key configuration and current validation source, not only a vault SKU.
- **Evidence:** Key configuration export and validation-reference review record.

## Evidence collection

| Evidence item | Format | Scope / limitation | Storage location |
|---|---|---|---|
| Microsoft service-encryption review | Review record + approved service-assurance artifact | Microsoft-managed service boundary; not a tenant setting | Compliance evidence repository |
| Negotiated TLS handshake | JSON/text | Representative endpoint/client/network observation | Compliance evidence repository |
| Exchange connector export | JSON/text | Only configured partner/hybrid/forced-TLS or mutual-TLS mail paths | Compliance evidence repository |
| SMTP AUTH legacy exception record | Change/exception record | Only `smtp-legacy` use controlled by `AllowLegacyTLSClients` | Compliance evidence repository |
| Multi-workload Customer Key DEP/assignment and onboarding state | JSON/text | Tenant-level Copilot MDEP policy and assignment; Exchange-mailbox DEP output is a separate scope | Compliance evidence repository |
| Azure Key Vault/Managed HSM configuration | JSON/text + portal export | Subscription, recovery, key type, and role configuration | Compliance evidence repository |
| Sensitivity-label/DKE test matrix | Test record | User/source/surface-specific behavior | Compliance evidence repository |

## Compliance mapping

| Regulation | Requirement | How this control supports it |
|---|---|---|
| GLBA §501(b) | Safeguards for customer information | Documents encryption evidence and key-management boundaries for Copilot data flows. |
| NYDFS Part 500 §500.15 | Encryption of NPI in transit and at rest based on risk assessment | Supports a risk-based review of transport, at-rest, and key-management evidence. |
| FFIEC IT Examination Handbook | Cryptographic controls | Supports examination-ready evidence of actual handshakes, key configuration, and exception decisions. |

- Back to [Control 2.8](../../../controls/pillar-2-security/2.8-encryption.md).
