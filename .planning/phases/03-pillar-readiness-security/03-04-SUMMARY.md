---
phase: 03-pillar-readiness-security
plan: "04"
subsystem: security
tags: [dlp, sensitivity-labels, purview, copilot, pnp-powershell, label-groups, agent-inheritance, sit-based, prompt-blocking]

requires:
  - phase: 02-global-naming-corrections
    provides: Clean terminology baseline — "Microsoft 365 Copilot Chat" vs "Microsoft 365 Copilot" distinction applied across all files before content updates begin

provides:
  - Control 2.1 with dual DLP policy architecture (label-based response blocking + SIT-based prompt blocking), default policy in simulation mode, Edge browser DLP
  - Control 2.2 with label groups taxonomy, Copilot Studio agent label inheritance governance, nested AND/OR/NOT auto-labeling conditions
  - 2.2 PowerShell playbook with mandatory PnP custom Entra app registration prerequisite (PLAY-01)
  - All 8 playbooks (4 per control) aligned to updated control content

affects:
  - 03-05-PLAN (Control 2.3 — CA policy enforcement builds on DLP + label foundation)
  - 03-06-PLAN (Control 2.4 — Information Barriers complement DLP label-based blocking)
  - Phase 6 cross-linking (controls 2.1 and 2.2 now have updated verification criteria for cross-referencing)

tech-stack:
  added: []
  patterns:
    - "Dual DLP policy pattern: two separate Purview DLP policies required for Copilot — one label-based (response side), one SIT-based (prompt side) — cannot be merged"
    - "Agent governance gate: Copilot Studio agents require label inheritance assessment before activation; highest label from knowledge sources defines agent's effective label"
    - "Nested auto-labeling: AND/OR/NOT condition groups enable complex FSI classification rules combining multiple SIT detections with contextual exclusions"
    - "PnP registration mandatory: all Connect-PnPOnline calls require -ClientId after multi-tenant PnP Management Shell deletion (Sep 9, 2024)"

key-files:
  created: []
  modified:
    - docs/controls/pillar-2-security/2.1-dlp-policies-for-copilot.md
    - docs/controls/pillar-2-security/2.2-sensitivity-labels-classification.md
    - docs/playbooks/control-implementations/2.1/portal-walkthrough.md
    - docs/playbooks/control-implementations/2.1/powershell-setup.md
    - docs/playbooks/control-implementations/2.1/verification-testing.md
    - docs/playbooks/control-implementations/2.1/troubleshooting.md
    - docs/playbooks/control-implementations/2.2/portal-walkthrough.md
    - docs/playbooks/control-implementations/2.2/powershell-setup.md
    - docs/playbooks/control-implementations/2.2/verification-testing.md
    - docs/playbooks/control-implementations/2.2/troubleshooting.md

key-decisions:
  - "DLP dual policy types are architecturally distinct enforcement mechanisms — Type 1 (label-based) blocks at Copilot's grounding/response phase; Type 2 (SIT-based) blocks at user prompt phase — these cannot be merged and must be documented as separate policies with separate governance"
  - "Default Copilot DLP policy (MC1182689, GA Jan 2026) described as SIT-based prompt blocking type based on Microsoft documentation characterizing it as prompt-scanning; accessible from MAC > Copilot > Overview > Security tab"
  - "Label groups terminology: 'parent labels migrating to label groups' — not 'parent labels deprecated' — per RESEARCH.md guidance from MC1111778; migration path documented via Purview > Information Protection > Labels > Migrate sensitivity label scheme"
  - "Copilot Studio agent label inheritance: agent inherits highest label across ALL knowledge sources — one HC document elevates the entire agent — documented as governance gate requiring compliance sign-off before activation at Recommended/Regulated tiers"
  - "SEC Reg S-P (17 CFR Section 248, amended Dec 3, 2025) citation used for SIT-based prompt blocking specifically — direct regulatory mapping as verified in RESEARCH.md"

patterns-established:
  - "Type 1 vs Type 2 distinction: when documenting Copilot DLP, always distinguish enforcement point (response/grounding vs prompt/input) — single-policy framing is incorrect"
  - "Agent governance at deployment: label inheritance assessment + DLP policy verification required before agent activation — pattern established for all future agent-touching controls"

requirements-completed:
  - P2-01
  - P2-02

duration: 11min
completed: 2026-02-17
---

# Phase 3 Plan 04: Pillar 2 Controls 2.1 and 2.2 Update Summary

**Dual DLP policy architecture for Copilot (label-based response blocking + SIT-based prompt blocking) with label groups taxonomy, Copilot Studio agent label inheritance governance, and nested auto-labeling conditions**

## Performance

- **Duration:** ~11 min
- **Started:** 2026-02-18T00:51:49Z
- **Completed:** 2026-02-18T01:03:00Z
- **Tasks:** 2
- **Files modified:** 10

## Accomplishments

- Control 2.1 now documents two architecturally distinct DLP policy types with a comparison table — the existing document covered only label-based blocking; SIT-based prompt blocking was entirely missing
- Control 2.2 documents label groups replacing parent labels (GA January 2026), Copilot Studio agent label inheritance (agents inherit highest label from knowledge sources), and nested AND/OR/NOT auto-labeling conditions (GA December 2025)
- 2.2 PowerShell playbook now has the mandatory PnP custom Entra app registration prerequisite and all `Connect-PnPOnline` calls updated with `-ClientId` (PLAY-01 complete for 2.2)
- All 8 playbooks across both controls aligned to updated control content; portal paths updated to include MAC > Copilot > Overview > Security tab access paths

## Task Commits

Each task was committed atomically:

1. **Task 1: Update control 2.1 with dual DLP policy types, default policy, and Edge DLP** - `fd16b64` (feat)
2. **Task 2: Update control 2.2 with label groups, agent inheritance, and auto-labeling rules** - `729260b` (feat)

**Plan metadata:** _(docs commit to follow)_

## Files Created/Modified

- `docs/controls/pillar-2-security/2.1-dlp-policies-for-copilot.md` — Major expansion: dual DLP policy types with comparison table, default policy (simulation mode, MC1182689), Edge browser DLP (Sep 2025), updated architecture diagram, updated governance levels, 2 additional verification criteria
- `docs/controls/pillar-2-security/2.2-sensitivity-labels-classification.md` — Label groups migration documentation, Copilot Studio agent label inheritance section, nested AND/OR/NOT auto-labeling, updated taxonomy table (label groups column), updated governance levels, 2 additional verification criteria
- `docs/playbooks/control-implementations/2.1/portal-walkthrough.md` — Separate steps for Type 1 and Type 2 policy creation; default policy review step; Edge DLP configuration step; updated FSI recommendations table
- `docs/playbooks/control-implementations/2.1/powershell-setup.md` — Separate scripts for Type 1 and Type 2 policy creation; policy status report flags if either type is missing; incident report separates matches by policy type
- `docs/playbooks/control-implementations/2.1/verification-testing.md` — Separate test cases for Type 1 and Type 2 verification; default policy simulation review test; Edge DLP test case; updated compliance mapping with SEC Reg S-P amendment
- `docs/playbooks/control-implementations/2.1/troubleshooting.md` — New Issue 1 explaining why the two types cannot be combined; Issue 3 for default policy not visible; Issue 7 for Edge DLP not applying
- `docs/playbooks/control-implementations/2.2/portal-walkthrough.md` — Label groups migration assessment step; agent label inheritance review step (Step 5); nested auto-labeling conditions configuration; updated FSI recommendations
- `docs/playbooks/control-implementations/2.2/powershell-setup.md` — PnP app registration prerequisite block at top; all Connect-PnPOnline calls updated with -ClientId; Script 4 (multi-site scan); Script 5 (label groups migration status)
- `docs/playbooks/control-implementations/2.2/verification-testing.md` — Test 1 for label groups migration status; Test 3 for agent label inheritance; Test 4 for nested auto-labeling conditions; updated evidence collection table
- `docs/playbooks/control-implementations/2.2/troubleshooting.md` — Issue 1 (DLP policies failing after label groups migration); Issue 3 (agent inheriting unexpected label); Issue 4 (nested auto-labeling conditions not applying correctly)

## Decisions Made

- **Default DLP policy type:** Described as SIT-based prompt blocking type based on Microsoft documentation characterizing it as prompt-scanning (MC1182689 message center note describes it as "safeguarding prompts containing sensitive data"). Noted accessible from both MAC and Purview per RESEARCH.md verified paths.
- **Agent inheritance documentation placement:** Added as a new subsection in Control 2.2 under "Control Description" — the volume of genuinely distinct content (new workflow: deployment approval gate, knowledge source audit, inherited label documentation) met the new subsection threshold from RESEARCH.md.
- **Nested auto-labeling:** Integrated into the existing auto-labeling section as an enhancement with an explanatory paragraph and updated the example table — did not warrant a new subsection per RESEARCH.md guidance ("integrate into existing auto-labeling section").
- **SEC Reg S-P citation:** Applied specifically to the SIT-based prompt blocking type (Type 2) per RESEARCH.md verified citation — "per SEC Regulation S-P (17 CFR Section 248), amended effective December 3, 2025 for larger entities, customer information safeguards must cover AI interaction surfaces."

## Deviations from Plan

None — plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- Control 2.1 and 2.2 are updated with all Phase 3 content (P2-01, P2-02 complete)
- PLAY-01 complete for control 2.2 PowerShell playbook; PLAY-03 portal paths updated for both controls
- Ready to proceed with Controls 2.3 (CA policies) and 2.4 (Information Barriers) in subsequent plans
- Controls 2.1 and 2.2 cross-reference each other — label-based DLP in 2.1 depends on the label taxonomy in 2.2; this dependency is explicitly documented in both controls

## Self-Check: PASSED

All 10 modified files confirmed present on disk. Both task commits (fd16b64, 729260b) confirmed in git log. SUMMARY.md created at correct path. No missing files or commits.

---

*Phase: 03-pillar-readiness-security*
*Completed: 2026-02-17*
