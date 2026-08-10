from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLAYBOOK = (
    REPO_ROOT
    / "docs"
    / "playbooks"
    / "control-implementations"
    / "2.13"
    / "powershell-setup.md"
)


def test_audit_page_call_forces_terminating_errors() -> None:
    script = PLAYBOOK.read_text(encoding="utf-8")
    assert "-ErrorAction Stop" in script


def test_audit_paging_fails_closed_after_nonterminating_cmdlet_error() -> None:
    playbook_path = str(PLAYBOOK).replace("'", "''")
    command = rf"""
$content = Get-Content -Raw '{playbook_path}'
$match = [regex]::Match(
    $content,
    '(?s)### Script 4:.*?```powershell\r?\n(.*?)\r?\n```'
)
if (-not $match.Success) {{
    throw 'Script 4 block not found.'
}}

$tokens = $null
$parseErrors = $null
$ast = [System.Management.Automation.Language.Parser]::ParseInput(
    $match.Groups[1].Value,
    [ref]$tokens,
    [ref]$parseErrors
)
if ($parseErrors.Count -gt 0) {{
    throw ($parseErrors.Message -join '; ')
}}

$functionAst = $ast.Find(
    {{
        param($node)
        $node -is [System.Management.Automation.Language.FunctionDefinitionAst] -and
            $node.Name -eq 'Get-PagedCopilotAuditRecord'
    }},
    $true
)
if ($null -eq $functionAst) {{
    throw 'Get-PagedCopilotAuditRecord was not found.'
}}
Invoke-Expression $functionAst.Extent.Text

$script:pageCall = 0
function Search-UnifiedAuditLog {{
    [CmdletBinding()]
    param(
        $StartDate,
        $EndDate,
        $RecordType,
        $Operations,
        $SessionId,
        $SessionCommand,
        $ResultSize
    )

    $script:pageCall++
    if ($script:pageCall -eq 1) {{
        return @(
            [pscustomobject]@{{
                AuditData = '{{"Id":"first-page-record"}}'
                ResultIndex = 1
                ResultCount = 2
                AuditSearchRequestMetadata = [pscustomobject]@{{
                    moreRecordsAvailable = $true
                }}
            }}
        )
    }}

    Write-Error 'simulated non-terminating audit service failure'
    return @()
}}

$threw = $false
$records = $null
try {{
    $records = @(
        Get-PagedCopilotAuditRecord `
            -StartDate ([datetime]'2026-08-01T00:00:00Z') `
            -EndDate ([datetime]'2026-08-01T01:00:00Z')
    )
}}
catch {{
    $threw = $true
    if ($_.Exception.Message -notmatch 'page 2') {{
        throw "Missing page context: $($_.Exception.Message)"
    }}
    if ($_.Exception.Message -notmatch 'simulated non-terminating audit service failure') {{
        throw "Missing underlying error context: $($_.Exception.Message)"
    }}
    if ($_.Exception.Message -notmatch 'No evidence from this run should be treated as complete') {{
        throw "Missing fail-closed guidance: $($_.Exception.Message)"
    }}
}}

if (-not $threw) {{
    throw 'The non-terminating Search-UnifiedAuditLog error was mistaken for exhaustion.'
}}
if ($null -ne $records) {{
    throw 'The failed retrieval returned partial records as successful evidence.'
}}
"""

    result = subprocess.run(
        ["pwsh", "-NoProfile", "-NonInteractive", "-Command", command],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    assert result.returncode == 0, result.stderr or result.stdout
