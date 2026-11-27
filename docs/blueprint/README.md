---
label: Blueprint integration
icon: code
order: 85
---
# Connecting game events to audio

MetaSound processes audio, but it does not automatically know where the player is standing, what material a bullet passed, or whether a source is behind a wall. AudioPhysx provides Blueprint-facing functions and components so you can feed that information into the sound graph.

The division is intentional: **world queries and gameplay events run outside the audio rendering loop**, while the MetaSound node uses the resulting values to select or process a sound. You don't need to use every integration feature to benefit from the Playback nodes.

## Pick a workflow

[!card layout="compact" title="Projectile flyby" text="Check a path near the listener and play a whizz or crack at the appropriate time."](flyby.md)

[!card layout="compact" title="Playback helpers" text="Play world-aware sounds, manage registered audio components and environment values."](playback-helpers.md)

[!card layout="compact" title="Acoustic path queries" text="Evaluate a direct or around-obstacle route and drive acoustic processing."](acoustic-paths.md)

[!card layout="compact" title="Level components" text="Emitters, barriers, portals and the physics/audio bridge."](components.md)

[!card layout="compact" title="Acoustic materials and settings" text="What physical parameters mean, how they feed models, and where budgets are configured."](materials-and-settings.md)

## Before wiring complex systems

Start by printing the Blueprint's distance, material or route result. Confirm it changes as expected in your level **before** spending time debugging the MetaSound. This keeps gameplay-data problems separate from audio-rendering problems.

<!-- IMAGE SLOT: docs/static/images/blueprint/bp-flyby-hitscan.png -->
