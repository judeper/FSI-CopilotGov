# Glossary

Definitions of key terms, products, regulations, and concepts used throughout the FSI Copilot Governance Framework.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../disclaimer.md).

---

## Products and Services

### Agent 365
Microsoft's centralized platform for monitoring, managing, and configuring Copilot agents across Microsoft 365 apps, Copilot Studio, and third-party integrations.

### Agent Mode
See *Edit with Copilot*.

### Azure Information Protection (AIP)
Microsoft's cloud-based solution for classifying and protecting documents and emails by applying labels. Sensitivity labels in Microsoft Purview are the successor to AIP labels; the underlying encryption and rights management capabilities remain.

### Microsoft 365 Copilot Chat
The free Microsoft 365 Copilot chat experience (accessed via microsoft365.com/chat or the Microsoft 365 Copilot app) that can query across all Microsoft 365 data a user has access to via the Microsoft Graph. Copilot Chat grounds its responses in organizational data from Exchange, SharePoint, OneDrive, Teams, and other M365 services. Included with any Microsoft 365 subscription; does not require a per-user Copilot license. For the licensed experience with full work data grounding, see Microsoft 365 Copilot.

### Copilot Chat (Basic)
The free tier of Copilot Chat available to all Microsoft 365 users via the web (copilot.microsoft.com) and inside Outlook. In-app access in Word, Excel, PowerPoint, and OneNote is limited or removed for large organizations (>2,000 users) as of April 15, 2026.

### Copilot Chat (Premium)
The paid tier of Copilot Chat included with a Microsoft 365 Copilot license. Provides full access to organizational data via Microsoft Graph, priority access, and advanced features across all Microsoft 365 apps.

### Copilot Cowork
A Copilot capability that enables delegation of multi-step business tasks to Copilot, with users able to monitor and intervene in the process.

### Copilot Pages
A collaborative AI-powered canvascreated from Microsoft 365 Copilot Chat responses. Users can convert a Copilot response into a Page for further editing and sharing. Copilot Pages (`.page` files) are stored in a user-owned SharePoint Embedded container shared with Copilot Notebooks and Loop My workspace, and creation is governed through Microsoft 365 Cloud Policy.

### Declarative Agents
Custom Copilot agents defined through configuration (not code) that scope Copilot's behavior to specific data sources, instructions, and capabilities. Can be created in Copilot Studio, SharePoint, or Teams developer tools.

### DSPM for AI (Data Security Posture Management for AI)
A Microsoft Purview capability that provides visibility into AI usage across the organization, identifies data risks related to AI interactions, and helps manage AI-related compliance. Accessible via the Purview AI hub.

### Edit with Copilot
Formerly known as "Agent Mode." An iterative, multi-step document creation and refinement experience in Word, Excel, and PowerPoint. Available to all Microsoft 365 users; unlicensed users are limited to web data sources only.

### Entra Agent ID
A unique identity assigned to Copilot agents in Microsoft Entra ID, enabling security and compliance tracking, policy enforcement, and audit trail for agent activities.

### Graph Connectors
Connectors that bring external data(from third-party systems, databases, or file shares) into the Microsoft Graph, making that data searchable and available to Copilot for grounding. Each connector requires security review as it expands Copilot's data access surface.

### Microsoft 365 Copilot
Microsoft's AI assistant embedded across Microsoft 365 applications. Copilot uses large language models (LLMs) grounded in organizational data accessed through the Microsoft Graph. It operates within the user's existing permission boundaries.

### Microsoft Defender for Cloud Apps
A Cloud Access Security Broker (CASB) that provides visibility, control, and threat protection for cloud services including Microsoft 365. Used to create session policies that can monitor and control Copilot interactions in web sessions.

### Microsoft Entra ID
Microsoft's cloud-based identity and access management service. Provides Conditional Access, identity protection, and access governance capabilities used to control who can access Copilot and under what conditions.

### Microsoft Graph
The unified API and data model that connects Microsoft 365 services. Copilot uses the Microsoft Graph to access emails, files, chats, meetings, and other organizational data when generating responses. Users' existing permissions govern what Graph data Copilot can access.

### Microsoft Purview
Microsoft's unified data governance, risk, and compliance platform. Includes information protection (sensitivity labels), DLP, audit, retention, eDiscovery, communication compliance, information barriers, insider risk management, and DSPM for AI.

### Microsoft Sentinel
Microsoft's cloud-native Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) solution built on Azure. Used to collect, analyze, and respond to Copilot audit data at enterprise scale.

### Plugins
Extensions that allow Copilot to interact with external services and APIs during a conversation. Plugins can retrieve real-time data, perform actions, or connect to line-of-business applications. Each plugin requires governance review for data handling and security.

### Restricted SharePoint Search (RSS)
A SharePoint Admin Center setting that limits Copilot Chat's grounding to a curated list of up to 100 SharePoint sites. Useful during oversharing remediation or for environments requiring tight control over which content Copilot can access in Copilot Chat.

### Semantic Index
Microsoft's AI-powered index that enhances Microsoft 365 search and Copilot grounding by understanding the meaning and relationships in organizational content. The Semantic Index processes content that users already have access to and respects existing permissions.

### SharePoint Advanced Management (SAM)
An add-on for SharePoint that provides advanced governance capabilities including oversharing reports, data access governance reports, inactive site policies, and site lifecycle management. Important for pre-deployment Copilot readiness assessments.

### Viva Insights
Part of the Microsoft Viva suite providing productivity and wellbeing insights. Includes a Copilot dashboard showing organizational Copilot adoption and usage patterns. Used for Copilot governance monitoring and license optimization.

### Viva Engage
Enterprise social networking service within Microsoft Viva (formerly Yammer). Copilot in Viva Engage assists with drafting posts and summarizing discussions.

### Work IQ
A Copilot capability that provides persistent organizational memory, allowing Copilot to prioritize and personalize assistance based on team context and previous work.

---

## Governance and Security Concepts

### Auto-labeling
The ability to automatically apply sensitivity labels to content based on sensitive information type detection or other conditions, without requiring user action. Includes client-side auto-labeling (label recommendation) and service-side auto-labeling (automatic application).

### Conditional Access
Microsoft Entra ID policies that control access to cloud applications based on conditions such as user identity, device compliance, location, sign-in risk, and application sensitivity. Used to require specific conditions (e.g., compliant device, MFA) for Copilot access.

### Communication Compliance
A Microsoft Purview solution that helps organizations detect, capture, and act on potentially inappropriate messages. In FSI contexts, used to implement FINRA 3110 supervisory review requirements for Copilot-assisted communications.

### Data Loss Prevention (DLP)
Microsoft Purview policies that identify, monitor, and protect sensitive information across Microsoft 365 services. DLP policies can be applied to the Microsoft 365 Copilot location to scan Copilot interactions for sensitive content.

### Discovery Amplification
The phenomenon where Copilot makes existing permissions problems more visible and impactful. If a user has access to content they should not see (due to overly broad permissions), Copilot can surface that content more readily than traditional search. This is not a Copilot security flaw — it is an amplification of existing permission gaps.

### eDiscovery
The process of identifying, collecting, producing, and reviewing electronically stored information (ESI) for legal, regulatory, or investigative purposes. Microsoft Purview eDiscovery enables searching and exporting Copilot interaction data.

### Editor
A sensitivity label permission level (formerly "Co-author") that grants users edit rights to labeled content. As of April 2026, the Editor permission no longer includes "Save as, Export" permissions for sensitivity labels. See also *Restricted Editor*.

### Graph Grounding
The process by which Copilot retrievesrelevant organizational data from the Microsoft Graph to inform its responses. Grounding data includes emails, documents, chats, meetings, and other M365 content the user can access.

### Information Barriers (IB)
Microsoft Purview policies that restrict communication and collaboration between specific groups of users. In FSI, information barriers support compliance with MNPI walls between departments such as investment banking and research.

### Label Inheritance
The behavior where Copilot applies the highest sensitivity label from all source documents used to generate a response. For example, if Copilot references one "Internal" document and one "Confidential" document, the output inherits the "Confidential" label.

### Oversharing
A condition where Microsoft 365 content is accessible to more users than intended, typically due to broad SharePoint permissions (e.g., "Everyone except external users"), open M365 Group membership, or permissive OneDrive sharing defaults. Copilot amplifies the impact of oversharing through discovery amplification.

### RAG (Retrieval-Augmented Generation)
An AI architecture pattern where a language model retrieves relevant data from external sources (in Copilot's case, the Microsoft Graph) and incorporates it into generated responses. RAG enables Copilot to provide contextual, organization-specific answers rather than relying solely on its training data.

### Restricted Editor
Renamed sensitivity label permission level (formerly "Reviewer"). See also *Editor*.

### Sensitivity Labels
Classification labels applied to documents, emails, and other content that define how the content should be protected. Labels can enforce encryption, content marking (headers, footers, watermarks), access restrictions, and DLP policy matching.

### Zero Trust
A security model based on the principle of "never trust, always verify." Every access request is authenticated, authorized, and encrypted regardless of network location. Microsoft's Zero Trust architecture applies to Copilot governance through Conditional Access, device compliance, identity protection, and data classification.

---

## Regulatory Bodies and Regulations

### CFPB (Consumer Financial Protection Bureau)
Federal agency responsible for consumer protection in the financial sector. Issues guidance on unfair, deceptive, or abusive acts or practices (UDAAP) that may apply to AI-generated consumer communications.

### FDIC (Federal Deposit Insurance Corporation)
Federal agency that provides deposit insurance and examines state-chartered banks. Co-issuer of the 2023 Interagency AI Guidance.

### FFIEC (Federal Financial Institutions Examination Council)
Interagency body that prescribes uniform principles, standards, and examination procedures for federal financial institution regulators. The FFIEC IT Examination Handbook provides examination guidance that applies to AI governance.

### FINRA (Financial Industry Regulatory Authority)
Self-regulatory organization that oversees broker-dealers in the United States. Issues rules governing communications (2210), supervision (3110), and books and records (4511) that apply to Copilot usage.

### FINRA Rule 2210 — Communications with the Public
Governs content standards, approval requirements, and filing obligations for broker-dealer communications. Copilot-drafted communications to retail customers may be subject to principal pre-approval and content standards requirements.

### FINRA Rule 3110 — Supervision
Requires broker-dealers to establish and maintain written supervisory procedures and to supervise associated persons. Copilot interactions may fall within the scope of supervisory review requirements.

### FINRA Rule 4511 — General Requirements for Books and Records
Requires broker-dealers to make and preserve books and records as prescribed. Copilot interaction data may constitute records that must be retained and produced upon regulatory request.

### GLBA (Gramm-Leach-Bliley Act)
Federal law requiring financial institutions to explain their information-sharing practices and safeguard sensitive data. Section 501(b) requires institutions to develop a comprehensive information security program.

### Interagency AI Guidance (2023)
Joint guidance issued by OCC, Federal Reserve, and FDIC in 2023 on managing risks associated with AI in financial services. Addresses governance, risk management, third-party risk, data management, and consumer protection.

### OCC (Office of the Comptroller of the Currency)
Federal agency that charters, regulates, and supervises national banks and federal savings associations. Issues guidance including OCC Bulletin 2011-12 on model risk management.

### OCC Bulletin 2011-12 / Fed SR 11-7 — Model Risk Management
Guidance on sound model risk management practices for banking organizations. Copilot may be considered a "model" under this guidance, requiring inventory, validation, monitoring, and governance documentation.

### SEC (Securities and Exchange Commission)
Federal agency that regulates securities markets and protects investors. Issues rules governing record-keeping (17a-3/4), privacy (Reg S-P), and best interest (Reg BI).

### SEC Rule 17a-3 — Records to be Made
Specifies the records that broker-dealers must create and maintain, including memoranda of orders, trades, and written communications.

### SEC Rule 17a-4 — Records to be Preserved
Specifies retention periods and storage requirements for broker-dealer records. Requires 3-6 year retention depending on record type and WORM-compliant storage for electronic records.

### SEC Regulation Best Interest (Reg BI)
Requires broker-dealers to act in the best interest of retail customers. Imposes disclosure, care, conflict of interest, and compliance obligations that may apply when Copilot assists with client-facing recommendations.

### SEC Regulation S-P — Privacy of Consumer Financial Information
Requires broker-dealers, investment companies, and investment advisers to protect the security and confidentiality of customer records and information.

### SOX (Sarbanes-Oxley Act)
Federal law establishing requirements for public company financial reporting, internal controls, and corporate governance. Sections 302 and 404 require CEO/CFO certification of internal controls and auditor attestation.

### SR 11-7
Federal Reserve Supervision and Regulation Letter 11-7, "Guidance on Model Risk Management." Companion guidance to OCC 2011-12, providing identical model risk management expectations for Fed-supervised institutions.

### UDAAP (Unfair, Deceptive, or Abusive Acts or Practices)
Prohibition under federal consumer financial protection law against unfair, deceptive, or abusive acts or practices. AI-generated communications and recommendations may be evaluated under UDAAP standards.

---

## Acronyms

| Acronym | Definition |
|---------|-----------|
| AIP | Azure Information Protection |
| CA | Conditional Access |
| CASB | Cloud Access Security Broker |
| CFPB | Consumer Financial Protection Bureau |
| DLP | Data Loss Prevention |
| DSPM | Data Security Posture Management |
| EDM | Exact Data Match |
| ESI | Electronically Stored Information |
| FDIC | Federal Deposit Insurance Corporation |
| FFIEC | Federal Financial Institutions Examination Council |
| FINRA | Financial Industry Regulatory Authority |
| FSI | Financial Services Industry |
| GLBA | Gramm-Leach-Bliley Act |
| GRC | Governance, Risk, and Compliance |
| IB | Information Barriers |
| LLM | Large Language Model |
| MFA | Multi-Factor Authentication |
| MNPI | Material Nonpublic Information |
| OCC | Office of the Comptroller of the Currency |
| RAG | Retrieval-Augmented Generation |
| RSS | Restricted SharePoint Search |
| SAM | SharePoint Advanced Management |
| SEC | Securities and Exchange Commission |
| SIEM | Security Information and Event Management |
| SIT | Sensitive Information Type |
| SOAR | Security Orchestration, Automation, and Response |
| SOX | Sarbanes-Oxley Act |
| UDAAP | Unfair, Deceptive, or Abusive Acts or Practices |
| WORM | Write Once Read Many |

---

*FSI Copilot Governance Framework v1.3 - April 2026*
