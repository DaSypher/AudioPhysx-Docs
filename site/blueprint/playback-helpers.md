---
label: "Physical sound playback"
icon: play
order: 80
---


# Playing sounds from Blueprint

Many AudioPhysx sounds begin in ordinary gameplay code. A character performs an interaction, a projectile hits a surface, or a persistent emitter needs to follow an Actor. The Blueprint playback library provides convenience operations to connect those events to audio while allowing optional acoustic management when the project needs it.

**`AP: Play Physical Sound`** accepts a sound asset and world location, with a source rotation, volume and relevant optional acoustic settings supplied through its function signature. It is useful when the event has a known position and you do not want to create a dedicated audio Actor for every occurrence. **`AP: Play Physical Impact`** is related, but takes an `FHitResult` so the event can use hit-location information already produced by gameplay.

These functions do not generate recordings or automatically configure a MetaSound graph. Supply a valid `USoundBase` asset with the desired Wave Players and processing. After the stereo upgrade, the inside of that MetaSound may be stereo or deliberately folded down to mono; the Blueprint call still works with the sound asset rather than its individual audio pins.

## Persistent sources and environment

For sounds that continue playing as the world changes, **`AP: Register Audio Component`** can associate an existing `UAudioComponent` with managed AudioPhysx parameter updates, optionally enabling obstruction tracing. When the source is no longer relevant, **`AP: Unregister Audio Component`** removes that registration. Use component lifetime deliberately rather than leaving an unlimited number of emitters active in an otherwise quiet scene.

The separate **`AP: Set World Environment`** operation supplies temperature, humidity and pressure to the AudioPhysx world environment. These values can influence appropriate acoustic calculations, but setting them does not automatically make every sound in the project change. Only nodes and registered systems that use those parameters can render a corresponding audible difference.

<!-- IMAGE SLOT: site/static/images/blueprint/bp-play-physical-sound.png -->

A useful first test is to create a known-good stereo MetaSound with one Random Wave Player, call Play Physical Sound at a visible world location, and confirm that you hear it as expected. Test that baseline before turning on any obstruction or propagation processing. If the sound fails only after adding acoustic queries, you have narrowed the problem to the additional data rather than decoding, module loading or the basic sound asset.
