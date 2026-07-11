# Copilot Surfaces Matrix

Feature-by-control applicability matrix showing which governance controls apply to each Microsoft 365 Copilot surface.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../disclaimer.md).

---

## How to Read This Matrix

| Cell Value | Meaning |
|------------|---------|
| **Supported** | The control category is fully applicable and enforceable for this Copilot surface |
| **Partial** | The control category applies with limitations — see notes for specifics |
| **N/A** | The control category is not applicable to this Copilot surface |
| **Planned** | Microsoft has announced planned support; not yet generally available |

---

## Matrix: Copilot Surface by Control Category

### Productivity Applications

| Copilot Surface | DLP | Sensitivity Labels | Conditional Access | Audit Logging | Retention | eDiscovery | Info Barriers | Comm Compliance | Admin Toggles |
|----------------|-----|-------------------|-------------------|---------------|-----------|------------|--------------|----------------|---------------|
| **Word** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Partial | Supported |
| **Excel** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Partial | Supported |
| **PowerPoint** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Partial | Supported |
| **OneNote** | Supported | Partial | Supported | Supported | Supported | Supported | Supported | N/A | Supported |
| **Loop** | Supported | Supported | Supported | Supported | Supported | Partial | Supported | N/A | Supported |
| **Whiteboard** | Partial | N/A | Supported | Supported | Partial | N/A | N/A | N/A | Supported |
| **Forms** | N/A | N/A | Supported | Supported | Supported | N/A | N/A | N/A | Supported |

### Communication Applications

| Copilot Surface | DLP | Sensitivity Labels | Conditional Access | Audit Logging | Retention | eDiscovery | Info Barriers | Comm Compliance | Admin Toggles |
|----------------|-----|-------------------|-------------------|---------------|-----------|------------|--------------|----------------|---------------|
| **Outlook** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| **Teams Chat** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| **Teams Meetings** | Supported | Partial | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| **Teams Phone** | Partial | N/A | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| **Teams Queues** | Partial | N/A | Supported | Supported | Supported | Supported | Supported | Supported | Supported |

### Collaboration Applications

| Copilot Surface | DLP | Sensitivity Labels | Conditional Access | Audit Logging | Retention | eDiscovery | Info Barriers | Comm Compliance | Admin Toggles |
|----------------|-----|-------------------|-------------------|---------------|-----------|------------|--------------|----------------|---------------|
| **SharePoint** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | N/A | Supported |
| **OneDrive** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | N/A | Supported |
| **Planner** | N/A | N/A | Supported | Supported | Supported | Partial | N/A | N/A | Supported |
| **Stream** | Partial | Supported | Supported | Supported | Supported | Partial | Supported | N/A | Supported |

### Intelligence Applications (Viva)

| Copilot Surface | DLP | Sensitivity Labels | Conditional Access | Audit Logging | Retention | eDiscovery | Info Barriers | Comm Compliance | Admin Toggles |
|----------------|-----|-------------------|-------------------|---------------|-----------|------------|--------------|----------------|---------------|
| **Viva Insights** | N/A | N/A | Supported | Supported | Partial | N/A | N/A | N/A | Supported |
| **Viva Engage** | Supported | Partial | Supported | Supported | Supported | Supported | Supported | Supported | Supported |

### AI-Native Surfaces

| Copilot Surface | DLP | Sensitivity Labels | Conditional Access | Audit Logging | Retention | eDiscovery | Info Barriers | Comm Compliance | Admin Toggles |
|----------------|-----|-------------------|-------------------|---------------|-----------|------------|--------------|----------------|---------------|
| **Copilot Chat (Basic)** | Partial | Partial | Supported | Supported | Partial | Partial | Partial | Partial | Supported |
| **Copilot Chat (Premium / Microsoft 365 Copilot)** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| **Microsoft 365 Copilot Search** | Partial | Partial | Supported | Supported | Partial | Partial | Supported | N/A | Supported |
| **Copilot Pages** | Supported | Supported | Supported | Supported | Supported | Supported | Partial | N/A | Supported |
| **Copilot Notebooks** | Supported | Partial | Supported | Supported | Supported | Supported | Partial | N/A | Supported |
| **Edit with Copilot (Agent Mode)** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Partial | Supported |
| **Copilot Cowork** | Supported | Supported | Supported | Supported | Supported | Partial | Supported | Partial | Supported |
| **Microsoft Scout (Frontier preview)** | Partial | Partial | Supported | Partial | Partial | Partial | Partial | N/A | Partial |
| **Copilot Tuning (preview)** | Partial | Partial | Supported | Supported | Partial | Partial | Partial | N/A | Supported |
| **Researcher** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| **Analyst** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Partial | Supported |

### Extensibility

| Copilot Surface | DLP | Sensitivity Labels | Conditional Access | Audit Logging | Retention | eDiscovery | Info Barriers | Comm Compliance | Admin Toggles |
|----------------|-----|-------------------|-------------------|---------------|-----------|------------|--------------|----------------|---------------|
| **Plugins** | Partial | N/A | Supported | Supported | Partial | Partial | N/A | N/A | Supported |
| **Graph Connectors** | Partial | Partial | Supported | Supported | Partial | Partial | N/A | N/A | Supported |
| **SharePoint declarative agents** | Partial | Partial | Supported | Supported | Partial | Partial | Partial | N/A | Supported |
| **Copilot Studio agents (declarative/custom)** | Partial | Partial | Supported | Supported | Partial | Partial | Partial | N/A | Supported |
| **Agent 365** | N/A | N/A | Supported | Supported | Partial | Partial | Partial | N/A | Supported |
| **Federated Connectors (MCP)** | Partial | N/A | Supported | Supported | Partial | Partial | N/A | N/A | Supported |

### Browser

| Copilot Surface | DLP | Sensitivity Labels | Conditional Access | Audit Logging | Retention | eDiscovery | Info Barriers | Comm Compliance | Admin Toggles |
|----------------|-----|-------------------|-------------------|---------------|-----------|------------|--------------|----------------|---------------|
| **Copilot in Edge** | Partial | N/A | Supported | Supported | Partial | Partial | N/A | N/A | Supported |

---

## Column Definitions

| Control Category | Description | Primary Admin Portal |
|-----------------|-------------|---------------------|
| **DLP** | Data Loss Prevention policies that scan Copilot interactions for sensitive content | Microsoft Purview |
| **Sensitivity Labels** | Information Protection labels that classify and protect Copilot inputs/outputs | Microsoft Purview |
| **Conditional Access** | Entra ID policies controlling who can access Copilot and under what conditions | Microsoft Entra |
| **Audit Logging** | Unified Audit Log capture of Copilot interaction events | Microsoft Purview |
| **Retention** | Retention policies governing how long Copilot interaction data is preserved | Microsoft Purview |
| **eDiscovery** | Ability to search and export Copilot interaction data for legal/regulatory purposes | Microsoft Purview |
| **Info Barriers** | Information barrier policies that restrict Copilot from crossing organizational walls | Microsoft Purview |
| **Comm Compliance** | Communication Compliance policies that flag Copilot-assisted communications for review | Microsoft Purview |
| **Admin Toggles** | Microsoft 365 admin center settings to enable/disable Copilot per application | Microsoft 365 admin center |

---

## Notes on Partial Support

### DLP

- **Whiteboard:** DLP does not inspect Whiteboard canvas content generated by Copilot. DLP applies to text shared from Whiteboard to other Microsoft 365 locations.
- **Teams Phone / Teams Queues:** DLP applies to voicemail transcription, call summaries, and queue-related artifacts but not to real-time voice content.
- **Copilot Chat (Basic):** DLP coverage is partial because Basic does not automatically ground responses in Microsoft Graph; controls apply to user-provided organizational data, uploaded files, prompts, and outputs where supported.
- **Copilot Search / Graph Connectors / SharePoint declarative agents / Copilot Studio agents:** DLP applies to content returned by Copilot but does not inspect data at the connector, search source, or agent source. Source-level DLP must be configured separately.
- **Copilot Tuning:** DLP applies to source data before tuning and to generated outputs; tuning dataset governance and model-risk review require additional controls.
- **Stream:** DLP applies to transcript content but not to the video content itself.

### Sensitivity Labels

- **OneNote:** Sensitivity labels apply at the notebook/section level; granular page-level Copilot labeling behavior may vary.
- **Copilot Notebooks:** Sensitivity label support is limited compared with Copilot Pages; test manual labels, auto-labeling, and label-based DLP before relying on labels as the primary control.
- **Teams Meetings:** Sensitivity labels apply to meeting transcripts and summaries; real-time meeting content does not carry labels.
- **Viva Engage:** Labels apply to attachments shared via Copilot but not to Engage conversation content directly.
- **Copilot Search / Graph Connectors / declarative agents:** Label inheritance applies to content surfaced from labeled Microsoft 365 sources, but external connector content may not carry labels.
- **Copilot Tuning:** Labels on source data should be reviewed before material is used for tuning; tuned-agent outputs may require separate labeling decisions.

### Retention and eDiscovery

- **Whiteboard:** Whiteboard Copilot content retention depends on the underlying storage location.
- **Copilot Pages / Copilot Notebooks:** Content is stored in SharePoint Embedded and should be covered through SharePoint retention and eDiscovery procedures. Individually deleted Copilot Notebooks do not have an end-user or admin item-level recycle bin under current Microsoft Learn guidance.
- **Planner / Plugins / Graph Connectors / agents:** Copilot interaction data for these surfaces is captured in the Unified Audit Log but may have limited direct retention and eDiscovery support depending on the storage location of generated content.
- **Agent 365:** Inventory and policy actions are governance records; generated business content remains governed by the host app, agent source, or output storage location.
- **Viva Insights:** Insights data follows separate privacy and retention controls managed through Viva admin settings.

### Information Barriers

- **Copilot Pages / Copilot Notebooks:** Information Barriers are not currently supported for SharePoint Embedded content; use Cloud Policy scoping or disable these surfaces for IB-sensitive populations.
- **Declarative agents:** Information barrier enforcement depends on the data sources configured in the agent; IB policies apply to the underlying Microsoft 365 content but agent-level enforcement may be partial.

### Communication Compliance

- **Word / Excel / PowerPoint:** Communication Compliance applies to content shared via Copilot in collaboration scenarios (e.g., shared documents) but does not inspect content during local authoring.
- **Edit with Copilot (Agent Mode):** Communication Compliance applies to content shared from documents created or modified via Agent Mode but does not inspect content during the multi-step editing session itself.
- **Copilot Cowork / Analyst:** Communication Compliance coverage for autonomously generated content may be limited to the final output shared by the user; intermediate processing steps may not be individually inspected.
- **Microsoft Scout (Frontier preview):** Communication Compliance is **not supported** for Scout activity. Scout is an endpoint agent whose local automation instructions, MCP output, and third-party inference occur outside the M365 DPA; Communication Compliance policies do not apply to that surface. Scout activity that touches M365 content and is later shared inherits Comm Compliance coverage for the destination surface (e.g., Teams, Outlook), not for the Scout session itself.
- **Teams Queues:** Communication Compliance coverage depends on how queue messages, transcripts, summaries, and follow-up artifacts are stored.

### eDiscovery

- **Copilot Cowork:** eDiscovery coverage for Cowork task outputs depends on how the generated content is stored and shared. Intermediate work products may have limited eDiscovery support.
- **Microsoft Scout (Frontier preview):** eDiscovery coverage is **partial**. Session and memory data stored in OneDrive are subject to existing OneDrive eDiscovery. **Automation instructions and MCP-server output are stored locally on the endpoint** and are outside the M365 DPA — they are not captured by Purview eDiscovery. Content processed through GitHub Copilot and third-party model providers is outside M365 residency and eDiscovery. Treat local artifact preservation as a known unsupported evidence gap (Control 4.16) rather than assuming Purview coverage.
- **Copilot Tuning:** Preserve tuning requests, approvals, source data lineage, and tuned-agent outputs through model-risk and records procedures where applicable.

### Basic vs Premium Access

Microsoft distinguishes between **Copilot Chat Basic** (no additional Copilot license; web grounding and user-provided organizational data) and **Copilot Chat Premium / Microsoft 365 Copilot** (add-on license; Microsoft Graph grounding and advanced app experiences). The following surfaces are affected:

| Surface | Basic Access | Premium Access |
|---------|-------------|---------------|
| **Copilot Chat** | Available; web grounding and user-provided organizational data only, without automatic tenant-wide Microsoft Graph grounding | Available with Microsoft Graph grounding across permitted organizational data |
| **Microsoft 365 Copilot Search** | Not available | Available to eligible licensed users from the Search module in the Microsoft 365 Copilot app |
| **Edit with Copilot (Agent Mode)** | Available with web data grounding only | Available with organizational data via Microsoft Graph |
| **Copilot Pages / Copilot Notebooks** | Available where tenant policy and app entitlement permit; content created from Basic chats is not automatically Graph-grounded | Available with Microsoft Graph-grounded content and SharePoint Embedded storage |
| **Copilot Cowork** | Not available | Available |
| **Microsoft Scout (Frontier preview)** | Not available | Not part of the standard M365 Copilot license; requires Frontier enrollment + Intune endpoint policy (imported `microsoft-scout` ADMX/ADML with **Allow Microsoft Scout Frontier access** plus documented ADMX admin controls) + admin attestation + an active **Microsoft 365 Copilot license** + a per-user **GitHub Copilot Business or Enterprise** entitlement on a linked GitHub account. Installation requires local Administrator permissions on the endpoint — prefer system-context managed deployment through Intune over standing local admin. |
| **Researcher** | Not available | Available |
| **Analyst** | Not available | Available |
| **Copilot Tuning (preview)** | Not available | Available only for eligible tenants with at least 5,000 Microsoft 365 Copilot licenses during preview |
| **Agent 365** | Admin surface, not a Basic user feature | Admin surface for governing deployed agents across eligible agent sources |

Governance controls in this matrix apply most fully to Premium access where Microsoft Graph-grounded organizational data is involved. Basic access carries lower automatic Graph-discovery risk but still requires supervision for user-provided organizational data, generated content, and web-sourced outputs.

---

## Using This Matrix for Governance Planning

1. **Identify your priority Copilot surfaces** — which Microsoft 365 apps will your organization enable Copilot in first?
2. **Check "Supported" columns** for those surfaces to understand which controls are fully enforceable
3. **Review "Partial" entries** to identify governance gaps that may require compensating controls
4. **Plan for "Planned" items** in your roadmap — these capabilities are expected but not yet available
5. **Cross-reference with** the [Copilot Admin Toggles](copilot-admin-toggles.md) to configure app-level enablement

---

*FSI Copilot Governance Framework v1.8.0 - July 2026*
