---
label: "Materials and settings"
icon: gear
order: 70
---
# Acoustic Physical Materials and project settings

## Acoustic material asset

`UAPAcousticPhysicalMaterial` extends Unreal's `UPhysicalMaterial` with acoustic information including:

- Acoustic density and longitudinal sound speed.
- Internal damping.
- Three-band authored transmission loss or approximate mass-law evaluation.
- Reference/fallback thickness and optional thickness scaling.
- Surface absorption and scattering values.

Values such as density and sound speed should represent the material **model you're authoring**; they are not automatically measured from geometry.

<!-- IMAGE SLOT: docs/static/images/settings/acoustic-material-inspector.png -->

## Project settings

`UAPAudioSettings` exposes performance budgets and acoustic controls, including emitter updates per tick, obstruction-query limits, atmosphere values, acoustic path depth and optional around-obstacle paths.

<!-- IMAGE SLOT: docs/static/images/settings/project-settings-audiophysx.png -->

## Surface Audio warning

`AP: Surface Wave Player` generates pins from enabled surface routes configured in project settings. **After changing that route list, restart the editor and inspect affected MetaSound assets**, because pin interfaces can change.

See [Surface Wave Player](../metasound/nodes/playback/surface-wave-player.md) and [Acoustic components](components.md).
