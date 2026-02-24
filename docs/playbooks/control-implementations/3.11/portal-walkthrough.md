# Control 3.11: Record Keeping and Books-and-Records Compliance — Portal Walkthrough

Step-by-step portal configuration for implementing record keeping controls that support compliance with SEC Rule 17a-4 (including the audit-trail alternative under Rule 17a-4(f)(2)(ii)(A)), FINRA Rule 4511, and other books-and-records requirements for Copilot-generated content -- including mobile Copilot access controls to prevent off-channel recordkeeping gaps.

## Prerequisites

- **Role:** Compliance Administrator, Records Management Administrator
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal, Microsoft Intune admin center

## Steps

### Step 1: Configure Records Management for Copilot Content

**Portal:** Microsoft Purview portal
**Path:** Solutions > Records management > File plan

1. Navigate to the Records management solution.
2. Create file plan categories aligned with SEC/FINRA record types:
   - **Business Communications** — Copilot-drafted emails, Teams messages
   - **Client Correspondence** — Copilot-assisted client communications
   - **Investment Recommendations** — AI-assisted advisory content
   - **Marketing Materials** — Copilot-generated marketing content
3. Assign retention periods per category (minimum 3 years for general communications, 6 years for client records).

### Step 2: Create Retention Labels with Regulatory Record Status

**Portal:** Microsoft Purview portal
**Path:** Solutions > Records management > File plan > Create a label

1. Create retention labels for each record category:
   - "SEC-17a4-Business-Communication-6yr" — 6-year retention, regulatory record
   - "FINRA-4511-Client-Record-7yr" — 7-year retention, regulatory record
   - "Investment-Recommendation-Record-7yr" — 7-year retention, regulatory record
2. Mark labels as **Regulatory records** where required (immutable, cannot be relabeled or deleted).
3. Configure disposition review for records approaching expiration.

### Step 3: Configure Auto-Apply Retention Labels

**Portal:** Microsoft Purview portal
**Path:** Solutions > Records management > Label policies > Auto-apply a label

1. Create auto-apply policies for each retention label:
   - Apply "Business Communication" labels based on Copilot interaction metadata
   - Apply "Client Correspondence" labels based on external recipient detection
   - Apply "Investment Recommendation" labels using trainable classifiers for advisory content
2. Target locations: Exchange, SharePoint, OneDrive, Teams.
3. Set each policy to run continuously.

### Step 4: Configure WORM Compliance — Audit-Trail Alternative or Third-Party Archival

**Portal:** Microsoft Purview portal
**Path:** Solutions > Records management > Retention policies

SEC Rule 17a-4(f) requires WORM storage or an audit-trail alternative under Rule 17a-4(f)(2)(ii)(A). Configure one of the following paths:

**Option A: Audit-Trail Alternative (Rule 17a-4(f)(2)(ii)(A))**

The audit-trail alternative allows records to be stored in non-WORM format if the firm maintains an audit trail of all modifications, deletions, and access events throughout the retention period. Microsoft Purview regulatory records combined with Preservation Lock may satisfy this requirement:

1. Verify that regulatory record labels are configured (Step 2 above): when applied, labels block modifications and deletions and log all attempts in the Purview audit log.
2. Enable **Preservation Lock** on the retention policy governing regulatory records:
   - Navigate to **Retention policies** > select the policy > **Lock**
   - Confirm the lock. **Preservation Lock is irreversible** — once enabled, the policy cannot be shortened or disabled.
   - Document the date, policy name, and administrator who applied the lock.
3. Verify that the **Purview audit log** captures access events for labeled items:
   - Navigate to **Audit** > **Search** > search for record-related audit events (e.g., ComplianceRecordChanged, RecordLocked, FileSensitivityLabelChanged)
   - Confirm audit events are being generated for labeled Copilot content
4. Document the compliance approach in writing, confirming with 17a-4 compliance counsel that the configuration meets Rule 17a-4(f)(2)(ii)(A) requirements before relying on this path.

**Option B: Third-Party WORM Archival (Traditional Path)**

1. Select a SEC 17a-4(f)-compliant archival solution (e.g., Bloomberg Vault, Smarsh, Global Relay).
2. Configure data connectors in Purview or from the archival vendor for:
   - Exchange (email and Copilot Chat content)
   - Teams (messages and meeting transcripts)
   - SharePoint and OneDrive (documents)
3. Verify WORM storage attestation from the vendor.
4. Confirm retention periods in the archival system match 17a-4 requirements.

### Step 5: Verify the Audit-Trail Alternative Configuration

**Portal:** Microsoft Purview portal
**Path:** Solutions > Audit > Search

After enabling Preservation Lock and regulatory record labels (Option A), verify that the audit trail is comprehensive:

1. Navigate to **Audit** > **Search**.
2. Set the date range and search for the following activity types:
   - **RecordStatusChanged** — captures when items are declared as regulatory records
   - **ComplianceRecordChanged** — captures attempts to modify regulatory records (should show blocked attempts)
   - **FileAccessedExtended** — captures file access events for SharePoint/OneDrive items
   - **FileSensitivityLabelChanged** — captures sensitivity label changes on labeled items
3. Confirm that audit events are being generated for Copilot-generated content covered by regulatory record labels.
4. Verify that the audit log retention policy is set to cover the full record retention period (minimum matching the 17a-4 retention requirement for the record type).
5. Export a sample audit log for a regulatory record item and document it as evidence of audit trail capability.

### Step 6: Configure Mobile Copilot Access Controls

**Portal:** Microsoft Intune admin center (intune.microsoft.com) + Microsoft Entra admin center
**Path:** Intune > Apps > App protection policies; Entra ID > Conditional Access

Mobile Copilot access through unmanaged devices creates an off-channel recordkeeping gap. Configure the following:

1. **Conditional Access — require managed device for Copilot:**
   - Navigate to Microsoft Entra admin center > **Protection** > **Conditional Access** > **New policy**
   - Target: Microsoft 365 Copilot app (and relevant M365 apps with Copilot functionality)
   - Condition: Device platforms (iOS, Android, Windows)
   - Grant: **Require device to be marked as compliant** (Intune) OR **Require approved client app** (for MAM without MDM enrollment)
   - See Control 2.3 for detailed Conditional Access Copilot policy configuration

2. **App Protection Policies (MAM) for mobile M365 apps:**
   - Navigate to Intune > **Apps** > **App protection policies** > **Create policy**
   - Platform: iOS/iPadOS and Android
   - Apps: Outlook, Teams, Word, Excel, PowerPoint (all include Copilot access)
   - Data protection settings:
     - Prevent backup of Org data
     - Send Org data to only policy-managed apps
     - Block screen capture
   - Access requirements:
     - PIN for app access
     - Corporate credentials for access
   - This ensures that even on unmanaged devices, corporate data accessed through Copilot in managed apps is protected

3. **Verify mobile retention policy coverage:**
   - Confirm that Teams mobile interactions (via official app) are covered by Teams retention policies
   - Confirm that Outlook mobile interactions (via official app) are covered by Exchange retention policies
   - Test by generating a Copilot interaction via mobile app and searching for it in Purview Audit within 24 hours

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Record classification | Manual | Auto-apply labels | Auto-apply with manual override |
| Regulatory record status | Optional | Key categories | All client-facing content |
| 17a-4(f) compliance path | Document selection | Option A (audit-trail alt.) or Option B (WORM) documented | Option A with counsel review OR Option B with vendor attestation |
| Preservation Lock | Not applied | Applied to critical records | Required (Option A or B) |
| Disposition review | Automatic | Review before disposition | Committee review |
| Mobile Copilot access | Managed apps only | Conditional Access policy | MDM + MAM + periodic mobile audit |
| Audit trail verification | Annual | Semi-annual | Quarterly |

## Regulatory Alignment

- **SEC Rule 17a-4(f)(2)(ii)(A)** — Audit-trail alternative to WORM storage; satisfied by Purview regulatory record labels + Preservation Lock + comprehensive audit log
- **SEC Rule 17a-4** — Supports compliance with electronic record retention and WORM storage requirements
- **FINRA Rule 4511** — Helps meet books-and-records retention obligations
- **SEC Rule 17a-3** — Supports record-making requirements for broker-dealer operations
- **Off-channel enforcement precedent** — Mobile Copilot controls prevent the off-channel record-keeping gap that has generated $2B+ in SEC/CFTC enforcement penalties

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for records management automation
- See [Verification & Testing](verification-testing.md) to validate record keeping controls
