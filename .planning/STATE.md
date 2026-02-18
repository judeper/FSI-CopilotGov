# State: FSI-CopilotGov

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-17)

**Core value:** Financial institutions can deploy M365 Copilot with confidence that every regulatory obligation is addressed through documented, auditable controls.
**Current focus:** v1.1 Review 01 — Phase 3: Pillar Updates — Readiness and Security

## Current Position

Phase: 3 of 6 (Pillar Updates — Readiness and Security)
Plan: 3 of 6 in current phase (03-01, 03-02, 03-03 complete)
Status: Phase 3 in progress (3/6 plans complete — 03-01, 03-02, 03-03 done; 03-04, 03-05, 03-06 pending)
Last activity: 2026-02-18 — Completed 03-03 (controls 1.9, 2.4, 2.9 updated; 13 files; Frontline/PAYG licensing, Channel Agent IB gap, AI app catalog 1,000+, Defender XDR agent threat detection)

Progress: [████████░░] 45% (9 of ~20 total plans complete)

## Performance Metrics

**Velocity:**
- Total plans completed: 6
- Average duration: ~6 min
- Total execution time: ~34 min

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 02-global-naming-corrections | 6 | ~34 min | ~6 min |

*Updated after each plan completion*
| Phase 02-global-naming-corrections P04 | 12 | 2 tasks | 40 files |
| Phase 02-global-naming-corrections P05 | 5 | 2 tasks | 1 files |
| Phase 02-global-naming-corrections P06 | 3 | 2 tasks | 14 files |
| Phase 03-pillar-readiness-security P03 | 9 | 2 tasks | 13 files |
| Phase 03-pillar-readiness-security P02 | 9 | 2 tasks | 11 files |

## Accumulated Context

### Decisions

- v1.0: 4 pillars, 4 playbooks per control, three-tier governance — all validated good
- v1.1: Phase 2 does global naming first (GLOB-01/02) before any pillar content work — unblocks clean review baseline
- v1.1: Phase 2 scope expanded to full terminology audit (not just BizChat) — Microsoft Learn is canonical authority
- v1.1: BizChat replacement is context-dependent — "Microsoft 365 Copilot Chat" (free/seeded) vs "Microsoft 365 Copilot" (licensed) — researcher must categorize each instance before replacement
- v1.1: GLOB-03 (SAM licensing) assigned to Phase 5 alongside FWRK-03 — both touch license-requirements.md; P1-05 handles control 1.7 side in Phase 3
- 02-01: All BizChat instances in Pillars 1-2 map to free/seeded experience — replaced with "Microsoft 365 Copilot Chat" throughout (not licensed "Microsoft 365 Copilot")
- [Phase 02-global-naming-corrections]: 02-03: All BizChat references in foundational docs map to 'Microsoft 365 Copilot Chat' (free/seeded experience); shortened form 'Copilot Chat' used after first mention per document, full name in headings
- [Phase 02-global-naming-corrections]: 02-02: All BizChat instances in Pillars 3 and 4 map to 'Microsoft 365 Copilot Chat' (free/seeded experience); full name in headers, 'Copilot Chat' shortened form in body text after first mention
- [Phase 02-global-naming-corrections]: 02-04: Office 365 E3/E5 SKU names preserved; generic Office 365 platform refs replaced; PowerShell API literals preserved; Entra ID is canonical name; purview.microsoft.com is canonical Purview portal URL
- [Phase 02-global-naming-corrections]: 02-04: Office 365 SKU names (E1/E3/E5) preserved; generic Office 365 platform refs replaced with Microsoft 365; PowerShell API literals preserved; purview.microsoft.com is canonical Purview portal URL
- [Phase 02-global-naming-corrections]: 02-05: Phase 2 success criteria updated from 4 to 5 criteria; dual-name mapping (M365 Copilot Chat free/seeded vs M365 Copilot licensed) and full terminology scope (Azure AD, O365, compliance.microsoft.com, etc.) now captured in ROADMAP.md
- [Phase 02-global-naming-corrections]: 02-06: SC-3 gap closure — first bare "Copilot Chat" occurrence per file expanded to full name; "formerly Business Chat" removed silently; headings use full product name; 63 files all have correct ordering; Phase 2 5/5 success criteria achieved
- [Phase 03-pillar-readiness-security]: 03-03: PAYG Copilot Chat documented as available to any user with appropriate base license (not F1/F3 specific); F1/F3 Copilot add-on documented without asserting feature parity with E3/E5
- [Phase 03-pillar-readiness-security]: 03-03: Channel Agent IB limitation documented as a platform gap with 4 compensating controls; standard Copilot surfaces retain full IB enforcement; limitation must appear in supervisory procedures per SEC 10b-5 and FINRA 5280/2241/2242
- [Phase 03-pillar-readiness-security]: 03-02: Three new DSPM for AI RBAC roles (AI Viewer, AI Content Viewer, AI Administrator) added to 1.6 as new subsection; SAM licensing corrected in 1.7 with full downstream logic rewrite; RAC documented alongside RCD as peer capability
- [Phase 03-pillar-readiness-security]: 03-02: PnP PLAY-01 pattern established: Prerequisites section + Register-PnPEntraIDAppForInteractiveLogin + -ClientId on all Connect-PnPOnline calls

### Blockers/Concerns

- 11 unrecognized relative links flagged in MkDocs build (quick-start.md: 8 links to playbook directories, 1.1 control: 1 link to templates/, playbooks/index.md: 2 links to docs/controls/) — to be addressed during Phase 6 cross-linking

### Pending Todos

None yet.

## Session Continuity

Last session: 2026-02-18
Stopped at: Completed 03-02-PLAN.md (controls 1.6 and 1.7 updated, PnP fix applied to 1.6 and 1.8)
Resume file: .planning/phases/03-pillar-readiness-security/03-02-SUMMARY.md
