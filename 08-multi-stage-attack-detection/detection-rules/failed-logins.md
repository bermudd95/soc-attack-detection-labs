# Detection: Failed Login Attempts

## Overview 
Detects failed authentication attempts, often associated with brute-force attacks or unauthorized access attempts.

--- 

## MITRE ATT&CK Mapping
- T1110 - Brute Force

---

## Detection Logic

### KQL Query
```kql
event.code: 4625
```
