# NIST AI Risk Management Framework Crosswalk

Crosswalk mapping FSI Copilot Governance Framework controls to the NIST AI Risk Management Framework (AI RMF 1.0) functions, categories, and subcategories.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. The NIST AI RMF is a voluntary framework; this crosswalk is intended to aid organizations using both frameworks together. See [full disclaimer](../disclaimer.md).

---

## About the NIST AI RMF

The [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework) provides a structured approach to managing AI risks across four core functions:

| Function | Purpose |
|----------|---------|
| **Govern** | Cultivate and implement a culture of AI risk management |
| **Map** | Contextualize risks related to an AI system |
| **Measure** | Analyze, assess, benchmark, and monitor AI risk |
| **Manage** | Allocate resources to mapped and measured risks on a regular basis |

This crosswalk maps each NIST AI RMF subcategory to the FSI-CopilotGov controls that support it. Not every subcategory has a direct mapping; Microsoft 365 Copilot is a third-party AI service, so some subcategories related to AI model development are addressed through vendor risk management rather than direct control.

---

## GOVERN Function

Cultivate a culture of AI risk management with governance structures, policies, and accountability.

| NIST Category | NIST Subcategory | Description | FSI-CopilotGov Controls |
|---------------|-----------------|-------------|------------------------|
| **GOVERN 1** — Policies, processes, procedures, and practices are in place, transparent, and documented | GOVERN 1.1 | Legal and regulatory requirements involving AI are understood, managed, and documented | Control 3.11 (Regulatory Record-keeping), Control 3.13 (FFIEC Alignment), Control 1.10 (Vendor Risk Assessment) |
| | GOVERN 1.2 | The characteristics of trustworthy AI are integrated into organizational policies | Control 1.12 (Governance Committee), Control 4.12 (Governance Calendar), Control 1.13 (Training Plan) |
| | GOVERN 1.3 | Processes, procedures, and practices are in place to determine the AI system's trustworthiness | Control 3.8 (Model Risk Management), Control 1.10 (Vendor Risk Assessment) |
| | GOVERN 1.4 | Ongoing monitoring processes are in place and documented | Control 4.6 (Usage Analytics), Control 3.9 (DSPM for AI), Control 4.11 (Sentinel Integration) |
| | GOVERN 1.5 | Ongoing monitoring includes mechanisms to identify when the AI system is performing in an unexpected manner | Control 4.11 (Sentinel Integration), Control 4.8 (Incident Response), Control 2.11 (Insider Risk Management) |
| | GOVERN 1.6 | Mechanisms are in place to inventory AI systems | Control 3.8 (Model Risk Management), Control 1.12 (Governance Committee) |
| | GOVERN 1.7 | Processes and procedures are in place for decommissioning and phasing out AI systems | Control 4.1 (Feature Toggle Management), Control 4.9 (Business Continuity) |
| **GOVERN 2** — Accountability structures are in place | GOVERN 2.1 | Roles, responsibilities, and lines of communication related to mapping, measuring, and managing AI risks are documented | Control 4.13 (Stakeholder RACI Matrix), Control 1.12 (Governance Committee) |
| | GOVERN 2.2 | The organization's personnel and partners have AI risk management skills | Control 1.13 (User Communication and Training), Control 1.12 (Governance Committee) |
| | GOVERN 2.3 | Executive leadership is responsible for decisions about AI risk | Control 1.12 (Governance Committee), Control 4.13 (RACI Matrix) |
| **GOVERN 3** — Workforce diversity, equity, inclusion, and accessibility | GOVERN 3.1 | AI workforce diversity and domain expertise are prioritized | Control 1.12 (Governance Committee) — committee composition should include diverse expertise |
| **GOVERN 4** — Organizational practices and culture | GOVERN 4.1 | Organizational practices and culture support risk management | Control 1.13 (Training Plan), Control 4.12 (Governance Calendar) |
| | GOVERN 4.2 | Organizational teams are empowered to raise concerns | Control 4.8 (Incident Response), Control 1.12 (Governance Committee) |
| | GOVERN 4.3 | Organizational practices are in place to enable AI testing, identification of incidents, and information sharing | Control 4.8 (Incident Response), Control 3.1 (Audit Logging), Control 4.11 (Sentinel) |
| **GOVERN 5** — Processes for engagement with relevant AI actors | GOVERN 5.1 | Organizational policies and practices for engagement with relevant AI actors and stakeholders are in place | Control 1.10 (Vendor Risk Assessment), Control 1.12 (Governance Committee), Control 4.13 (RACI Matrix) |
| | GOVERN 5.2 | Mechanisms are in place to receive and address third-party input on AI risk | Control 4.10 (Change Management), Control 1.10 (Vendor Risk Assessment) |
| **GOVERN 6** — Policies and procedures are in place to address AI risks from third-party entities | GOVERN 6.1 | Policies and procedures address risks from third-party AI | Control 1.10 (Vendor Risk Assessment), Control 4.5 (Plugin and Extensibility Governance), Control 3.8 (Model Risk Management) |
| | GOVERN 6.2 | Contingency processes for third-party AI system failures | Control 4.9 (Business Continuity), Control 4.8 (Incident Response) |

---

## MAP Function

Contextualize the risks related to the AI system by understanding its purpose, users, and environment.

| NIST Category | NIST Subcategory | Description | FSI-CopilotGov Controls |
|---------------|-----------------|-------------|------------------------|
| **MAP 1** — Context is established and understood | MAP 1.1 | Intended purposes, potentially beneficial uses, context of use, and assumptions are stated | Control 1.12 (Governance Committee), Control 1.13 (Training Plan), Control 3.8 (Model Risk Management) |
| | MAP 1.2 | Interdependencies between AI system components are mapped | Control 1.8 (Semantic Index Readiness), Control 2.15 (Zero Trust Alignment), Control 2.14 (Network Security) |
| | MAP 1.5 | Organizational risk tolerances are determined | Control 1.12 (Governance Committee), Control 3.8 (Model Risk Management) |
| | MAP 1.6 | System requirements and goals are established | Control 4.1 (Feature Toggle Management), Control 4.2 (Per-App Configuration), Control 1.9 (License Scoping) |
| **MAP 2** — Categorization of the AI system | MAP 2.1 | The AI system's intended users and subjects are characterized | Control 1.9 (License Assignment and Scoping), Control 4.2 (Per-App Configuration) |
| | MAP 2.2 | Scientific integrity and statistical accuracy are identified | Control 3.8 (Model Risk Management) — Copilot is a third-party model; vendor validation documentation |
| | MAP 2.3 | AI system categorization is performed | Control 3.8 (Model Risk Management), Control 1.11 (Data Classification Inventory) |
| **MAP 3** — AI capabilities, targeted usage, goals, and expected benefits are understood | MAP 3.1 | Potential benefits of the AI system are examined | Control 4.6 (Usage Analytics), Control 4.7 (Cost Management) |
| | MAP 3.4 | The AI system's possible impacts are assessed | Control 3.7 (UDAAP Compliance), Control 3.8 (Model Risk Management), Control 1.1 (Oversharing Assessment) |
| | MAP 3.5 | The likelihood and severity of identified impacts are characterized | Control 3.8 (Model Risk Management), Control 4.8 (Incident Response) |
| **MAP 4** — Risks and benefits are mapped for all components of the AI system | MAP 4.1 | Risks and benefits are mapped for the AI system's deployment context | Control 1.1 (Oversharing Assessment), Control 1.11 (Data Classification), Control 3.8 (Model Risk Management) |
| | MAP 4.2 | Internal risk controls are identified and documented | Control 2.4 (DLP), Control 2.1 (Sensitivity Labels), Control 2.7 (Conditional Access), Control 2.8 (Information Barriers) |
| **MAP 5** — Likelihood and severity of impacts are characterized | MAP 5.1 | Likelihood of each identified impact is characterized | Control 3.8 (Model Risk Management), Control 4.8 (Incident Response) |
| | MAP 5.2 | Practices are in place to manage data quality | Control 1.1 (Oversharing Assessment), Control 1.2 (Permissions Review), Control 1.11 (Data Classification) |

---

## MEASURE Function

Analyze, assess, benchmark, and monitor AI risk using quantitative and qualitative methods.

| NIST Category | NIST Subcategory | Description | FSI-CopilotGov Controls |
|---------------|-----------------|-------------|------------------------|
| **MEASURE 1** — Appropriate methods and metrics for AI risk measurement | MEASURE 1.1 | Approaches and metrics for AI risk measurement are selected | Control 3.9 (DSPM for AI), Control 4.6 (Usage Analytics), Control 4.11 (Sentinel Integration) |
| | MEASURE 1.3 | Internal processes for AI system measurement include results that are valid, reliable, and representative | Control 3.1 (Audit Logging), Control 3.12 (Audit Evidence) |
| **MEASURE 2** — AI systems are evaluated for trustworthy characteristics | MEASURE 2.1 | Privacy risk of the AI system is examined and documented | Control 3.10 (Privacy and Reg S-P), Control 2.4 (DLP), Control 2.12 (DSPM for AI) |
| | MEASURE 2.2 | AI system fairness is assessed | Control 3.7 (UDAAP Compliance), Control 3.8 (Model Risk Management) |
| | MEASURE 2.3 | AI system reliability and robustness are assessed | Control 4.9 (Business Continuity), Control 3.8 (Model Risk Management) |
| | MEASURE 2.5 | AI system security is evaluated | Control 2.7 (Conditional Access), Control 2.14 (Network Security), Control 2.15 (Zero Trust), Control 2.10 (Defender) |
| | MEASURE 2.6 | AI system transparency is assessed | Control 3.1 (Audit Logging), Control 4.6 (Usage Analytics), Control 3.8 (Model Risk Management) |
| | MEASURE 2.7 | AI system accountability measures are assessed | Control 3.1 (Audit Logging), Control 4.13 (RACI Matrix), Control 3.12 (Audit Evidence) |
| | MEASURE 2.8 | AI system value alignment is assessed | Control 1.12 (Governance Committee), Control 1.13 (Training), Control 3.7 (UDAAP Compliance) |
| | MEASURE 2.9 | AI system risks are documented | Control 3.8 (Model Risk Management), Control 3.12 (Audit Evidence) |
| | MEASURE 2.11 | Fairness and bias evaluation results are documented | Control 3.7 (UDAAP Compliance), Control 3.8 (Model Risk Management), Control 3.12 (Audit Evidence) |
| **MEASURE 3** — AI risks are tracked over time | MEASURE 3.1 | AI risks are tracked regularly over time | Control 3.9 (DSPM for AI), Control 4.11 (Sentinel), Control 4.12 (Governance Calendar) |
| | MEASURE 3.2 | Risk tracking approaches account for AI system context | Control 4.6 (Usage Analytics), Control 4.10 (Change Management) |
| | MEASURE 3.3 | Feedback mechanisms are in place | Control 4.8 (Incident Response), Control 4.10 (Change Management) |
| **MEASURE 4** — Measurement feedback is incorporated | MEASURE 4.1 | Measurement results are used to update MAP and MANAGE functions | Control 4.12 (Governance Calendar), Control 1.12 (Governance Committee) |

---

## MANAGE Function

Allocate resources to mapped and measured risks on a regular basis, including response strategies.

| NIST Category | NIST Subcategory | Description | FSI-CopilotGov Controls |
|---------------|-----------------|-------------|------------------------|
| **MANAGE 1** — AI risks are prioritized, responded to, and managed | MANAGE 1.1 | A determination is made as to whether the AI system achieves its intended purpose within acceptable risk tolerances | Control 1.12 (Governance Committee), Control 3.8 (Model Risk Management), Control 4.6 (Usage Analytics) |
| | MANAGE 1.2 | Treatment plans for the highest priority AI risks are established | Control 4.8 (Incident Response), Control 4.1 (Feature Toggle Management) |
| | MANAGE 1.3 | Responses to AI risks include risk avoidance, mitigation, transfer, or acceptance | Control 4.1 (Feature Toggle Management), Control 4.2 (Per-App Configuration), Control 2.4 (DLP), Control 2.8 (Information Barriers) |
| | MANAGE 1.4 | Negative impacts are mitigated | Control 2.4 (DLP), Control 2.1 (Sensitivity Labels), Control 2.7 (Conditional Access), Control 4.8 (Incident Response) |
| **MANAGE 2** — Strategies to maximize AI benefits and minimize negative impacts | MANAGE 2.1 | Resources are allocated for managing AI risks | Control 1.9 (License Scoping), Control 4.7 (Cost Management), Control 4.13 (RACI Matrix) |
| | MANAGE 2.2 | Mechanisms are in place for AI system operators and decision-makers to escalate | Control 4.8 (Incident Response), Control 1.12 (Governance Committee) |
| | MANAGE 2.3 | Procedures are followed to respond to and recover from identified AI incidents | Control 4.8 (Incident Response), Control 4.9 (Business Continuity) |
| | MANAGE 2.4 | Mechanisms are in place for deactivation of AI systems exhibiting anomalous behavior | Control 4.1 (Feature Toggle Management), Control 4.2 (Per-App Configuration) — ability to disable Copilot rapidly |
| **MANAGE 3** — AI risks and benefits from third-party resources are managed | MANAGE 3.1 | AI risks from third-party resources are managed | Control 1.10 (Vendor Risk Assessment), Control 4.5 (Plugin Governance), Control 3.8 (Model Risk Management) |
| | MANAGE 3.2 | Pre-trained models and third-party data are monitored | Control 4.10 (Change Management), Control 3.9 (DSPM for AI) |
| **MANAGE 4** — Risk treatments are documented and monitored | MANAGE 4.1 | Post-deployment AI system monitoring is carried out | Control 3.9 (DSPM for AI), Control 4.6 (Usage Analytics), Control 4.11 (Sentinel), Control 3.1 (Audit Logging) |
| | MANAGE 4.2 | Measurable activities for continual improvement are integrated into AI system updates | Control 4.10 (Change Management), Control 4.12 (Governance Calendar) |

---

## Coverage Summary

| NIST AI RMF Function | Categories Mapped | Key FSI-CopilotGov Controls |
|---------------------|-------------------|----------------------------|
| **GOVERN** (17 subcategories) | GOVERN 1-6 | 1.10, 1.12, 1.13, 3.8, 4.5, 4.6, 4.8, 4.9, 4.11, 4.12, 4.13 |
| **MAP** (12 subcategories) | MAP 1-5 | 1.1, 1.2, 1.8, 1.9, 1.11, 2.4, 2.7, 2.15, 3.7, 3.8, 4.2, 4.6 |
| **MEASURE** (14 subcategories) | MEASURE 1-4 | 3.1, 3.7, 3.8, 3.9, 3.10, 3.12, 4.6, 4.11, 4.12, 4.13 |
| **MANAGE** (10 subcategories) | MANAGE 1-4 | 1.10, 2.4, 3.9, 4.1, 4.2, 4.5, 4.6, 4.8, 4.9, 4.10, 4.11, 4.12 |

---

## Using This Crosswalk

1. **For NIST alignment reporting:** Use this table to demonstrate how your Copilot governance program maps to the NIST AI RMF
2. **For gap analysis:** Identify NIST subcategories without mapped controls — these may require additional organizational policies beyond this framework
3. **For examination preparation:** Examiners increasingly reference NIST AI RMF; having this crosswalk ready supports compliance with examination expectations
4. **Combined with regulatory mappings:** Use alongside the [Regulatory Mappings](regulatory-mappings.md) for comprehensive coverage documentation

---

*FSI Copilot Governance Framework v1.0 - February 2026*
