# AP: Acoustic Paths

**MetaSound · AudioPhysx / Acoustics**

Apply the acoustic path chosen by the game-world solver, including travel delay and low/mid/high frequency loss.

## What actually happens

The gameplay solver estimates a **selected** acoustic route between source and listener. The result is packed into four floating-point values: `delay milliseconds`, `low-band loss dB`, `mid-band loss dB`, and `high-band loss dB`. This node consumes that array and applies an audible delay and frequency-dependent reduction to the mono input.

The key design choice is that it renders **one chosen route**. It does not create two independent copies for direct and around-corner sound, which helps prevent phasey doubling and uncontrolled extra voices.

## Hear it in a game

Place a sound on the other side of a wall with a doorway nearby. Compare a clear direct path with an obstructed one and an available around-door route. Observe how the delay and band losses change in the route data, then listen for the difference.

## Build a working graph

>>> 1. Connect the original recording
Feed your existing mono playback into `Audio In`.
>>>

>>> 2. Supply the selected route
Provide the four-value `Selected Route` array, preferably from the Acoustic Path Blueprint/world subsystem integration.
>>>

>>> 3. Pass through completion
Connect the Wave Player completion to `Source Finished`, and use this node’s `On Finished` after the propagation tail.
>>>

## The controls that matter

`Smoothing (ms)` reduces abrupt changes in route colour or timing. `Delay Capacity (ms)` allocates the delay buffer when the operator is created: the default is designed for low latency and modest memory use; raising it allows longer delays but increases memory. Changing the pin during playback does not resize the allocated buffer.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Only the selected, delayed and filtered acoustic path.
- **`On Finished`** · Trigger — Triggered after the longest queued acoustic path tail.

!!!tip About finishing sounds
A trigger that indicates a source has finished is not always the end of **everything audible**. If you add propagation, early reflections or another tail-generating processor downstream, route completion through that final processor before ending your MetaSound Source.
!!!

## Things to watch for

- Array order matters: `[delay, low, mid, high]`. A wrongly ordered route can turn attenuation into a misleading filter response.
- If your MetaSound has downstream reverberation or reflections, use the **last audible processor’s** completion output rather than ending the source as soon as the original wave stops.

==- Full input reference
- **`Audio In`** · *Audio (mono)* — Mono input to propagate.
- **`Source Finished`** · *Trigger* — Wave Player On Finished; passed through after the path tails.
- **`Selected Route`** · *Float Array* — Float Array from AP.AcousticRoute.Selected: delay ms, low/mid/high loss dB. Route selection occurs on the game thread.
- **`Smoothing (ms)`** · *Float* — Smooth path loss and delay changes.
- **`Delay Capacity (ms)`** · *Float* — Delay buffer capacity allocated ONCE at graph creation. Default 128 ms; raise to 1500 ms only if long cinematic propagation is required. Changes during playback cannot grow the buffer.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Only the selected, delayed and filtered acoustic path.
- **`On Finished`** · Trigger — Triggered after the longest queued acoustic path tail.
===

## Continue learning

[Acoustic path queries](../../../blueprint/acoustic-paths.md) explains how to obtain and publish the path data. Also see the [Acoustics overview](../../acoustics.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
