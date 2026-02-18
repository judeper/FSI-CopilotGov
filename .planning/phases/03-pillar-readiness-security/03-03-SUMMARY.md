---
phase: 03-pillar-readiness-security
plan: "03"
subsystem: content
tags: [license-planning, information-barriers, defender-cloud-apps, frontline, payg, channel-agent, ai-catalog]
dependency_graph:
  requires: []
  provides: [P1-06, P2-04, P2-05]
  affects: [1.9-license-planning, 2.4-information-barriers, 2.9-defender-cloud-apps]
tech_stack:
  added: []
  patterns: [frontline-sku-add-on, payg-copilot-chat, channel-agent-ib-compensating-controls, generative-ai-catalog, agent-threat-detection-xdr]
key_files:
  created: []
  modified:
    - docs/controls/pillar-1-readiness/1.9-license-planning.md
    - docs/controls/pillar-2-security/2.4-information-barriers.md
    - docs/controls/pillar-2-security/2.9-defender-cloud-apps.md
    - docs/playbooks/control-implementations/1.9/portal-walkthrough.md
    - docs/playbooks/control-implementations/1.9/powershell-setup.md
    - docs/playbooks/control-implementations/1.9/verification-testing.md
    - docs/playbooks/control-implementations/1.9/troubleshooting.md
    - docs/playbooks/control-implementations/2.4/portal-walkthrough.md
    - docs/playbooks/control-implementations/2.4/verification-testing.md
    - docs/playbooks/control-implementations/2.4/troubleshooting.md
    - docs/playbooks/control-implementations/2.9/portal-walkthrough.md
    - docs/playbooks/control-implementations/2.9/verification-testing.md
    - docs/playbooks/control-implementations/2.9/troubleshooting.md
decisions:
  - "Control 1.9: PAYG documented as available to any user with appropriate base license (not F1/F3 specific) per RESEARCH.md open question resolution"
  - "Control 2.4: Channel Agent IB limitation documented as a platform gap with 4 compensating controls; existing IB enforcement statements for standard Copilot surfaces preserved"
  - "Control 2.9: Generative AI app catalog updated to 1,000+ (correcting stale 400+ figure from original plan spec); agent threat detection documented with September 2025 Defender XDR capabilities"
metrics:
  duration: "~9 minutes"
  completed_date: "2026-02-18"
  tasks_completed: 2
  files_modified: 13
---

# Phase 03 Plan 03: Controls 1.9, 2.4, 2.9 Updates Summary

**One-liner:** Frontline/PAYG licensing for 1.9, Channel Agent IB limitation with compensating controls for 2.4, and 1,000+ AI app catalog with Defender XDR agent threat detection for 2.9 — plus 10 aligned playbooks.

## What Was Done

### Task 1: Control 1.9 — Frontline SKUs and PAYG Licensing (P1-06)

Updated `1.9-license-planning.md` and all 4 playbooks with:

**Frontline (F1/F3) SKU availability:**
- Added Microsoft 365 Copilot as a $30/user/month add-on for F1/F3 base licenses to the license landscape table
- Documented FSI frontline use cases: branch tellers, operations center staff, compliance on frontline licenses
- Added SEC 2026 Division of Examinations Priorities framing (November 17, 2025) — frontline Copilot deployment brings internal operations under AI governance scope
- Explicitly noted that F1/F3 Copilot feature parity with E3/E5 is not fully documented; recommended testing before broad deployment
- Added F1 and F3 rows to the prerequisite license requirements table

**Pay-As-You-Go (PAYG) Copilot Chat:**
- Added PAYG at $0.01/message via Azure billing as a distinct licensing option
- Documented governance considerations: Azure Cost Management tracking, spend limits, no per-user assignment required
- Added tier recommendations: Baseline allows PAYG for pilots (<50 users); Recommended uses per-seat for regular users and PAYG for occasional/seasonal; Regulated restricts PAYG to non-regulated use cases
- Added MAC > Cost Management as the PAYG tracking path

**All 4 playbooks aligned:**
- Portal-walkthrough: added Frontline group (Copilot-Frontline-Users), PAYG Azure Cost Management configuration path, Step 6 for PAYG governance
- PowerShell: updated Script 1 to include Frontline SKU patterns; added Script 4 for Frontline Copilot status report
- Verification-testing: added Test 5 (Frontline license verification) and Test 6 (PAYG governance)
- Troubleshooting: added Issue 6 (F1/F3 Copilot add-on failures) and Issue 7 (PAYG unexpected costs)

### Task 2: Control 2.4 — Channel Agent IB Limitation (P2-04)

Updated `2.4-information-barriers.md` and 3 playbooks with:

**Channel Agent IB coverage matrix:**
- Updated the Copilot Surface Coverage table to separate "Teams Copilot (meeting summaries, chat)" (IB enforced) from "Channel Agent in Teams" (IB NOT enforced)
- Added explicit "No" entries for Channel Agent with documentation of the platform limitation

**Compensating controls section:**
- New section: "Channel Agent IB Limitation and Compensating Controls"
- 4 compensating controls: restrict deployment to homogeneous segments, apply sensitivity labels, monitor via DSPM for AI, document in supervisory procedures
- FSI regulatory framing: SEC Rule 10b-5 and FINRA Rules 5280, 2241, 2242 (Chinese Wall requirements)
- Governance level updates: all three tiers now include Channel Agent restrictions appropriate to the tier

**Verification Criteria:** Added criteria 6 (Channel Agent IB gap documentation) and 7 (Channel Agent compensating controls)

**3 playbooks aligned:**
- Portal-walkthrough: added Step 6 "Manage Channel Agent IB Gap" with channel membership audit and sensitivity label application
- Verification-testing: added Test 5 (Channel Agent IB coverage verification) and Test 6 (IB coverage matrix completeness)
- Troubleshooting: added Issue 6 (Channel Agent surfaces cross-barrier content — including directive to remove agent from non-compliant channels and escalate to Compliance) and Issue 7 (uncertainty about surface IB enforcement)

### Task 2: Control 2.9 — AI App Catalog and Agent Threat Detection (P2-05)

Updated `2.9-defender-cloud-apps.md` and 3 playbooks with:

**AI app catalog (1,000+ generative AI apps):**
- Corrected stale "400+" figure to "1,000+ generative AI apps" in the generative AI subcategory (31,000+ apps total in the MDCA catalog)
- Added Generative AI App Catalog to MDCA Capability Matrix table
- Added full "Generative AI App Catalog" section with Shadow AI discovery workflow, risk score assessment, and governance policy application
- Navigation path documented: Defender portal > Cloud Apps > Cloud app catalog > Filter: Category = "Generative AI"
- GLBA 501(b) regulatory framing for Shadow AI governance

**Agent threat detection in Defender XDR (September 2025):**
- Added Agent threat detection to MDCA Capability Matrix table
- Added full "Agent Threat Detection in Microsoft Defender XDR" section with: compromised agent detection, malicious behavior detection, unified XDR incident timeline integration, cross-activity correlation
- FSI framing: FINRA 2026 Annual Regulatory Oversight Report + FINRA Rules 3110/3120 supervisory obligations for agentic AI
- Navigation path documented: Defender portal > Incidents & alerts

**Governance levels and verification criteria** updated to include catalog review and agent monitoring requirements per tier

**3 playbooks aligned:**
- Portal-walkthrough: fixed portal paths ("Microsoft Defender portal" replacing stale "Defender for Cloud Apps" references); added Step 6 (Generative AI App Catalog) and Step 7 (Agent Threat Detection)
- Verification-testing: added Test 4 (Generative AI catalog coverage) and Test 5 (Agent threat detection verification)
- Troubleshooting: added Issue 5 (agent threat detection alerts not appearing) and Issue 6 (generative AI catalog not showing discovered apps)

## Deviations from Plan

None — plan executed exactly as written with one clarification applied from RESEARCH.md open questions:

**PAYG targeting clarification (RESEARCH.md Open Question 4):** The plan spec asked to document PAYG as available "for occasional users, pilot programs, or organizations wanting to test." RESEARCH.md open question 4 noted uncertainty about whether PAYG targets F1/F3 workers specifically. Per the research recommendation, PAYG was documented as available to any user without a full Copilot license (including F1/F3), managed through MAC > Cost Management. This is consistent with the plan intent and resolves the ambiguity appropriately.

## Self-Check: PASSED

### Files Verified

All 13 modified files exist on disk. Both commits are present in git history:
- `cf904ee` — feat(03-03): update control 1.9 with Frontline SKUs and PAYG licensing
- `bac38ff` — feat(03-03): update controls 2.4 (Channel Agent IB) and 2.9 (AI app catalog)

### Verification Results

| Check | Result |
|-------|--------|
| F1/F3/Frontline in 1.9 control | 9 occurrences |
| pay-as-you-go/PAYG/$0.01 in 1.9 control | 21 occurrences |
| Channel Agent in 2.4 control | 13 occurrences |
| IB limitation ("not supported") documented in 2.4 | Confirmed |
| "1,000" in 2.9 control | 3 occurrences |
| Agent threat/detection in 2.9 control | 10 occurrences |
| No "400" bare count in 2.9 | PASS |
| No "BizChat" or "M365 Chat" in any modified file | PASS |
