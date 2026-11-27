---
label: "AP: Random Wave Player"
icon: shuffle
order: 90
---
# AP: Random Wave Player

**MetaSound · AudioPhysx / Playback**

Play a random recording from an array whenever an event occurs, with optional variation and multiple simultaneous voices.

<!-- IMAGE SLOT: docs/static/images/nodes/node-random-wave-player.png -->

## What actually happens

This is the everyday alternative to placing a Random Get and Wave Player chain in every graph. The node chooses a playable Wave Asset from `Waves` on each `Play`, then sends the decoded audio to one mono output.

For events that can happen in quick succession, the configured voice capacity allows recordings to overlap. `No Immediate Repeat` is useful when a small sound library would otherwise make identical successive takes too obvious.

## Hear it in a game

Use five short stone-impact recordings and connect a gameplay impact trigger to `Play`. Trigger them repeatedly at different intervals. You should hear variation in the selected recordings rather than a perfectly identical impact each time.

## Build a working graph

>>> 1. Prepare the variation pool
Supply several recordings of the same *kind* of event to `Waves`.
>>>

>>> 2. Connect the gameplay trigger
Trigger `Play` when that event happens; connect `Out Mono` to the output.
>>>

>>> 3. Test overlapping events
Set `Max Voices` for the expected overlap and test `No Immediate Repeat` with at least two valid choices.
>>>

## The controls that matter

`Pitch Shift (st)` changes playback pitch in **semitones**; for orientation, +12 semitones is one octave and −12 is one octave down. `Max Voices` is a capacity limit, not a guarantee that every incoming trigger will be heard under load. `Stop` is for stopping the active playback rather than selecting another sound.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mixed mono output from active voices.
- **`On Finished`** · Trigger — Triggered when the final active voice  finishes naturally.
- **`On Rejected`** · Trigger — Triggered when playback cannot start.
- **`Selected Index`** · Integer — Index of the most recently accepted wave,  or -1 for a rejected selection.

## Things to watch for

- Recordings should be edited to comparable perceived loudness first. Randomization will not normalize badly mismatched takes.
- Check what happens at the maximum simultaneous-voice setting in an actual combat or destruction scene.

==- Full input reference
- **`Play`** · *Trigger* — Select one random valid Wave Asset and play it.
- **`Stop`** · *Trigger* — Stop all active wave playback.
- **`Waves`** · *Wave Asset Array* — Array of Wave Assets to randomly select from.
- **`No Immediate Repeat`** · *Boolean* — Prevent consecutive selections of the same  wave when alternatives are available.
- **`Pitch Shift (st)`** · *Float* — Playback pitch adjustment in semitones.  Also changes playback duration.
- **`Max Voices`** · *Integer* — Maximum number of overlapping recordings,  from 1 to 16.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mixed mono output from active voices.
- **`On Finished`** · Trigger — Triggered when the final active voice  finishes naturally.
- **`On Rejected`** · Trigger — Triggered when playback cannot start.
- **`Selected Index`** · Integer — Index of the most recently accepted wave,  or -1 for a rejected selection.
===

## Continue learning

[Shuffle-Bag Wave Player](shuffle-bag-wave-player.md) is a better choice when repeated picks should be distributed across all supplied variations. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
