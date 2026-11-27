# AP: Flyby Wave Player

**MetaSound · AudioPhysx / Playback**

Turn a projectile near-miss result into an audible whizz and optional ballistic crack.

## What actually happens

This node is the **audio rendering half** of the flyby system. The gameplay side computes the closest pass, distance, speed and whether a shock effect should be heard. The MetaSound node then picks recordings from `Whizz Waves` and, when requested, `Crack Waves`, shaping the sound with the supplied parameters.

A positive `Shock` signal indicates that the ballistic-crack layer is requested; it is **not** simply a synonym for high speed. The standalone player can be used manually, while `AP: Play Projectile Flyby` can prepare runtime parameters and schedule a near-miss sound automatically.

## Hear it in a game

Give it two whizz variants and two short crack recordings. Compare a close pass with a distant pass, then change `Shock` from 0 to 1. The crack should only be requested for the latter state; the final mix depends on the supplied recordings.

## Build a working graph

>>> 1. Create the flyby Source
Create a mono MetaSound Source, add this player, and connect its `Out Mono` output.
>>>

>>> 2. Supply whizz and crack variations
Assign `Whizz Waves` and optional `Crack Waves`. Wire the control values directly or expose the five named runtime parameters expected by the Blueprint flyby subsystem.
>>>

>>> 3. Connect the world-side parameters
Trigger `Play` in preview, then use the [Blueprint flyby guide](../../../blueprint/flyby.md) to test a real projectile path.
>>>

## The controls that matter

`Distance (m)` is **metres**, unlike Unreal world locations in centimetres. `Speed (m/s)` and `Speed of Sound (m/s)` are in metres per second. `Intensity` is a designer-friendly strength control. `Shock` is the crack-layer gate; it does not replace the game-thread geometry check.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mono whizz and crack mix. Spatialize in the MetaSound Source.
- **`On Finished`** · Trigger — All started variations have finished naturally.
- **`On Rejected`** · Trigger — No playable wave was selected.

## Things to watch for

- Do not feed Unreal centimetres directly into the metres input; a 500 cm pass is 5 m, not 500 m.
- This is a playback and near-miss approximation, not a full moving 3D source or precise shock-front solver. The game-side subsystem is responsible for timing and position.

==- Full input reference
- **`Play`** · *Trigger* — Start one flyby, restarting this player if already active.
- **`Stop`** · *Trigger* — Stop immediately; does not emit On Finished.
- **`Whizz Waves`** · *Wave Asset Array* — Randomly chosen rush/whizz Wave Asset Array.
- **`Crack Waves`** · *Wave Asset Array* — Randomly chosen supersonic crack Wave Asset Array.
- **`Distance (m)`** · *Float* — Closest approach in metres. Optional: for custom graph controls.
- **`Speed (m/s)`** · *Float* — Projectile speed in metres/second.
- **`Intensity`** · *Float* — Normalized near-miss strength, 0 to 1.
- **`Speed of Sound (m/s)`** · *Float* — Local speed of sound; used to validate shock playback.
- **`Shock`** · *Float* — 1 = Mach cone reaches listener (0 = ordinary whizz).
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mono whizz and crack mix. Spatialize in the MetaSound Source.
- **`On Finished`** · Trigger — All started variations have finished naturally.
- **`On Rejected`** · Trigger — No playable wave was selected.
===

## Continue learning

[Projectile Flyby Blueprint integration](../../../blueprint/flyby.md) contains the external parameter names and near-miss workflow. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
