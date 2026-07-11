# Control 4.16: Microsoft Scout Governance - Verification & Testing

Test cases and evidence collection for validating the three Scout admin gates (Frontier scoping, endpoint policy + admin attestation, GitHub Copilot entitlement), the default permission posture, MCP-server governance, and the documented storage and inference boundary during the Frontier preview.

## Test Cases

### Test 1: Frontier Scoping Matches the Approved Pilot

- **Objective:** Confirm Frontier scoping in the Microsoft 365 admin center matches the approved pilot for Scout.
- **Expected Result:** Frontier scope for users and admin accounts matches the documented decision; users outside the pilot are not Frontier-scoped for Scout.
- **Evidence:** Frontier scoping record and an admin-center export or screenshot.

### Test 2: Endpoint Policy Is Deployed and Correctly Scoped

- **Objective:** Confirm the Windows imported administrative-template policy enables **Allow Microsoft Scout Frontier access** (the `AllowScoutFrontierAccess` capability) and the macOS custom `.mobileconfig` device profile are deployed to the approved pilot device group only.
- **Expected Result:** `scout-intune-windows-policies.csv` and `scout-intune-macos-profiles.csv` reflect the intended profiles; `scout-intune-out-of-scope-assignments.csv` is empty; a sampled Windows device shows the expected policy value in `scout-local-policy-sample.csv`.
- **Evidence:** Intune policy and assignment exports; local-policy sample; macOS `profiles show` output where applicable.

### Test 2b: Documented ADMX Admin Controls Are Configured to the Approved Pilot Posture

- **Objective:** Confirm the pilot posture is recorded (and, where applicable, configured) for each of the ten ADMX admin controls documented in [Manage admin controls in Intune for Microsoft Scout](https://learn.microsoft.com/microsoft-scout/manage-group-policy): `PolicyVersion`, `DisabledServers`, `DisabledPermissions`, `ForcePrompt`, `DisabledModels`, `DisabledProviders`, `DisableHeartbeat`, `DisableWorkflows`, `RestrictToWorkspace`, and `BrowserEgressBlockedOrigins`.
- **Expected Result:** For each setting, the pilot posture is documented (with citation to current Microsoft documentation) and reconciled to the sampled `HKLM\SOFTWARE\Policies\Scout` values captured in `scout-local-policy-sample.csv`. Where a setting is "not configured / verify against current Microsoft default," the documentation notes that explicitly. For settings that materially reduce blast radius (`DisabledServers`, `DisabledPermissions`, `ForcePrompt`, `DisabledProviders`, `DisableWorkflows`, `RestrictToWorkspace`, `BrowserEgressBlockedOrigins`), values match the approved-MCP inventory, permission-type decision, unattended-execution decision, workspace-scoping standard, third-party inference exclusion decision, and browser-egress decision respectively.
- **Evidence:** Pilot posture record for each ADMX setting; `scout-local-policy-sample.csv`; Intune policy export showing configured values.

### Test 3: Admin Attestation Is Complete and Retained

- **Objective:** Confirm the admin attestation and opt-in gate (Microsoft's Frontier organization sign-up form) has been completed by an authorized admin and the record is retained as evidence.
- **Expected Result:** An admin-attestation record exists, names an authorized admin, and is stored in the governance evidence repository. Microsoft states this attestation is an additional gating layer beyond Frontier enrollment because Scout can route data outside Microsoft 365 to third-party inference paths.
- **Evidence:** Attestation record.

### Test 4a: Microsoft 365 Copilot License Assignment Matches the Approved Pilot

- **Objective:** Confirm pilot users hold an active Microsoft 365 Copilot license, per Microsoft's [Get started with Microsoft Scout](https://learn.microsoft.com/microsoft-scout/get-started) prerequisites and Control 1.9.
- **Expected Result:** `scout-m365-copilot-license-reconciliation.csv` shows every pilot user has `HasM365CopilotLicense = TRUE`. Users outside the pilot are not assigned a Microsoft 365 Copilot license solely as a Scout prerequisite.
- **Evidence:** License-reconciliation CSV and the current SKU part number verified against the Microsoft 365 admin center.

### Test 4b: GitHub Copilot Entitlement Matches the Approved Pilot

- **Objective:** Confirm users entitled through GitHub Copilot Business or Enterprise (with linked GitHub accounts) match the approved pilot list.
- **Expected Result:** Entitlement reconciliation from the GitHub administration surface matches the pilot list; users outside the pilot are not entitled.
- **Evidence:** GitHub entitlement export, reconciled to the pilot list and dated.

### Test 4c: Installer Deployment Follows the Least-Privilege Pattern

- **Objective:** Confirm the Scout installer is deployed through a system-context managed deployment (Intune) or a just-in-time elevation mechanism so end users are not granted standing local Administrator rights solely to install Scout.
- **Expected Result:** A documented deployment-pattern record exists; standing local Administrator group membership is not granted to pilot users for the purpose of installing Scout. Where a documented exception exists, it names the compensating endpoint controls and duration.
- **Evidence:** Deployment-pattern record; Intune app assignment export or elevation-tool report; local-admin group membership review for a sampled endpoint.

### Test 5: Installing the Application Alone Does Not Grant Access

- **Objective:** Confirm that installing the Scout application on a device that is not in the endpoint-policy scope, or for a user without the required per-user prerequisites (active Microsoft 365 Copilot license and GitHub Copilot Business or Enterprise entitlement), does not grant Scout functionality.
- **Expected Result:** Sign-in fails or Scout functionality is unavailable on out-of-scope endpoints or for users missing either license. Microsoft states that sign-in failures do not always show a clear in-product indication of the cause — troubleshooting starts at the admin gates and per-user prerequisites.
- **Evidence:** Test-device screenshots or a captured error state, plus the applicable gate/prerequisite record.

### Test 6: Shell Default Posture Is **Prompt** (or an Approved Auto-Approve List) and, Where Feasible, Backed by `ForcePrompt`

- **Objective:** Confirm the default shell command permission posture matches the approved decision and, where feasible, is backed by the documented **Force human approval for all non-read actions** (`ForcePrompt`) ADMX setting.
- **Expected Result:** Default is **prompt** during the pilot, or the specific auto-approve list is documented and approved with low-risk justification; where the pilot backs the default with `ForcePrompt`, the value is set to enable the setting and is captured in `scout-local-policy-sample.csv`.
- **Evidence:** Permission-mode decision record, (where applicable) the approved auto-approve list, and the sampled `ForcePrompt` value.

### Test 7: Autonomous Modes Are Disabled Without Separate Approval

- **Objective:** Confirm that Scout autonomous modes are not enabled unless a separately approved low-risk scoping decision exists.
- **Expected Result:** Autonomous modes are disabled, or the low-risk scoping decision is documented with workspace, shell, browser, network, and M365 scope restrictions and dual approval.
- **Evidence:** Autonomous-mode posture record.

### Test 8: Scheduled and Triggered Automations Are Disabled Without Separate Approval

- **Objective:** Confirm that unattended (scheduled or triggered) automations are not enabled for regulated populations without a separately approved unattended-execution decision, and that the "off" posture is backed by the documented `DisableWorkflows` ADMX setting where feasible.
- **Expected Result:** Unattended automations are disabled (Scout's ADMX `DisableWorkflows` is set to disable Automations) or the unattended-execution decision is documented and approved.
- **Evidence:** Unattended-execution posture record and the sampled `DisableWorkflows` value.

### Test 9: Approved-MCP-Server Inventory Matches Configuration and, Where Applicable, `DisabledServers` Reflects the Exclusion

- **Objective:** Confirm the approved-MCP-server inventory matches configured MCP servers, that each entry captures the data path, authentication mechanism, and external egress, and that where the pilot excludes MCP servers, the exclusion is reflected in the documented `DisabledServers` ADMX setting.
- **Expected Result:** No configured MCP server is outside the approved inventory; each entry has the required metadata; each server routes through extensibility governance under Control 4.13; the `DisabledServers` value matches the exclusion decision.
- **Evidence:** Approved-MCP-server inventory, configured-server reconciliation, and the sampled `DisabledServers` value.

### Test 9b: Permission-Type Exclusions Are Reflected in `DisabledPermissions`

- **Objective:** Confirm any pilot-level exclusion of permission types (Microsoft's examples: `shell`, `write`, `mcp`, `url`, `custom-tool`) is reflected in the documented `DisabledPermissions` ADMX setting.
- **Expected Result:** `DisabledPermissions` reflects the pilot's approved permission-type posture; where no exclusion is required, the pilot posture is documented as such.
- **Evidence:** Permission-type decision record and the sampled `DisabledPermissions` value.

### Test 9c: Third-Party Inference Exclusions Are Reflected in `DisabledProviders` and `DisabledModels`

- **Objective:** Confirm the pilot's third-party inference exclusion decision — including whether the Anthropic model family or OpenAI is scoped out — is reflected in the documented `DisabledProviders` and/or `DisabledModels` ADMX settings.
- **Expected Result:** `DisabledProviders` and `DisabledModels` reflect the third-party inference exclusion decision recorded in the storage-and-inference boundary documentation. Where no exclusion is required, the pilot posture is documented as such.
- **Evidence:** Third-party inference decision record and the sampled `DisabledProviders` / `DisabledModels` values.

### Test 9d: Workspace Scoping Is Reflected in `RestrictToWorkspace`

- **Objective:** Confirm the pilot's workspace-scoping standard is reflected in the documented `RestrictToWorkspace` ADMX setting where feasible.
- **Expected Result:** `RestrictToWorkspace` is enabled where the pilot standard requires file system and shell access to be limited to the current workspace, or the pilot posture is documented if the default remains in place.
- **Evidence:** Workspace-scoping standard and the sampled `RestrictToWorkspace` value.

### Test 9e: Browser Egress Restrictions Are Reflected in `BrowserEgressBlockedOrigins`

- **Objective:** Confirm the pilot's browser destination posture is reflected in the documented `BrowserEgressBlockedOrigins` ADMX setting where feasible.
- **Expected Result:** `BrowserEgressBlockedOrigins` matches the pilot's blocked origins list, or the pilot posture is documented if no origins are blocked. Recognize that this setting blocks HTTP or HTTPS origins from Playwright browser traffic — it is not a substitute for endpoint browser management.
- **Evidence:** Browser-egress decision record and the sampled `BrowserEgressBlockedOrigins` value.

### Test 9f: Heartbeat Posture Is Reflected in `DisableHeartbeat`

- **Objective:** Confirm the pilot's posture for Scout's Heartbeat monitoring feature is documented and reflected in the `DisableHeartbeat` ADMX setting where feasible.
- **Expected Result:** `DisableHeartbeat` matches the pilot posture (enabled to disable Heartbeat, or left unconfigured with a documented decision).
- **Evidence:** Heartbeat-posture decision record and the sampled `DisableHeartbeat` value.

### Test 10: Storage and Inference Boundary Is Documented

- **Objective:** Confirm the governance record identifies which Scout data lives in OneDrive versus locally on the endpoint, and identifies third-party inference as outside M365 protections.
- **Expected Result:** Documentation names OneDrive-stored data (session, memory), locally stored data (automation instructions, MCP output — outside the M365 DPA), and third-party inference (outside M365 residency, retention, label enforcement, and eDiscovery). Residual-risk acceptance is recorded.
- **Evidence:** Boundary documentation and risk-acceptance record.

### Test 11: Audit and Supervision Coverage Assessment Is Complete

- **Objective:** Confirm a documented assessment names what Scout activity is captured by Purview and which categories are known unsupported evidence.
- **Expected Result:** Assessment names captured activity (M365-sourced admin/agent events) and known gaps (local shell execution, automation instructions, MCP output, third-party inference, sensitivity-label inheritance on generated content), each with a remediation owner or a documented risk acceptance.
- **Evidence:** Coverage assessment and evidence-gap manifest.

### Test 12: Incident-Response Playbook Covers Independent Gate Revocation

- **Objective:** Confirm the incident-response playbook covers independent revocation of Frontier scoping, endpoint policy, and GitHub Copilot entitlement, plus preservation of locally stored Scout artifacts.
- **Expected Result:** Playbook names the revocation owner and steps for each gate and describes preservation of local automation instructions and MCP output for investigation.
- **Evidence:** Incident-response playbook excerpt.

### Test 13: Sensitivity-Label Behavior on Generated Content Is Acknowledged

- **Objective:** Confirm the governance record acknowledges that Scout can display sensitivity labels but that generated or modified content may not reliably inherit them.
- **Expected Result:** Documented acceptance that automatic label inheritance is not a compensating control for Scout outputs; any additional compensating discipline (for example, endpoint DLP, workspace scoping) is named.
- **Evidence:** Label-behavior acknowledgment.

### Test 14: External Content Is Treated as Untrusted

- **Objective:** Confirm the governance record acknowledges that Scout treats external content (web, files outside the workspace, MCP server output) as untrusted, and that prompt-injection resistance is a platform responsibility rather than a customer-configurable control.
- **Expected Result:** Documented acknowledgment and any complementary controls (for example, workspace scoping, browser-navigation restrictions) named.
- **Evidence:** Untrusted-content acknowledgment.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|---------------|--------|--------|-----------|
| Frontier scoping record | Governance workspace | CSV / Markdown | Per retention policy |
| Intune Scout policy and assignments (including documented ADMX admin controls) | Intune / Microsoft Graph | CSV / JSON | Per retention policy |
| Local Windows ADMX policy sample (all documented `HKLM\SOFTWARE\Policies\Scout` values) | Sampled device registry read | CSV | Per retention policy |
| macOS profile installation evidence | Endpoint (`profiles show`) or Intune export | Text / plist | Per retention policy |
| Admin-attestation record (Microsoft's Frontier organization sign-up) | Governance workspace | PDF / Markdown | 7 years for regulated evidence sets |
| Microsoft 365 Copilot license reconciliation | Microsoft Graph / M365 admin center | CSV / Markdown | Per retention policy |
| GitHub Copilot entitlement reconciliation | GitHub administration surface | CSV / Markdown | Per retention policy |
| Installation-privilege deployment record (system-context, JIT elevation, or exception) | Governance workspace / Intune app assignments | Markdown / CSV | Per retention policy |
| ADMX admin-control posture record (per setting) | Governance workspace | Markdown / CSV | 7 years for regulated evidence sets |
| Permission-mode decision (shell / autonomous / unattended) | Governance workspace | Markdown | 7 years for regulated evidence sets |
| Approved-MCP-server inventory | Governance workspace | CSV / Markdown | Per retention policy |
| Storage and inference boundary documentation | Governance workspace | Markdown | 7 years for regulated evidence sets |
| M365 audit subset for Scout-related activity | Unified audit log | CSV | 7 years for regulated evidence sets |
| Evidence-gap manifest | Governance workspace | Text / Markdown | Per retention policy |
| Incident-response playbook excerpt | Governance workspace | Markdown | Per retention policy |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework — Control 4.16 (Microsoft Scout, Frontier preview) · Last Verified 2026-07-10*
- Back to [Control 4.16](../../../controls/pillar-4-operations/4.16-microsoft-scout-governance.md)
