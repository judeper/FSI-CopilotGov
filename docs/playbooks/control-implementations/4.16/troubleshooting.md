# Control 4.16: Microsoft Scout Governance - Troubleshooting

Common issues and resolution steps for governing Microsoft Scout during its Frontier preview. Because Scout depends on three independent admin gates (Frontier scoping, endpoint policy + admin attestation, GitHub Copilot entitlement) and spans a mixed data-protection boundary (OneDrive vs local endpoint vs third-party inference), most issues resolve to a specific gate or a specific boundary rather than a single admin surface.

## Common Issues

### Issue 1: Scout Sign-In Fails Even After Installing the Application

- **Symptoms:** User installs the Scout desktop app but cannot sign in, or the app reports no access. Microsoft states that sign-in failures do not always show a clear in-product indication of the cause.
- **Resolution:** Verify all three admin gates and both per-user prerequisites independently: (a) the user's account is in Frontier scope in **Copilot > Settings > View all > Copilot Frontier** and the change has propagated (Microsoft cites up to about three hours); (b) the endpoint has the Scout endpoint policy applied — the imported Microsoft Scout ADMX/ADML with **Allow Microsoft Scout Frontier access** enabled on Windows, or the Microsoft-provided macOS `.mobileconfig` — and Microsoft's Frontier organization sign-up (admin attestation) is complete; (c) the user holds an **active Microsoft 365 Copilot license**; (d) the user holds a **GitHub Copilot Business or Enterprise** entitlement on a linked GitHub account. Installing the application alone grants nothing, and Microsoft directs troubleshooting to the admin gates and per-user prerequisites before investigating on the client.

### Issue 1b: End User Cannot Install Scout Because They Lack Local Administrator Rights

- **Symptoms:** End user attempts to install the Scout desktop app and the installer fails or is blocked because the account is not in the local Administrators group.
- **Resolution:** Do not resolve by granting standing local Administrator rights. Microsoft requires local Administrator permissions to install Scout but not for ongoing use. Deploy the Scout installer through a system-context managed deployment in Intune (or an equivalent MDM) so end users do not need local admin at any point, or use a just-in-time local admin elevation mechanism (for example, Endpoint Privilege Management or an equivalent) that is time-bound, purpose-scoped, and audited. Where a documented exception is required, record the compensating endpoint controls and duration in the governance workspace.

### Issue 1c: Pilot User Signs Into Scout Without an Active Microsoft 365 Copilot License

- **Symptoms:** A user in the approved pilot cannot sign in, or sign-in appears to succeed but Copilot capabilities are unavailable.
- **Resolution:** Reconcile the user's account against Microsoft 365 Copilot license assignment (per Control 1.9). Microsoft's [Get started with Microsoft Scout](https://learn.microsoft.com/microsoft-scout/get-started) lists an active Microsoft 365 Copilot license as a per-user prerequisite. Do not treat GitHub Copilot Business or Enterprise entitlement as a substitute for the Microsoft 365 Copilot license — Microsoft states that a GitHub Copilot license alone doesn't grant Frontier access, nor does Frontier access alone work without a Copilot license (business or enterprise).

### Issue 2: Scout Works for the Wrong Users

- **Symptoms:** Users outside the approved pilot can sign in to Scout or gain functionality.
- **Resolution:** Reconcile all three gates against the approved pilot: Frontier scope, endpoint-policy assignment, and GitHub Copilot entitlement. A gap in any one gate can either block a pilot silently or entitle users the organization did not intend to enable. Restrict the mismatched gate to the approved pilot group and re-run reconciliation from the PowerShell setup.

### Issue 3: Endpoint Policy Not Applying on Windows

- **Symptoms:** The imported Microsoft Scout administrative-template policy (or one of its ADMX admin controls) is deployed in Intune but does not appear on a sampled Windows device, or Scout continues to be blocked or unblocked contrary to the intended state.
- **Resolution:** Confirm the device is in scope of the assignment (Intune reporting), that policy sync has completed, and that the values under `HKLM\SOFTWARE\Policies\Scout` match the intended pilot posture for **Allow Microsoft Scout Frontier access** (`AllowScoutFrontierAccess`) and for the documented admin controls (`DisabledServers`, `DisabledPermissions`, `ForcePrompt`, `DisabledModels`, `DisabledProviders`, `DisableHeartbeat`, `DisableWorkflows`, `RestrictToWorkspace`, `BrowserEgressBlockedOrigins`, `PolicyVersion`). Re-verify the ADMX namespace and value names against current Microsoft documentation ([Set up Microsoft Scout with Intune](https://learn.microsoft.com/microsoft-scout/admin-intune-setup), [Manage admin controls in Intune for Microsoft Scout](https://learn.microsoft.com/microsoft-scout/manage-group-policy)) before treating output as evidence.

### Issue 4: Endpoint Policy Not Applying on macOS

- **Symptoms:** The custom `.mobileconfig` device profile is deployed in Intune but does not appear on a sampled macOS device.
- **Resolution:** Confirm the device is enrolled in the target device group, that the custom device configuration profile is present in Intune, and that the profile is installed on the device (`profiles show -type configuration`). Re-verify the payload against the Microsoft-provided `.mobileconfig` before treating output as evidence.

### Issue 5: Admin Attestation Missing or Not Retained

- **Symptoms:** No admin-attestation record exists in the governance workspace, or the record does not name an authorized admin.
- **Resolution:** Have an authorized admin complete the Frontier organization sign-up (admin attestation) form per Microsoft's [Admin access overview for Microsoft Scout](https://learn.microsoft.com/microsoft-scout/admin-access-overview), capture the record, and store it in the governance evidence repository. Microsoft states that this attestation is an additional gating layer beyond Frontier enrollment because Scout can route data outside Microsoft 365 to third-party inference paths — do not treat endpoint-policy deployment as a substitute for attestation. Both are required gates.

### Issue 6: Shell Command Auto-Approve Broader Than Intended

- **Symptoms:** Scout is executing shell commands without prompting on actions the pilot did not intend to auto-approve.
- **Resolution:** Reset the default posture to **prompt** unless a specific low-risk auto-approve list has been approved. Any auto-approve list should be narrow and documented; treat auto-approve as an elevated permission and re-run the permission-mode review. Where the pilot needs a policy-level override, enable the documented **Force human approval for all non-read actions** (`ForcePrompt`) ADMX setting so user-mode auto-approve settings for non-read actions are overridden regardless of local approval configuration.

### Issue 6b: Blocked Provider, Model, or MCP Server Still Appears Available in Scout

- **Symptoms:** A provider (for example, Anthropic or OpenAI), model, or MCP server (for example, `filesystem`, `playwright`, `WorkIQ`) that the pilot intended to exclude still appears available in the Scout UI or is invoked by a task.
- **Resolution:** Confirm the exclusion is reflected in the documented ADMX admin controls — **Disabled AI model providers** (`DisabledProviders`) for providers, **Disabled AI models** (`DisabledModels`) for models, and **Disabled MCP servers** (`DisabledServers`) for MCP servers — using the values documented in [Manage admin controls in Intune for Microsoft Scout](https://learn.microsoft.com/microsoft-scout/manage-group-policy). Verify the policy is assigned to the affected device group and applied on the sampled device (`HKLM\SOFTWARE\Policies\Scout`). User-mode preference is not a substitute for a policy-level exclusion.

### Issue 6c: Scout Writes Files Outside the Intended Workspace

- **Symptoms:** Scout reads or writes files outside the intended pilot workspace, or issues shell commands whose file-system reach exceeds the workspace-scoping standard.
- **Resolution:** Confirm the workspace-scoping standard is backed by the documented **Restrict file system access to workspace** (`RestrictToWorkspace`) ADMX setting where feasible. Reset any user-mode workspace configuration to the pilot's approved scope and re-verify on a sampled device.

### Issue 6d: Playwright Browser Reaches an Origin the Pilot Intended to Block

- **Symptoms:** Scout's Playwright browser navigates to or exchanges data with an HTTP or HTTPS origin the pilot intended to block.
- **Resolution:** Confirm the origin is listed in the documented **Blocked browser egress origins** (`BrowserEgressBlockedOrigins`) ADMX setting and that the policy is applied on the sampled device. Recognize that this setting is not a substitute for endpoint browser management; coordinate with endpoint-security and DLP owners.

### Issue 6e: Heartbeat Feature Is Enabled or Disabled Contrary to the Pilot Decision

- **Symptoms:** Scout's Heartbeat monitoring feature is running (or not running) contrary to the pilot's documented posture.
- **Resolution:** Confirm the pilot posture is reflected in the documented **Disable Heartbeat** (`DisableHeartbeat`) ADMX setting. Where the pilot has not made an explicit decision, record the current behavior and defer to a separately documented Heartbeat decision.

### Issue 7: Autonomous Mode Enabled Without Approval

- **Symptoms:** Scout is operating in an autonomous mode without a documented low-risk scoping decision.
- **Resolution:** Disable the autonomous mode. Re-enable only after a separately approved low-risk scoping decision covering workspace, shell, browser, network, and M365 scope restrictions is documented and, for regulated populations, dually approved by technology and compliance.

### Issue 8: Unattended Automation Running for a Regulated Population

- **Symptoms:** A scheduled or triggered Scout automation is running unattended for a regulated user population without a separately approved unattended-execution decision.
- **Resolution:** Disable the automation. Re-enable only after the unattended-execution decision is documented and approved, and add the automation to the supervisory review scope where its outputs contribute to client-facing work or recordkeeping. Where the pilot posture is "off," back it with the documented **Disable Automations** (`DisableWorkflows`) ADMX setting so user-mode configuration cannot re-enable automations without a policy change.

### Issue 9: MCP Server Configured Outside the Approved Inventory

- **Symptoms:** A configured MCP server is not present on the approved inventory, or the inventory entry is missing data path, authentication, or egress metadata.
- **Resolution:** Restrict or remove the unapproved MCP server, complete the inventory entry with the required metadata, and route the server through extensibility governance under [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md) before re-enablement.

### Issue 10: Scout Output Contains Content That Should Be Labeled

- **Symptoms:** A file generated or modified by Scout does not carry the sensitivity label expected from its source content.
- **Resolution:** Recognize that generated or modified Scout content may not reliably inherit sensitivity labels. Do not rely on automatic inheritance as a compensating control. Apply labels manually where appropriate, and reinforce the compensating discipline documented in the boundary record (for example, endpoint DLP, workspace scoping, review of Scout outputs).

### Issue 11: Purview Audit Does Not Show Expected Scout Activity

- **Symptoms:** Expected Scout activity does not appear in Purview unified-audit-log pulls.
- **Resolution:** Recognize that Purview captures only the M365-sourced subset of Scout activity. Local shell execution, MCP output, automation instructions, and third-party inference are outside M365 protections and are not captured by Purview. Source those categories from endpoint tooling, and document the coverage as **known unsupported evidence** rather than a Purview configuration bug.

### Issue 12: Session or Memory Data Retention Concern in OneDrive

- **Symptoms:** Session or memory data in OneDrive is not aligning with the organization's retention posture.
- **Resolution:** Confirm the tenant controls applied to OneDrive apply as expected to Scout session and memory storage, and re-verify against current Microsoft documentation. Coordinate with OneDrive tenant controls owners and update the boundary documentation.

### Issue 13: Automation Instructions or MCP Output Requested for eDiscovery

- **Symptoms:** eDiscovery request cannot locate Scout automation instructions or MCP output.
- **Resolution:** Recognize that automation instructions and MCP output are stored locally on the endpoint and are **outside the M365 DPA**. Source these from the endpoint through incident-response or endpoint tooling. This is a documented boundary of Scout during preview, not an eDiscovery configuration bug — document the coverage gap for legal, compliance, and eDiscovery stakeholders.

### Issue 14: Third-Party Inference Content Requested for eDiscovery or Retention Hold

- **Symptoms:** Legal, compliance, or eDiscovery requests cover Scout content that was processed through GitHub Copilot or a third-party model provider.
- **Resolution:** Recognize that content processed through third-party inference is outside M365 residency, retention, sensitivity-label enforcement, and eDiscovery. Consult the third-party provider's terms and the organization's third-party risk records. Document that this boundary is a known gap during preview and reflect it in the boundary documentation and evidence-gap manifest.

### Issue 15: External Web Content Appears to Influence Scout Behavior Unexpectedly

- **Symptoms:** Scout appears to take actions consistent with instructions embedded in retrieved web content or MCP server output.
- **Resolution:** Recognize that Scout tags external content as **untrusted**, but prompt-injection resistance is a Microsoft platform responsibility rather than a customer-configurable control. Report the behavior to Microsoft through Frontier preview feedback channels, restrict the browser or MCP surface, and document the incident with local artifacts preserved.

## Diagnostic Steps

1. Confirm Frontier scoping for the affected user or admin account in the Microsoft 365 admin center, including propagation time.
2. Confirm Intune endpoint-policy assignment covers the affected device group (Windows imported administrative template with **Allow Microsoft Scout Frontier access** and the documented ADMX admin controls, or macOS `.mobileconfig`).
3. Verify on a sampled device that the endpoint policy is applied (Windows registry sample of `HKLM\SOFTWARE\Policies\Scout` for all documented values; macOS `profiles show`).
4. Confirm the admin attestation record (Microsoft's Frontier organization sign-up) exists and names an authorized admin.
5. Reconcile Microsoft 365 Copilot license assignment (per Control 1.9) for the affected user.
6. Reconcile GitHub Copilot Business or Enterprise entitlement for the affected user.
7. Confirm the deployment pattern for the Scout installer did not require granting standing local Administrator rights on the endpoint.
8. Review the shell permission default (and `ForcePrompt` where applied), autonomous-mode posture, and unattended-automation posture (`DisableWorkflows` where applied) against the documented decisions.
9. Reconcile the configured MCP servers (and any `DisabledServers` / `DisabledPermissions` values) against the approved-MCP-server inventory and permission-type decision.
10. Reconcile any `DisabledProviders` / `DisabledModels` values against the third-party inference exclusion decision.
11. Consult the storage-and-inference boundary documentation and the evidence-gap manifest before treating a coverage question as a bug.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Documentation gap or single out-of-scope entitlement | Governance analyst |
| Medium | Endpoint policy or Frontier scope drift, unapproved MCP server, shell auto-approve broader than intended | Governance lead and M365 or endpoint admin |
| High | Autonomous mode or unattended automation enabled for a regulated population without separate approval | Compliance lead, endpoint admin, and Copilot admin |
| High | eDiscovery or retention request cannot be satisfied for Scout local artifacts or third-party inference content | Legal, compliance, and eDiscovery leads |
| Critical | Scout action against regulated data outside approved governance, or evidence of prompt-injection-influenced action against regulated data | CISO, compliance officer, incident-response lead; preserve local artifacts and coordinate with Microsoft through Frontier preview feedback channels |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework — Control 4.16 (Microsoft Scout, Frontier preview) · Last Verified 2026-07-10*
- Back to [Control 4.16](../../../controls/pillar-4-operations/4.16-microsoft-scout-governance.md)
