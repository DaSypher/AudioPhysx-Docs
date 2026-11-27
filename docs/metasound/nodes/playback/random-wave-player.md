---
label: "AP: Random Wave Player"
icon: shuffle
order: 90
---
# AP: Random Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Select one random playable Wave Asset and output its mono audio.

<!-- IMAGE SLOT: docs/static/images/nodes/node-random-wave-player.png -->

## When to use it

Most non-repeating one-shots: Foley, interactions, weapons and interface sounds.

## Quick setup

Populate `Waves`, trigger `Play`, and connect `Out Mono`. Configure pitch variation and simultaneous-voice count when useful.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Select one random valid Wave Asset and play it. |
| `Stop` | Trigger | Stop all active wave playback. |
| `Waves` | Wave Asset Array | Array of Wave Assets to randomly select from. |
| `No Immediate Repeat` | Boolean | Prevent consecutive selections of the same  wave when alternatives are available. |
| `Pitch Shift (st)` | Float | Playback pitch adjustment in semitones.  Also changes playback duration. |
| `Max Voices` | Integer | Maximum number of overlapping recordings,  from 1 to 16. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mixed mono output from active voices. |
| `On Finished` | Trigger | Triggered when the final active voice  finishes naturally. |
| `On Rejected` | Trigger | Triggered when playback cannot start. |
| `Selected Index` | Integer | Index of the most recently accepted wave,  or -1 for a rejected selection. |

## Behaviour and design notes

Use `No Immediate Repeat` when you have multiple recordings and want to avoid the same take twice in succession.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
