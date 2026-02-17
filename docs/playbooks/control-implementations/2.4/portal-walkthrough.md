# Control 2.4: Information Barriers for Copilot (Chinese Wall) — Portal Walkthrough

Step-by-step portal configuration for implementing Information Barriers that enforce Chinese Wall restrictions in Copilot interactions.

## Prerequisites

- Microsoft Purview Compliance Administrator role
- Microsoft 365 E5 or E5 Compliance license
- Entra ID user attributes populated (department, segment identifiers)
- Chinese Wall policy requirements documented by compliance team

## Steps

### Step 1: Define Information Barrier Segments

**Portal:** Microsoft Purview
**Path:** Purview > Information Barriers > Segments

Create segments based on organizational units that require information separation. For FSI environments, typical segments include:
- Investment Banking
- Research / Equity Analysis
- Trading / Sales
- Retail Banking / Wealth Management
- Corporate Treasury
- Compliance / Legal

Define each segment using Entra ID user attributes (department, custom attribute, or group membership).

### Step 2: Create Information Barrier Policies

**Portal:** Microsoft Purview
**Path:** Purview > Information Barriers > Policies > Create

Create barrier policies that define which segments cannot communicate or share data:
- **Policy 1:** Block communication between Investment Banking and Research
- **Policy 2:** Block communication between Investment Banking and Trading
- **Policy 3:** Block communication between Research and Sales

For each policy, define the segment pair and the restriction type (Block or Allow).

### Step 3: Apply Information Barrier Policies

**Portal:** Microsoft Purview
**Path:** Purview > Information Barriers > Policy application

After creating all policies, apply them to activate enforcement. Policy application may take 24-48 hours to fully propagate across all workloads including:
- Microsoft Teams (chat, channels, meetings)
- SharePoint Online and OneDrive
- Microsoft 365 Copilot (content grounding and response generation)

### Step 4: Verify Copilot Compliance with Barriers

**Portal:** Microsoft Purview
**Path:** Purview > Information Barriers > Status

Verify that Copilot respects Information Barrier policies:
- Users in the Investment Banking segment should not receive Copilot responses grounded on Research segment content
- Copilot should not surface content across barrier boundaries regardless of technical access permissions

### Step 5: Configure Barrier Exception Handling

Document and configure any approved exceptions to barrier policies:
- Compliance and Legal may need cross-barrier access for supervisory purposes
- Specific deal teams may need temporary barrier exceptions with governance approval
- Document all exceptions with business justification and expiration dates

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Define segments for primary Chinese Wall divisions; implement core barrier policies |
| **Recommended** | Full segment coverage with exception management process; verify Copilot enforcement |
| **Regulated** | Comprehensive barrier policies per regulatory requirements; documented exception process with time-limited approvals; continuous monitoring of barrier effectiveness |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for barrier management automation
- See [Verification & Testing](verification-testing.md) to validate barrier enforcement
- Review Control 2.1 for DLP integration with Information Barriers
