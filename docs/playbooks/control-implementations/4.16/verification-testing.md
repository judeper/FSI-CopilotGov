# Control 4.16: Microsoft Scout Governance - Verification & Testing

Test cases and evidence collection for validating the three Scout admin gates (Frontier scoping, endpoint policy + admin attestation, GitHub Copilot entitlement), the default permission posture, MCP-server governance, and the documented storage and inference boundary during the Frontier preview.

## Test Cases

### Test 1: Frontier Scoping Matches the Approved Pilot

- **Objective:** Confirm Frontier scoping in the Microsoft 365 admin center matches the approved pilot for Scout.
- **Expected Result:** Frontier scope for users and admin accounts matches the documented decision; users outside the pilot are not Frontier-scoped for Scout.
- **Evidence:** Frontier scoping record and an admin-center export or screenshot.

### Test 2: Endpoint Policy Is Deployed and Correctly Scoped

- **Objective:** Confirm the Windows ADMX-based `AllowScoutFrontierAccess` policy and/or the macOS custom `.mobileconfig` device profile are deployed to the approved pilot device group only.
- **Expected Result:** `scout-intune-windows-policies.csv` and `scout-intune-macos-profiles.csv` reflect the intended profiles; `scout-intune-out-of-scope-assignments.csv` is empty; a sampled Windows device shows the expected policy value in `scout-local-policy-sample.csv`.
- **Evidence:** Intune policy and assignment exports; local-policy sample; macOS `profiles show` output where applicable.

### Test 3: Admin Attestation Is Complete and Retained

- **Objective:** Confirm the admin attestation gate has been completed by an authorized admin and the record is retained as evidence.
- **Expected Result:** An admin-attestation record exists, names an authorized admin, and is stored in the governance evidence repository.
- **Evidence:** Attestation record.

### Test 4: GitHub Copilot Entitlement Matches the Approved Pilot

- **Objective:** Confirm users entitled through GitHub Copilot Business or Enterprise (with linked GitHub accounts) match the approved pilot list.
- **Expected Result:** Entitlement reconciliation from the GitHub administration surface matches the pilot list; users outside the pilot are not entitled.
- **Evidence:** GitHub entitlement export, reconciled to the pilot list and dated.

### Test 5: Installing the Application Alone Does Not Grant Access

- **Objective:** Confirm that installing the Scout application on a device that is not in the endpoint-policy scope, or for a user without GitHub Copilot Business/Enterprise entitlement, does not grant Scout functionality.
- **Expected Result:** Sign-in fails or Scout functionality is unavailable on out-of-scope endpoints or for unentitled users.
- **Evidence:** Test-device screenshots or a captured error state.

### Test 6: Shell Default Posture Is **Prompt** (or an Approved Auto-Approve List)

- **Objective:** Confirm the default shell command permission posture matches the approved decision.
- **Expected Result:** Default is **prompt** during the pilot, or the specific auto-approve list is documented and approved with low-risk justification.
- **Evidence:** Permission-mode decision record and (where applicable) the approved auto-approve list.

### Test 7: Autonomous Modes Are Disabled Without Separate Approval

- **Objective:** Confirm that Scout autonomous modes are not enabled unless a separately approved low-risk scoping decision exists.
- **Expected Result:** Autonomous modes are disabled, or the low-risk scoping decision is documented with workspace, shell, browser, network, and M365 scope restrictions and dual approval.
- **Evidence:** Autonomous-mode posture record.

### Test 8: Scheduled and Triggered Automations Are Disabled Without Separate Approval

- **Objective:** Confirm that unattended (scheduled or triggered) automations are not enabled for regulated populations without a separately approved unattended-execution decision.
- **Expected Result:** Unattended automations are disabled, or the unattended-execution decision is documented and approved.
- **Evidence:** Unattended-execution posture record.

### Test 9: Approved-MCP-Server Inventory Matches Configuration

- **Objective:** Confirm the approved-MCP-server inventory matches configured MCP servers, and each entry captures the data path, authentication mechanism, and external egress.
- **Expected Result:** No configured MCP server is outside the approved inventory; each entry has the required metadata; each server routes through extensibility governance under Control 4.13.
- **Evidence:** Approved-MCP-server inventory and configured-server reconciliation.

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
| Intune Scout policy and assignments | Intune / Microsoft Graph | CSV / JSON | Per retention policy |
| Local Windows ADMX policy sample | Sampled device registry read | CSV | Per retention policy |
| macOS profile installation evidence | Endpoint (`profiles show`) or Intune export | Text / plist | Per retention policy |
| Admin-attestation record | Governance workspace | PDF / Markdown | 7 years for regulated evidence sets |
| GitHub Copilot entitlement reconciliation | GitHub administration surface | CSV / Markdown | Per retention policy |
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
