# Wireless incident checklist

Use this checklist when you suspect unauthorized access to a home or small-office Wi-Fi network. It is for defensive review of networks you own or are authorized to administer. A device name, vendor, or MAC address is not reliable proof of a person's identity; these values may be absent, randomized, or changed.

## Start with the impact

- What specifically happened: an unfamiliar client, an account alert, changed router settings, unusual traffic, or service disruption?
- When was it first observed? Record local time and time zone.
- What data, devices, or services may have been exposed or changed?
- Is there an immediate safety or business-continuity concern?

## Preserve useful records

Before resetting equipment, save or export relevant router/security logs and note the device model, firmware version, time settings, and current configuration if it is safe to do so. Record what you observe and where it came from. Router logs may be incomplete or short-lived; do not assume absence of a log proves absence of access.

Avoid posting public screenshots that reveal Wi-Fi names, public IP addresses, device identifiers, or account details.

## Investigate identity and access

1. Review the router's connected-client list and authentication/security events for the relevant time window.
2. Compare entries against devices you recognize, including guest and household devices. Verify with their owners rather than relying only on a device label.
3. Check how the network is configured: security mode, guest access, administrator account, remote management, and firmware support status.
4. Ask whether the Wi-Fi passphrase was shared, reused, entered into an unexpected portal, or stored on a lost device. Do not ask anyone to send you the password.
5. Review router administrator access and changes. If available, check provider or managed-network logs for the same timeframe.
6. If the evidence is unclear, record the uncertainty and contact the router vendor, ISP, or your security team. Do not identify a particular gadget or person without corroborating evidence.

## Contain and recover

Use the vendor's trusted administrative interface and guidance. If unauthorized access is plausible:

- Change the router administrator password from a known-clean device.
- Set a new, unique Wi-Fi passphrase and update authorized devices through a trusted process.
- Remove unknown guest access and disable unused remote administration or convenience features.
- Install supported firmware updates; replace equipment that is no longer supported.
- Select WPA3-Personal when compatible, or WPA2-AES where WPA3 is unavailable. Avoid obsolete modes and weak compatibility settings when feasible.
- Review DNS, port forwarding, account recovery, and configuration for unexplained changes.
- Document the time and impact of each change. If a serious investigation is underway, ask responders before a factory reset because it may erase evidence.

## What the evidence can and cannot tell you

A new client entry may support that a device joined the network, but does not by itself establish who controlled it, what it accessed, or what objective was achieved. A familiar-looking name does not prove a device is trusted. The key questions remain: **what changed, when, which credential or access path was involved, what was touched, and is access still possible?**

Continue with the [incident response playbook](incident-response.md) and [evidence worksheet](evidence-and-timeline.md) if accounts, endpoints, cloud services, or data may also be affected.
