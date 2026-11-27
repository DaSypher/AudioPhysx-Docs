# AP: Distance Delay

**MetaSound · AudioPhysx / Propagation**

Delay a mono signal to imitate the time it takes sound to travel across a fixed source-to-listener distance.

## What actually happens

Sound does not arrive instantly in the real world. This node approximates travel time as **distance divided by speed of sound**, then delays the incoming audio by that amount, subject to the available buffer capacity.

The distinctive control is `Relatch`: instead of necessarily treating every small movement as a continuous Doppler effect, the delay can be captured deliberately for a discrete event such as an explosion.

## Hear it in a game

Take an explosion recording at a fixed distance and compare an immediate playback with a latched delayed version. At ordinary air sound speeds, a distant explosion should arrive later even when the visual event has already occurred.

## Build a working graph

>>> 1. Connect the mono sound
Feed a mono audio signal into `Audio`.
>>>

>>> 2. Provide distance and sound speed
Set `Distance (cm)` and `Speed of Sound (m/s)` with consistent units.
>>>

>>> 3. Latch the intended travel time
Ensure `Max Delay (s)` is large enough for the intended distance, then use `Relatch` when the playback event needs the current delay captured.
>>>

## The controls that matter

`Distance (cm)` is the source-listener separation in Unreal centimetres. `Speed of Sound (m/s)` is in metres per second. `Max Delay (s)` caps how much memory the delay buffer reserves. `Relatch` requests a new captured delay value.

## What the node outputs

- **`Audio`** · Audio (mono) — Delayed mono audio.

## Things to watch for

- A travel-time delay and a manually delayed sound can add together. Avoid applying both unless that is intentional.
- A large maximum delay reserves more audio memory; choose the smallest capacity that covers your intended scenario.

==- Full input reference
- **`Audio`** · *Audio (mono)* — Mono audio input.
- **`Distance (cm)`** · *Float* — Distance travelled by sound in Unreal centimetres. Sampled only when latched.
- **`Speed of Sound (m/s)`** · *Float* — Propagation speed in metres per second.  Default 343 m/s. Converted internally to cm/s.  Sampled only when latched.
- **`Max Delay (s)`** · *Float* — Maximum delay capacity in seconds (0.01-10). Allocated when the operator is constructed.
- **`Relatch`** · *Trigger* — Recalculate propagation delay and discard the previous pending audio tail.
===

==- Full output reference
- **`Audio`** · Audio (mono) — Delayed mono audio.
===

## Continue learning

[Dynamic Propagation](dynamic-propagation.md) handles continuously changing distance and moving-source effects. Also see the [Propagation overview](../../propagation.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
