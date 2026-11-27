# AP: Dynamic Propagation

**MetaSound · AudioPhysx / Propagation**

Apply a continuously changing travel-time delay to moving-source audio, with safeguards against abrupt jumps.

## What actually happens

A moving source changes the length of the sound path while audio is playing. This node reacts to updated `Distance (cm)` values, changing the effective propagation delay rather than relatching a single fixed arrival time.

Because changing delay can create audible pitch shifts or clicks, the node provides smoothing, a limit on Doppler-like changes, and special handling for large position jumps. It is a controlled approximation designed for responsive game audio.

## Hear it in a game

Attach a continuous engine sound to a fast vehicle and feed its listener distance into the graph. Compare a smooth approach and departure with a sudden teleport. Tune smoothing and jump crossfade so ordinary motion is audible but teleports do not create unpleasant artifacts.

## Build a working graph

>>> 1. Connect a moving sound
Feed the mono engine or movement recording into `Audio`.
>>>

>>> 2. Supply changing distance
Update `Distance (cm)` from your source/listener positions and choose `Max Delay (s)` large enough to contain the desired range.
>>>

>>> 3. Tune smoothing and jump handling
Adjust `Smoothing (ms)`, `Max Doppler (%)`, `Jump Threshold (cm)` and `Jump Crossfade (ms)` while auditioning movement.
>>>

## The controls that matter

`Smoothing (ms)` controls how quickly changes are applied. `Max Doppler (%)` limits the pitch/delay-rate effect. `Jump Threshold (cm)` identifies unusually large position changes, while `Jump Crossfade (ms)` smooths those transitions. `Speed of Sound (m/s)` controls the travel-time conversion.

## What the node outputs

- **`Audio`** · Audio (mono) — Mono audio after travel-time delay.
- **`Doppler Ratio`** · Float — Diagnostic pitch ratio. Do not apply again.

## Things to watch for

- Do not apply full-strength Unreal Doppler modulation on top of this effect without evaluating the combination.
- Large delay capacities and many active sources increase memory use. Test against the expected number of emitters.

==- Full input reference
- **`Audio`** · *Audio (mono)* — Mono signal to propagate.
- **`Distance (cm)`** · *Float* — Source-listener distance in centimetres.
- **`Speed of Sound (m/s)`** · *Float* — Sound speed in metres per second; default 343.
- **`Max Delay (s)`** · *Float* — Maximum travel time, fixed at voice creation.
- **`Smoothing (ms)`** · *Float* — Smooths small distance changes; default 25 ms.
- **`Max Doppler (%)`** · *Float* — Maximum pitch deviation; default 20 percent.
- **`Jump Threshold (cm)`** · *Float* — Large distance changes crossfade instead of scrubbing.
- **`Jump Crossfade (ms)`** · *Float* — Crossfade duration; default 40 ms.
===

==- Full output reference
- **`Audio`** · Audio (mono) — Mono audio after travel-time delay.
- **`Doppler Ratio`** · Float — Diagnostic pitch ratio. Do not apply again.
===

## Continue learning

[Distance Delay](distance-delay.md) is simpler when an event should use a fixed captured delay. Also see the [Propagation overview](../../propagation.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
