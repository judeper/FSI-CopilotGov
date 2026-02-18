---
phase: 04-pillar-compliance-operations
plan: 01
subsystem: compliance
tags: [purview, audit-logging, data-retention, copilot, agentic-ai, finra, sec]

# Dependency graph
requires:
  - phase: 03-pillar-readiness-security
    provides: Phase 3 pillar controls updated and verified clean

provides:
  - Control 3.1 updated with expanded CopilotInteraction audit schema (AgentId, AgentName, XPIA, JailbreakDetected, SensitivityLabelId)
  - Agent-specific RecordTypes documented (AgentAdminActivity, AgentSettingsAdminActivity) with FSI regulatory mapping
  - Pay-as-you-go audit billing model documented with governance controls and E5/PAYG tier table
  - Control 3.2 updated with restructured Purview retention locations (Microsoft Copilot experiences, Enterprise AI Apps, Other AI Apps)
  - Priority cleanup guidance with Baseline/Recommended/Regulated tier tiers per SEC 17a-3(a)(17)
  - Threaded summaries retention documented with FINRA 4511(c) citation
  - All 8 playbooks aligned with new audit capabilities and retention structure

affects:
  - 04-02-PLAN.md (3.3 eDiscovery will reference the retention location structure established here)
  - 04-03-PLAN.md through 04-xx (downstream controls referencing audit schema or retention locations)
  - Phase 5 (license requirements touched by PAYG billing model)

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "AgentAdminActivity and AgentSettingsAdminActivity RecordTypes used for agent change management audit trail"
    - "PAYG audit billing governance: budget caps + spend alerts + per-workload cost tracking"
    - "Threaded summary independence: retention covers both source content location and Microsoft Copilot experiences independently"
    - "Structured retention location: Microsoft Copilot experiences is the primary M365 Copilot retention target"

key-files:
  created: []
  modified:
    - docs/controls/pillar-3-compliance/3.1-copilot-audit-logging.md
    - docs/controls/pillar-3-compliance/3.2-data-retention-policies.md
    - docs/playbooks/control-implementations/3.1/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.1/powershell-setup.md
    - docs/playbooks/control-implementations/3.1/verification-testing.md
    - docs/playbooks/control-implementations/3.1/troubleshooting.md
    - docs/playbooks/control-implementations/3.2/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.2/powershell-setup.md
    - docs/playbooks/control-implementations/3.2/verification-testing.md
    - docs/playbooks/control-implementations/3.2/troubleshooting.md

key-decisions:
  - "AgentId and AgentName fields mapped to FINRA Rule 3110 supervisory documentation — agent identity is the supervisory mapping anchor for agentic AI governance"
  - "XPIA field framed around multi-agent orchestration chain telemetry requirement from FINRA 2026 agentic supervision expectations"
  - "JailbreakDetected events require immediate security escalation per OCC heightened standards and FFIEC incident response — documented as separate troubleshooting issue with false positive guidance"
  - "PAYG audit billing positioned at Regulated tier as E5 Audit Premium alternative — not standalone recommendation, requires governance controls (budget caps, alerting, per-workload tracking)"
  - "SEC Rule 17a-4(a) six-year retention is the primary PAYG billing driver — makes six years the minimum for Regulated tier"
  - "Microsoft Copilot experiences is the primary retention location for M365 Copilot deployments — Enterprise AI Apps and Other AI Apps noted for awareness only with explicit scope guardrail"
  - "Threaded summaries retained independently — source content deletion does not cascade to Copilot summary; both locations must be covered separately by retention policies and eDiscovery holds"
  - "Priority cleanup scoped conservatively — Regulated tier uses retain-all posture per SEC 17a-3(a)(17) broad communications coverage"

patterns-established:
  - "Scope guardrail pattern: Enterprise AI Apps / Other AI Apps mentioned for awareness, then redirect to Microsoft Copilot experiences as M365 Copilot target"
  - "Tier table pattern: explicit Baseline/Recommended/Regulated tier for each new capability introduced"
  - "Agent record type pattern: AgentAdminActivity = change management (SOX 404), AgentSettingsAdminActivity = supervisory documentation (FINRA 3110(b))"

requirements-completed: [P3-01, P3-02]

# Metrics
duration: 9min
completed: 2026-02-18
---

# Phase 4 Plan 01: Audit Logging and Data Retention Controls Summary

**Control 3.1 expanded to cover agentic AI audit schema (5 new fields, 2 new RecordTypes, PAYG billing); Control 3.2 restructured to reflect Purview's new retention location categories with threaded summary independence and priority cleanup guidance**

## Performance

- **Duration:** 9 min
- **Started:** 2026-02-18T03:19:19Z
- **Completed:** 2026-02-18T03:28:XX Z
- **Tasks:** 2 of 2
- **Files modified:** 10

## Accomplishments

- Control 3.1 now documents the complete expanded CopilotInteraction audit schema with all 5 new agentic AI fields and regulatory mapping for each, plus two new RecordTypes (AgentAdminActivity, AgentSettingsAdminActivity) with SOX 404 and FINRA 3110(b) context
- Control 3.1 includes the pay-as-you-go audit billing model positioned as a cost-effective alternative to E5 Audit Premium for six-year retention (SEC Rule 17a-4(a)), with required governance controls
- Control 3.2 documents the restructured Purview retention location categories with the Microsoft Copilot experiences location as the M365 Copilot primary target and explicit scope guardrails for Enterprise AI Apps and Other AI Apps
- Control 3.2 addresses priority cleanup for AI-generated drafts with a Baseline/Recommended/Regulated tier table and conservative Regulated posture citing SEC Rule 17a-3(a)(17)
- Control 3.2 documents threaded summary independence with FINRA Rule 4511(c) citation and the implication that both source content and summary locations must be covered
- All 8 playbooks aligned: portal navigation updated, PowerShell scripts added for new capabilities, verification tests added for new features, troubleshooting guides cover new failure modes

## Task Commits

Each task was committed atomically:

1. **Task 1: Update control 3.1 with expanded audit schema and PAYG billing** - `24e28b8` (feat)
2. **Task 2: Update control 3.2 with restructured retention locations** - `e834fcb` (feat)

## Files Created/Modified

- `docs/controls/pillar-3-compliance/3.1-copilot-audit-logging.md` — Added 5 new schema fields, 2 new RecordTypes, PAYG billing section with tier table
- `docs/controls/pillar-3-compliance/3.2-data-retention-policies.md` — Added restructured retention locations table, priority cleanup tiers, threaded summaries section
- `docs/playbooks/control-implementations/3.1/portal-walkthrough.md` — Added agent record type navigation, new schema field review steps, JailbreakDetected alert
- `docs/playbooks/control-implementations/3.1/powershell-setup.md` — Added Scripts 3-8 (AgentAdminActivity, filter by AgentId, JailbreakDetected scan, PAYG monitoring)
- `docs/playbooks/control-implementations/3.1/verification-testing.md` — Added Tests 5-8 (agent capture, JailbreakDetected, PAYG billing, AgentAdmin retention)
- `docs/playbooks/control-implementations/3.1/troubleshooting.md` — Added Issues 5-7 (agent event latency, PAYG cost spike, false positives)
- `docs/playbooks/control-implementations/3.2/portal-walkthrough.md` — Rewritten to lead with Microsoft Copilot experiences location, added priority cleanup and threaded summary steps
- `docs/playbooks/control-implementations/3.2/powershell-setup.md` — Added Scripts 1 (Copilot experiences policy), 5 (threaded summary coverage), 6 (distribution status)
- `docs/playbooks/control-implementations/3.2/verification-testing.md` — Added Tests 5-7 (threaded summaries, new location categories, priority cleanup scope)
- `docs/playbooks/control-implementations/3.2/troubleshooting.md` — Added Issues 2-4 (experiences location unavailable, post-restructuring policy gaps, threaded summary independence)

## Decisions Made

- **AgentId/FINRA 3110 mapping:** AgentId is the supervisory anchor for agentic AI — maps agent invocations to approved use cases per FINRA Rule 3110 supervisory procedures
- **XPIA framing:** Cross-plugin inter-agent interaction framed around multi-agent orchestration chain telemetry, anticipated by FINRA 2026 agentic supervision expectations
- **PAYG billing governance:** Three required controls documented (budget caps, spend threshold alerting, per-workload cost tracking) — positioned as governance overhead that makes E5 Audit Premium more attractive for high-volume tenants
- **Microsoft Copilot experiences scope guardrail:** Enterprise AI Apps and Other AI Apps always noted then redirected — this is the standard Phase 4 scope pattern per 04-CONTEXT.md decisions
- **Priority cleanup conservative posture:** Regulated tier retains all Copilot-generated content regardless of draft status — conservative interpretation of SEC Rule 17a-3(a)(17) "all communications relating to the member's business"
- **Threaded summary independence documented as expected behavior:** Issue 4 in 3.2 troubleshooting explicitly frames this as design, not error — aligns with FINRA 4511(c) preservation requirements

## Deviations from Plan

None — plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- Controls 3.1 and 3.2 updated and verified clean — ready for downstream Phase 4 plans that reference audit schema or retention locations
- eDiscovery playbooks (Control 3.3, upcoming 04-02 plan) should reference the Microsoft Copilot experiences location as the primary Copilot content discovery target
- The threaded summary independence principle should be carried forward into eDiscovery hold configuration guidance

## Self-Check: PASSED

All files verified present. Both task commits verified in git log.

| Check | Result |
|-------|--------|
| 3.1-copilot-audit-logging.md | FOUND |
| 3.2-data-retention-policies.md | FOUND |
| 3.1/portal-walkthrough.md | FOUND |
| 3.1/powershell-setup.md | FOUND |
| 3.1/verification-testing.md | FOUND |
| 3.1/troubleshooting.md | FOUND |
| 3.2/portal-walkthrough.md | FOUND |
| 3.2/powershell-setup.md | FOUND |
| 3.2/verification-testing.md | FOUND |
| 3.2/troubleshooting.md | FOUND |
| 04-01-SUMMARY.md | FOUND |
| Commit 24e28b8 (Task 1) | FOUND |
| Commit e834fcb (Task 2) | FOUND |

---
*Phase: 04-pillar-compliance-operations*
*Completed: 2026-02-18*
