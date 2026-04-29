"""Authored manifest content for Phase A3 — quick-start control bars.

This module contains hand-authored values for the SPA-extension fields
that require human judgment (yesBar/partialBar/noBar, priority,
sectorYesBar, facilitatorNotes, verifyIn, verifyPowerShell,
evidenceExpected, collectorField).

Used by ``scripts/merge_authored_content.py`` to overlay these values
on top of the harvested manifest, replacing TODO placeholders.

Phase A3 covers the 5 quick-start controls:

* 1.2  — SharePoint Oversharing Detection (DSPM for AI)
* 1.3  — Restricted SharePoint Search (RSS / RCD)
* 2.1  — DLP Policies for Copilot
* 3.1  — Copilot Audit Logging (Purview UAL)
* 4.1  — Copilot Admin Settings & Feature Management

Subsequent phases will extend AUTHORED with the remaining controls in the
manifest (the count is derived from the loaded manifest length, not hard-coded).

The merge is **idempotent**: only fields present in this dict overwrite
manifest values, and only when the manifest value is missing or starts
with ``TODO:``. Previously-authored manifest values are preserved.
"""
from __future__ import annotations

# Canonical FSI sectors (must match validate_manifest.py SECTORS)
_SECTORS = (
    "bank",
    "broker-dealer",
    "investment-adviser",
    "insurance-carrier",
    "insurance-wholesale",
    "credit-union",
    "holding-company",
    "other",
)


def _sector_map(**overrides: str) -> dict[str, str]:
    """Build a sectorYesBar with overrides; remaining sectors get TODO."""
    out = {s: "TODO: sector-specific yes-bar" for s in _SECTORS}
    for k, v in overrides.items():
        # Allow underscore in keys for Python kwargs (broker_dealer -> broker-dealer)
        canonical = k.replace("_", "-")
        if canonical in out:
            out[canonical] = v
    return out


AUTHORED: dict[str, dict] = {
    # ---------------------------------------------------------------
    # 1.2 — SharePoint Oversharing Detection
    # ---------------------------------------------------------------
    "1.2": {
        "priority": "critical",
        "yesBar": (
            "DSPM for AI is enabled, an oversharing assessment / data risk "
            "assessment runs on a documented cadence (weekly or better), "
            "findings are triaged into a tracked remediation backlog with "
            "named owners, and item-level remediation has been used at "
            "least once in the last 30 days for a Copilot-grounded site."
        ),
        "partialBar": (
            "DSPM is enabled and an assessment has been run, but findings "
            "are not yet triaged into a tracked backlog or remediation "
            "ownership is not formally assigned."
        ),
        "noBar": (
            "DSPM for AI is not enabled, no oversharing assessment has been "
            "run, or 'Everyone' / 'Everyone Except External Users' (EEEU) "
            "sharing exists on Copilot-grounded sites without compensating "
            "controls."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview",
                "path": "Data Security Posture Management > Overview",
                "url": "https://purview.microsoft.com/datasecurityposturemanagement",
            },
            {
                "portal": "Microsoft Purview",
                "path": "DSPM for AI > Reports > Oversharing assessments",
                "url": "https://purview.microsoft.com/aihub",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-DlpCompliancePolicy | Where-Object { $_.Name -like '*Copilot*' -or $_.Name -like '*Oversharing*' }"
        ),
        "evidenceExpected": [
            "DSPM for AI oversharing assessment report (PDF/JSON export)",
            "Remediation backlog ticket count + closure cadence",
            "Item-level remediation log entries for the last 30 days",
            "List of sites with EEEU/Everyone sharing flagged + dispositioned",
        ],
        "collectorField": "DSPM_OversharingAssessment",
        "sectorYesBar": _sector_map(
            bank=(
                "DSPM oversharing assessment runs weekly; any site with NPI "
                "(account numbers, SSNs, customer financial info) and broad "
                "sharing is auto-restricted within 5 business days per "
                "GLBA §501(b) safeguards expectations."
            ),
            broker_dealer=(
                "Weekly DSPM oversharing scan; sites containing trade blotters, "
                "research reports, or MNPI carry information-barrier evidence; "
                "remediation closure documented for SEC Reg S-P examiners."
            ),
            investment_adviser=(
                "Weekly DSPM oversharing scan; client portfolio documents and "
                "private fund records reviewed for least-privilege; remediation "
                "evidence retained for SEC OCIE / IA exam response."
            ),
            insurance_carrier=(
                "Weekly DSPM scan; PHI/PII-bearing sites (claims, underwriting) "
                "auto-restricted; HIPAA + state insurance regulator readiness."
            ),
            credit_union=(
                "Weekly DSPM scan with NCUA Part 748 alignment; member NPI "
                "sites carry documented sharing reviews."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has DSPM for AI been enabled, has an oversharing or data "
                "risk assessment been run within the last 30 days, and is "
                "remediation tracked with named owners?"
            ),
            "followUp": (
                "Open Microsoft Purview > Data Security Posture Management > "
                "Reports. Show the most recent oversharing/data-risk-assessment "
                "report, pull the top 5 flagged sites, and confirm each has "
                "an owner and target date in the remediation backlog."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 1.3 — Restricted SharePoint Search
    # ---------------------------------------------------------------
    "1.3": {
        "priority": "high",
        "yesBar": (
            "RSS is enabled tenant-wide with a documented allow-list of "
            "approved sites (≤100), RCD is used to surgically exclude "
            "high-risk sites that cannot be migrated, and there is a "
            "documented exit plan to transition off RSS as Purview / SAM "
            "long-term controls reach operational maturity."
        ),
        "partialBar": (
            "RSS is enabled but the allow-list lacks documented review "
            "cadence, or RCD is used without a written exception register, "
            "or no exit plan to long-term governance exists."
        ),
        "noBar": (
            "RSS is not enabled and no compensating control (RCD allow-list, "
            "Restricted Content Discovery, or item-level scoping) is in "
            "place to limit Copilot's tenant-wide search scope."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint Admin Center",
                "path": "Settings > Search > Restricted SharePoint Search",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOTenant | Select-Object IsRestrictedSPSearchEnabled, RestrictedSearchAllowedList"
        ),
        "evidenceExpected": [
            "Tenant setting screenshot showing IsRestrictedSPSearchEnabled = $true",
            "Current allow-list site URLs (≤100) with business owner per site",
            "RCD exception register (sites surgically excluded outside the allow-list model)",
            "Documented exit plan / transition target date to long-term Purview+SAM governance",
        ],
        "collectorField": "SPO_RestrictedSearchConfig",
        "sectorYesBar": _sector_map(
            bank=(
                "RSS enabled with allow-list reviewed quarterly; loan-ops, "
                "trust, and treasury sites included; deposit/credit account "
                "sites carrying NPI excluded until DSPM remediation closes."
            ),
            broker_dealer=(
                "RSS enabled; research and investment-banking sites carry RCD "
                "exclusion to honor information barriers; allow-list reviewed "
                "by supervisory principal monthly."
            ),
            investment_adviser=(
                "RSS enabled with allow-list limited to approved client-service "
                "and ops sites; private fund / portfolio company sites excluded."
            ),
            insurance_carrier=(
                "RSS enabled; claims and underwriting sites with PHI excluded "
                "from allow-list; HIPAA business-associate documentation references RSS scope."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Restricted SharePoint Search enabled, with a curated "
                "allow-list of ≤100 sites and a documented review cadence?"
            ),
            "followUp": (
                "Open SharePoint Admin Center > Settings > Search and verify "
                "Restricted SharePoint Search is on. Pull the current allow-list, "
                "confirm count is within the 100-site limit, and ask the SharePoint "
                "Admin who owns the quarterly review and where the allow-list is documented."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.1 — DLP Policies for Copilot
    # ---------------------------------------------------------------
    "2.1": {
        "priority": "critical",
        "yesBar": (
            "Both DLP policy types target the Microsoft 365 Copilot location: "
            "(a) label-based response blocking (preventing Copilot from "
            "surfacing labeled NPI/MNPI in responses) and (b) SIT-based "
            "prompt blocking (preventing users from pasting account numbers, "
            "SSNs, or other regulated SITs into prompts). Policies are in "
            "Enforce mode with documented owner, override workflow, and "
            "match-event review cadence."
        ),
        "partialBar": (
            "At least one DLP rule targets the Copilot location, but the "
            "other policy type is missing, the policy is in test/audit mode "
            "only, or match events are not reviewed on a documented cadence."
        ),
        "noBar": (
            "No DLP policy targets the Microsoft 365 Copilot location, or "
            "policies exist but are scoped to a single user / pilot group "
            "and not enforced for the Copilot-licensed user population."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview",
                "path": "Data Loss Prevention > Policies",
                "url": "https://purview.microsoft.com/datalossprevention/policies",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-DlpCompliancePolicy | Where-Object { $_.Workload -like '*Copilot*' } | "
            "Select-Object Name, Mode, Enabled, Workload"
        ),
        "evidenceExpected": [
            "DLP policy export showing 'Microsoft 365 Copilot' location in scope",
            "Both policy types present: label-based response blocking AND SIT-based prompt blocking",
            "Policy mode = Enforce (not Test / TestWithNotifications)",
            "Match-event report from Purview > Activity Explorer for the last 30 days",
            "Override workflow document showing who can request and approve overrides",
        ],
        "collectorField": "DLP_CopilotPolicies",
        "sectorYesBar": _sector_map(
            bank=(
                "Both DLP rule types enforced; SIT set covers ABA routing, "
                "account numbers, SSN, ITIN, GLBA NPI; Label-based blocking "
                "for 'Confidential — NPI' and 'Highly Confidential — MNPI' labels."
            ),
            broker_dealer=(
                "Both rule types enforced; SIT set covers CRD numbers, "
                "account numbers, SSN; label-based blocking for Research "
                "and IB Confidential labels supporting information-barrier policy."
            ),
            investment_adviser=(
                "Both rule types enforced; SIT set covers SSN, account numbers, "
                "and adviser-firm-defined SITs for client portfolio identifiers."
            ),
            insurance_carrier=(
                "Both rule types enforced; SIT set covers SSN, policy numbers, "
                "PHI patterns; label-based blocking for PHI sensitivity labels."
            ),
            credit_union=(
                "Both rule types enforced; SITs cover member account numbers "
                "+ SSN; label-based blocking aligned to NCUA NPI categories."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are both DLP policy types deployed and enforced for the "
                "Microsoft 365 Copilot location — label-based response "
                "blocking AND SIT-based prompt blocking?"
            ),
            "followUp": (
                "Open Microsoft Purview > Data Loss Prevention > Policies. "
                "Filter by location 'Microsoft 365 Copilot'. Confirm at least "
                "two distinct rules exist (one label-based, one SIT-based), "
                "both in Enforce mode. Then open Activity Explorer to show "
                "match events from the last 30 days are being reviewed."
            ),
            "timeBudgetMinutes": 10,
        },
    },
    # ---------------------------------------------------------------
    # 3.1 — Copilot Audit Logging
    # ---------------------------------------------------------------
    "3.1": {
        "priority": "critical",
        "yesBar": (
            "Unified Audit Log is enabled at the tenant level, "
            "CopilotInteraction events are queryable via Purview Audit / "
            "Search-UnifiedAuditLog, retention is set to meet the firm's "
            "regulatory minimum (typically 7 years for FINRA/SEC firms via "
            "E5 Audit Premium or PAYG), and audit data flows to an external "
            "WORM/SIEM archive on a documented cadence."
        ),
        "partialBar": (
            "UAL is enabled and CopilotInteraction events are present, but "
            "retention is at the E3 default (180 days) without a 7-year plan, "
            "or there is no SIEM/WORM archival path documented."
        ),
        "noBar": (
            "Unified Audit Log is disabled, CopilotInteraction events are "
            "not present in audit search, or audit retention is below the "
            "firm's regulatory minimum without a remediation plan."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview",
                "path": "Audit > Search",
                "url": "https://purview.microsoft.com/audit/auditsearch",
            },
            {
                "portal": "Microsoft Purview",
                "path": "Audit > Audit retention policies",
                "url": "https://purview.microsoft.com/audit/auditretentionpolicies",
            },
        ],
        "verifyPowerShell": (
            "Connect-ExchangeOnline; "
            "Get-AdminAuditLogConfig | Select-Object UnifiedAuditLogIngestionEnabled; "
            "Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) "
            "-RecordType CopilotInteraction -ResultSize 5"
        ),
        "evidenceExpected": [
            "Get-AdminAuditLogConfig output showing UnifiedAuditLogIngestionEnabled = True",
            "Sample Search-UnifiedAuditLog results for RecordType=CopilotInteraction (last 24h)",
            "Audit retention policy export showing target retention duration per RecordType",
            "SIEM ingestion connector configuration (e.g., Sentinel M365 Defender connector)",
            "WORM/external archive runbook with destination and cadence",
        ],
        "collectorField": "Audit_UALCopilotInteraction",
        "sectorYesBar": _sector_map(
            bank=(
                "UAL on; CopilotInteraction + AgentAdminActivity + "
                "AgentSettingsAdminActivity events retained 7 years; SIEM "
                "ingestion to bank-managed log lake; aligned to OCC Heightened "
                "Standards (12 CFR part 30, appendix D) for monitoring."
            ),
            broker_dealer=(
                "UAL on; CopilotInteraction events retained 7 years per SEC "
                "Rule 17a-4 where applicable; WORM archive evidence provided "
                "to FINRA on exam request; supervisory review of agent events."
            ),
            investment_adviser=(
                "UAL on; CopilotInteraction events retained ≥5 years per "
                "Investment Advisers Act Rule 204-2; SIEM/archive evidence "
                "available for SEC OCIE exams."
            ),
            insurance_carrier=(
                "UAL on; CopilotInteraction events retained per state "
                "insurance regulator record-keeping minimums; SIEM ingestion "
                "for HIPAA security-incident detection."
            ),
            credit_union=(
                "UAL on; CopilotInteraction events retained per NCUA Part 749 "
                "record retention; SIEM ingestion for member-data monitoring."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is the Unified Audit Log enabled, are CopilotInteraction "
                "events queryable, and is retention set to your firm's "
                "regulatory minimum (often 7 years for FINRA/SEC firms)?"
            ),
            "followUp": (
                "Run Get-AdminAuditLogConfig to verify ingestion is on, then "
                "Search-UnifiedAuditLog -RecordType CopilotInteraction for the "
                "last 24 hours. Open Purview > Audit > Audit retention policies "
                "and confirm the policy duration matches the firm's regulatory "
                "minimum. Confirm the SIEM/WORM archive destination and cadence."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 4.1 — Copilot Admin Settings & Feature Management
    # ---------------------------------------------------------------
    "4.1": {
        "priority": "critical",
        "yesBar": (
            "Copilot administration is exercised through the AI Administrator "
            "role (least privilege), Cloud Policy controls Pages / Notebooks "
            "/ code preview, billing & PAYG decisions are governed under the "
            "same change-management process as feature toggles, and an "
            "evidence pack of current settings is captured at each "
            "documented review cadence."
        ),
        "partialBar": (
            "Copilot settings are governed but split across roles inconsistently "
            "(M365 Global Admin used routinely instead of AI Administrator), "
            "or Cloud Policy / billing decisions are not part of the same "
            "change-management workflow."
        ),
        "noBar": (
            "Copilot settings are managed ad hoc by individual admins without "
            "documented change management, or settings drift between admin "
            "surfaces (Copilot Settings, Agents, Cloud Policy, Billing) is "
            "not tracked."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 Admin Center",
                "path": "Copilot > Settings",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
            {
                "portal": "Microsoft 365 Admin Center",
                "path": "Agents > All agents",
                "url": "https://admin.microsoft.com/Adminportal/Home#/agents",
            },
            {
                "portal": "Microsoft 365 Apps Admin Center",
                "path": "Customization > Policy Management",
                "url": "https://config.office.com",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes RoleManagement.Read.Directory; "
            "Get-MgRoleManagementDirectoryRoleDefinition -Filter \"displayName eq 'AI Administrator'\"; "
            "Get-MgRoleManagementDirectoryRoleAssignment -Filter \"roleDefinitionId eq '<AI Admin role id>'\""
        ),
        "evidenceExpected": [
            "List of users assigned 'AI Administrator' role with last sign-in",
            "Cloud Policy export covering Copilot Pages / Notebooks / code preview decisions",
            "Pay-as-you-go (PAYG) services configuration screenshot + budget alert thresholds",
            "Change-management record (ticket / PR) for the most recent Copilot setting toggle",
            "Documented review cadence (monthly / quarterly) with evidence-pack template",
        ],
        "collectorField": "M365Admin_CopilotSettings",
        "sectorYesBar": _sector_map(
            bank=(
                "AI Administrator role used; Cloud Policy locked-down for "
                "Pages/Notebooks/code; PAYG budgets aligned to bank cost "
                "centers; settings reviewed monthly under SOX IT general controls."
            ),
            broker_dealer=(
                "AI Administrator role used; Copilot Settings + Agents "
                "reviewed monthly by supervisory principal; Cloud Policy "
                "enforces approved Pages/Notebooks behavior for FINRA WSP alignment."
            ),
            investment_adviser=(
                "AI Administrator role used; Cloud Policy controls extension "
                "surfaces; settings reviewed quarterly with compliance officer."
            ),
            insurance_carrier=(
                "AI Administrator role used; Cloud Policy enforces "
                "Pages/Notebooks scope for PHI handling units; settings reviewed monthly."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Copilot administration exercised through the AI "
                "Administrator role (not M365 Global Admin), and are Cloud "
                "Policy + billing decisions part of the same documented "
                "change-management process?"
            ),
            "followUp": (
                "Open Microsoft 365 Admin Center > Roles and confirm who "
                "holds AI Administrator. Open Copilot > Settings, Agents > "
                "All agents, and config.office.com Customization > Policy "
                "Management. Ask for the most recent change-management ticket "
                "for a Copilot setting toggle and the documented review cadence."
            ),
            "timeBudgetMinutes": 10,
        },
    },
}

# ---------------------------------------------------------------
# Phase C2 — per-control mappings to FSI-CopilotGov-Solutions
# ---------------------------------------------------------------
# Source of truth: FSI-CopilotGov-Solutions/data/control-coverage.json
# at the pinned tag (see assessment/data/solutions-lock.json). Order
# preserved from coverage; first entry = primary, rest = supporting.
# Tier is mirrored from solutions.json (1=Baseline, 2=Recommended,
# 3=Regulated) as a numeric value.
#
# Controls with an intentional empty coverage set (e.g. controls
# tracked purely by policy, with no companion automation solution)
# declare `solutions: []` explicitly rather than omitting the key.

_SOLUTIONS_BY_CONTROL: dict[str, list[dict]] = {
    '1.1': [
        {"id": '01-copilot-readiness-scanner', "tier": 1, "role": 'primary'},
    ],
    '1.2': [
        {"id": '02-oversharing-risk-assessment', "tier": 1, "role": 'primary'},
        {"id": '16-item-level-oversharing-scanner', "tier": 2, "role": 'supporting'},
        {"id": '17-sharepoint-permissions-drift', "tier": 2, "role": 'supporting'},
        {"id": '18-entra-access-reviews', "tier": 2, "role": 'supporting'},
    ],
    '1.3': [
        {"id": '02-oversharing-risk-assessment', "tier": 1, "role": 'primary'},
        {"id": '16-item-level-oversharing-scanner', "tier": 2, "role": 'supporting'},
    ],
    '1.4': [
        {"id": '02-oversharing-risk-assessment', "tier": 1, "role": 'primary'},
        {"id": '16-item-level-oversharing-scanner', "tier": 2, "role": 'supporting'},
        {"id": '17-sharepoint-permissions-drift', "tier": 2, "role": 'supporting'},
    ],
    '1.5': [
        {"id": '01-copilot-readiness-scanner', "tier": 1, "role": 'primary'},
        {"id": '03-sensitivity-label-auditor', "tier": 2, "role": 'supporting'},
    ],
    '1.6': [
        {"id": '01-copilot-readiness-scanner', "tier": 1, "role": 'primary'},
        {"id": '02-oversharing-risk-assessment', "tier": 1, "role": 'supporting'},
        {"id": '16-item-level-oversharing-scanner', "tier": 2, "role": 'supporting'},
        {"id": '17-sharepoint-permissions-drift', "tier": 2, "role": 'supporting'},
        {"id": '18-entra-access-reviews', "tier": 2, "role": 'supporting'},
    ],
    '1.7': [
        {"id": '01-copilot-readiness-scanner', "tier": 1, "role": 'primary'},
    ],
    '1.8': [],
    '1.9': [
        {"id": '01-copilot-readiness-scanner', "tier": 1, "role": 'primary'},
        {"id": '08-license-governance-roi', "tier": 2, "role": 'supporting'},
        {"id": '11-risk-tiered-rollout', "tier": 1, "role": 'supporting'},
    ],
    '1.10': [],
    '1.11': [
        {"id": '11-risk-tiered-rollout', "tier": 1, "role": 'primary'},
    ],
    '1.12': [
        {"id": '11-risk-tiered-rollout', "tier": 1, "role": 'primary'},
    ],
    '1.13': [
        {"id": '10-connector-plugin-governance', "tier": 3, "role": 'primary'},
    ],
    '1.14': [
        {"id": '16-item-level-oversharing-scanner', "tier": 2, "role": 'primary'},
        {"id": '17-sharepoint-permissions-drift', "tier": 2, "role": 'supporting'},
    ],
    '1.15': [
        {"id": '16-item-level-oversharing-scanner', "tier": 2, "role": 'primary'},
        {"id": '17-sharepoint-permissions-drift', "tier": 2, "role": 'supporting'},
    ],
    '1.16': [
        {"id": '19-copilot-tuning-governance', "tier": 2, "role": 'primary'},
    ],
    '2.1': [
        {"id": '05-dlp-policy-governance', "tier": 2, "role": 'primary'},
    ],
    '2.2': [
        {"id": '03-sensitivity-label-auditor', "tier": 2, "role": 'primary'},
    ],
    '2.3': [
        {"id": '07-conditional-access-automation', "tier": 2, "role": 'primary'},
    ],
    '2.4': [],
    '2.5': [
        {"id": '02-oversharing-risk-assessment', "tier": 1, "role": 'primary'},
        {"id": '16-item-level-oversharing-scanner', "tier": 2, "role": 'supporting'},
        {"id": '17-sharepoint-permissions-drift', "tier": 2, "role": 'supporting'},
        {"id": '18-entra-access-reviews', "tier": 2, "role": 'supporting'},
    ],
    '2.6': [
        {"id": '07-conditional-access-automation', "tier": 2, "role": 'primary'},
        {"id": '09-feature-management-controller', "tier": 2, "role": 'supporting'},
    ],
    '2.7': [
        {"id": '12-regulatory-compliance-dashboard', "tier": 1, "role": 'primary'},
        {"id": '13-dora-resilience-monitor', "tier": 3, "role": 'supporting'},
    ],
    '2.8': [],
    '2.9': [
        {"id": '07-conditional-access-automation', "tier": 2, "role": 'primary'},
    ],
    '2.10': [
        {"id": '12-regulatory-compliance-dashboard', "tier": 1, "role": 'primary'},
        {"id": '14-communication-compliance-config', "tier": 3, "role": 'supporting'},
    ],
    '2.11': [
        {"id": '15-pages-notebooks-gap-monitor', "tier": 3, "role": 'primary'},
    ],
    '2.12': [
        {"id": '02-oversharing-risk-assessment', "tier": 1, "role": 'primary'},
        {"id": '18-entra-access-reviews', "tier": 2, "role": 'supporting'},
    ],
    '2.13': [
        {"id": '10-connector-plugin-governance', "tier": 3, "role": 'primary'},
    ],
    '2.14': [
        {"id": '10-connector-plugin-governance', "tier": 3, "role": 'primary'},
    ],
    '2.15': [],
    '2.16': [
        {"id": '10-connector-plugin-governance', "tier": 3, "role": 'primary'},
    ],
    '3.1': [
        {"id": '06-audit-trail-manager', "tier": 1, "role": 'primary'},
    ],
    '3.2': [
        {"id": '06-audit-trail-manager', "tier": 1, "role": 'primary'},
        {"id": '15-pages-notebooks-gap-monitor', "tier": 3, "role": 'supporting'},
    ],
    '3.3': [
        {"id": '06-audit-trail-manager', "tier": 1, "role": 'primary'},
        {"id": '15-pages-notebooks-gap-monitor', "tier": 3, "role": 'supporting'},
    ],
    '3.4': [
        {"id": '04-finra-supervision-workflow', "tier": 1, "role": 'primary'},
        {"id": '14-communication-compliance-config', "tier": 3, "role": 'supporting'},
    ],
    '3.5': [
        {"id": '04-finra-supervision-workflow', "tier": 1, "role": 'primary'},
        {"id": '14-communication-compliance-config', "tier": 3, "role": 'supporting'},
    ],
    '3.6': [
        {"id": '04-finra-supervision-workflow', "tier": 1, "role": 'primary'},
        {"id": '14-communication-compliance-config', "tier": 3, "role": 'supporting'},
    ],
    '3.7': [
        {"id": '12-regulatory-compliance-dashboard', "tier": 1, "role": 'primary'},
    ],
    '3.8': [
        {"id": '12-regulatory-compliance-dashboard', "tier": 1, "role": 'primary'},
        {"id": '19-copilot-tuning-governance', "tier": 2, "role": 'supporting'},
    ],
    '3.9': [
        {"id": '14-communication-compliance-config', "tier": 3, "role": 'primary'},
    ],
    '3.10': [
        {"id": '02-oversharing-risk-assessment', "tier": 1, "role": 'primary'},
        {"id": '05-dlp-policy-governance', "tier": 2, "role": 'supporting'},
    ],
    '3.11': [
        {"id": '03-sensitivity-label-auditor', "tier": 2, "role": 'primary'},
        {"id": '06-audit-trail-manager', "tier": 1, "role": 'supporting'},
        {"id": '15-pages-notebooks-gap-monitor', "tier": 3, "role": 'supporting'},
    ],
    '3.12': [
        {"id": '03-sensitivity-label-auditor', "tier": 2, "role": 'primary'},
        {"id": '05-dlp-policy-governance', "tier": 2, "role": 'supporting'},
        {"id": '06-audit-trail-manager', "tier": 1, "role": 'supporting'},
        {"id": '12-regulatory-compliance-dashboard', "tier": 1, "role": 'supporting'},
    ],
    '3.13': [
        {"id": '12-regulatory-compliance-dashboard', "tier": 1, "role": 'primary'},
    ],
    '4.1': [
        {"id": '09-feature-management-controller', "tier": 2, "role": 'primary'},
    ],
    '4.2': [
        {"id": '09-feature-management-controller', "tier": 2, "role": 'primary'},
    ],
    '4.3': [
        {"id": '09-feature-management-controller', "tier": 2, "role": 'primary'},
    ],
    '4.4': [
        {"id": '09-feature-management-controller', "tier": 2, "role": 'primary'},
    ],
    '4.5': [
        {"id": '08-license-governance-roi', "tier": 2, "role": 'primary'},
        {"id": '12-regulatory-compliance-dashboard', "tier": 1, "role": 'supporting'},
    ],
    '4.6': [
        {"id": '08-license-governance-roi', "tier": 2, "role": 'primary'},
    ],
    '4.7': [
        {"id": '12-regulatory-compliance-dashboard', "tier": 1, "role": 'primary'},
    ],
    '4.8': [
        {"id": '08-license-governance-roi', "tier": 2, "role": 'primary'},
    ],
    '4.9': [
        {"id": '13-dora-resilience-monitor', "tier": 3, "role": 'primary'},
    ],
    '4.10': [
        {"id": '13-dora-resilience-monitor', "tier": 3, "role": 'primary'},
    ],
    '4.11': [
        {"id": '13-dora-resilience-monitor', "tier": 3, "role": 'primary'},
    ],
    '4.12': [
        {"id": '09-feature-management-controller', "tier": 2, "role": 'primary'},
        {"id": '11-risk-tiered-rollout', "tier": 1, "role": 'supporting'},
    ],
    '4.13': [
        {"id": '09-feature-management-controller', "tier": 2, "role": 'primary'},
        {"id": '10-connector-plugin-governance', "tier": 3, "role": 'supporting'},
    ],
    '2.17': [
        {"id": '21-cross-tenant-agent-federation-auditor', "tier": 3, "role": 'primary'},
    ],
    '3.8a': [
        {"id": '20-generative-ai-model-governance-monitor', "tier": 3, "role": 'primary'},
    ],
    '3.14': [
        {"id": '22-pages-notebooks-retention-tracker', "tier": 3, "role": 'primary'},
    ],
    '4.14': [
        {"id": '23-copilot-studio-lifecycle-tracker', "tier": 3, "role": 'primary'},
    ],
}


# Fold per-control solution arrays into the main AUTHORED dict.
# Overlay-with-replace semantics (see scripts/merge_authored_content.py
# `_REPLACE_FIELDS`) guarantees this list is authoritative.
for _cid, _sols in _SOLUTIONS_BY_CONTROL.items():
    AUTHORED.setdefault(_cid, {})["solutions"] = list(_sols)
