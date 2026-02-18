---
phase: 04-pillar-compliance-operations
plan: 02
subsystem: compliance
tags: [ediscovery, communication-compliance, irm, insider-risk, purview, finra, sec, frcp]

# Dependency graph
requires:
  - phase: 03-pillar-readiness-security
    provides: IRM (Control 2.10) updated with Risky Agents and insider risk detection — CC-to-IRM integration documented here depends on that control being current
provides:
  - Control 3.3 updated with unified eDiscovery experience (May 2025 GA) and February 2026 UX simplification
  - Control 3.4 updated with expanded CC coverage scope and IRM integration pathway
  - 8 playbooks aligned to current portal paths and new capabilities
affects:
  - phase: 04-pillar-compliance-operations (plans 03+, any controls cross-referencing 3.3 or 3.4)

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Scope guardrail: expanded tool coverage noted for awareness only, configuration guidance stays within M365 Copilot scope"
    - "Cross-pillar governance loop: Pillar 3 CC feeds Pillar 2 IRM risk indicators"
    - "Unified experience as current state: present portal consolidation as current reality with brief historical migration note"

key-files:
  created: []
  modified:
    - docs/controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md
    - docs/controls/pillar-3-compliance/3.4-communication-compliance.md
    - docs/playbooks/control-implementations/3.3/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.3/powershell-setup.md
    - docs/playbooks/control-implementations/3.3/verification-testing.md
    - docs/playbooks/control-implementations/3.3/troubleshooting.md
    - docs/playbooks/control-implementations/3.4/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.4/powershell-setup.md
    - docs/playbooks/control-implementations/3.4/verification-testing.md
    - docs/playbooks/control-implementations/3.4/troubleshooting.md

key-decisions:
  - "Unified eDiscovery presented as current state: no 'new' framing — May 2025 GA is the current reality; February 2026 UX simplification documented with 'as of' language"
  - "Pre-migration case gap documented inline (not standalone section): fits within existing Control Description as a migration note, under 3 paragraphs"
  - "IRM integration tier structure: Baseline (no IRM), Recommended (high-risk policies), Regulated (all policies with automated escalation)"
  - "Scope guardrail for expanded CC surfaces: Security Copilot, Fabric Copilot, Copilot Studio mentioned in one sentence + table row with 'awareness only' notation; no configuration guidance"
  - "FRCP Rule 26(b)(1) proportionality standard cited in 3.3 as the relevant litigation discovery standard for expanded Copilot content scope"
  - "SEC Rule 17a-4(j) cited specifically for production of electronic records in response to SEC examination requests"
  - "FINRA Rule 3110(a) cited for 'reasonably designed' supervisory system standard — IRM integration satisfies this by automating escalation"

patterns-established:
  - "Cross-pillar link pattern: when Pillar 3 feeds Pillar 2, document the integration toggle path and add verification test confirming indicator flow"
  - "Scope guardrail pattern: one awareness sentence + table row notation; never provide configuration guidance for out-of-scope surfaces"

requirements-completed: [P3-03, P3-04]

# Metrics
duration: 8min
completed: 2026-02-17
---

# Phase 4 Plan 02: eDiscovery and Communication Compliance Updates Summary

**Unified eDiscovery experience (May 2025 GA) documented as current state for 3.3; IRM integration pathway added to 3.4 with FINRA 3110(a) framing and cross-pillar governance loop documentation**

## Performance

- **Duration:** 8 min
- **Started:** 2026-02-17T17:39:21Z
- **Completed:** 2026-02-17T17:47:Z
- **Tasks:** 2
- **Files modified:** 10

## Accomplishments

- Control 3.3 fully updated to reflect unified eDiscovery as current state: single portal path, capability tier table, February 2026 UX simplification (surface filters, inline content rendering), and pre-migration case gap note with specific remediation steps
- Control 3.4 updated with expanded CC coverage awareness (Security Copilot, Fabric Copilot, Copilot Studio) and complete IRM integration documentation: toggle path, tier recommendations, cross-pillar architecture diagram update, FINRA 3110(a) regulatory framing
- All 8 playbooks aligned: 3.3 playbooks use unified portal navigation and include pre-migration verification; 3.4 playbooks include IRM integration steps, PowerShell audit script, and IRM-specific test case and troubleshooting

## Task Commits

Each task was committed atomically:

1. **Task 1: Update control 3.3 with unified eDiscovery migration + playbook alignment** - `230faa7` (feat)
2. **Task 2: Update control 3.4 with expanded CC coverage and IRM integration + playbook alignment** - `7ad95a7` (feat)

**Plan metadata:** (docs commit — see below)

## Files Created/Modified

- `docs/controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md` — Unified eDiscovery as current state, Feb 2026 UX, capability tier table, FRCP 26(b)(1) and SEC 17a-4(j) citations, pre-migration note
- `docs/controls/pillar-3-compliance/3.4-communication-compliance.md` — Expanded CC coverage with scope guardrail, IRM integration section, FINRA 3110(a) citation, updated tier table, cross-pillar link to Control 2.10
- `docs/playbooks/control-implementations/3.3/portal-walkthrough.md` — Unified portal navigation, pre-migration verification step, Copilot surface filter step
- `docs/playbooks/control-implementations/3.3/powershell-setup.md` — Added Script 4 for pre-migration case audit, updated KQL to `kind:microsearch`
- `docs/playbooks/control-implementations/3.3/verification-testing.md` — Added Test 4 (pre-migration case verification), Test 1 updated for surface filter
- `docs/playbooks/control-implementations/3.3/troubleshooting.md` — Added Issue 2 (pre-migration missing Copilot locations), Issue 3 (surface filter license requirement), escalation row for pre-migration cases
- `docs/playbooks/control-implementations/3.4/portal-walkthrough.md` — Added Step 5 for IRM integration, updated FSI Recommendations table with IRM tiers
- `docs/playbooks/control-implementations/3.4/powershell-setup.md` — Added Script 4 for IRM integration health check via audit log
- `docs/playbooks/control-implementations/3.4/verification-testing.md` — Added Test 4 (IRM indicator confirmation after CC match)
- `docs/playbooks/control-implementations/3.4/troubleshooting.md` — Added Issue 3 (IRM indicators not showing with delay/licensing resolution), Issue 4 (expanded CC surfaces out of scope)

## Decisions Made

- Unified eDiscovery presented as current reality, not "migration to" — the May 2025 GA is the current state; pre-migration cases noted with inline guidance rather than a standalone section
- IRM integration tier structure chosen to match existing tier pattern: no IRM at Baseline (complexity threshold), high-risk policies at Recommended, all policies at Regulated with automated escalation
- Scope guardrail applied exactly as specified in CONTEXT.md: one awareness sentence + one table row; no configuration details for Security/Fabric/Studio surfaces
- FINRA Rule 3110(a) selected as the primary regulatory anchor for IRM integration because the "reasonably designed" standard directly maps to the automated escalation benefit

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Controls 3.3 and 3.4 are current with the unified eDiscovery platform and expanded CC capabilities
- Cross-pillar link from 3.4 to Control 2.10 (insider risk) documented and ready for Phase 4 plans covering Pillar 2/3 intersection
- Pre-migration case verification steps documented for firms with existing eDiscovery infrastructure

## Self-Check: PASSED

All 11 files verified present on disk. Both task commits (`230faa7`, `7ad95a7`) confirmed in git log. All success criteria verified:
- SC-1 (P3-03): "unified eDiscovery" and "February 2026" present in 3.3 control
- SC-2 (P3-04): expanded CC coverage with scope guardrail and IRM integration present in 3.4 control
- SC-3: Section-number citations verified (Rule 26(b)(1), 17a-4(j), 3110(a))
- SC-4: Zero deprecated terms (BizChat/M365 Chat) across all 10 modified files

---
*Phase: 04-pillar-compliance-operations*
*Completed: 2026-02-17*
