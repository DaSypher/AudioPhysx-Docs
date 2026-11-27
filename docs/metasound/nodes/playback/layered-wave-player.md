---
label: "AP: Layered Wave Player"
icon: file
order: 90
---
# AP: Layered Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Trigger multiple Wave Assets as a single sound stack, with per-layer gain, pitch and onset delay.

<!-- IMAGE SLOT: docs/static/images/nodes/node-layered-wave-player.png -->

## When to use it

Layered weapons, impacts, cinematic hits and machinery.

## Quick setup

Populate `Layer Waves` and optional aligned arrays for gain, pitch and delay. Trigger `Play`.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Start the valid layers as one atomic stack. |
| `Stop` | Trigger | Stop all stacks. Does not fire On Finished. |
| `Layer Waves` | Wave Asset Array | Wave Asset array: indices 0 to 7, one sound per layer. |
| `Layer Gains (dB)` | Float Array | Optional per-layer gains, aligned with Layer Waves. Missing values = 0 dB. |
| `Layer Pitch (st)` | Float Array | Optional per-layer playback-rate pitch offsets in semitones. Missing = 0. |
| `Layer Delays (ms)` | Float Array | Optional per-layer onset delay, 0 to 2000 ms. Missing = 0. |
| `Max Voices` | Integer | Maximum simultaneous individual layers across all stacks, 1 to 32. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mono mix of all active layers. |
| `On Finished` | Trigger | Last layer of all active stacks finished naturally. |
| `On Rejected` | Trigger | No playable layers or insufficient free voices for the entire stack. |
| `Active Layers` | Integer | Number of active or pending layers. |

## Behaviour and design notes

Array entries are indexed by layer. The implementation allows up to eight layers per stack, subject to total voice limits.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
