<!-- Educational reference only — not legal advice. Firms should resolve these questions with qualified counsel and compliance owners. -->

# Regulatory Applicability Questions

This appendix captures open applicability questions that each firm should resolve with counsel, compliance, records-management, model-risk, and business owners before treating the framework's regulatory references as applicable to its environment.

!!! warning "Firm/counsel determination"
    Regulatory citations identify commonly referenced requirements. Applicability, record classification, supervisory-source mapping, and retention periods are a firm and counsel determination. This framework does not assert that any regulation applies or is satisfied.

---

## Control 3.2 — Data Retention Policies

1. For this framework, which Copilot artifacts are records under FINRA 4511, SEC Rules 17a-3/17a-4, and SOX 802: Microsoft 365 Copilot Chat history, Teams meeting recaps, Teams chat Copilot interactions, Copilot Pages/Notebooks, unsent Copilot-assisted drafts, sent Copilot-assisted emails, Copilot-assisted financial analyses, and Copilot audit events; and what retention period applies to each category (3 years, 6 years, 7 years/internal standard, or other)?
2. Is Microsoft Purview Preservation Lock, configured with the proposed retention policy/label policy design for Control 3.2, an approved WORM/electronic-recordkeeping mechanism for this firm's SEC Rule 17a-4(f) obligations, including any required audit trail, serialization/download, third-party undertaking, and production obligations?
3. Under the firm's records schedule, may Priority cleanup ever be used for Copilot-related SharePoint/OneDrive content, and if so, which scenarios are approved: stale Teams recordings/transcripts, departed-user Preservation Hold Library cleanup, unsent Copilot drafts, or none for regulated populations?
4. When a Copilot-generated meeting recap or threaded summary summarizes a regulated business discussion, should the framework classify that summary as an independent books-and-records item, and should the control state that FINRA Rule 4511(c) requirements are met only after tenant evidence proves preservation/export format?
5. Should Copilot memory entries, inferred memories, saved memories, and custom instructions be treated as records when they contain client, investment, supervisory, or financial-analysis context; if yes, must high-risk users disable memory until retention/versioning support is tenant-verified?

## Control 3.6 — Supervision & Oversight

1. Are the specific numeric thresholds (50 supervised users/supervisor, 5%/25%/100% sampling tiers, Series 24/26 designation, 7-year retention, and the FINRA-3110(a)-to-agent-supervision extension) firm-approved compliance policy, or do they need Legal/Compliance sign-off before being presented as a control requirement?

## Control 3.7 — Regulatory Reporting

1. For the institutions this framework targets, which GLBA safeguards regime applies (banking-agency interagency guidelines, FTC Safeguards Rule, SEC Regulation S-P, or another regulator-specific rule), and what exact review cadence and breach-reporting recipient should Control 3.7 state?
2. Which specific CFPB source should this control cite for AI-generated customer-facing content risk: general UDAAP examination procedures, an ECOA/Regulation B complex-algorithm circular, another CFPB AI source, or no CFPB AI-specific citation?
3. As of the current verification date, is there a finalized SEC/Form ADV requirement or firm policy that requires disclosure of AI tool usage in advisory practices, and should Control 3.7 cite Form ADV, soften this to advisory-firm disclosure review, or remove it?
4. For each row in the 3.7 matrix, is the Copilot trigger, timeline, and recipient legally correct for the target FSI entity types, and should the framework present it as a regulatory filing, an internal governance report, or a monitoring/escalation input?

## Control 3.8 — Model Risk Management

1. Does the framework intentionally adopt SR 11-7/OCC 2011-12 principles as a voluntary internal policy derived from historical guidance, despite their supersession/rescission, or does it assert that those principles remain current supervisory guidance for generative AI? If voluntary, authorize wording that distinguishes internal policy from current agency guidance. If current supervisory guidance is intended, counsel/regulatory affairs must provide a current primary source.
2. Are the Tier 1/2/3 mapping, validation cadence, numeric thresholds, and examination package mandatory firm policy, nonbinding examples, or claims about regulator expectations? For each, choose one: (1) approved internal standard and identify the approving governance body; (2) illustrative example and remove `required`, `most common`, `consensus`, and examiner-prediction wording; or (3) regulatory expectation and supply the current primary source.
3. Which approved Copilot use cases actually participate in a credit or housing decision rather than merely drafting text?
4. Which entity types are in scope—bank, broker-dealer, adviser, mortgage lender, or multiple regulated entities?
5. Which FINRA communication category applies to each use case?
6. What source or approved records schedule establishes each five-/seven-year retention period?
7. Should phrases such as `supports compliance` be replaced with non-conclusive language unless counsel has approved them?

## Control 3.9 — AI Disclosure & Transparency

1. Does the firm want Control 3.9 to assert that Copilot-assisted lending, insurance, or advisory uses can be "high-risk systems" or "consequential decisions" under the Colorado AI Act, or should the row be narrowed to "legal to determine applicability" without a control-level conclusion?
2. Should Control 3.9 treat ordinary Copilot-assisted HR drafting or summarization as relevant to the Illinois AI Video Interview Act, or should the row be limited to cases where the firm uses AI analysis of applicant-submitted video interviews?
3. For California AI Transparency Act references, should the control treat SB 942 as a firm-facing disclosure obligation, or as a provider-side obligation that is relevant to Microsoft/vendor due diligence unless counsel identifies deployer-side duties?
4. Should Control 3.9 treat Copilot-assisted HR and employment activities as use of an automated employment decision tool under NYC Local Law 144, or narrow the row to AEDT use cases only?

## Control 3.13 — FFIEC Alignment

1. Which specific primary-source document, if any, should this control cite for interagency AI guidance? If no FFIEC/member-agency guidance document exists under that title, should the control be framed as monitoring for future FFIEC/member-agency AI guidance rather than asserting that joint AI guidance has been issued?

## Control 4.2 — Teams Meetings Governance

1. For Copilot-generated Teams meeting summaries/transcripts and Teams Phone call summaries, should the authoritative retention mapping be (1) SEC 17a-4(b)(4) business communications at 3 years; (2) a 6-year broker-dealer/account-record category under FINRA 4511 or SEC 17a-4(a)/(c)/(e), with the exact subpart named; (3) a 7-year firm/regulator-specific policy, with the actual authority named because `FINRA/SEC extended` was not found in FINRA 4511 or SEC 17a-4; or (4) different durations for meeting transcripts, meeting summaries, call summaries, and DLP evidence?

## Control 4.8 — Cost Allocation and License Optimization

1. Which Copilot cost-allocation controls are firm-internal financial controls versus regulatory requirements for this entity, and when are Microsoft 365 Copilot seats, Copilot pay-as-you-go services, and Copilot Credits spending policies material enough to include in SOX ICFR, OCC operational-risk, FFIEC technology-planning, fiduciary, or client-fee-disclosure evidence?

## Control 4.9 — Incident Reporting and Root Cause Analysis

1. For each Copilot incident category in Control 4.9, which notification sources actually apply to the entity and fact pattern (FINRA 4530, NYDFS 500.17, GLBA/Reg S-P/privacy breach rules, OCC/banking-regulator operational-incident processes, state breach laws, or internal-only escalation), and what recipient, timeline, and approval authority should the firm use?

## Control 4.15 — Copilot Cowork Governance

1. Which Cowork artifacts and actions are records or supervisory materials for this firm: conversations, scheduled prompts, event-driven task runs, browser-task audit records, generated files in OneDrive, uploaded/custom skills, plugins, app-skill outputs, images, and model-selection evidence; and what retention, supervision, and provider data-retention approvals are required before regulated use?

## Control 4.16 — Microsoft Scout Governance

1. Which Scout artifacts and actions are records, supervisory materials, or incident evidence for this firm: local workspace files, shell-command transcripts, browser automation, WorkIQ/Microsoft 365 retrievals, session/memory data in OneDrive, automation instructions, MCP server output, third-party inference content, and GitHub Copilot entitlement records; and which categories require endpoint capture outside Microsoft 365 eDiscovery?
