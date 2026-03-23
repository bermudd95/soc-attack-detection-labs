# Detection: Encoded PowerShell Execution

## Overview
This detection identifies PowerShell commands executed with encoded payloads. Attackers commonly use encoding to evade detection and obfuscate malicious scripts. 

---

## MITRRE ATT&CK Mapping
- T1059.001 - Command and Scripting Interpreter: PowerShell

---

## Detection Logic

### KQL Query
```kql
process.name: "powershell.exe" AND process.command_line: "*enc*"
```
