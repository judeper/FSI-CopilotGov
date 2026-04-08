# Control 2.8: Encryption (Data in Transit and at Rest) — Portal Walkthrough

Step-by-step portal verification for encryption controls protecting data processed by M365 Copilot.

## Prerequisites

- Global Administrator or Security Administrator role
- Microsoft Purview access for encryption key management
- Understanding of Microsoft 365 encryption architecture

## Steps

### Step 1: Verify Platform-Level Encryption

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Org Settings > Services > Encryption

Verify Microsoft 365 platform encryption is active. Microsoft encrypts all data at rest using BitLocker (disk-level) and service-level encryption keys. Data in transit is encrypted using TLS 1.2 or higher.

These protections are enabled by default and apply to all Copilot data processing.

### Step 2: Review Customer Key Configuration (Optional)

**Portal:** Microsoft Purview
**Path:** Purview > Data Encryption > Customer Key

If your organization uses Microsoft Customer Key for additional encryption control, verify:
- Customer Key is configured for Exchange Online and SharePoint Online
- Data Encryption Policies are active and assigned
- Key vault accessibility and key health status are healthy
- Key rotation schedule is documented and followed

Customer Key provides an additional encryption layer that you control.

### Step 3: Verify TLS Configuration

**Portal:** Exchange Admin Center
**Path:** Exchange Admin > Mail Flow > Connectors

Review TLS enforcement for email-related Copilot interactions:
- Verify TLS 1.2 is required for all inbound and outbound connectors
- Check that opportunistic TLS is enabled (minimum)
- For regulated communications, verify forced TLS with specific partner domains

### Step 4: Review Sensitivity Label Encryption Settings

**Portal:** Microsoft Purview
**Path:** Purview > Information Protection > Labels > [Select label] > Encryption

Review encryption settings on sensitivity labels that apply to Copilot-accessible content:
- Which labels enforce encryption
- Rights Management permissions on encrypted content
- Whether Copilot users have necessary decryption rights
- Co-authoring compatibility with encrypted documents

### Step 5: Document Encryption Posture

Create an encryption posture document covering:
- Platform encryption status (BitLocker, service encryption)
- Customer Key status (if applicable)
- TLS enforcement configuration
- Sensitivity label encryption settings
- Key management procedures and rotation schedule

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Verify default platform encryption; enforce TLS 1.2; document encryption posture |
| **Recommended** | Evaluate Customer Key for additional control; sensitivity label encryption for Confidential+ content |
| **Regulated** | Customer Key deployed with documented key management; FIPS 140-3 validated encryption; quarterly encryption posture review |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for encryption verification scripts
- See [Verification & Testing](verification-testing.md) to validate encryption
- Review Control 2.2 for sensitivity label encryption interaction with Copilot
