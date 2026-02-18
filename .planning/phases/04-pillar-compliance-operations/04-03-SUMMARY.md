---
phase: 04-pillar-compliance-operations
plan: 03
subsystem: compliance-documentation
tags: [finra-2210, finra-3110, sec-enforcement, agentic-ai, supervision, telemetry, audit, copilot-agents]

# Dependency graph
requires:
  - phase: 03-pillar-readiness-security
    provides: Communication Compliance foundation (3.4) and audit log schema (3.1) that 3.6 telemetry chain references
provides:
  - SEC v. Delphia enforcement precedent callout in control 3.5 with FINRA 2210(d)(1)(A) AI washing guidance
  - FINRA 2026 Oversight Report anticipatory framing in control 3.5
  - FINRA 2026 agentic AI supervision framing for Teams channel agents and declarative agents in control 3.6
  - Full-chain telemetry guidance for agent decision reconstruction (CopilotInteraction → AgentId/XPIA → CC records → business record)
  - SEC 2026 internal AI examination focus with anticipatory framing in control 3.6
  - Agent supervision playbooks: PowerShell scripts 5 and 6, verification tests 5 and 6, troubleshooting issues 5/6/7
affects: [04-pillar-compliance-operations, 04-04, 04-05, phase-5, phase-6-cross-linking]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Enforcement Precedent callout box pattern: MkDocs !!! warning admonition with case name and settlement date"
    - "Anticipatory framing pattern: 'institutions should prepare' / 'expected to' language for forward-looking FINRA/SEC guidance"
    - "Agentic AI supervision framing: M365 Copilot agents only (Teams channel agents, declarative agents); Copilot Studio excluded"
    - "Full-chain telemetry pattern: audit event chain documented as numbered tier guidance (Baseline/Recommended/Regulated)"
    - "Agent audit field references: AgentId, AgentName, XPIA named explicitly in powershell and portal playbooks"

key-files:
  created: []
  modified:
    - docs/controls/pillar-3-compliance/3.5-finra-2210-compliance.md
    - docs/controls/pillar-3-compliance/3.6-supervision-oversight.md
    - docs/playbooks/control-implementations/3.5/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.5/powershell-setup.md
    - docs/playbooks/control-implementations/3.5/verification-testing.md
    - docs/playbooks/control-implementations/3.5/troubleshooting.md
    - docs/playbooks/control-implementations/3.6/portal-walkthrough.md
    - docs/playbooks/control-implementations/3.6/powershell-setup.md
    - docs/playbooks/control-implementations/3.6/verification-testing.md
    - docs/playbooks/control-implementations/3.6/troubleshooting.md

key-decisions:
  - "SEC v. Delphia enforcement precedent placed in 'Why This Matters for FSI' section of 3.5 using !!! warning admonition; follow-up paragraph connects it to 2210(d)(1)(A) AI washing risk"
  - "FINRA 2026 anticipatory framing integrated into existing 'Regulatory Framework' section (not a standalone section — below 3-paragraph threshold)"
  - "AI washing detection added as Step 2 in portal-walkthrough and as Test 5 in verification-testing; troubleshooting Issue 5 covers false positives for legitimate Copilot capability descriptions"
  - "Agentic AI supervision in 3.6 placed in a dedicated 'Agentic AI Supervision Requirements' section (exceeds 3-paragraph threshold — Teams channel agents, declarative agents, and full-chain telemetry each require full treatment)"
  - "Full-chain telemetry documented as a numbered 4-step chain with tier guidance table (Baseline/Recommended/Regulated) — consistent with other tiered guidance in the framework"
  - "SEC 2026 exam focus placed in Financial Sector Considerations as standalone subsection (single focused paragraph with actionable guidance)"
  - "Agent audit PowerShell scripts use RecordType CopilotInteraction with AgentId filter — Scripts 5 (all agents) and 6 (specific AgentId) provide complementary retrieval patterns"

patterns-established:
  - "Enforcement Precedent callout: !!! warning admonition with settlement date in title, 2-3 sentences on what happened and regulatory liability established"
  - "Agentic AI supervision scope: always specify agent types (Teams channel agents, declarative agents) not generic 'AI agents'"
  - "Decision reconstruction chain: audit event source → agent fields → compliance records → business record (always 4-step with tier guidance)"

requirements-completed: [P3-05, P3-06]

# Metrics
duration: 9min
completed: 2026-02-18
---

# Phase 4 Plan 03: Pillar 3 Controls 3.5 and 3.6 — FINRA Enforcement, Agentic Supervision, and SEC 2026 Exam Focus Summary

**FINRA 2210 compliance updated with SEC v. Delphia AI washing enforcement precedent and FINRA 2026 anticipatory framing; FINRA 3110 supervision extended to M365 Copilot agents with full-chain telemetry and SEC 2026 examination preparation guidance**

## Performance

- **Duration:** 9 min
- **Started:** 2026-02-18T03:19:27Z
- **Completed:** 2026-02-18T03:28:08Z
- **Tasks:** 2
- **Files modified:** 10

## Accomplishments

- Control 3.5 now includes the SEC v. Delphia enforcement precedent as a dedicated MkDocs warning admonition, connecting AI washing risk directly to FINRA Rule 2210(d)(1)(A) and Investment Advisers Act Section 206 antifraud provisions
- Control 3.6 now includes a dedicated Agentic AI Supervision Requirements section documenting FINRA 3110(a) supervisory obligations for Teams channel agents and declarative agents, with full-chain telemetry guidance for decision reconstruction
- Both controls include anticipatory framing for FINRA 2026 Oversight Report and SEC 2026 examination focus using consistent "institutions should prepare" language
- All 8 playbooks updated: portal-walkthrough files add enforcement/agent audit navigation; PowerShell scripts 5 and 6 enable agent-specific audit event retrieval; verification tests 5 and 6 validate AI washing detection and agent audit trail capture; troubleshooting guides add AI washing false positive handling and three agent supervision issue types

## Task Commits

Each task was committed atomically:

1. **Task 1: Update control 3.5 with SEC v. Delphia precedent and FINRA 2026 Report + playbook alignment** - `404ec11` (feat)
2. **Task 2: Update control 3.6 with FINRA 2026 agentic supervision and SEC exam focus + playbook alignment** - `6943b3f` (feat)

**Plan metadata:** *(created in final commit)*

## Files Created/Modified

- `docs/controls/pillar-3-compliance/3.5-finra-2210-compliance.md` — Added SEC v. Delphia enforcement precedent callout, AI washing failure mode row, FINRA 2026 anticipatory framing, AI washing keyword dictionary in setup, Regulatory Framework section restructured
- `docs/controls/pillar-3-compliance/3.6-supervision-oversight.md` — Added Agentic AI Supervision Requirements section, Teams channel agent and declarative agent rows to surface coverage table, agent supervision row to Supervisory Framework Components table, full-chain telemetry guidance, SEC 2026 exam focus section
- `docs/playbooks/control-implementations/3.5/portal-walkthrough.md` — Added AI washing detection step to configuration, extended regulatory alignment table with 2210(d)(1)(A) and Section 206 references
- `docs/playbooks/control-implementations/3.5/powershell-setup.md` — Reviewed; no substantive changes needed (scripts accurate)
- `docs/playbooks/control-implementations/3.5/verification-testing.md` — Added Test 5 for AI washing detection with SEC v. Delphia regulatory basis
- `docs/playbooks/control-implementations/3.5/troubleshooting.md` — Added Issue 5 for AI washing detection false positives with resolution guidance
- `docs/playbooks/control-implementations/3.6/portal-walkthrough.md` — Added Step 5 for agent-specific audit event navigation in Purview; extended regulatory alignment and FSI Recommendations table with agent tier
- `docs/playbooks/control-implementations/3.6/powershell-setup.md` — Added Scripts 5 and 6 for agent audit event retrieval using RecordType CopilotInteraction and AgentId filter
- `docs/playbooks/control-implementations/3.6/verification-testing.md` — Added Tests 5 and 6 for agent audit trail capture and WSP coverage verification
- `docs/playbooks/control-implementations/3.6/troubleshooting.md` — Added Issues 5, 6, 7 covering agent output not in review queue, delayed/missing agent audit events, and WSP gap for newly deployed agents

## Decisions Made

- SEC v. Delphia enforcement precedent placed in "Why This Matters for FSI" section of 3.5 using `!!! warning` admonition with follow-up paragraph connecting the precedent to 2210(d)(1)(A) — the enforcement precedent pattern is now established for other controls in phase 4 that reference case law
- FINRA 2026 anticipatory framing integrated into existing "Regulatory Framework" section of 3.5 (not a standalone section — fits within the 3-paragraph threshold for integration)
- Agentic AI Supervision Requirements in 3.6 warranted a dedicated section (Teams channel agents, declarative agents, and full-chain telemetry each require full paragraph treatment — exceeds 3-paragraph threshold)
- Full-chain telemetry chain documented as numbered 4-step sequence with tier guidance table — consistent with existing tiered guidance patterns throughout the framework
- Agent PowerShell scripts use `RecordType CopilotInteraction` as primary filter then parse `AgentId` from AuditData JSON — this pattern aligns with how CopilotInteraction records are structured in the Purview audit schema

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Controls 3.5 and 3.6 are complete for Phase 4; enforcement precedent callout pattern is established and available for reuse
- Agentic AI supervision framing (Teams channel agents, declarative agents) is now documented in 3.6 and can be referenced by any subsequent plan that touches agent governance
- Full-chain telemetry chain (Control 3.1 → AgentId/XPIA → Control 3.4 → Control 3.11) explicitly cross-references other controls in the chain — future plans updating 3.1 or 3.11 should review 3.6 for consistency
- Phase 4 plan 04 can proceed; no blockers from this plan

---
*Phase: 04-pillar-compliance-operations*
*Completed: 2026-02-18*
