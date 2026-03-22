# Microsoft Open-Source Copilot Analytics Tools

**Purpose:** Use Microsoft-authored open-source companion repositories from Analytics Hub to extend native Microsoft 365 Copilot readiness, usage, impact, and audit reporting.
**Applies to:** Organizations needing deeper Copilot readiness analysis, adoption reporting, impact measurement, or enterprise-scale audit exports.
**Target audience:** Copilot Program Managers, Governance Leads, Compliance Officers, Power BI Analysts, Security Operations.

---

## Background: Analytics Hub as a Discovery Surface

[Analytics Hub](https://github.com/microsoft/Analytics-Hub) is a Microsoft-maintained umbrella repository that catalogs multiple open-source analytics tools for Copilot and AI adoption.

For the FSI Copilot Governance Framework, the directly relevant companion repositories are:

| Tool | GitHub Repository | Primary Fit | Use When |
|------|-------------------|-------------|----------|
| **AI-in-One Dashboard** | [microsoft/AI-in-One-Dashboard](https://github.com/microsoft/AI-in-One-Dashboard) | Usage analytics | You need a tenant-wide view of Copilot, Copilot Chat, agent, and AI activity |
| **Copilot Chat & Agent Intelligence** | [microsoft/CopilotChatAnalytics](https://github.com/microsoft/CopilotChatAnalytics) | Usage analytics | You need deeper reporting on Copilot Chat sessions and agent adoption |
| **M365 Copilot Readiness Report** | [microsoft/M365UsageAnalytics](https://github.com/microsoft/M365UsageAnalytics) | Readiness and license planning | You need to prioritize which users should receive Copilot licenses |
| **Decoding Super Usage** | [microsoft/DecodingSuperUsage](https://github.com/microsoft/DecodingSuperUsage) | Impact measurement | You need Viva Insights-based analysis of super-user adoption patterns |
| **Super User Impact** | [microsoft/superuserimpact](https://github.com/microsoft/superuserimpact) | Impact measurement | You need behavioral and ROI-style measurement of super-user outcomes |
| **CustomizeCopilot** | [microsoft/customizecopilot](https://github.com/microsoft/customizecopilot) | Impact measurement | You want add-on pages that extend the Viva Insights-based reports above |
| **PAX (Portable Audit eXporter)** | [microsoft/PAX](https://github.com/microsoft/PAX) | Audit export | You need automated Purview and Graph exports beyond portal limits |

`GitHubCopilotImpact` was assessed but is not included here because it targets GitHub Copilot developer analytics rather than Microsoft 365 Copilot governance.

---

## 1) Usage, Readiness, and Adoption Analytics

### AI-in-One Dashboard

**Best for:** Executive-ready tenant-wide reporting across Copilot, Copilot Chat, agents, and related AI activity.

Use this repo when you need:

- department and role-based Copilot analytics
- licensed vs. unlicensed usage reporting
- adoption trend reporting across Copilot surfaces
- a single Power BI dashboard that combines Purview and Entra data

### Copilot Chat & Agent Intelligence

**Best for:** Deeper drill-down into Copilot Chat sessions and agent adoption than the all-up dashboard provides.

Use this repo when you need:

- Copilot Chat prompt and session pattern analysis
- agent inventory and adoption trend reporting
- segmentation by business unit, surface, and user cohort
- a companion dashboard to supplement the broader AI-in-One view

### M365 Copilot Readiness Report

**Best for:** License planning, readiness scoring, and prioritizing future Copilot allocations.

Use this repo when you need:

- a ranked list of users most likely to benefit from Copilot licenses
- workload-based readiness scoring across Teams, Outlook, Word, Excel, and PowerPoint
- governance-ready license utilization and enablement planning

---

## 2) Impact and ROI Measurement

### Decoding Super Usage

Use this repo when you want Viva Insights-based visibility into how users become frequent or high-value Copilot users.

### Super User Impact

Use this repo when you need to connect super-user behavior with measurable work-pattern shifts and estimated value.

### CustomizeCopilot

Use this repo when you want to extend the Viva Insights-based reports with additional pages rather than building a new report from scratch.

These three repositories fit best where the framework discusses:

- Copilot impact measurement
- adoption maturity
- ROI reporting
- evidence-based board and committee reporting

---

## 3) Audit Export and Evidence Collection

### PAX (Portable Audit eXporter)

PAX is the companion repository to use when native Purview or Admin Center export paths are insufficient for FSI evidence needs.

Use this repo when you need:

- audit export automation beyond portal row limits
- incremental watermark-based extraction
- Purview and Graph data collection for downstream dashboards
- regulated evidence collection and longer-running export workflows

PAX is also relevant to AgentGov, where it already supports AI audit and reporting guidance.

---

## 4) Mapping to Framework Controls

| Control | Companion Repositories | Why |
|---------|------------------------|-----|
| **[1.9 License Planning](../../controls/pillar-1-readiness/1.9-license-planning.md)** | M365UsageAnalytics | Direct support for license readiness scoring and allocation decisions |
| **[3.1 Copilot Audit Logging](../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md)** | PAX, AI-in-One Dashboard, CopilotChatAnalytics | PAX automates export; the dashboards consume audit data for governance reporting |
| **[3.12 Evidence Collection](../../controls/pillar-3-compliance/3.12-evidence-collection.md)** | PAX | Helps produce repeatable audit export packages for examinations and internal reviews |
| **[4.5 Usage Analytics](../../controls/pillar-4-operations/4.5-usage-analytics.md)** | AI-in-One Dashboard, CopilotChatAnalytics, M365UsageAnalytics | Supports usage, readiness, and adoption reporting beyond native admin views |
| **[4.6 Viva Insights Measurement](../../controls/pillar-4-operations/4.6-viva-insights-measurement.md)** | DecodingSuperUsage, superuserimpact, customizecopilot | Supports impact, adoption, and ROI measurement using Viva Insights-derived data |
| **[4.8 Cost Allocation](../../controls/pillar-4-operations/4.8-cost-allocation.md)** | M365UsageAnalytics, superuserimpact | Helps align license usage and measured value with cost allocation narratives |

---

## 5) Inclusion Guidance

- Treat these repositories as **external companion repositories**, not as solutions to recreate locally.
- Use **pointer-based documentation** to surface them in the framework where they strengthen an existing control or playbook.
- Use **Analytics Hub** as the discovery surface, but document the individual repositories that are actually relevant to the control.
- Cross-link mixed repos where appropriate:
  - `AI-in-One Dashboard` is valid for both CopilotGov and AgentGov
  - `CopilotChatAnalytics` is valid for CopilotGov and secondarily useful for AgentGov because it includes agent intelligence
  - `PAX` is valid for both frameworks as an audit export companion repo

---

## 6) Additional Resources

- [Analytics Hub](https://github.com/microsoft/Analytics-Hub)
- [AI-in-One Dashboard](https://github.com/microsoft/AI-in-One-Dashboard)
- [Copilot Chat & Agent Intelligence](https://github.com/microsoft/CopilotChatAnalytics)
- [M365 Copilot Readiness Report](https://github.com/microsoft/M365UsageAnalytics)
- [Decoding Super Usage](https://github.com/microsoft/DecodingSuperUsage)
- [Super User Impact](https://github.com/microsoft/superuserimpact)
- [CustomizeCopilot](https://github.com/microsoft/customizecopilot)
- [PAX](https://github.com/microsoft/PAX)

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
