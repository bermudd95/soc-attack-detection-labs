# Correlation Detection (KQL)

## Overview
This detection aggregates multiple suspicious activities to provide broader visibility into potential attacker behavior.

---

## Detection Logic
```kql
(
  process.name: "powershell.exe" AND processs.command_line: "*enc*"
)
OR
(
  process.name: "schtasks.exe"
)
OR
(
  event.code: 4625
)
OR
(
  process.name: "powershell.exe" AND event.code: 3
)
