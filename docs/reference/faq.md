# Frequently Asked Questions

Answers to common questions about Microsoft 365 Copilot governance in financial services environments.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../disclaimer.md).

---

## Copilot Permissions and Access

### Does Copilot have elevated access to organizational data?

**No.** Microsoft 365 Copilot operates entirely within the calling user's existing Microsoft 365 permissions. Copilot does not have its own service account, does not bypass access controls, and cannot access content the user does not already have permission to view.

When a user asks Copilot a question, Copilot queries the Microsoft Graph using that user's identity and permissions. If the user cannot access a SharePoint site, Copilot cannot access it either. If the user does not have permission to view a document, Copilot will not surface content from that document.

**The key governance risk** is not that Copilot has elevated access, but that many organizations have broader permissions than they realize. Copilot makes existing permission gaps more visible through a phenomenon called "discovery amplification" — content that was technically accessible but practically undiscoverable via traditional search becomes easier to surface through natural language queries. This is why the [Quick Start Guide](../getting-started/quick-start.md) begins with an oversharing assessment.

**Relevant controls:** Control 1.1 (Copilot Readiness Assessment), Control 1.2 (SharePoint Oversharing Detection), Control 1.14 (Item-Level Permission Scanning), Control 1.15 (Permissions Drift Detection)

---

### Can I disable Copilot for specific users?

**Yes.** There are several approaches:

1. **License-based control (recommended):** Only assign Microsoft 365 Copilot licenses to approved users or groups. Users without a Copilot license cannot use Copilot features. Use group-based license assignment in Microsoft Entra to manage this at scale.

2. **Per-app toggles:** Disable Copilot in specific M365 applications (e.g., enable in Word and Outlook but disable in Teams meetings) via the M365 Admin Center.

3. **Conditional Access:** Create Entra ID Conditional Access policies to block Copilot access based on conditions (device compliance, location, user risk level).

4. **Service plans:** Within the Copilot license, individual service plans can be disabled to remove specific capabilities.

**Recommended approach for FSI:** Use group-based licensing with a phased rollout. Start with a pilot group, expand to low-risk use cases, then broaden as governance controls mature.

**Relevant controls:** Control 1.9 (License Planning), Control 4.1 (Copilot Admin Settings), Control 4.2 (Teams Meetings Governance)

---

## Copilot Licensing and Access

### What is the difference between Copilot Chat Basic and Premium?

**Copilot Chat (Basic)** is the free tier available to all Microsoft 365 users via the web (copilot.microsoft.com) and Outlook. It uses web data only and does not access organizational data through the Microsoft Graph.

**Copilot Chat (Premium)** requires a Microsoft 365 Copilot license and provides full access to organizational data via Microsoft Graph, priority access, and advanced features across all Microsoft 365 apps.

As of April 15, 2026, organizations with more than 2,000 users lose embedded Copilot Chat in Word, Excel, PowerPoint, and OneNote for unlicensed users. FSI organizations should review license allocation strategies and communicate access changes to affected users.

**Relevant controls:** Control 1.9 (License Planning), Control 4.1 (Copilot Admin Settings)

---

### What is Edit with Copilot (Agent Mode) and does it require a license?

Edit with Copilot (formerly Agent Mode) is an iterative document creation experience in Word, Excel, and PowerPoint. It is available to all Microsoft 365 users regardless of Copilot license status. However, unlicensed users can only use web data sources — organizational data requires a paid Copilot license.

FSI organizations should review whether web-sourced content meets their governance and supervision requirements, particularly for client-facing document generation.

**Relevant controls:** Control 4.1 (Copilot Admin Settings), Control 1.13 (User Training)

---

### Can users access third-party AI models through Copilot?

Microsoft has introduced support for third-party model providers including Anthropic Claude and xAI. Administrators can enable these models for specific users or groups via M365 Admin Center > Copilot > Settings > Other settings.

FSI organizations should evaluate the data handling, residency, and regulatory implications before enabling third-party models, as they may introduce additional data processing outside Microsoft's standard compliance boundary. Organizations should verify that third-party model usage aligns with their existing vendor risk management and data governance policies.

**Relevant controls:** Control 4.1 (Copilot Admin Settings), Control 2.6 (Web Search and Web Grounding Controls)

---

### Do Information Barriers apply to Copilot Pages and Notebooks?

**No.** Information Barriers are currently **not** supported for SharePoint Embedded content, which includes Copilot Pages and Copilot Notebooks. This is a significant consideration for FSI organizations with Chinese wall requirements.

Organizations should implement alternative controls such as restricting Copilot Pages creation for populations subject to information barriers. Use Microsoft 365 Cloud Policy to disable Copilot Pages and Notebooks for affected user groups.

**Relevant controls:** Control 2.4 (Information Barriers for Copilot), Control 4.1 (Copilot Admin Settings)

---

## Data Storage and Privacy

### Where is Copilot interaction data stored?

Microsoft 365 Copilot interaction data is stored within the Microsoft 365 compliance boundary:

| Data Type | Storage Location | Retention |
|-----------|-----------------|-----------|
| **Microsoft 365 Copilot Chat conversations** | User's Exchange Online mailbox (hidden folder) | Subject to Exchange retention policies |
| **Copilot in Teams chat** | Teams chat storage (Azure-based) | Subject to Teams retention policies |
| **Copilot in Teams meetings** | Meeting transcript storage (Exchange/SharePoint) | Subject to meeting retention policies |
| **Copilot in Outlook** | Exchange Online (within the email context) | Subject to Exchange retention policies |
| **Copilot in Word/Excel/PPT** | No persistent storage of the Copilot interaction itself; generated content saved by user is stored in the document | Subject to SharePoint/OneDrive retention policies |
| **Copilot Pages** | User-owned SharePoint Embedded container | Subject to SharePoint retention policies and manual legal hold workflows |
| **Audit logs (CopilotInteraction events)** | Unified Audit Log | Subject to audit log retention policies (180 days standard, up to 10 years with Audit Premium) |

**Data residency:** Copilot interaction data is stored in the same geographic region as the user's Microsoft 365 data. Copilot processing (LLM inference) occurs within the Microsoft 365 service boundary and is subject to the same data processing commitments.

**Relevant controls:** Control 3.1 (Copilot Audit Logging), Control 3.2 (Retention Policies)

---

### Does Copilot web search share organizational data externally?

**When web search is enabled:** Copilot may send search queries to Bing to retrieve additional grounding information. Microsoft states that these queries do not include the full user prompt or organizational data — they are derived search queries. However, the queries themselves could potentially reveal information about the user's intent.

**FSI recommendation:** Disable web search for Copilot in regulated environments. This is a Baseline governance recommendation in this framework for all FSI organizations. With web search disabled, Copilot responses are grounded exclusively in organizational data from the Microsoft Graph.

**How to disable:** M365 Admin Center > Copilot > Settings > Data access > Web search > Turn off.

**Relevant controls:** Control 2.6 (Web Search and Web Grounding Controls). See also: [Copilot Admin Toggles](copilot-admin-toggles.md)

---

## Auditing and Compliance

### How do I audit Copilot usage?

Copilot usage can be audited through several mechanisms:

1. **Unified Audit Log:** Search for `CopilotInteraction` events in Microsoft Purview. These events capture when Copilot was invoked, the application context, and metadata about the interaction. Audit (Premium) provides higher-fidelity events including referenced content sources.

2. **Copilot Usage Reports:** M365 Admin Center > Reports > Usage > Microsoft 365 Copilot. Provides aggregated usage metrics (active users, feature adoption) without individual interaction content.

3. **DSPM for AI:** Microsoft Purview > DSPM for AI provides a dashboard showing Copilot interaction volume, sensitive data exposure in Copilot interactions, and risk indicators.

4. **Microsoft Sentinel:** For enterprise-scale monitoring, stream Copilot audit data to Sentinel for correlation with other security events, custom analytics rules, and automated incident response.

5. **Viva Insights Copilot Dashboard:** Provides organizational-level Copilot adoption and productivity metrics for leadership reporting.

**For regulatory record-keeping (FINRA 4511, SEC 17a-4):** The Unified Audit Log with Audit (Premium) retention is the primary mechanism. Configure retention policies to meet your specific regulatory retention periods (typically 3-6 years).

**Relevant controls:** Control 3.1 (Copilot Audit Logging), Control 3.9 (AI Disclosure and Transparency), Control 4.6 (Copilot Analytics), Control 4.11 (Sentinel Integration)

---

### What retention policies apply to Copilot interactions?

Copilot interaction data is subject to the same Microsoft Purview retention policies as the underlying M365 service:

| Copilot Context | Retention Governed By | Policy Location |
|----------------|----------------------|-----------------|
| Microsoft 365 Copilot Chat | Exchange Online Copilot retention policy | Purview > Data lifecycle management > Retention policies > Copilot |
| Teams chat | Teams chat retention policy | Purview > Data lifecycle management > Retention policies > Teams |
| Teams meetings | Teams meeting/transcript retention policy | Purview > Data lifecycle management > Retention policies > Teams |
| Outlook | Exchange Online retention policy | Purview > Data lifecycle management > Retention policies > Exchange |
| Copilot Pages | SharePoint retention policy | Purview > Data lifecycle management > Retention policies > All SharePoint Sites |
| Audit logs | Audit log retention policy | Purview > Audit > Audit retention policies |

**FSI-specific considerations:**

- FINRA 4511 requires certain records for 3-6 years
- SEC 17a-4 requires 3-6 years depending on record type
- Configure Purview retention policies with "Retain" actions for the required period
- Use "Retain and then delete" for data minimization after the retention period expires
- Audit (Premium) supports retention of audit log data for up to 10 years

**Relevant controls:** Control 3.2 (Retention Policies), Control 3.11 (Record Keeping)

---

## Governance Features

### How does DSPM for AI relate to Copilot governance?

DSPM for AI (Data Security Posture Management for AI) is a Microsoft Purview capability specifically designed to help organizations govern AI usage including Microsoft 365 Copilot. It provides:

1. **Visibility:** Dashboard showing how Copilot is being used across the organization, including interaction volume by app, user group, and time period.

2. **Data risk assessment:** Identifies when Copilot interactions involve sensitive data (based on sensitivity labels and sensitive information types), helping security teams understand data exposure patterns.

3. **Policy recommendations:** Suggests DLP policies, sensitivity labels, and other controls to improve Copilot data security posture.

4. **Compliance monitoring:** Ongoing monitoring that helps detect anomalous patterns in Copilot usage that may indicate data handling concerns.

DSPM for AI complements (does not replace) the broader governance controls in this framework. Think of it as a monitoring and assessment layer that helps you measure the effectiveness of your DLP, labeling, and access control implementations.

**Requirements:** Microsoft Purview Suite (formerly E5 Compliance) + Microsoft 365 Copilot license.

**Relevant controls:** Control 1.2 (SharePoint Oversharing Detection), Control 3.9 (AI Disclosure and Transparency)

---

### What is the difference between FSI-CopilotGov and FSI-AgentGov?

These are companion frameworks that address different aspects of Microsoft 365 AI governance:

| Aspect | FSI-CopilotGov (this framework) | FSI-AgentGov |
|--------|--------------------------------|--------------|
| **Subject** | Microsoft 365 Copilot — the AI assistant embedded in M365 apps | Copilot Studio, Agent Builder, SharePoint agents, and custom AI agents |
| **Scope** | In-app AI assistance across 23+ M365 surfaces | Custom and declarative agent development, deployment, and lifecycle |
| **Governance model** | Baseline / Recommended / Regulated levels | Zone 1 (Personal) / Zone 2 (Team) / Zone 3 (Enterprise) agents |
| **Key concepts** | Semantic Index, Graph grounding, discovery amplification, label inheritance | Managed Environments, DLP connector policies, agent lifecycle, agent inventory |
| **Controls** | 58 controls across 4 lifecycle pillars | 71 controls across 4 governance domains |
| **Playbooks** | 216 implementation playbooks | 284 implementation playbooks |
| **Repository** | [FSI-CopilotGov](https://github.com/judeper/FSI-CopilotGov) | [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov) |

**Overlap:** Both frameworks address sensitivity labels, audit logging, DLP, and Conditional Access — but each provides guidance tailored to its specific scope. The frameworks are standalone with no cross-repo dependencies.

**Which do you need?**

- Deploying M365 Copilot (Word, Teams, Outlook, Microsoft 365 Copilot Chat, etc.)? Start with FSI-CopilotGov.
- Building custom agents in Copilot Studio or Agent Builder? Start with FSI-AgentGov.
- Doing both? Use both frameworks independently — they are designed to complement each other.

---

## Common Concerns

### Will Copilot generate inaccurate financial information?

Copilot, like all large language models, can generate inaccurate or "hallucinated" content. This is a known characteristic of LLMs, not a bug. The risk is particularly relevant in FSI contexts where inaccurate information in client communications, regulatory filings, or financial calculations could have material consequences.

**Mitigations in this framework:**

- **Communication Compliance (Control 3.4):** Flags Copilot-assisted communications for supervisory review before they reach clients
- **FINRA 2210 review process (Control 3.5):** Principal pre-approval requirements for Copilot-drafted retail communications
- **Model Risk Management (Control 3.8):** Documents Copilot in the model inventory with risk assessment and validation procedures
- **User Training (Control 1.13):** Educates users that Copilot output must be reviewed and validated before use in any business context

**Key principle:** Copilot is an assistant, not an autonomous agent. Users remain responsible for reviewing and validating all Copilot-generated content before using it in business contexts.

---

### Can Copilot access data across information barriers?

**No.** Microsoft 365 Copilot respects Information Barrier (IB) policies configured in Microsoft Purview. If a user is in an IB segment that is blocked from communicating with another segment, Copilot will not surface content from the blocked segment's SharePoint sites, Teams channels, or other M365 data.

**Important caveats:**

- IB enforcement in Copilot depends on IB policies being properly configured and applied across all relevant M365 services (Teams, SharePoint, OneDrive)
- IB enforcement for Copilot extensibility features (plugins, Graph connectors, declarative agents) may have limitations — see the [Copilot Surfaces Matrix](copilot-surfaces-matrix.md) for details
- IB policies should be tested with Copilot scenarios before relying on them for MNPI compliance

**Relevant controls:** Control 2.4 (Information Barriers for Copilot)

---

### How do sensitivity labels interact with Copilot?

Sensitivity labels interact with Copilot in three key ways:

1. **Label inheritance:** When Copilot generates content based on one or more labeled source documents, the output inherits the highest sensitivity label. If Copilot references both an "Internal" document and a "Highly Confidential" document, the generated content receives the "Highly Confidential" label.

2. **Encryption enforcement:** If a sensitivity label includes encryption settings, Copilot respects those settings. Users who do not have decryption rights cannot use Copilot to access the encrypted content.

3. **DLP integration:** DLP policies can use sensitivity labels as conditions. For example, a DLP policy can block Copilot from processing "Highly Confidential" content in certain contexts.

**FSI best practice:** Implement mandatory labeling for at least Word, Excel, PowerPoint, and Outlook so that all content Copilot may reference has a classification. This provides a foundation for both label inheritance and DLP policy enforcement.

**Relevant controls:** Control 2.2 (Sensitivity Labels and Label Inheritance), Control 2.1 (DLP Policies)

---

### Is Copilot compliant with my regulatory requirements?

Copilot is a technology tool — it is neither compliant nor non-compliant on its own. **Your organization's configuration, policies, and governance practices** determine whether your use of Copilot supports compliance with applicable regulations.

This framework provides controls and implementation guidance that help FSI organizations configure Copilot in ways that support compliance with FINRA, SEC, SOX, GLBA, OCC, CFPB, and FFIEC requirements. However:

- No single tool or configuration can guarantee regulatory compliance
- Regulatory requirements must be interpreted in the context of your specific business activities
- Implementation must be validated by your compliance and legal teams
- Ongoing monitoring and governance are required — compliance is not a one-time configuration

**Starting point:** Use the [Regulatory Mappings](regulatory-mappings.md) to identify which controls are relevant to your regulatory obligations, then use the [Implementation Checklist](../getting-started/checklist.md) to track your progress.

---

### What happens if Microsoft changes Copilot features?

Microsoft regularly updates Microsoft 365 Copilot with new features, changed behaviors, and updated admin controls. This is a governance risk that must be actively managed.

**How to stay informed:**

- Monitor the **M365 Message Center** (M365 Admin Center > Health > Message center) for Copilot-related announcements
- Subscribe to the **Microsoft 365 Roadmap** ([https://www.microsoft.com/en-us/microsoft-365/roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap)) for upcoming features
- Review **Microsoft Purview release notes** for changes to compliance capabilities
- Participate in **Microsoft FSI community calls** for industry-specific guidance

**Governance response:** Control 4.12 (Change Management for Copilot Updates) provides a structured process for evaluating, testing, and approving Copilot feature changes in your environment.

**Key risk:** New Copilot features often default to "On." When Microsoft releases a new capability, it may be available to users before your governance team has evaluated it. The governance calendar (Control 4.12) should include regular review of Message Center notifications for Copilot-related changes.

---

*FSI Copilot Governance Framework v1.4.0 - April 2026*
