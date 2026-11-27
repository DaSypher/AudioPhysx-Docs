# AP: Distance Switch (Dynamic)

**MetaSound · AudioPhysx / Qol**

Route one trigger into an appropriate distance range, without building a large nested Switch graph.

## What actually happens

This is a control-flow utility for a distance-based sound design. It evaluates the supplied `Distance (cm)` against expandable ranges and routes an incoming `Play` event to the selected output branch.

Unlike Distance Wave Player, this node does **not** select and decode a recording. It leaves audio playback to whichever nodes you connect to its dynamic outputs.

## Hear it in a game

Connect three range outputs to separate close, medium and far Wave Players. Move the listener across the authored thresholds and trigger `Play`. Only the appropriate branch should fire for the current distance.

## Build a working graph

>>> 1. Create the distance bands
Add the node and expand the desired distance bands.
>>>

>>> 2. Supply a distance value
Provide an ascending set of `Start Distance (cm)` values and a `Distance (cm)` input.
>>>

>>> 3. Route each output to playback
Connect each branch’s trigger to the corresponding sound or logic chain; use `Max Distance (cm)` and per-band `Volume` where appropriate.
>>>

## The controls that matter

`Distance (cm)` is the tested value. `Start Distance (cm)` specifies each band boundary and `Max Distance (cm)` the outer selection extent. `Volume` gives the associated branch a control value; confirm downstream nodes actually use it.

## What the node outputs

- **`Play`** · Trigger — Triggers when this range is selected.
- **`Gain`** · Float — Volume multiplier for the selected branch.
- **`Out of Range`** · Trigger — Triggered when distance exceeds Max Distance.
- **`Invalid Ranges`** · Trigger — Triggered when range configuration is invalid.
- **`Selected Index`** · Integer — Selected range index, or -1 if rejected.

## Things to watch for

- Keep the configured range groups consistent with the output connections after editing a graph.
- This is a routing node, not a distance attenuation or atmospheric propagation processor.

==- Full input reference
- **`Play`** · *Trigger* — Evaluate distance and trigger one range.
- **`Distance (cm)`** · *Float* — Source-to-listener distance in centimetres.
- **`Max Distance (cm)`** · *Float* — Maximum distance at which sound can start.
- **`Start Distance (cm)`** · *Float* — Distance at which this range becomes active.
- **`Volume`** · *Float* — Volume multiplier for this range.
===

==- Full output reference
- **`Play`** · Trigger — Triggers when this range is selected.
- **`Gain`** · Float — Volume multiplier for the selected branch.
- **`Out of Range`** · Trigger — Triggered when distance exceeds Max Distance.
- **`Invalid Ranges`** · Trigger — Triggered when range configuration is invalid.
- **`Selected Index`** · Integer — Selected range index, or -1 if rejected.
===

## Continue learning

[Distance Wave Player](../playback/distance-wave-player.md) combines band selection with integrated sound playback. Also see the [Qol overview](../../qol.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
