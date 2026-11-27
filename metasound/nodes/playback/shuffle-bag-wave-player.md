# AP: Shuffle-Bag Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Draw from a weighted bag of wave variations while reducing repetition across successive triggers.

## When to use it

Footsteps, dialogue barks, repetitive mechanisms and repeated impact samples.

## Quick setup

Supply a `Waves` array and optional aligned `Weights`. Trigger `Play`; use `Reset Bag` when you want a fresh cycle.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Draw and play one unused eligible wave. |
| `Stop` | Trigger | Stop all current voices without firing On Finished. |
| `Reset Bag` | Trigger | Discard the remaining bag; keep playing voices. |
| `Waves` | Wave Asset Array | Wave Asset Array. Maximum 128 entries. |
| `Weights` | Float Array | Optional non-negative weights aligned with Waves. Missing entries use 1; zero excludes an entry. |
| `Pitch Shift (st)` | Float | Playback-rate pitch in semitones, -24 to 24. |
| `Gain (dB)` | Float | Gain for newly started voices, -96 to +12 dB. |
| `Max Voices` | Integer | Maximum overlapping voices (1 to 16). |
| `Seed` | Integer | Nonzero seed is deterministic. Zero selects a random seed. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mixed playback audio. |
| `On Finished` | Trigger | Final active voice finished naturally. |
| `On Rejected` | Trigger | No eligible wave, free voice or playable proxy. |
| `Selected Index` | Integer | Most recent selected index; -1 on rejection/Stop. |
| `Bag Remaining` | Integer | Number of unplayed entries left in the current bag. |

## Behaviour and design notes

`Selected Index` and `Bag Remaining` are diagnostic outputs. Invalid or zero-weight entries are not eligible.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
