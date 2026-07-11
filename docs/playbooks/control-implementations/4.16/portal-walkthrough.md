# Control 4.16: Microsoft Scout Governance - Portal Walkthrough

Step-by-step admin workflow for governing Microsoft Scout while it is a Frontier preview capability: confirming Frontier scoping, deploying and verifying endpoint policy through Intune, completing admin attestation, aligning per-user GitHub Copilot entitlement, setting the default permission posture, governing MCP servers and skills, and confirming supervision coverage. This playbook governs the Scout endpoint agent; broader admin settings (Control 4.1), extensibility (Control 4.13), and Cowork governance (Control 4.15) remain owned by their respective controls.

## Prerequisites

- [Control 4.1 Admin Settings and Feature Management](../../../controls/pillar-4-operations/4.1-admin-settings-feature-management.md) baseline is documented.
- [Control 4.13 Extensibility Governance](../../../controls/pillar-4-operations/4.13-extensibility-governance.md) governs plugins, connectors, and MCP servers that extend Scout.
- [Control 1.9 License Planning](../../../controls/pillar-1-readiness/1.9-license-planning.md) is baselined so pilot users can be reconciled against active **Microsoft 365 Copilot license** assignment.
- Intune (or equivalent MDM) is deployed and healthy across the target device population.
- Windows pilot devices have the current [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist) as part of the managed-app baseline.
- The pilot has a documented installation-privilege plan: prefer a system-context managed deployment of the Scout installer through Intune (or a just-in-time elevation mechanism such as Endpoint Privilege Management) so end users are not granted standing local Administrator rights on the endpoint solely to install Scout. Microsoft's [get-started documentation](https://learn.microsoft.com/microsoft-scout/get-started) requires local Administrator permissions for installation but not for ongoing use.
- An approved pilot security group exists, aligned to (a) Frontier scoping, (b) endpoint-policy targeting, (c) Microsoft 365 Copilot license assignment, and (d) GitHub Copilot Business or Enterprise entitlement.
- A documented agent register and evidence repository are in place, per [Control 4.16](../../../controls/pillar-4-operations/4.16-microsoft-scout-governance.md).
- A named approver has been identified for each of the three gates (Copilot admin, endpoint management, GitHub administration) and for the M365 Copilot license reconciliation.

> **Important:** Scout is a Frontier preview capability. Its inference path, storage boundaries, permission model, admin-attestation flow, and endpoint policy schema have changed during preview and are expected to continue changing. Re-verify each step against current Microsoft documentation before relying on it in production governance.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft 365 admin center | Copilot > Settings > View all > Copilot Frontier (No access / All users / Specific users) | Scopes Frontier access for users and admins; required before Scout admin surfaces and user entitlement resolve. Microsoft cites up to about three hours for propagation. |
| Microsoft 365 admin center | Users > Active users (license assignment) or Billing > Licenses | Reconciles Microsoft 365 Copilot license assignment for pilot users — an active Copilot license is a documented per-user prerequisite for Scout |
| Microsoft Intune admin center | Devices > Configuration > Import ADMX | Imports the Microsoft-provided `microsoft-scout.admx` and `microsoft-scout.adml` templates so a Windows configuration policy can enable **Allow Microsoft Scout Frontier access** and the documented ADMX admin controls |
| Microsoft Intune admin center | Devices > Configuration > Policies (Windows imported administrative template; macOS custom `.mobileconfig`) | Deploys the Scout endpoint policy and the documented ADMX admin controls that authorize Scout to run on managed endpoints and govern its runtime behavior |
| Microsoft Intune admin center | Devices > Configuration profiles > Assignments | Restricts endpoint policy to the approved pilot device groups |
| Microsoft Intune admin center | Apps > Windows / macOS apps | Deploys the Scout installer in system context (preferred) so end users do not need local Administrator rights to install |
| Frontier organization sign-up (admin attestation) | Microsoft-provided Frontier organization sign-up form (linked from [Admin access overview for Microsoft Scout](https://learn.microsoft.com/microsoft-scout/admin-access-overview)) | Records the admin attestation and opt-in step required because Scout can route data outside Microsoft 365 to third-party inference paths |
| GitHub | Copilot administration for the linked GitHub organization or enterprise | Governs per-user GitHub Copilot Business or Enterprise entitlement, which is required for Scout sign-in |
| Microsoft Purview portal | Audit | Captures the subset of Scout-related activity that flows through M365 audit; not a complete evidence source for Scout |
| Governance evidence repository | Workspace of record | Stores Frontier decisions, endpoint policy exports (including ADMX admin-control snapshots), admin-attestation records, M365 Copilot license and GitHub entitlement reconciliations, MCP inventory, installation-privilege deployment records, and permission-mode decisions |

## Steps

### Step 1: Confirm Frontier scoping

Navigate to **Copilot > Settings > View all > Copilot Frontier** in the Microsoft 365 admin center. Record whether access is **No access**, **All users**, or **Specific users** and which users and admin accounts are scoped. Confirm scope matches the approved pilot security group. Capture the decision, approver, and target group in the register. Scout admin surfaces and user entitlement resolve only after Frontier scoping is in place and change propagation completes (Microsoft cites up to about three hours).

### Step 2: Deploy endpoint policy through Intune

Deploy the Scout endpoint policy for the intended device groups:

- **Windows 11 or later:** In the Intune admin center, go to **Devices > Configuration > Import ADMX** and import Microsoft's `microsoft-scout.admx` and `microsoft-scout.adml`. Create a Windows configuration policy from **Devices > Configuration > Policies > New policy** with platform **Windows 10 and later**, profile type **Templates**, template **Imported Administrative Templates**, then select the imported Microsoft Scout template. Under **Microsoft Scout > Capabilities**, set **Allow Microsoft Scout Frontier access** to **Enabled** (the `AllowScoutFrontierAccess` capability). In the same policy (or in a companion policy that targets the same device groups), record and configure the pilot posture for each of the documented ADMX admin controls under `HKLM\SOFTWARE\Policies\Scout`: `DisabledServers`, `DisabledPermissions`, `ForcePrompt`, `DisabledModels`, `DisabledProviders`, `DisableHeartbeat`, `DisableWorkflows`, `RestrictToWorkspace`, `BrowserEgressBlockedOrigins`, and `PolicyVersion`. Assign the policy or policies to the approved pilot device group only. Where a setting's default value is not stated by Microsoft, document the observed value and cite the current Microsoft Learn article and date verified — do not invent defaults.
- **macOS 12 or later:** Create a custom device configuration profile that deploys Microsoft's `microsoft-scout.mobileconfig`, and assign it to the approved pilot device group only. Where the equivalent of any Windows ADMX admin control is required on macOS, confirm the specific payload key against current Microsoft documentation before treating it as configured evidence.

Verify assignment coverage on a sample device (Windows: `gpresult` or the applicable Intune reporting plus a `HKLM\SOFTWARE\Policies\Scout` snapshot; macOS: `profiles show`), and capture an export of the profile(s) and their assignments as evidence.

### Step 3: Complete admin attestation and opt-in

Complete Microsoft's Frontier organization sign-up (admin attestation) form for the deployment using an authorized admin account. Retain the attestation record as evidence in the governance workspace. Microsoft states that this attestation is an additional gating layer beyond Frontier enrollment because Scout can route data outside Microsoft 365 to third-party inference paths — do not treat endpoint-policy deployment as a substitute for attestation. Confirm that installing the Scout application without the policy, attestation, and per-user prerequisites does not grant Scout functionality.

### Step 4: Reconcile Microsoft 365 Copilot license and GitHub Copilot entitlement

Reconcile Microsoft 365 Copilot license assignment for pilot users against Control 1.9 records. In parallel, reconcile the list of users who hold GitHub Copilot Business or Enterprise entitlement (with linked GitHub accounts) against the approved pilot list. Restrict entitlement to the pilot population, and document the entitlement decisions, approvers, and reconciliation dates. Recognize that GitHub administration is a separate governance surface from the Microsoft 365 admin center.

### Step 5: Confirm the installation-privilege deployment pattern

Confirm and record the deployment pattern used for the Scout installer on pilot endpoints. Preferred patterns:

- Package and deploy the Microsoft Scout installer as a managed Win32 or macOS app through Intune, installed in **system context** so end users never need local Administrator rights.
- Use a just-in-time local admin elevation mechanism (for example, Endpoint Privilege Management or an equivalent) that is time-bound, purpose-scoped, and audited.

Do not add end users permanently to the local Administrators group solely to install Scout. Where a documented exception is required, capture the compensating endpoint controls (least-privilege workspace, endpoint DLP, endpoint monitoring) and the duration of the exception.

### Step 6: Set the default permission posture

Document the default posture for Scout shell command permissions (auto-approve / prompt / deny). Keep the default at **prompt** during the pilot unless a specific low-risk auto-approve list has been approved. Where feasible, back the pilot default with the documented **Force human approval for all non-read actions** (`ForcePrompt`) ADMX setting so the policy-level override applies regardless of local approval settings. Explicitly document that autonomous modes are not enabled for the pilot unless a separately approved low-risk scoping decision exists covering workspace, shell, browser, network, and M365 scope restrictions. Explicitly document that scheduled or triggered automations are not enabled without a separately approved unattended-execution decision; where the pilot posture is "off," back it with the documented **Disable Automations** (`DisableWorkflows`) ADMX setting.

### Step 7: Govern MCP servers, skills, providers, and models

Establish an approved-MCP-server inventory. For each proposed MCP server, capture the data path (local vs remote), authentication mechanism, and any external egress before approval. Treat MCP servers as connectors under [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md), with MCP-specific approval criteria added. Apply the same discipline to any skills added to the pilot. Where the pilot excludes specific MCP servers, permission types, providers, or models, back the decisions with the documented ADMX admin controls: **Disabled MCP servers** (`DisabledServers`), **Disabled permission kinds** (`DisabledPermissions`), **Disabled AI model providers** (`DisabledProviders`), and **Disabled AI models** (`DisabledModels`).

### Step 8: Map the storage and inference boundary

Document, for the pilot, which Scout data lives in OneDrive (session and memory data, subject to tenant controls) versus locally on the endpoint (automation instructions, MCP output — outside the M365 DPA), and where inference is processed (Microsoft, GitHub Copilot, third-party model providers — some inference outside M365 residency, retention, label enforcement, and eDiscovery). Record the residual risk acceptance and the compensating endpoint controls (DLP, endpoint monitoring, workspace scoping). Where the pilot restricts workspace file access or browser egress, back the decisions with the documented **Restrict file system access to workspace** (`RestrictToWorkspace`) and **Blocked browser egress origins** (`BrowserEgressBlockedOrigins`) ADMX settings.

### Step 9: Confirm supervision, audit, and incident-response coverage

Confirm which Scout activity is visible to existing Purview audit and supervision tooling, and document coverage gaps (local automation instructions, MCP output, third-party inference). Ensure the incident-response playbook covers independent revocation of Frontier scoping, endpoint policy, and GitHub Copilot entitlement, plus removal of the Microsoft 365 Copilot license where applicable, plus preservation of locally stored Scout artifacts. Define a preview-change review cadence that includes the ADMX admin controls documented in [Manage admin controls in Intune for Microsoft Scout](https://learn.microsoft.com/microsoft-scout/manage-group-policy).

## FSI Recommendations

| Tier | Recommendation |
|------|----------------|
| **Baseline** | Document all three gates (Frontier scope, endpoint policy + attestation, GitHub entitlement), reconcile pilot users against active M365 Copilot license (Control 1.9), plan the installer deployment pattern so users are not granted standing local Administrator rights, keep shell default at **prompt** (back with `ForcePrompt` where feasible), record the pilot posture for each documented ADMX admin control, maintain an approved-MCP inventory, and record the storage/inference boundary. |
| **Recommended** | Use a change register with named approvers per gate, separate approval from implementation, restrict Scout workspaces to defined scopes (back with `RestrictToWorkspace` where feasible), back the approved-MCP inventory and permission-type decisions with the documented ADMX admin controls (`DisabledServers`, `DisabledPermissions`, `BrowserEgressBlockedOrigins`, `DisableWorkflows`) rather than user-mode configuration, and confirm audit coverage explicitly rather than by assumption. |
| **Regulated** | All Recommended controls plus: dual technology + compliance approval before enabling any regulated population, `ForcePrompt` on where feasible, no autonomous modes and no unattended automations without separate approval (back the "off" posture with `DisableWorkflows`), third-party inference exclusions reflected in `DisabledProviders` / `DisabledModels`, examination-ready evidence retention (including ADMX policy snapshots and installation-privilege deployment records), and documented acceptance of the third-party inference and local-storage boundaries as known unsupported evidence. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to inspect Intune policy assignment, capture Windows registry evidence, and pull M365-side audit evidence.
- Use [Verification & Testing](verification-testing.md) to validate the three gates, permission posture, MCP inventory, and audit-coverage assessment.
- Keep [Troubleshooting](troubleshooting.md) available for entitlement, endpoint-policy, attestation, MCP, and boundary-related issues.

*FSI Copilot Governance Framework — Control 4.16 (Microsoft Scout, Frontier preview) · Last Verified 2026-07-10*
- Back to [Control 4.16](../../../controls/pillar-4-operations/4.16-microsoft-scout-governance.md)
