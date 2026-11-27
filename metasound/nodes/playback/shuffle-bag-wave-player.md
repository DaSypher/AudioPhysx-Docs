# AP: Shuffle-Bag Wave Player

**MetaSound · AudioPhysx / Playback**

Choose variations without repeatedly favoring the same few recordings, with weights and an explicit bag reset.

## What actually happens

A shuffle bag builds a cycle of eligible selections, drawing from that pool until it has been exhausted. That differs from plain random selection: over a full cycle, you get more controlled coverage of the available options.

The node also supports weights, gain and pitch controls and multiple voices. It is useful for repetitive sound events where players can quickly notice when a particular clip keeps returning.

## Hear it in a game

Put six footsteps recorded on the same surface into `Waves`. Trigger the node on every step. The sequence should feel varied without the same take being chosen repeatedly at random. Use `Reset Bag` if the game needs to deliberately start a new selection cycle.

## Build a working graph

>>> 1. Build the bag
Supply the `Waves` array with the desired recordings.
>>>

>>> 2. Configure the selection rules
If using `Weights`, align the weight entries to the wave array and test the resulting distribution; omit extra complexity when equal weighting is enough.
>>>

>>> 3. Play and reset when needed
Wire `Play` and `Out Mono`. Use `Reset Bag` only when deliberately restarting the selection history.
>>>

## The controls that matter

`Weights` biases which clips appear more or less often; they do not change loudness. `Seed` controls reproducibility when a deterministic sequence is useful for tests. `Pitch Shift (st)` and `Gain (dB)` shape the sound after selection. `Max Voices` limits overlap.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mixed playback audio.
- **`On Finished`** · Trigger — Final active voice finished naturally.
- **`On Rejected`** · Trigger — No eligible wave, free voice or playable proxy.
- **`Selected Index`** · Integer — Most recent selected index; -1 on rejection/Stop.
- **`Bag Remaining`** · Integer — Number of unplayed entries left in the current bag.

## Things to watch for

- Weights and wave indices must describe the same selection order; keep arrays synchronized when editing.
- Shuffle-bag behaviour applies to *selection*, not the timing of events. The game still needs to send the `Play` triggers.

==- Full input reference
- **`Play`** · *Trigger* — Draw and play one unused eligible wave.
- **`Stop`** · *Trigger* — Stop all current voices without firing On Finished.
- **`Reset Bag`** · *Trigger* — Discard the remaining bag; keep playing voices.
- **`Waves`** · *Wave Asset Array* — Wave Asset Array. Maximum 128 entries.
- **`Weights`** · *Float Array* — Optional non-negative weights aligned with Waves. Missing entries use 1; zero excludes an entry.
- **`Pitch Shift (st)`** · *Float* — Playback-rate pitch in semitones, -24 to 24.
- **`Gain (dB)`** · *Float* — Gain for newly started voices, -96 to +12 dB.
- **`Max Voices`** · *Integer* — Maximum overlapping voices (1 to 16).
- **`Seed`** · *Integer* — Nonzero seed is deterministic. Zero selects a random seed.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mixed playback audio.
- **`On Finished`** · Trigger — Final active voice finished naturally.
- **`On Rejected`** · Trigger — No eligible wave, free voice or playable proxy.
- **`Selected Index`** · Integer — Most recent selected index; -1 on rejection/Stop.
- **`Bag Remaining`** · Integer — Number of unplayed entries left in the current bag.
===

## Continue learning

[Random Wave Player](random-wave-player.md) is simpler when draw-history control is unnecessary. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
