---
phase: 02-global-naming-corrections
plan: 02
subsystem: docs
tags: [naming, bizchat, microsoft-365-copilot-chat, pillar-3-compliance, pillar-4-operations, terminology]

# Dependency graph
requires:
  - phase: 02-global-naming-corrections
    provides: naming correction context and dual-name mapping decisions from 02-CONTEXT.md
provides:
  - 13 Pillar 3 compliance control files with zero deprecated product name instances
  - 4 Pillar 4 operations control files with zero deprecated product name instances
  - Correct use of "Microsoft 365 Copilot Chat" (free/seeded experience) replacing BizChat, M365 Chat, Microsoft 365 Chat
affects: [03-pillar-content, 04-playbooks, 05-framework, 06-cross-linking]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "All headings use full product name: Microsoft 365 Copilot Chat"
    - "First body mention uses full name; subsequent mentions use 'Copilot Chat' shortened form"
    - "Table column headers with bold use full product name; table cell text may use shortened form"
    - "Parenthetical qualifiers like 'BizChat (M365 Chat)' collapsed to single correct name"

key-files:
  created: []
  modified:
    - docs/controls/pillar-3-compliance/3.1-copilot-audit-logging.md
    - docs/controls/pillar-3-compliance/3.2-data-retention-policies.md
    - docs/controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md
    - docs/controls/pillar-3-compliance/3.4-communication-compliance.md
    - docs/controls/pillar-3-compliance/3.5-finra-2210-compliance.md
    - docs/controls/pillar-3-compliance/3.6-supervision-oversight.md
    - docs/controls/pillar-3-compliance/3.7-regulatory-reporting.md
    - docs/controls/pillar-3-compliance/3.8-model-risk-management.md
    - docs/controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md
    - docs/controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md
    - docs/controls/pillar-3-compliance/3.11-record-keeping.md
    - docs/controls/pillar-3-compliance/3.12-evidence-collection.md
    - docs/controls/pillar-3-compliance/3.13-ffiec-alignment.md
    - docs/controls/pillar-4-operations/4.1-admin-settings-feature-management.md
    - docs/controls/pillar-4-operations/4.5-usage-analytics.md
    - docs/controls/pillar-4-operations/4.10-business-continuity.md
    - docs/controls/pillar-4-operations/4.12-change-management-rollouts.md

key-decisions:
  - "All BizChat instances in Pillar 3 and 4 files map to 'Microsoft 365 Copilot Chat' (free/seeded experience) -- none were the licensed Microsoft 365 Copilot product"
  - "Shortened form 'Copilot Chat' used for subsequent body text references after first full-name mention per file"
  - "Table row headers with bold (e.g., | **Microsoft 365 Copilot Chat** |) always use full name regardless of position"
  - "Silent replacement applied -- no 'formerly known as' annotations added"

patterns-established:
  - "Naming-correct: BizChat -> Microsoft 365 Copilot Chat (first mention), Copilot Chat (subsequent)"
  - "Table-headings: Always full product name in bold table row headers"
  - "Shortened-form: 'Copilot Chat' acceptable in body text, table cells, verification steps after first full mention per file"

requirements-completed: [GLOB-01, GLOB-02]

# Metrics
duration: 6min
completed: 2026-02-17
---

# Phase 02 Plan 02: Global Naming Corrections -- Pillars 3 and 4 Summary

**Replaced all 38 BizChat/M365 Chat/Microsoft 365 Chat instances across 17 Pillar 3 and Pillar 4 control files with "Microsoft 365 Copilot Chat", applying correct shortened-form policy and heading rules throughout regulatory-facing compliance documentation.**

## Performance

- **Duration:** 6 min
- **Started:** 2026-02-17T21:41:15Z
- **Completed:** 2026-02-17T21:47:26Z
- **Tasks:** 2
- **Files modified:** 17

## Accomplishments

- Eliminated all 33 instances of deprecated names in 13 Pillar 3 compliance controls (audit logging, retention, eDiscovery, communication compliance, FINRA 2210, supervision, regulatory reporting, model risk, AI disclosure, Reg S-P, record keeping, evidence collection, FFIEC alignment)
- Eliminated all 5 instances of deprecated names in 4 Pillar 4 operations controls (admin settings, usage analytics, business continuity, change management)
- Applied dual-name categorization: all instances in these files correctly map to "Microsoft 365 Copilot Chat" (free/seeded experience, stored in Exchange mailbox hidden folder)
- Applied shortened-form policy consistently: first mention per file uses full name, subsequent mentions use "Copilot Chat", headings always use full name

## Task Commits

Each task was committed atomically:

1. **Task 1: Replace BizChat/M365 Chat in all 13 Pillar 3 control files** - `ec7d304` (fix)
2. **Task 2: Replace BizChat/M365 Chat in 4 affected Pillar 4 control files** - `287903c` (fix)

**Plan metadata:** (docs commit, see below)

## Files Created/Modified

- `docs/controls/pillar-3-compliance/3.1-copilot-audit-logging.md` - 2 replacements (AppAccessContext table, surface coverage table)
- `docs/controls/pillar-3-compliance/3.2-data-retention-policies.md` - 7 replacements (retention matrix, content locations, surface coverage, governance, setup step 1 heading and description, verification step 2)
- `docs/controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md` - 8 replacements (intro paragraph, content locations table, eDiscovery comparison table, KQL section heading and description, surface coverage, governance, setup step 3, verification step 1)
- `docs/controls/pillar-3-compliance/3.4-communication-compliance.md` - 1 replacement (surface coverage table)
- `docs/controls/pillar-3-compliance/3.5-finra-2210-compliance.md` - 1 replacement (surface coverage table, also updated inline description)
- `docs/controls/pillar-3-compliance/3.6-supervision-oversight.md` - 1 replacement (surface coverage table, also updated sampling reference)
- `docs/controls/pillar-3-compliance/3.7-regulatory-reporting.md` - 2 replacements (surface coverage table row and description)
- `docs/controls/pillar-3-compliance/3.8-model-risk-management.md` - 1 replacement (surface coverage table)
- `docs/controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md` - 1 replacement (surface coverage table)
- `docs/controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md` - 3 replacements (surface coverage table, recommended governance, setup step 1)
- `docs/controls/pillar-3-compliance/3.11-record-keeping.md` - 5 replacements (17a-4 retention table, surface coverage table, setup step 3 table, WORM third-party section, examination findings list)
- `docs/controls/pillar-3-compliance/3.12-evidence-collection.md` - 1 replacement (surface coverage table)
- `docs/controls/pillar-3-compliance/3.13-ffiec-alignment.md` - 1 replacement (surface coverage table)
- `docs/controls/pillar-4-operations/4.1-admin-settings-feature-management.md` - 2 replacements (per-app toggles table, surface coverage table)
- `docs/controls/pillar-4-operations/4.5-usage-analytics.md` - 1 replacement (usage reports table)
- `docs/controls/pillar-4-operations/4.10-business-continuity.md` - 1 replacement (fallback procedures table)
- `docs/controls/pillar-4-operations/4.12-change-management-rollouts.md` - 1 replacement (change register field example)

## Decisions Made

- All BizChat instances in these files describe the free/seeded Copilot chat experience (stored in Exchange mailbox hidden folder, web-grounded), confirming "Microsoft 365 Copilot Chat" as the correct replacement throughout -- none of the 38 instances referred to the licensed Microsoft 365 Copilot product.
- Shortened form "Copilot Chat" used in body text, table cells, and verification steps after first full-name mention per file; heading rows in surface coverage tables always retain full name.

## Deviations from Plan

None - plan executed exactly as written. All replacement counts matched plan's expected occurrence estimates.

## Issues Encountered

None. The grep verification commands confirmed zero remaining instances of deprecated terms after both tasks.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Pillars 3 and 4 are fully corrected for BizChat/M365 Chat terminology
- Pillar 1 (readiness) and Pillar 2 (security) naming corrections handled in plans 02-01 and 02-03/04/05 respectively
- All 17 files in this plan are ready for content review and auditor-facing use with correct terminology

## Self-Check: PASSED

- All 17 modified files confirmed present on disk
- Task 1 commit ec7d304 verified in git log
- Task 2 commit 287903c verified in git log
- Zero deprecated terms confirmed in final grep verification

---
*Phase: 02-global-naming-corrections*
*Completed: 2026-02-17*
