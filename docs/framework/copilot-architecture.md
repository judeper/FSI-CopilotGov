# Copilot Architecture

Technical deep-dive into Microsoft 365 Copilot architecture, data flows, and governance implications.

---

## Overview

Understanding the M365 Copilot architecture is essential for effective governance. This document describes how Copilot processes prompts, retrieves content, generates responses, and where governance controls intersect the data flow.

!!! info "Architecture Currency"
    Microsoft 365 Copilot architecture evolves with platform updates. This document reflects the architecture as of February 2026. Organizations should monitor Microsoft's official documentation for changes.

---

## Microsoft 365 Copilot Architecture Overview

Microsoft 365 Copilot is not a standalone product -- it is an orchestration layer that sits between the user, the Microsoft Graph, the Semantic Index, and a large language model (LLM).

```
+------------------------------------------------------------------+
|                    M365 COPILOT ARCHITECTURE                       |
|                                                                    |
|  +------------+                                                    |
|  |    User    |  Prompt: "Summarize the Q4 earnings deck"          |
|  +-----+------+                                                    |
|        |                                                           |
|        v                                                           |
|  +-----+------+                                                    |
|  | Copilot    |  Responsible AI filters                            |
|  | Orchest-   |  Content safety checks                             |
|  | rator      |  Prompt preprocessing                              |
|  +-----+------+                                                    |
|        |                                                           |
|        +-------------------+-------------------+                   |
|        |                   |                   |                   |
|        v                   v                   v                   |
|  +-----+------+    +------+------+    +-------+-----+             |
|  | Microsoft  |    |  Semantic   |    |  Web Search |             |
|  |   Graph    |    |    Index    |    | (if enabled)|             |
|  | (user's    |    | (pre-built  |    |             |             |
|  |  content)  |    |  index of   |    | Bing search |             |
|  |            |    |  tenant     |    | for current |             |
|  | SharePoint |    |  content)   |    | information |             |
|  | OneDrive   |    |             |    |             |             |
|  | Exchange   |    |             |    |             |             |
|  | Teams      |    |             |    |             |             |
|  +-----+------+    +------+------+    +-------+-----+             |
|        |                   |                   |                   |
|        +-------------------+-------------------+                   |
|                            |                                       |
|                            v                                       |
|                   +--------+--------+                              |
|                   | Grounded Prompt  |                              |
|                   | (user prompt +   |                              |
|                   |  retrieved data) |                              |
|                   +--------+--------+                              |
|                            |                                       |
|                            v                                       |
|                   +--------+--------+                              |
|                   |  Large Language  |                              |
|                   |  Model (LLM)    |                              |
|                   |  Azure OpenAI   |                              |
|                   +--------+--------+                              |
|                            |                                       |
|                            v                                       |
|                   +--------+--------+                              |
|                   |  Responsible AI  |                              |
|                   |  Post-processing |                              |
|                   |  (safety, cite)  |                              |
|                   +--------+--------+                              |
|                            |                                       |
|                            v                                       |
|                   +--------+--------+                              |
|                   |    Response      |                              |
|                   |  (with citations |                              |
|                   |   to source      |                              |
|                   |   documents)     |                              |
|                   +-----------------+                              |
|                                                                    |
+------------------------------------------------------------------+
```

### Key Architectural Components

| Component | Function | Governance Relevance |
|-----------|----------|---------------------|
| **Copilot Orchestrator** | Receives user prompt, coordinates retrieval, manages LLM interaction | Prompt preprocessing applies Responsible AI filters |
| **Microsoft Graph** | Provides access to user's M365 content (files, emails, chats, meetings) | Access scoped to user's existing permissions |
| **Semantic Index** | Pre-built search index of tenant content for fast retrieval | Indexes everything the user can access; governance must address permission scope |
| **LLM (Azure OpenAI)** | Generates response based on grounded prompt | Tenant data not used for model training; processed in Azure boundary |
| **Responsible AI layer** | Pre- and post-processing safety filters | Content safety, harmful content blocking, citation generation |
| **Web Search (Bing)** | Optional grounding from web content | May send contextual queries externally; controllable via admin settings |

---

## Semantic Index for Copilot

The Semantic Index is a critical component for governance because it determines what content Copilot can discover and retrieve.

### What the Semantic Index Indexes

| Content Type | Indexed? | Source |
|-------------|----------|--------|
| SharePoint documents (Word, Excel, PowerPoint, PDF) | Yes | SharePoint Online |
| OneDrive files | Yes | OneDrive for Business |
| Outlook emails and attachments | Yes | Exchange Online |
| Teams messages and chat | Yes | Teams |
| Teams meeting transcriptions | Yes | Teams (if transcription enabled) |
| OneNote pages | Yes | OneNote |
| Loop components | Yes | Loop |
| Planner tasks | Limited | Planner |
| Viva Engage posts | Yes | Viva Engage |
| Stream video transcripts | Yes | Stream |

### How the Semantic Index Works

1. **Crawling:** The Semantic Index continuously crawls M365 content accessible via Microsoft Graph
2. **Embedding:** Content is converted to vector embeddings (numerical representations of meaning)
3. **Indexing:** Embeddings are stored in a per-user index scoped to that user's permissions
4. **Retrieval:** When Copilot receives a prompt, the Semantic Index provides semantically relevant content

### Governance Implications

| Implication | Risk | Mitigation |
|-------------|------|------------|
| **Indexes all accessible content** | Content the user technically can access but should not routinely see becomes discoverable | Oversharing remediation (Controls 1.1-1.3) |
| **Includes meeting transcripts** | Spoken content from meetings is indexed and retrievable | Teams meeting governance (Control 1.5) |
| **Includes email content** | Full email bodies and attachments are searchable by Copilot | Exchange permissions review (Control 1.13) |
| **Near-real-time updates** | Newly shared content becomes available to Copilot quickly | Sensitivity labels applied at creation (Control 2.2) |
| **No content exclusion by site** | Administrators cannot selectively exclude specific SharePoint sites from the Semantic Index (except via Restricted SharePoint Search) | Restricted SharePoint Search (Control 1.4) |

!!! warning "Restricted SharePoint Search"
    **Restricted SharePoint Search (RSS)** is the primary mechanism for limiting which SharePoint sites are included in Copilot's grounding for Microsoft 365 Copilot Chat. When enabled, only sites on the approved list are used for Copilot grounding in the Copilot Chat experience. This is a critical control for Regulated environments. Note: RSS applies to Copilot Chat grounding, not to Copilot within individual apps (e.g., Copilot in Word still accesses files the user has open or recently accessed).

---

## Graph Grounding

Graph grounding is the process by which the Copilot Orchestrator retrieves relevant content from the Microsoft Graph to provide context for the LLM.

### How Graph Grounding Works

1. **Query formulation:** The orchestrator converts the user's natural language prompt into one or more Graph API queries
2. **Permission-scoped search:** Queries execute within the user's security context -- only content the user has permission to access is returned
3. **Relevance ranking:** Results are ranked by semantic relevance to the prompt
4. **Content extraction:** Relevant passages are extracted from documents, emails, and messages
5. **Prompt augmentation:** Extracted content is appended to the user's prompt as grounding context

### The No-Elevated-Access Principle

Microsoft 365 Copilot operates under a strict no-elevated-access principle:

- Copilot **never** accesses content the user cannot access directly through M365 applications
- Copilot uses the user's delegated token for all Graph API calls
- If a user's access to a document is revoked, Copilot immediately loses access to that document
- Admin-level access is not used for content retrieval

**Governance implication:** The no-elevated-access principle means that *permission governance is Copilot governance*. If permissions are correct, Copilot's access is correct. If permissions are overly broad, Copilot's access is overly broad.

---

## RAG Pipeline

Microsoft 365 Copilot uses a Retrieval-Augmented Generation (RAG) pipeline to produce grounded, contextual responses.

### End-to-End Data Flow

```
+------------------------------------------------------------------+
|                    RAG PIPELINE DATA FLOW                           |
|                                                                    |
|  1. USER PROMPT                                                    |
|     "Draft a summary of the ABC Corp Q4 earnings call"            |
|                |                                                   |
|                v                                                   |
|  2. RESPONSIBLE AI PRE-PROCESSING                                  |
|     - Content safety filter (block harmful prompts)                |
|     - Prompt injection detection                                   |
|     - Metaprompt injection (system instructions)                   |
|                |                                                   |
|                v                                                   |
|  3. RETRIEVAL (Graph Grounding)                                    |
|     - Query Semantic Index for relevant content                    |
|     - Search Microsoft Graph for matching documents                |
|     - Retrieve user's emails, files, meeting transcripts           |
|     - Apply permission boundary (user context only)                |
|     - Rank results by relevance                                    |
|                |                                                   |
|                v                                                   |
|  4. GROUNDED PROMPT ASSEMBLY                                       |
|     [System instructions] +                                        |
|     [Retrieved context from Graph/Semantic Index] +                |
|     [User prompt] +                                                |
|     [App context (current document, meeting, email)]               |
|                |                                                   |
|                v                                                   |
|  5. LLM INFERENCE (Azure OpenAI)                                   |
|     - Process grounded prompt                                      |
|     - Generate response                                            |
|     - Include citation markers                                     |
|                |                                                   |
|                v                                                   |
|  6. RESPONSIBLE AI POST-PROCESSING                                 |
|     - Output safety filter                                         |
|     - Grounding verification                                       |
|     - Citation attachment                                          |
|     - Harmful content blocking                                     |
|                |                                                   |
|                v                                                   |
|  7. RESPONSE DELIVERED TO USER                                     |
|     Response with citations to source documents                    |
|                                                                    |
|  8. AUDIT EVENT GENERATED                                          |
|     CopilotInteraction event logged to Unified Audit Log           |
|                                                                    |
+------------------------------------------------------------------+
```

### Governance Control Points in the RAG Pipeline

| Stage | Governance Control | Control ID |
|-------|-------------------|------------|
| Pre-processing | Responsible AI boundaries (Microsoft-managed) | N/A (Microsoft responsibility) |
| Retrieval | Permission governance, oversharing remediation | 1.1, 1.2, 1.3 |
| Retrieval | Restricted SharePoint Search | 1.4 |
| Retrieval | Sensitivity label enforcement | 2.2, 2.3 |
| Retrieval | DLP policy evaluation | 2.1 |
| Retrieval | Information barriers | 2.6 |
| Post-processing | Content safety (Microsoft-managed) | N/A (Microsoft responsibility) |
| Response delivery | Communication compliance monitoring | 3.4 |
| Audit | Copilot interaction logging | 3.1 |
| Audit | Retention policy application | 3.2 |

---

## Prompt Orchestration and Responsible AI Boundaries

### System Metaprompt

Every Copilot interaction includes a system metaprompt (invisible to the user) that instructs the LLM to:

- Ground responses in retrieved content (avoid hallucination)
- Cite sources for factual claims
- Decline requests that violate content safety policies
- Maintain appropriate tone and professional standards
- Avoid generating harmful, biased, or misleading content

The metaprompt is managed by Microsoft and is not configurable by tenant administrators.

### Responsible AI Filters

| Filter | Stage | Purpose |
|--------|-------|---------|
| **Prompt safety** | Pre-processing | Block harmful, illegal, or policy-violating prompts |
| **Prompt injection detection** | Pre-processing | Detect attempts to override system instructions |
| **Output safety** | Post-processing | Block harmful or inappropriate generated content |
| **Grounding check** | Post-processing | Verify response is grounded in retrieved content |
| **Citation generation** | Post-processing | Attach source document references to response |

### Governance Implications

- Organizations **cannot** customize the Responsible AI filters
- Organizations **can** layer additional governance via DLP, communication compliance, and sensitivity labels
- The metaprompt helps reduce but does not eliminate hallucination risk
- Organizations should not rely solely on Responsible AI filters for regulatory compliance

---

## Web Search / Web Grounding Data Flow

When web search (web grounding) is enabled, Copilot may query Bing to supplement Graph-grounded responses with current public information.

### Web Search Data Flow

```
+------------------------------------------------------------------+
|                    WEB SEARCH DATA FLOW                             |
|                                                                    |
|  User prompt: "What are the latest SEC enforcement actions         |
|                 on AI governance?"                                  |
|                |                                                   |
|                v                                                   |
|  Orchestrator determines web search may be helpful                 |
|                |                                                   |
|                v                                                   |
|  +-------------+---------------+                                   |
|  | Search query generated       |                                  |
|  | (derived from user prompt    |                                  |
|  |  and conversation context)   |                                  |
|  +-------------+---------------+                                   |
|                |                                                   |
|                v                                                   |
|  +-------------+---------------+                                   |
|  | Bing Search API              |                                  |
|  | (query sent to Bing)         |  <-- EXTERNAL DATA FLOW          |
|  +-------------+---------------+                                   |
|                |                                                   |
|                v                                                   |
|  Web results returned and combined with Graph results              |
|                |                                                   |
|                v                                                   |
|  LLM generates response from combined grounding                   |
|                                                                    |
+------------------------------------------------------------------+
```

### Governance Considerations for Web Search

| Consideration | Risk | Mitigation |
|---------------|------|------------|
| **Query content** | Search queries derived from prompts may contain sensitive context (client names, deal terms) | Disable web search for Regulated users (Control 2.7) |
| **External data quality** | Web results may be outdated, inaccurate, or misleading | User training on verifying Copilot outputs |
| **Data residency** | Web search queries are processed by Bing (separate from M365 data boundary) | Evaluate against data residency requirements |
| **Audit trail** | Web-grounded responses are logged but the specific search queries may not be separately retained | Monitor Microsoft updates on web search logging |

### Admin Controls for Web Search

| Setting | Location | Options |
|---------|----------|---------|
| Web search in Copilot | M365 Admin Center > Copilot | Enable / Disable (tenant-wide or per-group) |
| Optional connected experiences | M365 Apps admin > Privacy | Controls web-connected features |

**FSI Recommendation:** Disable web search for users in Regulated environments. For Recommended environments, evaluate on a case-by-case basis. For Baseline, enable with user guidance.

---

## Copilot Pages Architecture

Copilot Pages is an AI-native content surface that allows users to collaborate on Copilot-generated content.

### How Copilot Pages Work

1. User generates content via Copilot (in Microsoft 365 Copilot Chat or any M365 app)
2. User promotes the response to a "Page" for collaboration
3. The Page is stored in the user's SharePoint Embedded container (shared platform with Copilot Notebooks and Loop My workspace)
4. Other users can be invited to collaborate on the Page
5. Pages support real-time co-authoring and further Copilot interactions

### Governance Implications

| Concern | Risk | Control |
|---------|------|---------|
| **Storage location** | Pages may store sensitive content in SharePoint Embedded without appropriate classification or lifecycle controls | Sensitivity labels (2.2), auto-labeling (2.3) |
| **Sharing scope** | Pages can be shared broadly, potentially duplicating regulated content | Sharing governance (1.11), DLP (2.1) |
| **Retention** | Pages must be subject to the same retention policies as other M365 content | Retention policies (3.2) |
| **eDiscovery** | Pages must be discoverable for regulatory examination | eDiscovery configuration (3.3) |
| **Audit** | Page creation, sharing, and editing must generate audit events | Audit logging (3.1) |

---

## Plugin and Graph Connector Data Flow

Copilot's data reach can be extended beyond native M365 content through plugins and Graph connectors.

### Graph Connectors

Graph connectors ingest external data (from third-party systems, databases, or file shares) into the Microsoft Graph, making it available to Copilot for grounding.

```
+------------------------------------------------------------------+
|                    GRAPH CONNECTOR DATA FLOW                       |
|                                                                    |
|  +------------------+     +-----------------+     +--------------+ |
|  | External System  | --> | Graph Connector | --> | Microsoft    | |
|  | (ServiceNow,     |     | (ingestion and  |     | Graph        | |
|  |  Salesforce,     |     |  ACL mapping)   |     | (searchable  | |
|  |  file shares)    |     |                 |     |  by Copilot) | |
|  +------------------+     +-----------------+     +--------------+ |
|                                                                    |
|  GOVERNANCE CONSIDERATIONS:                                        |
|  - External data inherits Graph connector ACLs, not source ACLs   |
|  - ACL mapping must accurately reflect source permissions          |
|  - External data becomes part of Copilot's grounding corpus       |
|  - Sensitivity labels should be applied to ingested content        |
+------------------------------------------------------------------+
```

### Plugins (Message Extensions)

Copilot plugins extend functionality by allowing Copilot to interact with external services in real-time.

| Plugin Type | Data Flow | Governance Consideration |
|-------------|-----------|------------------------|
| **Message extensions** | Copilot sends structured queries to external APIs | Data leaves M365 boundary; evaluate per plugin |
| **API plugins** | Real-time API calls to external services | Authentication, data classification, audit |
| **Declarative agents** | Custom Copilot experiences with scoped instructions and data | Governance overlaps with FSI-AgentGov |

### Plugin Governance Controls

| Control | Purpose |
|---------|---------|
| Plugin approval workflow | Restrict which plugins are available to users (Control 2.8) |
| Graph connector ACL review | Verify permission mapping for ingested content (Control 2.8) |
| Plugin data classification | Classify data accessed by each plugin (Control 2.8) |
| Plugin audit logging | Log plugin invocations and data exchanges (Control 3.1) |

---

## Declarative Agent Architecture

Declarative agents are custom Copilot experiences built from SharePoint content, custom instructions, and scoped capabilities.

### How Declarative Agents Work

1. Administrator or user creates a declarative agent in the M365 Admin Center or SharePoint
2. The agent is scoped to specific SharePoint sites, instructions, and capabilities
3. Users interact with the agent through the Copilot interface
4. The agent retrieves content only from its configured sources (plus user's general M365 access)

### Governance Boundary

Declarative agents from SharePoint are within scope of this framework (FSI-CopilotGov) when they:

- Are built using SharePoint content as the knowledge base
- Operate within the M365 Copilot interface
- Do not require Copilot Studio or Power Platform

Declarative agents built in Copilot Studio or Agent Builder fall under [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov).

### Governance Controls for Declarative Agents

| Control Area | Governance Requirement |
|-------------|----------------------|
| **Source site governance** | SharePoint sites used for grounding must have correct permissions and sensitivity labels |
| **Agent publication** | Restrict who can publish declarative agents to the organization |
| **Content scope** | Review and approve the SharePoint sites scoped to each agent |
| **Audit** | Agent interactions must be logged and retained |
| **Access** | Agent availability should be restricted to appropriate user groups |

See Control 4.10 for detailed declarative agent governance requirements.

---

## Copilot Control System (Administrative Governance Surface)

The **Copilot Control System** is Microsoft's February 2026 branding for the consolidated administrative governance surface across Microsoft 365 Copilot. Previously, administrators had to navigate across multiple admin centers (M365 Admin Center, Teams Admin Center, Exchange Admin Center, SharePoint Admin Center, and Microsoft Purview) to manage Copilot settings. The Copilot Control System unifies these distributed controls into a coherent governance experience accessible primarily through **M365 Admin Center > Copilot**.

### What the Copilot Control System Consolidates

| Capability | Previous Location | Copilot Control System Location |
|------------|------------------|-------------------------------|
| **Global Copilot toggle** | M365 Admin Center (Copilot section) | MAC > Copilot (unchanged) |
| **Per-application feature toggles** | Individual app admin centers | Progressively migrating to MAC > Copilot |
| **Baseline Security Mode** | N/A (new capability) | MAC > Settings > Org settings > Security & privacy |
| **Copilot overview dashboard** | N/A (new capability) | MAC > Copilot > Overview |
| **License utilization and adoption** | Multiple reporting surfaces | Consolidated in Copilot overview dashboard |
| **Security posture summary** | Purview, Defender, Entra (separately) | Summary links from Copilot overview dashboard |

### Governance Relevance

The Copilot Control System is significant for governance architecture because it introduces a **single pane of glass** for Copilot administration, which directly supports:

- **SOX Section 404 ITGC evidence collection** -- the overview dashboard provides centralized proof of ongoing governance oversight
- **Segregation of duties enforcement** -- role-based access (Copilot Admin, Teams Admin, Exchange Admin, SharePoint Admin) is preserved within the unified surface
- **Configuration drift detection** -- a centralized baseline makes it easier to detect and remediate unauthorized setting changes
- **Regulatory examination readiness** -- a single admin surface simplifies evidence production for examiners

For detailed implementation guidance, including Baseline Security Mode configuration and change management procedures, see [Control 4.1: Copilot Admin Settings and Feature Management](../controls/pillar-4-operations/4.1-admin-settings-feature-management.md).

---

## Data Processing and Residency

### Data Processing Principles

| Principle | Description |
|-----------|-------------|
| **No model training** | Microsoft does not use customer tenant data to train, retrain, or improve foundation models |
| **Transient processing** | Prompts and responses are processed transiently; they are not stored by the LLM service after the interaction completes |
| **Audit logging** | Copilot interactions generate audit events that are stored in the tenant's Unified Audit Log |
| **Encryption** | Data is encrypted in transit (TLS 1.2+) and at rest (AES-256) |

### Data Residency

| Data Type | Location | Notes |
|-----------|----------|-------|
| **User content** (files, emails, chats) | Per M365 data residency settings | Stored in tenant's geographic region |
| **Semantic Index** | Co-located with tenant data | Follows tenant data residency |
| **LLM processing** | Azure region (may differ from tenant region) | Processed in Azure OpenAI boundary |
| **Web search queries** | Bing service (global) | Separate from M365 data boundary |
| **Audit logs** | Per M365 audit log residency | Stored in tenant's compliance boundary |

!!! warning "LLM Processing Location"
    LLM inference may occur in Azure regions different from the tenant's primary data location. Microsoft publishes data processing location details in the Product Terms and Data Protection Addendum. Organizations with strict data residency requirements should review these terms and consult with Microsoft.

---

## Architecture Summary for Governance

| Architecture Component | Primary Governance Concern | Key Controls |
|-----------------------|---------------------------|--------------|
| Semantic Index | Indexes all accessible content; oversharing is amplified | 1.1, 1.2, 1.3, 1.4 |
| Graph Grounding | Permission-scoped but inherits permission problems | 1.2, 1.6, 2.2 |
| Web Search | External data flow; query may contain sensitive context | 2.7 |
| LLM Processing | Hallucination risk; no model training on tenant data | 3.5, 3.7 |
| Copilot Pages | New content surface requiring classification and retention | 3.2, 4.8 |
| Plugins / Connectors | Extended data reach beyond M365 | 2.8, 4.10 |
| Audit Events | Copilot interactions logged for regulatory record-keeping | 3.1, 3.2 |
| Responsible AI | Microsoft-managed; organizations layer additional controls | DLP, communication compliance |
| Copilot Control System | Unified admin surface for all Copilot settings; configuration drift and SOX evidence | 4.1 |

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
