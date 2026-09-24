<!-- Educational reference only — not legal advice. Firms should resolve these questions with qualified counsel and compliance owners. -->

# Regulatory Applicability Questions

This appendix captures open applicability questions that each firm should resolve with counsel, compliance, records-management, model-risk, and business owners before treating the framework's regulatory references as applicable to its environment.

!!! warning "Firm/counsel determination"
    Regulatory citations identify commonly referenced requirements. Applicability, record classification, supervisory-source mapping, and retention periods are a firm and counsel determination. This framework does not assert that any regulation applies or is satisfied.

---

## Control 1.6 — Permission Model Audit

1. Which Microsoft 365 workloads and user populations require Copilot-specific permission-audit evidence under the firm's counsel-approved interpretations of GLBA §501(b), Sarbanes-Oxley §§302/404 where applicable to ICFR, the FFIEC IT Examination Handbook (Access Control), SEC Regulation S-P, FINRA Rule 3110, or internal least-privilege policy?
2. For current Microsoft Purview DSPM and AI-specific roles, should the firm treat Data Security Viewer, Purview Data Security AI Viewer, Purview Data Security AI Content Viewer, Content Explorer Content Viewer, Data Security AI Admins, and AI Administrator assignments as regulatory evidence, internal governance evidence, or both?
3. What firm-approved exception process, if any, permits the same person to hold Data Security AI Admins membership and AI Content Viewer / Content Explorer Content Viewer access?
4. What access-revocation deadline and evidence standard apply to terminated employees, contractors, vendors, regulators, examiners, and other guest users whose stale permissions Copilot would inherit?

## Control 1.7 — SharePoint Advanced Management Readiness for Copilot

1. Which SAM outputs should be retained as evidence for customer-information safeguards, technology-risk governance, privacy controls, or ICFR access certification under the firm's counsel-approved interpretations of GLBA §501(b), the FFIEC IT Examination Handbook (Information Security), Sarbanes-Oxley §§302/404, SEC Regulation S-P, or internal policy?
2. For sites containing material non-public information (MNPI), non-public personal information (NPI), regulatory examination materials, enforcement actions, consent orders, or examination responses, should Restricted Content Discovery, Restricted Access Control, or both be mandatory before the site is included in Copilot grounding scope?
3. Where records owners determine FINRA 4511, SEC 17a-4, or an institution-specific retention schedule applies, what approval is required before SAM site lifecycle management archives, deletes, or remediates a site?
4. What cadence and recipient list should apply to DAG reports, Content Management Assessment results, AI insights, SharePoint Admin Agent prompts, RAC/RCD configuration evidence, and site access review completion evidence?

## Control 1.8 — Information Architecture Review

1. Which customer, financial-reporting, supervisory, books-and-records, or consumer-financial-information content classes require information-architecture evidence before they are included in Copilot grounding scope under the firm's counsel-approved interpretations of GLBA §501(b), the FFIEC IT Handbook (Information Security), Sarbanes-Oxley §§302/404, SEC Regulation S-P, FINRA Rule 4511, or internal policy?
2. What approval standard should apply before Copilot in SharePoint-generated sites, libraries, public views, or autofill metadata columns are treated as authoritative governance metadata?
3. Is the ≥80% metadata population target an approved firm standard for key libraries, an illustrative benchmark, or a threshold that should vary by content class and business line?
4. Which legacy, stale, duplicated, migrated, or ad-hoc SharePoint/Teams content repositories must be remediated, archived, or excluded before Copilot is enabled for regulated populations?

## Control 2.4 — Information Barriers for Copilot

1. Which specific business populations and workflows require ethical-wall / Chinese Wall controls for Copilot under firm policy and counsel-approved interpretations of SEC Rule 10b-5, FINRA Rules 5280/2241/2242, SEC Regulation AC, or other applicable obligations?
2. For each approved Copilot surface, what tenant evidence is sufficient to prove that SharePoint, OneDrive, Teams, and other workload boundaries prevent barrier-separated content from grounding Copilot responses?
3. Because Microsoft documents that Information Barriers are not supported for Channel Agent in Teams, what firm-approved deployment rule applies: disable Channel Agent for IB-sensitive populations, allow only homogeneous-segment channels after membership audit, or another counsel-approved control?
4. Because Microsoft documents that Information Barriers are not supported for SharePoint Embedded content used by Copilot Pages and Copilot Notebooks, should those surfaces be disabled or restricted for IB-sensitive populations?
5. Because Microsoft documents that Information Barriers do not restrict Exchange Online email communication, what approved email control (for example, Exchange mail flow rules or supervisory procedure) covers Copilot-assisted email scenarios where the firm's wall design requires email separation?

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

## Control 4.2 — Teams Meetings Governance

1. For Copilot-generated Teams meeting summaries/transcripts and Teams Phone call summaries, should the authoritative retention mapping be (1) SEC 17a-4(b)(4) business communications at 3 years; (2) a 6-year broker-dealer/account-record category under FINRA 4511 or SEC 17a-4(a)/(c)/(e), with the exact subpart named; (3) a 7-year firm/regulator-specific policy, with the actual authority named because `FINRA/SEC extended` was not found in FINRA 4511 or SEC 17a-4; or (4) different durations for meeting transcripts, meeting summaries, call summaries, and DLP evidence?

## Control 4.3 — Teams Phone and Queues Governance

1. For Teams Phone calls, call transfers, Teams Phone Agent conversations, and Copilot Studio voice-agent handoffs, which artifacts are records under the firm's approved records schedule: recordings, transcripts, Copilot recaps, transfer summaries, prompts/responses, queue reports, and voice-agent transcripts?
2. Which consent notices, caller disclosures, and jurisdiction-specific call recording/transcription requirements apply before enabling `EnabledWithTranscript`, cloud recording, Teams Phone Agent, or Copilot Studio voice-agent workflows for client-facing populations?
3. May any AI-generated call summary supplement the authoritative call record, and if so what human review, sampling, and retention evidence are required before using it in supervisory workflows?

## Control 4.4 — Viva Suite Governance

1. Which employee-analytics, labor, privacy, works-council, or employment-law reviews are required before enabling Copilot Analytics, Viva Engage Copilot, Learning Agent, Viva Pulse, or Viva Glint Copilot features for regulated, HR, legal, compliance, or internal-audit populations?
2. Are Copilot Analytics, Viva Pulse, or Viva Glint sentiment outputs approved for management action, or only for aggregate governance reporting after human review?
3. Which historical Viva Goals records, if any, must be retained after the December 31, 2025 retirement, and which successor system is authoritative for OKR or compliance milestone evidence?

## Control 4.5 — Usage Analytics and Adoption Reporting

1. Which Copilot usage and adoption reports may be used as official governance evidence, and which are directional operational reports only?
2. May identifiable Copilot usage exports be used for supervisory, compliance, HR, or performance-management purposes, and which approvals and access controls are required?
3. Which populations are intentionally excluded from Graph Copilot usage-detail APIs, admin-center reports, Copilot Chat reports, Agent Dashboard, or Consumption Dashboard, and how should those exclusions be disclosed in committee reporting?

## Control 4.6 — Viva Insights Measurement

1. Which Copilot impact, sentiment, benchmark, intelligent-summary, and business-impact metrics are approved for board or committee reporting, and which require caveats that they are directional rather than proof of ROI or control effectiveness?
2. What minimum group size, attribute filtering, role access, and export controls are required before analysts can view group-level Copilot impact data?
3. Which uploaded business outcome data may be combined with Copilot Analytics, and who approves the methodology before any causal or financial-benefit claim is made?

## Control 4.7 — Feedback and Telemetry Data Governance

1. Should regulated populations be allowed to submit verbatim Microsoft feedback, screenshots, attachments, logs, content samples, or follow-up contact information, and what redaction/monitoring controls apply?
2. Which diagnostic data level and connected-experience settings are approved for Copilot users, and how should exceptions be documented?
3. Are Copilot feedback, diagnostic, usage-reporting, and telemetry exports part of the firm's privacy impact assessment, vendor inventory, or employee monitoring notice obligations?

## Control 4.8 — Cost Allocation and License Optimization

1. Which Copilot cost-allocation controls are firm-internal financial controls versus regulatory requirements for this entity, and when are Microsoft 365 Copilot seats, Copilot pay-as-you-go services, and Copilot Credits spending policies material enough to include in SOX ICFR, OCC operational-risk, FFIEC technology-planning, fiduciary, or client-fee-disclosure evidence?

## Control 4.9 — Incident Reporting and Root Cause Analysis

1. For each Copilot incident category in Control 4.9, which notification sources actually apply to the entity and fact pattern (FINRA 4530, NYDFS 500.17, GLBA/Reg S-P/privacy breach rules, OCC/banking-regulator operational-incident processes, state breach laws, or internal-only escalation), and what recipient, timeline, and approval authority should the firm use?

## Control 4.13 — Copilot Extensibility and Agent Operations Governance

1. Which Agent 365, Agent Registry, Agents > Tools, Integrated apps, Graph connector, and Work IQ operational signals are approved examination evidence for the firm's extensibility governance program?
2. Which agent metrics may be used for formal governance reporting before Agent 365 has accumulated a complete 30-day baseline after license activation, and how should metric incompleteness be disclosed?
3. Which plugin, MCP server, Work IQ, or external-publisher components constitute third-party relationships under the firm's third-party risk policy, and what reassessment cadence applies to each?
4. For Work IQ or federated/MCP tools with write capability, what operational evidence is required for approval, user confirmation, auditability, rollback, and ongoing supervision?

## Control 4.15 — Copilot Cowork Governance

1. Which Cowork artifacts and actions are records or supervisory materials for this firm: conversations, scheduled prompts, event-driven task runs, browser-task audit records, generated files in OneDrive, uploaded/custom skills, plugins, app-skill outputs, images, and model-selection evidence; and what retention, supervision, and provider data-retention approvals are required before regulated use?

## Control 4.16 — Microsoft Scout Governance

1. Which Scout artifacts and actions are records, supervisory materials, or incident evidence for this firm: local workspace files, shell-command transcripts, browser automation, WorkIQ/Microsoft 365 retrievals, session/memory data in OneDrive, automation instructions, MCP server output, third-party inference content, and GitHub Copilot entitlement records; and which categories require endpoint capture outside Microsoft 365 eDiscovery?
