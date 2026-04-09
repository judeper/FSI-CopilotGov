# FSI Configuration Examples

Four FSI-specific deployment scenarios demonstrating how to apply the governance framework to different institution types. Each example includes a regulatory profile, priority controls, admin toggle recommendations, and DLP policy examples.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. These examples are illustrative and must be adapted to your organization's specific regulatory environment and risk profile. See [full disclaimer](../disclaimer.md).

---

## Example 1: Broker-Dealer Copilot Deployment (FINRA-Focused)

### Regulatory Profile

| Attribute | Detail |
|-----------|--------|
| **Institution type** | Registered broker-dealer |
| **Primary regulators** | FINRA, SEC |
| **Key regulations** | FINRA 4511, 3110, 2210; SEC 17a-3, 17a-4, Reg S-P, Reg BI |
| **Governance level** | Regulated |
| **Risk factors** | Retail communications, supervisory review, MNPI walls, record-keeping |
| **Typical user groups** | Registered representatives, research analysts, investment bankers, compliance, operations |

### Priority Controls (Implementation Order)

| Phase | Controls | Rationale |
|-------|----------|-----------|
| **Phase 1: Pre-deployment** | 1.1 (Copilot Readiness Assessment), 1.2 (SharePoint Oversharing Detection), 1.14 (Item-Level Permission Scanning), 1.15 (Permissions Drift Detection), 1.9 (License Planning), 2.4 (Information Barriers) | Oversharing remediation and MNPI wall enforcement must be in place before any Copilot enablement |
| **Phase 2: Core governance** | 2.2 (Sensitivity Labels), 2.1 (DLP for Copilot), 3.1 (Audit Logging), 3.2 (Retention), 3.4 (Communication Compliance) | Regulatory record-keeping and supervisory review capabilities must be active at enablement |
| **Phase 3: Supervisory** | 3.5 (FINRA 2210), 3.6 (Supervision and Oversight), 3.11 (Record Keeping), 3.3 (eDiscovery) | Supervisory review workflows and record-keeping classification specific to broker-dealer obligations |
| **Phase 4: Operational maturity** | 4.1 (Copilot Admin Settings), 4.6 (Copilot Analytics), 4.11 (Sentinel Integration), 3.8 (Model Risk), 3.12 (Evidence Collection) | Ongoing monitoring, model risk documentation, and examination readiness |

### Admin Toggle Recommendations

| Toggle | Setting | Rationale |
|--------|---------|-----------|
| Web search | **Off** | Prevents external data queries; supports compliance with data handling policies |
| Copilot in Teams meetings | **Only during meeting** | Prevents post-meeting transcript access via Copilot to support MNPI controls |
| Meeting recap with Copilot | **Off** | AI-generated meeting summaries present record-keeping and supervisory review challenges |
| Third-party plugins | **Off** | No third-party plugins until governance review process is established |
| User-deployed plugins | **Off** | Central control over all extensions |
| Graph connectors | **Off** | Disable until each connector is individually approved by compliance |
| User-created agents | **Off** | Central governance over all agent creation |
| Copilot Pages sharing | **Specific people** | Prevents oversharing of AI-generated content |
| Copilot license auto-claim | **Off** | Controlled rollout via group-based assignment |
| Manager insights | **Off** | Privacy considerations for usage monitoring |

### DLP Policy Examples

#### Policy 1: Block Copilot from surfacing customer account numbers

```
Policy name: FSI-BD-DLP-001 - Customer Account Numbers in Copilot
Location: Microsoft 365 Copilot
Conditions:
  - Content contains: Custom SIT "Broker-Dealer Account Number" (regex pattern)
  - Content contains: SIT "US Social Security Number (SSN)"
  - Content contains: SIT "Credit Card Number"
Actions:
  - Block access with override (Confidential content)
  - Block access (Highly Confidential content)
  - Send notification to user with policy tip
  - Generate alert for compliance team
Override: Allow with business justification (Confidential only)
```

#### Policy 2: Block Copilot from surfacing MNPI-labeled content in Microsoft 365 Copilot Chat

```
Policy name: FSI-BD-DLP-002 - MNPI Content Protection
Location: Microsoft 365 Copilot
Conditions:
  - Content has sensitivity label: "MNPI - Restricted"
  - Content has sensitivity label: "MNPI - Deal Related"
Actions:
  - Block access (no override)
  - Generate alert for compliance team
  - Log to audit for FINRA 3110 supervisory review
Note: This policy works in conjunction with Information Barriers.
      IB policies prevent cross-segment access; DLP provides a secondary
      enforcement layer for labeled MNPI content.
```

#### Policy 3: Flag Copilot-drafted retail communications

```
Policy name: FSI-BD-DLP-003 - Retail Communication Monitoring
Location: Microsoft 365 Copilot, Exchange Online
Conditions:
  - Content contains keywords: "recommendation," "should consider,"
    "suitable for," "we suggest," "investment advice"
  - Sender is in group: "Registered Representatives"
  - Recipient is external
Actions:
  - Allow with policy tip: "This communication may require FINRA 2210
    principal pre-approval before sending."
  - Generate alert for supervisory review queue
  - Log interaction for Communication Compliance review
```

### Information Barriers Configuration

```
Segment 1: Investment Banking
  - Attribute: Department = "Investment Banking"
  - Block: Research, Retail Brokerage

Segment 2: Research
  - Attribute: Department = "Research"
  - Block: Investment Banking

Segment 3: Retail Brokerage
  - Attribute: Department = "Retail Brokerage"
  - Block: Investment Banking

Segment 4: Compliance
  - Attribute: Department = "Compliance"
  - Allow: All segments (compliance needs cross-barrier visibility)
```

---

## Example 2: Regional Bank Copilot Deployment (OCC/Fed-Focused)

### Regulatory Profile

| Attribute | Detail |
|-----------|--------|
| **Institution type** | National bank or state-chartered bank |
| **Primary regulators** | OCC (national) or state regulator + Fed/FDIC |
| **Key regulations** | OCC 2011-12 / SR 11-7, GLBA 501(b), FFIEC, SOX 302/404, Interagency AI Guidance 2023 |
| **Governance level** | Recommended to Regulated (depending on asset size) |
| **Risk factors** | Model risk management, consumer data protection, IT examination readiness, third-party AI risk |
| **Typical user groups** | Loan officers, branch operations, commercial banking, treasury, risk management, internal audit |

### Priority Controls (Implementation Order)

| Phase | Controls | Rationale |
|-------|----------|-----------|
| **Phase 1: Pre-deployment** | 1.1 (Copilot Readiness Assessment), 1.11 (Organizational Change Management), 1.10 (Vendor Risk Management), 3.8 (Model Risk Management) | Banking examiners expect vendor risk assessment and model risk documentation before AI deployment |
| **Phase 2: Data protection** | 2.2 (Sensitivity Labels), 2.1 (DLP), 2.3 (Conditional Access), 2.8 (Encryption) | GLBA 501(b) safeguards requirement |
| **Phase 3: Compliance** | 3.1 (Audit Logging), 3.2 (Retention), 3.13 (FFIEC Alignment), 3.10 (SEC Reg S-P) | Examination readiness and regulatory record-keeping |
| **Phase 4: Operations** | 4.6 (Copilot Analytics), 4.9 (Incident Reporting), 4.10 (Business Continuity), 4.11 (Sentinel Integration), 4.12 (Change Management) | Ongoing monitoring and operational resilience |

### Admin Toggle Recommendations

| Toggle | Setting | Rationale |
|--------|---------|-----------|
| Web search | **Off** | Consumer data protection; prevents external queries |
| Copilot in Teams meetings | **During and after meeting** | Less restrictive than broker-dealer; banks typically have fewer MNPI concerns |
| Meeting recap with Copilot | **On** (Recommended) / **Off** (Regulated) | Depends on institution's risk appetite for AI-generated meeting summaries |
| Third-party plugins | **Off** | Maintain control until vendor risk assessment process covers plugins |
| User-deployed plugins | **Off** | Central governance |
| Graph connectors | **Review individually** | May enable connectors for approved internal systems (core banking, CRM) after security review |
| User-created agents | **Off** | Central governance |
| Copilot Pages sharing | **Specific people** | Data minimization |
| Manager insights | **Off** | Employee privacy |

### DLP Policy Examples

#### Policy 1: Protect consumer financial data (GLBA)

```
Policy name: FSI-BANK-DLP-001 - Consumer Financial Data
Location: Microsoft 365 Copilot, Exchange Online, SharePoint, OneDrive
Conditions:
  - Content contains: SIT "US Social Security Number (SSN)"
  - Content contains: SIT "US Bank Account Number"
  - Content contains: SIT "Credit Card Number"
  - Content contains: Custom SIT "Loan Account Number"
Actions:
  - Block with override (Confidential)
  - Block (Highly Confidential)
  - Policy tip: "This interaction involves consumer financial data
    protected under GLBA. Verify recipient authorization."
  - Alert compliance team
```

#### Policy 2: Protect non-public personal information (NPI)

```
Policy name: FSI-BANK-DLP-002 - NPI Protection
Location: Microsoft 365 Copilot
Conditions:
  - Content has sensitivity label: "NPI - Consumer"
  - Content has sensitivity label: "NPI - Loan Data"
Actions:
  - Block access with override (business justification required)
  - Log all overrides for audit trail
  - Alert privacy officer
```

### Model Risk Management Documentation

For OCC 2011-12 / SR 11-7 compliance, document Copilot in the model inventory:

| Field | Value |
|-------|-------|
| Model name | Microsoft 365 Copilot |
| Model type | Third-party LLM (Generative AI) |
| Vendor | Microsoft Corporation |
| Model owner (internal) | [CIO / Head of Technology] |
| Business use cases | Document drafting, email summarization, meeting notes, data analysis assistance |
| Risk tier | [High / Medium — depends on use cases] |
| Validation approach | Vendor documentation review, output sampling, user feedback monitoring |
| Monitoring | DSPM for AI, Unified Audit Log, Copilot usage analytics, Sentinel |
| Last review date | [Date] |
| Next review date | [Date + review cycle] |
| Compensating controls | DLP, sensitivity labels, Conditional Access, user training, supervisory review |

---

## Example 3: Investment Adviser Copilot Deployment (SEC-Focused)

### Regulatory Profile

| Attribute | Detail |
|-----------|--------|
| **Institution type** | SEC-registered investment adviser (RIA) |
| **Primary regulators** | SEC (or state securities regulators for smaller firms) |
| **Key regulations** | SEC Reg S-P, Reg BI (if dual-registered), Investment Advisers Act, SEC 17a-3/4 (if dual-registered), SOX (if publicly held) |
| **Governance level** | Recommended (small/mid RIA) to Regulated (large RIA, dual-registered) |
| **Risk factors** | Client portfolio data, investment recommendations, fiduciary duty, client communications |
| **Typical user groups** | Portfolio managers, research analysts, client relationship managers, compliance, operations |

### Priority Controls (Implementation Order)

| Phase | Controls | Rationale |
|-------|----------|-----------|
| **Phase 1: Pre-deployment** | 1.1 (Copilot Readiness Assessment), 1.2 (SharePoint Oversharing Detection), 1.14 (Item-Level Permission Scanning), 1.9 (License Planning), 1.11 (Organizational Change Management) | Identify where client portfolio data and investment research are stored; remediate oversharing |
| **Phase 2: Data protection** | 2.2 (Sensitivity Labels), 2.1 (DLP), 2.3 (Conditional Access), 3.10 (SEC Reg S-P) | Client data protection is the primary regulatory obligation |
| **Phase 3: Record-keeping** | 3.1 (Audit Logging), 3.2 (Retention), 3.3 (eDiscovery) | SEC examination readiness and record-keeping |
| **Phase 4: Supervision** | 3.6 (Supervision and Oversight — if dual-registered), 3.7 (Regulatory Reporting), 4.6 (Copilot Analytics), 4.9 (Incident Reporting) | Fiduciary duty and operational governance |

### Admin Toggle Recommendations

| Toggle | Setting | Rationale |
|--------|---------|-----------|
| Web search | **Off** | Client data protection |
| Copilot in Teams meetings | **During and after meeting** | Useful for client meeting notes; subject to retention policies |
| Meeting recap with Copilot | **On** | Valuable for documenting client meetings; supports fiduciary duty documentation |
| Third-party plugins | **Off** | Vendor governance |
| User-deployed plugins | **Off** | Central control |
| Graph connectors | **Review** | May enable CRM connector (e.g., Salesforce, Dynamics 365) after security review to allow Copilot to reference client context |
| User-created agents | **Off** | Central governance |
| Copilot Pages sharing | **Specific people** | Client data protection |
| Copilot in Excel | **On with DLP** | Portfolio analysis is a high-value Copilot use case; DLP policies protect client account data |
| Manager insights | **Review** | Smaller firms may find adoption tracking useful |

### DLP Policy Examples

#### Policy 1: Protect client portfolio data

```
Policy name: FSI-RIA-DLP-001 - Client Portfolio Data
Location: Microsoft 365 Copilot, SharePoint, OneDrive
Conditions:
  - Content contains: Custom SIT "Client Account Number"
  - Content contains: Custom SIT "Portfolio Holdings" (keyword-based)
  - Content contains: SIT "US Social Security Number (SSN)"
Actions:
  - Block with override (Confidential — internal use)
  - Block (Highly Confidential — restricted client data)
  - Policy tip: "Client portfolio data detected. Verify this information
    is being used in accordance with Reg S-P and firm policies."
```

#### Policy 2: Flag investment recommendation language

```
Policy name: FSI-RIA-DLP-002 - Investment Recommendation Review
Location: Microsoft 365 Copilot, Exchange Online
Conditions:
  - Content contains keywords: "recommend," "should buy," "should sell,"
    "overweight," "underweight," "target price," "price target"
  - Sender is in group: "Investment Professionals"
  - Recipient is external
Actions:
  - Allow with policy tip: "This communication may contain investment
    recommendations subject to supervisory review."
  - Log for compliance review
```

### Fiduciary Duty Considerations

Investment advisers have a fiduciary duty to act in clients' best interests. Copilot governance for RIAs should address:

1. **Accuracy of AI-assisted recommendations:** Copilot output used in client-facing contexts must be reviewed by a qualified investment professional
2. **Documentation:** Copilot-assisted research and analysis should be documented as part of the investment decision-making record
3. **Client communication review:** Copilot-drafted client communications should be reviewed before sending, particularly for suitability language
4. **Data segregation:** Client data across different relationships should be appropriately segmented (sensitivity labels and site-level permissions)

---

## Example 4: Insurance Company Copilot Deployment

### Regulatory Profile

| Attribute | Detail |
|-----------|--------|
| **Institution type** | Insurance company (life, property/casualty, or health) |
| **Primary regulators** | State insurance departments, NAIC (model laws), potentially SEC (variable products) |
| **Key regulations** | State insurance data privacy laws, NAIC Insurance Data Security Model Law, GLBA 501(b), SOX (if publicly held), state AI regulations |
| **Governance level** | Recommended |
| **Risk factors** | Policyholder PII, claims data, underwriting data, agent communications, state-by-state regulatory variation |
| **Typical user groups** | Underwriters, claims adjusters, agents/producers, actuaries, compliance, customer service |

### Priority Controls (Implementation Order)

| Phase | Controls | Rationale |
|-------|----------|-----------|
| **Phase 1: Pre-deployment** | 1.1 (Copilot Readiness Assessment), 1.11 (Organizational Change Management), 1.9 (License Planning), 1.13 (Extensibility Readiness) | Policyholder data classification and oversharing remediation are foundational |
| **Phase 2: Data protection** | 2.2 (Sensitivity Labels), 2.1 (DLP and Custom SITs), 2.3 (Conditional Access) | Policyholder PII and claims data require strong protection |
| **Phase 3: Compliance** | 3.1 (Audit Logging), 3.2 (Retention), 3.10 (SEC Reg S-P), 3.7 (Regulatory Reporting — if applicable) | Record-keeping and privacy compliance |
| **Phase 4: Operations** | 4.1 (Copilot Admin Settings), 4.2 (Teams Meetings Governance), 4.6 (Copilot Analytics), 4.9 (Incident Reporting), 4.12 (Change Management) | Operational governance and change management |

### Admin Toggle Recommendations

| Toggle | Setting | Rationale |
|--------|---------|-----------|
| Web search | **Off** | Policyholder data protection |
| Copilot in Teams meetings | **During and after meeting** | Claims discussions and underwriting meetings benefit from meeting notes |
| Meeting recap with Copilot | **On** | Useful for claims and underwriting documentation |
| Third-party plugins | **Off** | Until governance review process is established |
| User-deployed plugins | **Off** | Central control |
| Graph connectors | **Review** | May enable connectors for policy administration and claims management systems after review |
| User-created agents | **Off** | Central governance |
| Copilot Pages sharing | **Specific people** | Policyholder data protection |
| Copilot in Word | **On** | High-value use case for policy document drafting and claims correspondence |
| Copilot in Outlook | **On** | Agent and customer communications with DLP enforcement |
| Manager insights | **Review** | May be appropriate for regional manager oversight |

### DLP Policy Examples

#### Policy 1: Protect policyholder PII

```
Policy name: FSI-INS-DLP-001 - Policyholder PII
Location: Microsoft 365 Copilot, Exchange Online, SharePoint, OneDrive
Conditions:
  - Content contains: SIT "US Social Security Number (SSN)"
  - Content contains: SIT "US Driver's License Number"
  - Content contains: Custom SIT "Policy Number"
  - Content contains: Custom SIT "Claim Number"
  - Content contains: SIT "Health/Medical terms" (for health insurance)
Actions:
  - Block with override (Confidential)
  - Block (Highly Confidential)
  - Policy tip: "Policyholder personally identifiable information
    detected. Handle in accordance with state privacy requirements."
  - Alert compliance team
```

#### Policy 2: Protect claims data

```
Policy name: FSI-INS-DLP-002 - Claims Data Protection
Location: Microsoft 365 Copilot
Conditions:
  - Content has sensitivity label: "Claims - Confidential"
  - Content has sensitivity label: "Claims - Litigation Hold"
Actions:
  - Block with override for "Claims - Confidential" (requires justification)
  - Block (no override) for "Claims - Litigation Hold"
  - Alert claims compliance team
```

#### Policy 3: Protect underwriting data

```
Policy name: FSI-INS-DLP-003 - Underwriting Data
Location: Microsoft 365 Copilot, SharePoint
Conditions:
  - Content contains keywords: "mortality table," "risk score,"
    "underwriting decision," "medical history," "actuarial"
  - Content has sensitivity label: "Underwriting - Restricted"
Actions:
  - Block with override (business justification required)
  - Log for audit trail
  - Alert underwriting compliance
```

### State Regulatory Considerations

Insurance companies face unique challenges due to state-by-state regulatory variation:

| Consideration | Impact on Copilot Governance |
|---------------|------------------------------|
| **NAIC Insurance Data Security Model Law** | Adopted by most states; requires comprehensive information security program similar to GLBA. Copilot governance controls help address these requirements. |
| **State privacy laws** (e.g., CCPA/CPRA, NYDFS Cybersecurity Regulation) | Some states have specific requirements for AI use in insurance decisions. Review state-specific obligations before enabling Copilot in underwriting or claims contexts. |
| **NYDFS Cybersecurity Regulation (23 NYCRR 500)** | Requires risk assessments for new technology deployments, access controls, audit trails, and incident response. Copilot deployment should be included in the 23 NYCRR 500 risk assessment. |
| **State AI regulations** | Multiple states are enacting or considering AI-specific regulations for insurance (particularly in underwriting and claims). Monitor state legislative developments. |
| **Market conduct examinations** | State examiners may review AI usage in customer-facing processes. Audit logging and communication monitoring help support examination readiness. |

---

## Configuration Comparison Summary

| Setting | Broker-Dealer | Regional Bank | Investment Adviser | Insurance Company |
|---------|--------------|---------------|-------------------|-------------------|
| Governance level | Regulated | Recommended-Regulated | Recommended-Regulated | Recommended |
| Web search | Off | Off | Off | Off |
| Information Barriers | Required (MNPI) | Situational | Situational | Not typically required |
| Communication Compliance | Required (FINRA 3110) | Optional | Situational (dual-reg) | Optional |
| Meeting recap | Off | Situational | On | On |
| Third-party plugins | Off | Off | Off | Off |
| Graph connectors | Off | Review individually | Review individually | Review individually |
| User-created agents | Off | Off | Off | Off |
| Model risk documentation | Required (may apply) | Required (OCC/SR 11-7) | Optional | Optional |
| Key DLP focus | MNPI, account numbers, communications | Consumer NPI, loan data | Client portfolio, recommendations | Policyholder PII, claims, underwriting |
| Primary record-keeping | FINRA 4511, SEC 17a-4 | GLBA, SOX, FFIEC | SEC rules, Reg S-P | State laws, NAIC Model Law |

---

*FSI Copilot Governance Framework v1.3 - April 2026*
