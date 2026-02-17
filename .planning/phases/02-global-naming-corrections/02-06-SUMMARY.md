---
phase: 02-global-naming-corrections
plan: 06
subsystem: documentation
tags: [naming, shortened-form-policy, copilot-chat, sc-3, gap-closure]

# Dependency graph
requires:
  - phase: 02-global-naming-corrections
    provides: 02-05 verification report identifying 13 SC-3 violations across 4 categories

provides:
  - SC-3 shortened-form policy fully satisfied across all 314 documentation files
  - Zero "formerly Business Chat" transition notes in any document
  - Zero headings using abbreviated "Copilot Chat" form
  - Full "Microsoft 365 Copilot Chat" name introduced before all shortened-form uses in every file
  - Phase 2 achieves 5/5 success criteria (SC-1 through SC-5 all verified)

affects:
  - 03-pillar-readiness-security
  - Phase 3 planning
  - All phases reading from docs/ pillar files

# Tech tracking
tech-stack:
  added: []
  patterns: []

key-files:
  created: []
  modified:
    - docs/playbooks/control-implementations/4.1/portal-walkthrough.md
    - docs/controls/pillar-3-compliance/3.2-data-retention-policies.md
    - docs/framework/adoption-roadmap.md
    - docs/getting-started/checklist.md
    - docs/getting-started/quick-start.md
    - docs/reference/license-requirements.md
    - docs/controls/pillar-4-operations/4.10-business-continuity.md
    - docs/controls/pillar-4-operations/4.12-change-management-rollouts.md
    - docs/playbooks/control-implementations/4.8/troubleshooting.md
    - docs/controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md
    - docs/controls/pillar-3-compliance/3.11-record-keeping.md
    - docs/controls/pillar-1-readiness/1.9-license-planning.md
    - docs/controls/pillar-2-security/2.2-sensitivity-labels-classification.md
    - docs/reference/copilot-admin-toggles.md

key-decisions:
  - "SC-3 gap closure: first bare 'Copilot Chat' occurrence in each file expanded to full 'Microsoft 365 Copilot Chat'; subsequent occurrences remain valid shortened forms"
  - "Heading policy enforced silently: 3.2 Step 1 heading expanded to full name without any transition note"
  - "'Formerly Business Chat' removed silently per Phase 2 silent-replacement policy"

patterns-established:
  - "Silent replacement: no 'formerly' or transition notes — docs read as if current names were always used"
  - "First-mention rule: first occurrence of product name in each document uses full 'Microsoft 365 Copilot Chat'"
  - "Heading rule: all headings at every level always use full product name, never shortened form"

requirements-completed: [GLOB-01, GLOB-02]

# Metrics
duration: 3min
completed: 2026-02-17
---

# Phase 2 Plan 06: SC-3 Gap Closure — Shortened-Form Policy Fixes Summary

**Removed 'formerly Business Chat' transition note, fixed one heading, and added full-name introductions across 13 files to achieve SC-3 compliance and complete Phase 2 with 5/5 success criteria**

## Performance

- **Duration:** 3 min
- **Started:** 2026-02-17T22:22:46Z
- **Completed:** 2026-02-17T22:25:59Z
- **Tasks:** 2
- **Files modified:** 14

## Accomplishments

- Removed forbidden "formerly Business Chat" parenthetical from portal-walkthrough.md (line 29) — highest-severity SC-3 violation eliminated
- Fixed 3.2-data-retention-policies.md heading to use full product name "Microsoft 365 Copilot Chat + Email" (line 106)
- Expanded first "Copilot Chat" occurrence to full name in 12 remaining files: 7 Category A files (never had full name), 5 Category B files (shortened form appeared before full name)
- Full verification suite: zero "formerly" notes, zero headings with shortened form, correct ordering in all 63 files containing "Copilot Chat", MkDocs build clean, no regressions in SC-1/SC-2/SC-4
- Phase 2 now achieves 5/5 success criteria — all GLOB-01 and GLOB-02 requirements fully satisfied

## Task Commits

Each task was committed atomically:

1. **Task 1: Fix highest-severity violation and heading violation** - `b04f39c` (fix)
2. **Task 2: Add full-name introductions and fix ordering in remaining 12 files** - `578646f` (fix)

**Plan metadata:** TBD (docs: complete plan)

## Files Created/Modified

- `docs/playbooks/control-implementations/4.1/portal-walkthrough.md` - Removed "formerly Business Chat" note; now introduces full name at first mention
- `docs/controls/pillar-3-compliance/3.2-data-retention-policies.md` - Step 1 heading now uses full "Microsoft 365 Copilot Chat + Email"
- `docs/framework/adoption-roadmap.md` - First "Copilot Chat" occurrence expanded to full name (line 149)
- `docs/getting-started/checklist.md` - First "Copilot Chat" occurrence expanded to full name (line 34)
- `docs/getting-started/quick-start.md` - First "Copilot Chat" occurrence expanded to full name (line 60)
- `docs/reference/license-requirements.md` - First "Copilot Chat" occurrence expanded to full name (line 30)
- `docs/controls/pillar-4-operations/4.10-business-continuity.md` - Table cell expanded to full name (line 73, only mention)
- `docs/controls/pillar-4-operations/4.12-change-management-rollouts.md` - Affected Surfaces column expanded to full name (line 174)
- `docs/playbooks/control-implementations/4.8/troubleshooting.md` - First "Copilot Chat" occurrence expanded to full name (line 34)
- `docs/controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md` - First bare occurrence expanded (line 17, was before full name at line 31)
- `docs/controls/pillar-3-compliance/3.11-record-keeping.md` - Table cell expanded (line 48, was before full name at line 116)
- `docs/controls/pillar-1-readiness/1.9-license-planning.md` - License table cell expanded (line 33, was before full name at line 103)
- `docs/controls/pillar-2-security/2.2-sensitivity-labels-classification.md` - Pages table cell expanded (line 68, was before full name at line 101)
- `docs/reference/copilot-admin-toggles.md` - Toggle name expanded (line 40: "Web content in Microsoft 365 Copilot Chat responses")

## Decisions Made

- Expanded only the FIRST bare "Copilot Chat" occurrence per file; all subsequent bare occurrences left as valid shortened forms
- copilot-admin-toggles.md: the toggle name "Web content in Copilot Chat responses" was the first bare occurrence (line 40); the impact column on the same line already contained "Microsoft 365 Copilot Chat" as a separate phrase — expanding the toggle name makes the full name first

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Phase 2 is complete with 5/5 success criteria verified
- All 314 documentation files now use correct Microsoft product terminology with proper shortened-form policy
- Ready to begin Phase 3: Pillar Updates — Readiness and Security
- Pre-existing MkDocs unrecognized links (quick-start.md playbook paths, 1.1 templates path) remain deferred to Phase 6 cross-linking

---
*Phase: 02-global-naming-corrections*
*Completed: 2026-02-17*
