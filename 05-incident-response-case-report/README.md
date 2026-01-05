# Threat Intelligence Brief – Credential Harvesting Campaign

## Overview
This project simulates the creation of an internal threat intelligence brief intended for SOC analysts and security leadership.

The objective is to translate external threat intelligence into actionable awareness, detection priorities, and response considerations.

---

## Audience
- SOC Analysts
- Incident Responders
- Security Leadership

---

## Threat Summary
Recent phishing campaigns have leveraged brand impersonation and urgency-based messaging to harvest employee credentials. These campaigns commonly target enterprise email users and rely on users clicking malicious links leading to spoofed login portals.

Successful credential compromise may lead to:
- Unauthorized account access
- Lateral movement
- Privilege escalation
- Data exfiltration

---

## Observed Tactics and Techniques
- Social engineering via urgent messaging
- Brand impersonation (financial and technology providers)
- Malicious hyperlinks redirecting to credential capture pages

Mapped MITRE ATT&CK Techniques:
- T1566.002 – Phishing: Link
- T1056 – Input Capture
- T1078 – Valid Accounts

---

## Impact Assessment
- High likelihood in environments with large email user bases
- Moderate to high business impact depending on account privileges
- Increased risk if MFA is not enforced

---

## Recommended Defensive Actions
- Increase monitoring for suspicious login activity
- Enforce MFA for all user accounts
- Conduct user awareness training focused on phishing indicators
- Ensure reporting mechanisms are visible and simple for users

---

## Analyst Notes
This brief is intended to guide detection priorities and awareness efforts rather than serve as a formal incident report.

---

## Disclaimer
This threat intelligence brief is a simulated exercise for educational purposes.
