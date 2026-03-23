# Detection PowerShell Network Activity

## Overview
Detects network connections initiated by PowerShell, which may indicate command-and-control communication. 

---

## MITRE ATT&CK Mapping
- T1071 - Application Layer Protocol

---

## Detection Logic

### KQL Query
```kql
process.name: "powershell.exe" AND event.code: 3
```
