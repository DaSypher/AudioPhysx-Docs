# Troubleshooting AudioPhysx

When something goes wrong, isolate the system in this order: **can Unreal play the asset? → does the MetaSound receive a trigger? → does the node output audio? → are world parameters correct?** Debugging each layer separately is usually faster than changing every setting at once.

## I can't find any AudioPhysx nodes

Open **Edit → Plugins** and verify AudioPhysx is enabled. Restart the Editor after plugin activation or a native rebuild. In a MetaSound Source, search `AP:` and inspect the AudioPhysx categories.

For source builds, confirm the full plugin directory includes the `.uplugin` descriptor and that its C++ module actually compiled for your installed engine version. Copying a standalone `Source` folder is not equivalent to installing a complete code plugin.

## My Wave Player is silent

Start with a simple mono MetaSound Source and **one known-good Wave Asset**. Connect `Play` and `Out Mono` before adding other processing. Check that the array is not empty and that the recording imports and auditions normally in Unreal.

If the sound plays in a simple Source but disappears in your game, examine attenuation, concurrency and world-space source position. If it stops when you add an acoustic effect, inspect that effect's input values and the completion routing.

## The sequence plays only the first recording

For a fixed or random sequence, make sure later slots contain playable Wave Assets and are genuinely part of the expandable group. The next sound should follow playback completion, not a manually connected delay. Check whether an early Source-level `On Finished` is terminating the graph.

## Start Loop End never ends

A held sequence is expected to keep its middle phase active while firing. **`Stop Firing` is required** to request the end phase. `Immediate Release` controls whether active recordings fade promptly or finish first. At positive RPM values, overlapping middle voices can remain audible after the release request when immediate release is disabled.

## Flyby doesn't trigger

Print the result from `AP: Calculate Flyby` before requesting playback. Check that the shot path passes within `AudibleRadiusM`, that path positions are in Unreal world units, and that speed is supplied in metres per second.

If geometry is accepted but audio remains silent, verify the five named external Float inputs in the flyby MetaSound and whether its `On Play` reaches the Wave Player.

## The acoustic path sounds too dark or delayed

Inspect the four selected-route values: **delay ms, low loss dB, mid loss dB, high loss dB**. Check that Unreal occlusion or air absorption is not doubling the effect, and confirm the requested delay is within the node's allocated capacity.

## My dynamic pins changed

When you edit the enabled surface-route list, `AP: Surface Wave Player` may expose a different pin layout. Back up the affected MetaSounds, restart after changing settings, and inspect connections before resaving. For an ordinary expandable group, verify the authored group instance count remains correct.

## C++ errors after a source update

Read the **first compiler error**, not only the final build summary. Close the Editor, disable Live Coding and make sure you have not kept two versions of the same node `.cpp` under different names. If generated reflection files are stale, remove the plugin's `Binaries` and `Intermediate` directories before regenerating/rebuilding.

## The Editor works but a packaged game doesn't

A clean Editor build is not proof of a working Shipping build. Check that assets were cooked, the runtime module loads, all references are included, and any optional audio system or config used by the graph is available at runtime. Begin with a packaged **Development** build for useful logging, then verify the same behaviour in **Shipping**.

## What to include in a useful bug report

- Exact Unreal Engine version, plugin version, operating system and build configuration.
- Which MetaSound node or Blueprint helper failed.
- A minimal graph or path setup with reproducible inputs.
- Expected result, actual result and first relevant log message.

[Requirements](../getting-started/requirements.md) · [Compatibility](compatibility.md)
