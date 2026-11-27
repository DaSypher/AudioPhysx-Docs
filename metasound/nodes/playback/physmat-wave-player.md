# AP: PhysMat Wave Player

**MetaSound · AudioPhysx / Playback**

Route playback using an exact Unreal Physical Material asset path, with a fallback when nothing matches.

## What actually happens

Surface type alone may be too coarse. Multiple Physical Materials can share a broad category but require different sounds. This player accepts `Hit PhysMat Path` and compares it against configured material routes, selecting a variation from the matching pool.

The player also has default recordings. That matters commercially: a missing or newly introduced material should be handled gracefully rather than requiring a new branch in every MetaSound.

## Hear it in a game

Imagine two surfaces both categorized as metal: a thin steel sheet and a heavy steel plate. Give them distinct Physical Materials and different impact recordings. Supply the actual asset path so the player can distinguish them.

## Build a working graph

>>> 1. Define Physical Material routes
Define Physical Material routes using the plugin’s supported configuration and confirm the path strings are accurate.
>>>

>>> 2. Provide reliable fallback sounds
Assign recordings for each route and populate `Default Waves` as a fallback.
>>>

>>> 3. Send the asset path and Play
Send the exact `Hit PhysMat Path` and trigger `Play`; test a valid configured path and an intentionally unmatched path.
>>>

## The controls that matter

`Hit PhysMat Path` is an **asset path**, not the display name of a material in Content Browser. `Waves` and `Volume` correspond to authored route entries. `Default Volume` applies to fallback recordings. `Max Voices` and `No Immediate Repeat` control overlapping playback and repetition.

## Outputs and completion

- **`Out Mono`** · Audio (mono) — Mixed mono audio output.
- **`On Finished`** · Trigger — Fires when the final voice ends naturally.
- **`On Rejected`** · Trigger — Fires when a requested voice cannot start.

## Things to watch for

- Renaming or moving Physical Material assets can change their paths. Test after asset migrations.
- Do not confuse the Acoustic Physical Material asset used for transmission calculations with the Physical Material path used for playback routing.

==- Full input reference
- **`Play`** · *Trigger* — Choose and play one recording.
- **`Stop`** · *Trigger* — Stop all active voices.
- **`Hit PhysMat Path`** · *String* — Exact Physical Material asset path.
- **`Default Waves`** · *Wave Asset Array* — Wave Asset array used when no route matches.
- **`Default Volume`** · *Float* — Linear gain of fallback recordings.
- **`No Immediate Repeat`** · *Boolean* — Avoid repeating the previous recording  when alternatives are available.
- **`Max Voices`** · *Integer* — Maximum overlapping recordings.
- **`Waves`** · *Wave Asset Array* — Wave Asset array for this material.
- **`Volume`** · *Float* — Linear volume for this material.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Mixed mono audio output.
- **`On Finished`** · Trigger — Fires when the final voice ends naturally.
- **`On Rejected`** · Trigger — Fires when a requested voice cannot start.
===

## Continue learning

[Material footsteps recipe](../../../examples/material-footsteps.md) compares this with surface-type routing. Also see the [Playback overview](../../playback.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
