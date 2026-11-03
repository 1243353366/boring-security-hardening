# Incident response playbook

A compact, evidence-led workflow for suspected account, endpoint, cloud, phishing, or network incidents. Follow your organization's incident plan and applicable legal, contractual, privacy, and reporting requirements. For serious incidents, involve qualified incident responders and relevant service providers early.

## Principles

- **Impact before gadget:** identify the objective or change, not the brand of tool suspected.
- **Preserve before altering:** retain relevant logs and messages when safe and feasible. Record any containment actions and their time.
- **Use trusted paths:** investigate and change credentials from a known-clean device and known-good administrative route.
- **Minimize harm:** contain proportionately; do not destroy evidence or interrupt essential services without considering the impact.
- **Separate fact from hypothesis:** label what is confirmed, inferred, and unknown.
- **No blame:** prompt reporting improves outcomes.

## 1. Confirm the impact

Ask what may have been accessed, created, executed, changed, or disrupted:

- Data viewed, downloaded, shared, or altered?
- Unrecognized process, application, browser extension, or scheduled activity?
- New account, administrator, MFA method, recovery address, forwarding rule, API key, or OAuth grant?
- Unexpected payment, configuration change, lockout, or service outage?
- Signs of access continuing after a password change or reboot?

Record the source of each observation. Do not treat a single unfamiliar device name or alert as proof on its own.

## 2. Establish scope

Determine affected identities, devices, services, networks, data, and time period. Check for related alerts and sign-ins across identity, email, endpoint, cloud, and network providers. Consider whether an account is shared or whether one compromised identity could access other systems.

Use provider-supported audit and security views. Avoid collecting more personal or sensitive data than needed. Do not probe systems outside your authority.

## 3. Build a timeline

Record the earliest known event, initial warning, access events, subsequent changes, discovery, and containment. Include timestamp, time zone, source, observer, and confidence. Preserve original timestamps and note if clocks may be inaccurate.

See the [evidence and timeline worksheet](evidence-and-timeline.md).

## 4. Identify a plausible access path

Use evidence to assess possibilities such as:

- Stolen, reused, exposed, or phished credentials; weak recovery process; unexpected MFA approval.
- Vulnerable or unsupported software, malicious or unwanted software, or an exposed service.
- Misconfiguration, excessive permissions, exposed secret, or unreviewed integration.
- A legitimate account or device used in an unexpected way.
- Wireless access using a credential, guest access, or a configuration weakness.

Do not infer a specific attack technique or physical device from a generic symptom. Keep multiple hypotheses open until evidence narrows them.

## 5. Contain safely

Choose containment based on the risk and available evidence. Examples include disabling or restricting an affected account, revoking sessions and tokens, removing an unrecognized integration, isolating a device using approved tools, or contacting the service provider. Record who made each change and when.

If data destruction, active extortion, safety risks, or critical services are involved, escalate immediately to the appropriate incident lead, provider, or authorities. Avoid communicating with a suspected attacker or making payment decisions without organizational and legal guidance.

## 6. Eradicate and recover

After scope is understood and evidence is preserved as appropriate:

- Remove unauthorized accounts, access methods, applications, and configuration changes.
- Patch or replace affected software and devices; correct the underlying misconfiguration.
- Reset credentials from a known-clean device; rotate exposed secrets and revoke sessions, API keys, and tokens. Review MFA and recovery methods.
- Restore affected systems or data from a known-good backup or trusted image where appropriate.
- Verify controls and monitor for recurrence before returning systems to normal use.

Changing a password alone may not remove active sessions, malicious forwarding rules, OAuth grants, access tokens, or persistence. Review the full set of access paths for the affected service.

## 7. Close out and improve

Document the confirmed impact, scope, root cause (if known), response decisions, recovery, remaining risk, and notifications. Keep evidence handling consistent with organizational policy. Identify a small number of owners and due dates for follow-up controls, then update the baseline checklist or playbook.

## Quick decision record

- Incident lead / contact:
- First observed (date, time, time zone):
- Current impact / safety concern:
- Affected identities, devices, and services:
- Confirmed facts:
- Hypotheses and confidence:
- Evidence preserved and location:
- Containment action, owner, and time:
- Provider / security team contacted:
- Next review time:
