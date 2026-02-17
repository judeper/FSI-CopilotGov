# Control 2.10: Insider Risk Detection for Copilot Usage — Portal Walkthrough

Step-by-step portal configuration for deploying insider risk detection that monitors Copilot usage patterns for anomalous or risky behavior.

## Prerequisites

- Microsoft Purview Insider Risk Management Administrator role
- Microsoft 365 E5 or E5 Compliance license
- HR connector configured (optional, for departing employee detection)
- Insider risk program approved by legal and compliance

## Steps

### Step 1: Enable Insider Risk Management for Copilot

**Portal:** Microsoft Purview
**Path:** Purview > Insider Risk Management > Settings > Policy indicators

Enable Copilot-relevant indicators in the insider risk settings:
- Unusual volume of file access via Copilot
- Sensitive content access patterns through Copilot
- Copilot usage outside normal business hours
- Bulk content summarization or extraction patterns

### Step 2: Create Insider Risk Policy for Copilot

**Portal:** Microsoft Purview
**Path:** Purview > Insider Risk Management > Policies > Create Policy

Create an insider risk policy targeting Copilot usage:
- **Template:** Data leaks or Data theft by departing users
- **Users:** All Copilot-licensed users (or priority user groups)
- **Triggering events:** DLP policy match, unusual Copilot activity volume, departing employee signal
- **Indicators:** Enable Copilot-specific indicators and general data access indicators

### Step 3: Configure Risk Levels and Thresholds

**Portal:** Microsoft Purview
**Path:** Purview > Insider Risk Management > Settings > Risk level thresholds

Configure thresholds that define what constitutes elevated risk for Copilot usage:
- **Low risk:** Slightly above-average Copilot interaction volume
- **Medium risk:** Significant increase in sensitive content access via Copilot
- **High risk:** Bulk data extraction patterns, off-hours access to restricted content

### Step 4: Set Up Alert Triage Workflow

**Portal:** Microsoft Purview
**Path:** Purview > Insider Risk Management > Alerts

Configure the alert triage workflow:
- Assign insider risk investigators
- Set up alert notification rules
- Define triage SLAs (critical: 4 hours, high: 24 hours, medium: 72 hours)
- Configure integration with your SIEM or case management system

### Step 5: Enable Privacy Controls

**Portal:** Microsoft Purview
**Path:** Purview > Insider Risk Management > Settings > Privacy

Configure privacy controls to balance risk detection with employee privacy:
- Enable pseudonymization for user identities until investigation threshold is met
- Configure data access restrictions for insider risk investigators
- Document the legal basis for insider risk monitoring

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable insider risk detection with Copilot indicators; basic alert monitoring |
| **Recommended** | Policy templates for data leaks and departing employees; priority user groups for high-risk roles; SIEM integration |
| **Regulated** | Comprehensive insider risk program with legal review; pseudonymization enabled; formal investigation procedures; documented legal basis for monitoring |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for insider risk monitoring automation
- See [Verification & Testing](verification-testing.md) to validate risk detection
- Review Control 2.9 for Defender for Cloud Apps session monitoring
