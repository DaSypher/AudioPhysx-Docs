---
label: "AP: Distance Delay"
icon: file
order: 70
---
# AP: Distance Delay

**MetaSound category:** `AudioPhysx → Propagation`  
**Source contract:** Unreal Engine 5.8.4 development source

Delay mono audio based on distance divided by speed of sound.

<!-- IMAGE SLOT: docs/static/images/nodes/node-distance-delay.png -->

## When to use it

Large propagation distances, distinct far-off events and controlled travel-time effects.

## Quick setup

Supply `Distance (cm)`, speed of sound and maximum delay capacity, then trigger `Relatch` when you need a new fixed delay.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio` | Audio (mono) | Mono audio input. |
| `Distance (cm)` | Float | Distance travelled by sound in Unreal centimetres. Sampled only when latched. |
| `Speed of Sound (m/s)` | Float | Propagation speed in metres per second.  Default 343 m/s. Converted internally to cm/s.  Sampled only when latched. |
| `Max Delay (s)` | Float | Maximum delay capacity in seconds (0.01-10). Allocated when the operator is constructed. |
| `Relatch` | Trigger | Recalculate propagation delay and discard the previous pending audio tail. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio` | Audio (mono) | Delayed mono audio. |

## Behaviour and design notes

Delay capacity is allocated when the operator is built. Increasing it raises per-instance memory use.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Propagation overview](../../propagation.md) and [Troubleshooting](../../../support/troubleshooting.md).
