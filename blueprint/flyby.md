# Projectile flybys from a path segment

A useful projectile near-miss sound should represent a projectile that actually passed near the listener, not every time any weapon fired. AudioPhysx's flyby helper accepts the start and end of a projectile path segment, its speed, and an audible radius. It can calculate the point of closest approach and an approximate arrival time. The audio renderer then uses that result to play a whizz and, where appropriate, a shock-like crack.

The public Blueprint API exposes `AP: Calculate Flyby`, which returns an `FAPFlybyResult` with values such as `bAudible`, `bShockWave`, `ClosestPoint`, `DistanceMeters`, `SpeedMetersPerSecond`, `Intensity` and `ArrivalSeconds`. This is valuable for debugging because it lets you inspect the geometry and acoustic decision **without immediately scheduling audio**. `AP: Play Projectile Flyby` combines the calculation with world-level scheduling; a `true` return means the request was accepted for scheduling, not that the listener has already heard the resulting sound.

## Connect the stereo MetaSound

Create a stereo MetaSound Source and add [AP: Flyby Wave Player](../metasound/playback-nodes/flyby-wave-player.md). Supply one or more `Whizz Waves` and optionally `Crack Waves`. Connect `Out Left` and `Out Right` to the Source's corresponding stereo outputs. Expose the following **Float** inputs with precisely these names, as used by the current flyby world subsystem:

- `AP.Flyby.DistanceM` → `Distance (m)`
- `AP.Flyby.SpeedMps` → `Speed (m/s)`
- `AP.Flyby.Intensity` → `Intensity`
- `AP.Flyby.SpeedOfSoundMps` → `Speed of Sound (m/s)`
- `AP.Flyby.Shock` → `Shock`

These are parameter-name contracts, not arbitrary labels. A name that looks nearly identical but differs in punctuation or capitalization should not be assumed to update the intended MetaSound input. The subsystem sets these controls before starting the sound.

## Send a path from gameplay

For a hitscan weapon, use the muzzle or trace start as `PathStart`, and the hit location or maximum trace end as `PathEnd`. Pass the final MetaSound Source as `FlybyMetaSound`. Provide projectile speed in **metres per second** and the audible radius in **metres**. A newly submitted hitscan event normally has a path age of zero.

For moving projectiles, provide successive path segments from the projectile's actual movement. `ProjectileInstance` should represent one distinct projectile, not the weapon that fires many rounds, because the world subsystem may use it to suppress duplicate near misses. `PathAgeSeconds` describes when the submitted segment occurred relative to the query; incorrect values may change the apparent arrival timing.

Start with an obviously close path and print the calculation result. Next submit a path outside the audible radius, then compare slower and faster projectiles. Only after the geometry makes sense should you tune the recordings and their stereo output. A close flyby may still be appropriate as a mono spatialized source in some projects; Stereo to Mono provides that option downstream.

The current acoustic model is deliberately approximate: it assumes simplified path and speed behaviour rather than a full shock-front or trajectory simulation. Measure the finished result by listening in your own game and check for duplicates, unrealistic near-miss thresholds and excessively loud cracks.
