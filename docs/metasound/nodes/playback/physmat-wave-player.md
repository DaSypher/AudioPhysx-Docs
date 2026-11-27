---
label: "AP: PhysMat Wave Player"
icon: file
order: 93
---

# AP: PhysMat Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

Choose impact or interaction recordings using the exact Physical Material asset involved in the event.

<!-- IMAGE SLOT: docs/static/images/nodes/node-physmat-wave-player.png -->

## Understanding the behaviour

Physical Materials can distinguish surfaces more precisely than a broad surface category. PhysMat Wave Player accepts a string path identifying the hit Physical Material and compares it to the configured route entries. When it finds a match, it selects from the associated Wave Asset Array; otherwise, it can use `Default Waves`. This is a sound-selection mechanism, not a world trace. Your gameplay or Blueprint system is responsible for obtaining the correct hit result and material identity.

The node now renders its selected recording in stereo. That means a stereo-captured surface impact can preserve channel differences through the player, even if you later choose to downmix it for a mono, spatialized world emitter.

Suppose two metal objects share the game's general metal category: a thin sheet and a heavy steel plate. You may want a lightweight, bright rattle for the sheet and a dense ringing impact for the plate. Assign those objects different Physical Materials, configure the paths, and let the player select a different pool for each.

A reasonable fallback is important in a large project. New levels and assets may introduce materials that were never explicitly mapped; supplying `Default Waves` prevents those legitimate interactions from becoming silent.

## Building and controlling the sound

Set up the material route configuration with the exact Physical Material asset paths and corresponding arrays. In your gameplay logic, obtain the Physical Material from the trace or hit information and supply its asset path as `Hit PhysMat Path`. Then trigger `Play` and connect `Out Left`/`Out Right` to the Source. Use one known matching material and one deliberately unmapped material in your first test.

The route entries have their own `Volume` values. The default pool has `Default Volume`, so you can balance the fallback separately. `Max Voices` and `No Immediate Repeat` make frequent footstep or impact requests more manageable.

An asset path is not merely the friendly display name shown in the Content Browser. Moving or renaming Physical Material assets can invalidate old paths. `On Rejected` indicates a playback request that could not start, while `On Finished` indicates the final naturally completing voice. Test what your trace returns rather than assuming a visual material assignment automatically identifies the relevant Physical Material.

**Practical limitations.** If your game only needs the coarse `EPhysicalSurface` value, Surface Wave Player may be simpler. If it needs more detailed wall transmission properties, use the separate Acoustic Physical Material model; exact-path playback routing is not equivalent to computing acoustic transmission.


==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Choose and play one recording.
- **`Stop`** — *Trigger*. Stop all active voices.
- **`Hit PhysMat Path`** — *String*. Exact Physical Material asset path.
- **`Default Waves`** — *Wave Asset Array*. Wave Asset array used when no route matches.
- **`Default Volume`** — *Float*. Linear gain of fallback recordings.
- **`No Immediate Repeat`** — *Boolean*. Avoid repeating the previous recording  when alternatives are available.
- **`Max Voices`** — *Integer*. Maximum overlapping recordings.
- **`Waves`** — *Wave Asset Array*. Wave Asset array for this material.
- **`Volume`** — *Float*. Linear volume for this material.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Stereo mix output.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Fires when the final voice ends naturally.
- **`On Rejected`** — *Trigger*. Fires when a requested voice cannot start.

===

**Related:** [Surface Wave Player](surface-wave-player.md) for category-based routing.
