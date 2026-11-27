---
label: "Acoustic scene components"
icon: package
order: 75
---


# Representing the acoustic scene

AudioPhysx includes optional components that associate sounds, physical obstacles and openings with real level objects. They are designed to let a managed acoustic system reason about where a sound begins and what it passes through. You do **not** need to attach all these components to use Random Wave Player or other ordinary playback nodes.

**`UAPSpatialAudioEmitterComponent`** represents a managed source with a sound asset, optional attenuation asset and obstruction-trace behaviour. It is a practical starting point for a sound that stays in the world while the listener or emitter moves. **`UAPAcousticBarrierComponent`** associates an acoustic material, a target primitive and optional thickness override with level geometry. The geometry and collision still have to be configured correctly, because the component cannot measure useful thickness from an object that the relevant trace never intersects.

**`UAPAcousticPortalComponent`** represents a possible passage with extra low, mid and high frequency losses, which the around-path system can consider when enabled and available. It should not be mistaken for a full portal-based reverb engine. **`UAPPhysicsBridgeComponent`** provides another link between game-side state and audio parameters for supported physics/environment workflows; it is not required for a simple standalone Wave Player.

## A reproducible test room

Create two simple spaces connected by a doorway, place one looping source in the first room, and put the listener in the second. Begin with no obstruction, then add a wall primitive with a valid Acoustic Barrier component and suitable collision. Use the Blueprint path query to inspect whether the wall is recognized. Only after the direct path works should you add the Portal near the opening and look for around-path candidates.

<!-- IMAGE SLOT: docs/static/images/acoustics/acoustic-test-room.png -->

The test should be as controlled as possible. Do not begin with a complex production level containing hundreds of intersecting meshes and several overlapping emitters. A small map makes it clear whether a change in sound comes from barrier properties, path selection, a manually authored filter or Unreal's normal attenuation.

Since the world system operates on scheduled updates and query budgets, you should also profile a realistic count of active sources. A feature can sound convincing in a room with one emitter and still require careful update limits to perform acceptably in a dense game environment.
