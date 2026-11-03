# Wireless observations, endpoints, and false positives

This guide gives a defensive, high-level way to reason about nearby wireless activity. It is not a guide to operating or configuring offensive hardware. Only monitor systems and networks you own or are explicitly authorized to administer, and follow applicable privacy and radio regulations.

## What is an endpoint here?

In ordinary security discussions, an endpoint is a device such as a phone, laptop, tablet, or server. In a wireless investigation, observations can also involve access points, routers, clients, and radio protocol activity. Depending on the device and supported accessories, a multi-radio tool may observe signals from technologies such as Wi-Fi, Bluetooth, NFC/RFID, infrared, or other short-range radio systems.

The exact capabilities depend on hardware, firmware, accessories, region, and configuration. A signal being detectable does not mean it is authenticated, understood, actionable, or evidence of unauthorized access.

## Observation is not attribution

Wireless devices routinely emit or receive discovery and management traffic. A nearby observation may indicate that a radio is present or scanning; on its own, it does not establish that a device joined a network, that a person controls it, or that data was accessed. Names and identifiers can be missing, randomized, duplicated, or spoofed.

Likewise, a tool's own radio activity and local test devices can appear in nearby observations. This is not automatically a self-attack or compromise. The behavior of any specific product depends on its design and configuration; do not assume that it will execute actions merely because it receives a signal.

## Handle false positives carefully

Collection tools can provide incomplete or ambiguous information. A detected network name, device identifier, signal, or event should be treated as a lead to verify—not a conclusion. Corroborate with independent, authorized sources such as access-point authentication records, identity-provider events, endpoint alerts, and user confirmation. Check timestamps, time zones, device ownership, and known test activity.

Avoid deliberately generating misleading wireless activity or trying to distract an operator. That can interfere with other users, create safety or legal concerns, and make incident evidence less reliable. For defense, improve signal-to-noise by documenting known devices and test windows, tuning approved monitoring, and requiring corroboration before escalating an alert.

## Defensive investigation questions

- What exactly was observed, by which system, and at what time?
- Does the observation show only detection, or does an independent source confirm authentication or access?
- Is the device expected, including guest devices, test equipment, or privacy-randomized identifiers?
- Which credentials or access methods were configured, and were they shared or recently changed?
- Is there evidence of a configuration change, account use, data access, or service impact?
- What is confirmed, what is only a hypothesis, and what evidence would safely distinguish them?

Use the [wireless incident checklist](wireless-incident-checklist.md) to review network access, and the [evidence and timeline worksheet](evidence-and-timeline.md) to record observations without overstating what a gadget can prove.
