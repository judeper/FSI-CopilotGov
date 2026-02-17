---
phase: 02-global-naming-corrections
plan: 01
subsystem: docs
tags: [naming, bizchat, copilot-chat, microsoft-365, pillar-1, pillar-2, terminology]

# Dependency graph
requires: []
provides:
  - 13 Pillar 1 control files with zero deprecated product names
  - 15 Pillar 2 control files with zero deprecated product names
  - Correct dual-name mapping applied: "Microsoft 365 Copilot Chat" (free/seeded) throughout Pillars 1-2
  - Shortened form policy established: full name on first mention and in headings, "Copilot Chat" subsequently
affects:
  - 03-pillar-content-updates
  - 04-compliance-playbooks
  - 05-framework-alignment
  - 06-cross-linking-final-review

# Tech tracking
tech-stack:
  added: []
  patterns: []

key-files:
  created: []
  modified:
    - docs/controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md
    - docs/controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md
    - docs/controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md
    - docs/controls/pillar-1-readiness/1.4-semantic-index-governance.md
    - docs/controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md
    - docs/controls/pillar-1-readiness/1.6-permission-model-audit.md
    - docs/controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md
    - docs/controls/pillar-1-readiness/1.8-information-architecture-review.md
    - docs/controls/pillar-1-readiness/1.9-license-planning.md
    - docs/controls/pillar-1-readiness/1.10-vendor-risk-management.md
    - docs/controls/pillar-1-readiness/1.11-change-management-adoption.md
    - docs/controls/pillar-1-readiness/1.12-training-awareness.md
    - docs/controls/pillar-1-readiness/1.13-extensibility-readiness.md
    - docs/controls/pillar-2-security/2.1-dlp-policies-for-copilot.md
    - docs/controls/pillar-2-security/2.2-sensitivity-labels-classification.md
    - docs/controls/pillar-2-security/2.3-conditional-access-policies.md
    - docs/controls/pillar-2-security/2.4-information-barriers.md
    - docs/controls/pillar-2-security/2.5-data-minimization-grounding-scope.md
    - docs/controls/pillar-2-security/2.6-web-search-controls.md
    - docs/controls/pillar-2-security/2.7-data-residency.md
    - docs/controls/pillar-2-security/2.8-encryption.md
    - docs/controls/pillar-2-security/2.9-defender-cloud-apps.md
    - docs/controls/pillar-2-security/2.10-insider-risk-detection.md
    - docs/controls/pillar-2-security/2.11-copilot-pages-security.md
    - docs/controls/pillar-2-security/2.12-external-sharing-governance.md
    - docs/controls/pillar-2-security/2.13-plugin-connector-security.md
    - docs/controls/pillar-2-security/2.14-declarative-agents-governance.md
    - docs/controls/pillar-2-security/2.15-network-security.md

key-decisions:
  - "All BizChat instances in Pillars 1-2 map to free/seeded experience — replaced with Microsoft 365 Copilot Chat (not the licensed Microsoft 365 Copilot)"
  - "Shortened form Copilot Chat used for all subsequent mentions within a document; full name required in headings and first mention"
  - "Silent replacement applied — no transition notes, parentheticals, or formerly-known-as language added"
  - "Compound phrases updated naturally (e.g., BizChat Query -> Copilot Chat Query, BizChat Search -> Copilot Chat Search)"

patterns-established:
  - "Naming pattern: Microsoft 365 Copilot Chat (first mention / headings) -> Copilot Chat (subsequent)"
  - "Table entries use full name Microsoft 365 Copilot Chat as the Copilot Surface row header"
  - "Inline body text and step instructions use shortened Copilot Chat after first full mention"

requirements-completed: [GLOB-01, GLOB-02]

# Metrics
duration: 4min
completed: 2026-02-17
---

# Phase 2 Plan 01: Global Naming Corrections (Pillars 1-2) Summary

**Zero deprecated product names across 28 control files — all BizChat/M365 Chat instances replaced with Microsoft 365 Copilot Chat using full-name/shortened-form policy**

## Performance

- **Duration:** 4 min
- **Started:** 2026-02-17T21:41:05Z
- **Completed:** 2026-02-17T21:45:19Z
- **Tasks:** 2 of 2
- **Files modified:** 28

## Accomplishments

- Eliminated all 16 instances of "BizChat (M365 Chat)" and related deprecated names across 13 Pillar 1 control files
- Eliminated all 28+ instances of "BizChat", "M365 Chat" patterns across 15 Pillar 2 control files (including 9 instances in the high-complexity 2.4-information-barriers.md)
- Applied consistent naming pattern: full product name "Microsoft 365 Copilot Chat" on first mention and in all headings; "Copilot Chat" shortened form for subsequent references in body text and table cells

## Task Commits

Each task was committed atomically:

1. **Task 1: Replace BizChat/M365 Chat in all 13 Pillar 1 control files** - `801d711` (fix)
2. **Task 2: Replace BizChat/M365 Chat in all 15 Pillar 2 control files** - `6744c7d` (fix)

**Plan metadata:** *(docs commit follows)*

## Files Created/Modified

### Pillar 1 - Readiness (13 files modified)
- `docs/controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md` - Table: BizChat -> Microsoft 365 Copilot Chat
- `docs/controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md` - Table: BizChat -> Microsoft 365 Copilot Chat
- `docs/controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md` - Table + inline: BizChat -> Copilot Chat
- `docs/controls/pillar-1-readiness/1.4-semantic-index-governance.md` - Table: BizChat -> Microsoft 365 Copilot Chat
- `docs/controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md` - Table + inline DLP text (2 instances)
- `docs/controls/pillar-1-readiness/1.6-permission-model-audit.md` - Table: BizChat -> Microsoft 365 Copilot Chat
- `docs/controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md` - Table + inline: BizChat -> Copilot Chat
- `docs/controls/pillar-1-readiness/1.8-information-architecture-review.md` - Table: BizChat -> Microsoft 365 Copilot Chat
- `docs/controls/pillar-1-readiness/1.9-license-planning.md` - License table (3 instances): BizChat -> Copilot Chat/Microsoft 365 Copilot Chat
- `docs/controls/pillar-1-readiness/1.10-vendor-risk-management.md` - Table: BizChat -> Microsoft 365 Copilot Chat
- `docs/controls/pillar-1-readiness/1.11-change-management-adoption.md` - Table + inline: BizChat -> Copilot Chat
- `docs/controls/pillar-1-readiness/1.12-training-awareness.md` - Table: BizChat -> Microsoft 365 Copilot Chat
- `docs/controls/pillar-1-readiness/1.13-extensibility-readiness.md` - Table: BizChat -> Microsoft 365 Copilot Chat

### Pillar 2 - Security (15 files modified)
- `docs/controls/pillar-2-security/2.1-dlp-policies-for-copilot.md` - Table + body text (2 instances)
- `docs/controls/pillar-2-security/2.2-sensitivity-labels-classification.md` - Table + Pages row (2 instances)
- `docs/controls/pillar-2-security/2.3-conditional-access-policies.md` - Table entry
- `docs/controls/pillar-2-security/2.4-information-barriers.md` - Heading, body text, code block, table, governance levels, verification steps (9 instances)
- `docs/controls/pillar-2-security/2.5-data-minimization-grounding-scope.md` - Table + verification steps (3 instances)
- `docs/controls/pillar-2-security/2.6-web-search-controls.md` - Table entry
- `docs/controls/pillar-2-security/2.7-data-residency.md` - Table entry
- `docs/controls/pillar-2-security/2.8-encryption.md` - Table entry
- `docs/controls/pillar-2-security/2.9-defender-cloud-apps.md` - Table entry
- `docs/controls/pillar-2-security/2.10-insider-risk-detection.md` - Table entry
- `docs/controls/pillar-2-security/2.11-copilot-pages-security.md` - Table + aggregation risk paragraph (2 instances)
- `docs/controls/pillar-2-security/2.12-external-sharing-governance.md` - Table + inline (2 instances)
- `docs/controls/pillar-2-security/2.13-plugin-connector-security.md` - Table entry
- `docs/controls/pillar-2-security/2.14-declarative-agents-governance.md` - Table + inline (2 instances)
- `docs/controls/pillar-2-security/2.15-network-security.md` - Table entry

## Decisions Made

- All BizChat instances in Pillars 1 and 2 refer to the free/seeded Copilot chat experience (cross-workload search, web-grounded), not the licensed per-user Microsoft 365 Copilot. This was confirmed by context in each file — these controls discuss the chat surface that is accessible to any M365 user, not the licensed Copilot assistant in productivity apps.
- 1.9-license-planning.md: The BizChat capability listed under the "Microsoft 365 Copilot" license row was renamed to "Copilot Chat" (the chat surface included in the licensed product), consistent with Microsoft's own SKU naming.
- Compound phrases updated naturally: "BizChat Query" -> "Copilot Chat Query", "BizChat Search" -> "Copilot Chat Search", "BizChat session" -> "Copilot Chat session", without restructuring sentences.

## Deviations from Plan

None - plan executed exactly as written. All expected occurrence counts matched; the dual-name mapping was straightforward (all instances in these 28 files refer to the free/seeded experience).

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Pillars 1 and 2 (28 files) now have a clean naming baseline
- Subsequent phases can confidently reference "Microsoft 365 Copilot Chat" without encountering legacy BizChat terminology in these foundational controls
- Pillars 3 and 4 naming corrections (Plans 02-04 in this phase) will complete the remaining control files

## Self-Check: PASSED

- SUMMARY.md: FOUND at .planning/phases/02-global-naming-corrections/02-01-SUMMARY.md
- Task 1 commit 801d711: FOUND
- Task 2 commit 6744c7d: FOUND
- Zero deprecated names remaining in Pillars 1 and 2: PASSED (0 matches)
- Correct replacements confirmed: 33 instances of "Microsoft 365 Copilot Chat" in 28 files

---
*Phase: 02-global-naming-corrections*
*Completed: 2026-02-17*
