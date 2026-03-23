# Incident Report: Multi-Stage Attack Detection

## Summary
A multi-stage attack was simulated and detected involving execution, obfuscation, persistence, authentication anomalies, and network activity.

---

## Timeline

| Time | Event |
|------|------|
| 12:01 | PowerShell execution |
| 12:02 | Encoded command |
| 12:03 | Scheduled task created |
| 12:04 | Failed login attempts |
| 12:05 | Network activity |

---

## Investigation Process

### Step 1: Identify Initial Execution
PowerShell activity detected on host.

### Step 2: Detect Obfuscation
Encoded command observed using Base64 encoding.

### Step 3: Identify Persistence
Scheduled task created indicating persistence.

### Step 4: Analyze Authentication Activity
Multiple failed login attempts detected.

### Step 5: Review Network Activity
Outbound connection observed from PowerShell.

---

## Findings
- Multi-stage attack behavior confirmed
- Indicators align with known attacker techniques
- Activity spans multiple log sources

---

## MITRE ATT&CK Mapping
- T1059.001 – PowerShell
- T1053 – Scheduled Task
- T1110 – Brute Force
- T1071 – Application Layer Protocol

---

## Impact Assessment
High likelihood of malicious activity based on correlated events.

---

## Recommendations
- Restrict PowerShell usage
- Monitor scheduled tasks
- Implement account lockout policies
- Enhance network monitoring

---

## Conclusion
The attack chain was successfully detected and analyzed using SIEM correlation and endpoint telemetry.
