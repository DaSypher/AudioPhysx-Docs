---
label: "AP: Random Sequence Wave Player"
icon: list-ordered
order: 90
---
# AP: Random Sequence Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Play an ordered sequence where each step chooses one random recording from an array.

<!-- IMAGE SLOT: docs/static/images/nodes/node-random-sequence-wave-player.png -->

## When to use it

Varying multi-stage actions, environmental interactions, or sequences that should keep their structure without sounding identical.

## Quick setup

Add steps to the `Sequence Steps` group and fill each `Waves` array with alternatives. Trigger `Play` and connect `Out Mono`.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Start the sequence. Play again to restart. |
| `Stop` | Trigger | Stop immediately without On Finished. |
| `Loop Sequence` | Boolean | Restart after the final recording. |
| `Waves` | Wave Asset Array | A Wave Asset Array for this expandable step. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Audio from the current step. |
| `On Finished` | Trigger | Fires after all playable steps finish. |

## Behaviour and design notes

Each step has its own array. The player selects one recording per step and waits for it to finish before advancing. Empty steps are skipped.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
