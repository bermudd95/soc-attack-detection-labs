# Detection & Response Use Case – Credential Abuse Following Phishing

## Overview
This project documents a conceptual SOC detection and response use case designed to identify potential credential abuse following a phishing event.

The objective is to demonstrate how phishing activity can be correlated with authentication anomalies to produce actionable alerts and guide analyst response.

This project focuses on **detection logic, alert context, and response actions**, rather than tool-specific SIEM implementation.

---

## Objectives
- Design a SOC-relevant detection use case based on common post-phishing behavior
- Identify key data sources required for detection
- Define meaningful alert context for analysts
- Outline appropriate response actions following alert validation

---

## Threat Scenario
Following a phishing campaign, an attacker uses harvested credentials to authenticate to enterprise systems. These logins may appear legitimate but often exhibit anomalous characteristics such as new locations, unusual timing, or failed login patterns.

If not detected early, credential abuse may lead to:
- Unauthorized account access
- Lateral movement
- Privilege escalation
- Data exposure

---

## Data Sources
- Authentication and identity logs
- Email security alerts and phishing reports
- Endpoint or VPN access logs

---

## Detection Approach
The detection logic focuses on correlating:
- Reported phishing activity
- Authentication attempts from unfamiliar locations or devices
- Failed login attempts followed by successful authentication

This correlation increases confidence that the activity represents credential compromise rather than normal user behavior.

---

## Analyst Workflow
When the alert is triggered, analysts are expected to:
1. Review authentication context and timing
2. Validate activity with the user if necessary
3. Assess risk based on account role and access
4. Initiate containment actions when appropriate

---

## Response Considerations
Response actions may include:
- Credential resets
- Session revocation
- Temporary account suspension
- Escalation to incident response for further investigation

---

## Project Files
- `detection-use-case.md` — Conceptual detection logic and false positive considerations
- `alert-context.md` — Information provided to analysts when the alert fires
- `response-actions.md` — Recommended response steps and escalation criteria

---

## Skills Demonstrated
- Detection engineering concepts
- SOC alert design
- Threat-to-detection correlation
- Incident response decision-making

---

## Disclaimer
This project is a conceptual exercise created for educational and portfolio demonstration purposes. No production systems were involved.
