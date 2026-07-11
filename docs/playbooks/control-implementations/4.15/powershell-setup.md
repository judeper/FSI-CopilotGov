# Control 4.15: Copilot Cowork Governance - PowerShell Setup

Automation workflow for capturing evidence supporting Cowork governance at general availability: Cowork-related unified-audit-log events (including browser tasks), reconciliation of Cowork users against the approved pilot group, and packaging portal exports (access posture, model toggles, browser toggle, plugin/skill inventory, consumption limits). Cowork's configuration surfaces are managed in the admin center UI and the Cowork Customize page; this playbook focuses on evidence collection rather than configuration.

## Prerequisites

- PowerShell 7+
- `ExchangeOnlineManagement` for unified-audit-log queries
- `Microsoft.Graph` (`AuditLog.Read.All`, `Group.Read.All`) for group membership reconciliation
- M365 Global Reader (or equivalent least-privilege read role); AI Administrator or M365 Global Admin is required to view Cost management and Copilot settings in the portal
- Approved evidence-retention path
- Portal exports (or documented screenshots) capturing: usage-based billing scope and spending policy, discovery-setting state, Anthropic-family and Fable 5 (Preview) toggles, Cowork Browsing toggle, plugin availability, uploaded plugin packages, custom skills and their sharing scope, and per-user/per-group consumption limits
- An exported or documented record of the approved pilot group

> **Important:** There is no publicly documented Cowork-specific PowerShell cmdlet that returns the tenant's usage-based billing scope, discovery setting, model toggles, Cowork Browsing toggle, plugin inventory, custom skills, or consumption limits. Those governance decisions must be captured from the Microsoft 365 admin center and the Cowork Customize page as portal exports or screenshots. Do not rely on undocumented cmdlets. The scripts below capture only the evidence that has documented API/PowerShell paths: unified-audit-log activity (including Cowork browser tasks) and Microsoft Graph group membership.

## Script Flow

### Script 1: Capture Cowork-related unified-audit-log events

Cowork browser tasks and other Cowork activity are recorded in the unified audit log alongside other Copilot activity. Because Microsoft's audit-log-activities reference evolves, retrieve a wide window and filter on Cowork-related content rather than hard-coding a fixed operation list.

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

# Pull Copilot interaction events plus agent-management events, then filter for Cowork.
# Reference: https://learn.microsoft.com/purview/audit-log-activities
$operations = @(
  'CopilotInteraction',
  'DeployedAgent',
  'RemovedAgent',
  'UpdatedAgent'
)

Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -Operations $operations `
  -ResultSize 5000 |
  Where-Object { $_.AuditData -match 'Cowork' -or $_.AuditData -match 'cowork' } |
  Export-Csv .\artifacts\4.15\cowork-audit.csv -NoTypeInformation
```

If your tenant has communication compliance or Purview supervision policies configured for Copilot, prefer their exports for supervisory review; the raw audit-log pull above is best used for coverage-gap detection.

### Script 2: Reconcile Cowork users against the approved pilot group

Because usage-based billing scope is managed in the admin center (not through a documented cmdlet), this script reconciles the members of the **approved pilot group** you record in the availability decision, so you can compare it against the Cost management export you capture manually.

```powershell
Connect-MgGraph -Scopes 'Group.Read.All'

# Source the group ID from the documented access-posture decision.
$approvedGroupId = (Import-Csv .\config\cowork-access-decision.csv).ApprovedGroupId | Select-Object -First 1

Get-MgGroupMember -GroupId $approvedGroupId -All |
  Select-Object Id,
    @{n='Display';e={ $_.AdditionalProperties.displayName }},
    @{n='UserPrincipalName';e={ $_.AdditionalProperties.userPrincipalName }} |
  Export-Csv .\artifacts\4.15\cowork-approved-members.csv -NoTypeInformation
```

Reconcile `cowork-approved-members.csv` against the users listed in your Cost management export. Any user with usage-based billing enabled who is not in the approved group is an exception that needs a documented approval or a remediation.

### Script 3: Summarize Cowork audit activity

```powershell
$audit = Import-Csv .\artifacts\4.15\cowork-audit.csv

$audit |
  ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [pscustomobject]@{
      CreationDate = $_.CreationDate
      UserIds      = $_.UserIds
      Operation    = $_.Operations
      # AuditData shape varies by operation; capture what is present without inventing fields.
      AppName      = $data.AppName
      AgentName    = $data.AgentName
      AgentId      = $data.AgentId
      Context      = ($data | ConvertTo-Json -Depth 4 -Compress)
    }
  } |
  Export-Csv .\artifacts\4.15\cowork-audit-summary.csv -NoTypeInformation
```

### Script 4: Flag Cowork activity from users outside the approved scope

```powershell
$activity = Import-Csv .\artifacts\4.15\cowork-audit-summary.csv
# Search-UnifiedAuditLog emits UserIds as a UPN/email; compare against approved members' UPN.
$approved = (Import-Csv .\artifacts\4.15\cowork-approved-members.csv).UserPrincipalName

$activity |
  Where-Object { $approved -notcontains $_.UserIds } |
  Export-Csv .\artifacts\4.15\cowork-out-of-scope-activity.csv -NoTypeInformation
```

### Script 5: Package portal exports and audit evidence

```powershell
# Expected inputs under .\artifacts\4.15\portal\ (captured from the admin center + Cowork Customize):
#   - cost-management-billing-scope.<csv|pdf|png>
#   - discovery-setting-state.<pdf|png>
#   - copilot-settings-anthropic-family-toggle.<pdf|png>
#   - copilot-settings-fable5-preview-toggle.<pdf|png>
#   - cowork-browsing-toggle.<pdf|png>
#   - plugin-inventory.<csv|pdf|png>
#   - customize-skills-inventory.<csv|pdf|png>
#   - customize-uploaded-plugin-packages.<csv|pdf|png>
#   - consumption-limits.<csv|pdf|png>
#   - consumption-reporting-window.<csv|pdf|png>

$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
Compress-Archive -Path .\artifacts\4.15\* `
  -DestinationPath ".\artifacts\4.15\cowork-governance-evidence-$stamp.zip"
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Cowork audit pull | Weekly | Feeds coverage-gap detection and supervisory review inputs |
| Approved-group reconciliation | Monthly | Confirms the users with usage-based billing enabled remain within the approved pilot scope |
| Out-of-scope activity review | Monthly | Investigates Cowork activity from users outside the approved scope |
| Access-request review | Weekly (during pilot) | Reviews and documents pending user access requests |
| Model-toggle re-verification | Monthly and on Microsoft update | Re-confirms Anthropic-family and Fable 5 (Preview) toggle state and provider data-retention posture |
| Browser-toggle re-verification | Monthly and on Microsoft update | Re-confirms the Cowork Browsing toggle and the Edge policies it inherits |
| Plugin, uploaded package, and custom skill inventory review | Monthly | Confirms available plugins, uploaded packages, and custom skills (with sharing scope) match the approved inventory |
| Consumption reporting review | Weekly (during pilot), Monthly (steady state) | Confirms spending remains within budget and thresholds |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for access-posture, model, browser, plugin/skill, consumption, and Purview/audit validation.
- Reference [Troubleshooting](troubleshooting.md) for access, billing, discovery, model-toggle, browser-use, and plugin issues.

*FSI Copilot Governance Framework v1.8.0 - July 2026*
- Back to [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)
