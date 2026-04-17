# FSI Use-Case Risk Scenario Matrix

High-risk Microsoft 365 Copilot use cases in financial services mapped to applicable governance controls.

!!! warning "Disclaimer"
    This matrix is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../disclaimer.md).

---

## How to Use This Matrix

This matrix identifies common high-risk Copilot use cases in financial services and maps each to the governance controls that specifically apply. Use this to:

1. **Prioritize control implementation** for your organization's specific Copilot use cases
2. **Prepare for regulatory examinations** by demonstrating risk-aware governance
3. **Scope pilot deployments** by understanding which controls must be in place before enabling specific use cases

---

## Anti-Money Laundering (AML) and Fraud Detection

Copilot used to assist analysts in reviewing suspicious activity reports (SARs), reducing false positives in transaction monitoring, or summarizing investigation findings.

| Risk Factor | Description | Applicable Controls |
|-------------|-------------|-------------------|
| **Model risk** | Copilot-generated analysis may miss true positives or create false confidence in clearing alerts | [3.8 Model Risk Management](../controls/pillar-3-compliance/3.8-model-risk-management.md) |
| **Data accuracy** | Copilot responses grounded on stale or incomplete transaction data could lead to incorrect SAR filing decisions | [1.4 Semantic Index Governance](../controls/pillar-1-readiness/1.4-semantic-index-governance.md) |
| **Audit trail** | BSA/AML examiners require complete documentation of investigation steps — Copilot-assisted analysis must be auditable | [3.1 Audit Logging](../controls/pillar-3-compliance/3.1-copilot-audit-logging.md), [3.11 Record Keeping](../controls/pillar-3-compliance/3.11-record-keeping.md) |
| **NPI exposure** | AML investigation data contains customer NPI that Copilot must not surface to unauthorized users | [3.10 Reg S-P Privacy](../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md), [2.4 Information Barriers](../controls/pillar-2-security/2.4-information-barriers.md) |
| **Retention** | Investigation records and Copilot-generated summaries must be retained per BSA retention requirements (5 years for SARs) | [3.2 Data Retention](../controls/pillar-3-compliance/3.2-data-retention-policies.md) |

**Regulatory references:** Bank Secrecy Act (BSA), FinCEN guidance, OCC Bulletin 2011-12 (SR 11-7)

---

## Client Communications (Advisory and Sales)

Copilot used to draft client emails, proposal letters, investment recommendation summaries, or marketing materials for retail or institutional clients.

| Risk Factor | Description | Applicable Controls |
|-------------|-------------|-------------------|
| **FINRA 2210 compliance** | Copilot-drafted communications must meet content standards — fair and balanced, no misleading claims, required risk disclosures | [3.5 FINRA 2210](../controls/pillar-3-compliance/3.5-finra-2210-compliance.md) |
| **Supervisory review** | Principal pre-approval is required for retail communications; Copilot drafts are not exempt from this requirement | [3.6 Supervision and Oversight](../controls/pillar-3-compliance/3.6-supervision-oversight.md) |
| **Communication compliance** | Copilot-drafted client communications should trigger communication compliance policy review | [3.4 Communication Compliance](../controls/pillar-3-compliance/3.4-communication-compliance.md) |
| **Books and records** | All Copilot-drafted client communications are business records under FINRA Rule 4511 and SEC Rule 17a-4 | [3.11 Record Keeping](../controls/pillar-3-compliance/3.11-record-keeping.md), [3.2 Data Retention](../controls/pillar-3-compliance/3.2-data-retention-policies.md) |
| **DLP for NPI** | Client communications may contain account numbers, SSNs, or other sensitive data that DLP should intercept | [2.1 DLP Policies](../controls/pillar-2-security/2.1-dlp-policies-for-copilot.md) |
| **Disclosure obligations** | SEC Marketing Rule (206(4)-1) and AI disclosure requirements may apply to Copilot-drafted advisory content | [3.9 AI Disclosure](../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md) |

**Regulatory references:** FINRA Rule 2210, FINRA Rule 3110, SEC Reg BI, SEC Marketing Rule

---

## Investment Research and Analysis

Copilot used to summarize market data, draft research reports, analyze financial statements, or assist portfolio managers with investment decisions.

| Risk Factor | Description | Applicable Controls |
|-------------|-------------|-------------------|
| **Chinese wall enforcement** | Research analysts using Copilot must not access investment banking deal information — information barriers are critical | [2.4 Information Barriers](../controls/pillar-2-security/2.4-information-barriers.md) |
| **Web grounding risk** | Copilot web search grounding may introduce unvetted external data into research analysis | [2.6 Web Search Controls](../controls/pillar-2-security/2.6-web-search-controls.md) |
| **Model risk** | AI-assisted investment analysis is subject to model risk management requirements under OCC SR 11-7 | [3.8 Model Risk Management](../controls/pillar-3-compliance/3.8-model-risk-management.md) |
| **Data accuracy** | Copilot may hallucinate financial data or misrepresent source material — verification workflows are essential | [1.4 Semantic Index Governance](../controls/pillar-1-readiness/1.4-semantic-index-governance.md) |
| **Trading ahead** | Research generated with Copilot assistance must follow FINRA Rule 5280 timing requirements | [2.4 Information Barriers](../controls/pillar-2-security/2.4-information-barriers.md) |

**Regulatory references:** FINRA Rule 5280, FINRA Rule 2241/2242, OCC SR 11-7

---

## Financial Reporting and SOX Workflows

Copilot used in financial close processes, journal entry preparation, audit evidence assembly, or internal control documentation.

| Risk Factor | Description | Applicable Controls |
|-------------|-------------|-------------------|
| **SOX control evidence** | Copilot-assisted financial reporting workflows must produce auditable evidence trails | [3.12 Evidence Collection](../controls/pillar-3-compliance/3.12-evidence-collection.md), [3.1 Audit Logging](../controls/pillar-3-compliance/3.1-copilot-audit-logging.md) |
| **Data integrity** | Copilot-generated financial summaries used in reporting must be verified against source systems | [1.4 Semantic Index Governance](../controls/pillar-1-readiness/1.4-semantic-index-governance.md) |
| **Access control** | Financial reporting data requires strict access controls — Copilot should not surface financial data to unauthorized users | [2.4 Information Barriers](../controls/pillar-2-security/2.4-information-barriers.md), [1.6 Permission Model](../controls/pillar-1-readiness/1.6-permission-model-audit.md) |
| **Retention** | Financial reporting records have specific SEC retention requirements (typically 7 years) | [3.2 Data Retention](../controls/pillar-3-compliance/3.2-data-retention-policies.md) |
| **Copilot for Finance** | Microsoft's Finance Agent (2026 Wave 1) supports multi-rule reconciliation and variance analysis — SOX implications for AI-assisted reconciliation outputs require specific governance | [4.13 Extensibility Governance](../controls/pillar-4-operations/4.13-extensibility-governance.md) |

**Regulatory references:** SOX Section 302/404, PCAOB AS 2201, SEC Rule 13a-15

---

## Meeting Governance (Board, Committee, Client)

Copilot in Teams meetings generating transcripts, summaries, action items, and video recaps for regulated discussions.

| Risk Factor | Description | Applicable Controls |
|-------------|-------------|-------------------|
| **Record retention** | Meeting transcripts and Copilot summaries may constitute business records requiring retention | [4.2 Teams Meetings Governance](../controls/pillar-4-operations/4.2-teams-meetings-governance.md), [3.2 Data Retention](../controls/pillar-3-compliance/3.2-data-retention-policies.md) |
| **MNPI in meetings** | Board and committee meetings often involve MNPI — Copilot should be disabled for sensitive meetings via sensitivity labels | [2.2 Sensitivity Labels](../controls/pillar-2-security/2.2-sensitivity-labels-classification.md) |
| **Supervisory review** | Meeting summaries describing investment recommendations or client interactions may require FINRA 3110 supervisory review | [3.6 Supervision and Oversight](../controls/pillar-3-compliance/3.6-supervision-oversight.md) |
| **Video recap** | Video recaps are a distinct artifact type with different retention considerations under FINRA 4511 | [4.2 Teams Meetings Governance](../controls/pillar-4-operations/4.2-teams-meetings-governance.md) |

**Regulatory references:** FINRA Rule 4511, FINRA Rule 3110, SEC Rule 17a-4

---

## Quick Reference: Control Applicability by Use Case

| Use Case | Critical Controls | Key Regulations |
|----------|------------------|-----------------|
| **AML/Fraud** | 3.8, 3.1, 3.11, 2.4, 3.10 | BSA, OCC SR 11-7 |
| **Client Communications** | 3.5, 3.6, 3.4, 3.11, 2.1, 3.9 | FINRA 2210, Reg BI |
| **Investment Research** | 2.4, 2.6, 3.8, 1.4 | FINRA 5280, OCC SR 11-7 |
| **Financial Reporting** | 3.12, 3.1, 2.4, 3.2 | SOX 302/404 |
| **Meetings** | 4.2, 3.2, 2.2, 3.6 | FINRA 4511, FINRA 3110 |

---

*FSI Copilot Governance Framework v1.4 - April 2026*
