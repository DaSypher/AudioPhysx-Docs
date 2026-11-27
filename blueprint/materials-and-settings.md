# Acoustic materials, thickness and performance settings

An Acoustic Physical Material describes the model you want AudioPhysx to use for a surface's sound-transmission behaviour. The current `UAPAcousticPhysicalMaterial` derives from Unreal's Physical Material and adds acoustic parameters such as density, longitudinal sound speed, internal damping, transmission loss, reference thickness, absorption and scattering. It is an authorable model, **not a laboratory measurement automatically extracted from your mesh**.

When enabled, the material can use an authored low/mid/high transmission-loss description or an approximate mass-law approach. Authored losses are useful when a sound designer knows the listening result they want and wants reproducible control. The alternative model uses material-related values to derive an estimate. Either approach must be judged by what the gameplay geometry and audio routing actually supply; a heavy-looking object with the wrong collision or missing material assignment may contribute no meaningful acoustic data.

## Set up the model in stages

First make sure a trace identifies the intended primitive or Physical Material. Then assign an Acoustic Barrier component or supported acoustic material configuration. Start with an easily heard contrast between a clear and blocked source, using reasonable thickness and a clear three-band loss difference. Once the result works, refine density, damping, reference thickness and any optional scattering or absorption data that the chosen processing path actually uses.

**`UAPAudioSettings`** contains environment values, surface routes and performance limits. The current source exposes emitter updates per tick, obstruction traces per tick, scheduled acoustic-ray budgets, query refresh intervals, maximum barrier layers, thickness measurement controls and optional around-obstacle paths. These settings exist because acoustic world queries must remain predictable as the number of active emitters increases.

A final important setting concerns **Surface Audio routes**. `AP: Surface Wave Player` can generate input pins from the configured enabled surfaces. Changes to that list can affect existing graph interfaces, so back up and review affected MetaSound assets before assuming a new surface configuration will be harmless. The stereo upgrade is another independent interface change: reconnect both channel outputs in migrated graphs, and verify saved graphs before publishing the plugin to customers.
