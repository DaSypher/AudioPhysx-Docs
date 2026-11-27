---
label: "AP: Sequence Wave Player"
icon: list-ordered
order: 90
---
# AP: Sequence Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Play a set of recordings in a fixed order, starting each wave after the previous one finishes.

<!-- IMAGE SLOT: docs/static/images/nodes/node-sequence-wave-player.png -->

## When to use it

Sequences of mechanical actions, short scripted audio moments, or composed one-shot sounds.

## Quick setup

Add the node, expand the Wave slots, assign recordings in order, connect `On Play` to `Play`, and route `Out Mono` to the MetaSound output.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Play the wave sequence from the beginning. Retriggering restarts it. |
| `Stop` | Trigger | Stop playback immediately, without firing On Finished. |
| `Loop Sequence` | Boolean | Restart from the first valid wave after the last finishes. |
| `Wave` | Wave Asset | Wave Asset to play in sequence. Add or remove Wave slots on the node. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mono audio output from the currently playing wave. |
| `On Finished` | Trigger | Fires once after the last wave finishes naturally (when not looping). |

## Behaviour and design notes

Stop cancels playback without a natural-completion trigger. Set `Loop Sequence` to repeat the entire list.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
