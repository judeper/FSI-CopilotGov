# Control 3.1: Copilot Interaction Audit Logging — Portal Walkthrough

Step-by-step portal configuration for enabling comprehensive audit logging of all Microsoft 365 Copilot interactions to support compliance with FSI regulatory requirements.

## Prerequisites

- **Role:** Entra Global Admin or Purview Compliance Admin
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

1. In the **Activities - friendly names** filter, expand **Copilot activities** to view all Copilot-specific events.
2. Confirm that the following activities are available for search: `CopilotInteraction`, `CopilotFeedback`, `CopilotPluginRun`.
3. Create a saved search for "All Copilot Activity" selecting all Copilot-related event types.
4. To search for agent-specific events, use the **Record type** filter and select `AgentAdminActivity` or `AgentSettingsAdminActivity`.

### Step 3: Search for New Audit Schema Fields

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Audit > Search > Export results

To surface the expanded audit schema fields (AgentId, AgentName, XPIA, JailbreakDetected, SensitivityLabelId):

1. Run a `CopilotInteraction` search for your desired date range and export results to CSV.
2. Open the exported CSV and review the **AuditData** column (JSON format) for the new fields.
3. When reviewing agent-assisted interactions, the `AgentId` and `AgentName` fields identify which Copilot agent was invoked — use these to map agent usage to FINRA Rule 3110 supervisory records.
4. Filter the exported data for rows where `JailbreakDetected` is `true` — these events require security escalation per FFIEC incident response standards.
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
   - **Record types:** Select `AgentAdminActivity` and `AgentSettingsAdminActivity`
   - **Duration:** 6 years (Sarbanes-Oxley §404 IT general controls require multi-year change management records)
   - **Priority:** Same as the Copilot interaction policy

### Step 5: Configure Agent-Specific Record Type Navigation

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Audit > Search

To search for agent administrative events in the portal:

1. In the Audit search interface, set the date range.
2. In the **Record type** filter (advanced search options), select `AgentAdminActivity` to find agent configuration changes.
3. Select `AgentSettingsAdminActivity` to find agent settings modifications.
4. Combine with the **User** filter to scope searches to specific administrators who manage Copilot agents.
5. Export results and use the `AgentId` field to trace which agents were created, modified, or deleted.

### Step 6: Configure Audit Log Alert Policies

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Policies > Alert policies

1. Create a new alert policy for unusual Copilot interaction volume.
2. Set the activity to `CopilotInteraction` with threshold of more than 500 events per hour per user.
3. Create a second alert for `JailbreakDetected` events — set threshold to 1 (any jailbreak attempt triggers an alert).
4. Assign alert recipients to the compliance monitoring team distribution group.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Audit log status | Enabled | Enabled | Enabled |
| CopilotInteraction retention | 180 days | 1 year | 6-10 years |
| AgentAdminActivity retention | Not required | 1 year | 6 years |
| Copilot activity alerts | Optional | Recommended | Required |
| JailbreakDetected alert | Optional | Recommended | Required |
| Audit Premium or PAYG | Optional | Recommended | Required |
| Agent record type searches | Optional | Recommended | Required |

## Regulatory Alignment

- **SEC Rule 17a-4(a)** — Six-year retention requirement drives the regulated-tier audit retention configuration
- **FINRA Rule 4511** — Books-and-records obligations for AI-assisted communications and agent-configured workflows
- **FINRA Rule 3110** — Supervisory mapping of agent activities; AgentId/AgentName fields are the primary evidence
- **SOX Section 404** — IT general controls audit trail; AgentAdminActivity captures configuration change history
- **FFIEC** — Incident response requirements; JailbreakDetected events require documented escalation procedures

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automation of audit log configuration
- See [Verification & Testing](verification-testing.md) to validate audit logging is operational
- Back to [Control 3.1](../../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md)
