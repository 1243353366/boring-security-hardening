# Boring Security Hardening

Practical defenses for the risks that most often matter: compromised endpoints, browsers, credentials, cloud accounts, phishing, and misconfiguration.

The premise is simple: real-world incidents rarely require broken cryptography. They more often exploit misplaced trust, stale software, weak account recovery, excessive permissions, legacy settings, or a convincing message. Strong defaults and repeatable response habits close a lot of that gap.

## Start here

- [Baseline checklist](docs/baseline-checklist.md) — a prioritized, platform-neutral hardening checklist.
- [Incident response playbook](docs/incident-response.md) — work backward from impact and evidence to cause, scope, and containment.
- [Evidence and timeline worksheet](docs/evidence-and-timeline.md) — record what changed without overclaiming.
- [Wireless incident checklist](docs/wireless-incident-checklist.md) — investigate suspicious Wi-Fi access by identity and artifacts, not by guessing which gadget was used.
- [Wireless observations and false positives](docs/wireless-observations.md) — understand what nearby radio observations can and cannot establish.
- [Security policy](SECURITY.md) — scope, safe use, and how to report a problem in this project.

## The defensive question

> What changed that shouldn't have changed?

A successful attack is defined by the objective achieved—not by the tool used. An incident may involve unauthorized access, execution, persistence, privilege escalation, data access or alteration, exfiltration, or service disruption. Responders should establish what happened, when, to which identities and systems, and whether access remains.

A useful investigation model is:

```text
Goal achieved
    ↑
Actions taken
    ↑
Capabilities gained
    ↑
Initial access
```

Start with the impact and work downward. Preserve evidence and keep a clear distinction between confirmed facts, hypotheses, and unknowns.

## Priorities

1. Keep supported devices, browsers, applications, and network equipment updated.
2. Use unique passwords stored in a reputable password manager; enable phishing-resistant MFA where available.
3. Remove unnecessary administrator rights, accounts, apps, browser extensions, and cloud permissions.
4. Secure account recovery and protect email accounts, which often control password resets elsewhere.
5. Use modern, vendor-supported Wi-Fi security and disable obsolete compatibility modes when practical.
6. Require HTTPS and valid certificate checks; never train users to click through certificate warnings.
7. Back up important data and periodically test restoration.
8. Prepare a simple incident process before an incident occurs.

## How to use this repository

This is general defensive guidance, not a substitute for vendor documentation, legal advice, or a qualified incident-response team. Adapt controls to your environment, safety needs, and regulatory requirements. For a suspected compromise, use a known-clean device to change credentials and contact your organization's security team or service provider.

## Contributing

Contributions should be actionable, defensive, vendor-neutral where possible, and clear about assumptions. Do not include live credentials, personal data, exploit payloads, or instructions for unauthorized access. See [SECURITY.md](SECURITY.md).

---

Thanks for reading. More of my work: [github.com/1243353366](https://github.com/1243353366).
