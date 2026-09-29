# Control 3.1: Copilot Interaction Audit Logging — Portal Walkthrough

Step-by-step portal configuration for enabling comprehensive audit logging of all Microsoft 365 Copilot interactions to support compliance with FSI regulatory requirements.

## Prerequisites

- **Role:** `Audit Logs` or `View-Only Audit Logs` in Microsoft Purview Audit for search and export. If you also use `Search-UnifiedAuditLog`, assign the same role capability in the Exchange admin center / Exchange Online role groups. For the retention-policy step below, Microsoft documents the `Organization Configuration` role in Microsoft Purview as required.
- **License:** Microsoft 365 E5 or E5 Compliance add-on (or PAYG Audit billing configured)
- **Access:** Microsoft Purview portal

## Steps

### Step 1: Verify Unified Audit Log Is Enabled

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Audit

1. Navigate to the Audit solution in the Purview portal.
2. Confirm the banner reads "Audit is turned on" — if not, click **Start recording user and admin activity**.
3. Note that changes may take up to 60 minutes to propagate across the tenant.

### Step 2: Configure Copilot-Specific Audit Activities

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Audit > Search

1. In the **Activities - friendly names** filter, expand **Copilot activities** to view the current Copilot-specific operations.
2. Confirm that `CopilotInteraction` is available for Microsoft Copilot interactions and that the current Teams/Facilitator activity names (`AINotesUpdate`, `LiveNotesUpdate`, `TeamCopilotMsgInteraction`) appear under the Teams-related activity lists when those scenarios are in scope.
3. If your review covers Microsoft 365 Copilot administration, confirm the current admin operations you plan to monitor (for example `CreatePlugin`, `DeletePlugin`, `EnablePlugin`, `DisableCopilotPlugin`, `UpdatePlugin`, `EnablePromptBook`, `DisablePromptBook`, `UpdatePromptBook`, `UpdateTenantSettings`) match the Microsoft audit catalog.
4. To search for agent-specific events, use the **Record type** filter and select `CopilotAgentManagement`.

### Step 3: Search for New Audit Schema Fields

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Audit > Search > Export results

To surface the expanded audit schema fields — the top-level `AgentId`, `AgentName`, and `SensitivityLabelId`, plus the nested `AccessedResources.XPIADetected` and `Messages.JailbreakDetected` sub-properties:

1. Run a `CopilotInteraction` search for your desired date range and export results to CSV.
2. Open the exported CSV and review the **AuditData** column (JSON format) for the new fields.
3. When reviewing agent-assisted interactions, the `AgentId` and `AgentName` fields identify which Copilot agent was invoked — use these to map agent usage to FINRA Rule 3110 supervisory records.
4. Parse the **AuditData** JSON and flag records where any `Messages[].JailbreakDetected` sub-property is `true` — these events require security escalation per FFIEC incident response standards.
5. Use `SensitivityLabelId` values to cross-reference against your label inventory and verify that Copilot respected label-based access boundaries.

### Step 4: Enable Audit (Premium) for Extended Retention

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Audit > Audit retention policies

1. Click **New audit retention policy**.
2. Set **Record type** to `CopilotInteraction`.
3. Set **Duration** to 10 years (FSI regulated recommendation; minimum 6 years per SEC Rule 17a-4(a)).
4. Set **Priority** to a value higher than the default retention policy.
5. Click **Save** to apply.
6. Create a second policy for agent record types:
   - **Record types:** Select `CopilotAgentManagement`
   - **Duration:** 7 years in the portal (or 10 years if your policy standard prefers additional headroom). The Purview portal does not expose a 6-year option, and Microsoft requires the 10-year Audit Log Retention add-on for the portal's 3-, 5-, and 7-year options, and for the 10-year option.
   - **Priority:** Same as the Copilot interaction policy

> **Role note:** Use an account with the `Organization Configuration` role for the retention-policy step. Search-only roles such as `Audit Logs` / `View-Only Audit Logs` aren't sufficient to create or modify audit retention policies.

### Step 5: Configure Agent-Specific Record Type Navigation

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Audit > Search

To search for agent administrative events in the portal:

1. In the Audit search interface, set the date range.
2. In the **Record type** filter (advanced search options), select `CopilotAgentManagement` to find agent configuration changes.
4. Combine with the **User** filter to scope searches to specific administrators who manage Copilot agents.
5. Export results and use the `AgentId` field to trace which agents were created, modified, or deleted.

### Step 6: Configure Audit Log Alert Policies

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Policies > Alert policies

> **Permission note:** This step requires policy-management permissions beyond the search-only `Audit Logs` / `View-Only Audit Logs` roles. Use the alert-policy administration role assignment your tenant documents for Purview policy management.

1. Create a new alert policy for unusual Copilot interaction volume.
2. Set the activity to `CopilotInteraction` with threshold of more than 500 events per hour per user.
3. Do not assume `JailbreakDetected` is a first-class alert activity. Microsoft documents it as a nested `Messages[].JailbreakDetected` property inside `CopilotInteraction` audit data, so detect it by exporting or ingesting `CopilotInteraction` records and parsing the JSON downstream (for example, in a SIEM).
4. Assign alert recipients to the compliance monitoring team distribution group.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Audit log status | Enabled | Enabled | Enabled |
| CopilotInteraction retention | 180 days | 1 year | 7-10 years |
| CopilotAgentManagement retention | Not required | 1 year | 7-10 years |
| Copilot activity alerts | Optional | Recommended | Required |
| JailbreakDetected review automation | Optional | Recommended | Required |
| Audit Premium or PAYG | Optional | Recommended | Required |
| Agent record type searches | Optional | Recommended | Required |

## Regulatory Alignment

- **SEC Rule 17a-4(a)** — Six-year retention requirement drives the regulated-tier audit retention configuration
- **FINRA Rule 4511** — Books-and-records obligations for AI-assisted communications and agent-configured workflows
- **FINRA Rule 3110** — Supervisory mapping of agent activities; AgentId/AgentName fields are the primary evidence
- **SOX Section 404** — IT general controls audit trail; CopilotAgentManagement captures configuration change history
- **FFIEC** — Incident response requirements; JailbreakDetected events require documented escalation procedures

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automation of audit log configuration
- See [Verification & Testing](verification-testing.md) to validate audit logging is operational
- Back to [Control 3.1](../../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md)
