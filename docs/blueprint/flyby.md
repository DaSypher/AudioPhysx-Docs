---
label: Projectile flybys
icon: rocket
order: 95
---
# Projectile flybys from Blueprint

A good near-miss sound is about **where the projectile passed** and **when the listener would hear it**, not simply whether the weapon fired. AudioPhysx lets you submit a straight path segment and evaluate the closest approach without setting up Chaos physics or spawning special audio-specific bullet Actors.

The integration has two parts: a game-side helper decides whether and when a close pass is audible; [AP: Flyby Wave Player](../metasound/nodes/playback/flyby-wave-player.md) renders the whizz and optional crack from your supplied recordings.

## Understand the path calculation

Imagine a bullet travelling along a line that passes beside the listener. The nearest point on that line is its **closest approach**. If that point is inside the configured audible radius, the event may qualify as a flyby. The helper also estimates arrival time and whether the configured speed and geometry permit a shock-wave effect.

`AP: Calculate Flyby` returns an `FAPFlybyResult` containing `bAudible`, `bShockWave`, `ClosestPoint`, `DistanceMeters`, `SpeedMetersPerSecond`, `Intensity` and `ArrivalSeconds`. This function is useful for debugging the geometry before requesting playback.

`AP: Play Projectile Flyby` performs the test and submits an accepted sound for scheduling. Its Boolean return means **accepted for scheduling**, not that the player has already heard the clip.

## Build the MetaSound once

>>> 1. Create a mono Source
Make a MetaSound Source that will be used only for flyby playback. Add `AP: Flyby Wave Player` from the Playback category.

>>> 2. Supply your recordings
Fill `Whizz Waves` with your licensed near-miss variations. Fill `Crack Waves` if you want a separate supersonic shock layer. Short, clearly edited samples make debugging easier.

>>> 3. Wire playback
Connect the Source's `On Play` to the Flyby player's `Play`, its `Out Mono` to the Source output, and route completion appropriately.

>>> 4. Create five exposed Float inputs
Use the **exact names** below. Connect them to the corresponding Flyby Wave Player controls; they are set by the world subsystem before the sound starts.

>>> 5. Audition and save
Test the MetaSound manually with reasonable values first. Then use it as the asset supplied to the Blueprint helper.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/graph-flyby-metasound.png -->

### The five runtime inputs

- **`AP.Flyby.DistanceM`** → `Distance (m)`. Closest distance from the projectile path to the listener, **in metres**.
- **`AP.Flyby.SpeedMps`** → `Speed (m/s)`. Projectile speed, in metres per second.
- **`AP.Flyby.Intensity`** → `Intensity`. The computed strength control.
- **`AP.Flyby.SpeedOfSoundMps`** → `Speed of Sound (m/s)`. Acoustic model speed in metres per second.
- **`AP.Flyby.Shock`** → `Shock`. A Float gate, typically 1 for requested crack and 0 otherwise.

The parameter names above come from the reviewed `APFlybyWorldSubsystem.cpp` development source. Keep them identical in the MetaSound graph.

## Send a hitscan shot

>>> 1. Build the shot path
Use the weapon muzzle world location for `PathStart` and the trace hit point (or maximum trace end) for `PathEnd`.

>>> 2. Set projectile speed
Provide `ProjectileSpeedMps` in **metres per second**, even though Unreal's path vectors are world units in centimetres.

>>> 3. Supply the sound asset
Pass your flyby MetaSound Source as `FlybyMetaSound` and choose an `AudibleRadiusM` appropriate to your test.

>>> 4. Request one evaluation
Call `AP: Play Projectile Flyby` **once per hitscan shot**. `PathAgeSeconds` is zero for a fresh, instantaneous hitscan query.

>>> 5. Test a passing and a missing shot
Shoot beside the listener, then farther away than the radius. Watch the Boolean acceptance result and listen for the corresponding audio behaviour.
>>>

<!-- IMAGE SLOT: docs/static/images/blueprint/bp-flyby-hitscan.png -->

## Moving projectile segments

For a projectile that has already moved, send consecutive start/end positions rather than predicting its whole future path. The optional `ProjectileInstance` should uniquely identify **that specific projectile** so the system can suppress duplicate near-miss events. A shared weapon object is not a suitable substitute when it fires multiple independent bullets.

`PathAgeSeconds` describes how old the reported movement segment is. The source comments recommend using segment length divided by projectile speed for a segment submitted after motion, so that scheduling can account for already elapsed travel time.

!!!warning What is approximate?
This first version assumes a simplified constant-speed path and approximate acoustic arrival. It positions playback near the closest approach; it does not perform a continuous 3D flyby simulation or exact shock-front tracing. Test very close passes, fast shots and different listener positions in your game before treating timings as final.
!!!

[Try the short flyby recipe](../examples/projectile-flyby.md) · [Flyby Wave Player reference](../metasound/nodes/playback/flyby-wave-player.md)
