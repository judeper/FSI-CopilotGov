# Regulatory Mappings

Complete regulation-to-control mapping table for the FSI Copilot Governance Framework. Use this reference to identify which controls support compliance with each regulatory requirement.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. Each institution should work with qualified legal counsel to validate applicability of these mappings to their specific regulatory environment. See [full disclaimer](../disclaimer.md).

---

## How to Use This Reference

- **Preparing for an examination?** Find your regulator's rules below, then review the linked controls for implementation status.
- **Building a compliance matrix?** Export the tables below into your GRC tool and map to your internal control IDs.
- **Prioritizing implementation?** Controls appearing across multiple regulations should be prioritized first.

**Governance Levels:** B = Baseline | R = Recommended | Reg = Regulated

---

## FINRA Rule 4511 — Books and Records

Requires member firms to make and preserve books and records as prescribed by FINRA rules and the Exchange Act.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| 4511(a) | Make and preserve books, accounts, records, memoranda, and correspondence | Control 3.1 (Copilot Audit Logging), Control 3.2 (Retention Policies), Control 3.11 (Regulatory Record-keeping) | B / Reg |
| 4511(b) | Retain records for prescribed periods (6 years for general records, 3 years for certain communications) | Control 3.2 (Retention Policies), Control 3.11 (Regulatory Record-keeping) | Reg |
| 4511(c) | Records must be readily accessible for first 2 years | Control 3.1 (Copilot Audit Logging), Control 3.3 (eDiscovery) | R |
| 4511(d) | Electronic storage media must meet non-rewriteable, non-erasable requirements (WORM) | Control 3.2 (Retention Policies), Control 3.11 (Regulatory Record-keeping) | Reg |

---

## FINRA Rule 3110 — Supervision

Requires each member firm to establish, maintain, and enforce a system to supervise the activities of associated persons.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| 3110(a) | Establish and maintain written supervisory procedures | Control 3.6 (Supervisory Review Procedures), Control 1.12 (Governance Committee) | Reg |
| 3110(b) | Designate supervisory principals for each type of business | Control 4.13 (Stakeholder RACI Matrix), Control 3.6 (Supervisory Review) | Reg |
| 3110(b)(4) | Review of communications with the public | Control 3.4 (Communication Compliance), Control 3.5 (FINRA 2210), Control 3.6 (Supervisory Review) | Reg |
| 3110(d) | Review of customer account activity | Control 3.1 (Copilot Audit Logging), Control 4.6 (Usage Analytics) | R |

---

## FINRA Rule 2210 — Communications with the Public

Governs retail communications, correspondence, and institutional communications including content standards.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| 2210(a) | Classification of communications (retail, correspondence, institutional) | Control 3.5 (FINRA 2210 Compliance), Control 2.1 (Sensitivity Labels) | Reg |
| 2210(b) | Approval and review requirements — principal pre-approval for retail communications | Control 3.5 (FINRA 2210 Compliance), Control 3.6 (Supervisory Review) | Reg |
| 2210(d) | Content standards — fair, balanced, not misleading | Control 3.5 (FINRA 2210 Compliance), Control 3.4 (Communication Compliance) | Reg |
| 2210(d)(1) | No false, exaggerated, unwarranted, or misleading statements | Control 3.5 (FINRA 2210 Compliance), Control 3.7 (UDAAP Compliance) | Reg |

---

## SEC Rule 17a-3 — Records to be Made

Requires broker-dealers to create and maintain specified records relating to their business.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| 17a-3(a)(6) | Memorandum of each order including terms and conditions | Control 3.11 (Regulatory Record-keeping), Control 3.1 (Audit Logging) | Reg |
| 17a-3(a)(7) | Memorandum of each purchase and sale of a security | Control 3.11 (Regulatory Record-keeping) | Reg |
| 17a-3(a)(17) | Records of written communications relating to the business | Control 3.4 (Communication Compliance), Control 3.11 (Record-keeping) | Reg |
| 17a-3(a)(25) | Records of written supervisory procedures and reviews | Control 3.6 (Supervisory Review), Control 3.12 (Audit Evidence) | Reg |

---

## SEC Rule 17a-4 — Records to be Preserved

Specifies record retention periods and storage requirements for broker-dealer records.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| 17a-4(a) | Records preserved for not less than 6 years | Control 3.2 (Retention Policies), Control 3.11 (Record-keeping) | Reg |
| 17a-4(b) | Records preserved for not less than 3 years (communications) | Control 3.2 (Retention Policies), Control 3.4 (Communication Compliance) | Reg |
| 17a-4(f) | Electronic storage media requirements — WORM compliance | Control 3.2 (Retention Policies), Control 3.11 (Record-keeping) | Reg |
| 17a-4(j) | Third-party access and SEC examination access | Control 3.3 (eDiscovery), Control 3.12 (Audit Evidence) | Reg |

---

## SEC Regulation S-P — Privacy of Consumer Financial Information

Requires broker-dealers, investment companies, and investment advisers to protect consumer financial information.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| 248.30(a) | Policies and procedures to protect customer records and information | Control 3.10 (Privacy and Reg S-P), Control 2.4 (DLP Policies), Control 2.13 (Encryption) | R |
| 248.30(a) | Protection against unauthorized access or use | Control 2.7 (Conditional Access), Control 2.8 (Information Barriers), Control 1.1 (Oversharing Assessment) | R / Reg |
| 248.30(b) | Disposal of consumer information | Control 3.2 (Retention Policies), Control 1.7 (Content Lifecycle) | R |

---

## SEC Regulation Best Interest (Reg BI)

Requires broker-dealers to act in the best interest of retail customers when recommending securities or investment strategies.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| 240.15l-1(a)(1) | Disclosure obligation | Control 3.5 (FINRA 2210), Control 3.7 (UDAAP Compliance) | Reg |
| 240.15l-1(a)(2)(ii) | Care obligation — reasonable diligence, care, and skill | Control 3.6 (Supervisory Review), Control 3.8 (Model Risk Management) | Reg |
| 240.15l-1(a)(2)(iii) | Conflict of interest obligation | Control 2.8 (Information Barriers), Control 3.6 (Supervisory Review) | Reg |
| 240.15l-1(a)(2)(iv) | Compliance obligation — policies and procedures | Control 1.12 (Governance Committee), Control 4.12 (Governance Calendar) | Reg |

---

## Sarbanes-Oxley Act (SOX) Sections 302 and 404

Requires public companies to maintain internal controls over financial reporting.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| SOX 302 | CEO/CFO certification of financial reports and internal controls | Control 3.1 (Audit Logging), Control 3.12 (Audit Evidence), Control 4.13 (RACI Matrix) | Reg |
| SOX 404 | Management assessment of internal controls; auditor attestation | Control 3.1 (Audit Logging), Control 3.12 (Audit Evidence), Control 2.4 (DLP), Control 2.13 (Encryption) | Reg |
| SOX 404 | Change management controls | Control 4.10 (Change Management), Control 4.1 (Feature Toggle Management) | R |

---

## GLBA Section 501(b) — Safeguards Rule

Requires financial institutions to develop, implement, and maintain a comprehensive information security program.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| 501(b) | Protect security and confidentiality of customer records | Control 2.1 (Sensitivity Labels), Control 2.4 (DLP), Control 2.13 (Encryption), Control 2.7 (Conditional Access) | B / R |
| 501(b) | Protect against anticipated threats or hazards | Control 2.10 (Defender Integration), Control 2.11 (Insider Risk), Control 4.8 (Incident Response) | R |
| 501(b) | Protect against unauthorized access or use | Control 1.1 (Oversharing Assessment), Control 1.2 (Permissions Review), Control 2.7 (Conditional Access) | B |

---

## OCC Bulletin 2011-12 / Fed SR 11-7 — Model Risk Management

Provides guidance on model risk management for banking organizations.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| Model Identification | Identify and inventory all models | Control 3.8 (Model Risk Management) | Reg |
| Model Validation | Independent review and validation | Control 3.8 (Model Risk Management), Control 3.12 (Audit Evidence) | Reg |
| Ongoing Monitoring | Monitor model performance and outcomes | Control 4.6 (Usage Analytics), Control 3.9 (DSPM for AI), Control 4.11 (Sentinel Integration) | Reg |
| Model Governance | Board and senior management oversight | Control 1.12 (Governance Committee), Control 4.13 (RACI Matrix) | Reg |
| Documentation | Maintain comprehensive model documentation | Control 3.8 (Model Risk Management), Control 3.12 (Audit Evidence) | Reg |
| Vendor Models | Assess third-party model risk | Control 1.10 (Vendor Risk Assessment), Control 3.8 (Model Risk Management) | Reg |

---

## CFPB UDAAP — Unfair, Deceptive, or Abusive Acts or Practices

Prohibits unfair, deceptive, or abusive acts or practices by covered persons in consumer financial products or services.

| Section | Requirement | Applicable Controls | Level |
|---------|-------------|-------------------|-------|
| Unfair Acts | Acts that cause substantial injury not reasonably avoidable | Control 3.7 (UDAAP Compliance), Control 3.8 (Model Risk Management) | Reg |
| Deceptive Acts | Material misleading representations or omissions | Control 3.7 (UDAAP Compliance), Control 3.5 (FINRA 2210), Control 3.4 (Communication Compliance) | Reg |
| Abusive Acts | Acts that take unreasonable advantage of consumer understanding | Control 3.7 (UDAAP Compliance), Control 3.6 (Supervisory Review) | Reg |
| AI and UDAAP | CFPB guidance on AI-generated consumer communications | Control 3.7 (UDAAP Compliance), Control 3.8 (Model Risk Management), Control 1.13 (Training) | Reg |

---

## FFIEC IT Examination Handbook

Interagency guidance for IT examination of financial institutions.

| Domain | Requirement | Applicable Controls | Level |
|--------|-------------|-------------------|-------|
| Audit | IT audit program covering AI tools | Control 3.1 (Audit Logging), Control 3.12 (Audit Evidence), Control 3.13 (FFIEC Alignment) | Reg |
| Information Security | Controls over AI-generated content and data access | Control 2.4 (DLP), Control 2.7 (Conditional Access), Control 2.13 (Encryption) | R |
| Management | IT governance including AI adoption | Control 1.12 (Governance Committee), Control 4.13 (RACI Matrix), Control 3.13 (FFIEC Alignment) | Reg |
| Operations | Operational resilience for AI services | Control 4.8 (Incident Response), Control 4.9 (Business Continuity), Control 3.13 (FFIEC Alignment) | R |
| Development and Acquisition | Vendor management for AI services | Control 1.10 (Vendor Risk Assessment), Control 3.13 (FFIEC Alignment) | Reg |
| Business Continuity | Continuity planning for AI service disruption | Control 4.9 (Business Continuity), Control 3.13 (FFIEC Alignment) | R |

---

## Interagency AI Guidance (2023) — OCC, Fed, FDIC

Joint guidance on managing risks associated with AI in financial services, including third-party AI models.

| Topic | Requirement | Applicable Controls | Level |
|-------|-------------|-------------------|-------|
| Risk Management | Incorporate AI risk into enterprise risk framework | Control 3.8 (Model Risk Management), Control 1.12 (Governance Committee) | Reg |
| Governance | Board and management oversight of AI adoption | Control 1.12 (Governance Committee), Control 4.13 (RACI Matrix), Control 4.12 (Governance Calendar) | Reg |
| Third-Party Risk | Assess and monitor third-party AI providers | Control 1.10 (Vendor Risk Assessment) | Reg |
| Data Management | Controls over data used in AI systems | Control 1.1 (Oversharing Assessment), Control 1.11 (Data Classification), Control 2.4 (DLP) | R |
| Consumer Protection | Protect consumers from AI-related harm | Control 3.7 (UDAAP Compliance), Control 3.5 (FINRA 2210) | Reg |
| Fair Lending | Address potential bias in AI outputs | Control 3.7 (UDAAP Compliance), Control 3.8 (Model Risk Management) | Reg |
| Cybersecurity | Secure AI systems and data flows | Control 2.7 (Conditional Access), Control 2.14 (Network Security), Control 2.15 (Zero Trust) | R / Reg |

---

## Cross-Regulation Control Frequency

Controls that appear across the most regulations should be prioritized for implementation.

| Control | Regulation Count | Regulations |
|---------|-----------------|-------------|
| Control 3.1 (Copilot Audit Logging) | 7 | FINRA 4511, 3110, SEC 17a-3, SOX, GLBA, FFIEC, Interagency AI |
| Control 3.2 (Retention Policies) | 5 | FINRA 4511, SEC 17a-4, Reg S-P, GLBA, FFIEC |
| Control 3.11 (Regulatory Record-keeping) | 4 | FINRA 4511, SEC 17a-3, SEC 17a-4, SOX |
| Control 2.4 (DLP Policies) | 5 | Reg S-P, SOX, GLBA, FFIEC, Interagency AI |
| Control 3.6 (Supervisory Review) | 5 | FINRA 3110, 2210, SEC 17a-3, Reg BI, CFPB UDAAP |
| Control 3.8 (Model Risk Management) | 4 | OCC 2011-12, Reg BI, CFPB UDAAP, Interagency AI |
| Control 1.12 (Governance Committee) | 4 | FINRA 3110, Reg BI, OCC 2011-12, Interagency AI |
| Control 3.12 (Audit Evidence) | 4 | SEC 17a-3, SEC 17a-4, SOX, OCC 2011-12 |
| Control 3.4 (Communication Compliance) | 4 | FINRA 3110, 2210, SEC 17a-3, CFPB UDAAP |
| Control 3.7 (UDAAP Compliance) | 3 | FINRA 2210, CFPB UDAAP, Interagency AI |

---

*FSI Copilot Governance Framework v1.0 - February 2026*
