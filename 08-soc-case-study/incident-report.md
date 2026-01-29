# Incident Report: Suspected SSH Account Compromise

## Summary
A suspected account compromise was identified following a successful SSH login after repeated authentication failures. The activity originated from an external IP address and was preceded by brute-force attempts.

---

## Impact
- Potential unauthorized access to a Linux server
- Risk of privilege escalation and persistence

---

## Response Actions
1. Isolated the affected host
2. Blocked the attacking IP address
3. Reset credentials for the impacted account
4. Reviewed system logs for post-compromise activity

---

## MITRE ATT&CK Mapping
- T1110.001 – Brute Force: Password Guessing
- T1078 – Valid Accounts
