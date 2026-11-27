---
label: "AP: Impact Dynamics"
icon: zap
order: 80
---
# AP: Impact Dynamics

**MetaSound category:** `AudioPhysx → Acoustics`  
**Source contract:** Unreal Engine 5.8.4 development source

Shape the transient, level and filtering of an impact recording according to impact strength.

<!-- IMAGE SLOT: docs/static/images/nodes/node-impact-dynamics.png -->

## When to use it

Soft versus hard footsteps, collisions and physical interactions.

## Quick setup

Connect an impact recording to `Audio In`, fire `Impact` when playback starts and supply normalized `Impact Strength`.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio In` | Audio (mono) | Mono audio from the impact Wave Player. |
| `Impact` | Trigger | Restart the transient when playback starts. |
| `Impact Strength` | Float | Normalized impact strength, 0 to 1. |
| `Soft Gain` | Float | Linear gain at impact strength 0. |
| `Hard Gain` | Float | Linear gain at impact strength 1. |
| `Soft Cutoff (Hz)` | Float | Low-pass cutoff for gentle impacts. |
| `Hard Cutoff (Hz)` | Float | Low-pass cutoff for strong impacts. |
| `Transient Boost` | Float | Extra attack gain applied to harder hits. |
| `Transient Time (ms)` | Float | Duration of the attack enhancement. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Impact-shaped mono audio. |
| `Applied Strength` | Float | Clamped strength used by this operator. |

## Behaviour and design notes

This is a sound-shaping operator; it does not detect collisions or generate the source recording by itself.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Acoustics overview](../../acoustics.md) and [Troubleshooting](../../../support/troubleshooting.md).
