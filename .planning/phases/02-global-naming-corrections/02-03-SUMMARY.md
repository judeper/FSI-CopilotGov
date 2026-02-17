---
phase: 02-global-naming-corrections
plan: 03
subsystem: docs
tags: [naming, terminology, bizchat, microsoft-365-copilot-chat, glossary, framework, reference]

# Dependency graph
requires: []
provides:
  - "17 canonical docs files using correct Microsoft 365 Copilot Chat terminology"
  - "Glossary entry for Microsoft 365 Copilot Chat with current definition"
  - "Copilot surfaces catalog fully updated with correct naming"
  - "Zero instances of BizChat, M365 Chat, or Microsoft 365 Chat in framework/reference/root/getting-started files"
affects:
  - "02-global-naming-corrections"
  - "all subsequent phases that reference these canonical docs"

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Shortened form policy: full name on first mention per doc, 'Copilot Chat' in subsequent mentions and table cells, full name in all headings"
    - "Silent replacement: no 'formerly known as' notes, no inline parentheticals"

key-files:
  created: []
  modified:
    - "docs/framework/copilot-surfaces.md"
    - "docs/framework/copilot-architecture.md"
    - "docs/framework/governance-fundamentals.md"
    - "docs/framework/relationship-to-agentgov.md"
    - "docs/framework/adoption-roadmap.md"
    - "docs/reference/glossary.md"
    - "docs/reference/faq.md"
    - "docs/reference/copilot-admin-toggles.md"
    - "docs/reference/copilot-surfaces-matrix.md"
    - "docs/reference/license-requirements.md"
    - "docs/reference/fsi-configuration-examples.md"
    - "docs/reference/index.md"
    - "docs/index.md"
    - "README.md"
    - "docs/getting-started/checklist.md"
    - "docs/getting-started/quick-start.md"
    - "docs/playbooks/getting-started/phase-0-governance-setup.md"

key-decisions:
  - "All BizChat instances in these files describe the free/seeded chat experience, mapped to 'Microsoft 365 Copilot Chat'"
  - "Shortened form 'Copilot Chat' used in table cells and subsequent body text mentions after first full use per document"
  - "Full name 'Microsoft 365 Copilot Chat' used in all headings and first mentions"
  - "Glossary entry fully rewritten with free-experience definition and pointer to licensed Microsoft 365 Copilot"
  - "phase-0-governance-setup.md 'Business Chat (Microsoft 365 Chat / BizChat)' alias chain removed entirely"

patterns-established:
  - "Shortened form policy: 'Microsoft 365 Copilot Chat' on first mention, 'Copilot Chat' thereafter, full name in headings"

requirements-completed:
  - GLOB-01
  - GLOB-02

# Metrics
duration: 6min
completed: 2026-02-17
---

# Phase 2 Plan 03: Global Naming Corrections (Framework, Reference, Root) Summary

**Replaced all BizChat/M365 Chat instances with 'Microsoft 365 Copilot Chat' across 17 canonical framework, reference, getting-started, and root files — including a fully rewritten glossary entry and updated copilot surfaces catalog.**

## Performance

- **Duration:** 6 min
- **Started:** 2026-02-17T21:41:06Z
- **Completed:** 2026-02-17T21:47:12Z
- **Tasks:** 2
- **Files modified:** 17

## Accomplishments

- Eliminated every instance of deprecated names (BizChat, M365 Chat, Microsoft 365 Chat) from 17 canonical files
- Rewrote glossary entry from "BizChat (Microsoft 365 Chat)" heading with old definition to "Microsoft 365 Copilot Chat" heading with current free-experience definition and licensed-experience pointer
- Updated copilot-surfaces.md section heading, surface category table, body text, admonition title, risk tier table, and quick reference table (9 instances corrected)
- Removed parenthetical alias chain "Business Chat (Microsoft 365 Chat / BizChat)" from phase-0-governance-setup.md — silent replacement with clean terminology
- Applied shortened form policy consistently: full name on first mention per document, "Copilot Chat" in subsequent mentions and table cells, full name in all headings

## Task Commits

1. **Task 1: Replace BizChat/M365 Chat in framework and reference files** - `5493cd8` (fix)
2. **Task 2: Replace BizChat/M365 Chat in root, getting-started, and playbook files** - `5cb3170` (fix)

**Plan metadata:** (docs commit - see below)

## Files Created/Modified

- `docs/framework/copilot-surfaces.md` - 9 terminology instances corrected (category table, section heading, body text, admonition, risk tier table, quick reference table)
- `docs/framework/copilot-architecture.md` - RSS admonition text and Copilot Pages section corrected
- `docs/framework/governance-fundamentals.md` - What This Framework Covers scope list corrected
- `docs/framework/relationship-to-agentgov.md` - Comparison table, scope table, diagram, when-to-use table, migration section (5 instances)
- `docs/framework/adoption-roadmap.md` - Restricted SharePoint Search checklist item
- `docs/reference/glossary.md` - BizChat entry renamed and rewritten; Copilot Pages entry updated; RSS entry updated
- `docs/reference/faq.md` - Data storage table, retention table, FAQ answer (3 instances)
- `docs/reference/copilot-admin-toggles.md` - Web content toggle, Copilot Pages toggle, RSS setting (3 instances)
- `docs/reference/copilot-surfaces-matrix.md` - AI-Native surface row (BizChat -> Microsoft 365 Copilot Chat)
- `docs/reference/license-requirements.md` - RSS description
- `docs/reference/fsi-configuration-examples.md` - DLP policy heading
- `docs/reference/index.md` - Surface matrix description
- `docs/index.md` - AI-Native surface list
- `README.md` - Framework coverage description
- `docs/getting-started/checklist.md` - RSS control description
- `docs/getting-started/quick-start.md` - Oversharing assessment step
- `docs/playbooks/getting-started/phase-0-governance-setup.md` - Two instances: per-app toggles list and defer recommendation

## Decisions Made

- All BizChat references in these foundational files describe the free/seeded chat experience, so all map to "Microsoft 365 Copilot Chat" (not "Microsoft 365 Copilot" which is the licensed product)
- The glossary entry definition was rewritten to explicitly distinguish the free experience from the licensed "Microsoft 365 Copilot" product and include a cross-reference
- The shortened form "Copilot Chat" is used in table cells and body text after first full mention per document, per the established policy
- All headings use the full product name "Microsoft 365 Copilot Chat"

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- All 17 canonical files now use correct Microsoft 365 Copilot Chat terminology
- Glossary provides authoritative definition that all other docs can rely on
- Ready for any subsequent phases that reference these framework/reference/getting-started files
- Requirements GLOB-01 and GLOB-02 satisfied for these files (remaining files addressed by other plans in Phase 2)

## Self-Check

### Files Exist

- `docs/framework/copilot-surfaces.md` - FOUND (modified)
- `docs/framework/copilot-architecture.md` - FOUND (modified)
- `docs/framework/governance-fundamentals.md` - FOUND (modified)
- `docs/framework/relationship-to-agentgov.md` - FOUND (modified)
- `docs/framework/adoption-roadmap.md` - FOUND (modified)
- `docs/reference/glossary.md` - FOUND (modified)
- `docs/reference/faq.md` - FOUND (modified)
- `docs/reference/copilot-admin-toggles.md` - FOUND (modified)
- `docs/reference/copilot-surfaces-matrix.md` - FOUND (modified)
- `docs/reference/license-requirements.md` - FOUND (modified)
- `docs/reference/fsi-configuration-examples.md` - FOUND (modified)
- `docs/reference/index.md` - FOUND (modified)
- `docs/index.md` - FOUND (modified)
- `README.md` - FOUND (modified)
- `docs/getting-started/checklist.md` - FOUND (modified)
- `docs/getting-started/quick-start.md` - FOUND (modified)
- `docs/playbooks/getting-started/phase-0-governance-setup.md` - FOUND (modified)

### Commits Exist

- `5493cd8` - Task 1 commit: fix(naming): replace BizChat with Microsoft 365 Copilot Chat across framework and reference docs
- `5cb3170` - Task 2 commit: fix(naming): replace BizChat with Microsoft 365 Copilot Chat in root and getting-started files

### Verification Checks

- Zero deprecated terms (BizChat/M365 Chat/Microsoft 365 Chat) in all 17 files: PASS
- `### Microsoft 365 Copilot Chat` in glossary.md: PASS
- `### Microsoft 365 Copilot Chat` in copilot-surfaces.md: PASS
- 9 correct usages of Microsoft 365 Copilot Chat/Copilot Chat in copilot-surfaces.md: PASS

## Self-Check: PASSED

---
*Phase: 02-global-naming-corrections*
*Completed: 2026-02-17*
