# Control 2.9: Defender for Cloud Apps — Copilot Session Controls — Verification & Testing

Test cases and evidence collection for validating session controls.

## Test Cases

### Test 1: Session Monitoring Activation

- **Objective:** Confirm Copilot sessions are monitored by Defender for Cloud Apps
- **Steps:**
  1. As a test user, perform several Copilot interactions in Word and Teams
  2. Navigate to Defender > Investigate > Activity Log
  3. Filter for the test user and verify Copilot activities appear
  4. Confirm activity details include interaction context
- **Expected Result:** Copilot activities appear in the Defender activity log
- **Evidence:** Activity log entries for test user

### Test 2: Content Inspection Detection

- **Objective:** Verify content inspection detects sensitive data in sessions
- **Steps:**
  1. Use Copilot to interact with a document containing test sensitive data
  2. Verify the session policy content inspection triggers
  3. Confirm the alert is generated with the correct severity
  4. Verify the detection details include the sensitive information type
- **Expected Result:** Content inspection detects and alerts on sensitive data
- **Evidence:** Alert record with detection details

### Test 3: Alert Generation and Delivery

- **Objective:** Confirm alerts are generated and delivered to the security team
- **Steps:**
  1. Trigger a session policy condition (e.g., sensitive data detection)
  2. Verify an alert appears in Defender portal > Alerts
  3. Confirm email notification is delivered to configured recipients
  4. Verify alert severity matches the policy configuration
- **Expected Result:** Alerts generated and delivered within expected timeframe
- **Evidence:** Alert notification and email confirmation

### Test 4: Generative AI App Catalog Coverage

- **Objective:** Verify the organization has reviewed and governed generative AI app usage via the MDCA catalog
- **Steps:**
  1. Navigate to Defender portal > Cloud Apps > Cloud app catalog > filter by Generative AI category
  2. Confirm the catalog loads and displays generative AI apps
  3. Check the "Discovered apps" view to identify any generative AI apps used in the organization that are not Microsoft 365 Copilot
  4. Verify that high-risk discovered generative AI apps have governance policies applied (blocked, unsanctioned, or explicitly approved)
  5. Confirm Microsoft 365 Copilot is marked as "Sanctioned" in the catalog
- **Expected Result:** Generative AI catalog has been reviewed; high-risk apps are governed; sanctioned apps are documented
- **Evidence:** App catalog screenshot with discovered apps; governance policy configuration for high-risk apps

### Test 5: Agent Threat Detection Verification

- **Objective:** Confirm agent threat detection is operational for Copilot agent deployments
- **Steps:**
  1. Navigate to Defender portal > Incidents & alerts and filter for agent-related alerts
  2. Confirm that agent monitoring is active for organizational Copilot agent deployments
  3. Review any existing agent-related incidents to verify the detection is surfacing actionable intelligence
  4. Verify at least one custom agent anomaly detection rule is configured
  5. Confirm agent threat alert routing: alerts should reach the SOC or security team within the defined SLA
- **Expected Result:** Agent threat detection is active, alerts are routing correctly, and custom rules are configured
- **Evidence:** Agent alert configuration; sample agent incident records; alert routing confirmation

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Session policy configuration | Screenshot/PDF | Compliance evidence repository | 7 years |
| Activity log samples | CSV | Compliance evidence repository | 7 years |
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
