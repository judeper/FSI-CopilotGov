# Control 2.8: Encryption (Data in Transit and at Rest) — Evidence Walkthrough

Control 2.8 is a manual evidence review. Microsoft 365 service encryption, endpoint TLS negotiation, connector settings, and Customer Key configuration have different evidence sources. Do not replace those sources with a generic portal screen or unrelated Microsoft Graph organization properties.

## Prerequisites

- Access to the organization’s approved Microsoft 365/Copilot endpoint inventory.
- Exchange Online Admin access if Exchange connector or SMTP AUTH evidence is in scope.
- Access to the Customer Key onboarding/DEP record and the relevant Azure subscriptions if Customer Key is deployed.
- Access to the applicable Service Trust Portal evidence.

## Steps

### Step 1: Review the Microsoft 365 service encryption boundary manually

There is no tenant-wide Microsoft 365 Admin Center encryption screen that proves tenant-wide encryption.

1. Review [Microsoft 365 encryption](https://learn.microsoft.com/en-us/microsoft-365/compliance/encryption) and the [technical encryption reference](https://learn.microsoft.com/en-us/microsoft-365/compliance/technical-reference-details-about-encryption).
2. Retrieve the applicable Service Trust Portal report or assurance artifact through the organization’s approved process.
3. Record the document/report version, reviewer, date, workloads in scope, and any service-specific limitation.

This establishes the Microsoft-managed service boundary. It does not replace evidence for customer-configurable paths.

### Step 2: Capture negotiated TLS handshake evidence

Run the [PowerShell handshake procedure](powershell-setup.md#script-1-capture-actual-negotiated-tls-handshakes) from representative managed-network locations.

1. Start with the organization’s approved Microsoft 365/Copilot endpoint inventory.
2. Record each endpoint, port, client/network location, negotiated protocol, cipher suite, certificate, and timestamp.
3. Retain the raw output with the evidence pack.
4. Treat TLS 1.3 as endpoint- and client-dependent. Microsoft states that it is rolling out across applications and services; it is not universal across Microsoft 365.

Do not use TCP reachability, a client protocol preference, or an endpoint’s DNS name as TLS-version proof.

### Step 3: Review Exchange connector and SMTP AUTH exception settings when applicable

**Portal:** [Exchange admin center](https://admin.exchange.microsoft.com)
**Path:** **Mail flow > Connectors**

For a tenant with partner, hybrid, forced-TLS, or mutual-TLS mail flow:

1. Review inbound connector `RequireTls` and sender certificate configuration.
2. Review outbound connector TLS settings, TLS domain, smart-host, and certificate configuration.
3. Export the same configuration through the PowerShell procedure for retained evidence.
4. If SMTP AUTH is used, review `AllowLegacyTLSClients`. It only controls the opt-in legacy SMTP AUTH endpoint and is not a general Microsoft 365 TLS setting.

Connector evidence applies only to the configured mail-flow path. It does not prove a negotiated TLS version for Microsoft 365 Copilot HTTPS traffic.

### Step 4: Review Customer Key evidence when deployed

Customer Key setup and validation are performed through Exchange Online PowerShell, the Customer Key Onboarding Service, and Azure resource configuration. Do not assume there is a single Purview portal screen that reports complete Customer Key status.

1. Retain the relevant DEP state and Customer Key Onboarding Service request result.
2. Confirm the request used **two distinct paid Azure subscriptions** and that there is one Azure Key Vault Premium vault or Managed HSM in each subscription for the Customer Key scenario.
3. In the [Azure portal](https://portal.azure.com), review each vault/HSM in its own subscription context:
   - Premium/HSM configuration and HSM-protected production key.
   - Azure Key Vault soft-delete retention of 90 days and purge protection.
   - Managed HSM purge protection and the applicable recovery configuration.
   - Required Microsoft 365 application permissions and key operation access.
4. Confirm the Customer Key Onboarding Service `Validate` result is successful before retaining `Enable` evidence.

For Azure Key Vault, separate pairs are required when Multiple Workloads, Exchange, and SharePoint/OneDrive Customer Key scenarios are all deployed. Managed HSM uses two instances, one per subscription, across Customer Key workloads.

### Step 5: Review sensitivity-label encryption behavior

**Portal:** [Microsoft Purview portal](https://purview.microsoft.com)
**Path:** **Solutions > Information Protection > Sensitivity labels > [label] > Encryption**

For each label in scope, capture the effective rights and test outcomes rather than relying on the label name:

1. VIEW without EXTRACT: Copilot normally does not summarize the encrypted item but can reference it with a link.
2. OWNER: Full control includes EXTRACT; the person applying encryption is the Rights Management owner and can receive the content.
3. User-defined permissions: test unopened SharePoint/OneDrive files, direct `/**` references, and a file open in an Office app.
4. Edge: if Edge DLP is not deployed, test the active-browser-tab exception.
5. External plugins and Graph connectors: test separately because their sensitivity labels/encryption are not recognized by Microsoft 365 Copilot Chat; Power BI is a documented exception.
6. DKE: test separately as an intentional Copilot/agent exclusion.

### Step 6: Assemble the manual evidence pack

Include:

- Microsoft documentation and Service Trust Portal review record.
- Raw negotiated TLS handshake output.
- Exchange connector and SMTP AUTH exception export, where applicable.
- Customer Key DEP/onboarding state and Azure Key Vault/Managed HSM configuration, where applicable.
- Sensitivity-label/DKE test matrix and identified exceptions.
- Scope, date, reviewer, evidence locations, and remediation owner for any gap.

## FSI Recommendations

| Tier | Recommendation |
|---|---|
| **Baseline** | Retain a service-boundary review and negotiated TLS handshakes for representative approved endpoints. |
| **Recommended** | Add connector evidence where those mail-flow paths exist and evaluate Customer Key/DKE against approved data categories. |
| **Regulated** | Maintain recurring evidence, explicit exception decisions, separate Customer Key subscription/key ownership, and current HSM validation evidence when required by the organization’s policy. |

## Next Steps

- Run [PowerShell Setup](powershell-setup.md) to collect scoped evidence.
- Use [Verification & Testing](verification-testing.md) for the test matrix.
- See [Troubleshooting](troubleshooting.md) for diagnostic paths.
- Back to [Control 2.8](../../../controls/pillar-2-security/2.8-encryption.md).
