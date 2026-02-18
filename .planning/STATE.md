# State: FSI-CopilotGov

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-17)

**Core value:** Financial institutions can deploy M365 Copilot with confidence that every regulatory obligation is addressed through documented, auditable controls.
**Current focus:** v1.1 Review 01 — Phase 4: Pillar Updates — Compliance and Governance

## Current Position

Phase: 4 of 6 in progress (Pillar Updates — Compliance and Operations)
Plan: 3 of 7 complete in Phase 4 (04-01, 04-02, 04-03 complete; 04-04 through 04-07 remaining)
Status: Phase 4 IN PROGRESS (3/7 plans with SUMMARYs)
Last activity: 2026-02-18 — Completed 04-03 (Controls 3.5 FINRA 2210 + SEC v. Delphia enforcement precedent, Control 3.6 agentic AI supervision + SEC 2026 exam focus; P3-05 and P3-06 requirements satisfied)

Progress: [████████████░] 65% (13 of ~20 total plans complete; Phase 4 plan 03 added)

## Performance Metrics

**Velocity:**
- Total plans completed: 12
- Average duration: ~7 min
- Total execution time: ~79 min

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 02-global-naming-corrections | 6 | ~34 min | ~6 min |
| 03-pillar-readiness-security | 6 of 6 | ~45 min | ~7.5 min |

*Updated after each plan completion*
| Phase 02-global-naming-corrections P04 | 12 | 2 tasks | 40 files |
| Phase 02-global-naming-corrections P05 | 5 | 2 tasks | 1 files |
| Phase 02-global-naming-corrections P06 | 3 | 2 tasks | 14 files |
| Phase 03-pillar-readiness-security P03 | 9 | 2 tasks | 13 files |
| Phase 03-pillar-readiness-security P02 | 9 | 2 tasks | 11 files |
| Phase 03-pillar-readiness-security P04 | 11 | 2 tasks | 10 files |
| Phase 03-pillar-readiness-security P05 | 9 | 2 tasks | 10 files |
| Phase 03-pillar-readiness-security P01 | 12 | 2 tasks | 15 files |
| Phase 03-pillar-readiness-security P06 | 5 | 2 tasks | 1 files |
| Phase 04-pillar-compliance-operations P05 | 8 | 2 tasks | 10 files |
| Phase 04-pillar-compliance-operations P02 | 8 | 2 tasks | 10 files |

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
- [Phase 03-pillar-readiness-security]: 03-05: Control 2.10 warrants new subsection for Risky Agents — 4 distinct capabilities each with 2+ paragraphs crosses the 3-paragraph new-subsection threshold
- [Phase 03-pillar-readiness-security]: 03-05: IRM Triage Agent documented as requiring SR 11-7 model inventory entry — OCC Bulletin 2011-12 model risk management applies to AI decision-support tools
- [Phase 03-pillar-readiness-security]: 03-05: Troubleshooting guide in 2.3 intentionally mentions wrong app ID in diagnostic context only — appropriate documentation for admins to identify and correct misconfigured policies
- [Phase 03-pillar-readiness-security]: 03-04: DLP dual policy types are architecturally distinct — Type 1 (label-based) blocks at grounding/response phase; Type 2 (SIT-based) blocks at user prompt phase — must be configured as separate policies, cannot be merged
- [Phase 03-pillar-readiness-security]: 03-04: Label groups terminology: 'parent labels migrating to label groups' (GA January 2026, MC1111778) not 'parent labels deprecated'; migration path via Purview > Information Protection > Labels > Migrate sensitivity label scheme
- [Phase 03-pillar-readiness-security]: 03-04: Copilot Studio agents inherit highest sensitivity label from all knowledge sources — agents require label inheritance assessment as governance gate before activation
- [Phase 03-pillar-readiness-security]: 03-04: SEC Reg S-P (17 CFR Section 248, amended Dec 3, 2025) citation applied specifically to SIT-based prompt blocking (Type 2) — customer information safeguards must cover AI interaction surfaces
- [Phase 03-pillar-readiness-security]: 03-01: Unified DSPM documented with dual portal paths (Purview + MAC > Copilot > Overview > Security tab); item-level remediation at Regulated tier; Purview Posture Agent and Shadow AI discovery at Recommended tier
- [Phase 03-pillar-readiness-security]: 03-01: RCD positioned as Baseline starting point for 1.3 (lower admin overhead), RSS+RCD combination at Regulated tier; SAM included with Copilot licenses at no additional cost; PnP multi-tenant app deleted Sep 9 2024 — custom registration mandatory
- [Phase 03-pillar-readiness-security]: 03-06: Wrong CA app ID in troubleshooting.md is intentional diagnostic reference — documents known transcription error for admin identification; all operational files use correct ID fb8d773d-7ef8-4ec0-a117-179f88add510
- [Phase 03-pillar-readiness-security]: 03-06: Phase 3 all 5 success criteria pass; all 12 updated controls verified clean; MkDocs 11 pre-existing warnings stable with zero new warnings from Phase 3
- [Phase 04-pillar-compliance-operations]: Copilot Control System branding in 4.1: 'formerly distributed controls' referenced once, then new name throughout — same pattern as Phase 2 terminology corrections
- [Phase 04-pillar-compliance-operations]: Teams default change callout: \!\!\! danger ACTION REQUIRED with inline PowerShell in control doc; SEC 17a-4(b)(4), FINRA 4511, FINRA 3110(b)(4) cited per Phase 4 citation style
- [Phase 04-pillar-compliance-operations]: 04-02: Unified eDiscovery presented as current state (May 2025 GA); pre-migration case gap documented inline; February 2026 UX simplification documented with 'as of' framing
- [Phase 04-pillar-compliance-operations]: 04-02: IRM integration tier structure — Baseline (no IRM), Recommended (high-risk CC policies), Regulated (all policies with automated escalation workflows)
- [Phase 04-pillar-compliance-operations]: 04-02: Scope guardrail for expanded CC surfaces — Security Copilot, Fabric Copilot, Copilot Studio mentioned for awareness only (one sentence + table row); no configuration guidance

### Blockers/Concerns

- 11 unrecognized relative links flagged in MkDocs build (quick-start.md: 8 links to playbook directories, 1.1 control: 1 link to templates/, playbooks/index.md: 2 links to docs/controls/) — to be addressed during Phase 6 cross-linking

### Pending Todos

None yet.

## Session Continuity

Last session: 2026-02-17
Stopped at: Completed 04-02-PLAN.md (control 3.3 unified eDiscovery + 3.4 CC IRM integration; 10 files updated; P3-03 and P3-04 requirements marked complete)
Resume file: .planning/phases/04-pillar-compliance-operations/04-02-SUMMARY.md
