---
label: Interfaces and parameters
icon: code
order: 50
---
# Passing world data into MetaSound

A Wave Player can play a recording with only a trigger, but an acoustic processor needs to know something about the world: distance, material, obstruction, source direction or environment. AudioPhysx has interfaces and parameter names that link those game-side calculations to a MetaSound graph.

## The selected acoustic route

The current source uses one compact Float Array named **`AP.AcousticRoute.Selected`**. Its four values are ordered as follows:

```text
[delay in ms, low-band loss in dB, mid-band loss in dB, high-band loss in dB]
```

The game-world solver decides which route to use. [AP: Acoustic Paths](nodes/acoustics/acoustic-paths.md) reads that selected route and renders the corresponding delayed and filtered mono audio. This avoids connecting several unrelated route controls and accidentally using values from different world updates.

<!-- IMAGE SLOT: docs/static/images/graphs/graph-acoustic-interface.png -->

## Why order and units matter

If you swap the low- and high-loss values, the filter could make the source sound brighter when the material should muffle it. If you pass seconds as milliseconds, a travel delay can be wrong by a factor of a thousand. Treat the array as a **data contract**, not a bag of arbitrary floats.

## Other named parameters

The source also contains propagation, atmosphere, transmission and impact parameters. These are registered by AudioPhysx's native interfaces and world/Blueprint helpers. Prefer the exact pins and interface versions supplied by the installed plugin over manually recreating near-identical parameters with different names.

The standalone flyby subsystem supplies five named Float parameters, listed on the [Flyby Blueprint guide](../blueprint/flyby.md). Those must be exposed with matching names so the world helper can populate them before playback.

!!!warning Existing graph compatibility
When changing engine or plugin versions, inspect a saved graph's generated MetaSound inputs **before resaving it**, especially if interface versions or surface-route settings changed. A graph can compile but listen to the wrong input if names or types no longer match.
!!!
