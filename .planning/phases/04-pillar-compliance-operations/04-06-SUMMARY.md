---
phase: 04-pillar-compliance-operations
plan: 06
subsystem: compliance-documentation
tags: [viva-insights, viva-engage, copilot-chat-analytics, payg-billing, cost-governance, fsi, ffiec, sox, occ]

# Dependency graph
requires:
  - phase: 03-pillar-readiness-security
    provides: Updated Pillar 3 controls establishing baseline for Pillar 4 updates
provides:
  - Updated Control 4.4 with Viva Copilot Chat insights and Engage-to-Teams integration governance
  - Updated Control 4.8 with PAYG billing model, per-seat vs PAYG comparison, and governance controls
  - 4 updated playbooks for Control 4.4 (portal, powershell, verification, troubleshooting)
  - 4 updated playbooks for Control 4.8 (portal, powershell, verification, troubleshooting)
affects: [04-pillar-compliance-operations, verification-gate]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - PAYG governance pattern: budget cap + anomaly detection + approval workflow for variable AI spending
    - Engage-to-Teams compliance perimeter: dual-location policy coverage (Yammer + Teams) for content that crosses platforms
    - Copilot Chat analytics privacy pattern: aggregated-only, minimum group size applies, individual queries never exposed

key-files:
  created: []
  modified:
    - docs/controls/pillar-4-operations/4.4-viva-suite-governance.md
    - docs/controls/pillar-4-operations/4.8-cost-allocation.md
    - docs/playbooks/control-implementations/4.4/portal-walkthrough.md
    - docs/playbooks/control-implementations/4.4/powershell-setup.md
    - docs/playbooks/control-implementations/4.4/verification-testing.md
    - docs/playbooks/control-implementations/4.4/troubleshooting.md
    - docs/playbooks/control-implementations/4.8/portal-walkthrough.md
    - docs/playbooks/control-implementations/4.8/powershell-setup.md
    - docs/playbooks/control-implementations/4.8/verification-testing.md
    - docs/playbooks/control-implementations/4.8/troubleshooting.md

key-decisions:
  - "Copilot Chat analytics documented as aggregation-only: individual queries never visible to managers/admins, min group size (default 10, FSI recommended 25) applies equally to Copilot Chat data"
  - "FFIEC IT Examination Handbook Section II.C cited for Copilot Chat analytics: IT risk monitoring expectation directly fulfilled by usage pattern analytics"
  - "Engage-to-Teams integration documented as net positive for compliance: dual-location policy coverage (Yammer + Teams) extends compliance perimeter automatically"
  - "PAYG breakeven calculation explicitly documented: 3,000 messages/user/month at $0.01/message = $30/user/month per-seat cost"
  - "SOX 404 PAYG framing: variable PAYG costs require budget authorization controls as IT general controls; monthly reconciliation to Azure Commerce billing required"
  - "OCC Heightened Standards (12 CFR Part 30, Appendix D) cited for PAYG cost governance: budget caps and anomaly detection demonstrate responsive governance"
  - "FFIEC Management Booklet Section II.D cited for per-seat vs PAYG cost-benefit analysis documentation requirement"

patterns-established:
  - "PAYG governance pattern: budget cap configuration + 80%/100% alerts + department tagging + anomaly detection + approval workflow — complete 5-element governance framework"
  - "Dual-location compliance policy pattern: Engage-to-Teams integration requires both Yammer and Teams locations in CC and retention policies"
  - "Copilot Chat analytics privacy citation pattern: FFIEC IT Examination Handbook Section II.C as primary regulatory anchor for usage monitoring"

requirements-completed: [P4-03, P4-04]

# Metrics
duration: 12min
completed: 2026-02-18
---

# Phase 4 Plan 06: Viva Suite Governance and Cost Allocation Summary

**Control 4.4 updated with Viva Copilot Chat insights (aggregated analytics, FFIEC alignment) and Engage-to-Teams compliance perimeter; Control 4.8 updated with PAYG billing ($0.01/message), per-seat vs PAYG comparison table (3,000 msg/month breakeven), and full governance controls (budget caps, anomaly detection, SOX/OCC/FFIEC framing)**

## Performance

- **Duration:** 12 min
- **Started:** 2026-02-18T03:19:36Z
- **Completed:** 2026-02-18T03:31:44Z
- **Tasks:** 2
- **Files modified:** 10

## Accomplishments

- Control 4.4 documents expanded Viva Copilot Chat insights with full privacy controls (aggregation-only, min group size applies, FFIEC IT Examination Handbook Section II.C citation), Engage-to-Teams integration with dual-location compliance perimeter implications, and tier-consistent recommendations across all three tiers
- Control 4.8 documents the PAYG billing model ($0.01/message via Azure Commerce), per-seat vs PAYG comparison table with explicit 3,000 messages/month breakeven calculation, PAYG governance controls (budget caps, 80%/100% alerts, department tagging, anomaly detection, approval workflows), and FSI regulatory framing (SOX Section 404, OCC 12 CFR Part 30, FFIEC Section II.D)
- All 8 playbooks (4 per control) updated: portal walkthroughs add new configuration steps; PowerShell guides add 2 new scripts for 4.4 and 3 new scripts for 4.8; verification testing adds 2 new tests for 4.4 and 3 new tests for 4.8; troubleshooting adds 2 new issues for 4.4 and 3 new issues for 4.8

## Task Commits

Each task was committed atomically:

1. **Task 1: Update control 4.4 with Viva Copilot Chat insights and Engage integration + playbook alignment** - `b6974d8` (feat)
2. **Task 2: Update control 4.8 with PAYG billing model and governance controls + playbook alignment** - `10028ab` (feat)

**Plan metadata:** *(will be added in final commit)*

## Files Created/Modified

- `docs/controls/pillar-4-operations/4.4-viva-suite-governance.md` — Added Copilot Chat Insights section, Engage-to-Teams integration section, updated tier recommendations (3 new items), Surface Coverage table (2 new rows), Verification Criteria (2 new rows), FSI Considerations (FFIEC citation), Setup Step 1b and updated Step 2
- `docs/controls/pillar-4-operations/4.8-cost-allocation.md` — Added PAYG billing model section, per-seat vs PAYG comparison table, PAYG governance controls section, updated Why This Matters (PAYG regulatory framing), Governance Levels (PAYG items at all tiers), Setup Step 1b, Surface Coverage table (PAYG row), Verification Criteria (2 new rows), FSI Considerations (3 new PAYG-specific paragraphs)
- `docs/playbooks/control-implementations/4.4/portal-walkthrough.md` — Added Step 1 (Copilot Chat analytics configuration) and updated Step 2 (Engage-to-Teams compliance perimeter); updated FSI Recommendations table and Regulatory Alignment
- `docs/playbooks/control-implementations/4.4/powershell-setup.md` — Added Scripts 1-2 (Copilot Chat department analytics, privacy threshold validation), Script 4 (Engage-to-Teams retention check); updated Scheduled Tasks table
- `docs/playbooks/control-implementations/4.4/verification-testing.md` — Added Tests 1-2 (Copilot Chat insights availability, Engage-to-Teams retention coverage); updated Evidence Collection and Compliance Mapping
- `docs/playbooks/control-implementations/4.4/troubleshooting.md` — Added Issues 1-2 (Copilot Chat not populating, Engage content not captured); renumbered existing issues; updated Diagnostic Steps and Escalation table
- `docs/playbooks/control-implementations/4.8/portal-walkthrough.md` — Added Step 1b (Azure Commerce PAYG monitoring, budget cap configuration, tag setup); updated FSI Recommendations table and Regulatory Alignment with specific citations
- `docs/playbooks/control-implementations/4.8/powershell-setup.md` — Added Scripts 1-3 (PAYG monthly billing report, budget cap configuration, anomaly detection); renumbered existing scripts to 4-7; updated Scheduled Tasks table
- `docs/playbooks/control-implementations/4.8/verification-testing.md` — Added Tests 1-3 (PAYG billing accuracy, budget cap enforcement, cost allocation); renumbered existing tests to 4-7; updated Evidence Collection and Compliance Mapping with specific regulatory citations
- `docs/playbooks/control-implementations/4.8/troubleshooting.md` — Added Issues 1-3 (PAYG costs not appearing, budget cap not enforcing, tag propagation failures); renumbered existing issues to 4-7; updated Diagnostic Steps and Escalation table

## Decisions Made

- Copilot Chat analytics documented as aggregation-only with explicit privacy boundary: individual query content never accessible through Viva Insights — consistent with Viva Insights' existing privacy architecture
- FFIEC IT Examination Handbook Section II.C (management monitoring of technology usage patterns) identified as primary regulatory anchor for Copilot Chat analytics governance
- Engage-to-Teams integration framed as net positive for recordkeeping compliance: dual-location policy coverage extends compliance perimeter automatically without requiring additional manual processes
- PAYG breakeven calculation explicitly documented at 3,000 messages/user/month to enable institutions to make informed per-seat vs PAYG allocation decisions
- SOX Section 404 PAYG framing: variable PAYG costs require budget authorization controls as part of IT general controls; monthly reconciliation to Azure Commerce billing established as required procedure at Regulated tier
- OCC Heightened Standards (12 CFR Part 30, Appendix D) and FFIEC Management Booklet Section II.D cited with specific references following the Section number + context sentence pattern established in Phase 4 context decisions

## Deviations from Plan

None — plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- Controls 4.4 and 4.8 (P4-03, P4-04) complete with seamless integration
- Plan 06 is the final content plan for Phase 4; verification gate (if included in Phase 4) can now proceed
- All 10 files updated cleanly with no deprecated terms (BizChat/M365 Chat) introduced

## Self-Check: PASSED

- All 10 modified files confirmed present on disk
- Both task commits confirmed in git log: `b6974d8` (Task 1), `10028ab` (Task 2)
- SUMMARY.md created at `.planning/phases/04-pillar-compliance-operations/04-06-SUMMARY.md`

---
*Phase: 04-pillar-compliance-operations*
*Completed: 2026-02-18*
