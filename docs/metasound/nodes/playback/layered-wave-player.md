---
label: "AP: Layered Wave Player"
icon: file
order: 90
---
# AP: Layered Wave Player

**MetaSound · AudioPhysx / Playback**

Build one composite effect from several recordings that start together or at different offsets.

<!-- IMAGE SLOT: docs/static/images/nodes/node-layered-wave-player.png -->

## What actually happens

Some sounds are easier to construct from separate layers: an attack transient, a low-frequency body, and a mechanical detail. This player starts the configured layers as one event and combines them into a mono output.

`Layer Gains (dB)`, `Layer Pitch (st)` and `Layer Delays (ms)` are **arrays aligned by index** to `Layer Waves`. That lets one layer be softer, another pitched differently, and a third delayed slightly without needing separate Wave Player nodes.

## Hear it in a game

For a heavy door, use a short handle click, a low mechanical movement, and a latch close. Adjust the layer delays until the action feels physically coordinated instead of sounding like three unrelated recordings.

## Build a working graph

>>> 1. Choose the layers
Populate `Layer Waves` with the recordings that should form one compound event.
>>>

>>> 2. Align per-layer controls
Create optional gain, pitch and delay arrays in the **same order** as the wave array.
>>>

>>> 3. Trigger the combined effect
Connect `Play` and `Out Mono`, then increase `Max Voices` only if multiple compound events should overlap.
>>>

## The controls that matter

`Layer Delays (ms)` offsets the start of a particular layer; it does not represent the total sound duration. `Layer Gains (dB)` trims individual contributions. `Layer Pitch (st)` shifts an individual layer in semitones. `Max Voices` limits concurrent playback capacity.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mono mix of all active layers.
- **`On Finished`** · Trigger — Last layer of all active stacks finished naturally.
- **`On Rejected`** · Trigger — No playable layers or insufficient free voices for the entire stack.
- **`Active Layers`** · Integer — Number of active or pending layers.

## Things to watch for

- Do not assume different recordings are transient-aligned. Inspect the samples and compensate for leading silence where necessary.
- A large number of loud layers can clip when added together. Gain-stage the components before increasing the final output.

==- Full input reference
- **`Play`** · *Trigger* — Start the valid layers as one atomic stack.
- **`Stop`** · *Trigger* — Stop all stacks. Does not fire On Finished.
- **`Layer Waves`** · *Wave Asset Array* — Wave Asset array: indices 0 to 7, one sound per layer.
- **`Layer Gains (dB)`** · *Float Array* — Optional per-layer gains, aligned with Layer Waves. Missing values = 0 dB.
- **`Layer Pitch (st)`** · *Float Array* — Optional per-layer playback-rate pitch offsets in semitones. Missing = 0.
- **`Layer Delays (ms)`** · *Float Array* — Optional per-layer onset delay, 0 to 2000 ms. Missing = 0.
- **`Max Voices`** · *Integer* — Maximum simultaneous individual layers across all stacks, 1 to 32.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mono mix of all active layers.
- **`On Finished`** · Trigger — Last layer of all active stacks finished naturally.
- **`On Rejected`** · Trigger — No playable layers or insufficient free voices for the entire stack.
- **`Active Layers`** · Integer — Number of active or pending layers.
===

## Continue learning

[Random Sequence](random-sequence-wave-player.md) plays *one after another*, not as simultaneous layers. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
