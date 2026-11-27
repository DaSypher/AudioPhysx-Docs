# AP: Sequence Wave Player

**MetaSound · AudioPhysx / Playback**

Build a fixed sequence of recordings without timing it by hand. Each playable wave starts after the one before it finishes.

## What actually happens

This player walks through an expandable list of **Wave Asset** slots in their order. Only one recording is active at a time. When playback of the current slot completes, the next valid slot becomes the source of audio. Empty or invalid slots are skipped instead of creating an artificial pause.

The timing is determined by the chosen recordings, **not** an adjustable delay. This makes it suitable for actions with a definite order: a key turning, a latch moving, and then a mechanism closing.

## Hear it in a game

Try three contrasting recordings: a short click, a longer motor movement, and a final clunk. Trigger `Play` once and listen to the full action. Change the length of the motor file: the clunk should follow the *new* ending automatically.

## Build a working graph

>>> 1. Place the sounds in order
Create a **mono MetaSound Source** and add **AP: Sequence Wave Player** from Playback.
>>>

>>> 2. Connect Play and audio
Expand `Sequence Waves` to the required number of `Wave` slots. Assign the recordings in the order they should be heard.
>>>

>>> 3. Check the finishing event
Connect your starting trigger to `Play`, and route `Out Mono` to the Source audio output. Use `On Finished` to end the Source only if nothing downstream needs to ring out.
>>>

## The controls that matter

`Loop Sequence` repeats the list after the last valid recording. `Stop` cancels the active sequence rather than playing an outro. A new `Play` restarts from the beginning; it does not resume the previous position.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mono audio output from the currently playing wave.
- **`On Finished`** · Trigger — Fires once after the last wave finishes naturally (when not looping).

## Things to watch for

- Do not use this node to create a rapid-fire overlap: each recording must finish before the next begins. For independent overlapping shots, use the RPM mode on Start Loop End.
- A player may finish at an audio-block boundary; check completion in both preview and packaged gameplay when other processors contribute tails.

==- Full input reference
- **`Play`** · *Trigger* — Play the wave sequence from the beginning. Retriggering restarts it.
- **`Stop`** · *Trigger* — Stop playback immediately, without firing On Finished.
- **`Loop Sequence`** · *Boolean* — Restart from the first valid wave after the last finishes.
- **`Wave`** · *Wave Asset* — Wave Asset to play in sequence. Add or remove Wave slots on the node.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mono audio output from the currently playing wave.
- **`On Finished`** · Trigger — Fires once after the last wave finishes naturally (when not looping).
===

## Continue learning

[Random Sequence](random-sequence-wave-player.md) replaces each fixed slot with a random choice from an array. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
