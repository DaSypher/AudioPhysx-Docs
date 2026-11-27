---
label: "AP: Flyby Wave Player"
icon: rocket
order: 90
---
# AP: Flyby Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Play randomized near-miss whizz recordings, optionally including a ballistic crack layer.

<!-- IMAGE SLOT: docs/static/images/nodes/node-flyby-wave-player.png -->

## When to use it

Bullets, arrows and fast objects passing near the listener.

## Quick setup

Fill `Whizz Waves` and optionally `Crack Waves`, feed flyby parameters and trigger `Play`.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Start one flyby, restarting this player if already active. |
| `Stop` | Trigger | Stop immediately; does not emit On Finished. |
| `Whizz Waves` | Wave Asset Array | Randomly chosen rush/whizz Wave Asset Array. |
| `Crack Waves` | Wave Asset Array | Randomly chosen supersonic crack Wave Asset Array. |
| `Distance (m)` | Float | Closest approach in metres. Optional: for custom graph controls. |
| `Speed (m/s)` | Float | Projectile speed in metres/second. |
| `Intensity` | Float | Normalized near-miss strength, 0 to 1. |
| `Speed of Sound (m/s)` | Float | Local speed of sound; used to validate shock playback. |
| `Shock` | Float | 1 = Mach cone reaches listener (0 = ordinary whizz). |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mono whizz and crack mix. Spatialize in the MetaSound Source. |
| `On Finished` | Trigger | All started variations have finished naturally. |
| `On Rejected` | Trigger | No playable wave was selected. |

## Behaviour and design notes

Spatialize the mono output through the MetaSound Source or use the Blueprint flyby helper. The acoustic model is an approximation, not full ballistic shock-wave simulation.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
