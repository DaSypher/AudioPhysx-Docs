---
label: "Acoustic components"
icon: package
order: 75
---
# Acoustic components

AudioPhysx includes several components for representing environmental acoustics in a level.

| Component | Role |
| --- | --- |
| `UAPSpatialAudioEmitterComponent` | Holds a sound, optional attenuation asset and managed obstruction-trace behaviour. |
| `UAPAcousticBarrierComponent` | Associates acoustic material and thickness information with a primitive component. |
| `UAPAcousticPortalComponent` | Represents an enabled passage with configurable low/mid/high-band extra loss. |
| `UAPPhysicsBridgeComponent` | Bridges scene/audio components with movement/environment/transmission settings. |

## Suggested demonstration

Create a small map with two rooms, a doorway and a sound emitter. Give one wall an acoustic barrier component. Move the listener between positions and compare clear/blocked/around-path results.

<!-- IMAGE SLOT: docs/static/images/acoustics/acoustic-test-room.png -->

## Important

- Acoustic barrier geometry still needs a suitable target primitive and collision behaviour.
- The portal component does not itself model a fully traced room impulse response.
- Project-wide scheduling limits are configurable in AudioPhysx settings; high emitter counts should be profiled in a packaged build.
