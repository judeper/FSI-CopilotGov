# State: FSI-CopilotGov

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-17)

**Core value:** Financial institutions can deploy M365 Copilot with confidence that every regulatory obligation is addressed through documented, auditable controls.
**Current focus:** v1.1 Review 01 — Phase 4: Pillar Updates — Compliance and Governance

## Current Position

Phase: 4 of 6 in progress (Pillar Updates — Compliance and Operations)
Plan: 6 of 7 complete in Phase 4 (04-01 through 04-06 complete; 04-07 remaining)
Status: Phase 4 IN PROGRESS (6/7 plans with SUMMARYs)
Last activity: 2026-02-18 — Completed 04-06 (Control 4.4 Viva Copilot Chat insights + Engage-to-Teams integration; Control 4.8 PAYG billing model + per-seat vs PAYG comparison + governance controls; P4-03 and P4-04 requirements satisfied)

Progress: [████████████████░] 80% (16 of ~20 total plans complete)

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
| Phase 04-pillar-compliance-operations P03 | 9 | 2 tasks | 10 files |
| Phase 04-pillar-compliance-operations P01 | 9 | 2 tasks | 10 files |
| Phase 04-pillar-compliance-operations P06 | 12 | 2 tasks | 10 files |
| Phase 04-pillar-compliance-operations P04 | 18 | 2 tasks | 15 files |

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
- [Phase 04-pillar-compliance-operations]: 04-03: SEC v. Delphia enforcement precedent placed in 'Why This Matters for FSI' section of 3.5 using !!! warning admonition; follow-up paragraph connects it to 2210(d)(1)(A) AI washing risk
- [Phase 04-pillar-compliance-operations]: 04-03: Agentic AI supervision in 3.6 placed in dedicated section — Teams channel agents and declarative agents each require full paragraph treatment; full-chain telemetry documented as 4-step chain with tier guidance
- [Phase 04-pillar-compliance-operations]: 04-03: Agent PowerShell scripts use RecordType CopilotInteraction with AgentId filter — Scripts 5 (all agents) and 6 (specific AgentId) provide complementary retrieval patterns for supervisory review
- [Phase 04-pillar-compliance-operations]: 04-01: AgentId/FINRA 3110 mapping — AgentId is the supervisory anchor for agentic AI; maps agent invocations to approved use cases per FINRA Rule 3110 supervisory procedures
- [Phase 04-pillar-compliance-operations]: 04-01: PAYG audit billing positioned at Regulated tier as E5 alternative — requires governance controls (budget caps, spend alerting, per-workload tracking); SEC Rule 17a-4(a) six-year retention is primary driver
- [Phase 04-pillar-compliance-operations]: 04-01: Microsoft Copilot experiences is the primary retention location for M365 Copilot — Enterprise AI Apps and Other AI Apps noted for awareness only with explicit scope guardrail
- [Phase 04-pillar-compliance-operations]: 04-01: Threaded summaries retained independently — source content deletion does not cascade to Copilot summary; both source location and Copilot experiences must be covered in retention policies and eDiscovery holds
- [Phase 04-pillar-compliance-operations]: 04-01: Priority cleanup conservative posture — Regulated tier retains all Copilot-generated content per SEC Rule 17a-3(a)(17) broad communications coverage
- [Phase 04-pillar-compliance-operations]: 04-06: Copilot Chat analytics documented as aggregation-only in Viva Insights — individual queries never visible; FFIEC IT Examination Handbook Section II.C anchors the monitoring expectation
- [Phase 04-pillar-compliance-operations]: 04-06: Engage-to-Teams integration is net positive for compliance — dual-location policy coverage (Yammer + Teams) extends compliance perimeter automatically for regulated content
- [Phase 04-pillar-compliance-operations]: 04-06: PAYG breakeven explicitly documented at 3,000 messages/user/month ($30 per-seat / $0.01 per message); SOX 404 and OCC Heightened Standards (12 CFR Part 30) cited for PAYG budget authorization controls; FFIEC Section II.D for cost-benefit analysis documentation
- [Phase 04-pillar-compliance-operations]: 04-04: OCC Bulletin 2025-26 proportionality applies to all institution sizes; tier selection (Tier 1/2/3) follows actual usage scope and risk profile; documented rationale citing OCC Bulletin 2025-26 required for Tier 3 at community banks
- [Phase 04-pillar-compliance-operations]: 04-04: Copilot SR 11-7 gray zone resolved as model inventory inclusion posture — industry consensus and 2023 Interagency AI Guidance support treating Copilot as a model subject to MRM at appropriate tier
- [Phase 04-pillar-compliance-operations]: 04-04: Reg S-P 72-hour vendor notification (Rule 248.30(a)(3)) requires Microsoft MSRC notification for Copilot NPI incidents; notification precedes investigation completion; 72-hour clock starts at detection, not investigation end
- [Phase 04-pillar-compliance-operations]: 04-04: SEC Rule 17a-4(f)(2)(ii)(A) audit-trail alternative offered alongside Option B (third-party WORM); Purview regulatory record labels + Preservation Lock + audit log coverage satisfies alternative; compliance counsel review required before relying on Option A
- [Phase 04-pillar-compliance-operations]: 04-04: Unified narrative threading in 3.11 — 17a-4 audit-trail alternative, $2B+ off-channel enforcement context, and mobile Copilot recordkeeping woven into single cohesive narrative per Phase 4 locked decision; no separate subsections
- [Phase 04-pillar-compliance-operations]: 04-04: Mobile Copilot Conditional Access cross-reference to Control 2.3 — detailed CA policy configuration lives in 2.3; 3.11 documents the requirement and mobile coverage gap risk

### Blockers/Concerns

- 11 unrecognized relative links flagged in MkDocs build (quick-start.md: 8 links to playbook directories, 1.1 control: 1 link to templates/, playbooks/index.md: 2 links to docs/controls/) — to be addressed during Phase 6 cross-linking

### Pending Todos

None yet.

## Session Continuity

Last session: 2026-02-18
Stopped at: Completed 04-04-PLAN.md (Controls 3.8/3.10/3.11 with OCC Bulletin 2025-26 proportionality, Reg S-P 72-hour amendment, 17a-4 audit-trail alternative, off-channel enforcement, mobile recordkeeping; 15 files updated; P3-07/P3-08/P3-09 satisfied)
Resume file: .planning/phases/04-pillar-compliance-operations/04-04-SUMMARY.md
