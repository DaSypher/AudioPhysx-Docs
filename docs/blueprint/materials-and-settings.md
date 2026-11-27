---
label: Materials and settings
icon: gear
order: 70
---
# Acoustic Physical Materials

An acoustic material describes how an authored surface should affect sound. It is not a recording and is not automatically measured from your level geometry. The values express a **model** that AudioPhysx can use when estimating transmission and other acoustic behaviour.

`UAPAcousticPhysicalMaterial` extends Unreal's Physical Material with acoustic properties. It can include material density and longitudinal sound speed, damping, a thickness context and low/mid/high authored transmission losses. There are also absorption and scattering controls for acoustic models that use them.

## Think in terms of listening results

A heavy, sealed barrier may need much larger transmission loss than a thin partition. That loss can differ across frequency bands; the goal is to make obstructed audio believable, not to pretend every wall is accurately described by one physical constant.

You can use an authored three-band loss curve or the available approximate mass-law model. Authored values are useful when you want repeatable, designer-controlled outcomes. The mass-law option is a simplified estimate, not a measurement of a specific finished structure.

<!-- IMAGE SLOT: docs/static/images/settings/acoustic-material-inspector.png -->

## Project-wide acoustic settings

`UAPAudioSettings` contains environment and workload controls, including world update scheduling, obstruction-ray limits, maximum path detail and optional alternate-route processing. These matter when the scene contains many emitters: a convincing effect that performs poorly with twenty active sources is not ready for shipping.

<!-- IMAGE SLOT: docs/static/images/settings/project-settings-audiophysx.png -->

## Important: surface-specific node pins

[AP: Surface Wave Player](../metasound/nodes/playback/surface-wave-player.md) can generate pins based on enabled surface routes in AudioPhysx settings. If you change that list, **restart the editor and review existing MetaSound graphs**. Unlike a runtime float value, a changed pin layout can affect authored graph connections.

[Acoustic components](components.md) · [Material Transmission](../metasound/nodes/acoustics/material-transmission.md)
