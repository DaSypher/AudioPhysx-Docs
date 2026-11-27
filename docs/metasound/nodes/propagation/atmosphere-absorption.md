---
label: "AP: Atmosphere Absorption"
icon: file
order: 70
---
# AP: Atmosphere Absorption

**MetaSound · AudioPhysx / Propagation**

Make distant sound lose some of its brightness as it travels through air.

<!-- IMAGE SLOT: docs/static/images/nodes/node-atmosphere-absorption.png -->

## What actually happens

Air tends to reduce high-frequency content over distance, and the amount depends on conditions such as temperature, humidity and pressure. This node applies an approximate distance-and-atmosphere-dependent spectral loss to the mono signal.

Unlike standard distance attenuation, the goal is not just to reduce overall volume but to change the tonal balance. A distant sharp recording can become less brittle and more subdued.

## Hear it in a game

Play a short crisp impact while increasing `Distance (cm)` from near to far. Then change humidity and temperature to hear how the approximate frequency response changes. Compare against a reference recording rather than relying only on extreme parameter settings.

## Build a working graph

>>> 1. Feed mono audio
Route mono audio into `Audio`.
>>>

>>> 2. Provide atmospheric conditions
Provide `Distance (cm)`; use the project’s current environmental values when available.
>>>

>>> 3. Compare near and far tone
Tune the result while comparing direct sound against already-enabled Unreal air absorption.
>>>

## The controls that matter

`Temperature (C)` is degrees Celsius, `Humidity (%)` is relative humidity, and `Pressure (kPa)` is kilopascals. `Distance (cm)` is in Unreal centimetres and drives how much the atmospheric model affects the sound.

## What the node outputs

- **`Audio`** · Audio (mono) — Audio after atmospheric absorption.

## Things to watch for

- This is an approximate game-audio model, not a laboratory-calibrated propagation solver.
- If Unreal attenuation settings already perform air absorption, the two effects may make the source unnecessarily dark.

==- Full input reference
- **`Audio`** · *Audio (mono)* — Mono input audio.
- **`Distance (cm)`** · *Float* — Distance travelled by sound in centimetres.
- **`Temperature (C)`** · *Float* — Air temperature in degrees Celsius; default 20.
- **`Humidity (%)`** · *Float* — Relative humidity from 0 to 100; default 50.
- **`Pressure (kPa)`** · *Float* — Atmospheric pressure in kilopascals; default 101.325.
===

==- Full output reference
- **`Audio`** · Audio (mono) — Audio after atmospheric absorption.
===

## Continue learning

[Material Transmission](../acoustics/material-transmission.md) changes spectral content because of barriers instead of air. Also see the [Propagation overview](../../propagation.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
