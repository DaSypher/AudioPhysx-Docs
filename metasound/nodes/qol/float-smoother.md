# AP: Float Smoother

**MetaSound · AudioPhysx / Qol**

Prevent sudden gameplay value changes from producing audible jumps in volume, filtering or other controls.

## What actually happens

A MetaSound Float input may change in discrete blocks even when the game value is continuous. Feeding those updates directly into a filter or mix control can create stepping. Float Smoother gradually approaches a target using separate rise and fall responses.

It operates at **control/block rate**, so think of it as a parameter-conditioning tool, not an audio-waveform filter.

## Hear it in a game

Connect a changing engine-load value to `Target`. Give increasing values a short `Rise (ms)` and decreasing values a longer `Fall (ms)` so the motor reacts quickly to throttle but relaxes more slowly.

## Build a working graph

>>> 1. Connect the target value
Connect the changing Float to `Target`.
>>>

>>> 2. Set rise and fall response
Set independent `Rise (ms)` and `Fall (ms)` values. Start with modest values and judge them by ear.
>>>

>>> 3. Route the smoothed control
Use `Smoothed` wherever a downstream node expects the stabilized control. Use `Snap` when a level or state change should happen immediately.
>>>

## The controls that matter

`Rise (ms)` and `Fall (ms)` are smoothing time constants rather than fixed delays. Zero snaps immediately in the corresponding direction. `Snap` overrides the gradual transition for the current target.

## What the node outputs

- **`Smoothed`** · Float — Rise/fall smoothed Float control signal (block-rate).

## Things to watch for

- A very long rise or fall time can make responsive effects feel disconnected from gameplay.
- Because the output is block-rate, it should not be mistaken for sample-by-sample modulation of an audio buffer.

==- Full input reference
- **`Target`** · *Float* — Float value to smooth. Sampled once per audio block.
- **`Rise (ms)`** · *Float* — Exponential time constant for increasing values. Zero snaps immediately.
- **`Fall (ms)`** · *Float* — Exponential time constant for decreasing values. Zero snaps immediately.
- **`Snap`** · *Trigger* — Immediately set the output to Target in this block (block-rate behaviour).
===

==- Full output reference
- **`Smoothed`** · Float — Rise/fall smoothed Float control signal (block-rate).
===

## Continue learning

[Trigger Cooldown](trigger-cooldown.md) controls event frequency rather than the smoothness of numeric values. Also see the [Qol overview](../../qol.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
