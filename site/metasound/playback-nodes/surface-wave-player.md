---
label: "AP: Surface Wave Player"
icon: file
order: 92
---

# AP: Surface Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

Use Unreal physical surface types to select footstep, impact or interaction variations through one MetaSound player.

<!-- IMAGE SLOT: site/static/images/nodes/node-surface-wave-player.png -->

## Understanding the behaviour

Surface Wave Player uses the integer value of `EPhysicalSurface` supplied through `Hit Surface Type`. Configured AudioPhysx routes determine which surface-specific Wave Asset Array should be used, with `Default Waves` available for unmatched values. This is especially useful when the game already classifies surfaces into a manageable set such as grass, concrete, gravel and metal.

The surface-specific pins are generated from configuration, rather than being identical in every possible project. That reduces pointless pins when only a few surfaces are used, but it creates an authoring responsibility: if route configuration changes, inspect the saved MetaSound graph to ensure its dynamic input layout still matches the intended assets.

In a footstep system, the animation usually defines the exact timing of the step and the gameplay trace identifies the ground material. Surface Wave Player uses that supplied value to choose a recording pool. It does **not** perform the character's foot trace or decide how often footsteps should occur.

With stereo output, a designer can preserve deliberately stereo footstep recordings through the graph. For a single, precisely positioned footstep in the world, downmixing to mono just before the Source output may still be the better spatial choice.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Configure Surface Audio before graph authoring
In AudioPhysx project settings, enable the surface routes you intend to use. Because this node can generate pins from those settings, restart the Editor if needed before you build the MetaSound.

>>> 2. Create the stereo player graph
Create a Stereo MetaSound Source and add **AP: Surface Wave Player**. Review the route-specific Wave Asset Array pins that appear on the node.

>>> 3. Fill route and default recordings
Provide recordings to the enabled surface slots and assign `Default Waves` for unsupported surfaces. Use `Default Volume` to balance the fallback material.

>>> 4. Feed the surface type and trigger
Supply `Hit Surface Type` from a game trace or a known test integer, then trigger the player with `Play`. Connect `Out Left`/`Out Right` to the stereo outputs.

>>> 5. Validate and protect saved graphs
Test two configured surface types and an unmatched type. After changing the project route list, inspect existing saved graphs for changed pins before resaving them.
>>>

<!-- IMAGE SLOT: site/static/images/graphs/setup-surface-wave-player.png -->

**After the basic setup:** First configure the enabled Surface Audio routes in AudioPhysx project settings and restart the Editor when required. Create a Source and add the player, then assign the arrays to the generated surface pins. Fill `Default Waves` with a safe fallback, supply the hit surface's integer value to `Hit Surface Type`, and connect `Play` and both audio outputs.

Test three cases separately: one surface with an exact route, another configured route, and an intentionally unmapped surface. You should be able to tell which pool is selected without changing the gameplay event timing.

`Max Voices` controls the maximum number of overlapping recordings. `No Immediate Repeat` is useful with several takes per surface, but cannot guarantee variation with only one valid recording. `Default Volume` balances the fallback pool; route-specific volume controls balance authored surfaces. The player's `On Finished` output reflects natural completion of the last playing voice.

**Practical limitations.** This is one of the nodes most sensitive to configuration changes. If you disable or reorder configured surfaces, saved node pins may change and connections can be lost or become stale. Back up affected MetaSound assets before modifying the surface route settings. Do not assume editing a Physics Material asset alone updates the player's route list; verify what the gameplay trace supplies.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Select one valid wave from the hit surface.
- **`Stop`** — *Trigger*. Stop all playing samples.
- **`Hit Surface Type`** — *Integer*. Unreal EPhysicalSurface integer value  of the impacted physical material.
- **`Max Voices`** — *Integer*. Maximum overlapping samples (1 to 16).
- **`No Immediate Repeat`** — *Boolean*. Avoid selecting the previous sample  when alternatives exist.
- **`Default Waves`** — *Wave Asset Array*. Fallback array for unmatched surfaces  or empty surface arrays.
- **`Default Volume`** — *Float*. Linear volume for fallback samples.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Stereo mix from active samples.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Fires when the last playing voice ends naturally.  Stop or rejected Play events do not trigger it.

===

**Related:** [Material-dependent footsteps](../../examples/material-footsteps.md) for a complete gameplay setup.
