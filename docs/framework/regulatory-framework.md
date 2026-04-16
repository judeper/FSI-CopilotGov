# Regulatory Framework

Comprehensive mapping of framework controls to US financial services regulatory requirements for Microsoft 365 Copilot.

---

## Overview

This document maps the FSI Copilot Governance Framework controls to applicable US financial regulations. Organizations should use this mapping to prioritize control implementation based on their regulatory profile.

!!! warning "Disclaimer"
    This mapping is provided for informational purposes and does not constitute legal or regulatory advice. Regulatory interpretations vary by institution type, use case, and jurisdiction. Consult legal counsel for specific compliance requirements.

!!! info "Emerging International Considerations"
    While the EU AI Act is outside the primary scope of this US-focused framework, Microsoft Purview is expanding AI data lineage tracking capabilities in response to EU AI Act requirements. These capabilities -- including AI interaction provenance and data flow documentation -- may benefit US FSI organizations' own audit and examination readiness posture. Organizations with international operations should monitor how EU AI Act obligations intersect with their US regulatory programs.

---

## Primary US Financial Regulations

### FINRA Rule 4511 -- Books and Records

**Overview:** Requires FINRA member firms to make and preserve books, accounts, records, memoranda, and correspondence in conformity with applicable rules and regulations.

**Key Requirements for M365 Copilot:**

!!! info "SEC 2026 Examination Priorities"
    The SEC Division of Examinations 2026 priorities include a focus on firms' internal use of AI tools, including generative AI. Examiners are expected to evaluate whether firms have adequate policies and procedures governing AI tool deployment, supervisory review of AI outputs, and recordkeeping for AI-assisted activities. Organizations should be prepared to demonstrate their Copilot governance controls during routine examinations.

- Copilot interaction logs constitute business records subject to retention
- Copilot-generated content that becomes part of customer communications or transaction records must be preserved
- Records must be maintained in a format that is readily accessible for the required retention period
- Retention periods vary by record type (see matrix below)

!!! warning "Record Type Matters for Retention"
    Retention periods vary by record type. Copilot interaction logs typically qualify as "communications" with 3-year retention under SEC 17a-4(b)(4), not the 6-year period for financial/customer records. However, if Copilot interactions generate or modify financial records, those outputs follow the applicable 6-year period.

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.1 | Copilot Audit Logging | Capture all Copilot interactions in Unified Audit Log |
| 3.2 | Retention Policies | Retention per record type (3 years communications, 6 years financial records) |
| 3.3 | eDiscovery | Search, export, and produce Copilot records for examination |
| 3.11 | Recordkeeping (SEC 17a-3/4) | Comprehensive record preservation |

**Governance Level Requirements:**

- **Baseline:** Enable Copilot audit logging; apply default M365 retention policies
- **Recommended:** Configure Copilot-specific retention policies aligned to record types; enable eDiscovery for Copilot content
- **Regulated:** WORM-compliant retention for applicable records; 6-year retention for financial records, 3-year for communications (first 2 years readily accessible); documented examination response procedures

---

### Retention Period Matrix

| Record Type | Retention | Regulation | Access Requirement |
|-------------|-----------|------------|--------------------|
| **Communications** (Copilot interaction logs, drafted emails, chat assists) | 3 years | SEC 17a-4(b)(4) | First 2 years readily accessible |
| **Accounting/Financial Records** (Copilot-generated financial analyses, reports) | 6 years | SEC 17a-4(a) | First 2 years readily accessible |
| **Customer Account Records** (Copilot interactions involving customer data) | 6 years after account close | SEC 17a-4(c)(e)(5) | First 2 years readily accessible |
| **FINRA-Specific Records** (no SEC retention period) | 6 years | FINRA 4511(b) | First 2 years easily accessible |
| **Partnership/Corporate Records** | Life of enterprise + 3 years | SEC 17a-4(d) | Readily accessible |
| **Audit Workpapers** | 7 years | SOX 802 | Accessible for examination |

!!! info "Copilot Logs as Communications"
    Copilot interaction logs (prompts, responses, interaction history) typically fall under the 3-year **communications** retention period per SEC 17a-4(b)(4), not the 6-year financial records period. However, if Copilot interactions generate or modify financial records, those outputs follow the applicable 6-year period.

---

### FINRA Rule 3110 -- Supervision

**Overview:** Requires member firms to establish and maintain written supervisory procedures (WSPs) reasonably designed to achieve compliance with applicable securities laws and FINRA rules. This includes supervision of tools and technologies used by associated persons.

**Key Requirements for M365 Copilot:**

1. Written supervisory procedures covering Copilot use by associated persons
2. Qualified supervisor assignment for Copilot-assisted activities
3. Ongoing supervision and review of Copilot outputs
4. Documentation of supervisory activities
5. Annual testing of supervisory control systems (Rule 3120)

**M365 Copilot Application:**

- Copilot is a tool used by associated persons -- existing Rule 3110 obligations apply
- Supervisory procedures must address how Copilot-assisted activities are reviewed
- Sampling protocols for Copilot-drafted communications
- Escalation procedures for identified issues

!!! info "FINRA 2026 Annual Risk Monitoring and Examination Priorities"
    FINRA's 2026 oversight report highlights agentic AI supervision as an emerging examination focus area. As AI tools move from passive assistance to agentic workflows (where AI takes actions on behalf of associated persons), firms must evaluate whether existing supervisory procedures adequately cover AI-initiated actions. Organizations deploying Microsoft 365 Copilot should assess whether agentic features (such as Copilot agents acting on SharePoint content or processing workflows) require enhanced supervisory controls beyond those designed for interactive Copilot use.

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.6 | Supervisory Review (FINRA 3110) | Supervisory procedures for Copilot-assisted activities |
| 3.4 | Communication Compliance | Monitor Copilot-assisted communications |
| 3.5 | FINRA 2210 Communication Review | Review Copilot-drafted customer communications |
| 3.1 | Copilot Audit Logging | Audit trail for supervisory review |
| 3.9 | Regulatory Reporting | Compliance documentation for examination |

**Governance Level Requirements:**

- **Baseline:** User awareness training on Copilot; basic usage guidelines
- **Recommended:** Written supervisory procedures covering Copilot use; supervisory sampling program; quarterly compliance reviews
- **Regulated:** Comprehensive WSPs for Copilot; real-time communication compliance monitoring; documented sampling rates and review procedures; annual testing per Rule 3120; monthly compliance certification

---

### FINRA Rule 2210 -- Communications with the Public

**Overview:** Requires that all member communications with the public be fair, balanced, not misleading, and subject to appropriate supervision. This applies regardless of whether the communication is human-authored or AI-assisted.

**Key Requirements for M365 Copilot:**

- Copilot-drafted customer emails, letters, proposals, and presentations are "correspondence" or "retail communications" under Rule 2210
- All Copilot-assisted customer communications must be fair, balanced, and not misleading
- Principal approval may be required for certain communication types (retail communications)
- Content standards apply equally to AI-generated and human-authored content

!!! info "FINRA Regulatory Notice 24-09"
    FINRA Notice 24-09 (June 2024) confirms that existing FINRA rules apply equally to AI-generated content. The technology used to create a communication does not change the supervisory obligation.

!!! info "SEC v. Delphia and Global Predictions (2024)"
    The SEC's enforcement actions against Delphia Inc. and Global Predictions Inc. established precedent for AI-related enforcement in financial services. Both firms were charged with making misleading claims about their use of AI in investment processes. This precedent reinforces the importance of accurate disclosure when using AI tools like Copilot in client-facing contexts and supervision of AI-generated content to prevent misleading statements.

**Copilot-Specific Concerns:**

| Concern | Risk | Mitigation |
|---------|------|------------|
| **Hallucinated claims** | Copilot may generate performance figures, regulatory citations, or product features that are incorrect | Pre-send review for customer communications |
| **Unbalanced presentation** | Copilot may emphasize benefits without adequate risk disclosure | Communication compliance policies |
| **Promissory language** | Copilot may generate language that implies assured outcomes or promises | Keyword monitoring in communication compliance |
| **Missing disclosures** | Copilot-drafted content may omit required regulatory disclosures | Supervisory review checklists |

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.5 | FINRA 2210 Communication Review | Specific compliance program for Copilot-drafted customer communications |
| 3.4 | Communication Compliance | Automated monitoring for policy violations |
| 3.6 | Supervisory Review | Principal review of applicable communications |
| 3.1 | Copilot Audit Logging | Retain Copilot interaction that generated the communication |

**Governance Level Requirements:**

- **Baseline:** User training on FINRA 2210 obligations when using Copilot
- **Recommended:** Communication compliance policies monitoring Copilot-assisted emails; supervisory sampling program
- **Regulated:** Automated pre-send or post-send review for all Copilot-assisted customer communications; comprehensive keyword policies; documented sampling rates; principal approval workflows

---

### SEC Rules 17a-3 and 17a-4 -- Recordkeeping

**Overview:** Require broker-dealers to make and keep current certain records (17a-3) and to preserve records for specified periods (17a-4). Retention periods vary by record type -- see the Retention Period Matrix above.

**Key Requirements for M365 Copilot:**

- Copilot interactions that constitute or generate business records must be preserved
- Records must be maintained in non-rewritable, non-erasable format (WORM) where applicable
- Records must be readily accessible for the first two years of the retention period
- eDiscovery capabilities must support regulatory examination requests

**Record Categories:**

- **Copilot interaction logs:** Prompts, responses, citations (3 years per SEC 17a-4(b)(4), first 2 years readily accessible)
- **Copilot-generated documents:** If they become transaction records, customer correspondence, or financial reports (retention per record type)
- **Copilot usage metadata:** User activity, feature usage (retain per organizational policy)

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.11 | Recordkeeping (SEC 17a-3/4) | Comprehensive record preservation program |
| 3.1 | Copilot Audit Logging | Capture Copilot interactions as records |
| 3.2 | Retention Policies | Enforce retention per record type |
| 3.3 | eDiscovery | Search, export, produce for examination |

---

### SEC Regulation S-P -- Privacy of Consumer Financial Information

**Overview:** Requires financial institutions to protect the privacy of consumer financial information, provide privacy notices, and allow consumers to opt out of information sharing.

**Key Requirements for M365 Copilot:**

- Copilot must not expose consumer financial information to unauthorized personnel
- Permission governance must prevent Copilot from surfacing PII or account data to users without need-to-know
- Privacy notices must address AI tool usage if consumer data is processed by Copilot

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.10 | Privacy Controls (Reg S-P) | Privacy program for Copilot-processed consumer data |
| 1.1 | Oversharing Assessment | Identify consumer financial data exposure before Copilot |
| 1.2 | Permissions Remediation | Restrict access to consumer data to authorized users |
| 2.1 | DLP Policies | Detect and block consumer financial information in Copilot outputs |
| 2.2 | Sensitivity Labels | Classify consumer financial information |

**Governance Level Requirements:**

- **Baseline:** Basic DLP policies for financial PII; oversharing assessment
- **Recommended:** Comprehensive DLP for consumer financial data; sensitivity labels on consumer records; access reviews
- **Regulated:** Full privacy program for Copilot; documented controls for consumer data protection; privacy impact assessment for Copilot deployment

---

### SEC Regulation Best Interest (Reg BI) -- Best Interest Standard

**Overview:** Requires broker-dealers to act in the best interest of retail customers when making recommendations. This extends to tools used to assist in the recommendation process.

**Key Requirements for M365 Copilot:**

- If Copilot assists in generating investment recommendations or customer advice, the output must meet Reg BI standards
- Copilot-generated content used in customer communications must not be misleading
- Supervisory procedures must address Copilot's role in the recommendation process

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.6 | Supervisory Review | Supervision of Copilot-assisted recommendation processes |
| 3.5 | FINRA 2210 Communication Review | Review of Copilot-drafted recommendations |
| 3.8 | Model Risk Documentation | Documentation of Copilot's role in recommendation workflows |

---

### SOX Sections 302 and 404 -- Internal Controls

**Overview:** Requires public companies to maintain effective internal controls over financial reporting (ICFR). Section 302 requires management certification; Section 404 requires assessment and audit of ICFR effectiveness.

**Key Requirements for M365 Copilot:**

- If Copilot accesses or processes financial reporting data, it becomes part of the ICFR environment
- Access controls must prevent unauthorized Copilot access to financial data
- Change management for Copilot configuration changes affecting financial systems
- Audit trail for Copilot interactions involving financial reporting data

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.12 | SOX Internal Controls Integration | Integrate Copilot governance into ICFR program |
| 3.1 | Copilot Audit Logging | Audit trail for financial data access |
| 1.3 | Least-Privilege Access Review | Access controls for financial data |
| 4.12 | Change Management | Change control for Copilot configuration |

**Governance Level Requirements:**

- **Baseline:** Not applicable (SOX applies only to public companies)
- **Recommended:** Limited scope if Copilot users access financial reporting data
- **Regulated:** Full SOX integration for Copilot controls affecting financial reporting; documented controls, testing, and evidence

!!! info "SOX and AI"
    SOX does not explicitly address AI or automated systems. AI tools affecting financial reporting are governed implicitly through existing ICFR frameworks. The PCAOB is conducting research to determine whether new standards are needed for AI in audits and financial reporting.

---

### GLBA Section 501(b) -- Safeguards Rule

**Overview:** Requires financial institutions to develop, implement, and maintain a comprehensive information security program that includes administrative, technical, and physical safeguards for customer information.

**Key Requirements for M365 Copilot:**

- Copilot deployment must be incorporated into the organization's information security program
- Customer information accessed by Copilot must be protected by appropriate safeguards
- Risk assessment must address Copilot-specific risks (oversharing amplification, web search data flow)
- Service provider oversight must address Microsoft's role in Copilot processing

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 2.1 | DLP Policies | Technical safeguard for customer information |
| 2.2 | Sensitivity Labels | Classification of customer information |
| 2.4 | Conditional Access | Access safeguards for Copilot users |
| 2.11 | Encryption and Rights Management | Encryption for customer data |
| 1.10 | Vendor Risk Assessment | Service provider (Microsoft) oversight |
| 4.5 | Incident Response | Incident response procedures for Copilot-related events |

---

### OCC Bulletin 2011-12 / Federal Reserve SR 11-7 -- Model Risk Management

**Overview:** Provides guidance on model risk management (MRM) for banks using models in decision-making. Requires model validation, ongoing monitoring, governance, and independent validation.

!!! info "OCC Bulletin 2025-26: MRM Proportionality"
    OCC Bulletin 2025-26 reinforces the proportionality principle for model risk management: the rigor of MRM controls should be commensurate with the risk posed by the model's use case. For general-purpose AI productivity tools like M365 Copilot, this means MRM obligations scale with how the tool's outputs are used — casual productivity assistance requires lighter governance than AI-assisted investment recommendations or credit decisions.

**Key Requirements for M365 Copilot:**

Model risk management applicability to M365 Copilot depends on how Copilot outputs are used:

| Use Case | MRM Applicability | Rationale |
|----------|-------------------|-----------|
| General productivity (drafting, summarizing) | Low / Not applicable | Copilot as productivity tool, not decision model |
| Information retrieval for research | Low | Tool for information gathering, human decision-making |
| Drafting customer communications | Moderate | Output directly reaches customers; supervisory review required |
| Assisting investment recommendations | High | Output may influence regulated decisions |
| Generating financial analyses or reports | High | Output may inform financial reporting or risk decisions |
| Credit decision support | High | Fair lending implications; ECOA considerations |

!!! warning "Fair Lending and ECOA"
    If Copilot outputs influence credit decisions, lending processes, or customer treatment decisions, organizations must consider fair lending implications under the Equal Credit Opportunity Act (ECOA) and Fair Housing Act. Even if Copilot is used for research or drafting, biased grounding data could lead to disparate treatment or disparate impact. Banks subject to OCC/Fed supervision should evaluate Copilot use cases against their fair lending compliance program.

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.8 | Model Risk Documentation | Formal MRM alignment for high-impact Copilot use cases |
| 3.7 | CFPB UDAAP Monitoring | Monitor for unfair/deceptive outputs |
| 3.6 | Supervisory Review | Oversight of Copilot-assisted decisions |
| 4.7 | Quality Monitoring | Ongoing monitoring of Copilot output quality |

**Applicability:**

- National banks (OCC)
- State member banks (Federal Reserve)
- State non-member banks (FDIC applies interagency guidance)
- Not directly applicable to broker-dealers or investment advisers (but SEC examination may reference MRM concepts)

**Governance Level Requirements:**

- **Baseline:** Not applicable (MRM typically applies to banks)
- **Recommended:** Awareness documentation of Copilot use cases and MRM implications
- **Regulated:** Formal MRM alignment for high-impact Copilot use cases; documented risk assessment; ongoing monitoring; independent validation where applicable

---

### CFPB UDAAP -- Unfair, Deceptive, or Abusive Acts or Practices

**Overview:** The Consumer Financial Protection Bureau prohibits unfair, deceptive, or abusive acts or practices (UDAAP) by consumer financial service providers.

**Key Requirements for M365 Copilot:**

- Copilot-generated customer communications must not be deceptive or misleading
- AI-assisted outputs used in consumer interactions must be accurate
- Organizations must monitor for Copilot outputs that could cause consumer harm
- Copilot use in consumer-facing contexts must not result in disparate treatment

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.7 | CFPB UDAAP Monitoring | Monitor Copilot outputs for UDAAP risk |
| 3.5 | FINRA 2210 Communication Review | Review customer communications |
| 3.4 | Communication Compliance | Automated monitoring for harmful content |
| 4.7 | Quality Monitoring | Track Copilot output accuracy |

---

### FFIEC IT Examination Handbook

**Overview:** The Federal Financial Institutions Examination Council provides guidance for IT examination of financial institutions, covering information security, business continuity, audit, and vendor management.

**Key Requirements for M365 Copilot:**

- Copilot deployment should be documented in the institution's IT risk assessment
- Vendor management must address Microsoft as the AI service provider
- Business continuity planning should address Copilot availability
- Information security controls must be extended to cover Copilot

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 3.13 | FFIEC Examination Alignment | Align Copilot governance with FFIEC IT Handbook |
| 1.10 | Vendor Risk Assessment | Vendor management for Microsoft Copilot service |
| 4.9 | Business Continuity and DR | BC/DR planning for Copilot |
| 4.5 | Incident Response | Incident response for Copilot-related events |

---

### Interagency AI Guidance (2023)

**Overview:** Joint guidance from OCC, Federal Reserve, FDIC, CFPB, and NCUA on AI risk management for financial institutions. Emphasizes that existing risk management frameworks apply to AI technologies.

**Key Requirements for M365 Copilot:**

- Existing risk management practices apply to AI tool deployment
- Vendor risk management must assess AI capabilities and limitations
- Governance structures must address AI-specific risks
- Ongoing monitoring of AI tool performance is expected

**Applicable Controls:**

| Control | Requirement | Mapping |
|---------|-------------|---------|
| 1.10 | Vendor Risk Assessment | AI vendor risk management |
| 3.8 | Model Risk Documentation | AI governance documentation |
| 4.7 | Quality Monitoring | AI performance monitoring |
| 4.5 | Incident Response | AI-specific incident procedures |

---

### State Laws

The following state regulations may apply but require separate analysis beyond the primary scope of this framework:

#### Colorado AI Act (SB 24-205)

**Overview:** Effective June 2026 (per Colorado SB 25B-004 amendment), requires developers and deployers of "high-risk AI systems" to use reasonable care to protect consumers from known or foreseeable risks of algorithmic discrimination.

**M365 Copilot Relevance:** May apply if Copilot outputs influence consequential decisions (employment, lending, insurance). Organizations operating in Colorado should assess whether their Copilot use cases constitute "high-risk AI" under the Act.

**Applicable Controls:** 3.7 (UDAAP), 3.8 (Model risk), 4.7 (Quality monitoring)

#### NYDFS Part 500 -- Cybersecurity Requirements

**Overview:** New York Department of Financial Services cybersecurity regulation requiring covered entities to maintain a cybersecurity program, conduct risk assessments, and implement specific controls.

**M365 Copilot Relevance:** Copilot deployment must be included in the entity's cybersecurity risk assessment. Access controls, audit logging, and incident response for Copilot must align with Part 500 requirements.

**Applicable Controls:** 2.4 (Conditional access), 2.11 (Encryption), 3.1 (Audit logging), 4.5 (Incident response)

#### CCPA/CPRA -- California Consumer Privacy Act

**Overview:** Provides California consumers with rights regarding their personal information, including the right to know, delete, and opt out of the sale of personal information.

**M365 Copilot Relevance:** If Copilot processes California consumer personal information, the organization must be able to identify, disclose, and delete that information upon request. Copilot interaction logs containing consumer PI may be subject to CCPA access requests.

**Applicable Controls:** 3.10 (Privacy), 3.3 (eDiscovery), 2.1 (DLP)

---

## Regulatory Priority by Institution Type

### Broker-Dealers (FINRA/SEC)

**Primary Regulators:** FINRA, SEC

**Priority Controls:**

| Priority | Control | Regulation | Why |
|----------|---------|------------|-----|
| 1 | 3.5 (FINRA 2210 Communication Review) | FINRA 2210 | Copilot-drafted customer communications |
| 2 | 3.6 (Supervisory Review) | FINRA 3110 | Supervision of Copilot-assisted activities |
| 3 | 3.1 (Copilot Audit Logging) | FINRA 4511, SEC 17a-4 | Books and records for Copilot interactions |
| 4 | 3.2 (Retention Policies) | SEC 17a-4 | Record preservation |
| 5 | 3.4 (Communication Compliance) | FINRA 3110 | Automated supervision tool |

### Banks (OCC/Fed)

**Primary Regulators:** OCC, Federal Reserve, FDIC

**Priority Controls:**

| Priority | Control | Regulation | Why |
|----------|---------|------------|-----|
| 1 | 3.8 (Model Risk Documentation) | OCC 2011-12, SR 11-7 | MRM for high-impact Copilot use cases |
| 2 | 1.1 (Oversharing Assessment) | GLBA §501(b) | Customer information protection |
| 3 | 3.1 (Copilot Audit Logging) | FFIEC | Audit and examination readiness |
| 4 | 2.1 (DLP Policies) | GLBA §501(b) | Technical safeguards |
| 5 | 3.7 (CFPB UDAAP Monitoring) | CFPB UDAAP | Consumer protection |

### Investment Advisers (SEC)

**Primary Regulator:** SEC

**Priority Controls:**

| Priority | Control | Regulation | Why |
|----------|---------|------------|-----|
| 1 | 3.6 (Supervisory Review) | SEC Reg BI | Supervision of Copilot-assisted advice |
| 2 | 3.5 (Communication Review) | SEC Correspondence | Client communication review |
| 3 | 3.1 (Copilot Audit Logging) | SEC 17a-4 | Record preservation |
| 4 | 3.10 (Privacy Controls) | SEC Reg S-P | Client information privacy |
| 5 | 1.1 (Oversharing Assessment) | Fiduciary duty | Client data protection |

### Credit Unions (NCUA)

**Primary Regulator:** NCUA

**Priority Controls:**

| Priority | Control | Regulation | Why |
|----------|---------|------------|-----|
| 1 | 2.1 (DLP Policies) | NCUA Part 748 | Security program |
| 2 | 3.1 (Copilot Audit Logging) | NCUA guidance | Record requirements |
| 3 | 1.1 (Oversharing Assessment) | GLBA §501(b) | Member information protection |
| 4 | 4.5 (Incident Response) | NCUA Part 748 | Security incident procedures |
| 5 | 3.10 (Privacy Controls) | GLBA, NCUA | Member privacy |

---

## Regulation-Level Mapping

### FINRA Examination Focus by Governance Level

| Regulation | Baseline | Recommended | Regulated |
|------------|----------|-------------|-----------|
| FINRA 4511 | Basic logging | Extended retention | Full examination readiness |
| FINRA 3110 | Awareness training | Supervisory sampling | Comprehensive supervision |
| FINRA 2210 | User guidance | Communication compliance | Full review program |

### SEC Examination Focus by Governance Level

| Regulation | Baseline | Recommended | Regulated |
|------------|----------|-------------|-----------|
| SEC 17a-3/4 | Basic retention | Searchable archive | WORM, examination-ready |
| SEC Reg S-P | DLP baseline | Oversharing remediation | Full privacy program |
| SEC Reg BI | N/A | Supervisory controls | Best interest documentation |

### Banking Examination Focus by Governance Level

| Regulation | Baseline | Recommended | Regulated |
|------------|----------|-------------|-----------|
| GLBA §501(b) | Basic safeguards | Comprehensive DLP | Full security program |
| OCC 2011-12 / SR 11-7 | N/A | Awareness docs | Formal MRM alignment |
| FFIEC IT Handbook | Basic controls | IT risk assessment | Full FFIEC alignment |
| Interagency AI Guidance | Awareness | Vendor assessment | Comprehensive AI governance |

---

## Examination Readiness Checklist

### Pre-Examination Preparation

- [ ] Copilot deployment documentation current (scope, users, configuration)
- [ ] Audit logs accessible for required retention period (Control 3.1)
- [ ] Supervisory procedures documented for Copilot use (Control 3.6)
- [ ] Communication compliance policies active and monitored (Control 3.4)
- [ ] DLP policy configuration documented (Control 2.1)
- [ ] Oversharing assessment completed and remediation documented (Control 1.1)
- [ ] Training records current for Copilot governance (Control 4.13)
- [ ] Incident reports filed and accessible (Control 4.5)
- [ ] Governance committee meeting minutes available (Operating Model)

!!! tip "Agent 365 and Entra Agent ID for Examination Readiness"
    Agent 365 and Entra Agent ID introduce new audit and traceability capabilities relevant to regulatory examinations. Entra Agent ID provides a unique, auditable identity for each AI agent, enabling examiners to trace agent actions, data access patterns, and decision workflows. Organizations deploying agents should incorporate agent identity logs and lifecycle records into their examination response artifacts.

### Common Examiner Requests

| Request | Control | Documentation |
|---------|---------|---------------|
| Description of AI tools deployed | 4.1 | Copilot deployment documentation |
| How Copilot accesses customer data | 1.1 | Oversharing assessment, permissions review |
| Supervisory procedures for AI-assisted communications | 3.6 | Written supervisory procedures |
| Copilot audit logs for specific user/date range | 3.1 | Purview Audit export |
| DLP policy configuration and violation reports | 2.1 | Purview DLP reports |
| Communication compliance policy results | 3.4 | Communication compliance dashboard |
| Copilot feature configuration (web search, plugins) | 4.1 | M365 Admin Center settings documentation |
| Training records for Copilot governance | 4.13 | HR/LMS export |
| Incident history related to Copilot | 4.5 | Incident management system |

---

## Framework Coverage Summary

| Regulation | Controls Mapped | Primary Coverage Areas |
|------------|-----------------|----------------------|
| FINRA 4511 | 4 controls | Books and records, retention |
| FINRA 3110 | 5 controls | Supervision, communication compliance |
| FINRA 2210 | 4 controls | Customer communication review |
| SEC 17a-3/4 | 4 controls | Recordkeeping, eDiscovery |
| SEC Reg S-P | 5 controls | Privacy, access governance |
| SEC Reg BI | 3 controls | Supervisory review |
| Sarbanes-Oxley §§302/404 | 4 controls | Internal controls, audit trail |
| GLBA §501(b) | 6 controls | Safeguards, vendor management |
| OCC 2011-12 / SR 11-7 | 4 controls | Model risk management |
| CFPB UDAAP | 4 controls | Consumer protection |
| FFIEC IT Handbook | 4 controls | IT governance, vendor management |
| Interagency AI Guidance | 4 controls | AI risk management |

**Total:** 57 controls across 4 pillars providing mapped coverage to primary US financial regulations.

!!! note
    Coverage indicates which framework controls address aspects of each regulation. Actual compliance requires implementation, validation, ongoing maintenance, and legal counsel review.

---

*FSI Copilot Governance Framework v1.3 - April 2026*
