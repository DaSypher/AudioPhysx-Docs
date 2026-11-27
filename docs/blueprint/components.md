---
label: Acoustic components
icon: package
order: 75
---
# Representing an acoustic scene

AudioPhysx has components that connect real game objects to the acoustic model. You don't need all of them for ordinary playback. They're most useful when you want source-to-listener obstruction or around-opening behaviour to react to the level.

## The emitter: where the sound begins

`UAPSpatialAudioEmitterComponent` represents a managed sound source with its audio and optional attenuation behaviour. It can participate in obstruction updates, allowing the sound to react as the listener and environment change.

## The barrier: what blocks the sound

`UAPAcousticBarrierComponent` associates thickness and acoustic material information with a primitive. Its model is more descriptive than treating a wall as simply “blocked or clear.” The associated geometry and collision still have to be set up correctly in the map.

## The portal: where an alternate path may exist

`UAPAcousticPortalComponent` represents an opening or passage with extra frequency-band loss. An around-path candidate can use it when the world path solver supports that route. This is **not** a full room impulse-response or reverberation bake.

## The bridge: exposing additional state

`UAPPhysicsBridgeComponent` connects movement, transmission and environment-related information to audio. The exact configuration depends on the emitter and game system; this is not a requirement for simple Wave Player nodes.

## A useful test map

Build two simple rooms, a doorway and one looping source. Add an acoustic barrier to a relevant primitive and a portal near the opening. Move the listener between clear line of sight, obstructed position and doorway. Inspect the [path query result](acoustic-paths.md) before adjusting how the MetaSound renders it.

<!-- IMAGE SLOT: docs/static/images/acoustics/acoustic-test-room.png -->

!!!tip Performance is part of the design
Acoustic tracing is scheduled and budgeted. Begin with just one emitter, then profile how the subsystem scales with your expected number of active sources rather than enabling high-frequency traces on everything.
!!!
