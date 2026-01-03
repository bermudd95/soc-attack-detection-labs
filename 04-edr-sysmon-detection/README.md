# Endpoint Detection & Response – Sysmon Lab

## Overview
This lab demonstrates endpoint monitoring and detection using Sysmon on a
Windows 11 system. The project simulates suspicious process execution and
PowerShell activity to analyze endpoint telemetry from a SOC perspective.

## Objectives
- Deploy Sysmon for endpoint telemetry collection
- Simulate suspicious endpoint activity
- Analyze Sysmon logs for detection indicators
- Document SOC-style incident triage

## Tools Used
- Sysmon (Sysinternals)
- Windows Event Viewer
- PowerShell

## Key Findings
- Encoded PowerShell execution generates high-fidelity telemetry
- LOLBins such as certutil can be detected through process and command-line analysis
- Proper context is critical to avoid false positives

## MITRE ATT&CK Mapping
- T1059.001 – PowerShell
- T1027 – Obfuscated Files or Information
- T1218 – Signed Binary Proxy Execution
