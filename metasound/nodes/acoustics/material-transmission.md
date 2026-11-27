# AP: Material Transmission

**MetaSound · AudioPhysx / Acoustics**

Colour and attenuate sound when a source is behind a material or barrier.

## What actually happens

An obstructing material often reduces high frequencies more than lows. Rather than muting a source, this node uses authored low-band and high-band attenuation, a crossover and thickness-related controls to shape the sound that passes through a barrier.

The node needs an external `Obstructed` state and material information. It does not perform collision traces itself; it makes a mono signal respond to data supplied by your game.

## Hear it in a game

Take a voice or a door slam. Toggle `Obstructed` while adjusting `Low Loss (dB)` and `High Loss (dB)`. A barrier with much greater high-frequency loss should sound duller and more distant than an open path.

## Build a working graph

>>> 1. Connect the dry source
Insert the node after a mono playback source.
>>>

>>> 2. Supply obstruction and losses
Feed a Boolean into `Obstructed`, and start with authored band losses that create a clear contrast.
>>>

>>> 3. Tune material coloration
Adjust thickness, crossover, leakage and smoothing only after the unblocked/blocked transition behaves as expected.
>>>

## The controls that matter

`Thickness (cm)` and `Reference Thickness (cm)` provide a thickness context for the model. `Low Loss (dB)` and `High Loss (dB)` set the band attenuation in decibels. `Crossover (Hz)` determines where the low/high shaping transitions. `Leakage (%)` allows some unfiltered content to bleed through; `Smoothing (ms)` prevents hard switching.

## What the node outputs

- **`Out Mono`** · Audio (mono) — Mono audio after transmission filtering.

## Things to watch for

- Avoid double-obstructing the same sound. If an Acoustic Paths node already applies path losses, choose a deliberate combination rather than summing two full-strength filters.
- This is approximate transmission coloration, not a substitute for measured transmission-loss data for a particular wall.

==- Full input reference
- **`Audio`** · *Audio (mono)* — Mono source audio.
- **`Obstructed`** · *Boolean* — True when the sound path is obstructed.
- **`Thickness (cm)`** · *Float* — Assigned obstacle thickness in centimetres.
- **`Reference Thickness (cm)`** · *Float* — Thickness at which the specified losses apply.
- **`Low Loss (dB)`** · *Float* — Low-band transmission loss at reference thickness.
- **`High Loss (dB)`** · *Float* — High-band transmission loss at reference thickness.
- **`Crossover (Hz)`** · *Float* — Approximate low/high frequency division.
- **`Leakage (%)`** · *Float* — Fraction of unobstructed audio mixed back in.
- **`Smoothing (ms)`** · *Float* — Smoothing time for changing transmission gains.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mono audio after transmission filtering.
===

## Continue learning

[Acoustic obstruction recipe](../../../examples/acoustic-obstruction.md) offers two different ways to build a blocked-sound demonstration. Also see the [Acoustics overview](../../acoustics.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
