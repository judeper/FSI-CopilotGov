# Colorado AI Act Readiness

Compliance considerations for Colorado SB 24-205 (Colorado Artificial Intelligence Act) as it applies to Microsoft 365 Copilot deployments in financial services organizations.

---

## Overview

The Colorado AI Act (SB 24-205), signed into law in 2024, establishes requirements for developers and deployers of "high-risk artificial intelligence systems" — AI systems that make, or are a substantial factor in making, consequential decisions affecting consumers. Financial services organizations using M365 Copilot should assess whether their use cases fall within the Act's scope.

**Effective date:** February 1, 2026
**Applicability:** Organizations that deploy AI systems making or substantially contributing to consequential decisions in areas including financial services, insurance, and lending.

## Scope Assessment for M365 Copilot

### When the Act Likely Applies

M365 Copilot use cases that may fall under the Colorado AI Act:

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

## Key Requirements for Deployers

### 1. Risk Management Policy

**Requirement:** Implement a risk management policy and program to govern the deployment of high-risk AI systems.

**How FSI Copilot Governance Framework supports compliance:**
- The governance committee charter and RACI matrix establish the governance structure
- The AI Risk Assessment Template provides the risk evaluation methodology
- The Governance Operating Calendar defines ongoing risk management activities
- Controls across all four pillars implement the risk management program

### 2. Impact Assessment

**Requirement:** Complete an impact assessment for high-risk AI deployments before deployment and annually thereafter.

**How to comply:**
- Complete the AI Risk Assessment Template for each high-risk Copilot use case
- Document the purpose, intended use, data inputs, and expected outputs
- Assess risks of algorithmic discrimination
- Evaluate the effectiveness of safeguards
- Review and update the assessment annually

### 3. Consumer Notification

**Requirement:** Notify consumers when a high-risk AI system is used to make or substantially contribute to a consequential decision.

**How to comply:**
- Identify Copilot use cases where outputs substantially contribute to consumer-affecting decisions
- Develop consumer notification language for affected interactions
- Integrate notification into customer-facing processes where applicable
- Document notification procedures and maintain records of notifications

### 4. Disclosure and Transparency

**Requirement:** Provide statements on the deployer's website describing the types of high-risk AI systems deployed and how they manage risks.

**How to comply:**
- Create a public-facing AI transparency statement
- Describe the types of AI systems deployed (including M365 Copilot where applicable)
- Summarize the risk management approach
- Publish the statement on the organization's website

### 5. Algorithmic Discrimination Prevention

**Requirement:** Use reasonable care to protect consumers from known or reasonably foreseeable risks of algorithmic discrimination.

**How to comply:**
- Assess whether Copilot use cases could result in disparate impact on protected classes
- Document safeguards against algorithmic discrimination
- Monitor Copilot outputs in high-risk use cases for discriminatory patterns
- Implement human review for decisions substantially influenced by Copilot

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

- [ ] Configure Copilot governance controls per the framework (Pillars 1-4)
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
