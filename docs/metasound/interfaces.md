---
label: "Interfaces and external parameters"
icon: code
order: 50
---
# MetaSound interfaces and game-provided data

AudioPhysx can publish acoustic parameter values from Blueprint/world systems to a MetaSound graph. Use the interfaces and names included with your **installed plugin build**, rather than creating independent duplicate parameters with similar names.

The current source includes a compact selected-route contract:

| Parameter | Data |
| --- | --- |
| `AP.AcousticRoute.Selected` | Float Array: `[delay ms, low loss dB, mid loss dB, high loss dB]` |

Connect that array to [AP: Acoustic Paths](nodes/acoustics/acoustic-paths.md) when using the managed route system.

Other parameters are grouped by propagation, atmosphere, transmission and impact; refer to your installed interface list in the MetaSound editor. Avoid manually mixing data from different interface versions.

<!-- IMAGE SLOT: docs/static/images/graphs/graph-acoustic-interface.png -->

## Authoring tip

When an engine or plugin interface changes, compare the generated MetaSound pins **before saving modified graphs**. This is particularly important for projects with previously authored material routes.
