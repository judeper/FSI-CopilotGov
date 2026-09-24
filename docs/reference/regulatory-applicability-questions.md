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


## Control 3.3 — eDiscovery for Copilot-Generated Content

1. Which Copilot and AI-application artifacts are in scope for each matter type: mailbox-stored prompts/responses, Copilot memory (`IPM.Contact`), Copilot Pages, Copilot Notebooks, Loop components, native files, audit events, or external/generated web-search query logs?
2. Which production formats are approved for Copilot interaction records: PST, individual messages, review-set export package, Microsoft Graph/API output, JSON, native files, redacted PDF, or requester-specific formats?
3. When must legal hold include only the custodian mailbox, and when must it also include SharePoint, OneDrive, Loop, or SharePoint Embedded container URLs?

## Control 3.5 — FINRA 2210 Compliance

1. For each Copilot-assisted communication workflow, which FINRA communication category applies (retail communication, correspondence, institutional communication, public appearance, internal communication, or out of scope), and which principal pre-approval, post-use review, filing, and recordkeeping procedures apply?
2. How should the firm treat SEC AI-washing enforcement precedents in broker-dealer, adviser, and issuer communications about Microsoft 365 Copilot capabilities?
3. Which proposed or pending FINRA/SEC Rule 2210 amendments are being monitored, and which controls must remain under current Rule 2210 until final approval and effective dates are verified?

## Control 3.10 — SEC Reg S-P Privacy

1. Which entity types and customer-information populations are subject to amended SEC Regulation S-P for this deployment, and which compliance date applies to each entity?
2. What contractual evidence confirms the Microsoft service-provider notification process required by Rule 248.30(a)(3), and what internal event starts the firm's 72-hour tracking clock?
3. Which Copilot NPI events require customer notification under the amended Reg S-P standard, and which are internal control incidents only?

## Control 3.11 — Record Keeping

1. For each Copilot artifact category, does the firm approve the audit-trail alternative, third-party WORM archival, or both for SEC Rule 17a-4(f), and what evidence must be preserved for the full retention period?
2. Which Purview audit events are sufficient for the firm's audit-trail alternative position, and where must access-event evidence be preserved separately from modification/deletion audit trail evidence?
3. Which Copilot mobile and browser access channels are approved, blocked, or treated as off-channel risk pending coverage testing?

## Control 3.14 — Copilot Pages and Notebooks Retention and Provenance

1. Which Copilot Pages, Copilot Notebooks, and Loop components are record material under the firm's records schedule, and what retention period applies to each artifact type?
2. Is **All SharePoint Sites** sufficient for the firm's SharePoint Embedded retention scope, or must specific Copilot Pages/Notebooks container URLs be added to policies and holds?
3. What tenant-visible audit evidence is sufficient to reconstruct Page/Notebook lineage and Loop host references, given Microsoft's documented Loop application identity and file-extension-based audit filters?
4. If information barriers are required for a workflow, should Copilot Pages and Copilot Notebooks be disabled because Microsoft documents information barriers as unsupported for SharePoint Embedded content?

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

## Control 2.14 — Declarative and SharePoint Agents Governance

1. For declarative, SharePoint-backed, Agent Builder, and externally published agents, which regulatory citations in Control 2.14 are actually applicable to the firm's entity type and agent use cases, and should the control retain GLBA-only metadata or include FFIEC/OCC references only as internal governance considerations?
2. Which agent events, if any, become firm books-and-records or supervisory-review artifacts: creation requests, sharing approvals, pinned-agent decisions, Agent Registry exports, Agent Map reviews, or agent usage telemetry?
3. Which tenant-specific creation controls are legally/policy required for declarative and SharePoint agents, distinct from Microsoft 365 admin center **User access** controls that govern consumption and installation?

## Control 2.16 — Federated Connector and MCP Governance

1. For each enabled federated connector or MCP server, should the firm classify the vendor or publisher as a third-party service provider under the firm's GLBA, SEC Reg S-P, FFIEC, OCC Bulletin 2023-17, or other third-party-risk framework?
2. If federated connector write/update/delete actions become available in the tenant, do those actions create additional approval, supervision, recordkeeping, DLP, or customer-notification requirements beyond read-only retrieval?
3. Which connector invocation, authentication, and DLP events must be preserved as examination evidence, and what retention period and export format does the firm's records schedule require?

## Control 2.17 — Cross-Tenant Agent Federation

1. Which cross-tenant agent patterns are approved for the firm: externally published Copilot Studio agents, A2A-connected external agents, external MCP servers, Entra Agent ID-backed external agents, or none?
2. For each approved external tenant or counterparty, which regulatory framework drives the required review: GLBA safeguards, SEC Reg S-P, FFIEC information-security expectations, OCC Bulletin 2023-17 third-party risk, FINRA Rule 3110 supervision, or firm-only policy?
3. Which cross-tenant invocation artifacts must be retained or supervised, including A2A payload metadata, full chat-history transfer to external A2A endpoints, external tenant approvals, MCP attestations, and termination evidence?

## Control 4.2 — Teams Meetings Governance

1. For Copilot-generated Teams meeting summaries/transcripts and Teams Phone call summaries, should the authoritative retention mapping be (1) SEC 17a-4(b)(4) business communications at 3 years; (2) a 6-year broker-dealer/account-record category under FINRA 4511 or SEC 17a-4(a)/(c)/(e), with the exact subpart named; (3) a 7-year firm/regulator-specific policy, with the actual authority named because `FINRA/SEC extended` was not found in FINRA 4511 or SEC 17a-4; or (4) different durations for meeting transcripts, meeting summaries, call summaries, and DLP evidence?

## Control 4.13 — Copilot Extensibility and Agent Operations Governance

1. Which extensibility artifacts are regulatory records or examination evidence for the firm: Integrated apps inventory, Agent Registry exports, Agent 365 operational metrics, plugin/tool approvals, MCP requests, Graph connector reviews, Agent Map dependency reviews, A2A endpoint approvals, and decommission records?
2. Where an agent-to-agent chain sends full chat history or structured metadata to an external A2A endpoint, which supervision, vendor-risk, data-residency, DLP, privacy, and recordkeeping reviews are required before enablement?
3. Does the firm apply model-risk management standards to multi-agent orchestration chains, and if yes, which current primary source or internal policy establishes the applicable validation, lineage, and auditability requirements?
