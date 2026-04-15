# Control 3.6: Supervision and Oversight (FINRA 3110 / SEC Reg BI) — PowerShell Setup

Automation scripts for managing supervisory review workflows, reporting, and compliance monitoring for Copilot-assisted activities, including agent-specific audit event retrieval for supervisory review of M365 Copilot agents.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Purview Compliance Admin
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "AuditLog.Read.All", "User.Read.All", "Group.Read.All"
```

## Scripts

### Script 1: Generate Supervisory Review Compliance Report

```powershell
# Report on supervisory review activity for FINRA 3110 documentation
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$reviewActions = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionReviewAction" `
    -ResultSize 5000

$summary = @{
    TotalReviewed     = ($reviewActions | Where-Object { $_.Operations -eq "SupervisionReviewAction" }).Count
    Approved          = ($reviewActions | Where-Object { $_.AuditData -like "*Approve*" }).Count
    Escalated         = ($reviewActions | Where-Object { $_.AuditData -like "*Escalate*" }).Count
    FalsePositives    = ($reviewActions | Where-Object { $_.AuditData -like "*FalsePositive*" }).Count
}

Write-Host "`nSupervisory Review Summary (Last 30 Days):" -ForegroundColor Cyan
$summary.GetEnumerator() | Format-Table Name, Value -AutoSize

# Export for FINRA examination evidence
$reviewActions | Export-Csv "SupervisoryReview_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Audit Supervisor-to-Representative Ratio

```powershell
# Check supervisor-to-rep ratios to identify overloaded supervisors
$supervisorGroupId = "supervisor-group-object-id"
$repGroupId = "registered-rep-group-object-id"

$supervisors = Get-MgGroupMember -GroupId $supervisorGroupId -All
$reps = Get-MgGroupMember -GroupId $repGroupId -All

$ratio = [math]::Round($reps.Count / $supervisors.Count, 1)

Write-Host "`nSupervisory Capacity Analysis:" -ForegroundColor Cyan
Write-Host "Supervisors: $($supervisors.Count)"
Write-Host "Registered Representatives: $($reps.Count)"
Write-Host "Ratio: 1:$ratio"

if ($ratio -gt 50) {
    Write-Warning "Supervisor ratio exceeds recommended 1:50 — consider adding supervisors"
}
```

### Script 3: Track Review SLA Compliance

```powershell
# Calculate SLA compliance for supervisory reviews
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$matches = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionPolicyMatch" `
    -ResultSize 5000

$reviews = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionReviewAction" `
    -ResultSize 5000

$totalMatches = $matches.Count
$reviewedWithin24h = 0
$reviewedWithin48h = 0

# Estimate SLA compliance based on match-to-review timing
Write-Host "SLA Compliance Metrics (Last 30 Days):"
Write-Host "Total policy matches: $totalMatches"
Write-Host "Total reviews completed: $($reviews.Count)"
Write-Host "Review completion rate: $([math]::Round(($reviews.Count / [Math]::Max($totalMatches,1)) * 100, 1))%"
```

### Script 4: Generate Reg BI Best Interest Documentation Report

```powershell
# Report on Copilot-assisted recommendation communications reviewed for Reg BI
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$regBIMatches = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionPolicyMatch" `
    -ResultSize 5000

$report = $regBIMatches | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Date          = $_.CreationDate
        Representative = $_.UserIds
        PolicyMatch   = $data.PolicyName
        Channel       = $data.CommunicationChannel
        ReviewStatus  = $data.ReviewStatus
    }
} | Where-Object { $_.PolicyMatch -like "*RegBI*" -or $_.PolicyMatch -like "*BestInterest*" }

$report | Export-Csv "RegBI_Review_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Reg BI review report exported: $($report.Count) items" -ForegroundColor Green
```

### Script 5: Search Agent-Specific Audit Events for Supervisory Review

```powershell
# Search CopilotInteraction audit events filtered by AgentId or AgentName
# for supervisory review of Teams channel agents and declarative agents
# Supports FINRA Rule 3110(a) agent supervision requirements

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

# Search all CopilotInteraction records (RecordType 261 = CopilotInteraction)
$copilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

# Filter for agent interactions — events where AgentId is present
$agentInteractions = $copilotEvents | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    if ($data.AgentId) {
        [PSCustomObject]@{
            Date       = $_.CreationDate
            User       = $_.UserIds
            AgentId    = $data.AgentId
            AgentName  = $data.AgentName
            XPIA       = $data.XPIA  # Cross-prompt injection attempt flag
            EventData  = $data.CopilotEventData | ConvertTo-Json -Depth 3
        }
    }
} | Where-Object { $_ -ne $null }

Write-Host "Agent interactions found: $($agentInteractions.Count)" -ForegroundColor Cyan
$agentInteractions | Format-Table Date, User, AgentName, XPIA -AutoSize

$agentInteractions | Export-Csv "AgentInteractions_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Agent audit events exported for supervisory review" -ForegroundColor Green
```

### Script 6: Search Agent Events by Specific Agent ID

```powershell
# Retrieve all audit events for a specific Copilot agent by AgentId
# Use when reviewing a particular Teams channel agent or declarative agent
# that has been flagged for supervisory follow-up

# Set these variables before running
$TargetAgentId = "your-agent-id-here"   # Replace with the agent's GUID
$DaysBack = 30

$startDate = (Get-Date).AddDays(-$DaysBack)
$endDate = Get-Date

$allCopilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$agentEvents = $allCopilotEvents | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    if ($data.AgentId -eq $TargetAgentId) {
        [PSCustomObject]@{
            Date      = $_.CreationDate
            User      = $_.UserIds
            AgentId   = $data.AgentId
            AgentName = $data.AgentName
            XPIA      = $data.XPIA
            RawData   = $_.AuditData
        }
    }
} | Where-Object { $_ -ne $null }

Write-Host "Events for agent '$TargetAgentId': $($agentEvents.Count)" -ForegroundColor Cyan
$agentEvents | Export-Csv "AgentEvents_${TargetAgentId}_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Agent-specific audit events exported" -ForegroundColor Green
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Supervisory review report | Weekly | Script 1 |
| Supervisor ratio audit | Monthly | Script 2 |
| SLA compliance tracking | Weekly | Script 3 |
| Reg BI documentation report | Monthly | Script 4 |
| Agent interaction audit | Weekly | Script 5 |
| Specific agent review | As needed | Script 6 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate supervisory controls
- See [Troubleshooting](troubleshooting.md) for supervision workflow issues
- Back to [Control 3.6](../../../controls/pillar-3-compliance/3.6-supervision-oversight.md)
