---
phase: 03-pillar-readiness-security
plan: 02
subsystem: governance-documentation
tags: [sharepoint, purview, rbac, dspm-for-ai, sam, dag-reports, restricted-access-control, pnp-powershell, copilot-governance]

# Dependency graph
requires:
  - phase: 02-global-naming-corrections
    provides: Clean BizChat/M365 Chat terminology across all pillar docs — baseline for content updates

provides:
  - Control 1.6 updated with three new DSPM for AI RBAC roles (Purview Data Security AI Viewer, AI Content Viewer, AI Administrator)
  - Control 1.7 SAM licensing corrected (included with Copilot) with DAG reports expanded and RAC documented
  - 1.6 and 1.8 PowerShell playbooks updated with mandatory PnP custom app registration (PLAY-01)
  - All 1.6 playbooks aligned with new RBAC role assignment paths and verification steps
  - All 1.7 playbooks aligned with corrected licensing, DAG, and RAC configuration

affects:
  - 03-03-PLAN (Pillar 2 security controls — may reference SAM/DAG capabilities from 1.7)
  - phase-5 (GLOB-03 SAM licensing note in license-requirements.md — should be consistent with 1.7 correction)
  - phase-6 (cross-linking — 1.7 now references RAC alongside RCD; cross-links to 1.3 should note both)

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Factual error correction: fix root fact and rewrite all downstream logic that depended on it (not just the fact)"
    - "RBAC documentation: role + description + use case + assignment path + tier-gated recommendation"
    - "PnP PLAY-01 pattern: Prerequisites section with Register-PnPEntraIDAppForInteractiveLogin + -ClientId on all Connect-PnPOnline calls"

key-files:
  created: []
  modified:
    - docs/controls/pillar-1-readiness/1.6-permission-model-audit.md
    - docs/controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md
    - docs/playbooks/control-implementations/1.6/portal-walkthrough.md
    - docs/playbooks/control-implementations/1.6/powershell-setup.md
    - docs/playbooks/control-implementations/1.6/verification-testing.md
    - docs/playbooks/control-implementations/1.6/troubleshooting.md
    - docs/playbooks/control-implementations/1.7/portal-walkthrough.md
    - docs/playbooks/control-implementations/1.7/powershell-setup.md
    - docs/playbooks/control-implementations/1.7/verification-testing.md
    - docs/playbooks/control-implementations/1.7/troubleshooting.md
    - docs/playbooks/control-implementations/1.8/powershell-setup.md

key-decisions:
  - "Three new RBAC roles integrated as new subsection in 1.6 (not top-level section) — volume justified subsection per threshold rule (3+ paragraphs of distinct role content)"
  - "SAM licensing rewrite in 1.7: entire cost-benefit section and licensing nuance rewritten, not just table row — surrounding logic was built on the wrong fact"
  - "RAC documented as a SAM capability peer to RCD in 1.7, not subordinated — both are per-site controls with different enforcement mechanisms and use cases"
  - "1.7 'Cost-Benefit of SAM Licensing' consideration rewritten to 'SAM Licensing Clarification' — the old heading implied a budget decision that no longer applies for Copilot orgs"
  - "PnP fix applied to 1.8 powershell-setup.md even though 1.8 has no Phase 3 content requirement — PLAY-01 scope covers 1.8 regardless"

patterns-established:
  - "Factual correction pattern: locate all text that logically depends on the wrong fact, correct the root, rewrite dependents seamlessly"
  - "RBAC role documentation pattern: Role | Description | Use Case table, then assignment paths per portal, then tier recommendations integrated into Governance Levels table"
  - "PnP PLAY-01 pattern: Prerequisites section heading, one-time setup block with Register-PnPEntraIDAppForInteractiveLogin, save-the-Client-ID note, then all Connect-PnPOnline calls use -ClientId $clientId"

requirements-completed: [P1-04, P1-05]

# Metrics
duration: 9min
completed: 2026-02-18
---

# Phase 3 Plan 02: Control 1.6 RBAC Roles + Control 1.7 SAM Licensing Rewrite Summary

**DSPM for AI RBAC roles added to Control 1.6; SAM licensing corrected in Control 1.7 with Restricted Access Control and expanded DAG reports documented; PnP app registration applied to 1.6 and 1.8 PowerShell playbooks**

## Performance

- **Duration:** 9 min
- **Started:** 2026-02-18T00:52:01Z
- **Completed:** 2026-02-18T01:01:00Z
- **Tasks:** 2
- **Files modified:** 11

## Accomplishments

- Control 1.6 now documents all three DSPM for AI RBAC roles (Purview Data Security AI Viewer, Purview Data Security AI Content Viewer, AI Administrator) with descriptions, use cases, tier-gated recommendations, and assignment paths in both Purview portal and Entra admin center
- Control 1.7 SAM licensing table corrected: Microsoft 365 Copilot row now shows "Yes" with "included at no additional cost (Ignite 2024)"; all downstream logic that assumed SAM was a separate purchase has been rewritten including the former "Cost-Benefit of SAM Licensing" section
- Control 1.7 expanded with Restricted Access Control (RAC) as a new SAM capability and site permissions snapshot report added to DAG report types, with FSI regulatory framing per GLBA 501(b) and SEC Regulation S-P
- 1.6 and 1.8 PowerShell playbooks updated with PnP custom Entra app registration prerequisite (PLAY-01) — all Connect-PnPOnline calls now include -ClientId

## Task Commits

Each task was committed atomically:

1. **Task 1: Update control 1.6 with new RBAC roles and PnP fixes for 1.6 and 1.8 playbooks** - `7aeef96` (feat)
2. **Task 2: Rewrite control 1.7 SAM licensing and add DAG/RAC with playbook alignment** - `5d56e5b` (feat)

**Plan metadata:** (docs commit — see state updates)

## Files Created/Modified

- `docs/controls/pillar-1-readiness/1.6-permission-model-audit.md` — Added DSPM for AI RBAC roles subsection with role table, assignment paths, tier recommendations; updated governance levels; added Step 6 for role assignment; updated verification criteria
- `docs/controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md` — Corrected SAM licensing table and rewrote downstream cost logic; added site permissions snapshot to DAG table; added Restricted Access Control (RAC) subsection; updated objective, governance levels, setup steps, FSI considerations, and verification criteria
- `docs/playbooks/control-implementations/1.6/portal-walkthrough.md` — Added Step 5 for assigning DSPM roles via Purview portal and Entra admin center; updated tier recommendations
- `docs/playbooks/control-implementations/1.6/powershell-setup.md` — Added PnP custom app registration prerequisite block; updated Connect-PnPOnline in Script 3 to use -ClientId
- `docs/playbooks/control-implementations/1.6/verification-testing.md` — Added Test 5 for DSPM role assignment verification; added FFIEC compliance mapping row
- `docs/playbooks/control-implementations/1.6/troubleshooting.md` — Added Issue 6 (PnP connection failures post-retirement) and Issue 7 (DSPM role visibility); added AI Content Viewer escalation path
- `docs/playbooks/control-implementations/1.7/portal-walkthrough.md` — Rewrote Step 1 for SAM licensing clarification; added Steps 4 (RCD config) and 5 (RAC config) with detailed instructions; updated tier recommendations
- `docs/playbooks/control-implementations/1.7/powershell-setup.md` — Added Script 4 for bulk RAC configuration using Set-SPOSite -RestrictedAccessControl; updated Script 3 to capture RCD status; added quarterly RAC review to scheduled tasks
- `docs/playbooks/control-implementations/1.7/verification-testing.md` — Added Tests 4 (RCD enforcement) and 5 (RAC enforcement); added site permissions snapshot to evidence collection; updated compliance mapping with GLBA, SEC Regulation S-P, and SOX rows
- `docs/playbooks/control-implementations/1.7/troubleshooting.md` — Updated Issue 1 with SAM licensing clarification for Copilot orgs; added Issues 6 (RAC not blocking users) and 7 (RAC breaking legitimate access)
- `docs/playbooks/control-implementations/1.8/powershell-setup.md` — Added PnP custom app registration prerequisite block; updated Connect-PnPOnline in Script 3 to use -ClientId

## Decisions Made

- Three new RBAC roles integrated as a new `###` subsection within Control 1.6 (not a top-level section) — the volume of distinct role content (3 roles with descriptions, use cases, two separate portal assignment paths, and tier recommendations) crossed the subsection threshold
- SAM licensing rewrite in 1.7 treated as a full downstream logic correction: the "Cost-Benefit of SAM Licensing" framing in the Financial Sector Considerations section was rewritten to "SAM Licensing Clarification" since the budget decision no longer applies for Copilot-licensed organizations
- RAC documented as a peer to RCD (not subordinated) with its own subsection, configuration path, and separate tier recommendations — RAC and RCD serve different purposes (access boundary enforcement vs. Copilot discovery exclusion) and FSI institutions may need both

## Deviations from Plan

None - plan executed exactly as written. All 11 files in the plan were updated. The plan's correction pattern for 1.7 (rewrite surrounding logic, not just the fact) was followed completely.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- P1-04 and P1-05 complete — Control 1.6 and 1.7 are fully updated
- PLAY-01 applied to 1.6 and 1.8 PowerShell playbooks (1.2 and 2.2 playbooks remain in their respective plans)
- PLAY-03 applied to all modified portal-walkthrough playbooks
- Ready for 03-03 and remaining phase plans

---
*Phase: 03-pillar-readiness-security*
*Completed: 2026-02-18*
