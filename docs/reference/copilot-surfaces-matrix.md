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
| **Microsoft 365 Copilot Chat** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| **Copilot Pages** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | N/A | Supported |
| **Agent Mode / Edit with Copilot** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Partial | Supported |
| **Copilot Cowork** | Supported | Supported | Supported | Supported | Supported | Partial | Supported | Partial | Supported |
| **Researcher** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| **Analyst** | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Partial | Supported |

### Extensibility

| Copilot Surface | DLP | Sensitivity Labels | Conditional Access | Audit Logging | Retention | eDiscovery | Info Barriers | Comm Compliance | Admin Toggles |
|----------------|-----|-------------------|-------------------|---------------|-----------|------------|--------------|----------------|---------------|
| **Plugins** | Partial | N/A | Supported | Supported | Partial | Partial | N/A | N/A | Supported |
| **Graph Connectors** | Partial | Partial | Supported | Supported | Partial | Partial | N/A | N/A | Supported |
| **Declarative Agents** | Partial | Partial | Supported | Supported | Partial | Partial | Partial | N/A | Supported |
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
| **Admin Toggles** | M365 Admin Center settings to enable/disable Copilot per application | M365 Admin Center |

---

## Notes on Partial Support

### DLP

- **Whiteboard:** DLP does not inspect Whiteboard canvas content generated by Copilot. DLP applies to text shared from Whiteboard to other M365 locations.
- **Teams Phone:** DLP applies to voicemail transcription and call summaries but not to real-time voice content.
- **Plugins / Graph Connectors / Declarative Agents:** DLP applies to content returned by Copilot but does not inspect data at the connector or plugin source. Source-level DLP must be configured separately.
- **Stream:** DLP applies to transcript content but not to the video content itself.

### Sensitivity Labels

- **OneNote:** Sensitivity labels apply at the notebook/section level; granular page-level Copilot labeling behavior may vary.
- **Teams Meetings:** Sensitivity labels apply to meeting transcripts and summaries; real-time meeting content does not carry labels.
- **Viva Engage:** Labels apply to attachments shared via Copilot but not to Engage conversation content directly.
- **Graph Connectors / Declarative Agents:** Label inheritance applies to content surfaced from labeled M365 sources but external connector content may not carry labels.

### Retention and eDiscovery

- **Whiteboard:** Whiteboard Copilot content retention depends on the underlying storage location.
- **Planner / Plugins / Graph Connectors / Declarative Agents:** Copilot interaction data for these surfaces is captured in the Unified Audit Log but may have limited direct retention and eDiscovery support depending on the storage location of generated content.
- **Viva Insights:** Insights data follows separate privacy and retention controls managed through Viva admin settings.

### Information Barriers

- **Declarative Agents:** Information barrier enforcement for declarative agents depends on the data sources configured in the agent; IB policies apply to the underlying M365 content but agent-level enforcement may be partial.

### Communication Compliance

- **Word / Excel / PowerPoint:** Communication Compliance applies to content shared via Copilot in collaboration scenarios (e.g., shared documents) but does not inspect content during local authoring.
- **Agent Mode / Edit with Copilot:** Communication Compliance applies to content shared from documents created or modified via Agent Mode but does not inspect content during the multi-step editing session itself.
- **Copilot Cowork / Analyst:** Communication Compliance coverage for autonomously generated content may be limited to the final output shared by the user; intermediate processing steps may not be individually inspected.

### eDiscovery

- **Copilot Cowork:** eDiscovery coverage for Cowork task outputs depends on how the generated content is stored and shared. Intermediate work products may have limited eDiscovery support.

### Basic vs Premium Access

Microsoft distinguishes between **Basic** (unlicensed, web-data-only) and **Premium** (licensed, organizational data) Copilot access. The following surfaces are affected:

| Surface | Basic Access | Premium Access |
|---------|-------------|---------------|
| **Agent Mode / Edit with Copilot** | Available (web data grounding only) | Available (organizational data via Microsoft Graph) |
| **Copilot Cowork** | Not available | Available |
| **Researcher** | Not available | Available |
| **Analyst** | Not available | Available |
| **Microsoft 365 Copilot Chat** | Available (web data grounding only) | Available (organizational data via Microsoft Graph) |

Governance controls in this matrix apply primarily to **Premium** access where organizational data is involved. Basic access carries lower organizational data risk but may still require supervision for content generation and web-sourced outputs.

---

## Using This Matrix for Governance Planning

1. **Identify your priority Copilot surfaces** — which M365 apps will your organization enable Copilot in first?
2. **Check "Supported" columns** for those surfaces to understand which controls are fully enforceable
3. **Review "Partial" entries** to identify governance gaps that may require compensating controls
4. **Plan for "Planned" items** in your roadmap — these capabilities are expected but not yet available
5. **Cross-reference with** the [Copilot Admin Toggles](copilot-admin-toggles.md) to configure app-level enablement

---

*FSI Copilot Governance Framework v1.4.0 - April 2026*
