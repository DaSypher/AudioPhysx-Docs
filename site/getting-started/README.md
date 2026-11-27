---
label: "Getting started"
icon: rocket
order: 95
---


# Getting started with AudioPhysx

The fastest way to understand AudioPhysx is to make one sound work end to end before building a complicated acoustic system. You can begin with an ordinary imported recording, one trigger and a stereo MetaSound Source. Once the basic signal flows correctly, it becomes much easier to understand why a material-aware player, propagation processor or world-query component is useful.

This documentation uses the **current stereo C++ source** as its contract. An older MetaSound graph may still have `Out Mono` pins from a previous version of the plugin; those assets should be backed up and migrated deliberately rather than resaved as soon as Unreal refreshes their nodes.

## A practical learning order

**Begin with [installation](installation.md).** Confirm that the AudioPhysx plugin loads and the node categories appear in the MetaSound editor. Then read [requirements and terminology](requirements.md) for the difference between Wave Assets, audio buffers, control values and triggers. These distinctions prevent many silent-graph problems later.

**Build [your first MetaSound](first-metasound.md).** The tutorial uses Sequence Wave Player because it demonstrates how playback timing and completion work without needing gameplay path queries or project-wide acoustic settings. After that, the [stereo routing guide](stereo-routing.md) explains how to keep Left and Right channels or fold them down to mono for appropriate 3D sources.

**Add game integration when the sound needs it.** The Blueprint section explains how to obtain the physical material from a hit, submit a projectile path, and query a selected acoustic route. These calculations are useful, but they should not be made prerequisites for a simple random or layered sound effect.

If something does not play, use the [setup checklist](checklist.md) and [troubleshooting](../support/troubleshooting.md). It is usually faster to isolate one missing Wave Asset or trigger than to adjust ten unrelated DSP settings.

<!-- IMAGE SLOT: site/static/images/setup/node-search.png -->
