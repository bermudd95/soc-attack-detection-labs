# False Positives and Benign Activity

## PowerShell Execution Alert – 09:27 UTC

The scenario describes a low-severity PowerShell execution alert that was assessed as routine administrative maintenance and closed as benign.

### Scenario Rationale

- The activity was associated with a known administrator account.
- It occurred during an approved maintenance window.
- It originated from an internal management host.
- The scenario states that no additional suspicious indicators were observed.

### Validation Considerations

The scenario does not include the command line, process tree, event IDs, account identifier, or maintenance record. In a real SOC investigation, an analyst should validate these details before closing the alert:

- Confirm that the account and management host are authorized for the activity.
- Review the PowerShell command line and script content, where available.
- Examine parent and child processes and the execution context.
- Verify the approved maintenance window with an authoritative change or maintenance record.
- Check for related authentication, endpoint, and network indicators.

### Classification Note

An alert can correctly identify PowerShell execution while the underlying activity is authorized. Depending on the detection's purpose, this may be more accurately described as benign or authorized activity rather than a false positive. The scenario's original disposition is preserved, but the supporting telemetry is not available for independent validation.

## Repeated PowerShell Commands – 10:22 UTC

A second, medium-severity PowerShell alert appears in the timeline. The original scenario does not document its investigation or disposition. It is therefore **unresolved** in this case study and should not be grouped with the 09:27 benign alert without additional evidence.

Recommended review includes command-line analysis, account and host context, process lineage, execution frequency, and related endpoint or network activity.

## Alert-Tuning Considerations

Use validated administrative context to reduce unnecessary alerts, but avoid broad exclusions based only on an internal IP address, administrator username, or maintenance-window overlap. Tuning should retain visibility into unusual commands, unexpected parent processes, and activity outside approved administrative patterns.
