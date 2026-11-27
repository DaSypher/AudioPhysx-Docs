---
label: "AP: Source Directivity"
icon: broadcast
order: 80
---
# AP: Source Directivity

**MetaSound · AudioPhysx / Acoustics**

Make a sound change as you move around the front, side and rear of its emitter.

<!-- IMAGE SLOT: docs/static/images/nodes/node-source-directivity.png -->

## What actually happens

A speaker, exhaust or human voice does not radiate identically in every direction. The node receives an angle between source orientation and the listener and uses it to shape both loudness and spectral content.

It separates broad rear attenuation from lower-frequency directivity. That matters because bass energy tends to remain more omnidirectional than high-frequency detail in many real sources; the node gives you an accessible way to suggest that effect.

## Hear it in a game

Put a radio or machine in a test level and walk around it. Feed the changing listener-relative angle into the MetaSound. Listen for the brightness and loudness changing between the front and the back without a sudden on/off switch.

## Build a working graph

>>> 1. Connect audio
Connect the mono recording to `Audio`.
>>>

>>> 2. Provide source-listener orientation
Supply `Angle (deg)` from the game or acoustic parameter system, making sure the angle convention matches the source orientation.
>>>

>>> 3. Tune front and rear tone
Adjust `Directivity (%)` and `Rear Attenuation (dB)`, then add low-frequency shaping and smoothing.
>>>

## The controls that matter

`Directivity (%)` is the overall directional strength. `Rear Attenuation (dB)` is the rear-facing loss. `Low Frequency Directivity (%)` lets bass react less aggressively. `Crossover (Hz)` defines the spectral transition and `Smoothing (ms)` prevents angular movement from sounding stepped.

## What the node outputs

- **`Out Mono`** · Audio (mono) — Mono audio after directional filtering.

## Things to watch for

- If Unreal spatialization or a separate directivity attenuation model is already active, check the combined result rather than applying both at full strength.
- The node expects orientation data; it cannot derive a source facing direction from a mono audio buffer.

==- Full input reference
- **`Audio`** · *Audio (mono)* — Mono input audio.
- **`Angle (deg)`** · *Float* — Angle from the source forward direction  to the listener. 0 is front, 180 is rear.
- **`Directivity (%)`** · *Float* — Directivity strength, 0 to 100 percent.
- **`Rear Attenuation (dB)`** · *Float* — Maximum high-frequency attenuation at 180 degrees.
- **`Low Frequency Directivity (%)`** · *Float* — Fraction of high-frequency attenuation  applied to the lower frequencies.
- **`Crossover (Hz)`** · *Float* — Approximate low/high frequency division.
- **`Smoothing (ms)`** · *Float* — Smooth changes in directional attenuation.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mono audio after directional filtering.
===

## Continue learning

[Doppler Ratio](../propagation/doppler-ratio.md) addresses radial motion rather than facing direction. Also see the [Acoustics overview](../../acoustics.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
