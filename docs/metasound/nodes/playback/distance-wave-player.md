---
label: "AP: Distance Wave Player"
icon: file
order: 90
---
# AP: Distance Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Choose recordings from configurable distance ranges at play time.

<!-- IMAGE SLOT: docs/static/images/nodes/node-distance-wave-player.png -->

## When to use it

Near/mid/far weapon tails, ambience and sound-design perspective changes.

## Quick setup

Configure the dynamic distance ranges and their `Waves` arrays. Supply `Distance (cm)` before triggering `Play`.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Select one sample from the current distance range. |
| `Stop` | Trigger | Stop every active voice. |
| `Distance (cm)` | Float | Source-to-listener distance in centimetres. |
| `Max Distance (cm)` | Float | Hard playback cutoff evaluated only on Play. |
| `Max Voices` | Integer | Maximum simultaneous samples (1 to 16). |
| `No Immediate Repeat` | Boolean | Avoid selecting the same sample consecutively  within the selected distance range. |
| `Start Distance (cm)` | Float | Distance at which this range becomes active. |
| `Waves` | Wave Asset Array | Array of samples for this range. |
| `Volume` | Float | Linear gain latched when a sample begins. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mixed mono audio of all active voices. |
| `On Finished` | Trigger | Fires when the last playing voice ends naturally.  Stop or rejected Play events do not trigger it. |

## Behaviour and design notes

Distance selection is evaluated when a voice starts; it is not an automatic live crossfade between active recordings.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
