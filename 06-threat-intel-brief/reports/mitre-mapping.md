# MITRE ATT&CK Mapping – Credential Harvesting Campaign

## Purpose
This document maps observed phishing and credential harvesting behaviors to relevant MITRE ATT&CK techniques. The intent is to provide SOC analysts with a common framework for understanding attacker behavior and aligning detection and response efforts.

---

## Initial Access

### T1566.002 – Phishing: Link
Attackers deliver phishing emails containing malicious links that redirect users to spoofed login pages designed to capture credentials.

**Observed Behavior**
- Urgent messaging prompting immediate action
- Impersonation of trusted brands or internal IT teams
- Embedded hyperlinks leading to external credential capture pages

---

## Credential Access

### T1056 – Input Capture
Once a victim interacts with the phishing page, credentials are harvested through fake login portals.

**Observed Behavior**
- Web-based forms mimicking legitimate authentication pages
- Credentials transmitted to attacker-controlled infrastructure

---

## Persistence / Privilege Abuse

### T1078 – Valid Accounts
Compromised credentials may be used to authenticate successfully to enterprise systems, bypassing perimeter defenses.

**Observed Behavior**
- Successful logins following phishing activity
- Access originating from unfamiliar IP addresses or locations
- Elevated risk if MFA is not enforced

---

## Defensive Considerations
- Monitor authentication logs for anomalous login patterns
- Correlate reported phishing emails with subsequent login activity
- Enforce multi-factor authentication across all user accounts
- Educate users on identifying phishing indicators

---

## Analyst Notes
This mapping is intended to support threat awareness and detection alignment rather than represent a complete attack chain.
