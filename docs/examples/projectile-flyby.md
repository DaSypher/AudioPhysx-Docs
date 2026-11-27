---
label: Projectile near miss
icon: play
order: 85
---
# A projectile passing close to the listener

**Goal:** Hear an appropriate flyby when a projectile passes nearby, without playing a near-miss sound for every shot in the level.

The trick is to test the projectile's **path**, not merely its firing event. AudioPhysx can estimate closest approach from a submitted segment and, for accepted near misses, schedule playback near that point.

## What you need

A mono MetaSound Source containing [AP: Flyby Wave Player](../metasound/nodes/playback/flyby-wave-player.md), whizz and optional crack Wave Asset Arrays, and a Blueprint that knows the projectile's path start, path end and nominal speed.

## Test it in three passes

>>> 1. Configure the MetaSound
Wire the five runtime Float parameters described in the [flyby Blueprint guide](../blueprint/flyby.md). Confirm the player auditions with manual values first.

>>> 2. Submit a close path
Call `AP: Play Projectile Flyby` with a path that passes near the listener, within `AudibleRadiusM`.

>>> 3. Submit a distant path
Keep the speed and recording the same, but move the path outside the audible radius. This should not be accepted as a near miss.

>>> 4. Compare subsonic and supersonic cases
Change the supplied speed while keeping the geometry comparable. The crack layer depends on the calculated shock condition, not simply the presence of a bullet recording.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/graph-projectile-flyby.png -->

## Common mistake

Positions are in Unreal world units (normally **centimetres**), but `ProjectileSpeedMps` and `AudibleRadiusM` are in **metres per second** and **metres**. Mixing units can make a believable path look thousands of times too far away or too fast.

!!!info Model scope
This is a useful game-audio approximation, not a complete aerodynamic shock-wave simulation. Test timing and source placement in your actual gameplay level.
!!!
