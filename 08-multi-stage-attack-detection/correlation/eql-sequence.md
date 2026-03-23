# Correlation Detection (EQL Sequence)

## Overview
this rule detects ordered attack behavior using event correlation accross multiple stages. 

---

## Detection Logic
```eql
sequence by host.id
  [process where process.name == "powershell.exe" and process.command_line like "*enc*"]
  [process where process.name == "schtasks.exe"]
  [authentication where event.code == "4625"]
```
