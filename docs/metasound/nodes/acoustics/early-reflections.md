---
label: "AP: Early Reflections"
icon: broadcast
order: 80
---
# AP: Early Reflections

**MetaSound category:** `AudioPhysx → Acoustics`  
**Source contract:** Unreal Engine 5.8.4 development source

Add a small set of simulated early reflections to a mono recording.

<!-- IMAGE SLOT: docs/static/images/nodes/node-early-reflections.png -->

## When to use it

Interior spaces, hard-walled corridors and acoustic previewing.

## Quick setup

Connect mono audio and an upstream `Source Finished` trigger, then set room size, wet/dry levels and damping.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio In` | Audio (mono) | Mono signal to reflect. |
| `Source Finished` | Trigger | Connect the Wave Player's On Finished output. |
| `Room Size (m)` | Float | Controls four synthetic extra reflection  path lengths. Does not trace geometry. |
| `Speed of Sound (m/s)` | Float | Propagation speed for reflection delays. |
| `Dry Level` | Float | Level of the original sound. |
| `Wet Level` | Float | Level of the reflection taps. |
| `HF Damping` | Float | Higher values remove more high frequencies  from reflections. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Original sound plus early reflections. |
| `On Finished` | Trigger | Fires after the last reflection tail. |

## Behaviour and design notes

This is a synthetic approximation controlled by room-size parameters, not a geometry-traced reflection solver.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Acoustics overview](../../acoustics.md) and [Troubleshooting](../../../support/troubleshooting.md).
