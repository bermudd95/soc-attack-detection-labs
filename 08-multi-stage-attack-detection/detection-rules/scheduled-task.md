# Detection: Scheduled Task Creation

## Overview
Detects the creation of scheduled tasks, a common persistence mechanism used by attackers to maintain access. 

---

## MITRE ATT&CK Mapping
- T1053 - Scheduled Task/Job

---

## Detection Logic

### KQL Query
```kql
process.name: "schtasks.exe"
```
