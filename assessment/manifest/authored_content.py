"""Authored manifest content for all 64 controls.

This module contains hand-authored values for the SPA-extension fields
that require human judgment (yesBar/partialBar/noBar, priority,
sectorYesBar, facilitatorNotes, verifyIn, verifyPowerShell,
evidenceExpected, collectorField).

Used by ``scripts/merge_authored_content.py`` to overlay these values
on top of the harvested manifest, replacing TODO placeholders.

All 64 controls across the four governance pillars are covered:

* Pillar 1 (Readiness): 16 controls (1.1–1.16)
* Pillar 2 (Security): 17 controls (2.1–2.17)
* Pillar 3 (Compliance): 15 controls (3.1–3.14 + 3.8a)
* Pillar 4 (Operations): 16 controls (4.1–4.16)

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
    "credit-union",
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
    # 1.1 — Copilot Readiness Assessment and Data Hygiene
    # ---------------------------------------------------------------
    "1.1": {
        "priority": "critical",
        "yesBar": (
            "A comprehensive pre-deployment readiness assessment of the data "
            "environment has been completed within the last 12 months, covering "
            "SharePoint site hygiene, permission sprawl, sensitivity-label "
            "coverage, and data classification gaps. Findings are tracked in a "
            "remediation backlog with named owners and target dates."
        ),
        "partialBar": (
            "A readiness assessment has been started but does not cover all "
            "data sources (SharePoint, OneDrive, Exchange, Teams), findings "
            "are not tracked in a formal backlog, or the assessment is older "
            "than 12 months."
        ),
        "noBar": (
            "No pre-deployment readiness assessment has been performed, or "
            "Copilot was enabled without documented review of the data "
            "environment posture."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Data Security Posture Management > Overview",
                "url": "https://purview.microsoft.com/datasecurityposturemanagement",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOSite -Limit ALL | Measure-Object"
        ),
        "evidenceExpected": [
            "Readiness assessment report with date, scope, and findings summary",
            "Remediation backlog with named owners and target dates",
            "Data classification coverage percentage across Copilot-grounded sites",
            "Executive sign-off on readiness findings and go/no-go decision",
        ],
        "collectorField": "ReadinessAssessment",
        "sectorYesBar": _sector_map(
            bank=(
                "Readiness assessment covers all Copilot-grounded sites with "
                "NPI; remediation backlog reviewed monthly; aligned to FFIEC IT "
                "Examination Handbook information security expectations."
            ),
            broker_dealer=(
                "Assessment covers trade blotter, research, and client-facing "
                "sites; MNPI sites identified and information-barrier readiness "
                "validated before Copilot enablement."
            ),
            investment_adviser=(
                "Assessment covers client portfolio and private fund document "
                "sites; remediation prioritized by SEC OCIE exam focus areas."
            ),
            insurance_carrier=(
                "Assessment covers claims and underwriting sites with PHI/PII; "
                "HIPAA BAA documentation reviewed for Copilot data processing."
            ),
            credit_union=(
                "Assessment covers member NPI sites; remediation aligned to "
                "NCUA Part 748 expectations."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has a comprehensive pre-deployment readiness assessment been "
                "completed within the last 12 months, covering all data sources "
                "Copilot may access?"
            ),
            "followUp": (
                "Request the readiness assessment report, verify it covers "
                "SharePoint, OneDrive, Exchange, and Teams. Check the "
                "remediation backlog for open items and confirm executive "
                "sign-off on the go/no-go decision."
            ),
            "timeBudgetMinutes": 8,
        },
    },
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
                "portal": "Microsoft Purview portal",
                "path": "Data Security Posture Management > Overview",
                "url": "https://purview.microsoft.com/datasecurityposturemanagement",
            },
            {
                "portal": "Microsoft Purview portal",
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
                "Open Microsoft Purview portal > Data Security Posture Management > "
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
            "RSS is enabled tenant-wide as a short-term scoping control with "
            "a documented allow-list of approved sites (≤100), RCD is used "
            "for targeted high-risk sites, and there is a documented exit "
            "plan to transition to long-term Purview / SAM governance. The "
            "assessment notes that RSS and RCD do not change user permissions "
            "or replace labels, RBAC, or DLP."
        ),
        "partialBar": (
            "RSS is enabled but the allow-list lacks documented review "
            "cadence, exceptions for recently accessed or Teams/Outlook-shared "
            "sites are not tracked, RCD is used without a written exception "
            "register, or no exit plan to long-term governance exists."
        ),
        "noBar": (
            "RSS is not enabled and no compensating control (RCD targeted "
            "exclusions, Purview / SAM access governance, or item-level "
            "scoping) is in place to limit Copilot's tenant-wide search scope."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint admin center",
                "path": "Settings > Search > Restricted SharePoint Search",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOTenantRestrictedSearchMode; "
            "Get-SPOTenantRestrictedSearchAllowedList; "
            "Get-SPOSite -Identity https://<site-url> | "
            "Select-Object Url, RestrictContentOrgWideSearch"
        ),
        "evidenceExpected": [
            "PowerShell output showing Get-SPOTenantRestrictedSearchMode returns Enabled",
            "Current allow-list site URLs (≤100) with business owner per site",
            "RCD exception register for targeted site-level exclusions",
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
                "Open SharePoint admin center > Settings > Search and verify "
                "Restricted SharePoint Search is on. Run Get-SPOTenantRestrictedSearchMode "
                "and Get-SPOTenantRestrictedSearchAllowedList, confirm count is within "
                "the 100-site limit, and ask the SharePoint Admin who owns the "
                "quarterly review and where recently accessed/shared exceptions are documented."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 1.4 — Semantic Index Governance and Scope Control
    # ---------------------------------------------------------------
    "1.4": {
        "priority": "high",
        "yesBar": (
            "Semantic-index inclusion/exclusion rules are documented, reviewed "
            "on a scheduled cadence (quarterly or better), and aligned with "
            "the organization's data-classification policy. Sites excluded "
            "from indexing are logged with business justification."
        ),
        "partialBar": (
            "Semantic-index rules exist but lack a documented review cadence, "
            "or exclusion decisions are ad hoc without business justification."
        ),
        "noBar": (
            "No semantic-index governance exists, or Copilot indexes all "
            "tenant content without documented scoping decisions."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint admin center",
                "path": "Settings > Search > Content Processing",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOSite -Limit ALL | Select-Object Url, DenyAddAndCustomizePages, "
            "SearchBoxInNavBar"
        ),
        "evidenceExpected": [
            "Documented semantic-index scope policy with inclusion/exclusion criteria",
            "List of sites excluded from indexing with business justification",
            "Review cadence evidence (meeting minutes, policy revision date)",
            "Data classification alignment documentation",
        ],
        "collectorField": "SPO_SemanticIndexScope",
        "sectorYesBar": _sector_map(
            bank=(
                "Semantic index scoped to exclude NPI-bearing sites without "
                "compensating DLP controls; scope reviewed quarterly by "
                "information-security team."
            ),
            broker_dealer=(
                "Research and MNPI sites governed by information barriers; "
                "semantic-index exclusions reviewed by supervisory principal."
            ),
            investment_adviser=(
                "Index scope reviewed for client portfolio and private fund "
                "document sites; exclusions aligned to SEC Reg S-P NPI handling."
            ),
            insurance_carrier=(
                "Index scope excludes claims and underwriting sites with PHI/PII "
                "unless compensating DLP controls are in place."
            ),
            credit_union=(
                "Index scope reviewed for member NPI sites per NCUA Part 748 "
                "expectations; exclusions documented with business justification."
            ),
            other=(
                "Index scope reviewed and exclusions documented with business "
                "justification per organization's data governance policy."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are semantic-index inclusion/exclusion rules documented and "
                "reviewed on a scheduled cadence?"
            ),
            "followUp": (
                "Request the index scope policy document. Verify review cadence "
                "and check that high-risk sites are excluded or have "
                "compensating controls."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 1.5 — Sensitivity Label Taxonomy Review for Copilot
    # ---------------------------------------------------------------
    "1.5": {
        "priority": "high",
        "yesBar": (
            "The sensitivity-label taxonomy has been reviewed for AI readiness "
            "within the last 12 months. Labels used for Copilot content "
            "exclusion (DLP) and grounding-scope control are documented, and "
            "auto-labeling policies cover high-risk content types."
        ),
        "partialBar": (
            "Sensitivity labels exist but have not been reviewed for Copilot "
            "AI readiness, or auto-labeling is not configured for high-risk "
            "content types that Copilot may access."
        ),
        "noBar": (
            "No sensitivity-label taxonomy review has been performed for "
            "Copilot readiness, or labels are not used in DLP policies "
            "targeting the Copilot location."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Information Protection > Labels",
                "url": "https://purview.microsoft.com/informationprotection/labels",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-Label | Select-Object Name, Priority, ContentType, "
            "ParentLabelDisplay"
        ),
        "evidenceExpected": [
            "Sensitivity-label taxonomy document with AI-readiness review date",
            "Labels mapped to Copilot DLP content-exclusion rules",
            "Auto-labeling policy configuration for high-risk content types",
            "Label usage report showing coverage across Copilot-grounded sites",
        ],
        "collectorField": "Purview_SensitivityLabelTaxonomy",
        "sectorYesBar": _sector_map(
            bank=(
                "Label taxonomy reviewed for NPI classification; auto-labeling "
                "covers customer financial data per GLBA §501(b)."
            ),
            broker_dealer=(
                "Labels cover MNPI, research, and client-confidential tiers; "
                "reviewed by supervisory principal for FINRA WSP alignment."
            ),
            insurance_carrier=(
                "Labels cover PHI and PII tiers; HIPAA alignment verified "
                "with privacy officer."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has the sensitivity-label taxonomy been reviewed for AI "
                "readiness in the last 12 months?"
            ),
            "followUp": (
                "Open Microsoft Purview portal > Information Protection > Labels. "
                "Verify the taxonomy has been reviewed for Copilot and that "
                "DLP rules reference the appropriate labels."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 1.6 — Permission Model Audit
    # ---------------------------------------------------------------
    "1.6": {
        "priority": "critical",
        "yesBar": (
            "A least-privilege permission audit covering all Copilot-grounded "
            "sites (SharePoint, OneDrive, Exchange, Teams) has been completed "
            "within the last 90 days. 'Everyone' and 'Everyone Except External "
            "Users' (EEEU) grants are remediated or documented with "
            "compensating controls."
        ),
        "partialBar": (
            "A permission audit has been completed but does not cover all "
            "Copilot-grounded sources, is older than 90 days, or EEEU grants "
            "remain without documented compensating controls."
        ),
        "noBar": (
            "No permission audit has been performed for Copilot-grounded "
            "content sources, or broad sharing (Everyone/EEEU) exists on "
            "sensitive sites without remediation."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint admin center",
                "path": "Active sites > Sharing column",
                "url": "https://admin.microsoft.com/sharepoint",
            },
            {
                "portal": "Microsoft Purview portal",
                "path": "DSPM for AI > Reports",
                "url": "https://purview.microsoft.com/aihub",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOSite -Limit ALL | Select-Object Url, SharingCapability, "
            "ConditionalAccessPolicy"
        ),
        "evidenceExpected": [
            "Permission audit report with date, scope, and findings",
            "List of sites with Everyone/EEEU sharing and remediation status",
            "Least-privilege evidence for Copilot-grounded knowledge sources",
            "Audit cadence documentation (90-day cycle)",
        ],
        "collectorField": "SPO_PermissionAudit",
        "sectorYesBar": _sector_map(
            bank=(
                "Permission audit covers all NPI-bearing sites; EEEU grants "
                "remediated within 5 business days; audit cadence aligned to "
                "GLBA §501(b) safeguards."
            ),
            broker_dealer=(
                "Audit covers research, IB, and client-facing sites; "
                "information-barrier scope validated at each audit cycle."
            ),
            insurance_carrier=(
                "Audit covers claims and underwriting sites with PHI; "
                "HIPAA access-control evidence produced."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has a least-privilege permission audit covering all "
                "Copilot-grounded sites been completed within the last 90 days?"
            ),
            "followUp": (
                "Request the audit report. Verify coverage of SharePoint, "
                "OneDrive, and Teams. Check for unresolved Everyone/EEEU "
                "grants on sensitive sites."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 1.7 — SharePoint Advanced Management Readiness
    # ---------------------------------------------------------------
    "1.7": {
        "priority": "high",
        "yesBar": (
            "SharePoint Advanced Management (SAM) features — including "
            "Restricted Access Control (RAC), Restricted Content Discoverability "
            "(RCD), Content Management Assessment, site lifecycle management, "
            "and Microsoft 365 Archive — are enabled and configured for "
            "Copilot-grounded sites with a documented governance policy."
        ),
        "partialBar": (
            "SAM is licensed but only partially configured, or governance "
            "policies for RAC/RCD and site lifecycle are not documented."
        ),
        "noBar": (
            "SAM is not licensed or not configured, and no compensating "
            "access-governance controls exist for Copilot-grounded sites."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint admin center",
                "path": "Active sites > Access control column",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOSite -Identity https://<site-url> | "
            "Select-Object Url, RestrictContentOrgWideSearch, "
            "ReadOnlyForUnmanagedDevices"
        ),
        "evidenceExpected": [
            "SAM license confirmation and feature activation status",
            "RAC/RCD configuration for high-risk Copilot-grounded sites",
            "Site lifecycle management policy with review cadence",
            "Content Management Assessment report (if available)",
        ],
        "collectorField": "SPO_AdvancedManagement",
        "sectorYesBar": _sector_map(
            bank=(
                "SAM enabled; RAC applied to NPI sites; site lifecycle "
                "management enforced with quarterly review."
            ),
            broker_dealer=(
                "SAM enabled; RCD applied to research and MNPI sites; "
                "RAC used to enforce information barriers at site level."
            ),
            investment_adviser=(
                "SAM enabled; RAC applied to client portfolio sites; "
                "site lifecycle reviewed quarterly by compliance."
            ),
            insurance_carrier=(
                "SAM enabled; RAC applied to claims and PHI/PII sites; "
                "site lifecycle aligned to data retention requirements."
            ),
            credit_union=(
                "SAM enabled; RAC applied to member NPI sites per NCUA "
                "Part 748; site lifecycle reviewed semi-annually."
            ),
            other=(
                "SAM enabled and configured per organization's data "
                "governance policy; RAC/RCD applied to sensitive sites."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are SharePoint Advanced Management features (RAC, RCD, site "
                "lifecycle) enabled and configured for Copilot-grounded sites?"
            ),
            "followUp": (
                "Open SharePoint admin center > Active sites. Verify RAC/RCD "
                "settings on high-risk sites. Check site lifecycle policies."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 1.8 — Information Architecture Review
    # ---------------------------------------------------------------
    "1.8": {
        "priority": "medium",
        "yesBar": (
            "The information architecture (site topology, hub associations, "
            "content types, metadata taxonomy) has been reviewed for Copilot "
            "grounding suitability. Findings are tracked to remediation with "
            "named owners."
        ),
        "partialBar": (
            "An IA review has been started but does not cover all Copilot-grounded "
            "content sources, or findings are not tracked to remediation."
        ),
        "noBar": (
            "No information architecture review has been performed for "
            "Copilot grounding suitability."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint admin center",
                "path": "Active sites > Hub associations",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "IA review report with date, scope, and grounding suitability findings",
            "Hub-association map for Copilot-grounded sites",
            "Content-type and metadata taxonomy alignment documentation",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(),
        "facilitatorNotes": {
            "ask": (
                "Has the information architecture been reviewed for Copilot "
                "grounding suitability, with findings tracked to remediation?"
            ),
            "followUp": (
                "Request the IA review report. Verify it covers site topology, "
                "hub associations, and metadata for Copilot-grounded sites."
            ),
            "timeBudgetMinutes": 5,
        },
    },
    # ---------------------------------------------------------------
    # 1.9 — License Planning and Copilot Assignment Strategy
    # ---------------------------------------------------------------
    "1.9": {
        "priority": "high",
        "yesBar": (
            "A documented license assignment strategy governs Copilot "
            "enablement by role, department, and risk tier. License "
            "assignments are reviewed on a documented cadence, inactive "
            "licenses are reclaimed, and PAYG cost controls are in place."
        ),
        "partialBar": (
            "Copilot licenses are assigned but without a documented strategy, "
            "or license utilization is not reviewed on a regular cadence."
        ),
        "noBar": (
            "No license assignment strategy exists, or Copilot licenses are "
            "assigned broadly without role-based or risk-tiered governance."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Billing > Licenses",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/licenses",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes User.Read.All; "
            "Get-MgUser -Filter \"assignedLicenses/any(l:l/skuId eq "
            "'639dec6b-bb19-468b-871c-c5c441c4b0cb')\" -CountVariable count; "
            "$count"
        ),
        "evidenceExpected": [
            "License assignment strategy document with role/risk-tier mapping",
            "Current license utilization report from M365 admin center",
            "License reclamation cadence and recent reclamation evidence",
            "PAYG budget thresholds and alert configuration",
        ],
        "collectorField": "M365Admin_LicenseAssignment",
        "sectorYesBar": _sector_map(
            bank=(
                "License assignment aligned to bank cost centers; inactive "
                "licenses reclaimed monthly; PAYG budgets reviewed under SOX "
                "IT general controls."
            ),
            broker_dealer=(
                "Licenses assigned by registered-rep status; utilization "
                "reviewed monthly by supervisory principal."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is there a documented license assignment strategy with "
                "role-based or risk-tiered governance and regular utilization "
                "review?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Billing > Licenses. Verify "
                "Copilot license count, assignment method, and reclamation cadence."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 1.10 — Vendor Risk Management for Microsoft AI Services
    # ---------------------------------------------------------------
    "1.10": {
        "priority": "high",
        "yesBar": (
            "A vendor risk assessment (per OCC Bulletin 2023-17) has been "
            "completed for Microsoft Copilot, covering data processing, "
            "sub-processor risk, and third-party plug-in/connector risk. "
            "The assessment is refreshed annually or on material change."
        ),
        "partialBar": (
            "A vendor risk assessment exists but does not cover plug-ins and "
            "connectors, or has not been refreshed within the last 12 months."
        ),
        "noBar": (
            "No vendor risk assessment has been completed for Microsoft "
            "Copilot or its extensibility surfaces."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Vendor risk assessment report for Microsoft Copilot (dated)",
            "Sub-processor risk evaluation covering Azure OpenAI data processing",
            "Third-party plug-in/connector risk inventory and assessment",
            "Annual refresh schedule or material-change trigger documentation",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "Vendor risk assessment aligned to OCC Bulletin 2023-17; "
                "third-party AI services included in bank's vendor management "
                "program with annual refresh."
            ),
            broker_dealer=(
                "Assessment includes FINRA Regulatory Notice coverage; "
                "vendor risk reviewed as part of supervisory review program."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has a vendor risk assessment per OCC Bulletin 2023-17 been "
                "completed for Copilot, plug-ins, and connectors?"
            ),
            "followUp": (
                "Request the vendor risk assessment report. Verify it covers "
                "data processing, sub-processor risk, and extensibility "
                "surfaces. Confirm refresh cadence."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 1.11 — Organizational Change Management and Adoption Planning
    # ---------------------------------------------------------------
    "1.11": {
        "priority": "medium",
        "yesBar": (
            "A documented change-management and adoption plan is in place for "
            "Copilot rollout, with executive sponsorship, stakeholder "
            "communication cadence, and success metrics defined."
        ),
        "partialBar": (
            "A change-management plan exists but lacks executive sponsorship, "
            "defined success metrics, or a structured communication cadence."
        ),
        "noBar": (
            "No change-management or adoption plan exists for Copilot rollout."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Change-management and adoption plan document",
            "Executive sponsor designation and communication cadence",
            "Success metrics / KPIs for Copilot adoption",
            "Stakeholder communication log or newsletter archive",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "Change management aligned to OCC Heightened Standards "
                "(12 CFR part 30, appendix D) for technology adoption."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is a documented change-management and adoption plan in place "
                "for Copilot rollout, with executive sponsorship?"
            ),
            "followUp": (
                "Request the adoption plan. Verify executive sponsor, success "
                "metrics, and communication cadence."
            ),
            "timeBudgetMinutes": 5,
        },
    },
    # ---------------------------------------------------------------
    # 1.12 — Training and Awareness Program
    # ---------------------------------------------------------------
    "1.12": {
        "priority": "medium",
        "yesBar": (
            "All in-scope users have completed Copilot training and "
            "acceptable-use acknowledgement within the last 12 months. "
            "Training covers responsible AI use, data handling expectations, "
            "and firm-specific policies."
        ),
        "partialBar": (
            "Training exists but completion rate is below target, "
            "acceptable-use acknowledgement is not tracked, or training "
            "has not been refreshed within 12 months."
        ),
        "noBar": (
            "No Copilot training or acceptable-use program exists, or "
            "users are enabled without training completion verification."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Training completion report with percentage of in-scope users trained",
            "Acceptable-use policy and acknowledgement tracking records",
            "Training curriculum covering responsible AI use and firm policies",
            "Annual refresh date for training content",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "Training covers GLBA NPI handling expectations for AI; "
                "completion tracked per FFIEC IT Handbook requirements."
            ),
            broker_dealer=(
                "Training includes FINRA Rule 3110 supervisory awareness; "
                "completion tracked for registered representatives."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Have all in-scope users completed Copilot training and "
                "acceptable-use acknowledgement in the last 12 months?"
            ),
            "followUp": (
                "Request training completion reports. Verify acceptable-use "
                "acknowledgement is tracked and training covers responsible "
                "AI use."
            ),
            "timeBudgetMinutes": 5,
        },
    },
    # ---------------------------------------------------------------
    # 1.13 — Extensibility Readiness
    # ---------------------------------------------------------------
    "1.13": {
        "priority": "high",
        "yesBar": (
            "An extensibility governance framework (covering declarative "
            "agents, plug-ins, Graph connectors, and MCP) has been formally "
            "adopted before enabling extensibility surfaces. The framework "
            "includes approval workflows, inventory management, and risk "
            "classification."
        ),
        "partialBar": (
            "Extensibility surfaces are enabled but governance is partial — "
            "approval workflow exists for some but not all surfaces, or "
            "inventory is incomplete."
        ),
        "noBar": (
            "No extensibility governance framework exists, or extensibility "
            "surfaces are enabled without formal approval or inventory."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Settings > Integrated apps",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/Settings/IntegratedApps",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Extensibility governance framework document",
            "Approval workflow documentation for agents, plug-ins, connectors",
            "Current extensibility inventory (agents, plug-ins, connectors, MCP)",
            "Risk classification scheme for extensibility surfaces",
        ],
        "collectorField": "M365Admin_ExtensibilityInventory",
        "sectorYesBar": _sector_map(
            bank=(
                "Extensibility governance aligned to OCC Bulletin 2023-17 "
                "third-party risk requirements; each connector/plug-in "
                "risk-classified before approval."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has an extensibility governance framework been formally "
                "adopted before enabling agents, plug-ins, and connectors?"
            ),
            "followUp": (
                "Request the governance framework. Verify approval workflows "
                "and inventory for all extensibility surfaces."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 1.14 — Item-Level Permission Scanning
    # ---------------------------------------------------------------
    "1.14": {
        "priority": "high",
        "yesBar": (
            "Item-level permissions on Copilot-grounded knowledge sources "
            "are scanned on a documented cadence. Items with overly broad "
            "permissions (Everyone, EEEU, large security groups) are flagged "
            "and remediated with named owners."
        ),
        "partialBar": (
            "Item-level scanning exists but runs ad hoc without a documented "
            "cadence, or flagged items are not tracked to remediation."
        ),
        "noBar": (
            "No item-level permission scanning is performed on Copilot-grounded "
            "knowledge sources."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "DSPM for AI > Reports",
                "url": "https://purview.microsoft.com/aihub",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOSite -Identity https://<site-url> | "
            "Select-Object Url, SharingCapability"
        ),
        "evidenceExpected": [
            "Item-level permission scan report with scan date and scope",
            "List of items with overly broad permissions and remediation status",
            "Documented scan cadence (weekly, monthly, quarterly)",
            "Remediation backlog with named owners",
        ],
        "collectorField": "SPO_ItemLevelPermissions",
        "sectorYesBar": _sector_map(
            bank=(
                "Item-level scans cover NPI-bearing documents; overly broad "
                "permissions remediated within 5 business days per GLBA "
                "§501(b) safeguards."
            ),
            broker_dealer=(
                "Scans cover MNPI documents; information-barrier compliance "
                "validated at item level."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are item-level permissions on Copilot-grounded knowledge "
                "sources scanned and reviewed on a documented cadence?"
            ),
            "followUp": (
                "Request the most recent scan report. Verify scan cadence "
                "and check remediation status for flagged items."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 1.15 — SharePoint Permissions Drift Detection
    # ---------------------------------------------------------------
    "1.15": {
        "priority": "high",
        "yesBar": (
            "SharePoint permissions drift is monitored on a documented cadence "
            "using RAC, site lifecycle management, or automated scripts. "
            "Drift events are reconciled and documented."
        ),
        "partialBar": (
            "Permissions drift monitoring exists but runs ad hoc, or drift "
            "events are not reconciled within a defined SLA."
        ),
        "noBar": (
            "No permissions drift monitoring is in place for Copilot-grounded "
            "SharePoint sites."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint admin center",
                "path": "Active sites > Sharing column",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOSite -Limit ALL | Select-Object Url, SharingCapability, "
            "LastContentModifiedDate"
        ),
        "evidenceExpected": [
            "Permissions drift detection report or alert log",
            "Reconciliation records for detected drift events",
            "Monitoring cadence documentation",
            "RAC or site lifecycle management configuration evidence",
        ],
        "collectorField": "SPO_PermissionsDrift",
        "sectorYesBar": _sector_map(
            bank=(
                "Drift monitoring runs weekly on NPI sites; reconciliation "
                "SLA is 5 business days."
            ),
            broker_dealer=(
                "Drift monitoring includes information-barrier-protected "
                "sites; reconciliation documented for FINRA exam readiness."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is SharePoint permissions drift monitored and reconciled on "
                "a documented cadence?"
            ),
            "followUp": (
                "Request drift detection evidence. Verify monitoring cadence "
                "and reconciliation records."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 1.16 — Copilot Tuning Governance
    # ---------------------------------------------------------------
    "1.16": {
        "priority": "high",
        "yesBar": (
            "Copilot Tuning is subject to a model-governance review (model "
            "risk management, evaluation harness, bias testing) before "
            "publishing tuned models. Tuning artifacts and evaluation results "
            "are retained as governance evidence."
        ),
        "partialBar": (
            "Copilot Tuning governance exists but lacks a formal evaluation "
            "harness or bias-testing requirement, or tuning artifacts are "
            "not retained."
        ),
        "noBar": (
            "No governance process exists for Copilot Tuning, or tuned "
            "models are published without model-risk review."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings > Tuning",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Model-governance review documentation for Copilot Tuning",
            "Evaluation harness results (accuracy, bias, safety)",
            "Tuning artifact retention policy and location",
            "Approval workflow for publishing tuned models",
        ],
        "collectorField": "M365Admin_CopilotTuning",
        "sectorYesBar": _sector_map(
            bank=(
                "Tuning governance aligned to SR 11-7 / OCC Bulletin 2011-12 "
                "model risk management principles; evaluation evidence retained "
                "per bank's model-inventory requirements."
            ),
            broker_dealer=(
                "Tuning review includes supervisory principal approval before "
                "publishing for registered-representative use."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Copilot Tuning subject to a model-governance review "
                "before publishing tuned models?"
            ),
            "followUp": (
                "Request tuning governance documentation. Verify evaluation "
                "harness, bias testing, and artifact retention."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    "2.1": {
        "priority": "critical",
        "yesBar": (
            "DLP controls target the Microsoft 365 Copilot and Copilot Chat "
            "location and cover all three current Copilot scenarios: "
            "(a) sensitivity-label files/emails excluded from Copilot response "
            "processing, (b) SIT-based prompt processing blocked for regulated "
            "data, and (c) SIT-based external web search / web grounding blocked. "
            "Policies are in Enforce mode with documented owner, override "
            "workflow, and match-event review cadence."
        ),
        "partialBar": (
            "At least one DLP rule targets the Microsoft 365 Copilot and "
            "Copilot Chat location, but sensitivity-label content processing, "
            "SIT prompt processing, or SIT external web-search restriction is "
            "missing; the policy is in test/audit mode only; or match events "
            "are not reviewed on a documented cadence."
        ),
        "noBar": (
            "No DLP policy targets the Microsoft 365 Copilot and Copilot Chat "
            "location, or policies exist but are scoped to a single user / "
            "pilot group and not enforced for the approved Copilot user population."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Data Loss Prevention > Policies",
                "url": "https://purview.microsoft.com/datalossprevention/policies",
            },
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings > Web Content",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/copilot/settings/webcontent",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-DlpCompliancePolicy | Where-Object { "
            "$_.EnforcementPlanes -contains 'CopilotExperiences' -or "
            "$_.Locations -match '470f2276-e011-4e9d-a6ec-20768be3a4b0' } | "
            "Select-Object Name, Mode, Enabled, Locations, EnforcementPlanes"
        ),
        "evidenceExpected": [
            "DLP policy export showing 'Microsoft 365 Copilot and Copilot Chat' location or CopilotExperiences enforcement plane in scope",
            "Three Copilot DLP scenarios present: sensitivity-label content processing, SIT prompt processing, and SIT external web-search restriction",
            "Microsoft 365 admin center Web Content setting evidence showing web search scoped per approved user/group",
            "Policy mode = Enforce (not Test / TestWithNotifications)",
            "Match-event report from Microsoft Purview portal > Activity Explorer for the last 30 days",
            "Override workflow document showing who can request and approve overrides",
        ],
        "collectorField": "DLP_CopilotPolicies",
        "sectorYesBar": _sector_map(
            bank=(
                "All three Copilot DLP scenarios enforced; SIT set covers ABA "
                "routing, account numbers, SSN, ITIN, and GLBA §501(b) NPI; "
                "label and external web-search rules cover customer NPI and MNPI labels."
            ),
            broker_dealer=(
                "All three scenarios enforced; SIT set covers CRD numbers, "
                "account numbers, SSN; label and web-search rules align with "
                "Research and IB Confidential labels supporting information-barrier policy."
            ),
            investment_adviser=(
                "All three scenarios enforced; SIT set covers SSN, account numbers, "
                "and adviser-firm-defined SITs for client portfolio identifiers, "
                "including external web-search restrictions for those SITs."
            ),
            insurance_carrier=(
                "All three scenarios enforced; SIT set covers SSN, policy numbers, "
                "and PHI patterns; label and web-search rules align with PHI "
                "sensitivity labels."
            ),
            credit_union=(
                "All three scenarios enforced; SITs cover member account numbers "
                "+ SSN; label and web-search rules align to NCUA NPI categories."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Copilot DLP controls enforced for the Microsoft 365 Copilot "
                "and Copilot Chat location across sensitivity-label content, "
                "SIT prompt processing, and external web search / web grounding?"
            ),
            "followUp": (
                "Open Microsoft Purview portal > Data Loss Prevention > Policies. "
                "Filter by location 'Microsoft 365 Copilot and Copilot Chat' "
                "or policies using the CopilotExperiences enforcement plane. "
                "Confirm three rule/action patterns exist: sensitivity-label "
                "content processing, SIT prompt processing, and SIT external "
                "web-search restriction, all in Enforce mode. Then open "
                "Microsoft 365 admin center > Copilot > Settings > Web Content "
                "to verify web search is scoped to approved users/groups, and "
                "use Activity Explorer to show match events from the last 30 days."
            ),
            "timeBudgetMinutes": 12,
        },
    },
    # ---------------------------------------------------------------
    # 2.2 — Sensitivity Labels and Copilot Content Classification
    # ---------------------------------------------------------------
    "2.2": {
        "priority": "critical",
        "yesBar": (
            "Sensitivity labels are published and enforced across all "
            "Copilot-eligible workloads. Auto-labeling policies cover "
            "high-risk content types, labels propagate to Copilot-generated "
            "content, and label usage is monitored via Activity Explorer."
        ),
        "partialBar": (
            "Sensitivity labels are published but auto-labeling is incomplete, "
            "label propagation to Copilot outputs is not verified, or label "
            "usage is not monitored."
        ),
        "noBar": (
            "Sensitivity labels are not applied to Copilot-eligible content, "
            "or labeling is optional without enforcement."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Information Protection > Labels",
                "url": "https://purview.microsoft.com/informationprotection/labels",
            },
            {
                "portal": "Microsoft Purview portal",
                "path": "Information Protection > Label policies",
                "url": "https://purview.microsoft.com/informationprotection/labelpolicies",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-Label | Select-Object Name, Priority, ContentType; "
            "Get-LabelPolicy | Select-Object Name, Labels, Settings"
        ),
        "evidenceExpected": [
            "Sensitivity-label taxonomy with Copilot content classification mapping",
            "Auto-labeling policy configuration and coverage report",
            "Label usage report from Activity Explorer for the last 30 days",
            "Evidence of label propagation to Copilot-generated outputs",
        ],
        "collectorField": "Purview_SensitivityLabels",
        "sectorYesBar": _sector_map(
            bank=(
                "Labels cover NPI, MNPI, and customer-financial-data "
                "classifications per GLBA §501(b); auto-labeling enforced "
                "for Copilot-grounded document libraries."
            ),
            broker_dealer=(
                "Labels align with information-barrier segments (Research "
                "Confidential, IB Confidential, Client Confidential); "
                "auto-labeling covers trade blotters and research reports."
            ),
            investment_adviser=(
                "Labels cover client portfolio data and private fund documents; "
                "auto-labeling aligned to SEC Reg S-P NPI categories."
            ),
            insurance_carrier=(
                "Labels cover PHI and PII classifications; auto-labeling "
                "enforced for claims and underwriting document libraries."
            ),
            credit_union=(
                "Labels cover member NPI per NCUA Part 748; auto-labeling "
                "configured for member-facing document sites."
            ),
            other=(
                "Labels applied per organization's data classification policy; "
                "auto-labeling configured for high-risk content types."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are sensitivity labels published and enforced across all "
                "Copilot-eligible workloads with auto-labeling for high-risk "
                "content?"
            ),
            "followUp": (
                "Open Microsoft Purview portal > Information Protection. "
                "Verify label policies, auto-labeling rules, and check "
                "Activity Explorer for label usage trends."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 2.3 — Conditional Access Policies for Copilot
    # ---------------------------------------------------------------
    "2.3": {
        "priority": "critical",
        "yesBar": (
            "Conditional Access policies enforce MFA, compliant-device "
            "requirements, and location-based restrictions for Copilot "
            "workloads. Policies target the Office 365 and Microsoft 365 "
            "Copilot app registrations and are in Report-only for at least "
            "7 days before enforcement."
        ),
        "partialBar": (
            "CA policies exist but do not specifically target Copilot "
            "workloads, MFA is not enforced for all Copilot-eligible users, "
            "or device compliance is not required."
        ),
        "noBar": (
            "No Conditional Access policies target Copilot workloads, or "
            "Copilot is accessible without MFA or device compliance."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Entra admin center",
                "path": "Protection > Conditional Access > Policies",
                "url": "https://entra.microsoft.com/#view/Microsoft_AAD_ConditionalAccess/ConditionalAccessBlade/~/Policies",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes Policy.Read.All; "
            "Get-MgIdentityConditionalAccessPolicy | "
            "Select-Object DisplayName, State, Conditions, GrantControls"
        ),
        "evidenceExpected": [
            "CA policy export targeting Copilot / Office 365 app registrations",
            "MFA enforcement evidence for Copilot-eligible users",
            "Device compliance requirement configuration",
            "Location-based restriction configuration (if applicable)",
        ],
        "collectorField": "Graph_ConditionalAccessPolicies",
        "sectorYesBar": _sector_map(
            bank=(
                "CA policies enforce MFA + compliant device for all Copilot "
                "users; location restrictions apply to high-risk NPI access "
                "per FFIEC expectations."
            ),
            broker_dealer=(
                "CA policies enforce MFA for all registered representatives "
                "using Copilot; compliant device required per FINRA "
                "cybersecurity guidance."
            ),
            insurance_carrier=(
                "CA policies enforce MFA and compliant device per NYDFS "
                "Part 500 MFA requirements for Copilot workloads."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Do Conditional Access policies enforce MFA and device "
                "compliance for Copilot workloads?"
            ),
            "followUp": (
                "Open Microsoft Entra admin center > Conditional Access. "
                "Filter policies by target app (Office 365 / Copilot). "
                "Verify MFA and device compliance are required."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 2.4 — Information Barriers for Copilot (Chinese Wall)
    # ---------------------------------------------------------------
    "2.4": {
        "priority": "critical",
        "yesBar": (
            "Information Barrier (IB) policies are configured to prevent "
            "Copilot from surfacing content across ethical-wall segments "
            "(e.g., Research and Investment Banking). IB segments are tested, "
            "verified, and reviewed on a documented cadence."
        ),
        "partialBar": (
            "IB policies exist but have not been tested for Copilot content "
            "surfacing scenarios, or segment definitions are incomplete."
        ),
        "noBar": (
            "No Information Barrier policies are configured, or Copilot "
            "can surface content across ethical-wall segments without "
            "restriction."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Information Barriers > Policies",
                "url": "https://purview.microsoft.com/informationbarriers",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-InformationBarrierPolicy | Select-Object Name, State, "
            "AssignedSegment, SegmentsAllowed, SegmentsBlocked"
        ),
        "evidenceExpected": [
            "IB policy configuration export with segment definitions",
            "Test results showing Copilot honors IB boundaries",
            "Segment membership review cadence documentation",
            "Ethical-wall compliance evidence for examiner response",
        ],
        "collectorField": "Graph_InformationBarriers",
        "sectorYesBar": _sector_map(
            bank=(
                "IB segments separate wealth management, commercial lending, "
                "and trust; Copilot boundary testing documented quarterly."
            ),
            broker_dealer=(
                "IB segments enforce Research / IB / Trading separation per "
                "FINRA Rule 5280 and SEC Rule 10b-5 requirements; Copilot "
                "boundary tested at each IB policy change."
            ),
            investment_adviser=(
                "IB segments separate public-side and private-side functions; "
                "Copilot boundary compliance documented for SEC OCIE exams."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Information Barrier policies configured and tested for "
                "Copilot content surfacing across ethical-wall segments?"
            ),
            "followUp": (
                "Open Microsoft Purview portal > Information Barriers. "
                "Verify segment definitions and test that Copilot respects "
                "IB boundaries in a controlled test."
            ),
            "timeBudgetMinutes": 10,
        },
    },
    # ---------------------------------------------------------------
    # 2.5 — Data Minimization and Grounding Scope
    # ---------------------------------------------------------------
    "2.5": {
        "priority": "high",
        "yesBar": (
            "Data minimization has been applied to Copilot grounding scope: "
            "per-agent and per-site limits are documented, grounding sources "
            "are approved, and scope is reviewed on a documented cadence."
        ),
        "partialBar": (
            "Grounding scope limits exist but are not formally documented, "
            "or review cadence is not established."
        ),
        "noBar": (
            "No data minimization has been applied to Copilot grounding "
            "scope, or all tenant content is available without scoping."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint admin center",
                "path": "Active sites",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Grounding scope policy with approved knowledge-source list",
            "Per-agent or per-site scope limits documentation",
            "Review cadence for grounding scope (quarterly or better)",
            "Approval records for adding new grounding sources",
        ],
        "collectorField": "SPO_GroundingScope",
        "sectorYesBar": _sector_map(
            bank=(
                "Grounding scope excludes NPI-bearing sites without DLP "
                "controls; approved grounding list reviewed quarterly."
            ),
            broker_dealer=(
                "Grounding scope respects information barriers; research and "
                "MNPI sites excluded unless IB-validated."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has data minimization been applied to Copilot grounding "
                "scope with documented per-agent/site limits?"
            ),
            "followUp": (
                "Request the approved grounding-source list. Verify scope "
                "limits and review cadence."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.6 — Copilot Web Search and Web Grounding Controls
    # ---------------------------------------------------------------
    "2.6": {
        "priority": "high",
        "yesBar": (
            "Web search and web grounding in Copilot Chat are configured "
            "per the organization's risk appetite: enabled for approved "
            "user groups via Microsoft 365 admin center, with DLP policies "
            "blocking SIT-based queries from triggering external web search, "
            "and usage monitored via audit logs."
        ),
        "partialBar": (
            "Web search is enabled but not scoped to approved user groups, "
            "DLP web-search restriction is not configured, or usage is not "
            "monitored."
        ),
        "noBar": (
            "Web search settings have not been reviewed or configured, or "
            "web search is enabled tenant-wide without DLP controls."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings > Web Content",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/copilot/settings/webcontent",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Microsoft 365 admin center Web Content setting screenshot",
            "Approved user group list for web search enablement",
            "DLP policy evidence showing SIT-based web-search restriction",
            "Audit log review cadence for web-search usage",
        ],
        "collectorField": "M365Admin_WebSearchSettings",
        "sectorYesBar": _sector_map(
            bank=(
                "Web search disabled for users handling NPI; enabled only "
                "for approved groups with DLP web-search restriction for "
                "regulated SITs."
            ),
            broker_dealer=(
                "Web search disabled for registered representatives by "
                "default; enabled only with supervisory approval and DLP "
                "MNPI SIT restriction."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are web search and web grounding controls configured for "
                "Copilot Chat with appropriate DLP restrictions?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Copilot > Settings > Web "
                "Content. Verify user group scoping and DLP web-search rules."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.7 — Data Residency and Cross-Border Data Flow
    # ---------------------------------------------------------------
    "2.7": {
        "priority": "high",
        "yesBar": (
            "Data residency requirements for Copilot processing are "
            "documented and aligned with the organization's data-sovereignty "
            "policy. Multi-geo configuration is verified, and cross-border "
            "data flows are mapped and approved."
        ),
        "partialBar": (
            "Data residency is considered but not formally documented, "
            "multi-geo settings have not been verified for Copilot, or "
            "cross-border flows are not mapped."
        ),
        "noBar": (
            "No data residency assessment has been performed for Copilot "
            "processing, or data sovereignty requirements are unknown."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Settings > Org settings > Organization profile > Data location",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/Settings/OrganizationProfile/:/Settings/L1/DataResidency",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes Organization.Read.All; "
            "Get-MgOrganization | Select-Object -ExpandProperty "
            "VerifiedDomains"
        ),
        "evidenceExpected": [
            "Data residency policy aligned to Copilot processing locations",
            "Multi-geo configuration verification for Copilot workloads",
            "Cross-border data flow map and approval records",
            "Data sovereignty compliance documentation",
        ],
        "collectorField": "M365Admin_DataResidency",
        "sectorYesBar": _sector_map(
            bank=(
                "Data residency documented per GLBA §501(b); cross-border "
                "flows mapped and approved by legal/compliance."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are data residency requirements documented and verified for "
                "Copilot processing?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Organization profile > "
                "Data location. Verify Copilot processing aligns with data "
                "sovereignty requirements."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.8 — Encryption (Data in Transit and at Rest)
    # ---------------------------------------------------------------
    "2.8": {
        "priority": "high",
        "yesBar": (
            "Encryption at rest and in transit meets or exceeds the "
            "organization's cryptographic standards for all Copilot data "
            "flows. Customer Key or Double Key Encryption is evaluated "
            "for regulated workloads, and TLS 1.2+ is enforced."
        ),
        "partialBar": (
            "Standard Microsoft encryption is in place but Customer Key / "
            "DKE has not been evaluated for regulated workloads, or TLS "
            "enforcement has not been verified."
        ),
        "noBar": (
            "Encryption requirements have not been assessed for Copilot "
            "data flows, or non-standard encryption is in use."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Information Protection > Encryption",
                "url": "https://purview.microsoft.com/informationprotection",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes Organization.Read.All; "
            "Get-MgOrganization | Select-Object -ExpandProperty "
            "SecurityComplianceNotificationPhones"
        ),
        "evidenceExpected": [
            "TLS 1.2+ enforcement evidence for Copilot data flows",
            "Customer Key or DKE evaluation documentation (if applicable)",
            "Encryption-at-rest configuration verification",
            "Cryptographic standards alignment documentation",
        ],
        "collectorField": "Graph_EncryptionSettings",
        "sectorYesBar": _sector_map(
            bank=(
                "TLS 1.2+ enforced; Customer Key evaluated per FFIEC "
                "cryptographic guidance; encryption-at-rest verified "
                "quarterly."
            ),
            insurance_carrier=(
                "Encryption meets NYDFS Part 500 requirements; TLS 1.2+ "
                "enforced for all Copilot data flows."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Does encryption at rest and in transit meet organizational "
                "standards for Copilot data flows?"
            ),
            "followUp": (
                "Verify TLS enforcement and review Customer Key / DKE "
                "evaluation for regulated workloads."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.9 — Defender for Cloud Apps — Copilot Session Controls
    # ---------------------------------------------------------------
    "2.9": {
        "priority": "high",
        "yesBar": (
            "Defender for Cloud Apps session policies and anomaly alerts "
            "are configured for Copilot workloads, reviewed on a documented "
            "cadence, and integrated with the SOC alerting pipeline."
        ),
        "partialBar": (
            "Defender for Cloud Apps is enabled but session policies do not "
            "specifically cover Copilot workloads, or alert review is ad hoc."
        ),
        "noBar": (
            "No Defender for Cloud Apps session controls are configured "
            "for Copilot workloads."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Defender portal",
                "path": "Cloud Apps > Policies > Policy management",
                "url": "https://security.microsoft.com/cloudapps/policies/management",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Defender for Cloud Apps session policy configuration for Copilot",
            "Anomaly detection alert rules targeting Copilot usage",
            "Alert review cadence documentation",
            "SOC integration evidence for Copilot-related alerts",
        ],
        "collectorField": "Defender_CopilotSessionPolicies",
        "sectorYesBar": _sector_map(
            bank=(
                "Session policies monitor exfiltration and anomalous usage "
                "patterns; alerts reviewed by SOC within 4-hour SLA per "
                "FFIEC expectations."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Defender for Cloud Apps Copilot session policies and "
                "anomaly alerts reviewed on a documented cadence?"
            ),
            "followUp": (
                "Open Microsoft Defender portal > Cloud Apps > Policies. "
                "Verify session policies targeting Copilot and alert "
                "review records."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.10 — Insider Risk Detection for Copilot Usage
    # ---------------------------------------------------------------
    "2.10": {
        "priority": "high",
        "yesBar": (
            "Insider Risk Management policies cover Copilot usage patterns, "
            "alerts are triaged on a documented cadence, and escalation "
            "paths to compliance and legal are defined."
        ),
        "partialBar": (
            "Insider Risk policies exist but do not specifically include "
            "Copilot usage indicators, or alert triage cadence is not "
            "documented."
        ),
        "noBar": (
            "No Insider Risk Management policies cover Copilot usage, or "
            "the Insider Risk solution is not enabled."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Insider Risk Management > Policies",
                "url": "https://purview.microsoft.com/insiderriskmanagement",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-InsiderRiskPolicy | Select-Object Name, IsEnabled, "
            "PolicyType"
        ),
        "evidenceExpected": [
            "Insider Risk policy configuration including Copilot indicators",
            "Alert triage cadence and escalation path documentation",
            "Recent alert review log (last 30 days)",
            "Integration with HR/legal escalation workflows",
        ],
        "collectorField": "Purview_InsiderRiskPolicies",
        "sectorYesBar": _sector_map(
            bank=(
                "Insider Risk policies include Copilot data exfiltration "
                "indicators; alerts triaged daily per SOX IT general "
                "control requirements."
            ),
            broker_dealer=(
                "Insider Risk covers registered-rep Copilot usage; alerts "
                "reviewed by supervisory principal per FINRA Rule 3110."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Do Insider Risk Management policies cover Copilot usage "
                "patterns with documented alert triage?"
            ),
            "followUp": (
                "Open Microsoft Purview portal > Insider Risk Management. "
                "Verify policy indicators include Copilot activities and "
                "review recent alert log."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.11 — Copilot Pages Security and Sharing Controls
    # ---------------------------------------------------------------
    "2.11": {
        "priority": "high",
        "yesBar": (
            "Copilot Pages and Loop components have sharing controls aligned "
            "with the organization's data governance policy. External sharing "
            "is restricted, sensitivity labels apply to Pages content, and "
            "sharing activity is audited."
        ),
        "partialBar": (
            "Pages are enabled but sharing controls are at tenant defaults, "
            "sensitivity labels do not apply to Pages, or sharing activity "
            "is not audited."
        ),
        "noBar": (
            "No governance controls are applied to Copilot Pages, or Pages "
            "sharing is unrestricted."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings > Pages",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
            {
                "portal": "SharePoint admin center",
                "path": "Active sites > Loop app",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Pages sharing policy configuration",
            "Sensitivity label enforcement for Pages content",
            "External sharing restriction evidence",
            "Sharing activity audit log entries for Pages",
        ],
        "collectorField": "SPO_PagesSharing",
        "sectorYesBar": _sector_map(
            bank=(
                "Pages external sharing disabled; sensitivity labels "
                "enforced; sharing audit reviewed monthly."
            ),
            broker_dealer=(
                "Pages sharing restricted to internal only; audit logs "
                "reviewed for FINRA Rule 4511 records compliance."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Copilot Pages sharing controls configured with "
                "sensitivity labels and external sharing restrictions?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Copilot > Settings. "
                "Verify Pages sharing policy and label enforcement."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.12 — External Sharing and Guest Access Governance
    # ---------------------------------------------------------------
    "2.12": {
        "priority": "high",
        "yesBar": (
            "External sharing and guest access settings are reviewed for "
            "Copilot-grounded sites. Guest access is restricted to approved "
            "domains, Entra access reviews are configured for guest accounts, "
            "and sharing activity is monitored."
        ),
        "partialBar": (
            "External sharing is restricted but guest access reviews are "
            "not configured, or sharing activity is not monitored for "
            "Copilot-grounded sites."
        ),
        "noBar": (
            "External sharing is unrestricted for Copilot-grounded sites, "
            "or guest access is not governed."
        ),
        "verifyIn": [
            {
                "portal": "SharePoint admin center",
                "path": "Policies > Sharing",
                "url": "https://admin.microsoft.com/sharepoint",
            },
        ],
        "verifyPowerShell": (
            "Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; "
            "Get-SPOTenant | Select-Object SharingCapability, "
            "RequireAcceptingAccountMatchInvitedAccount"
        ),
        "evidenceExpected": [
            "Tenant and site-level sharing policy configuration",
            "Approved external domain list (if domain restriction is used)",
            "Entra access review configuration for guest accounts",
            "Sharing activity monitoring report from audit logs",
        ],
        "collectorField": "SPO_ExternalSharing",
        "sectorYesBar": _sector_map(
            bank=(
                "External sharing disabled for NPI sites; guest access "
                "reviewed quarterly via Entra access reviews per GLBA "
                "§501(b)."
            ),
            broker_dealer=(
                "External sharing restricted per SEC Reg S-P; guest "
                "access reviews conducted monthly."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are external sharing and guest access controls configured "
                "and reviewed for Copilot-grounded sites?"
            ),
            "followUp": (
                "Open SharePoint admin center > Sharing. Verify tenant and "
                "site-level settings. Check Entra access reviews for guest "
                "accounts."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.13 — Plugin and Graph Connector Security Governance
    # ---------------------------------------------------------------
    "2.13": {
        "priority": "high",
        "yesBar": (
            "The plug-in and Graph connector inventory is maintained, "
            "reviewed, and approved on a documented cadence. Unapproved "
            "connectors are blocked, and each approved connector has a "
            "documented risk classification and data-flow assessment."
        ),
        "partialBar": (
            "An inventory exists but is incomplete, review cadence is not "
            "documented, or unapproved connectors are not blocked."
        ),
        "noBar": (
            "No plug-in or connector inventory or governance exists."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Settings > Integrated apps",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/Settings/IntegratedApps",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes Application.Read.All; "
            "Get-MgServicePrincipal -Filter \"tags/any(t:t eq "
            "'WindowsAzureActiveDirectoryIntegratedApp')\" | "
            "Select-Object DisplayName, AppId"
        ),
        "evidenceExpected": [
            "Plug-in and connector inventory with approval status",
            "Risk classification for each approved connector",
            "Data-flow assessment for connectors accessing regulated data",
            "Documented review cadence and most recent review date",
        ],
        "collectorField": "Graph_PluginConnectorInventory",
        "sectorYesBar": _sector_map(
            bank=(
                "Connector risk classification aligned to OCC Bulletin "
                "2023-17; each connector assessed for NPI data-flow risk."
            ),
            broker_dealer=(
                "Connector inventory reviewed by supervisory principal; "
                "data-flow assessments cover MNPI exposure per FINRA "
                "guidance."
            ),
            investment_adviser=(
                "Connectors assessed for client data exposure per SEC "
                "Reg S-P; approved connectors reviewed quarterly by CCO."
            ),
            insurance_carrier=(
                "Connector data-flow assessments cover PHI/PII exposure; "
                "risk classification aligned to NYDFS Part 500."
            ),
            credit_union=(
                "Connector inventory maintained per NCUA examination "
                "expectations; unapproved connectors blocked."
            ),
            other=(
                "Connector inventory maintained and reviewed per "
                "organization's third-party risk management policy."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is the plug-in and connector inventory reviewed and "
                "approved on a documented cadence with unapproved "
                "connectors blocked?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Integrated apps. Verify "
                "inventory completeness and check for unapproved apps."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.14 — Declarative and SharePoint Agents Governance
    # ---------------------------------------------------------------
    "2.14": {
        "priority": "high",
        "yesBar": (
            "Declarative agents are subject to a publishing-approval workflow "
            "with a maintained inventory. Each agent has a documented owner, "
            "data-source scope, and risk classification."
        ),
        "partialBar": (
            "An approval workflow exists but the agent inventory is "
            "incomplete, or not all agents have documented owners and "
            "risk classification."
        ),
        "noBar": (
            "No declarative agent governance exists, or agents are "
            "published without approval or inventory."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Agents > All agents",
                "url": "https://admin.microsoft.com/Adminportal/Home#/agents",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes Application.Read.All; "
            "Get-MgServicePrincipal -Filter \"tags/any(t:t eq "
            "'CopilotAgent')\" | Select-Object DisplayName, AppId, "
            "AccountEnabled"
        ),
        "evidenceExpected": [
            "Declarative agent inventory with owner and risk classification",
            "Publishing-approval workflow documentation",
            "Data-source scope documentation per agent",
            "Most recent inventory review date",
        ],
        "collectorField": "Graph_DeclarativeAgents",
        "sectorYesBar": _sector_map(
            bank=(
                "Agent governance aligned to OCC Bulletin 2023-17; each "
                "agent risk-classified and approved by information-security."
            ),
            broker_dealer=(
                "Agent inventory reviewed by supervisory principal per "
                "FINRA Rule 3110; publishing approval required before "
                "registered-representative use."
            ),
            investment_adviser=(
                "Agent governance aligned to SEC investment adviser "
                "supervisory obligations; data-source scope documented "
                "per agent."
            ),
            insurance_carrier=(
                "Agent risk classification covers PHI/PII data-source "
                "access; approval workflow aligned to NYDFS Part 500."
            ),
            credit_union=(
                "Agent inventory maintained per NCUA expectations; "
                "publishing approval documented."
            ),
            other=(
                "Agent inventory maintained with documented risk "
                "classification and owner assignment."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are declarative agents subject to a publishing-approval "
                "workflow with a maintained inventory?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Agents. Verify inventory "
                "and check approval workflow documentation."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.15 — Network Security and Private Connectivity
    # ---------------------------------------------------------------
    "2.15": {
        "priority": "medium",
        "yesBar": (
            "Network security controls (Private Link, VPN, conditional "
            "access named locations) are configured for Copilot workloads "
            "where required by the organization's network security policy."
        ),
        "partialBar": (
            "Network security is considered but Private Link or conditional "
            "access location restrictions are not implemented for Copilot."
        ),
        "noBar": (
            "No network security controls are applied to Copilot workloads "
            "beyond default Microsoft 365 transport security."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Entra admin center",
                "path": "Protection > Conditional Access > Named locations",
                "url": "https://entra.microsoft.com/#view/Microsoft_AAD_ConditionalAccess/ConditionalAccessBlade/~/NamedLocations",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes Policy.Read.All; "
            "Get-MgIdentityConditionalAccessNamedLocation"
        ),
        "evidenceExpected": [
            "Named location configuration for Copilot CA policies",
            "Private Link configuration (if applicable)",
            "Network security policy alignment documentation",
        ],
        "collectorField": "Graph_NetworkSecurity",
        "sectorYesBar": _sector_map(
            bank=(
                "Named locations restrict Copilot to corporate network / "
                "approved locations per FFIEC network security expectations."
            ),
            insurance_carrier=(
                "Network controls align to NYDFS Part 500 requirements "
                "for access from secure networks."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are network security controls configured for Copilot "
                "workloads per the organization's policy?"
            ),
            "followUp": (
                "Verify CA named locations and Private Link configuration "
                "for Copilot workloads."
            ),
            "timeBudgetMinutes": 5,
        },
    },
    # ---------------------------------------------------------------
    # 2.16 — Federated Copilot Connector and MCP Governance
    # ---------------------------------------------------------------
    "2.16": {
        "priority": "high",
        "yesBar": (
            "Federated connectors and MCP endpoints are subject to a "
            "documented approval process, maintained in an allow-list, and "
            "reviewed on a documented cadence. Each endpoint has a data-flow "
            "assessment and named owner."
        ),
        "partialBar": (
            "An approval process exists but the allow-list is incomplete, "
            "or review cadence is not documented."
        ),
        "noBar": (
            "No governance exists for federated connectors or MCP "
            "endpoints."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Settings > Integrated apps",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/Settings/IntegratedApps",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Federated connector and MCP endpoint allow-list",
            "Approval workflow documentation",
            "Data-flow assessment per endpoint",
            "Review cadence and most recent review date",
        ],
        "collectorField": "Graph_MCPGovernance",
        "sectorYesBar": _sector_map(
            bank=(
                "MCP endpoints assessed per OCC Bulletin 2023-17 third-party "
                "risk requirements; allow-list reviewed quarterly."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are federated connectors and MCP endpoints subject to "
                "documented approval and review?"
            ),
            "followUp": (
                "Request the allow-list and approval records. Verify "
                "data-flow assessments are current."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 2.17 — Cross-Tenant Agent Federation
    # ---------------------------------------------------------------
    "2.17": {
        "priority": "high",
        "yesBar": (
            "Cross-tenant Entra Agent ID trust relationships, MCP federated "
            "server attestations, and Copilot Studio multi-tenant publishings "
            "are subject to documented approval and periodic review. Trust "
            "relationships are inventoried with named owners."
        ),
        "partialBar": (
            "Cross-tenant trust relationships exist but lack formal approval "
            "documentation, or inventory is incomplete."
        ),
        "noBar": (
            "No governance exists for cross-tenant agent federation, or "
            "trust relationships are established without approval."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Entra admin center",
                "path": "Identity > External identities > Cross-tenant access settings",
                "url": "https://entra.microsoft.com/#view/Microsoft_AAD_IAM/CompanyRelationshipsMenuBlade/~/CrossTenantAccessSettings",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes Policy.Read.All; "
            "Get-MgPolicyCrossTenantAccessPolicyPartner"
        ),
        "evidenceExpected": [
            "Cross-tenant trust relationship inventory with named owners",
            "Approval records for each trust relationship",
            "MCP federated server attestation documentation",
            "Periodic review cadence and most recent review date",
        ],
        "collectorField": "Graph_CrossTenantFederation",
        "sectorYesBar": _sector_map(
            bank=(
                "Cross-tenant federation assessed per OCC Bulletin 2023-17; "
                "trust relationships approved by CISO and reviewed "
                "quarterly."
            ),
            broker_dealer=(
                "Federation trust reviewed by supervisory principal; "
                "FINRA Rule 3110 supervision scope includes federated "
                "agent interactions."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are cross-tenant agent trust relationships and MCP "
                "federation subject to documented approval and review?"
            ),
            "followUp": (
                "Open Microsoft Entra admin center > Cross-tenant access. "
                "Verify trust relationships and request approval records."
            ),
            "timeBudgetMinutes": 8,
        },
    },
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
                "portal": "Microsoft Purview portal",
                "path": "Audit > Search",
                "url": "https://purview.microsoft.com/audit/auditsearch",
            },
            {
                "portal": "Microsoft Purview portal",
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
                "UAL on; CopilotInteraction + CopilotAgentManagement events "
                "retained 7 years; SIEM "
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
                "last 24 hours. Open Microsoft Purview portal > Audit > Audit retention policies "
                "and confirm the policy duration matches the firm's regulatory "
                "minimum. Confirm the SIEM/WORM archive destination and cadence."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.2 — Data Retention Policies for Copilot Interactions
    # ---------------------------------------------------------------
    "3.2": {
        "priority": "critical",
        "yesBar": (
            "Retention policies cover Copilot interactions, Copilot Pages, "
            "and Copilot-generated content with retention durations aligned "
            "to the firm's regulatory minimum. Retention labels are applied "
            "to Copilot content locations and verified in Purview."
        ),
        "partialBar": (
            "Retention policies exist but do not specifically cover Copilot "
            "interactions, or retention duration is below the firm's "
            "regulatory minimum."
        ),
        "noBar": (
            "No retention policies cover Copilot interactions or Copilot-"
            "generated content."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Data Lifecycle Management > Retention policies",
                "url": "https://purview.microsoft.com/datalifecyclemanagement/retentionpolicies",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-RetentionCompliancePolicy | Select-Object Name, Enabled, "
            "RetentionDuration, ExchangeLocation, SharePointLocation"
        ),
        "evidenceExpected": [
            "Retention policy export covering Copilot interaction locations",
            "Retention duration aligned to regulatory minimum (often 7 years for FINRA/SEC)",
            "Retention label configuration for Copilot content types",
            "Verification that Copilot Pages/Notebooks are in retention scope",
        ],
        "collectorField": "Purview_RetentionPolicies",
        "sectorYesBar": _sector_map(
            bank=(
                "Retention policies cover Copilot interactions with 7-year "
                "minimum per SOX IT general control requirements."
            ),
            broker_dealer=(
                "Retention policies retain Copilot interactions for 7 years "
                "per FINRA Rule 4511 and SEC Rule 17a-4 where applicable to "
                "required records."
            ),
            investment_adviser=(
                "Retention policies retain Copilot interactions for 5+ years "
                "per Investment Advisers Act Rule 204-2."
            ),
            credit_union=(
                "Retention aligned to NCUA Part 749 record retention "
                "requirements."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Do retention policies cover Copilot interactions with "
                "duration aligned to the firm's regulatory minimum?"
            ),
            "followUp": (
                "Open Microsoft Purview portal > Data Lifecycle Management. "
                "Verify retention policies cover Copilot content locations "
                "and duration meets regulatory requirements."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.3 — eDiscovery for Copilot-Generated Content
    # ---------------------------------------------------------------
    "3.3": {
        "priority": "critical",
        "yesBar": (
            "eDiscovery searches can locate and preserve Copilot-generated "
            "content (interactions, Pages, Notebooks). At least one test "
            "search has confirmed Copilot content is discoverable, and "
            "custodian holds can target Copilot data sources."
        ),
        "partialBar": (
            "eDiscovery is available but Copilot content discoverability "
            "has not been tested, or custodian holds have not been verified "
            "for Copilot data sources."
        ),
        "noBar": (
            "eDiscovery cannot locate Copilot-generated content, or "
            "eDiscovery readiness for Copilot has not been assessed."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "eDiscovery > Cases",
                "url": "https://purview.microsoft.com/ediscovery",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-ComplianceCase | Select-Object Name, Status, CaseType"
        ),
        "evidenceExpected": [
            "Test eDiscovery search results confirming Copilot content is discoverable",
            "Custodian hold configuration targeting Copilot data sources",
            "eDiscovery readiness documentation for Copilot",
            "Confirmation that Copilot Pages/Notebooks are in eDiscovery scope",
        ],
        "collectorField": "Purview_eDiscoveryCases",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "eDiscovery verified for Copilot content per FINRA Rule 4511; "
                "custodian holds tested for registered-rep Copilot data."
            ),
            bank=(
                "eDiscovery readiness verified for Copilot per SOX "
                "litigation-hold requirements."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Can eDiscovery searches locate and preserve Copilot-"
                "generated content including Pages and Notebooks?"
            ),
            "followUp": (
                "Open Microsoft Purview portal > eDiscovery. Verify test "
                "search results for Copilot content and custodian hold "
                "configuration."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.4 — Communication Compliance Monitoring
    # ---------------------------------------------------------------
    "3.4": {
        "priority": "critical",
        "yesBar": (
            "Communication compliance policies cover Copilot interactions "
            "in scope channels (Teams, Outlook). The review queue has been "
            "reviewed within the last 30 days, with documented escalation "
            "paths for policy matches."
        ),
        "partialBar": (
            "Communication compliance policies exist but do not cover "
            "Copilot interaction channels, or the review queue has not "
            "been reviewed within 30 days."
        ),
        "noBar": (
            "No communication compliance policies cover Copilot interactions, "
            "or communication compliance is not enabled."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Communication Compliance > Policies",
                "url": "https://purview.microsoft.com/communicationcompliance",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-SupervisoryReviewPolicyV2 | Select-Object Name, IsEnabled"
        ),
        "evidenceExpected": [
            "Communication compliance policy configuration covering Copilot channels",
            "Review queue log showing reviews within the last 30 days",
            "Escalation path documentation for policy matches",
            "Coverage confirmation for Teams and Outlook Copilot interactions",
        ],
        "collectorField": "Purview_CommCompliancePolicies",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "Communication compliance covers registered-rep Copilot "
                "interactions per FINRA Rule 3110 supervisory requirements "
                "and FINRA Rule 2210 review obligations."
            ),
            bank=(
                "Communication compliance covers Copilot in customer-facing "
                "channels; review queue reviewed weekly."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Do communication compliance policies cover Copilot "
                "interactions with the review queue reviewed in the last "
                "30 days?"
            ),
            "followUp": (
                "Open Microsoft Purview portal > Communication Compliance. "
                "Verify policy scope includes Copilot channels and check "
                "review queue dates."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.5 — FINRA Rule 2210 Compliance
    # ---------------------------------------------------------------
    "3.5": {
        "priority": "critical",
        "yesBar": (
            "Copilot outputs used in FINRA Rule 2210 communications "
            "(retail, institutional, correspondence) are subject to "
            "documented principal review before use. Detection patterns "
            "for prohibited marketing language are configured in "
            "communication compliance."
        ),
        "partialBar": (
            "Principal review exists but is ad hoc, detection patterns "
            "are incomplete, or not all FINRA 2210 communication types "
            "are covered."
        ),
        "noBar": (
            "No principal review or detection process exists for Copilot "
            "outputs used in FINRA 2210 communications."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Communication Compliance > Policies",
                "url": "https://purview.microsoft.com/communicationcompliance",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Principal review workflow for Copilot-drafted communications",
            "Detection pattern configuration for prohibited marketing language",
            "FINRA 2210 communication type coverage documentation",
            "Recent review log showing principal approvals",
        ],
        "collectorField": "Purview_FINRA2210Compliance",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "All Copilot-drafted retail and institutional communications "
                "subject to principal review per FINRA Rule 2210 and FINRA "
                "Regulatory Notice 24-09; detection patterns cover prohibited "
                "promissory and superlative language."
            ),
            investment_adviser=(
                "Copilot-drafted client communications subject to review "
                "per SEC Marketing Rule (Rule 206(4)-1) requirements."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Copilot outputs used in FINRA 2210 communications "
                "subject to documented principal review?"
            ),
            "followUp": (
                "Request the principal review workflow. Verify detection "
                "patterns for prohibited language and review recent "
                "approval records."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.6 — Supervision and Oversight (FINRA 3110 / SEC Reg BI)
    # ---------------------------------------------------------------
    "3.6": {
        "priority": "critical",
        "yesBar": (
            "A designated supervisory principal oversees Copilot use in "
            "regulated workflows with a documented review cadence aligned "
            "to FINRA Rule 3110 Written Supervisory Procedures (WSPs)."
        ),
        "partialBar": (
            "Supervisory oversight exists but lacks a designated principal "
            "for Copilot workflows, or the review cadence is not aligned "
            "to FINRA WSP requirements."
        ),
        "noBar": (
            "No supervisory oversight process exists for Copilot use in "
            "regulated workflows."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Designated supervisory principal for Copilot-related activities",
            "Written Supervisory Procedures (WSPs) addressing Copilot use",
            "Documented review cadence and recent review evidence",
            "Escalation path for supervisory concerns about Copilot outputs",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "Designated supervisory principal per FINRA Rule 3110; WSPs "
                "updated to cover Copilot use in client-facing and trading "
                "workflows; review conducted at least monthly."
            ),
            investment_adviser=(
                "Supervisory oversight aligned to SEC Reg BI best-interest "
                "obligations for Copilot-assisted recommendations."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is there a designated supervisory principal for Copilot "
                "use with a documented review cadence per FINRA Rule 3110?"
            ),
            "followUp": (
                "Request WSP documentation covering Copilot. Verify the "
                "designated principal and recent review records."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.7 — Regulatory Reporting
    # ---------------------------------------------------------------
    "3.7": {
        "priority": "high",
        "yesBar": (
            "Copilot-related regulatory reports (book/record certifications, "
            "AI disclosures, SOX attestations) are produced on the required "
            "cadence with documented evidence trails."
        ),
        "partialBar": (
            "Regulatory reports exist but Copilot-related content is not "
            "specifically addressed, or reporting cadence gaps exist."
        ),
        "noBar": (
            "No regulatory reporting process addresses Copilot-related "
            "activities."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Regulatory reporting schedule including Copilot-related items",
            "Most recent report or certification referencing Copilot",
            "Evidence trail documentation for Copilot regulatory reports",
            "SOX attestation evidence (if applicable to ICFR)",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "SOX §§302/404 attestations address Copilot where applicable "
                "to ICFR; GLBA §501(b) safeguards review includes Copilot."
            ),
            broker_dealer=(
                "FINRA Rule 4530 reporting covers Copilot-related incidents; "
                "books-and-records certifications include Copilot interactions."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Copilot-related regulatory reports produced on the "
                "required cadence?"
            ),
            "followUp": (
                "Request the regulatory reporting schedule and most recent "
                "reports referencing Copilot."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 3.8 — Model Risk Management Alignment
    # ---------------------------------------------------------------
    "3.8": {
        "priority": "high",
        "yesBar": (
            "A model-risk-management review aligned to SR 11-7 / OCC "
            "Bulletin 2011-12 has been completed for Copilot deployments "
            "touching regulated functions. The review documents model "
            "limitations, validation methodology, and ongoing monitoring."
        ),
        "partialBar": (
            "Model risk management is acknowledged but a formal review "
            "has not been completed, or the review does not cover all "
            "regulated functions using Copilot."
        ),
        "noBar": (
            "No model-risk-management review has been performed for "
            "Copilot deployments."
        ),
        "verifyIn": [
            {
                "portal": "Internal GRC platform",
                "path": "Model inventory > Copilot / AI models",
                "url": "https://purview.microsoft.com/compliancemanager",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Model risk management review document for Copilot",
            "Validation methodology and limitation documentation",
            "Ongoing monitoring plan for model performance",
            "Model inventory entry for Copilot (if applicable)",
        ],
        "collectorField": "Compliance_ModelRiskReview",
        "sectorYesBar": _sector_map(
            bank=(
                "MRM review aligned to SR 11-7 / OCC Bulletin 2011-12; "
                "Copilot entered in model inventory with validation schedule."
            ),
            broker_dealer=(
                "MRM review completed for Copilot use in client-facing "
                "functions; validation cadence aligned to FINRA guidance."
            ),
            investment_adviser=(
                "MRM review covers Copilot use in advisory and portfolio "
                "management functions; documentation retained for SEC exam."
            ),
            insurance_carrier=(
                "MRM review covers Copilot use in underwriting and claims; "
                "model limitations documented per NYDFS Part 500."
            ),
            credit_union=(
                "MRM review aligned to NCUA expectations for AI/ML model "
                "governance; Copilot in model inventory."
            ),
            other=(
                "MRM review completed per organization's model governance "
                "policy; validation methodology and monitoring documented."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has a model-risk-management review aligned to SR 11-7 / "
                "OCC Bulletin 2011-12 been completed for Copilot?"
            ),
            "followUp": (
                "Request the MRM review document. Verify it covers "
                "validation methodology, limitations, and ongoing monitoring."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.8a — Generative AI Model Governance
    # ---------------------------------------------------------------
    "3.8a": {
        "priority": "high",
        "yesBar": (
            "A generative-AI model-governance review (NIST AI RMF 1.0 / "
            "ISO/IEC 42001) has been completed for Copilot, addressing the "
            "SR 26-2 / OCC Bulletin 2026-13 generative-AI exclusion. "
            "Governance covers bias testing, safety evaluation, and "
            "responsible-AI principles."
        ),
        "partialBar": (
            "Generative-AI governance is in progress but the review is "
            "incomplete, or not all NIST AI RMF categories are addressed."
        ),
        "noBar": (
            "No generative-AI model-governance review has been completed "
            "for Copilot."
        ),
        "verifyIn": [
            {
                "portal": "Internal GRC platform",
                "path": "AI governance > Generative AI reviews",
                "url": "https://purview.microsoft.com/compliancemanager",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Generative-AI governance review document for Copilot",
            "NIST AI RMF 1.0 alignment documentation",
            "Bias testing and safety evaluation results",
            "Responsible-AI principles adoption evidence",
        ],
        "collectorField": "Compliance_GenAIGovernance",
        "sectorYesBar": _sector_map(
            bank=(
                "GenAI governance aligned to NIST AI RMF 1.0; addresses "
                "SR 26-2 / OCC 2026-13 explicit exclusion of generative AI "
                "by continuing to apply SR 11-7 / OCC 2011-12 principles."
            ),
            broker_dealer=(
                "GenAI governance completed for Copilot use in client-facing "
                "and trading functions; NIST AI RMF alignment documented "
                "for FINRA exam readiness."
            ),
            investment_adviser=(
                "GenAI governance covers Copilot use in advisory functions; "
                "bias testing includes client-communication scenarios."
            ),
            insurance_carrier=(
                "GenAI governance covers Copilot use in underwriting and "
                "claims; bias testing per NYDFS fair lending requirements."
            ),
            credit_union=(
                "GenAI governance aligned to NCUA expectations; NIST AI RMF "
                "categories reviewed for member-facing Copilot use."
            ),
            other=(
                "GenAI governance review completed per organization's AI "
                "policy; NIST AI RMF 1.0 alignment documented."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has a generative-AI model-governance review been completed "
                "for Copilot addressing the SR 26-2 genAI exclusion?"
            ),
            "followUp": (
                "Request the governance review. Verify NIST AI RMF alignment "
                "and bias/safety evaluation results."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.9 — AI Disclosure, Transparency, and SEC Marketing Rule
    # ---------------------------------------------------------------
    "3.9": {
        "priority": "high",
        "yesBar": (
            "AI disclosure language is presented to customers and "
            "counterparties before any Copilot-generated content is shared "
            "externally. Disclosure templates are reviewed by legal/compliance "
            "and align to SEC Marketing Rule requirements."
        ),
        "partialBar": (
            "AI disclosure is used but templates are not reviewed by "
            "legal/compliance, or disclosure is inconsistently applied."
        ),
        "noBar": (
            "No AI disclosure process exists for externally shared "
            "Copilot-generated content."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "AI disclosure template(s) reviewed by legal/compliance",
            "Process documentation for applying disclosure to external content",
            "SEC Marketing Rule alignment documentation",
            "Evidence of disclosure usage in recent external communications",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "AI disclosure aligned to FINRA Regulatory Notice 24-09 "
                "and SEC AI Marketing Risk Alert; disclosure reviewed by "
                "supervisory principal."
            ),
            investment_adviser=(
                "AI disclosure aligned to SEC Marketing Rule (Rule 206(4)-1) "
                "and Investment Advisers Act §206; reviewed by CCO."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is AI disclosure language presented before Copilot-generated "
                "content is shared externally?"
            ),
            "followUp": (
                "Request disclosure templates and verify legal/compliance "
                "review. Check recent external communications for disclosure "
                "presence."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 3.10 — SEC Reg S-P — Privacy of Consumer Financial Information
    # ---------------------------------------------------------------
    "3.10": {
        "priority": "critical",
        "yesBar": (
            "SEC Reg S-P / GLBA §501(b) privacy controls have been reviewed "
            "for Copilot processing of customer NPI. DLP policies prevent "
            "Copilot from surfacing NPI outside authorized workflows, and "
            "privacy impact is documented."
        ),
        "partialBar": (
            "Privacy controls exist but have not been specifically reviewed "
            "for Copilot NPI processing, or DLP policies do not target "
            "NPI in Copilot workflows."
        ),
        "noBar": (
            "No privacy control review has been performed for Copilot "
            "processing of customer NPI."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Data Loss Prevention > Policies",
                "url": "https://purview.microsoft.com/datalossprevention/policies",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-DlpCompliancePolicy | Where-Object { "
            "$_.Workload -match 'Exchange|SharePoint|OneDrive' }"
        ),
        "evidenceExpected": [
            "Privacy impact assessment for Copilot NPI processing",
            "DLP policy configuration preventing NPI surfacing outside authorized workflows",
            "SEC Reg S-P alignment documentation for Copilot",
            "GLBA §501(b) safeguards review covering Copilot",
        ],
        "collectorField": "Purview_RegSP_PrivacyPolicies",
        "sectorYesBar": _sector_map(
            bank=(
                "Privacy controls reviewed for Copilot NPI processing per "
                "GLBA §501(b); DLP policies cover NPI SITs in Copilot "
                "location."
            ),
            broker_dealer=(
                "SEC Reg S-P compliance reviewed for Copilot; NPI DLP "
                "policies cover account numbers, SSN, and client identifiers."
            ),
            investment_adviser=(
                "SEC Reg S-P privacy controls reviewed for Copilot processing "
                "of client NPI; DLP policies cover advisory account data."
            ),
            insurance_carrier=(
                "Privacy controls reviewed for Copilot processing of PHI/PII; "
                "DLP policies cover HIPAA and state privacy requirements."
            ),
            credit_union=(
                "Privacy controls reviewed for Copilot NPI processing per "
                "NCUA Part 748; DLP covers member account identifiers."
            ),
            other=(
                "Privacy controls reviewed for Copilot per organization's "
                "data privacy policy; DLP policies cover sensitive personal data."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Have SEC Reg S-P / GLBA §501(b) privacy controls been "
                "reviewed for Copilot processing of customer NPI?"
            ),
            "followUp": (
                "Request the privacy impact assessment. Verify DLP policies "
                "prevent NPI surfacing outside authorized workflows."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.11 — Record Keeping and Books-and-Records Compliance
    # ---------------------------------------------------------------
    "3.11": {
        "priority": "critical",
        "yesBar": (
            "Copilot interactions are captured into the firm's books-and-"
            "records system per SEC Rule 17a-4 (where applicable to required "
            "broker-dealer records). Retention policies ensure WORM "
            "compliance, and records are retrievable for examiner requests."
        ),
        "partialBar": (
            "Copilot interactions are retained but not in a WORM-compliant "
            "archive, or retrievability for examiner requests has not been "
            "tested."
        ),
        "noBar": (
            "Copilot interactions are not captured in the books-and-records "
            "system, or retention does not meet SEC 17a-4 requirements."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Data Lifecycle Management > Retention policies",
                "url": "https://purview.microsoft.com/datalifecyclemanagement/retentionpolicies",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-RetentionCompliancePolicy | Select-Object Name, "
            "RetentionDuration, RetentionAction"
        ),
        "evidenceExpected": [
            "Books-and-records policy covering Copilot interactions",
            "WORM archive configuration for Copilot records (if applicable)",
            "Retrievability test results for examiner response readiness",
            "Retention duration aligned to SEC 17a-4 / FINRA 4511",
        ],
        "collectorField": "Purview_BooksAndRecords",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "Copilot interactions captured per SEC Rule 17a-4 where "
                "applicable to required records; WORM archive validated; "
                "retrievable within 48 hours for FINRA exam requests."
            ),
            bank=(
                "Copilot interactions retained per SOX record-keeping "
                "requirements where applicable to ICFR evidence."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Copilot interactions captured in the books-and-records "
                "system per SEC 17a-4 (where applicable)?"
            ),
            "followUp": (
                "Verify retention policies, WORM archive configuration, "
                "and test retrievability for examiner requests."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 3.12 — Evidence Collection and Audit Attestation
    # ---------------------------------------------------------------
    "3.12": {
        "priority": "high",
        "yesBar": (
            "A documented evidence-collection runbook exists for Copilot-"
            "related audits and exam responses. The runbook covers all "
            "four collector domains (Graph, Purview, SharePoint, Sentinel) "
            "and produces a portable evidence pack."
        ),
        "partialBar": (
            "Evidence collection exists but is ad hoc, does not cover all "
            "collector domains, or does not produce a portable evidence pack."
        ),
        "noBar": (
            "No evidence-collection process exists for Copilot-related "
            "audits."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Evidence-collection runbook document with collector domain coverage",
            "Sample evidence pack from most recent collection run",
            "Audit attestation template aligned to regulatory requirements",
            "Collection schedule and most recent run date",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "Evidence collection runbook aligned to SOX §§302/404 "
                "attestation requirements where applicable to ICFR."
            ),
            broker_dealer=(
                "Evidence pack structured for FINRA Rule 3120 testing and "
                "inspection response."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is there a documented evidence-collection runbook for "
                "Copilot-related audits and exam responses?"
            ),
            "followUp": (
                "Request the runbook and sample evidence pack. Verify "
                "coverage of all collector domains."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 3.13 — FFIEC IT Examination Handbook Alignment
    # ---------------------------------------------------------------
    "3.13": {
        "priority": "high",
        "yesBar": (
            "FFIEC IT Handbook alignment (Information Security, Outsourcing "
            "Technology Services, Architecture) has been reviewed for Copilot "
            "deployment with documented gap analysis and remediation plan."
        ),
        "partialBar": (
            "FFIEC alignment review is in progress but does not cover all "
            "relevant handbook sections, or gap remediation is not tracked."
        ),
        "noBar": (
            "No FFIEC IT Handbook alignment review has been performed for "
            "Copilot deployment."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "FFIEC IT Handbook alignment assessment for Copilot",
            "Gap analysis document with remediation plan",
            "Coverage of Information Security, Outsourcing, and Architecture sections",
            "Review date and next scheduled review",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "FFIEC alignment covers Information Security Booklet "
                "requirements for AI workloads; gaps tracked with "
                "remediation owners."
            ),
            credit_union=(
                "FFIEC alignment reviewed per NCUA expectations for "
                "technology governance."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has FFIEC IT Handbook alignment been reviewed for Copilot "
                "deployment?"
            ),
            "followUp": (
                "Request the alignment assessment and gap analysis. Verify "
                "coverage of relevant handbook sections."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 3.14 — Copilot Pages and Notebooks Retention and Provenance
    # ---------------------------------------------------------------
    "3.14": {
        "priority": "high",
        "yesBar": (
            "Branch-aware Copilot Pages, Notebook section-level coverage, "
            "and Loop component provenance are addressed in retention and "
            "records-management policies. Provenance metadata tracks which "
            "content originated from Copilot."
        ),
        "partialBar": (
            "Retention policies exist but do not specifically address "
            "Pages/Notebooks branching, section-level granularity, or "
            "Copilot provenance metadata."
        ),
        "noBar": (
            "No retention or provenance governance exists for Copilot "
            "Pages and Notebooks."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Purview portal",
                "path": "Data Lifecycle Management > Retention policies",
                "url": "https://purview.microsoft.com/datalifecyclemanagement/retentionpolicies",
            },
        ],
        "verifyPowerShell": (
            "Connect-IPPSSession; "
            "Get-RetentionCompliancePolicy | Where-Object { "
            "$_.SharePointLocation -ne $null }"
        ),
        "evidenceExpected": [
            "Retention policy covering Copilot Pages and Notebooks",
            "Branch-aware retention configuration documentation",
            "Provenance metadata strategy for Copilot-generated content",
            "Section-level retention granularity documentation",
        ],
        "collectorField": "Purview_PagesRetention",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "Pages/Notebooks retention aligned to FINRA Rule 4511 and "
                "SEC Rule 17a-4 where applicable; provenance tracked for "
                "examiner response."
            ),
            bank=(
                "Retention covers Pages/Notebooks per SOX record-keeping "
                "requirements."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Copilot Pages and Notebooks covered by retention "
                "policies with provenance tracking?"
            ),
            "followUp": (
                "Verify retention policies include Pages/Notebooks "
                "locations. Check provenance metadata availability."
            ),
            "timeBudgetMinutes": 6,
        },
    },
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
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
            {
                "portal": "Microsoft 365 admin center",
                "path": "Agents > All agents",
                "url": "https://admin.microsoft.com/Adminportal/Home#/agents",
            },
            {
                "portal": "Microsoft 365 Apps admin center",
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
                "Open Microsoft 365 admin center > Roles and confirm who "
                "holds AI Administrator. Open Copilot > Settings, Agents > "
                "All agents, and config.office.com Customization > Policy "
                "Management. Ask for the most recent change-management ticket "
                "for a Copilot setting toggle and the documented review cadence."
            ),
            "timeBudgetMinutes": 10,
        },
    },
    # ---------------------------------------------------------------
    # 4.2 — Copilot in Teams Meetings Governance
    # ---------------------------------------------------------------
    "4.2": {
        "priority": "high",
        "yesBar": (
            "Copilot in Teams meetings is governed with documented policies "
            "covering meeting transcription, summarization, and note-taking. "
            "Meeting organizers control Copilot availability, and "
            "transcription retention aligns with the firm's record-keeping "
            "requirements."
        ),
        "partialBar": (
            "Copilot in meetings is enabled but governance policies are "
            "incomplete, meeting organizer controls are not documented, or "
            "transcription retention is at default settings."
        ),
        "noBar": (
            "No governance exists for Copilot in Teams meetings, or "
            "meetings are transcribed without documented retention policy."
        ),
        "verifyIn": [
            {
                "portal": "Teams admin center",
                "path": "Meetings > Meeting policies",
                "url": "https://admin.teams.microsoft.com/policies/meetings",
            },
        ],
        "verifyPowerShell": (
            "Connect-MicrosoftTeams; "
            "Get-CsTeamsMeetingPolicy | Select-Object Identity, "
            "AllowTranscription, AllowCloudRecording, CopilotWithTranscript"
        ),
        "evidenceExpected": [
            "Teams meeting policy configuration showing Copilot settings",
            "Meeting organizer control documentation",
            "Transcription retention policy aligned to regulatory requirements",
            "Governance policy document for Copilot in meetings",
        ],
        "collectorField": "Teams_MeetingPolicies",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "Meeting transcriptions retained per FINRA Rule 4511 and "
                "SEC Rule 17a-4 where applicable; supervisory review of "
                "client-facing meeting summaries per FINRA Rule 3110."
            ),
            bank=(
                "Meeting transcription retention aligned to SOX "
                "record-keeping; Copilot disabled for NPI-sensitive "
                "committee meetings unless approved."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Copilot in Teams meetings governed with documented "
                "policies covering transcription and retention?"
            ),
            "followUp": (
                "Open Teams admin center > Meeting policies. Verify "
                "Copilot settings, organizer controls, and transcription "
                "retention alignment."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 4.3 — Copilot in Teams Phone and Queues Governance
    # ---------------------------------------------------------------
    "4.3": {
        "priority": "high",
        "yesBar": (
            "Copilot in Teams Phone and call queues is governed with "
            "documented policies covering call summarization, voicemail "
            "transcription, and call-queue analytics. Call recording "
            "retention meets regulatory requirements."
        ),
        "partialBar": (
            "Copilot in Teams Phone is enabled but policies are incomplete "
            "or call-recording retention is at default settings."
        ),
        "noBar": (
            "No governance exists for Copilot in Teams Phone and queues."
        ),
        "verifyIn": [
            {
                "portal": "Teams admin center",
                "path": "Voice > Calling policies",
                "url": "https://admin.teams.microsoft.com/policies/callingpolicy",
            },
        ],
        "verifyPowerShell": (
            "Connect-MicrosoftTeams; "
            "Get-CsTeamsCallingPolicy | Select-Object Identity, "
            "AllowCallRecording"
        ),
        "evidenceExpected": [
            "Teams calling policy configuration for Copilot features",
            "Call-recording retention policy aligned to regulatory minimum",
            "Governance document covering call summarization and analytics",
            "Queue configuration with Copilot feature settings",
        ],
        "collectorField": "Teams_CallingPolicies",
        "sectorYesBar": _sector_map(
            broker_dealer=(
                "Call recordings retained per FINRA Rule 4511 and SEC "
                "Rule 17a-4 where applicable; call summaries reviewed by "
                "supervisory principal per FINRA Rule 3110."
            ),
            bank=(
                "Call recording retention aligned to GLBA §501(b) "
                "expectations; Copilot disabled for customer service lines "
                "unless approved."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Copilot in Teams Phone and queues governed with "
                "documented policies covering call recording and retention?"
            ),
            "followUp": (
                "Open Teams admin center > Calling policies. Verify "
                "Copilot settings and call-recording retention."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 4.4 — Copilot in Viva Suite Governance
    # ---------------------------------------------------------------
    "4.4": {
        "priority": "medium",
        "yesBar": (
            "Viva-suite Copilot integration (Insights, Engage, Topics) is "
            "reviewed on a documented governance cadence. Privacy controls "
            "for Viva Insights are configured, and Copilot features are "
            "scoped to approved user groups."
        ),
        "partialBar": (
            "Viva Copilot features are enabled but governance review "
            "cadence is not established or privacy controls are at "
            "tenant defaults."
        ),
        "noBar": (
            "No governance review exists for Copilot in the Viva suite."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Settings > Viva",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/Settings/L1/VivaInsights",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Viva Copilot governance policy document",
            "Privacy control configuration for Viva Insights",
            "Approved user group scoping for Copilot features",
            "Governance review cadence and most recent review date",
        ],
        "collectorField": "Viva_CopilotSettings",
        "sectorYesBar": _sector_map(
            bank=(
                "Viva Insights privacy controls aligned to GLBA §501(b); "
                "Copilot features reviewed quarterly."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Viva-suite Copilot integration reviewed on a documented "
                "governance cadence with privacy controls configured?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Viva. Verify privacy "
                "controls and Copilot feature scoping."
            ),
            "timeBudgetMinutes": 5,
        },
    },
    # ---------------------------------------------------------------
    # 4.5 — Copilot Usage Analytics and Adoption Reporting
    # ---------------------------------------------------------------
    "4.5": {
        "priority": "high",
        "yesBar": (
            "Copilot usage analytics are reported to leadership on a "
            "documented cadence. Anomalies (usage spikes, unusual patterns) "
            "are flagged and investigated. Reports include adoption metrics "
            "and ROI indicators."
        ),
        "partialBar": (
            "Usage analytics are available but not reported on a regular "
            "cadence, or anomaly detection is not configured."
        ),
        "noBar": (
            "No usage analytics or adoption reporting exists for Copilot."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Reports > Usage > Microsoft 365 Copilot",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/reportsUsage",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Copilot usage report from Microsoft 365 admin center",
            "Leadership reporting cadence and most recent report",
            "Anomaly detection configuration and recent alerts",
            "ROI/adoption metric dashboard or report",
        ],
        "collectorField": "M365Admin_UsageAnalytics",
        "sectorYesBar": _sector_map(
            bank=(
                "Usage analytics reported monthly to technology governance "
                "committee per SOX IT general control expectations."
            ),
            broker_dealer=(
                "Usage analytics reviewed monthly by supervisory principal; "
                "anomalies investigated per FINRA Rule 3110."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Copilot usage analytics reported to leadership on a "
                "documented cadence with anomalies flagged?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Reports > Usage. "
                "Verify reporting cadence and anomaly detection."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 4.6 — Viva Insights and Copilot Analytics Impact Measurement
    # ---------------------------------------------------------------
    "4.6": {
        "priority": "medium",
        "yesBar": (
            "Viva Insights Copilot impact reports are reviewed on a "
            "documented cadence. Caveats about statistical limitations "
            "and correlation-vs-causation are applied when reporting to "
            "leadership."
        ),
        "partialBar": (
            "Viva Insights reports are available but not reviewed regularly, "
            "or caveats about statistical limitations are not applied."
        ),
        "noBar": (
            "No Viva Insights Copilot impact measurement is in place."
        ),
        "verifyIn": [
            {
                "portal": "Viva Insights",
                "path": "Organization insights > Copilot dashboard",
                "url": "https://insights.viva.office.com",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Viva Insights Copilot impact report with caveats applied",
            "Review cadence documentation and most recent review date",
            "Statistical-limitation disclaimers in leadership reports",
        ],
        "collectorField": "Viva_CopilotImpact",
        "sectorYesBar": _sector_map(),
        "facilitatorNotes": {
            "ask": (
                "Are Viva Insights Copilot impact reports reviewed on a "
                "documented cadence with statistical caveats applied?"
            ),
            "followUp": (
                "Open Viva Insights > Copilot dashboard. Verify review "
                "cadence and caveats in leadership reports."
            ),
            "timeBudgetMinutes": 5,
        },
    },
    # ---------------------------------------------------------------
    # 4.7 — Copilot Feedback and Telemetry Data Governance
    # ---------------------------------------------------------------
    "4.7": {
        "priority": "medium",
        "yesBar": (
            "Copilot feedback (thumb ratings, user comments) and telemetry "
            "data are reviewed on a documented cadence and routed to "
            "product owners. Privacy controls ensure feedback data is "
            "handled per the organization's data governance policy."
        ),
        "partialBar": (
            "Feedback is collected but not reviewed regularly, or feedback "
            "routing to product owners is not established."
        ),
        "noBar": (
            "No feedback or telemetry review process exists for Copilot."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings > Feedback",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Feedback review cadence and routing documentation",
            "Privacy controls for feedback/telemetry data handling",
            "Product owner assignment for feedback triage",
            "Most recent feedback review summary",
        ],
        "collectorField": "M365Admin_FeedbackSettings",
        "sectorYesBar": _sector_map(
            bank=(
                "Feedback data governed per GLBA §501(b); reviewed monthly "
                "by product owner."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Copilot feedback and telemetry data reviewed on a "
                "documented cadence and routed to product owners?"
            ),
            "followUp": (
                "Verify feedback settings and review cadence. Check that "
                "privacy controls are applied to feedback data."
            ),
            "timeBudgetMinutes": 5,
        },
    },
    # ---------------------------------------------------------------
    # 4.8 — Cost Allocation and License Optimization
    # ---------------------------------------------------------------
    "4.8": {
        "priority": "medium",
        "yesBar": (
            "Copilot license cost allocation is reviewed on a documented "
            "cadence. Chargeback or showback is executed to business units, "
            "inactive licenses are reclaimed, and PAYG costs are tracked "
            "against budgets."
        ),
        "partialBar": (
            "Cost tracking exists but chargeback/showback is not implemented, "
            "or inactive licenses are not reclaimed regularly."
        ),
        "noBar": (
            "No cost allocation or license optimization process exists "
            "for Copilot."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Billing > Your products",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/subscriptions",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Cost allocation report by business unit / cost center",
            "License reclamation cadence and recent reclamation records",
            "PAYG cost tracking dashboard with budget alerts",
            "Chargeback/showback documentation",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "Cost allocation aligned to bank cost centers per OCC "
                "Heightened Standards (12 CFR part 30, appendix D) "
                "for technology governance."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Copilot license cost allocation reviewed with "
                "chargeback/showback and license reclamation?"
            ),
            "followUp": (
                "Request cost allocation reports. Verify license reclamation "
                "cadence and PAYG budget tracking."
            ),
            "timeBudgetMinutes": 5,
        },
    },
    # ---------------------------------------------------------------
    # 4.9 — Incident Reporting and Root Cause Analysis
    # ---------------------------------------------------------------
    "4.9": {
        "priority": "critical",
        "yesBar": (
            "A documented incident-response process covers Copilot-specific "
            "incidents (oversharing, hallucination, prompt injection, data "
            "leakage) with reporting paths, severity classification, and "
            "root-cause-analysis requirements."
        ),
        "partialBar": (
            "Incident response exists but does not specifically cover "
            "Copilot incident types, or RCA is not required for Copilot "
            "incidents."
        ),
        "noBar": (
            "No incident-response process covers Copilot-specific incidents."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Incident-response runbook covering Copilot-specific scenarios",
            "Severity classification scheme for Copilot incidents",
            "Reporting path documentation (internal + regulatory if required)",
            "Root-cause-analysis template and recent RCA examples",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "Incident response aligned to OCC Heightened Standards; "
                "regulatory reporting per GLBA §501(b) and NYDFS Part 500 "
                "breach notification requirements."
            ),
            broker_dealer=(
                "Incident reporting per FINRA Rule 4530; Copilot-specific "
                "incidents subject to supervisory escalation."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is there a documented incident-response process covering "
                "Copilot-specific incidents with RCA requirements?"
            ),
            "followUp": (
                "Request the incident-response runbook. Verify it covers "
                "oversharing, hallucination, and prompt injection scenarios."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 4.10 — Business Continuity and Disaster Recovery
    # ---------------------------------------------------------------
    "4.10": {
        "priority": "high",
        "yesBar": (
            "A business-continuity plan for Copilot-dependent workflows "
            "has been documented and tested within the last 12 months. "
            "Fallback procedures exist for Copilot service disruption."
        ),
        "partialBar": (
            "A BC/DR plan exists but does not specifically cover Copilot "
            "dependency, or testing has not been performed within 12 months."
        ),
        "noBar": (
            "No business-continuity plan covers Copilot-dependent workflows."
        ),
        "verifyIn": [],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "BC/DR plan covering Copilot-dependent workflows",
            "Fallback procedure documentation for Copilot outages",
            "Most recent BC/DR test results (within 12 months)",
            "Copilot dependency assessment for critical business processes",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "BC/DR plan aligned to OCC Heightened Standards and FFIEC "
                "Business Continuity Management handbook; tested annually."
            ),
            broker_dealer=(
                "BC/DR plan includes Copilot per FINRA Rule 4370 business "
                "continuity requirements."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Has a business-continuity plan for Copilot-dependent "
                "workflows been documented and tested within 12 months?"
            ),
            "followUp": (
                "Request the BC/DR plan and most recent test results. "
                "Verify fallback procedures for Copilot outages."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 4.11 — Microsoft Sentinel Integration for Copilot Events
    # ---------------------------------------------------------------
    "4.11": {
        "priority": "high",
        "yesBar": (
            "Microsoft Sentinel detection rules cover Copilot misuse "
            "scenarios (data exfiltration, anomalous usage, prompt "
            "injection attempts). Rules are tuned on a documented cadence "
            "and integrated with the SOC workflow."
        ),
        "partialBar": (
            "Sentinel is enabled but detection rules do not specifically "
            "cover Copilot scenarios, or rule tuning cadence is not "
            "documented."
        ),
        "noBar": (
            "No Sentinel detection rules cover Copilot events."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft Sentinel",
                "path": "Analytics > Active rules",
                "url": "https://portal.azure.com/#blade/Microsoft_Azure_Security_Insights/MainMenuBlade/Analytics",
            },
        ],
        "verifyPowerShell": (
            "Connect-AzAccount; "
            "Get-AzSentinelAlertRule -ResourceGroupName <rg> "
            "-WorkspaceName <ws> | Where-Object { "
            "$_.DisplayName -like '*Copilot*' }"
        ),
        "evidenceExpected": [
            "Sentinel analytic rules targeting Copilot scenarios",
            "Rule tuning cadence and most recent tuning date",
            "SOC integration documentation for Copilot alerts",
            "Recent alert log showing Copilot detection rule activity",
        ],
        "collectorField": "Sentinel_CopilotDetections",
        "sectorYesBar": _sector_map(
            bank=(
                "Sentinel rules cover Copilot data exfiltration and "
                "anomalous usage per FFIEC IT Handbook expectations; SOC "
                "review within 4-hour SLA."
            ),
            insurance_carrier=(
                "Sentinel rules cover Copilot PHI access anomalies per "
                "NYDFS Part 500 monitoring requirements."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Sentinel detection rules covering Copilot misuse "
                "reviewed and tuned on a documented cadence?"
            ),
            "followUp": (
                "Open Microsoft Sentinel > Analytics. Verify detection "
                "rules for Copilot and check tuning records."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 4.12 — Change Management for Copilot Feature Rollouts
    # ---------------------------------------------------------------
    "4.12": {
        "priority": "high",
        "yesBar": (
            "Copilot feature releases (Microsoft-managed and tenant-managed) "
            "are tracked via the M365 Message Center and risk-reviewed "
            "before user enablement. A change advisory process exists with "
            "documented approval records."
        ),
        "partialBar": (
            "Feature releases are tracked but risk review is ad hoc, or "
            "change advisory approval is not documented."
        ),
        "noBar": (
            "No change management process exists for Copilot feature "
            "rollouts."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Health > Message center",
                "url": "https://admin.microsoft.com/AdminPortal/Home#/MessageCenter",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Change advisory board records for Copilot feature rollouts",
            "M365 Message Center monitoring evidence",
            "Risk review documentation for recent feature changes",
            "Approval records for tenant-managed feature enablement",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "Change management aligned to SOX IT general control "
                "change advisory requirements; feature rollouts risk-reviewed "
                "before enablement."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are Copilot feature releases risk-reviewed and approved "
                "before user enablement?"
            ),
            "followUp": (
                "Request change advisory records. Verify M365 Message "
                "Center monitoring and risk review documentation."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 4.13 — Copilot Extensibility and Agent Operations
    # ---------------------------------------------------------------
    "4.13": {
        "priority": "high",
        "yesBar": (
            "Extensibility surfaces (declarative agents, MCP, plug-ins) "
            "are governed by an approval and inventory process. Operational "
            "monitoring covers agent health, usage patterns, and error rates."
        ),
        "partialBar": (
            "Extensibility governance exists but operational monitoring "
            "is incomplete or not documented."
        ),
        "noBar": (
            "No operational governance exists for Copilot extensibility "
            "surfaces."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Agents > All agents",
                "url": "https://admin.microsoft.com/Adminportal/Home#/agents",
            },
        ],
        "verifyPowerShell": (
            "Connect-MgGraph -Scopes Application.Read.All; "
            "Get-MgServicePrincipal -All | Where-Object { "
            "$_.Tags -contains 'CopilotAgent' -or "
            "$_.Tags -contains 'WindowsAzureActiveDirectoryIntegratedApp' } | "
            "Select-Object DisplayName, AppId, AccountEnabled"
        ),
        "evidenceExpected": [
            "Agent and plug-in inventory with operational status",
            "Approval workflow for new extensibility surface publication",
            "Operational monitoring dashboard for agent health and usage",
            "Error rate tracking and alerting configuration",
        ],
        "collectorField": "M365Admin_AgentOperations",
        "sectorYesBar": _sector_map(
            bank=(
                "Agent operations governance aligned to OCC Bulletin 2023-17 "
                "third-party risk requirements for AI agents."
            ),
            broker_dealer=(
                "Agent operations reviewed by supervisory principal per "
                "FINRA Rule 3110; error rates monitored for client-facing "
                "agents."
            ),
            investment_adviser=(
                "Agent operations monitoring covers advisory-function agents; "
                "usage patterns reviewed quarterly by CCO."
            ),
            insurance_carrier=(
                "Agent operations monitoring covers claims and underwriting "
                "agents; error rates tracked per NYDFS Part 500."
            ),
            credit_union=(
                "Agent operations governance per NCUA expectations; "
                "operational monitoring for member-facing agents."
            ),
            other=(
                "Agent operations monitored per organization's operational "
                "governance policy; health and error rates tracked."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Are extensibility surfaces governed by an approval and "
                "inventory process with operational monitoring?"
            ),
            "followUp": (
                "Open Microsoft 365 admin center > Agents. Verify inventory, "
                "approval workflow, and operational monitoring."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 4.14 — Copilot Studio Agent Lifecycle Governance
    # ---------------------------------------------------------------
    "4.14": {
        "priority": "high",
        "yesBar": (
            "The Copilot Studio agent lifecycle (authoring, testing, "
            "publishing, versioning, deprecation) is governed with documented "
            "evidence at each gate. Lifecycle stages are tracked in an "
            "inventory and retirement decisions are documented."
        ),
        "partialBar": (
            "Lifecycle governance exists but not all stages have documented "
            "evidence gates, or agent retirement is not tracked."
        ),
        "noBar": (
            "No lifecycle governance exists for Copilot Studio agents."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Agents > All agents",
                "url": "https://admin.microsoft.com/Adminportal/Home#/agents",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Agent lifecycle governance policy document",
            "Lifecycle gate evidence (testing, approval, publishing records)",
            "Agent inventory with lifecycle stage tracking",
            "Retirement/deprecation documentation for decommissioned agents",
        ],
        "collectorField": "M365Admin_AgentLifecycle",
        "sectorYesBar": _sector_map(
            bank=(
                "Lifecycle governance aligned to OCC Bulletin 2023-17 and "
                "OCC Heightened Standards (12 CFR part 30, appendix D) for "
                "technology lifecycle management."
            ),
            broker_dealer=(
                "Agent lifecycle includes supervisory approval gate per "
                "FINRA Rule 3110 before publication for registered-rep use."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is the Copilot Studio agent lifecycle governed with "
                "documented evidence at each stage gate?"
            ),
            "followUp": (
                "Request the lifecycle governance document. Verify evidence "
                "at each gate (testing, approval, publishing, deprecation)."
            ),
            "timeBudgetMinutes": 6,
        },
    },
    # ---------------------------------------------------------------
    # 4.15 — Copilot Cowork Governance
    # ---------------------------------------------------------------
    "4.15": {
        "priority": "high",
        "yesBar": (
            "Copilot Cowork governance reflects GA operating controls: usage-based "
            "billing scope is approved, discovery is set deliberately, model "
            "toggles (including Anthropic family and Claude Fable 5 preview) are "
            "documented, local browser use is governed as a preview sub-feature, "
            "consumption limits are monitored, plugin/skill inventories are "
            "approved, and Purview/audit coverage is evidenced."
        ),
        "partialBar": (
            "Cowork governance is partially implemented, but one or more required "
            "GA decisions (billing/discovery, model policy, browser toggle, "
            "consumption limits, plugin/skill approvals, or Purview coverage) "
            "is missing, outdated, or lacks approver evidence."
        ),
        "noBar": (
            "Cowork is effectively unmanaged: billing/discovery posture is not "
            "approved, model and browser settings are not governed, no verified "
            "plugin/skill inventory exists, and Purview/supervision evidence is absent."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Cost management",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings > AI experiences enabled by usage-based billing",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings > View all > Cowork settings",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
            {
                "portal": "Microsoft Purview portal",
                "path": "AI hub / Copilot security and compliance for Cowork",
                "url": "https://purview.microsoft.com/aihub",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Usage-based billing scope export (user/group assignments) with approver",
            "Discovery-setting decision record and access-request workflow evidence",
            "Model-policy record for Anthropic family and Claude Fable 5 (Preview)",
            "Cowork Browsing tenant-toggle decision tied to browser-control review",
            "Consumption-limit policy and recent spend/consumption report",
            "Approved plugin, uploaded package, and custom-skill inventory with owner",
            "Purview coverage evidence (audit/eDiscovery/DLP alignment) and gap log",
        ],
        "collectorField": "M365Admin_CoworkGovernance",
        "sectorYesBar": _sector_map(
            bank=(
                "Cowork enablement (billing scope, discovery, model/browser toggles) "
                "is treated as a formal change-control event aligned to FFIEC IT "
                "Examination Handbook expectations and OCC Heightened Standards "
                "(12 CFR part 30, appendix D)."
            ),
            broker_dealer=(
                "Cowork for registered reps is gated on FINRA Rule 3110 supervisory "
                "readiness, with documented review of agentic outputs that can "
                "contribute to client communications or records."
            ),
            investment_adviser=(
                "Cowork rollout is approved by compliance leadership where adviser "
                "workflows touch client communications, with usage and model "
                "decisions documented for SEC exam response."
            ),
            insurance_carrier=(
                "Cowork is limited to approved underwriting/claims populations "
                "after privacy and browser-use controls are reviewed for PHI/PII "
                "handling obligations."
            ),
            credit_union=(
                "Cowork scope is tied to member-data least-privilege posture; "
                "billing/discovery decisions and consumption controls are retained "
                "as NCUA examination evidence."
            ),
            other=(
                "Cowork governance decisions (access, models, browser use, plugins, "
                "consumption, and Purview coverage) are documented under the "
                "institution's AI governance standard."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Is Cowork operated under a documented GA governance posture "
                "(billing/discovery, models, browser use, consumption, plugins/skills, "
                "and Purview supervision) before expansion?"
            ),
            "followUp": (
                "Open Copilot cost-management and settings pages to confirm billing "
                "scope, discovery state, model/browser toggles, and consumption "
                "limits. Then verify plugin/skill approvals plus Purview/audit "
                "coverage evidence and unresolved gaps."
            ),
            "timeBudgetMinutes": 8,
        },
    },
    # ---------------------------------------------------------------
    # 4.16 — Microsoft Scout Governance
    # ---------------------------------------------------------------
    "4.16": {
        "priority": "high",
        "yesBar": (
            "Microsoft Scout is governed through all three required gates "
            "(Frontier scope, managed-endpoint policy with admin attestation, and "
            "GitHub Copilot Business/Enterprise entitlement), with managed endpoint "
            "posture validated, shell/browser/local-file permissions governed, "
            "autonomous/unattended modes explicitly controlled, MCP approvals "
            "documented, mixed M365/GitHub/local boundary risks acknowledged, and "
            "supervision evidence retained."
        ),
        "partialBar": (
            "Scout governance exists but one or more critical controls is missing "
            "or stale (gate reconciliation, endpoint policy evidence, permission "
            "defaults, MCP approval records, supervision cadence, or known-evidence "
            "limitations tracking)."
        ),
        "noBar": (
            "Scout is enabled or piloted without reconciled Frontier/Intune/GitHub "
            "gating, without documented permission boundaries, and without evidence "
            "of supervision or residual-risk acceptance for local and third-party "
            "processing surfaces."
        ),
        "verifyIn": [
            {
                "portal": "Microsoft 365 admin center",
                "path": "Copilot > Settings > Frontier",
                "url": "https://admin.microsoft.com/Adminportal/Home#/copilot",
            },
            {
                "portal": "Microsoft Intune admin center",
                "path": "Devices > Configuration > Policies (Scout Frontier profile / AllowScoutFrontierAccess)",
                "url": "https://intune.microsoft.com",
            },
            {
                "portal": "GitHub organization settings",
                "path": "Copilot > Access / seat assignments (Business or Enterprise)",
                "url": "https://github.com/organizations",
            },
        ],
        "verifyPowerShell": "",
        "evidenceExpected": [
            "Frontier enrollment and scoping record for tenant and pilot groups",
            "Intune policy export showing Scout enablement profile assignment and effective state",
            "Admin attestation record naming approver and completion date",
            "GitHub Copilot Business/Enterprise entitlement export matched to pilot users",
            "Documented default permission posture for local files, shell commands, and browser actions",
            "Autonomous-mode and unattended-automation decision records with scope constraints",
            "Approved MCP inventory including authentication, egress, and data-path classification",
            "Boundary map showing M365-protected data vs GitHub/local/third-party processing surfaces",
            "Known unsupported evidence register (local automation artifacts, local MCP output, third-party inference telemetry)",
        ],
        "collectorField": "",
        "sectorYesBar": _sector_map(
            bank=(
                "Scout pilot is approved as an endpoint and third-party-risk change "
                "event; Frontier/Intune/GitHub gates and residual-risk acceptance "
                "are documented for FFIEC and OCC Heightened Standards oversight."
            ),
            broker_dealer=(
                "Scout use by registered populations is gated on FINRA Rule 3110 "
                "supervisory procedures and explicit records-treatment decisions "
                "for artifacts potentially in scope under SEC Rule 17a-4."
            ),
            investment_adviser=(
                "Scout deployment for adviser workflows includes compliance approval, "
                "documented entitlement scope, and supervision over client-facing "
                "outputs produced through local file/shell/browser actions."
            ),
            insurance_carrier=(
                "Scout is limited to managed endpoints with documented PHI/PII "
                "handling boundaries, with endpoint-policy evidence and exception "
                "tracking retained for audit."
            ),
            credit_union=(
                "Scout enablement for member-data workflows is constrained to "
                "approved pilot users and managed devices, with gate reconciliation "
                "and boundary-risk evidence retained for NCUA examinations."
            ),
            other=(
                "TODO: define sector-specific regulated Scout threshold once "
                "Microsoft publishes GA-stable evidence and policy surfaces."
            ),
        ),
        "facilitatorNotes": {
            "ask": (
                "Can you show reconciled evidence that Scout is governed across "
                "Frontier scope, Intune policy + attestation, and GitHub Copilot "
                "entitlement, with explicit controls for permissions, autonomy, and MCP?"
            ),
            "followUp": (
                "Validate all three gates against the same pilot roster, then review "
                "permission defaults (local file/shell/browser), autonomous-mode "
                "posture, MCP approvals, and the known unsupported evidence register "
                "for local/third-party boundaries."
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
    '4.15': [],
    '4.16': [],
}


# Fold per-control solution arrays into the main AUTHORED dict.
# Overlay-with-replace semantics (see scripts/merge_authored_content.py
# `_REPLACE_FIELDS`) guarantees this list is authoritative.
for _cid, _sols in _SOLUTIONS_BY_CONTROL.items():
    AUTHORED.setdefault(_cid, {})["solutions"] = list(_sols)
