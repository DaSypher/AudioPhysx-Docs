---
label: "Playback"
icon: play
order: 90
---
# Playback

Playback nodes select and play recordings. Most expose `Out Mono` and, where implemented, playback completion events.

| Node | Purpose |
| --- | --- |
| [AP: Sequence Wave Player](nodes/playback/sequence-wave-player.md) | Play a set of recordings in a fixed order, starting each wave after the previous one finishes. |
| [AP: Random Sequence Wave Player](nodes/playback/random-sequence-wave-player.md) | Play an ordered sequence where each step chooses one random recording from an array. |
| [AP: Start Loop End Player](nodes/playback/start-loop-end.md) | Play a randomized introduction, repeat middle recordings, then play a randomized ending on release. |
| [AP: Random Wave Player](nodes/playback/random-wave-player.md) | Select one random playable Wave Asset and output its mono audio. |
| [AP: Shuffle-Bag Wave Player](nodes/playback/shuffle-bag-wave-player.md) | Draw from a weighted bag of wave variations while reducing repetition across successive triggers. |
| [AP: Layered Wave Player](nodes/playback/layered-wave-player.md) | Trigger multiple Wave Assets as a single sound stack, with per-layer gain, pitch and onset delay. |
| [AP: Distance Wave Player](nodes/playback/distance-wave-player.md) | Choose recordings from configurable distance ranges at play time. |
| [AP: PhysMat Wave Player](nodes/playback/physmat-wave-player.md) | Select recordings by exact Physical Material asset path, with fallback recordings. |
| [AP: Surface Wave Player](nodes/playback/surface-wave-player.md) | Select waves using Unreal physical surface types and a configured route table. |
| [AP: Flyby Wave Player](nodes/playback/flyby-wave-player.md) | Play randomized near-miss whizz recordings, optionally including a ballistic crack layer. |

## How to choose

- **One random sample:** Random Wave Player.
- **Control repeat cycles:** Shuffle-Bag Wave Player.
- **Several layers at once:** Layered Wave Player.
- **Sounds in order:** Sequence Wave Player.
- **A varied multi-stage event:** Random Sequence Wave Player.
- **Held action with an ending:** Start Loop End Player.
- **Material-aware sound:** PhysMat or Surface Wave Player.
- **Near/mid/far recording choices:** Distance Wave Player.
- **Near-miss projectiles:** Flyby Wave Player.

For a reproducible demonstration, start with the [first MetaSound tutorial](../getting-started/first-metasound.md).
