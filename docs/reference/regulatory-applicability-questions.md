<!-- Educational reference only — not legal advice. Firms should resolve these questions with qualified counsel and compliance owners. -->

# Regulatory Applicability Questions

This appendix captures open applicability questions that each firm should resolve with counsel, compliance, records-management, model-risk, and business owners before treating the framework's regulatory references as applicable to its environment.

!!! warning "Firm/counsel determination"
    Regulatory citations identify commonly referenced requirements. Applicability, record classification, supervisory-source mapping, and retention periods are a firm and counsel determination. This framework does not assert that any regulation applies or is satisfied.

---

## Control 2.14 — Declarative and SharePoint Agents Governance

1. Which regulatory citations, if any, should the firm treat as directly applicable to declarative agents and SharePoint-backed agents in its environment, and which should remain contextual governance considerations only?
2. For SharePoint-backed agents that surface customer NPI, MNPI, or regulated records, what firm-approved evidence proves that source-site permissions, labels, sharing posture, and agent audience controls satisfy the firm's safeguard and supervisory requirements?
3. Should Entra Agent ID and Conditional Access for agents be mandatory internal requirements for any broadly shared or high-risk declarative agent, or only tenant-verified optional controls where licensing and product support are available?
4. If third-party model-provider settings or external-publisher agents are available in the tenant, what approval, data-residency, and vendor-risk evidence is required before any such provider or agent can process firm data?

## Control 2.16 — Federated Connector and MCP Governance

1. For federated connector data retrieved in real time through the user's identity, which regulatory obligations does the firm consider triggered: third-party risk, customer-information safeguards, books-and-records, privacy, data residency, information barriers, or none without a specific use case?
2. What firm-approved evidence is required to show that **Allowed agent types**, connector-specific allowed-user scope, staged rollout, and controlled end-user tests prove effective connector access posture?
3. Before enabling create, update, or delete tools for federated connectors, what approvals are required for write-capable third-party actions, explicit user confirmation, audit retention, source-system rollback, and segregation-of-duties review?
4. For Work IQ MCP in Copilot Studio, does the firm permit preview usage, usage-based billing, and administrator-enabled write operations; if yes, what risk acceptance, spending policy, data-classification, and supervision evidence is required?

## Control 2.17 — Cross-Tenant Agent Federation

1. Which external-agent patterns are in scope for this control in the firm's tenant: Entra Agent ID-backed agents, BYO MCP servers, Copilot Studio A2A endpoints, externally published agents, or another pattern?
2. For each in-scope pattern, which tenant control is legally and operationally authoritative for permit/block decisions, and what evidence proves that CTAP, Agent Registry, Agents > Tools, Copilot Studio, or another surface actually controls that pattern?
3. When an external A2A endpoint receives full chat history or structured conversation metadata, what data-residency, privacy, confidentiality, records-retention, and vendor-risk obligations does the firm apply?
4. What termination evidence is required to prove that an external tenant or endpoint no longer has residual access after a counterparty relationship ends?

## Control 4.13 — Copilot Extensibility and Agent Operations Governance

1. Which Agent 365, Agent Registry, Agents > Tools, Integrated apps, Graph connector, and Work IQ operational signals are approved examination evidence for the firm's extensibility governance program?
2. Which agent metrics may be used for formal governance reporting before Agent 365 has accumulated a complete 30-day baseline after license activation, and how should metric incompleteness be disclosed?
3. Which plugin, MCP server, Work IQ, or external-publisher components constitute third-party relationships under the firm's third-party risk policy, and what reassessment cadence applies to each?
4. For Work IQ or federated/MCP tools with write capability, what operational evidence is required for approval, user confirmation, auditability, rollback, and ongoing supervision?

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
