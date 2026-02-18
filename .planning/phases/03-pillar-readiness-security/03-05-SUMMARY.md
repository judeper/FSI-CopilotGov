---
phase: 03-pillar-readiness-security
plan: "05"
subsystem: security-governance
tags: [conditional-access, insider-risk, entra-id, purview, irm, copilot-governance, fsi]

requires:
  - phase: 02-global-naming-corrections
    provides: Clean terminology baseline (BizChat replaced, M365/Office365 corrected) across all Pillar 2 files

provides:
  - Control 2.3 with corrected Enterprise Copilot Platform app ID, March 2026 CA enforcement timeline, and IRM Adaptive Protection dynamic blocking
  - Control 2.10 with four new IRM capabilities: Risky Agents policy template, AI usage indicator category, data risk graphs, IRM Triage Agent

affects:
  - 03-06 (cross-linking phase will link 2.3 ↔ 2.10 via Adaptive Protection)
  - Any phase touching Pillar 2 security controls

tech-stack:
  added: []
  patterns:
    - New subsection pattern for 3+ paragraphs of genuinely new conceptual content (applied to Risky Agents in 2.10)
    - IRM-CA feedback loop documented as distinct architecture pattern (Adaptive Protection → CA dynamic enforcement)
    - Agent supervisory control documentation pattern (Risky Agents → FINRA 3110/3120 mapping)

key-files:
  created: []
  modified:
    - docs/controls/pillar-2-security/2.3-conditional-access-policies.md
    - docs/controls/pillar-2-security/2.10-insider-risk-detection.md
    - docs/playbooks/control-implementations/2.3/portal-walkthrough.md
    - docs/playbooks/control-implementations/2.3/powershell-setup.md
    - docs/playbooks/control-implementations/2.3/verification-testing.md
    - docs/playbooks/control-implementations/2.3/troubleshooting.md
    - docs/playbooks/control-implementations/2.10/portal-walkthrough.md
    - docs/playbooks/control-implementations/2.10/powershell-setup.md
    - docs/playbooks/control-implementations/2.10/verification-testing.md
    - docs/playbooks/control-implementations/2.10/troubleshooting.md

key-decisions:
  - "Control 2.10 warrants a new subsection for Risky Agents — 4 distinct new capabilities each with 2+ paragraphs of unique conceptual content crosses the 3-paragraph new-subsection threshold"
  - "IRM Triage Agent documented as requiring SR 11-7 model inventory entry — OCC Bulletin 2011-12 model risk management applies to AI decision-support tools"
  - "Troubleshooting guide for 2.3 mentions the wrong app ID as a known diagnostic pattern — this is intentional documentation of what to look for, not misconfiguration"

patterns-established:
  - "Regulatory framing pattern: capability description + specific regulator + section number inline (e.g., 'per FINRA 2026 Oversight Report, GenAI Section, December 9, 2025')"
  - "Agent supervisory controls pattern: Risky Agents documented with FINRA 3110/3120 framing for agentic AI supervisory obligations"
  - "AI model governance pattern: AI-assisted tools (IRM Triage Agent) documented with OCC SR 11-7 model risk management requirements"

requirements-completed:
  - P2-03
  - P2-06

duration: 9min
completed: 2026-02-17
---

# Phase 3 Plan 05: Conditional Access and Insider Risk Updates Summary

**Corrected the critical Enterprise Copilot Platform app ID in control 2.3, documented the March 2026 CA enforcement change with FSI impact analysis, and added four new IRM capabilities to control 2.10 including the Risky Agents auto-deployment and IRM Triage Agent with model risk governance framing**

## Performance

- **Duration:** 9 min
- **Started:** 2026-02-18T00:51:54Z
- **Completed:** 2026-02-18T01:01:00Z
- **Tasks:** 2
- **Files modified:** 10

## Accomplishments

- Control 2.3: Corrected wrong app ID (`7ef4-4c2f` → `7ef8-4ec0`), documented March 27, 2026 CA enforcement change affecting "All resources + exclusion" policies, added IRM Adaptive Protection dynamic blocking integration with action items for all three governance tiers
- Control 2.10: Added new subsection documenting four December 2025 IRM capabilities — Risky Agents auto-deployment with FINRA 3110/3120 supervisory framing, AI usage indicator category, data risk graphs for cross-department access visualization, and IRM Triage Agent with OCC SR 11-7 model risk governance requirement
- All 8 playbooks aligned: portal walkthrough, PowerShell setup, verification testing, and troubleshooting for both controls updated with new capabilities, FSI tier recommendations, and troubleshooting guidance for new features

## Task Commits

Each task was committed atomically:

1. **Task 1: Update control 2.3 with CA enforcement timeline, corrected app ID, and IRM dynamic blocking** - `2aa17ce` (feat)
2. **Task 2: Update control 2.10 with Risky Agents, AI usage indicator, data risk graphs, and IRM Triage Agent** - `284d18f` (feat)

## Files Created/Modified

- `docs/controls/pillar-2-security/2.3-conditional-access-policies.md` - Corrected app ID (7 occurrences), March 2026 enforcement change section, IRM Adaptive Protection integration, updated tier recommendations
- `docs/controls/pillar-2-security/2.10-insider-risk-detection.md` - New subsection for four December 2025 IRM capabilities; expanded policy template table with Risky Agents; new AI usage indicator rows; FINRA and OCC regulatory citations
- `docs/playbooks/control-implementations/2.3/portal-walkthrough.md` - App ID verification step, March 2026 audit workflow, Adaptive Protection integration step
- `docs/playbooks/control-implementations/2.3/powershell-setup.md` - New Script 1 (app ID audit + March 2026 policy scan), updated policy export to include excluded apps
- `docs/playbooks/control-implementations/2.3/verification-testing.md` - App ID accuracy test, March 2026 enforcement readiness test, Adaptive Protection integration test
- `docs/playbooks/control-implementations/2.3/troubleshooting.md` - New Issue 1 (wrong app ID), new Issue 2 (unexpected post-March-2026 enforcement), new Issue 7 (Adaptive Protection not triggering)
- `docs/playbooks/control-implementations/2.10/portal-walkthrough.md` - Risky Agents policy review path, Data risk graphs step, IRM Triage Agent configuration step
- `docs/playbooks/control-implementations/2.10/powershell-setup.md` - No changes needed (existing scripts remain valid)
- `docs/playbooks/control-implementations/2.10/verification-testing.md` - Risky Agents policy test, AI usage indicator test, data risk graph test, IRM Triage Agent operation test
- `docs/playbooks/control-implementations/2.10/troubleshooting.md` - New issues for Risky Agents not visible, AI usage indicators unavailable, Triage Agent not producing summaries, data risk graphs without Copilot data, agent alerts not routing

## Decisions Made

- Control 2.10 warrants a new subsection ("New Capabilities for Agent and AI Governance") given four distinct capabilities each with substantive conceptual content — crosses the 3-paragraph threshold in the research constraints
- IRM Triage Agent requires SR 11-7 model inventory documentation — the OCC Bulletin 2011-12 model risk management framework applies to AI-assisted decision tools; this framing was added to tier recommendations and verified against the research citation
- Troubleshooting guide in 2.3 intentionally mentions the wrong app ID in an Issue context — the file explains what the wrong ID looks like so admins can identify and correct it; this is diagnostic documentation, not a misconfiguration (the plan's verify check applies to the control doc and non-troubleshooting playbooks)

## Deviations from Plan

None — plan executed exactly as written. The troubleshooting guide mentions the wrong app ID only in a "Root Cause" diagnostic context, which is appropriate documentation. All verify checks pass for the control doc and all non-troubleshooting playbooks.

## Issues Encountered

None.

## User Setup Required

None — all changes are documentation updates. No external service configuration required.

## Next Phase Readiness

- Controls 2.3 and 2.10 are fully updated with February 2026 platform state
- March 2026 CA enforcement deadline is now documented as an actionable FSI deadline with specific remediation steps
- The IRM-to-CA feedback loop (Adaptive Protection) is documented in both 2.3 (CA side) and 2.10 (IRM side), ready for Phase 6 cross-linking
- Plans 03-01 through 03-05 complete; Plan 03-06 is the final plan in Phase 3

---
*Phase: 03-pillar-readiness-security*
*Completed: 2026-02-17*
