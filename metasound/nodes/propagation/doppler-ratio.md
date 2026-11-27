# AP: Doppler Ratio

**MetaSound · AudioPhysx / Propagation**

Calculate a playback pitch multiplier from the motion of the source and listener toward one another.

## What actually happens

Doppler shift is the change in perceived pitch caused by relative motion. This node operates on **radial velocity**—the component of motion directly toward or away from the other participant—not the total speed of either object.

It outputs a pitch ratio for use elsewhere in the graph. It does not decode or pitch-shift a Wave Asset by itself.

## Hear it in a game

Drive a vehicle past a stationary listener and compare approaching and receding motion. Feed the directional velocity components into the node, then apply its output to a compatible pitch control downstream. Keep the effect moderate for believable engine audio.

## Build a working graph

>>> 1. Feed radial source velocity
Supply source velocity **toward** the listener to `Source Toward Listener (m/s)`.
>>>

>>> 2. Feed listener velocity and sound speed
Supply listener velocity **toward** the source to `Listener Toward Source (m/s)` and provide the speed of sound.
>>>

>>> 3. Use the resulting ratio
Connect the output ratio to the playback/pitch system you actually use.
>>>

## The controls that matter

A positive radial velocity here means movement **toward** the other point, according to the pin labels. `Speed of Sound (m/s)` affects the magnitude of the ratio. This node expects metres per second rather than Unreal centimetres per second.

## What the node outputs

- **`Pitch Ratio`** · Float — Pitch multiplier for playback WITHOUT Dynamic Propagation.

## Things to watch for

- Passing an unsigned speed (always positive) erases the distinction between approach and departure.
- Avoid stacking this full-strength ratio with Dynamic Propagation or Unreal’s own Doppler unless you intentionally want an exaggerated effect.

==- Full input reference
- **`Source Toward Listener (m/s)`** · *Float* — Positive means source approaches listener.
- **`Listener Toward Source (m/s)`** · *Float* — Positive means listener approaches source.
- **`Speed of Sound (m/s)`** · *Float* — Default 343 m/s.
===

==- Full output reference
- **`Pitch Ratio`** · Float — Pitch multiplier for playback WITHOUT Dynamic Propagation.
===

## Continue learning

[Dynamic Propagation](dynamic-propagation.md) works directly on mono audio rather than merely supplying a ratio. Also see the [Propagation overview](../../propagation.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
