# Control 4.16: Microsoft Scout Governance - Troubleshooting

Common issues and resolution steps for governing Microsoft Scout during its Frontier preview. Because Scout depends on three independent admin gates (Frontier scoping, endpoint policy + admin attestation, GitHub Copilot entitlement) and spans a mixed data-protection boundary (OneDrive vs local endpoint vs third-party inference), most issues resolve to a specific gate or a specific boundary rather than a single admin surface.

## Common Issues

### Issue 1: Scout Sign-In Fails Even After Installing the Application

- **Symptoms:** User installs the Scout desktop app but cannot sign in or the app reports no access.
- **Resolution:** Verify all three gates independently: (a) the user's account is in the Frontier scope in **Copilot > Settings > Frontier**; (b) the endpoint has the Scout endpoint policy applied — Windows ADMX-based `AllowScoutFrontierAccess` or macOS custom `.mobileconfig` device profile — and admin attestation has been completed; (c) the user holds a **GitHub Copilot Business or Enterprise** entitlement on a linked GitHub account. Installing the application alone grants nothing.

### Issue 2: Scout Works for the Wrong Users

- **Symptoms:** Users outside the approved pilot can sign in to Scout or gain functionality.
- **Resolution:** Reconcile all three gates against the approved pilot: Frontier scope, endpoint-policy assignment, and GitHub Copilot entitlement. A gap in any one gate can either block a pilot silently or entitle users the organization did not intend to enable. Restrict the mismatched gate to the approved pilot group and re-run reconciliation from the PowerShell setup.

### Issue 3: Endpoint Policy Not Applying on Windows

- **Symptoms:** The Scout ADMX policy is deployed in Intune but does not appear on a sampled Windows device, or Scout continues to be blocked or unblocked contrary to the intended state.
- **Resolution:** Confirm the device is in scope of the assignment (Intune reporting), that policy sync has completed, and that the ADMX namespace in the local policy hive matches the version verified from current Microsoft documentation. Re-verify the registry path used in the local sample script against current Scout ADMX guidance before treating output as evidence.

### Issue 4: Endpoint Policy Not Applying on macOS

- **Symptoms:** The custom `.mobileconfig` device profile is deployed in Intune but does not appear on a sampled macOS device.
- **Resolution:** Confirm the device is enrolled in the target device group, that the custom device configuration profile is present in Intune, and that the profile is installed on the device (`profiles show -type configuration`). Re-verify the payload against the Microsoft-provided `.mobileconfig` before treating output as evidence.

### Issue 5: Admin Attestation Missing or Not Retained

- **Symptoms:** No admin-attestation record exists in the governance workspace, or the record does not name an authorized admin.
- **Resolution:** Have an authorized admin complete the attestation step per current Microsoft documentation, capture the record, and store it in the governance evidence repository. Do not treat endpoint-policy deployment as a substitute for attestation — both are required gates.

### Issue 6: Shell Command Auto-Approve Broader Than Intended

- **Symptoms:** Scout is executing shell commands without prompting on actions the pilot did not intend to auto-approve.
- **Resolution:** Reset the default posture to **prompt** unless a specific low-risk auto-approve list has been approved. Any auto-approve list should be narrow and documented; treat auto-approve as an elevated permission and re-run the permission-mode review.

### Issue 7: Autonomous Mode Enabled Without Approval

- **Symptoms:** Scout is operating in an autonomous mode without a documented low-risk scoping decision.
- **Resolution:** Disable the autonomous mode. Re-enable only after a separately approved low-risk scoping decision covering workspace, shell, browser, network, and M365 scope restrictions is documented and, for regulated populations, dually approved by technology and compliance.

### Issue 8: Unattended Automation Running for a Regulated Population

- **Symptoms:** A scheduled or triggered Scout automation is running unattended for a regulated user population without a separately approved unattended-execution decision.
- **Resolution:** Disable the automation. Re-enable only after the unattended-execution decision is documented and approved, and add the automation to the supervisory review scope where its outputs contribute to client-facing work or recordkeeping.

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

1. Confirm Frontier scoping for the affected user or admin account in the Microsoft 365 admin center.
2. Confirm Intune endpoint-policy assignment covers the affected device group (Windows ADMX or macOS profile).
3. Verify on a sampled device that the endpoint policy is applied (Windows registry sample; macOS `profiles show`).
4. Confirm the admin attestation record exists and names an authorized admin.
5. Reconcile GitHub Copilot Business or Enterprise entitlement for the affected user.
6. Review the shell permission default, autonomous-mode posture, and unattended-automation posture against the documented decisions.
7. Reconcile the configured MCP servers against the approved-MCP-server inventory.
8. Consult the storage-and-inference boundary documentation and the evidence-gap manifest before treating a coverage question as a bug.

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
