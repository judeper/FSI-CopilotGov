---
phase: 04-pillar-compliance-operations
plan: 05
subsystem: compliance-documentation
tags: [copilot-control-system, teams-governance, recordkeeping, finra, sec, sox, enabledwithtranscript]

# Dependency graph
requires:
  - phase: 03-pillar-readiness-security
    provides: Phase 3 pillar content baseline with correct terminology and controls
provides:
  - Control 4.1 updated with Copilot Control System branding, MAC Copilot dashboard, Baseline Security Mode
  - Control 4.2 updated with Teams Copilot default change ACTION REQUIRED callout and remediation
  - All 4.1 and 4.2 playbooks updated for new admin experience and recordkeeping enforcement
affects:
  - 04-06-PLAN (subsequent pillar-4 controls)
  - 04-07-PLAN (phase verification gate — SC-4 depends on this plan)

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Copilot Control System branding: first mention with 'formerly...' parenthetical, then new name throughout"
    - "ACTION REQUIRED callout: !!! danger admonition for compliance-critical breaking changes"
    - "Inline PowerShell in control docs for must-act regulatory remediations"
    - "Tier guidance table for new Microsoft features: Baseline/Recommended/Regulated rows"

key-files:
  created: []
  modified:
    - docs/controls/pillar-4-operations/4.1-admin-settings-feature-management.md
    - docs/controls/pillar-4-operations/4.2-teams-meetings-governance.md
    - docs/playbooks/control-implementations/4.1/portal-walkthrough.md
    - docs/playbooks/control-implementations/4.1/powershell-setup.md
    - docs/playbooks/control-implementations/4.1/verification-testing.md
    - docs/playbooks/control-implementations/4.1/troubleshooting.md
    - docs/playbooks/control-implementations/4.2/portal-walkthrough.md
    - docs/playbooks/control-implementations/4.2/powershell-setup.md
    - docs/playbooks/control-implementations/4.2/verification-testing.md
    - docs/playbooks/control-implementations/4.2/troubleshooting.md

key-decisions:
  - "Copilot Control System branding in 4.1: 'formerly distributed controls across...' referenced once in first paragraph, then Copilot Control System used throughout — same pattern as Phase 2 terminology corrections"
  - "Copilot for Admins governed by same CAB/SOD requirements as manual changes — documented with explicit FSI governance note warning callout"
  - "Baseline Security Mode: Baseline tier enables as starting point; Regulated tier enables plus customizes with deviation justification required"
  - "Teams default change callout: !!! danger (not warning) per locked decision — ACTION REQUIRED level; inline PowerShell included in control doc, not deferred to playbook"
  - "Regulatory citations in 4.2 callout: SEC 17a-4(b)(4), FINRA 4511, FINRA 3110(b)(4) — all cited with section number and one-sentence context per Phase 4 citation style decision"
  - "4.2 table format: EnabledWithTranscript vs Enabled compliance posture comparison added to make regulatory difference explicit"

patterns-established:
  - "ACTION REQUIRED pattern: !!! danger + bold date-specific framing + inline remediation PowerShell + verify command"
  - "Copilot Control System references: always refer to MAC > Copilot as the navigation path, not legacy Settings > Copilot"

requirements-completed:
  - P4-01
  - P4-02

# Metrics
duration: 8min
completed: 2026-02-18
---

# Phase 4 Plan 05: Copilot Control System and Teams Default Change Summary

**Control 4.1 updated with Copilot Control System branding and MAC dashboard; Control 4.2 updated with ACTION REQUIRED callout for March 2026 Teams Copilot default change (EnabledWithTranscript to Enabled) with inline PowerShell remediation and SEC/FINRA citations**

## Performance

- **Duration:** 8 min
- **Started:** 2026-02-18T03:19:31Z
- **Completed:** 2026-02-18T03:27:22Z
- **Tasks:** 2
- **Files modified:** 10

## Accomplishments

- Control 4.1 adopts "Copilot Control System" branding with the old distributed approach referenced once for continuity, then unified name throughout; documents MAC > Copilot > Overview dashboard, portal consolidation, Copilot for Admins, and Baseline Security Mode with tier-specific guidance
- Control 4.2 adds the SC-4 compliance-critical ACTION REQUIRED callout documenting the March 2026 Microsoft default change from `EnabledWithTranscript` to `Enabled`, including inline PowerShell remediation (`Set-CsTeamsMeetingPolicy -CopilotWithoutTranscript Disabled`), SEC 17a-4(b)(4), FINRA 4511, and FINRA 3110(b)(4) citations
- All 8 playbooks (4 per control) updated to reflect the new Copilot Control System admin experience and the Teams meeting policy remediation workflow

## Task Commits

Each task was committed atomically:

1. **Task 1: Control 4.1 with Copilot Control System and admin capabilities + playbook alignment** - `d93e3c9` (feat)
2. **Task 2: Control 4.2 with Teams Copilot default change and FSI recordkeeping impact + playbook alignment** - `ab338a4` (feat)

**Plan metadata:** (pending — docs commit)

## Files Created/Modified

- `docs/controls/pillar-4-operations/4.1-admin-settings-feature-management.md` — Copilot Control System branding, MAC Copilot dashboard, Copilot for Admins governance note, Baseline Security Mode tiers, SOX 404 regulatory framing
- `docs/controls/pillar-4-operations/4.2-teams-meetings-governance.md` — ACTION REQUIRED callout for Teams default change, EnabledWithTranscript vs Enabled comparison table, updated tier recommendations, inline PowerShell remediation
- `docs/playbooks/control-implementations/4.1/portal-walkthrough.md` — Rewritten to start from MAC > Copilot > Overview dashboard; Baseline Security Mode configuration steps added
- `docs/playbooks/control-implementations/4.1/powershell-setup.md` — Script 5 added for Baseline Security Mode verification and CA policy audit
- `docs/playbooks/control-implementations/4.1/verification-testing.md` — Tests for dashboard accessibility, Baseline Security Mode, Copilot for Admins added
- `docs/playbooks/control-implementations/4.1/troubleshooting.md` — Added Issues 3-5: dashboard data gaps, Baseline Security Mode conflicts, Copilot for Admins licensing
- `docs/playbooks/control-implementations/4.2/portal-walkthrough.md` — Step 1 is now the EnabledWithTranscript override for March 2026 default change; tier table updated
- `docs/playbooks/control-implementations/4.2/powershell-setup.md` — Script 1 fully rewritten as critical remediation; Script 4 added as full policy audit; schedule table updated
- `docs/playbooks/control-implementations/4.2/verification-testing.md` — Tests 1-2 for EnabledWithTranscript enforcement and audit log event pairing; compliance mapping updated with section-specific citations
- `docs/playbooks/control-implementations/4.2/troubleshooting.md` — Issue 1 reframed around March 2026 default change; Issues 2-3 added for propagation delays and per-user vs organizer policy inheritance

## Decisions Made

- **Copilot Control System branding:** First mention uses "formerly the set of distributed Copilot admin controls across M365 Admin Center, Teams Admin Center, and individual app admin centers" parenthetical, then "Copilot Control System" throughout — same pattern as Phase 2 terminology corrections
- **Copilot for Admins safety note:** Used `!!! warning` (not danger) for the FSI governance note on Copilot for Admins, as this is an ongoing procedural reminder rather than an urgent action item
- **Teams callout admonition level:** Used `!!! danger` per locked decision (ACTION REQUIRED level) — not `!!! warning`
- **Regulatory citations:** SEC 17a-4(b)(4), FINRA 4511, FINRA 3110(b)(4) all cited with section number and context sentence per Phase 4 citation style decision
- **Inline PowerShell in control 4.2:** Both the remediation cmdlet and verification cmdlet included in the callout box itself, not deferred to playbook — per locked decision

## Deviations from Plan

None — plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- P4-01 and P4-02 requirements fulfilled; controls 4.1 and 4.2 are now current
- SC-4 success criterion (Teams default change documented with ACTION REQUIRED callout) is satisfied by this plan
- Phase verification gate (04-07) can now validate SC-4 using the grep checks specified in the plan

## Self-Check: PASSED

All 11 files verified present. All 2 task commits (d93e3c9, ab338a4) confirmed in git log.

---
*Phase: 04-pillar-compliance-operations*
*Completed: 2026-02-18*
