# Control 4.16: Microsoft Scout Governance - Portal Walkthrough

Step-by-step admin workflow for governing Microsoft Scout while it is a Frontier preview capability: confirming Frontier scoping, deploying and verifying endpoint policy through Intune, completing admin attestation, aligning per-user GitHub Copilot entitlement, setting the default permission posture, governing MCP servers and skills, and confirming supervision coverage. This playbook governs the Scout endpoint agent; broader admin settings (Control 4.1), extensibility (Control 4.13), and Cowork governance (Control 4.15) remain owned by their respective controls.

## Prerequisites

- [Control 4.1 Admin Settings and Feature Management](../../../controls/pillar-4-operations/4.1-admin-settings-feature-management.md) baseline is documented.
- [Control 4.13 Extensibility Governance](../../../controls/pillar-4-operations/4.13-extensibility-governance.md) governs plugins, connectors, and MCP servers that extend Scout.
- Intune (or equivalent MDM) is deployed and healthy across the target device population.
- An approved pilot security group exists, aligned to (a) Frontier scoping, (b) endpoint-policy targeting, and (c) GitHub Copilot Business or Enterprise entitlement.
- A documented agent register and evidence repository are in place, per [Control 4.16](../../../controls/pillar-4-operations/4.16-microsoft-scout-governance.md).
- A named approver has been identified for each of the three gates (Copilot admin, endpoint management, GitHub administration).

> **Important:** Scout is a Frontier preview capability. Its inference path, storage boundaries, permission model, admin-attestation flow, and endpoint policy schema have changed during preview and are expected to continue changing. Re-verify each step against current Microsoft documentation before relying on it in production governance.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft 365 admin center | Copilot > Settings > Frontier | Scopes Frontier access for users and admins; required before Scout admin surfaces and user entitlement resolve |
| Microsoft Intune admin center | Devices > Configuration profiles (Windows: imported ADMX with `AllowScoutFrontierAccess`; macOS: custom `.mobileconfig` device profile) | Deploys the Scout endpoint policy that authorizes Scout to run on managed endpoints |
| Microsoft Intune admin center | Devices > Configuration profiles > Assignments | Restricts endpoint policy to the approved pilot device groups |
| Scout admin attestation surface | As directed by current Microsoft Scout documentation | Records that an authorized admin has attested to the deployment; a required gate distinct from policy deployment |
| GitHub | Copilot administration for the linked GitHub organization or enterprise | Governs per-user GitHub Copilot Business or Enterprise entitlement, which is required for Scout sign-in |
| Microsoft Purview portal | Audit | Captures the subset of Scout-related activity that flows through M365 audit; not a complete evidence source for Scout |
| Governance evidence repository | Workspace of record | Stores Frontier decisions, endpoint policy exports, admin-attestation records, entitlement reconciliations, MCP inventory, and permission-mode decisions |

## Steps

### Step 1: Confirm Frontier scoping

Navigate to **Copilot > Settings > Frontier** in the Microsoft 365 admin center and record which users and admin accounts are scoped for Frontier. Confirm scope matches the approved pilot security group. Capture the decision, approver, and target group in the register. Scout admin surfaces and user entitlement resolve only after Frontier scoping is in place.

### Step 2: Deploy endpoint policy through Intune

Deploy the Scout endpoint policy for the intended device groups:

- **Windows 11 or later:** In the Intune admin center, import the Scout ADMX and ADML files, create a device configuration profile that sets `AllowScoutFrontierAccess`, and assign it to the approved pilot device group only.
- **macOS 12 or later:** Create a custom device configuration profile that deploys the Microsoft-provided Scout `.mobileconfig`, and assign it to the approved pilot device group only.

Verify assignment coverage on a sample device (Windows: `gpresult` or the applicable Intune reporting; macOS: `profiles show`), and capture an export of the profile and its assignments as evidence.

### Step 3: Complete admin attestation

Complete the admin attestation step required by Scout for the deployment, using an authorized admin account. Retain the attestation record as evidence in the governance workspace. Confirm that installing the Scout application without policy and attestation does not grant Scout functionality — the app relies on the admin gates being in place.

### Step 4: Reconcile GitHub Copilot entitlement

Reconcile the list of users who hold GitHub Copilot Business or Enterprise entitlement (with linked GitHub accounts) against the approved pilot list. Restrict entitlement to the pilot population, and document the entitlement decision, approver, and reconciliation date. Recognize that GitHub administration is a separate governance surface from the Microsoft 365 admin center.

### Step 5: Set the default permission posture

Document the default posture for Scout shell command permissions (auto-approve / prompt / deny). Keep the default at **prompt** during the pilot unless a specific low-risk auto-approve list has been approved. Explicitly document that autonomous modes are not enabled for the pilot unless a separately approved low-risk scoping decision exists that covers workspace, shell, browser, network, and M365 scope restrictions. Explicitly document that scheduled or triggered automations are not enabled without a separately approved unattended-execution decision.

### Step 6: Govern MCP servers and skills

Establish an approved-MCP-server inventory. For each proposed MCP server, capture the data path (local vs remote), authentication mechanism, and any external egress before approval. Treat MCP servers as connectors under [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md), with MCP-specific approval criteria added. Apply the same discipline to any skills added to the pilot.

### Step 7: Map the storage and inference boundary

Document, for the pilot, which Scout data lives in OneDrive (session and memory data, subject to tenant controls) versus locally on the endpoint (automation instructions, MCP output — outside the M365 DPA), and where inference is processed (Microsoft, GitHub Copilot, third-party model providers — some inference outside M365 residency, retention, label enforcement, and eDiscovery). Record the residual risk acceptance and the compensating endpoint controls (DLP, endpoint monitoring, workspace scoping).

### Step 8: Confirm supervision, audit, and incident-response coverage

Confirm which Scout activity is visible to existing Purview audit and supervision tooling, and document coverage gaps (local automation instructions, MCP output, third-party inference). Ensure the incident-response playbook covers independent revocation of Frontier scoping, endpoint policy, and GitHub Copilot entitlement, plus preservation of locally stored Scout artifacts. Define a preview-change review cadence.

## FSI Recommendations

| Tier | Recommendation |
|------|----------------|
| **Baseline** | Document all three gates (Frontier scope, endpoint policy + attestation, GitHub entitlement), keep shell default at **prompt**, maintain an approved-MCP inventory, and record the storage/inference boundary. |
| **Recommended** | Use a change register with named approvers per gate, separate approval from implementation, restrict Scout workspaces to defined scopes, and confirm audit coverage explicitly rather than by assumption. |
| **Regulated** | All Recommended controls plus: dual technology + compliance approval before enabling any regulated population, no autonomous modes and no unattended automations without separate approval, examination-ready evidence retention, and documented acceptance of the third-party inference and local-storage boundaries as known unsupported evidence. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to inspect Intune policy assignment, capture Windows registry evidence, and pull M365-side audit evidence.
- Use [Verification & Testing](verification-testing.md) to validate the three gates, permission posture, MCP inventory, and audit-coverage assessment.
- Keep [Troubleshooting](troubleshooting.md) available for entitlement, endpoint-policy, attestation, MCP, and boundary-related issues.

*FSI Copilot Governance Framework — Control 4.16 (Microsoft Scout, Frontier preview) · Last Verified 2026-07-10*
- Back to [Control 4.16](../../../controls/pillar-4-operations/4.16-microsoft-scout-governance.md)
