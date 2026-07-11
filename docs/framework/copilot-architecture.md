# Copilot Architecture

Technical deep-dive into Microsoft 365 Copilot architecture, data flows, and governance implications.

---

## Overview

Understanding the Microsoft 365 Copilot architecture is essential for effective governance. This document describes how Copilot processes prompts, retrieves content, generates responses, and where governance controls intersect the data flow.

!!! info "Architecture Currency"
    Microsoft 365 Copilot architecture evolves with platform updates. This document reflects the architecture as of April 2026. Organizations should monitor Microsoft's official documentation for changes.

---

## Microsoft 365 Copilot Architecture Overview

Microsoft 365 Copilot is not a standalone product -- it acts as an **orchestrator** (the **Copilot orchestrator**) between the user, Microsoft Graph, the Semantic Index, Microsoft 365 Copilot Search, optional web grounding, and large language models (LLMs).

!!! note "Terminology"
    Microsoft Learn describes Microsoft 365 Copilot as acting as an **orchestrator** that coordinates prompt processing, grounding, and model calls; this document uses **"Copilot orchestrator"** for that layer. **"Microsoft 365 Brain"** is an informal term sometimes used for the same orchestration layer and is not canonical Microsoft product terminology. Verify against the [Microsoft 365 Copilot architecture](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture) page. *(Verified on Microsoft Learn, 2026-06-12.)*

```
+------------------------------------------------------------------+
|              MICROSOFT 365 COPILOT ARCHITECTURE                    |
|                                                                    |
|  +------------+                                                    |
|  |    User    |  Prompt: "Summarize the Q4 earnings deck"          |
|  +-----+------+                                                    |
|        |                                                           |
|        v                                                           |
|  +-----+------+                                                    |
|  | Copilot    |  Responsible AI filters                            |
|  | orchestr-  |  Content safety checks                             |
|  | ator       |  Prompt preprocessing                              |
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
|                   |  Microsoft-hosted|                              |
|                   |  OpenAI plus     |                              |
|                   |  optional 3P     |                              |
|                   |  models          |                              |
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
| **Copilot orchestrator** | Receives user prompt, coordinates retrieval, search, tool calls, and LLM interaction | Prompt preprocessing applies Responsible AI filters; orchestration choices determine which grounding sources are used |
| **Microsoft Graph** | Provides access to user's Microsoft 365 content (files, emails, chats, meetings) | Access scoped to user's existing permissions |
| **Semantic Index** | Pre-built search index of tenant content for fast retrieval | Indexes content the user can access; governance must address permission scope |
| **Microsoft 365 Copilot Search** | Search module and admin-managed retrieval surface in the Microsoft 365 Copilot app, including Microsoft 365 and configured third-party data sources | Govern result sources, authoritative sites, connectors, and eligible users through Microsoft 365 admin settings |
| **LLM (foundation models)** | Generates response based on grounded prompt. Default path uses Microsoft-hosted OpenAI models within Microsoft's managed Azure boundary; optional providers include Anthropic Claude (available across Microsoft 365 Copilot, Researcher, and Copilot in Microsoft 365 apps) and xAI Grok (preview, currently surfaced through Copilot Studio) where enabled. | Tenant prompts, responses, and Microsoft Graph data are not used to train foundation LLMs. **Microsoft-hosted OpenAI**: processed in Microsoft-managed Azure boundary under the Product Terms / DPA, with EU Data Boundary and in-country LLM processing commitments where applicable. **Anthropic Claude**: provided under the Microsoft Product Terms and DPA, but **out of scope for the EU Data Boundary and in-country LLM processing commitments**; on by default for most commercial-cloud customers (excluding EU/EFTA and UK). **xAI Grok (preview)**: hosted by xAI **outside Microsoft-managed environments and audit controls** under xAI's separate Terms of Service and Data Processing Addendum — Microsoft Product Terms, DPA, data residency commitments, audit and compliance requirements, SLAs, and the Customer Copyright Commitment do not apply. |
| **Responsible AI layer** | Pre- and post-processing safety filters | Content safety, harmful content blocking, citation generation |
| **Web Search (Bing)** | Optional grounding from web content | May send contextual queries externally; controllable via admin settings |

!!! note "Third-party model provider currency"
    Provider scope and default-state claims above are time-sensitive. The Anthropic Claude posture (under Microsoft Product Terms/DPA; out of scope for the EU Data Boundary; on by default outside EU/EFTA/UK) and the xAI Grok posture (hosted outside Microsoft-managed environments; Product Terms, DPA, residency, and Customer Copyright Commitment do not apply) were verified against [Connect to Anthropic models](https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor) and [Connect to xAI's models](https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models) on **2026-06-12**. Re-verify before relying on these statements, as availability and default state change over time.

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

1. **Crawling:** The Semantic Index continuously crawls Microsoft 365 content accessible via Microsoft Graph
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

## Microsoft 365 Copilot Search

Microsoft 365 Copilot Search is the Search module in the Microsoft 365 Copilot app for users with eligible Microsoft 365 Copilot licenses. The Microsoft 365 admin center includes a Copilot Search admin experience to manage, customize, and optimize search across the organization. Search results can include Microsoft 365 content and configured third-party data sources, including Graph connector content, subject to the user's existing permissions and source access controls.

### Governance Implications

| Implication | Risk | Mitigation |
|-------------|------|------------|
| **Authoritative source ranking** | Low-quality or outdated sites may rank alongside approved sources | Maintain authoritative source designations and content-owner review cycles |
| **Third-party data sources** | Connector content can broaden what users discover through Copilot Search | Review Graph connector ACL mapping, source ownership, and data classification (Control 2.13) |
| **Eligible-user access** | Search availability follows Microsoft 365 Copilot licensing and admin configuration | Align Copilot Search rollout with license assignment and training plans |
| **Search analytics** | Query and result telemetry may reveal sensitive business interests | Limit admin access and review audit/telemetry handling procedures |

---

## Graph Grounding

Graph grounding is the process by which the Copilot orchestrator retrieves relevant content from the Microsoft Graph to provide context for the LLM.

### How Graph Grounding Works

1. **Query formulation:** the Copilot orchestrator converts the user's natural language prompt into one or more Graph API queries or search requests
2. **Permission-scoped search:** Queries execute within the user's security context -- only content the user has permission to access is returned
3. **Relevance ranking:** Results are ranked by semantic relevance to the prompt
4. **Content extraction:** Relevant passages are extracted from documents, emails, and messages
5. **Prompt augmentation:** Extracted content is appended to the user's prompt as grounding context

### The No-Elevated-Access Principle

Microsoft 365 Copilot operates under a strict no-elevated-access principle:

- Copilot **never** accesses content the user cannot access directly through Microsoft 365 applications
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
|  3. RETRIEVAL (Graph Grounding / Copilot Search)                   |
|     - Query Semantic Index and Copilot Search for relevant content |
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
|  5. LLM INFERENCE (Microsoft-hosted OpenAI by default;            |
|     optional Anthropic subprocessor or xAI independent provider)  |
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
| **Data residency** | Web search queries are processed by Bing (separate from the Microsoft 365 data boundary) | Evaluate against data residency requirements |
| **Audit trail** | Web-grounded responses are logged but the specific search queries may not be separately retained | Monitor Microsoft updates on web search logging |

### Admin Controls for Web Search

| Setting | Location | Options |
|---------|----------|---------|
| Web search in Copilot | Microsoft 365 admin center > Copilot | Enable / Disable (tenant-wide or per-group) |
| Optional connected experiences | Microsoft 365 Apps admin center > Privacy | Controls web-connected features |

**FSI Recommendation:** Disable web search for users in Regulated environments. For Recommended environments, evaluate on a case-by-case basis. For Baseline, enable with user guidance.

---

## Copilot Pages Architecture

Copilot Pages is an AI-native content surface that allows users to collaborate on Copilot-generated content.

### How Copilot Pages Work

1. User generates content via Copilot (in Microsoft 365 Copilot Chat or a supported Microsoft 365 app)
2. User promotes the response to a "Page" for collaboration
3. The Page is stored in the user's SharePoint Embedded container (shared platform with Copilot Notebooks and Loop My workspace)
4. Other users can be invited to collaborate on the Page
5. Pages support real-time co-authoring and further Copilot interactions

### Governance Implications

| Concern | Risk | Control |
|---------|------|---------|
| **Storage location** | Pages may store sensitive content in SharePoint Embedded without appropriate classification or lifecycle controls | Sensitivity labels (2.2), auto-labeling (2.3) |
| **Sharing scope** | Pages can be shared broadly, potentially duplicating regulated content | Sharing governance (1.11), DLP (2.1) |
| **Retention** | Pages must be subject to the same retention policies as other Microsoft 365 content | Retention policies (3.2) |
| **eDiscovery** | Pages must be discoverable for regulatory examination | eDiscovery configuration (3.3) |
| **Audit** | Page creation, sharing, and editing must generate audit events | Audit logging (3.1) |

---

## Plugin and Graph Connector Data Flow

Copilot's data reach can be extended beyond native Microsoft 365 content through plugins and Graph connectors.

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
| **Message extensions** | Copilot sends structured queries to external APIs | Data leaves the Microsoft 365 boundary; evaluate per plugin |
| **API plugins** | Real-time API calls to external services | Authentication, data classification, audit |
| **Declarative agents** | Custom Copilot experiences with scoped instructions and data | SharePoint declarative agents and Microsoft 365 deployment controls are in scope here; Copilot Studio build and ALM governance lives in FSI-AgentGov |

### Plugin Governance Controls

| Control | Purpose |
|---------|---------|
| Plugin approval workflow | Restrict which plugins are available to users (Control 2.8) |
| Graph connector ACL review | Verify permission mapping for ingested content (Control 2.8) |
| Plugin data classification | Classify data accessed by each plugin (Control 2.8) |
| Plugin audit logging | Log plugin invocations and data exchanges (Control 3.1) |

---

## Declarative Agent Architecture

Declarative agents are configuration-defined Copilot experiences built from scoped content, custom instructions, and approved capabilities. SharePoint declarative agents and Agent 365 inventory/policy oversight are in scope for this framework; detailed Copilot Studio and Power Platform build lifecycle governance belongs in FSI-AgentGov.

### How Declarative Agents Work

1. Administrator or user creates a declarative agent in the Microsoft 365 admin center or SharePoint
2. The agent is scoped to specific SharePoint sites, instructions, and capabilities
3. Users interact with the agent through the Copilot interface
4. The agent retrieves content only from its configured sources (plus the user's general Microsoft 365 access where the host experience allows it)

### Governance Boundary

Declarative agents from SharePoint are within scope of this framework (FSI-CopilotGov) when they:

- Are built using SharePoint content as the knowledge base
- Operate within the Microsoft 365 Copilot interface
- Do not require Copilot Studio or Power Platform

Detailed build, environment, model-card, and lifecycle promotion governance for Copilot Studio or Agent Builder agents falls under [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov). Agent 365 inventory, policy, and Microsoft 365 deployment controls remain relevant here when those agents are deployed into the Microsoft 365 Copilot estate.

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

The **Copilot Control System** is Microsoft's February 2026 branding for the consolidated administrative governance surface across Microsoft 365 Copilot. Previously, administrators had to navigate across multiple admin centers (Microsoft 365 admin center, Microsoft Teams admin center, Exchange admin center, SharePoint admin center, and Microsoft Purview) to manage Copilot settings. The Copilot Control System unifies these distributed controls into a coherent governance experience accessible primarily through **Microsoft 365 admin center > Copilot**.

### What the Copilot Control System Consolidates

| Capability | Previous Location | Copilot Control System Location |
|------------|------------------|-------------------------------|
| **Global Copilot toggle** | Microsoft 365 admin center (Copilot section) | MAC > Copilot (unchanged) |
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

## Agent 365 Platform

**Agent 365** is Microsoft's centralized platform for monitoring, managing, and configuring Copilot agents across Microsoft 365 apps, Copilot Studio, and third-party integrations. It extends the Agents control plane in the Microsoft 365 admin center into a unified governance hub that spans the full agent lifecycle.

### What Agent 365 Adds

| Capability | Description | Governance Relevance |
|-----------|-------------|---------------------|
| **Unified agent inventory** | Single view of all agents — Microsoft first-party, organization-published, partner, and Copilot Studio agents | Supports compliance inventory and ownership tracking across agent sources |
| **Agent usage analytics** | Telemetry on sessions, active users, runtime, and exception rates per agent | Aids in identifying material agent dependencies and operational risk |
| **Centralized policy controls** | Allowed types, sharing rules, user access, and template governance in one surface | Reduces configuration drift by consolidating previously distributed settings |
| **Cross-platform visibility** | Agents from Microsoft 365, Copilot Studio, and third-party integrations appear in the same registry | Helps address third-party risk and lifecycle management for all agent sources |

### Governance Implications

- **Examination readiness:** Agent 365 provides a single evidence source for agent inventory, ownership, and usage — supporting FFIEC and OCC examination preparation.
- **Change control:** Centralized settings reduce the risk of inconsistent agent governance across admin portals.
- **Third-party oversight:** Partner and third-party agents are visible alongside internal agents, which supports OCC Bulletin 2023-17 third-party risk management expectations.

For operational governance procedures using Agent 365, see [Control 4.13: Extensibility Governance](../controls/pillar-4-operations/4.13-extensibility-governance.md). For security configuration, see [Control 2.14: Declarative Agents Governance](../controls/pillar-2-security/2.14-declarative-agents-governance.md).

---

## Entra Agent ID

Microsoft Entra ID now supports **Entra Agent ID** — a capability that assigns unique identities to Copilot agents within the Entra identity platform. Each agent receives a distinct identity object that can be governed using familiar Entra ID tools and policies.

### How Entra Agent ID Works

| Aspect | Detail |
|--------|--------|
| **Identity assignment** | Each agent registered in Agent 365 or Copilot Studio can receive an Entra ID identity |
| **Security tracking** | Agent identities appear in Entra sign-in and audit logs, supporting security monitoring |
| **Conditional Access** | Agents can be scoped by Conditional Access policies, controlling where and how they operate |
| **Compliance mapping** | Agent identities enable per-agent compliance tracking and attribution in Purview audit trails |

### Governance Implications

- **Accountability:** Entra Agent ID provides a traceable identity for each agent, linking agent activity to audit events and supporting regulatory attribution requirements.
- **Access governance:** Organizations can apply Conditional Access and identity governance policies to agents, consistent with how human identities are managed.
- **Risk segmentation:** Agent identities allow security teams to distinguish agent-initiated activity from user-initiated activity in sign-in logs and security alerts.

Organizations should verify that Entra Agent ID configuration aligns with their existing identity governance framework and Conditional Access policies.

---

## Work IQ

**Work IQ** is Copilot's persistent organizational memory layer. It enables Copilot to prioritize and personalize assistance based on team context, organizational patterns, and accumulated interaction history within the tenant.

### What Work IQ Provides

| Capability | Description |
|-----------|-------------|
| **Organizational context** | Copilot learns team structures, project relationships, and collaboration patterns to deliver more relevant responses |
| **Priority signals** | Work IQ surfaces priority indicators from emails, meetings, and tasks to help Copilot focus on what matters most |
| **Persistent memory** | Unlike individual Copilot conversations that reset, Work IQ maintains organizational context across sessions |

### Governance Implications

| Concern | Risk | Mitigation |
|---------|------|------------|
| **Data accumulation** | Work IQ builds a persistent organizational knowledge layer that may surface patterns not intended for broad discovery | Review Work IQ data retention settings and scope; align with organizational data governance policies |
| **Cross-boundary context** | Organizational memory may surface context from teams or projects the user does not directly participate in | Verify that Work IQ respects existing permission boundaries and information barriers |
| **Behavioral inference** | Priority and collaboration signals could reveal work patterns or organizational dynamics | Evaluate Work IQ output against privacy and employee data protection expectations |

Organizations should verify Work IQ configuration and scope as part of their Copilot governance posture review.

---

## Copilot Cowork

**Copilot Cowork** enables delegation of multi-step business tasks to Copilot. Unlike single-turn Copilot interactions, Cowork allows users to assign complex workflows that Copilot executes autonomously with periodic user monitoring and intervention points.

### How Copilot Cowork Works

1. User defines a multi-step task (e.g., "Research competitor earnings and draft a comparison memo")
2. Copilot breaks the task into steps and begins autonomous execution
3. User receives progress updates and can intervene, redirect, or approve at checkpoints
4. Copilot delivers the completed output for final review

### Governance Implications

| Concern | Risk | Mitigation |
|---------|------|------------|
| **Autonomous data access** | Cowork may access content across multiple Microsoft 365 sources during multi-step execution | Copilot Cowork operates within the user's existing permission boundary; oversharing remediation (Controls 1.1-1.3) remains critical |
| **Extended processing scope** | Multi-step tasks may accumulate and combine data from sources that individually are appropriate but collectively create sensitivity | Review Cowork task outputs before distribution; apply sensitivity labels to generated artifacts |
| **Reduced human oversight** | Autonomous execution reduces the frequency of human review compared to single-turn interactions | Establish organizational policies for when Cowork is appropriate vs. when manual Copilot interaction is required |
| **Audit attribution** | Multi-step tasks generate multiple Copilot interactions attributed to a single delegated workflow | Verify that Unified Audit Log captures Cowork task events with sufficient detail for regulatory record-keeping |

For FSI environments, organizations should document which business functions are approved for Copilot Cowork delegation and establish review requirements for Cowork-generated outputs, particularly for client-facing or regulated content.

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
| **User content** (files, emails, chats) | Per Microsoft 365 data residency settings | Stored in tenant's geographic region |
| **Semantic Index** | Co-located with tenant data | Follows tenant data residency |
| **Microsoft 365 Copilot Search** | Microsoft 365 service boundary plus configured connector sources | Results inherit Microsoft 365 permissions; connector source data follows source-system residency |
| **LLM processing** | Azure region (may differ from tenant region) | Processed in Azure OpenAI boundary for the default Microsoft-hosted path |
| **Third-party model provider processing** | Provider-specific boundary | Anthropic Claude through Microsoft 365 Copilot Premium follows Microsoft Product Terms/DPA but has separate data-boundary commitments; xAI Grok preview follows xAI terms where enabled |
| **Web search queries** | Bing service (global) | Separate from Microsoft 365 data boundary |
| **Audit logs** | Per Microsoft 365 audit log residency | Stored in tenant's compliance boundary |

!!! warning "LLM Processing Location"
    LLM inference may occur in Azure regions different from the tenant's primary data location. Microsoft publishes data processing location details in the Product Terms and Data Protection Addendum. Organizations with strict data residency requirements should review these terms and consult with Microsoft.

---

## Architecture Summary for Governance

| Architecture Component | Primary Governance Concern | Key Controls |
|-----------------------|---------------------------|--------------|
| Copilot orchestrator | Orchestrates retrieval, search, tools, and LLM interaction across Copilot experiences | 3.1, 4.1 |
| Semantic Index | Indexes accessible content; oversharing is amplified | 1.1, 1.2, 1.3, 1.4 |
| Microsoft 365 Copilot Search | Search surface over Microsoft 365 and configured third-party data sources; result and source governance | 1.1, 1.13, 2.13 |
| Graph Grounding | Permission-scoped but inherits permission problems | 1.2, 1.6, 2.2 |
| Web Search | External data flow; query may contain sensitive context | 2.7 |
| LLM Processing | Hallucination risk; no model training on tenant data | 3.5, 3.7 |
| Third-party model providers | Provider-specific terms, data residency, and audit commitments for Anthropic Claude and xAI Grok preview | 1.10, 2.7 |
| Copilot Pages and Notebooks | New content surfaces requiring classification, retention, and lifecycle controls | 2.11, 3.2 |
| Plugins / Connectors | Extended data reach beyond Microsoft 365 | 2.13, 4.13 |
| Audit Events | Copilot interactions logged for regulatory record-keeping | 3.1, 3.2 |
| Responsible AI | Microsoft-managed; organizations layer additional controls | DLP, communication compliance |
| Copilot Control System | Unified admin surface for all Copilot settings; configuration drift and SOX evidence | 4.1 |
| Agent 365 | Centralized agent inventory, telemetry, and lifecycle governance across agent sources | 2.14, 4.13 |
| Entra Agent ID | Unique agent identities for security tracking, Conditional Access, and compliance attribution | 2.14, 1.13 |
| Work IQ | Persistent organizational memory; data accumulation and cross-boundary context risk | 3.10, 1.1 |
| Copilot Cowork | Multi-step autonomous task delegation; extended processing scope and reduced human oversight | 3.1, 3.5 |

### Microsoft Secure and Govern Blueprint

Microsoft's **[Secure and Govern Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance)** blueprint organizes Copilot security and governance into three pillars:

1. **Remediate oversharing** — Identify high-risk sites via DSPM data risk assessments, apply interim protections (RCD, DLP for Copilot), and fix access/permissions (RAC, site access reviews)
2. **Set up guardrails** — Establish secure defaults at provisioning, configure DLP for Copilot grounding and prompts, enable Insider Risk Management with Adaptive Protection, and continuously enforce via DSPM Activity Explorer
3. **Meet regulations** — Assess AI compliance gaps via Compliance Manager, define audit and retention requirements for Copilot interactions, and improve data hygiene with site lifecycle management and Microsoft 365 Archive

This framework's {{ counts.controls }} controls map comprehensively to all three blueprint pillars. See the **[Configure guide](https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot)** for step-by-step implementation and the **[Purview Secure by Default deployment model](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-intro)** for the recommended labeling strategy.

---

*FSI Copilot Governance Framework v1.8.0 - July 2026*
