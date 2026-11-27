# AP: Start Loop End Player

**MetaSound · AudioPhysx / Playback**

Play an opening sound, sustain a repeatable middle section, and finish with a proper release when the action ends.

## What actually happens

This node follows three phases: **Start**, **Middle**, and **End**. Each phase chooses a recording from its respective Wave Asset Array. It works for automatic weapons, powered tools, long energy effects, and other actions that start, continue, then stop.

The important distinction is **RPM**. At `RPM = 0`, middle recordings play consecutively when each recording finishes. At a positive RPM, the node schedules fresh middle recordings at a fixed number of starts per minute, so the recordings can overlap. The implementation maintains a bounded pool of twelve middle voices instead of dynamically creating a new audio player for every shot.

## Hear it in a game

For a rifle, put an initial bolt/attack in `Start Waves`, several shot bodies in `Loop Waves`, and mechanical release recordings in `End Waves`. Set `RPM` to 600: a new middle shot is scheduled approximately every 100 milliseconds once the intro finishes. Then send `Stop Firing` and listen to the ending.

## Build a working graph

>>> 1. Choose attack, middle and end sounds
Fill the three arrays. `Start Waves` is optional; if it has no playable recording, playback proceeds to the middle.
>>>

>>> 2. Wire press and release
Connect the weapon pressed signal to `Start Firing` and release signal to `Stop Firing`. Connect `Out Mono` and `On Finished` according to your Source lifecycle.
>>>

>>> 3. Set RPM and release behaviour
Choose `RPM = 0` for completion-driven machinery loops, or a positive RPM for timed overlapping shots. Test both `Immediate Release` settings with your actual recordings.
>>>

## The controls that matter

`Immediate Release = true` fades currently active audio and begins the end recording promptly. When false, the player waits for active shots or intro audio to finish before entering the end phase. `RPM` is a **firing interval**, not a playback speed control: raising it should increase the number of shot starts without shortening individual recordings. The source clamps positive rates to its supported range.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mixed mono audio output.
- **`On Finished`** · Trigger — Fires when ending audio and any remaining shots have finished.

!!!tip About finishing sounds
A trigger that indicates a source has finished is not always the end of **everything audible**. If you add propagation, early reflections or another tail-generating processor downstream, route completion through that final processor before ending your MetaSound Source.
!!!

## Things to watch for

- At high RPM with long recordings, all twelve middle voices can be occupied. The newest scheduled shot is then skipped rather than cutting an existing voice.
- `On Finished` follows the release sequence; it is not expected during a continuously held firing action. Missing middle waves can prevent audible firing even if the state remains active.
- The node is not a ballistic simulation; it controls recording playback. Keep muzzle, mechanical and environmental content appropriately designed.

==- Full input reference
- **`Start Firing`** · *Trigger* — Play a random intro, then begin firing middle waves.
- **`Stop Firing`** · *Trigger* — Stop scheduling shots and enter the ending.
- **`Immediate Release`** · *Boolean* — True: fade active waves and play ending immediately. False: let all active waves finish before ending.
- **`RPM`** · *Float* — 0 = legacy sequential middle waves. 60-2400 = middle shots per minute, with overlap. Updated at shot boundaries.
- **`Start Waves`** · *Wave Asset Array* — Random intro wave array. If empty, start middle sounds immediately.
- **`Loop Waves`** · *Wave Asset Array* — Random middle wave array; RPM sets the interval between starts, not between completions.
- **`End Waves`** · *Wave Asset Array* — Random ending wave array.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mixed mono audio output.
- **`On Finished`** · Trigger — Fires when ending audio and any remaining shots have finished.
===

## Continue learning

[Automatic weapon recipe](../../../examples/automatic-weapon.md) walks through practical recording choices and Stop Firing behaviour. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
