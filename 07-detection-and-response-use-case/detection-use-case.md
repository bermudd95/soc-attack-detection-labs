# Detection Use Case – Post-Phishing Credential Abuse

## Objective
Detect potential credential compromise following a phishing event by correlating authentication anomalies with reported phishing activity.

---

## Threat Scenario
After a phishing email is delivered, an attacker uses harvested credentials to authenticate to enterprise systems.

---

## Data Sources
- Authentication logs
- Email security alerts
- Endpoint or VPN access logs

---

## Detection Logic (Conceptual)
Trigger an alert when:
- A user account authenticates from a new or unusual geographic location
- The authentication occurs shortly after a reported phishing email
- Multiple failed login attempts precede a successful login

---

## False Positive Considerations
- User travel
- VPN usage
- Password resets initiated by the user

---

## Detection Value
Early identification of credential abuse reduces the likelihood of lateral movement and data access.
