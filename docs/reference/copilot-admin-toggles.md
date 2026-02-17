# Copilot Admin Toggles

Complete inventory of every admin toggle for Microsoft 365 Copilot, organized by category. Includes portal paths, default values, and FSI-recommended settings at each governance level.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../disclaimer.md).

---

## How to Use This Reference

- **Default** = Microsoft's out-of-box setting for new tenants
- **Baseline (B)** = Minimum FSI governance recommendation
- **Recommended (R)** = Best practice for most FSI production environments
- **Regulated (Reg)** = Setting for high-risk, examination-ready deployments
- Portal paths are current as of February 2026; Microsoft may update admin portal layouts

---

## Global Copilot Settings

**Portal:** M365 Admin Center > Settings > Microsoft 365 Copilot

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Microsoft 365 Copilot enabled | Settings > Microsoft 365 Copilot > Manage how your org uses Copilot | On | On | On | On | Master switch for Copilot availability across tenant |
| Copilot license auto-claim | Settings > Microsoft 365 Copilot > Licenses | On | Off | Off | Off | When On, users with eligible base licenses automatically receive Copilot. Turn Off to control rollout via group-based assignment. |
| Data, privacy, and security settings | Settings > Microsoft 365 Copilot > Data, privacy, and security | Default | Review | Review | Review | Review tenant-level data handling, storage, and processing commitments |
| Optional connected experiences | Settings > Org settings > Services > Microsoft 365 on the web | On | Off | Off | Off | Controls whether optional connected experiences (including some Copilot features) are available |

---

## Web Search Settings

**Portal:** M365 Admin Center > Settings > Microsoft 365 Copilot

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Web search in Copilot | Settings > Microsoft 365 Copilot > Web search | On | Off | Off | Off | When On, Copilot can query Bing for additional grounding data. Regulated FSI environments should disable this to prevent external data retrieval and potential data leakage in queries. |
| Web content in Microsoft 365 Copilot Chat responses | Settings > Microsoft 365 Copilot > Web search | On | Off | Off | Off | When On, Microsoft 365 Copilot Chat includes web-sourced information in responses. Disable to limit responses to organizational data only. |

---

## Per-App Settings: Teams

**Portal:** Teams Admin Center > Messaging policies / Meeting policies

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Copilot in Teams meetings | Teams Admin Center > Meetings > Meeting policies > [policy] > Copilot | On — during and after meeting | During and after | During and after | Only during meeting | Controls when Copilot is available. "Only during meeting" prevents post-meeting transcript access via Copilot, which may be required for MNPI controls. |
| Copilot in Teams chat | Teams Admin Center > Messaging policies > [policy] > Copilot | On | On | On | On | Enables Copilot summarization and drafting in Teams chat. Governance via DLP and Communication Compliance. |
| Copilot in Teams channels | Teams Admin Center > Messaging policies > [policy] > Copilot | On | On | On | On | Enables Copilot in channel conversations. Subject to Information Barriers. |
| Transcription for meetings | Teams Admin Center > Meetings > Meeting policies > [policy] > Transcription | On | On | On | On | Required for meeting Copilot to function. Disabling transcription disables meeting Copilot. |
| Meeting recap with Copilot | Teams Admin Center > Meetings > Meeting policies > [policy] > Recap | On | On | On | Off | Intelligent meeting recap uses Copilot. Disable in Regulated if post-meeting AI summaries are restricted. |
| Voice isolation | Teams Admin Center > Meetings > Meeting policies | Off | On | On | On | Reduces background noise; improves Copilot transcription accuracy for compliance record-keeping. |

---

## Per-App Settings: Outlook

**Portal:** M365 Admin Center > Settings > Microsoft 365 Copilot / Exchange Admin Center

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Copilot in Outlook | M365 Admin Center > Settings > Microsoft 365 Copilot > Apps that work with Copilot | On | On | On | On | Enables draft, summarize, and coaching features. Governed by DLP and sensitivity labels. |
| Copilot email coaching | M365 Admin Center > Settings > Microsoft 365 Copilot | On | On | On | Review | Provides tone and clarity coaching for email drafts. Review for Regulated to confirm coaching suggestions align with compliance communication standards. |
| Copilot email summarization | M365 Admin Center > Settings > Microsoft 365 Copilot | On | On | On | On | Summarizes email threads. Subject to DLP and sensitivity labels. |

---

## Per-App Settings: Word, Excel, PowerPoint

**Portal:** M365 Admin Center > Settings > Microsoft 365 Copilot

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Copilot in Word | Settings > Microsoft 365 Copilot > Apps that work with Copilot | On | On | On | On | Enables drafting, rewriting, summarizing. Subject to sensitivity label inheritance. |
| Copilot in Excel | Settings > Microsoft 365 Copilot > Apps that work with Copilot | On | On | On | On | Enables formula generation, data analysis, chart creation. Review for regulated data sets. |
| Copilot in PowerPoint | Settings > Microsoft 365 Copilot > Apps that work with Copilot | On | On | On | On | Enables slide generation from documents. Inherits sensitivity labels from source files. |

---

## Copilot Pages Settings

**Portal:** M365 Admin Center > Settings > Microsoft 365 Copilot

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Copilot Pages | Settings > Microsoft 365 Copilot > Copilot Pages | On | On | On | Review | When On, users can create Copilot Pages from Copilot Chat responses. Pages are stored in the user's OneDrive. Review for Regulated to assess data residency and retention implications. |
| Copilot Pages sharing | Settings > Microsoft 365 Copilot > Copilot Pages | Anyone in org | Specific people | Specific people | Specific people | Default sharing scope for newly created Pages. Set to "Specific people" to prevent unintended oversharing. |

---

## Extensibility Settings: Plugins and Connectors

**Portal:** M365 Admin Center > Settings > Integrated apps / Microsoft 365 Copilot

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| User-deployed plugins | Settings > Integrated apps > User-deployed apps | On | Off | Off | Off | When On, users can install their own Copilot plugins. Disable for governance control over plugin approvals. |
| Admin-deployed plugins | Settings > Integrated apps > Admin-deployed apps | Off | Off | Review | Review | Admin-deployed plugins are controlled centrally. Review plugins for data handling and security before deployment. |
| Third-party plugins | Settings > Microsoft 365 Copilot > Plugins | On | Off | Off | Off | When On, third-party plugins can be used in Copilot. Disable until a plugin governance review process is established. |
| Microsoft plugins | Settings > Microsoft 365 Copilot > Plugins | On | On | On | Review | First-party Microsoft plugins. Review individually for Regulated environments. |
| Graph connectors for Copilot | Settings > Microsoft 365 Copilot > Graph connectors | On | Review | Review | Off | Graph connectors bring external data into Copilot's grounding context. Review each connector's data classification. Disable in Regulated until connectors are individually approved. |

---

## Extensibility Settings: Declarative Agents

**Portal:** M365 Admin Center > Settings > Microsoft 365 Copilot / Integrated apps

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Declarative agents in Copilot | Settings > Microsoft 365 Copilot > Agents | On | Review | Review | Off | Allows declarative agents to be available in Copilot. Review agent capabilities and data access before enabling. |
| SharePoint declarative agents | SharePoint Admin Center > Settings > Copilot agents | On | Review | Review | Off | Allows site owners to create declarative agents scoped to SharePoint site content. Review for Regulated to assess data exposure. |
| User-created agents | Settings > Microsoft 365 Copilot > Agents | On | Off | Off | Off | When On, end users can create their own agents. Disable for FSI environments to maintain central governance. |

---

## Viva Settings

**Portal:** Viva Admin Center / M365 Admin Center

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Copilot in Viva Insights | Viva Admin Center > Insights > Copilot dashboard | On | On | On | Review | Provides Copilot usage analytics and productivity insights. Review for Regulated to assess employee privacy implications. |
| Copilot in Viva Engage | Viva Admin Center > Engage > Feature management | On | On | On | Review | Enables Copilot drafting and summarization in Viva Engage. Subject to DLP and Communication Compliance. |
| Copilot in Viva Learning | Viva Admin Center > Learning | On | On | On | On | Low-risk: assists with learning content recommendations. |
| Manager insights (Copilot data) | Viva Admin Center > Insights > Manager settings | On | Off | Off | Off | Provides managers with aggregated Copilot usage data for their team. Disable unless organizational policy permits manager-level AI usage visibility. |

---

## SharePoint Settings

**Portal:** SharePoint Admin Center

| Toggle | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Restricted SharePoint Search | SharePoint Admin Center > Settings > Search > Restricted SharePoint Search | Off | Review | Off | Review | When On, limits Copilot Chat grounding to a curated list of up to 100 SharePoint sites. Enable during oversharing remediation or for highly segmented environments. |
| SharePoint content access for Copilot | SharePoint Admin Center > Settings > Copilot | On | On | On | On | Global control for Copilot's ability to access SharePoint content. Permissions still apply. |

---

## Implementation Notes

### Priority Order for FSI Deployments

1. **Disable web search** — Prevents external data queries; most critical for regulated environments
2. **Disable user-deployed and third-party plugins** — Maintains central control over extensibility
3. **Set Copilot Pages sharing to "Specific people"** — Prevents accidental oversharing of AI-generated content
4. **Review meeting Copilot settings** — Configure transcript retention and meeting recap per your record-keeping requirements
5. **Disable user-created agents** — Maintains governance oversight of agent creation
6. **Review all "Review" items** against your institution's specific regulatory requirements

### Monitoring Toggle Changes

- Subscribe to **M365 Message Center** notifications for Copilot-related updates
- New toggles may be added by Microsoft with future Copilot feature releases
- Default values for new toggles are typically "On" — review promptly when announced
- See Control 4.10 (Change Management for Copilot Updates) for the recommended change tracking process

---

*FSI Copilot Governance Framework v1.0 - February 2026*
