---
label: "AP: Trigger Cooldown"
icon: clock
order: 60
---
# AP: Trigger Cooldown

**MetaSound category:** `AudioPhysx → QoL`  
**Source contract:** Unreal Engine 5.8.4 development source

Let triggers through only when a configured cooldown has elapsed.

<!-- IMAGE SLOT: docs/static/images/nodes/node-trigger-cooldown.png -->

## When to use it

Preventing repeated impact or UI sounds from firing too frequently.

## Quick setup

Connect `In`, configure `Cooldown (ms)`, and route `On Passed` to the destination.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `In` | Trigger | Triggers to rate-limit. |
| `Reset` | Trigger | Clear the cooldown; simultaneous In triggers may pass. |
| `Cooldown (ms)` | Float | Minimum time between accepted triggers. Zero passes all triggers. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `On Passed` | Trigger | Triggers allowed through at the original sample frame. |
| `On Rejected` | Trigger | Triggers blocked by the cooldown at the original sample frame. |
| `Remaining (ms)` | Float | Cooldown remaining at the end of this audio block. Block-rate Float. |

## Behaviour and design notes

`On Rejected` exposes blocked triggers so the graph can respond or debug. `Reset` clears the current cooldown.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [QoL overview](../../qol.md) and [Troubleshooting](../../../support/troubleshooting.md).
