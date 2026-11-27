# AP: Distance Wave Player

**MetaSound · AudioPhysx / Playback**

Choose a recording collection based on how far the sound source is from the listener.

## What actually happens

The node groups recordings into **distance ranges**. At playback time, it checks `Distance (cm)` and selects the matching range, then chooses a suitable recording from that range. This is about selecting a *different recording*, not merely making the same file quieter.

Close recordings may contain strong mechanical detail; far recordings can instead emphasize the report and environment. The dynamic range entries let a designer author those perspectives without building a large branching graph.

## Hear it in a game

Prepare a close gunshot, a medium-distance gunshot and a distant report. Put the files into suitable bands; then change `Distance (cm)` before `Play`. Confirm the selected recording changes when the listener crosses each authored threshold.

## Build a working graph

>>> 1. Author the distance bands
Expand and configure your distance ranges in ascending order of `Start Distance (cm)`.
>>>

>>> 2. Supply listener distance
Put a `Waves` array in each band and supply `Distance (cm)` from your existing distance system.
>>>

>>> 3. Audition near and far
Use `Play` to request a sound. Set `Max Distance (cm)` and range `Volume` as needed, then audition the band transitions.
>>>

## The controls that matter

`Start Distance (cm)` marks where an authored band starts; `Max Distance (cm)` sets the overall outer limit. `Waves` contains recordings for that band. `Volume` adjusts band playback level. `Max Voices` controls overlap; `No Immediate Repeat` reduces back-to-back identical choices.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mixed mono audio of all active voices.
- **`On Finished`** · Trigger — Fires when the last playing voice ends naturally.  Stop or rejected Play events do not trigger it.

## Things to watch for

- A recording switching bands is not itself acoustic propagation. If Unreal attenuation is also enabled, test the combined loudness and distance response.
- Use consistent capture/processing of near and far recordings. A volume-only difference may sound less convincing than intended.

==- Full input reference
- **`Play`** · *Trigger* — Select one sample from the current distance range.
- **`Stop`** · *Trigger* — Stop every active voice.
- **`Distance (cm)`** · *Float* — Source-to-listener distance in centimetres.
- **`Max Distance (cm)`** · *Float* — Hard playback cutoff evaluated only on Play.
- **`Max Voices`** · *Integer* — Maximum simultaneous samples (1 to 16).
- **`No Immediate Repeat`** · *Boolean* — Avoid selecting the same sample consecutively  within the selected distance range.
- **`Start Distance (cm)`** · *Float* — Distance at which this range becomes active.
- **`Waves`** · *Wave Asset Array* — Array of samples for this range.
- **`Volume`** · *Float* — Linear gain latched when a sample begins.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mixed mono audio of all active voices.
- **`On Finished`** · Trigger — Fires when the last playing voice ends naturally.  Stop or rejected Play events do not trigger it.
===

## Continue learning

[Distance Switch](../qol/distance-switch.md) routes triggers by band when you want to control external playback nodes instead. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
