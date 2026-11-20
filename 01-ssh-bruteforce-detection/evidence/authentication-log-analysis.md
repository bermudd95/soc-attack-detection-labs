# SSH Authentication Evidence Analysis

## Purpose

This document describes how a SOC analyst would examine Ubuntu authentication records during the SSH brute-force exercise. It separates the facts recorded in the project from the additional evidence that would be needed for a complete investigation.

## Evidence currently documented

The original exercise notes establish that:

- Hydra was run from Kali Linux against `192.168.226.130`.
- The target account was `bob_victim`.
- The target was an Ubuntu Linux virtual machine.
- Hydra successfully discovered a password accepted by the SSH service.

The original ZIP does not contain raw authentication-log excerpts, an exact attempt count, or a timestamped event sequence. Do not present illustrative log lines as captured evidence.

## Relevant log source

On many Ubuntu installations, SSH authentication events are recorded in:

```text
/var/log/auth.log
```

Depending on the system's logging configuration, related records may also be available through the system journal:

```bash
sudo journalctl -u ssh
```

The exact service unit name and logging destination can vary by distribution and configuration.

## Example review commands

These are commands a lab analyst could use to inspect retained records. They are investigation guidance, not commands documented as having been run during the original exercise.

```bash
sudo grep -E 'sshd|Failed password|Accepted password|Invalid user' /var/log/auth.log
```

To narrow the review to the target account:

```bash
sudo grep 'bob_victim' /var/log/auth.log
```

To review SSH service messages through the journal:

```bash
sudo journalctl -u ssh --since '2025-03-05 00:00:00' --until '2025-03-06 00:00:00'
```

## What to establish

| Question | Evidence to seek |
|---|---|
| Were repeated failures generated? | Multiple failed SSH authentication records within a defined period |
| Which source initiated the attempts? | Source IP or hostname recorded by `sshd` |
| Which account was targeted? | Username in the authentication record |
| Was a password accepted? | Successful authentication record, such as an `Accepted password` event |
| Did the successful event follow the failures? | Timestamps and matching source, account, and destination context |
| Was a session established? | Session-open records and corroborating session or audit telemetry |
| What happened after login? | Process, privilege, account, file, and command audit records where available |

## Evidence interpretation

A successful password discovery reported by Hydra establishes that the SSH service accepted a password from the supplied list. A corresponding `Accepted password` entry in the target's authentication log would provide host-side corroboration.

A successful authentication record does not, by itself, establish malicious commands, privilege escalation, persistence, or data access. Those conclusions require additional evidence.

## Evidence record to complete if logs are recovered

| Field | Value |
|---|---|
| Log file or source | Not included in original project ZIP |
| First observed failure | Not recorded |
| Last observed failure | Not recorded |
| Successful authentication time | Not recorded |
| Source IP in host logs | Not recorded |
| Target account | `bob_victim` |
| Target host | Ubuntu VM (`192.168.226.130`) |
| Number of failures | Not recorded |
| Session established | Not established by available source |
| Post-authentication activity | Not established by available source |

## Analyst conclusion

The scenario demonstrates successful password discovery against the target SSH account. The available documentation does not contain enough raw telemetry to reconstruct the precise authentication sequence or determine what occurred after credential discovery. The correct reporting position is to identify the valid credential discovery as confirmed by the exercise notes and leave unsupported post-authentication conclusions open.
