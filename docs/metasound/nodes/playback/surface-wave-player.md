---
label: "AP: Surface Wave Player"
icon: file
order: 90
---
# AP: Surface Wave Player

**MetaSound · AudioPhysx / Playback**

Select surface-appropriate sound variations using Unreal surface types and your project’s AudioPhysx route settings.

<!-- IMAGE SLOT: docs/static/images/nodes/node-surface-wave-player.png -->

## What actually happens

The Surface Wave Player uses `Hit Surface Type` to decide which pool of recordings should play. It can expose **surface-specific pins** based on AudioPhysx settings, and it includes a default pool for unmatched material IDs.

It is intended for workflows such as footsteps or impacts where the gameplay side already knows what surface was hit. The MetaSound is responsible for choosing and playing the recording, not for tracing the world itself.

## Hear it in a game

Create stone, metal and grass variations, then play a footstep animation with a surface trace. Send the returned surface type to the graph and listen for the correct texture. Test an unconfigured surface too: it should use `Default Waves` when that pool is populated.

## Build a working graph

>>> 1. Configure surface routes
Configure the project’s AudioPhysx surface routes first, then restart the editor if the project settings require it.
>>>

>>> 2. Assign surface recordings
Add the player to a MetaSound and connect the exposed surface-specific arrays as well as `Default Waves`.
>>>

>>> 3. Send surface type and Play
Supply `Hit Surface Type` before sending `Play`. Tune the volume and `Max Voices` for footsteps or repeated impacts.
>>>

## The controls that matter

`Hit Surface Type` is the numerical physical-surface selection provided by game logic. `Default Waves` and `Default Volume` supply a fallback when no authored route matches. `No Immediate Repeat` affects variation choice; `Max Voices` caps overlapping playback.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mixed mono audio from active samples.
- **`On Finished`** · Trigger — Fires when the last playing voice ends naturally.  Stop or rejected Play events do not trigger it.

## Things to watch for

- **Saved-graph compatibility:** changing which surface routes are enabled can change this node’s pin layout. Review existing graphs after route-setting changes rather than assuming connections remain intact.
- A physical-material trace generally needs physical material return information enabled in the relevant query/collision setup. This node does not perform the trace for you.

==- Full input reference
- **`Play`** · *Trigger* — Select one valid wave from the hit surface.
- **`Stop`** · *Trigger* — Stop all playing samples.
- **`Hit Surface Type`** · *Integer* — Unreal EPhysicalSurface integer value  of the impacted physical material.
- **`Max Voices`** · *Integer* — Maximum overlapping samples (1 to 16).
- **`No Immediate Repeat`** · *Boolean* — Avoid selecting the previous sample  when alternatives exist.
- **`Default Waves`** · *Wave Asset Array* — Fallback array for unmatched surfaces  or empty surface arrays.
- **`Default Volume`** · *Float* — Linear volume for fallback samples.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mixed mono audio from active samples.
- **`On Finished`** · Trigger — Fires when the last playing voice ends naturally.  Stop or rejected Play events do not trigger it.
===

## Continue learning

[PhysMat Wave Player](physmat-wave-player.md) selects by exact Physical Material path rather than surface-type number. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
