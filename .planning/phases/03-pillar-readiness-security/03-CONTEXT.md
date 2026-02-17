# Phase 3: Pillar Updates — Readiness and Security - Context

**Gathered:** 2026-02-17
**Status:** Ready for planning

<domain>
## Phase Boundary

Update Pillar 1 (Readiness) and Pillar 2 (Security) control documents and their playbooks to accurately reflect current Microsoft 365 Copilot platform capabilities. 12 requirements (P1-01 through P1-06, P2-01 through P2-06) drive specific control updates. Additionally absorbs PLAY-01 (PnP PowerShell Entra app registration for controls 1.2, 1.6, 1.8, 2.2) and PLAY-03 (portal path updates) from Phase 6 since we're already in these playbooks. Opportunistically review all Pillar 1+2 playbooks for obvious issues even on controls without requirements.

</domain>

<decisions>
## Implementation Decisions

### Update depth
- Default approach: integrate new content into existing document sections — new bullets, expanded paragraphs, updated tables. Do not create new top-level sections unless absolutely necessary.
- Claude's discretion on whether major additions (e.g., P2-01 two DLP policy types, P2-06 Risky Agents with 4 sub-features) warrant a new subsection. Threshold: roughly 3+ paragraphs of genuinely new conceptual content.
- Seamless integration — no "Updated v1.1" markers, no changelogs. Updated controls should read as if they were always current. Commit history tracks what changed.
- When correcting factual errors (e.g., P1-05 SAM licensing), rewrite surrounding content that was built on the wrong assumption. Don't just fix the fact — fix the logic that depended on it.

### Playbook boundaries
- **Full playbook alignment**: when updating a control, also update all 4 playbook types (portal-walkthrough, PowerShell, audit-log, compliance-report) for that control to match.
- Absorb PLAY-01 (PnP PowerShell Entra app registration requirement for controls 1.2, 1.6, 1.8, 2.2) and PLAY-03 (portal path updates) into Phase 3. Phase 6 retains PLAY-02 (Exchange REST-only patterns) and PLAY-04 (cross-linking).
- Opportunistically review ALL Pillar 1+2 playbooks, even for controls without Phase 3 requirements — fix obvious issues (stale paths, wrong portal names) encountered while working in neighboring files.

### FSI framing depth
- Every new capability gets regulatory mapping when the connection is direct and specific. Format: capability description + explicit regulator + section number (e.g., "per FINRA 2026 Oversight Report, Section 4.2" or "per OCC 2025-26 §III.B").
- Skip regulatory framing when the connection is indirect or a stretch — pure platform feature updates don't need forced reg ties.
- Normalize the FSI tone across all Pillar 1+2 controls during this phase. Use the update as an opportunity to strengthen FSI framing in controls that are currently too generic. All controls should feel written for financial institutions, not just generic Microsoft guidance.

### Tier differentiation
- **Tier-gated rollout** for new capabilities:
  - **Baseline**: minimum viable configuration — feature is actually enabled with simplest, safest defaults
  - **Recommended**: standard operational configuration with monitoring and moderate enforcement
  - **Regulated**: strictest settings with additional audit requirements and manual review gates
- Match each control's existing tier presentation format (some use tables, some use sections). Be consistent within each file, don't impose a new format.
- When existing tier recommendations become outdated (feature is now Microsoft default): note the change in the text but keep the tier structure stable. Organizations following the framework shouldn't see disruptive tier reassignments.

### Claude's Discretion
- Whether individual major additions warrant new subsections vs. inline integration
- Exact placement of new content within existing document structures
- How to restructure surrounding content when correcting factual errors
- Which playbooks on non-requirement controls need fixes when reviewing opportunistically

</decisions>

<specifics>
## Specific Ideas

- Regulatory citations must include section numbers, not just regulator names — the framework should be auditable
- SAM licensing correction in P1-05 is a rewrite, not just a find-and-replace — surrounding recommendations may be based on incorrect assumption that SAM is a separate purchase
- The PnP PowerShell Entra app registration (PLAY-01) should be addressed in controls 1.2, 1.6, 1.8, and 2.2 playbooks since we're already updating those controls
- Portal path updates (PLAY-03) should use current Microsoft 365 Admin Center paths

</specifics>

<deferred>
## Deferred Ideas

- PLAY-02 (Exchange REST-only patterns for 12 Exchange Online playbooks) — remains in Phase 6
- PLAY-04 (cross-linking: Related Controls, Prerequisites, See Also) — remains in Phase 6
- Full playbook structural overhaul — out of scope; Phase 3 aligns content, not architecture

</deferred>

---

*Phase: 03-pillar-readiness-security*
*Context gathered: 2026-02-17*
