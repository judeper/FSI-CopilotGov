# RACI Governance Template

Responsibility Assignment Matrix (RACI) for M365 Copilot governance activities in financial services organizations. Use these matrices to assign clear ownership for governance decisions and operations.

**R** = Responsible (does the work) | **A** = Accountable (final decision authority) | **C** = Consulted (provides input) | **I** = Informed (kept up to date)

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## Governance Roles

| Role | Abbreviation | Description |
|------|-------------|-------------|
| M365 Global Admin | **M365** | Microsoft 365 and Copilot technical administration |
| Purview Compliance Admin | **PCA** | DLP, sensitivity labels, audit, and compliance portal administration |
| CISO / Security Lead | **CISO** | Overall Copilot security posture and governance authority |
| AI Governance Lead | **AIGL** | Day-to-day governance program management |
| Compliance Officer | **CO** | Regulatory compliance, examination readiness, and supervisory oversight |
| Legal Counsel | **Legal** | Legal review, regulatory interpretation, and contractual matters |
| Security Operations | **SecOps** | Security monitoring, incident detection, and triage |
| Business Unit Owners | **BUO** | Business use case validation and departmental adoption |

---

## RACI Matrix: Copilot Deployment Decisions

| Decision | M365 | PCA | CISO | AIGL | CO | Legal | BUO |
|----------|------|-----|------|------|----|-------|-----|
| Approve Copilot adoption | I | I | A | R | C | C | C |
| Define pilot group membership | R | I | C | A | C | I | C |
| Select per-app Copilot toggles | R | C | A | R | C | I | C |
| Approve expansion waves | I | I | A | R | C | I | C |
| Approve Copilot for new use cases | I | C | A | R | C | C | R |
| Approve web search / grounding settings | R | C | A | R | C | C | I |
| License assignment and revocation | R | I | I | A | I | I | C |
| Approve Copilot plugins and extensions | R | C | A | R | C | C | I |
| Emergency Copilot kill switch activation | R | I | A | C | C | I | I |

---

## RACI Matrix: DLP Policy Changes

| Activity | M365 | PCA | CISO | AIGL | CO | Legal | BUO |
|----------|------|-----|------|------|----|-------|-----|
| Create new DLP policy for Copilot | I | R | A | C | C | I | I |
| Modify existing DLP policy rules | I | R | A | C | C | I | I |
| Tune sensitive information type thresholds | I | R | C | I | C | I | I |
| Enable DLP enforcement (from test mode) | I | R | A | C | C | I | I |
| Review DLP violation reports | I | R | C | I | A | I | I |
| Approve DLP policy exceptions | I | C | A | C | R | C | I |
| Add custom sensitive information types | I | R | C | C | A | C | I |

---

## RACI Matrix: Sensitivity Label Updates

| Activity | M365 | PCA | CISO | AIGL | CO | Legal | BUO |
|----------|------|-----|------|------|----|-------|-----|
| Create new sensitivity label | I | R | C | C | A | C | I |
| Modify label protection settings | I | R | A | C | C | I | I |
| Update auto-labeling policies | I | R | C | C | A | I | I |
| Change label scoping or publishing | I | R | C | C | A | I | C |
| Review label adoption metrics | I | R | I | A | I | I | I |
| Approve label taxonomy changes | I | C | A | R | C | C | I |
| Configure default labels for sites | C | R | C | C | A | I | C |

---

## RACI Matrix: Incident Response

| Activity | M365 | PCA | CISO | AIGL | CO | Legal | BUO |
|----------|------|-----|------|------|----|-------|-----|
| Detect and triage Copilot incident | C | C | A | R | I | I | I |
| Classify incident severity | I | I | A | C | C | I | I |
| Execute containment (disable Copilot) | R | I | A | C | I | I | I |
| Preserve evidence and audit logs | C | R | C | I | C | I | I |
| Investigate root cause | R | R | A | C | C | I | I |
| Assess regulatory notification requirements | I | I | C | I | R | A | I |
| Execute remediation | R | R | A | C | C | I | I |
| Conduct post-incident review | C | C | A | R | C | C | I |
| File regulatory notifications (if required) | I | I | I | I | R | A | I |
| Update governance controls based on findings | C | R | A | R | C | I | I |

---

## RACI Matrix: Regulatory Examination Response

| Activity | M365 | PCA | CISO | AIGL | CO | Legal | BUO |
|----------|------|-----|------|------|----|-------|-----|
| Receive and log examination notice | I | I | I | I | R | A | I |
| Assemble examination response team | I | I | C | C | R | A | I |
| Collect technical evidence | R | R | C | C | I | I | I |
| Collect governance documentation | I | I | I | R | R | C | I |
| Review responses before submission | I | I | C | C | C | A | I |
| Submit examination responses | I | I | I | I | R | A | I |
| Conduct live demonstrations (if requested) | R | R | C | C | C | I | I |
| Track examiner follow-up requests | I | I | I | C | R | A | I |
| Implement remediation for findings | R | R | A | R | C | C | I |
| Conduct post-examination retrospective | C | C | A | R | R | C | I |

---

## RACI Matrix: Feature Rollout Approvals

| Activity | M365 | PCA | CISO | AIGL | CO | Legal | BUO |
|----------|------|-----|------|------|----|-------|-----|
| Evaluate new Copilot features (Message Center) | R | C | C | A | C | I | I |
| Assess compliance impact of new features | I | R | C | C | A | C | I |
| Assess security impact of new features | R | I | A | C | C | I | I |
| Approve feature enablement | I | I | A | R | C | C | C |
| Configure and deploy approved features | R | C | I | C | I | I | I |
| Update governance documentation | I | I | I | R | C | I | I |
| Communicate feature changes to users | I | I | I | R | I | I | C |
| Monitor feature adoption and issues | R | C | I | A | I | I | I |

---

## How to Use This Template

1. **Customize roles** -- map the role abbreviations to named individuals in your organization
2. **Validate assignments** -- confirm that each row has exactly one **A** (Accountable)
3. **Review with stakeholders** -- share the RACI with all named individuals for acknowledgment
4. **Publish** -- store in the governance repository and reference in committee charter
5. **Update** -- review quarterly or when organizational roles change

### Common Mistakes to Avoid

- **Multiple Accountable (A)** per row -- only one person should be accountable for each activity
- **No Responsible (R)** per row -- every activity needs someone doing the work
- **Too many Consulted (C)** -- excessive consultation slows decisions; be selective
- **Missing Informed (I)** -- stakeholders left uninformed create governance gaps

---

*Customize this RACI based on your organizational structure. Review and update quarterly or when roles change.*

*FSI Copilot Governance Framework v1.4.0 - April 2026*
