# AP: Random Sequence Wave Player

**MetaSound · AudioPhysx / Playback**

Keep the stages of an action in order, but randomly vary the recording played at each stage.

## What actually happens

Each expandable **Sequence Steps** input is a **Wave Asset Array**, not a single file. On reaching a step, the player chooses one valid member of that array and plays it to completion. It then moves on to the next step and selects again there.

The step order stays predictable, but the details change each time: a lock might always click, turn, and release, without sounding like the exact same three recordings on every use. Previous selections are tracked per step to reduce immediate repetition when alternatives are available.

## Hear it in a game

Create three arrays: `Open` clicks, `Mechanism` rotations, and `Close` clunks. Put at least two variations in each. The three stages should always happen in the same order, but the chosen recordings should change over repeated plays.

## Build a working graph

>>> 1. Add the sequence stages
Add the node to a mono MetaSound Source and expand `Sequence Steps` to the number of stages.
>>>

>>> 2. Fill each stage with variations
For each `Waves` slot, create an array containing recordings for *that stage only*. Do not mix opening and closing recordings in the same array.
>>>

>>> 3. Connect and test the complete action
Connect `Play`, `Out Mono`, and optionally `On Finished`. Enable `Loop Sequence` only if the entire multi-stage action should repeat.
>>>

## The controls that matter

`Loop Sequence` starts again at step one after the last valid step. `Stop` cancels the current pass. The contents of the arrays determine the durations; there is no manual per-step delay or global RPM.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Audio from the current step.
- **`On Finished`** · Trigger — Fires after all playable steps finish.

## Things to watch for

- A step with no valid assets is skipped, which can make the audible sequence shorter than the number of configured steps.
- Random selection is not the same as shuffle-bag exhaustion. Use Shuffle-Bag when you want to hear every variation before a cycle repeats.

==- Full input reference
- **`Play`** · *Trigger* — Start the sequence. Play again to restart.
- **`Stop`** · *Trigger* — Stop immediately without On Finished.
- **`Loop Sequence`** · *Boolean* — Restart after the final recording.
- **`Waves`** · *Wave Asset Array* — A Wave Asset Array for this expandable step.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Audio from the current step.
- **`On Finished`** · Trigger — Fires after all playable steps finish.
===

## Continue learning

[Sequence Wave Player](sequence-wave-player.md) is the simpler fixed-recording alternative. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
