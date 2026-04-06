# Colorado AI Act Readiness

Compliance considerations for Colorado SB 24-205 (Colorado Artificial Intelligence Act) as it applies to Microsoft 365 Copilot deployments in financial services organizations.

---

## Overview

The Colorado AI Act (SB 24-205), signed into law in 2024, establishes requirements for developers and deployers of "high-risk artificial intelligence systems" — AI systems that make, or are a substantial factor in making, consequential decisions affecting consumers. Financial services organizations using Microsoft 365 Copilot should assess whether their use cases fall within the Act's scope.

**Effective date:** June 30, 2026 (amended by SB 25B-004)
**Applicability:** Organizations that deploy AI systems making or substantially contributing to consequential decisions in areas including financial services, insurance, and lending.

## Scope Assessment for Microsoft 365 Copilot

### When the Act Likely Applies

Microsoft 365 Copilot use cases that may fall under the Colorado AI Act:

| Use Case | Risk Assessment |
|----------|----------------|
| Copilot drafting client communications that influence financial decisions | Potentially in scope if substantially contributing to consequential decision |
| Copilot summarizing customer data for loan review processes | Likely in scope — affects lending decisions |
| Copilot generating investment research summaries used in recommendations | Potentially in scope — affects investment decisions |
| Copilot analyzing employee performance data for HR decisions | Likely in scope — affects employment decisions |

### When the Act Likely Does Not Apply

| Use Case | Rationale |
|----------|-----------|
| Copilot drafting internal meeting notes | Not a consequential decision |
| Copilot summarizing internal policies for employee reference | Informational only |
| Copilot creating presentation formatting or editing | Productivity tool, not decision-making |
| Copilot answering general knowledge questions | Not affecting specific consumers |

### Federal Banking Regulator Exemption

The Colorado AI Act includes an exemption for entities regulated by federal banking regulators — specifically the Office of the Comptroller of the Currency (OCC), Federal Deposit Insurance Corporation (FDIC), and the Federal Reserve. Banks and depository institutions supervised by these agencies may fall outside the Act's scope.

However, **broker-dealers, investment advisers, and insurance entities** are generally not supervised by federal banking regulators and likely remain subject to the Act's requirements. Organizations should verify their specific regulatory status with legal counsel before relying on this exemption.

!!! note "Scope Verification"
    The federal banking regulator exemption does not extend to all financial services entities. Consult legal counsel to determine whether your organization qualifies for this exemption based on your primary regulator.

## Key Requirements for Deployers

### 1. Risk Management Policy

**Requirement:** Implement a risk management policy and program to govern the deployment of high-risk AI systems.

**How FSI Copilot Governance Framework helps address this requirement:**

- The governance committee charter and RACI matrix establish the governance structure
- The AI Risk Assessment Template provides the risk evaluation methodology
- The Governance Operating Calendar defines ongoing risk management activities
- **Relevant controls:** [Control 3.8](../../controls/pillar-3-compliance/3.8-model-risk-management.md) (Model Risk Management), [Control 1.1](../../controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md) (Readiness Assessment), [Control 4.9](../../controls/pillar-4-operations/4.9-incident-reporting.md) (Incident Reporting)

### 2. Impact Assessment

**Requirement:** Complete an impact assessment for high-risk AI deployments before deployment and annually thereafter.

**How to comply:**

- Complete the AI Risk Assessment Template for each high-risk Copilot use case
- Document the purpose, intended use, data inputs, and expected outputs
- Assess risks of algorithmic discrimination
- Evaluate the effectiveness of safeguards
- Review and update the assessment annually
- **Relevant controls:** [Control 3.8](../../controls/pillar-3-compliance/3.8-model-risk-management.md) (Model Risk Management), [Control 1.1](../../controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md) (Readiness Assessment)

### 3. Consumer Notification

**Requirement:** Notify consumers when a high-risk AI system is used to make or substantially contribute to a consequential decision.

**How to comply:**

- Identify Copilot use cases where outputs substantially contribute to consumer-affecting decisions
- Develop consumer notification language for affected interactions
- Integrate notification into customer-facing processes where applicable
- Document notification procedures and maintain records of notifications
- **Relevant controls:** [Control 3.9](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md) (AI Disclosure and Transparency), [Control 3.4](../../controls/pillar-3-compliance/3.4-communication-compliance.md) (Communication Compliance)

### 4. Disclosure and Transparency

**Requirement:** Provide statements on the deployer's website describing the types of high-risk AI systems deployed and how they manage risks.

**How to comply:**

- Create a public-facing AI transparency statement
- Describe the types of AI systems deployed (including Microsoft 365 Copilot where applicable)
- Summarize the risk management approach
- Publish the statement on the organization's website
- **Relevant controls:** [Control 3.9](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md) (AI Disclosure and Transparency), [Control 3.7](../../controls/pillar-3-compliance/3.7-regulatory-reporting.md) (Regulatory Reporting)

### 5. Algorithmic Discrimination Prevention

**Requirement:** Use reasonable care to protect consumers from known or reasonably foreseeable risks of algorithmic discrimination.

**How to comply:**

- Assess whether Copilot use cases could result in disparate impact on protected classes
- Document safeguards against algorithmic discrimination
- Monitor Copilot outputs in high-risk use cases for discriminatory patterns
- Implement human review for decisions substantially influenced by Copilot
- **Relevant controls:** [Control 3.6](../../controls/pillar-3-compliance/3.6-supervision-oversight.md) (Supervision and Oversight), [Control 3.1](../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md) (Audit Logging), [Control 2.10](../../controls/pillar-2-security/2.10-insider-risk-detection.md) (Insider Risk Detection)

## Implementation Checklist

### Assessment Phase

- [ ] Inventory all Copilot use cases across the organization
- [ ] Classify each use case as high-risk or not based on the Act's definitions
- [ ] Conduct impact assessments for identified high-risk use cases
- [ ] Engage legal counsel for scope determination guidance

### Policy and Procedure Phase

- [ ] Document the AI risk management policy (leverage the governance framework)
- [ ] Create consumer notification procedures for high-risk use cases
- [ ] Draft the public AI transparency statement
- [ ] Establish algorithmic discrimination monitoring procedures

### Technical Control Phase

- [ ] Configure Copilot governance controls per the framework (see Controls [1.1](../../controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md), [3.1](../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md), [3.8](../../controls/pillar-3-compliance/3.8-model-risk-management.md), [3.9](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md))
- [ ] Implement human-in-the-loop review for high-risk use cases
- [ ] Configure audit logging for high-risk Copilot interactions
- [ ] Set up monitoring for potential discriminatory outcomes

### Ongoing Compliance Phase

- [ ] Conduct annual impact assessment reviews
- [ ] Monitor for regulatory guidance updates and enforcement actions
- [ ] Update consumer notifications as use cases change
- [ ] Report AI governance posture to governance committee

## Interaction with Other Regulations

The Colorado AI Act operates alongside existing FSI regulations:

| Regulation | Interaction with Colorado AI Act |
|-----------|----------------------------------|
| FINRA Rules | FINRA supervision requirements complement the Act's risk management obligations |
| SEC Regulation Best Interest | The Act's consumer protection aligns with Reg BI suitability requirements |
| ECOA / Fair Lending | The Act's anti-discrimination provisions reinforce fair lending obligations |
| GLBA | The Act's transparency requirements complement GLBA privacy notices |

## Monitoring Regulatory Developments

The Colorado AI Act regulatory landscape is evolving:
- Monitor the Colorado Attorney General's office for rulemaking and guidance
- Track enforcement actions for precedent on scope interpretation
- Watch for amendments to the Act (legislative sessions)
- Monitor other states adopting similar AI legislation
- Review industry association guidance (ABA, SIFMA) on compliance approaches

---

*This module provides general compliance guidance. Consult legal counsel for organization-specific compliance advice. Review and update as the regulatory landscape evolves.*
