---
phase: 04-pillar-compliance-operations
plan: 04
subsystem: compliance-documentation
tags: [model-risk-management, reg-sp, recordkeeping, occ-bulletin-2025-26, sec-17a-4, worm, audit-trail-alternative, off-channel-enforcement, mobile-copilot]

# Dependency graph
requires:
  - phase: 03-pillar-readiness-security
    provides: Pillar 2 and Pillar 3 baseline controls reviewed and terminology corrected
  - phase: 04-pillar-compliance-operations (plans 01-03)
    provides: Controls 3.1-3.6 updated with Phase 4 regulatory developments

provides:
  - Control 3.8 with OCC Bulletin 2025-26 MRM proportionality and Copilot SR 11-7 tier classification framework
  - Control 3.10 with Reg S-P 2023 amendment details (72-hour vendor notification, mandatory IRP, compliance dates)
  - Control 3.11 with 17a-4(f)(2)(ii)(A) audit-trail alternative, $2B+ off-channel enforcement context, and mobile recordkeeping — unified narrative
  - 12 aligned playbooks (4 per control) covering portal, PowerShell, verification, and troubleshooting

affects:
  - 04-07 (Phase 4 verification gate) — all three controls must be verified per SC-2 citation specificity check
  - Pillar 3 examination packages — enhanced regulatory citations and proportionality documentation

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "OCC Bulletin 2025-26 proportionality three-path model inventory registration (Tier 1/2/3) with community bank documentation path"
    - "Reg S-P 72-hour vendor notification tracking via PowerShell incident timer script"
    - "SEC Rule 17a-4(f)(2)(ii)(A) audit-trail alternative via Purview regulatory record labels + Preservation Lock"
    - "Unified narrative threading for 3.11 — three regulatory topics woven together, not separate subsections"
    - "Mobile Copilot recordkeeping: managed device coverage confirmed; Conditional Access cross-reference to Control 2.3"

key-files:
  created: []
  modified:
    - docs/controls/pillar-3-compliance/3.8-model-risk-management.md
    - docs/controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md
    - docs/controls/pillar-3-compliance/3.11-record-keeping.md
    - docs/playbooks/control-implementations/3.8/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.8/powershell-setup.md
    - docs/playbooks/control-implementations/3.8/verification-testing.md
    - docs/playbooks/control-implementations/3.8/troubleshooting.md
    - docs/playbooks/control-implementations/3.10/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.10/powershell-setup.md
    - docs/playbooks/control-implementations/3.10/verification-testing.md
    - docs/playbooks/control-implementations/3.10/troubleshooting.md
    - docs/playbooks/control-implementations/3.11/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.11/powershell-setup.md
    - docs/playbooks/control-implementations/3.11/verification-testing.md
    - docs/playbooks/control-implementations/3.11/troubleshooting.md

key-decisions:
  - "OCC Bulletin 2025-26 proportionality applies to all bank sizes, not only community banks — proportionality determination is documented based on actual usage scope and risk profile"
  - "Copilot SR 11-7 model status resolved as gray zone — consensus posture is to include in model inventory at appropriate tier rather than argue exemption"
  - "Three-tier classification (Tier 1/2/3) codified in model inventory entry with required proportionality rationale for Tier 3"
  - "Reg S-P 72-hour vendor notification (Rule 248.30(a)(3)) triggers notification to Microsoft MSRC — notification precedes investigation completion"
  - "SEC Rule 17a-4(f)(2)(ii)(A) audit-trail alternative offered as Option A alongside Option B (third-party WORM) — compliance counsel review required before relying on Option A"
  - "Unified narrative threading in 3.11 per locked Phase 4 decision — 17a-4 audit-trail alternative, off-channel enforcement ($2B+), and mobile recordkeeping woven into single cohesive narrative"
  - "Mobile Copilot cross-reference: Conditional Access device compliance requirement documented in 3.11, detailed configuration deferred to Control 2.3"

patterns-established:
  - "Three-path model inventory registration pattern: Path A (community bank proportionality, Tier 3), Path B (Tier 2), Path C (Tier 1 regulated)"
  - "Incident response timer script pattern: capture detection timestamp, calculate all notification deadlines, export incident record"
  - "Audit-trail alternative verification pattern: check Preservation Lock status + audit log event coverage per record retention period"
  - "Mobile coverage dual-test pattern: Test managed device (expected capture) + Test unmanaged device (expected block)"

requirements-completed: [P3-07, P3-08, P3-09]

# Metrics
duration: 18min
completed: 2026-02-18
---

# Phase 4 Plan 04: Compliance Controls 3.8, 3.10, 3.11 Summary

**OCC Bulletin 2025-26 MRM proportionality, Reg S-P 72-hour vendor notification requirement, and SEC 17a-4(f)(2)(ii)(A) audit-trail alternative documented across controls 3.8, 3.10, and 3.11 with unified off-channel/mobile narrative in 3.11**

## Performance

- **Duration:** 18 min
- **Started:** 2026-02-18T03:19:35Z
- **Completed:** 2026-02-18T03:37:51Z
- **Tasks:** 2
- **Files modified:** 15

## Accomplishments

- Control 3.8 now documents OCC Bulletin 2025-26 proportionality with a three-tier classification framework (Tier 1/2/3) and clarifies Copilot's SR 11-7 model status as a gray zone resolved by pragmatic inventory inclusion
- Control 3.10 now documents the Reg S-P 2023 amendment details: 72-hour vendor notification (Rule 248.30(a)(3)), mandatory written incident response program (Rule 248.30(a)(4)), and staggered compliance dates (June 2025 large entities, December 2025 small entities)
- Control 3.11 now contains a unified narrative threading the SEC 17a-4(f)(2)(ii)(A) audit-trail alternative, $2B+ off-channel enforcement context, and mobile Copilot recordkeeping into a cohesive modernization discussion per the Phase 4 locked decision on narrative threading

## Task Commits

Each task was committed atomically:

1. **Task 1: Update controls 3.8 and 3.10 with OCC MRM proportionality and Reg S-P amendments** - `e834fcb` (feat — content was previously committed as part of plan 04-01 execution; no additional commit required)
2. **Task 2: Update control 3.11 with 17a-4 audit-trail alternative, off-channel enforcement, and mobile recordkeeping** - `b700c8f` (feat)

**Plan metadata:** (docs commit — created below)

## Files Created/Modified

- `docs/controls/pillar-3-compliance/3.8-model-risk-management.md` — OCC Bulletin 2025-26 proportionality, three-tier SR 11-7 classification, updated governance tiers
- `docs/controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md` — Reg S-P 2023 amendments: 72-hour notification (Rule 248.30(a)(3)), mandatory IRP (Rule 248.30(a)(4)), June/December 2025 dates
- `docs/controls/pillar-3-compliance/3.11-record-keeping.md` — Unified narrative: 17a-4(f)(2)(ii)(A) audit-trail alternative, $2B+ off-channel enforcement, mobile Copilot recordkeeping with Conditional Access cross-reference
- `docs/playbooks/control-implementations/3.8/portal-walkthrough.md` — Three-path model inventory registration with community bank proportionality path
- `docs/playbooks/control-implementations/3.8/verification-testing.md` — Test 2: proportionality classification verification
- `docs/playbooks/control-implementations/3.8/troubleshooting.md` — Issues 4-6: tier classification debate, mid-size proportionality, SR 11-7 model status dispute
- `docs/playbooks/control-implementations/3.10/portal-walkthrough.md` — Steps 5-6: IRP configuration and 72-hour Microsoft notification workflow
- `docs/playbooks/control-implementations/3.10/powershell-setup.md` — Script 5: incident response timer tracking 72-hour and 30-day notification windows
- `docs/playbooks/control-implementations/3.10/verification-testing.md` — Tests 4-5: written IRP verification, NPI simulation with 72-hour window test
- `docs/playbooks/control-implementations/3.10/troubleshooting.md` — Issues 5-7: 72-hour calculation, Microsoft MSRC notification procedure, written IRP requirement
- `docs/playbooks/control-implementations/3.11/portal-walkthrough.md` — Steps 4A (audit-trail alternative config) and 6 (mobile access controls)
- `docs/playbooks/control-implementations/3.11/powershell-setup.md` — Scripts 4-5: Preservation Lock verification, audit trail coverage check
- `docs/playbooks/control-implementations/3.11/verification-testing.md` — Tests 3-6: Preservation Lock, audit-trail alternative compliance, mobile managed/unmanaged verification
- `docs/playbooks/control-implementations/3.11/troubleshooting.md` — Issues 5-7: mobile unmanaged access, off-channel scope, audit log retention for audit-trail alternative

## Decisions Made

- OCC Bulletin 2025-26 proportionality principle confirmed as applying to all institution sizes (not only community banks) — tier selection follows actual usage scope and risk profile, not just asset size; key is documented rationale
- Copilot SR 11-7 "gray zone" resolution: industry consensus posture is model inventory inclusion at appropriate tier rather than arguing exemption; 2023 Interagency AI Guidance cited as support
- For Reg S-P 72-hour notification: Microsoft notification channel is MSRC (msrc.microsoft.com) for security incidents; notification must precede completed investigation per rule timing
- SEC 17a-4(f)(2)(ii)(A) audit-trail alternative offered as legitimate compliance path alongside Option B (WORM); compliance counsel review required before relying on Option A; audit log retention period must match record retention period
- Unified narrative threading in 3.11 confirmed as the correct approach — three related topics woven together in the "Why This Matters" section rather than separate sub-sections (per Phase 4 locked decision)

## Deviations from Plan

### Task 1 Execution Context

**Context:** When Task 1 execution began, the 3.8 and 3.10 control documents and their 8 playbooks already contained the full updated content required by this plan. These files were committed as part of plan 04-01's execution (commit `e834fcb`), which bundled multiple control files in a single commit. The content matched all Task 1 verification criteria (OCC Bulletin 2025-26, proportionality language, SR 11-7, 72-hour, 248.30, incident response program, June/December 2025 dates). No changes were required for Task 1 files beyond what was already committed.

This is not a deviation from the plan's content requirements — all required content was present and correct. The deviation was in the commit structure: the atomic per-task commit for Task 1 was effectively the prior `e834fcb` commit rather than a new commit created during this execution.

**No content was omitted. All Task 1 success criteria verified as met.**

**Total deviations:** None from plan content. One execution context difference (Task 1 content pre-committed).

## Issues Encountered

- Task 1 files were found to already contain all required content at HEAD, committed as part of plan 04-01 execution. New Write operations produced content identical to what was committed. The verification checks confirmed all Task 1 requirements were met. Task 2 proceeded normally and was committed as `b700c8f`.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Controls 3.8, 3.10, 3.11 are ready for the Phase 4 verification gate (plan 04-07)
- All three controls use specific section number citations as required by Phase 4 citation style decision
- 3.11 unified narrative threading satisfies the Phase 4 locked decision on multi-regulation controls
- Mobile Copilot Conditional Access cross-reference to Control 2.3 is documented but detailed policy configuration remains in the Pillar 2 control

---
*Phase: 04-pillar-compliance-operations*
*Completed: 2026-02-18*
