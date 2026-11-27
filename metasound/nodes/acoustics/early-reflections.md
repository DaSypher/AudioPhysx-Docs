# AP: Early Reflections

**MetaSound · AudioPhysx / Acoustics**

Add a handful of short delayed copies that suggest nearby surfaces without simulating a complete room impulse response.

## What actually happens

Early reflections are the first distinct sound returns from nearby surfaces: what you hear just after a clap in a small room. This node creates an approximate reflection pattern from a room-size control and the speed of sound, mixing it with the direct input.

It is a deliberate lightweight acoustic model. It helps make a dry recording feel placed in a space, but it does not trace walls or replace a full reverb for long late tails.

## Hear it in a game

Play a hand clap or short gunshot through the node. Increase `Wet Level` slowly and vary `Room Size (m)`. Listen for the change from close, tight taps to a broader room impression without turning the signal into a long reverb wash.

## Build a working graph

>>> 1. Add audio input
Connect an existing mono sound to `Audio In`.
>>>

>>> 2. Choose a room response
Provide `Room Size (m)`, `Dry Level`, `Wet Level`, and `HF Damping` suitable for your test space.
>>>

>>> 3. Preserve the audible tail
Connect upstream completion to `Source Finished` and route this node’s `On Finished` onward so reflection tails are not cut off.
>>>

## The controls that matter

`Dry Level` controls the unchanged direct recording and `Wet Level` controls the generated reflection contribution. `HF Damping` reduces higher-frequency energy in the reflections. `Speed of Sound (m/s)` influences the modeled travel timing.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Original sound plus early reflections.
- **`On Finished`** · Trigger — Fires after the last reflection tail.

!!!tip About finishing sounds
A trigger that indicates a source has finished is not always the end of **everything audible**. If you add propagation, early reflections or another tail-generating processor downstream, route completion through that final processor before ending your MetaSound Source.
!!!

## Things to watch for

- Two separate early-reflection or reverb systems can create an over-wet result; compare with Unreal’s room-effect setup.
- Room Size is a useful design control, not a claim that the node has reconstructed the real map geometry.

==- Full input reference
- **`Audio In`** · *Audio (mono)* — Mono signal to reflect.
- **`Source Finished`** · *Trigger* — Connect the Wave Player's On Finished output.
- **`Room Size (m)`** · *Float* — Controls four synthetic extra reflection  path lengths. Does not trace geometry.
- **`Speed of Sound (m/s)`** · *Float* — Propagation speed for reflection delays.
- **`Dry Level`** · *Float* — Level of the original sound.
- **`Wet Level`** · *Float* — Level of the reflection taps.
- **`HF Damping`** · *Float* — Higher values remove more high frequencies  from reflections.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Original sound plus early reflections.
- **`On Finished`** · Trigger — Fires after the last reflection tail.
===

## Continue learning

[Acoustic Paths](acoustic-paths.md) is intended for world-derived path loss and propagation delay, rather than local room taps. Also see the [Acoustics overview](../../acoustics.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
