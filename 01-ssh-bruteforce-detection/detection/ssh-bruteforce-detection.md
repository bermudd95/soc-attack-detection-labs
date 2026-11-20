# SSH Brute-Force Detection Approach

## Detection objective

Identify repeated SSH authentication failures that may indicate password guessing, and raise the priority when a successful authentication follows the failures for the same source and account.

This document proposes detection logic based on the behavior exercised in the lab. The original project does not include a deployed SIEM rule or a saved query, so the logic below is conceptual and should not be described as production-tested.

## Detection signals

Useful authentication fields include:

- Event timestamp
- Source IP address
- Destination host
- Target username
- Authentication result (success or failure)
- Authentication method
- SSH service or process identifier

## Analytic 1: Repeated SSH authentication failures

**Concept:** Group failed SSH authentication events by source IP, destination host, and username over a defined time window. Alert when the count exceeds a tuned threshold.

Illustrative starting point:

```text
GROUP BY source_ip, destination_host, username
WHERE service = "sshd" AND outcome = "failure"
WITHIN 5 minutes
HAVING count >= 5
```

The threshold and time window are examples for initial testing, not values validated by this lab. Tune them against the environment's normal authentication patterns.

## Analytic 2: Failure followed by success

**Concept:** Increase alert priority when a successful SSH authentication follows multiple failures from the same source against the same account and destination host within a defined period.

Correlation keys:

- Same source IP
- Same destination host
- Same username
- Failed events preceding a successful event
- Bounded time window

This analytic is particularly relevant to the lab outcome because Hydra successfully discovered a password accepted by the target SSH service.

## Triage guidance

When an alert fires, an analyst should:

1. Confirm the source, destination, username, and event timestamps.
2. Determine whether failures and success share the same source, account, and host.
3. Check whether the source is an approved scanner, administrator workstation, VPN egress, or other known system.
4. Review whether the account is privileged or sensitive.
5. Look for session establishment and post-authentication activity.
6. Escalate when a successful authentication follows suspicious failures and cannot be explained by an authorized activity.

## False-positive considerations

Potential benign explanations include a user repeatedly entering an incorrect password, an administrator troubleshooting access, a vulnerability scanner, or multiple users sharing a NAT egress address. Validate context before suppressing alerts. Avoid broad allowlists based only on source IP.

## Validation plan

To validate the analytic in a future lab iteration:

- Generate a controlled sequence of failed SSH logins.
- Confirm the failure threshold triggers as expected.
- Generate a successful authentication after failures using a disposable test account.
- Confirm the correlation logic matches the same source, host, and username.
- Test unrelated failures from another source or account to ensure they do not incorrectly correlate.
- Record event counts, timestamps, query output, and known limitations.

## Current validation status

**Conceptual detection design; not a deployed or independently validated SIEM rule.** The original lab notes document Hydra's successful password discovery but do not include a saved detection query or raw event data sufficient to validate a correlation rule.
