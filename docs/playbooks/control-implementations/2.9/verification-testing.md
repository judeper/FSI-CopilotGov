# Control 2.9: Defender for Cloud Apps — Copilot Session Controls — Verification & Testing

Test cases and evidence collection for validating session controls.

## Test Cases

### Test 1: Session Monitoring Activation

- **Objective:** Confirm Copilot sessions are monitored by Defender for Cloud Apps
- **Steps:**
  1. As a test user, sign out of existing Microsoft 365 browser sessions and then reauthenticate to the protected Microsoft 365 web app
  2. Confirm the session is routed through Conditional Access App Control (lock icon in Edge or `.mcas` suffix in another supported browser)
  3. Navigate to Defender > Cloud Apps > Policies > Policy management and open the relevant session policy report
  4. Confirm the routed **Login** activity appears for the test user; if using detailed policies, confirm the supported file or activity events also appear
- **Expected Result:** Routed browser sessions appear in the policy report; detailed monitored actions appear only when a content-inspecting or block-activities policy is in scope
- **Evidence:** Policy report entries for the test user, plus screenshots of routed-session indicators

### Test 2: Content Inspection Detection

- **Objective:** Verify content inspection detects sensitive data in supported browser-session actions
- **Steps:**
  1. In a supported browser session, attempt a governed file download, upload, or send/share action involving a document that contains test sensitive data
  2. Verify the session policy content inspection triggers
  3. Confirm the alert is generated with the correct severity
  4. Verify the detection details include the sensitive information type
- **Expected Result:** Content inspection detects and alerts on sensitive data
- **Evidence:** Alert record with detection details

### Test 3: Alert Generation and Delivery

- **Objective:** Confirm routed-session or anomaly alerts are generated and delivered to the security team
- **Steps:**
  1. Trigger a supported session-policy condition (for example, a sensitive file download) or a test anomaly scenario consistent with your tenant policy
  2. Verify an alert or policy match appears in Defender portal > Alerts or in the relevant policy report
  3. Confirm email notification is delivered to configured recipients
  4. Verify alert severity matches the policy configuration
- **Expected Result:** Alerts generated and delivered within expected timeframe
- **Evidence:** Alert notification and email confirmation

### Test 4: Generative AI App Catalog Coverage

- **Objective:** Verify the organization has reviewed and governed generative AI app usage via the MDCA catalog
- **Steps:**
  1. Navigate to Defender portal > Cloud Apps > Cloud app catalog > filter by Generative AI category
  2. Confirm the catalog loads and displays generative AI apps
  3. Open Defender portal > Cloud Apps > Cloud discovery > Discovered apps and identify any generative AI apps used in the organization that are not Microsoft Copilot
  4. Verify that high-risk discovered generative AI apps have governance actions applied (unsanctioned, blocked through a supported governance stream, or explicitly approved)
  5. Confirm the sanctioned/unsanctioned review cadence is documented
- **Expected Result:** Generative AI catalog and Cloud Discovery have both been reviewed; high-risk apps are governed; approval or prohibition decisions are documented
- **Evidence:** App catalog screenshot, discovered-app evidence, and governance policy/configuration for high-risk apps

### Test 5: Agent Threat Detection Verification

- **Objective:** Confirm agent threat detection is operational for Copilot agent deployments
- **Steps:**
  1. Confirm the tenant holds a Microsoft Agent 365-eligible license using the [Control 2.9 qualifying-license guidance](../../../controls/pillar-2-security/2.9-defender-cloud-apps.md#agent-365-qualifying-license-guidance); Microsoft 365 E5 is not an exclusive prerequisite. This is required as of July 1, 2026 for Copilot Studio/Foundry agent threat-detection coverage
  2. Navigate to Defender portal > Assets > AI agents and confirm Copilot agent deployments appear with a current risk level
  3. Navigate to Defender portal > Incidents & alerts and filter for agent-related alerts
  4. Review any existing agent-related incidents to verify the detection is surfacing actionable intelligence
  5. Verify at least one custom agent anomaly detection rule is configured
  6. Confirm agent threat alert routing: alerts should reach the SOC or security team within the defined SLA
- **Expected Result:** The tenant's Agent 365 license is confirmed, agents appear in the AI agent inventory with a risk level, alerts are routing correctly, and custom rules are configured
- **Evidence:** Agent 365 license confirmation; agent inventory screenshot; sample agent incident records; alert routing confirmation

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Session policy configuration | Screenshot/PDF | Compliance evidence repository | 7 years |
| Policy report / activity log samples | CSV | Compliance evidence repository | 7 years |
| Alert records | CSV | Compliance evidence repository | 7 years |
| Content inspection test results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory system monitoring | Session controls support compliance with AI interaction monitoring requirements |
| SEC Rule 17a-4 | Electronic communication monitoring | Session logging helps meet communication monitoring obligations |
| FFIEC Handbook | Security monitoring | Real-time session controls support compliance with security monitoring requirements |
| NIST CSF | DE.CM-1 Network monitoring | Session controls provide monitoring for AI workloads |
- Back to [Control 2.9](../../../controls/pillar-2-security/2.9-defender-cloud-apps.md)
