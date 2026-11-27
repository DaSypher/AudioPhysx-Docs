# Projectile flyby integration

You can trigger a close-pass flyby using **a path segment**, without using Chaos or spawning special AudioPhysx projectile actors.

## Available functions

| Blueprint function | What it returns / does |
| --- | --- |
| `AP: Calculate Flyby` | Returns an `FAPFlybyResult` with `bAudible`, `bShockWave`, closest point, distance, speed, intensity and estimated arrival time. |
| `AP: Play Projectile Flyby` | Evaluates the near-miss and submits a sound for world-level scheduling when accepted. Its Boolean return means scheduling accepted, **not** that the sound has already played. |

## Create the MetaSound

1. Create a mono MetaSound Source and add [AP: Flyby Wave Player](../metasound/nodes/playback/flyby-wave-player.md).
2. Fill `Whizz Waves` and optionally `Crack Waves` with licensed recordings.
3. Wire its `Out Mono` into the MetaSound output and its completion as appropriate.
4. Expose the flyby parameter inputs expected by the Blueprint integration. Their names must match the source contract; see the parameter table below.

## Call it from a hitscan weapon

Call `AP: Play Projectile Flyby` **once per shot**, with `Path Start` at the muzzle and `Path End` at your trace end or impact location. Use a projectile speed in **metres per second** and set `Path Age Seconds` to zero for a new hitscan event.

| Parameter | Unit / meaning |
| --- | --- |
| `WorldContextObject` | World context for playback and scheduling. |
| `FlybyMetaSound` | MetaSound Source created above, typed as `USoundBase`. |
| `PathStart`, `PathEnd` | Unreal world locations in centimetres. |
| `ProjectileSpeedMps` | Projectile speed, metres per second. |
| `AudibleRadiusM` | Maximum closest-pass distance, metres. |
| `Volume` | Playback volume scaling. |
| `PathAgeSeconds` | Age of the submitted path segment in seconds. |
| `ProjectileInstance` | Optional unique object representing one projectile for duplicate suppression. |

## For moving projectiles

Submit consecutive path segments instead of the whole future path. If you provide `ProjectileInstance`, it should uniquely identify **one projectile**, not the weapon producing many projectiles. For a segment submitted after movement, the source comment recommends using segment length divided by projectile speed for `PathAgeSeconds`.

!!!warning Acoustic approximation
The initial flyby system uses simplified constant-speed near-miss/acoustic timing. Do not advertise it as an exact ballistic shock-wave solver. Test listener motion and very fast or very long paths in the final game.
!!!

## Exact MetaSound parameter names

The current world subsystem supplies the following **Float** parameters *before* starting the flyby MetaSound. Create graph inputs with these exact names and connect them to the corresponding Flyby Wave Player controls:

| External MetaSound Float input | Connect to |
| --- | --- |
| `AP.Flyby.DistanceM` | `Distance (m)` |
| `AP.Flyby.SpeedMps` | `Speed (m/s)` |
| `AP.Flyby.Intensity` | `Intensity` |
| `AP.Flyby.SpeedOfSoundMps` | `Speed of Sound (m/s)` |
| `AP.Flyby.Shock` | `Shock` (1 or 0) |

These names are taken from `APFlybyWorldSubsystem.cpp` in the reviewed source. Confirm they remain unchanged in the final release.

See [Flyby Wave Player](../metasound/nodes/playback/flyby-wave-player.md) and [Troubleshooting](../support/troubleshooting.md).
