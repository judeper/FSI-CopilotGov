---
phase: 03-pillar-readiness-security
plan: 01
subsystem: content
tags: [sharepoint, dspm, copilot, governance, pnp-powershell, rcd, rss, optimization-assessment]

requires:
  - phase: 02-global-naming-corrections
    provides: Clean terminology baseline (BizChat replaced, portal names corrected) across all Pillar 1-2 control docs

provides:
  - Updated control 1.1 with Optimization Assessment as pre-deployment step and Office update channel governance
  - Updated control 1.2 with unified DSPM experience (AI observability, item-level remediation, Purview Posture Agent, Shadow AI discovery)
  - Updated control 1.3 with RCD vs RSS comparison table and SAM licensing note
  - Updated 1.2 PowerShell playbook with PnP custom Entra app registration (PLAY-01 partial)
  - Updated all 12 playbooks for controls 1.1, 1.2, 1.3 with current portal paths and new capabilities

affects:
  - 03-02 through 03-06 (remaining Phase 3 plans touching Pillar 1 and Pillar 2 controls)
  - Phase 6 PLAY-04 cross-linking (Related Controls sections reference 1.2, 1.3 relationship)

tech-stack:
  added: []
  patterns:
    - Dual portal path documentation — full Purview path + MAC quick access path for DSPM controls
    - PnP PowerShell prerequisite block (Register-PnPEntraIDAppForInteractiveLogin) in all affected PowerShell playbooks
    - RCD+RSS complementary tool documentation pattern — comparison table + simultaneous use guidance

key-files:
  created: []
  modified:
    - docs/controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md
    - docs/controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md
    - docs/controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md
    - docs/playbooks/control-implementations/1.1/portal-walkthrough.md
    - docs/playbooks/control-implementations/1.1/powershell-setup.md
    - docs/playbooks/control-implementations/1.1/verification-testing.md
    - docs/playbooks/control-implementations/1.1/troubleshooting.md
    - docs/playbooks/control-implementations/1.2/portal-walkthrough.md
    - docs/playbooks/control-implementations/1.2/powershell-setup.md
    - docs/playbooks/control-implementations/1.2/verification-testing.md
    - docs/playbooks/control-implementations/1.2/troubleshooting.md
    - docs/playbooks/control-implementations/1.3/portal-walkthrough.md
    - docs/playbooks/control-implementations/1.3/powershell-setup.md
    - docs/playbooks/control-implementations/1.3/verification-testing.md
    - docs/playbooks/control-implementations/1.3/troubleshooting.md

key-decisions:
  - "1.2 DSPM description rewritten for unified experience (Dec 2025 preview) — not classic DSPM for AI; dual portal paths documented (Purview + MAC > Copilot > Overview > Security tab)"
  - "RCD documented as Baseline-tier starting point for 1.3, with RSS+RCD combination at Regulated tier — complementary, not competing tools"
  - "SAM licensing note in 1.3: included with M365 Copilot licenses at no additional cost; standalone add-on still required for non-Copilot tenants"
  - "PnP custom Entra app registration prerequisite added to 1.2 PowerShell playbook — multi-tenant PnP Management Shell app deleted September 9, 2024"

patterns-established:
  - "Tier table updates: new capabilities integrated as additional text in existing tier rows, not new rows"
  - "Playbook alignment: portal-walkthrough gets dual paths (Purview + MAC), powershell-setup gets PnP registration block, verification-testing gets new test cases, troubleshooting gets new issues"

requirements-completed: [P1-01, P1-02, P1-03]

duration: 12min
completed: 2026-02-18
---

# Phase 3 Plan 01: Pillar 1 Controls 1.1, 1.2, 1.3 Updates Summary

**Controls 1.1-1.3 updated with Optimization Assessment infrastructure governance, unified DSPM experience (AI observability, Purview Posture Agent, Shadow AI, item-level remediation), and RCD+RSS complementary scope control — plus PnP PowerShell custom app registration fix across 12 playbooks**

## Performance

- **Duration:** 12 min
- **Started:** 2026-02-18T00:52:11Z
- **Completed:** 2026-02-18T01:04:00Z
- **Tasks:** 2
- **Files modified:** 15

## Accomplishments

- Control 1.1 updated with Optimization Assessment as Step 2 of the assessment workflow (MAC > Health > Copilot readiness), Office update channel governance (Current/Monthly Enterprise Channel required, tier-scored), and FFIEC IT Handbook citation for infrastructure readiness
- Control 1.2 rewritten to reflect the unified DSPM experience: AI observability, item-level remediation, Purview Posture Agent (Jan 2026 preview), and Shadow AI discovery — plus dual portal access paths
- Control 1.3 updated with RCD vs RSS comparison table, SAM licensing note (included with Copilot licenses), tier-differentiated use of both tools, and complementary use guidance
- 1.2 PowerShell playbook updated with mandatory PnP Entra app registration prerequisite (PLAY-01) — all Connect-PnPOnline calls include -ClientId
- All 12 playbooks (1.1, 1.2, 1.3) aligned to their respective control updates with current portal paths and new verification/troubleshooting content

## Task Commits

Each task was committed atomically:

1. **Task 1: Update controls 1.1 and 1.2 with playbook alignment** - `516b2a3` (feat)
2. **Task 2: Update control 1.3 with RCD/RSS comparison and playbook alignment** - `3e56d3b` (feat)

**Plan metadata:** `579206d` (docs: complete plan)

## Files Created/Modified

- `docs/controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md` — Added Optimization Assessment tool + workflow step, update channel governance scoring, updated steps 1-6
- `docs/controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md` — Rewritten DSPM section for unified experience, new capabilities table, dual portal paths, updated tier table and setup steps
- `docs/controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md` — Added RCD vs RSS comparison table, SAM licensing note, updated tier recommendations, updated setup steps
- `docs/playbooks/control-implementations/1.1/portal-walkthrough.md` — Added Optimization Assessment Step 1, MAC > Copilot > Security tab alternative path
- `docs/playbooks/control-implementations/1.1/powershell-setup.md` — Minor path updates for consistency
- `docs/playbooks/control-implementations/1.1/verification-testing.md` — Added Test 1 (Optimization Assessment completeness)
- `docs/playbooks/control-implementations/1.1/troubleshooting.md` — Added Issue 1 (update channel compliance), renumbered Issues 2-6
- `docs/playbooks/control-implementations/1.2/portal-walkthrough.md` — Complete rewrite for unified DSPM, dual paths, item-level remediation, Shadow AI, Posture Agent steps
- `docs/playbooks/control-implementations/1.2/powershell-setup.md` — Added PnP app registration prerequisite block, item-level remediation script, -ClientId on all Connect-PnPOnline calls
- `docs/playbooks/control-implementations/1.2/verification-testing.md` — Added Test 1 (unified DSPM + dual path), Test 5a (Shadow AI discovery)
- `docs/playbooks/control-implementations/1.2/troubleshooting.md` — Added Issue 1 (PnP auth failure), renumbered Issues 2-6
- `docs/playbooks/control-implementations/1.3/portal-walkthrough.md` — Complete rewrite for RSS+RCD dual approach with step-by-step for both tools
- `docs/playbooks/control-implementations/1.3/powershell-setup.md` — Added Scripts 5-7 (RCD enable, bulk enable, audit) with RestrictContentOrgWideSearch, SAM licensing note
- `docs/playbooks/control-implementations/1.3/verification-testing.md` — Added Test 5 (RCD functional), updated Test 6 (change control for both RSS and RCD)
- `docs/playbooks/control-implementations/1.3/troubleshooting.md` — Added Issue 1b (RCD propagation), updated Issue 1 with SAM licensing context

## Decisions Made

- Dual portal path pattern established for DSPM: full path via Microsoft Purview > Data Security Posture Management for complete functionality; quick access via MAC > Copilot > Overview > Security tab for Copilot-specific controls
- RCD positioned as Baseline starting point (lower admin overhead) with RSS as the Regulated-tier primary posture — this reflects real-world deployment patterns where RCD is simpler to start with
- SAM licensing documented as "included with M365 Copilot licenses at no additional cost" with explicit note that non-Copilot tenants still need standalone SAM — precision per RESEARCH.md pitfall guidance
- Item-level remediation added as Regulated-tier requirement for 1.2 — enables surgical remediation without site-wide disruption, particularly valuable in financial services contexts

## Deviations from Plan

None — plan executed exactly as written. All must_haves verified.

## Issues Encountered

None.

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- Controls 1.1, 1.2, 1.3 fully updated — ready for review
- Phase 3 Plan 02 (controls 1.6 and 1.7) can proceed immediately
- The PnP registration pattern established in 1.2 PowerShell playbook must be replicated in 1.6, 1.8, and 2.2 PowerShell playbooks (PLAY-01 remaining scope)

---
*Phase: 03-pillar-readiness-security*
*Completed: 2026-02-18*

## Self-Check: PASSED

All key files verified present. Both task commits (516b2a3, 3e56d3b) confirmed in git log. Requirements P1-01, P1-02, P1-03 marked complete in REQUIREMENTS.md.
