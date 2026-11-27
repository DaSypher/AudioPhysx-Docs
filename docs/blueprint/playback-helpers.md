---
label: "Physical sound playback"
icon: play
order: 85
---
# Blueprint playback helpers

The public `UAPAudioBlueprintLibrary` exposes these callable operations in the current source:

| Display name | Purpose / primary inputs |
| --- | --- |
| `AP: Play Physical Sound` | Play `USoundBase` at a location and source rotation, with optional obstruction query and volume scaling. |
| `AP: Play Physical Impact` | Play a sound using hit location data, with optional obstruction query. |
| `AP: Register Audio Component` | Register an existing audio component for managed AudioPhysx parameter updates; choose whether to trace obstruction. |
| `AP: Unregister Audio Component` | Remove that audio component from managed updates. |
| `AP: Set World Environment` | Update temperature, relative humidity and pressure for the AudioPhysx world context. |

## Typical flow

1. Prepare a MetaSound Source using the relevant AudioPhysx interface/parameters.
2. Supply a `USoundBase` and world context to the Blueprint helper.
3. Pass location, rotation or an `FHitResult` from your own gameplay system.
4. Verify the sound and any propagated acoustic parameters in standalone play.

<!-- IMAGE SLOT: docs/static/images/blueprint/bp-play-physical-sound.png -->

> These functions don't produce sound recordings automatically; the supplied sound asset is still required. Some rely on world registration/configuration and may behave differently if no listener or audio device is available.
