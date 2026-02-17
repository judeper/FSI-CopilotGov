# Control 3.1: Copilot Interaction Audit Logging — Portal Walkthrough

Step-by-step portal configuration for enabling comprehensive audit logging of all Microsoft 365 Copilot interactions to support compliance with FSI regulatory requirements.

## Prerequisites

- **Role:** Global Administrator or Compliance Administrator
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview compliance portal

## Steps

### Step 1: Verify Unified Audit Log Is Enabled

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Audit > Audit (Standard)

1. Navigate to the Audit solution in the Purview portal.
2. Confirm the banner reads "Audit is turned on" — if not, click **Start recording user and admin activity**.
3. Note that changes may take up to 60 minutes to propagate across the tenant.

### Step 2: Configure Copilot-Specific Audit Activities

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Audit > Audit Search > Activities filter

1. In the Activities filter, expand **Copilot activities** to view all Copilot-specific events.
2. Confirm that the following activities are available for search: `CopilotInteraction`, `CopilotFeedback`, `CopilotPluginRun`.
3. Create a saved search for "All Copilot Activity" selecting all Copilot-related event types.

### Step 3: Enable Audit (Premium) for Extended Retention

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Audit > Audit retention policies

1. Click **New audit retention policy**.
2. Set **Record type** to `CopilotInteraction`.
3. Set **Duration** to 10 years (FSI regulated recommendation).
4. Set **Priority** to a value higher than the default retention policy.
5. Click **Save** to apply.

### Step 4: Configure Audit Log Alert Policies

**Portal:** Microsoft Purview Compliance Portal
**Path:** Policies > Alert policies

1. Create a new alert policy for unusual Copilot interaction volume.
2. Set the activity to `CopilotInteraction` with threshold of more than 500 events per hour per user.
3. Assign alert recipients to the compliance monitoring team distribution group.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Audit log status | Enabled | Enabled | Enabled |
| Retention period | 90 days | 1 year | 10 years |
| Copilot activity alerts | Optional | Recommended | Required |
| Audit Premium | Optional | Recommended | Required |

## Regulatory Alignment

- **SEC Rule 17a-4** — Supports compliance with electronic record retention requirements
- **FINRA Rule 4511** — Helps meet books-and-records obligations for AI-assisted communications
- **FFIEC** — Supports IT audit trail requirements for AI-augmented processes

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automation of audit log configuration
- See [Verification & Testing](verification-testing.md) to validate audit logging is operational
