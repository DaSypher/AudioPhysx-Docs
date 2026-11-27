# Footsteps that match the ground

**Goal:** Make a footstep choose the correct texture—stone, grass, metal or another material—based on what the player actually stepped on.

AudioPhysx does **not** automatically perform the footstep trace inside the Wave Player. Your character, animation system or Blueprint sends the surface identifier. The player then selects a recording pool for that surface.

## Choose how to identify a material

+++ Surface type

Use [AP: Surface Wave Player](../metasound/nodes/playback/surface-wave-player.md) when Unreal's physical-surface type is enough. It is useful for broadly defined categories such as grass, gravel or metal.

The node's dynamic surface routes may depend on AudioPhysx project settings. Configure those **before** authoring a large number of graphs.

+++ Exact Physical Material

Use [AP: PhysMat Wave Player](../metasound/nodes/playback/physmat-wave-player.md) when multiple surfaces share a type but still need distinct sound choices. It compares the full Physical Material asset path rather than just a category number.

+++

## Build the footstep event

>>> 1. Collect the surface information
At the foot contact moment, trace or otherwise identify the Physical Material of the ground. Confirm the gameplay query returns material information as intended.

>>> 2. Send the correct identifier
Use the surface type for Surface Wave Player, or the exact material asset path for PhysMat Wave Player. Supply it before firing `Play`.

>>> 3. Provide variations and a fallback
Assign multiple Wave Assets for each surface and fill default recordings for unknown or unmapped surfaces.

>>> 4. Test movement over two surfaces
Walk across the boundary while watching the returned material data. Confirm the recordings follow the ground and that unmatched materials fall back sensibly.
>>>

## Make it sound believable

A good footstep system also depends on **which recording is chosen and when**. Keep variation within a surface coherent, align transients so feet land on time, and avoid overloading the node with sounds for every gameplay state. Movement speed and footwear can be handled by additional routing if needed.
