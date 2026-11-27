# Bringing game-world information into audio

MetaSound processes audio and audio-rate events, but it does not automatically know where a projectile travelled, what wall is between a source and listener, or which Physical Material was returned by a collision query. AudioPhysx uses Blueprint-accessible helpers, world subsystems and Actor components to provide that information without moving world-geometry work onto the audio rendering thread.

The recommended process is to **verify the game data before processing the sound**. If an acoustic filter seems wrong, print the obstruction flag or selected path. If a material player chooses the fallback recordings, print the material identifier from the hit result. If a flyby never plays, first check whether the path passed within the audible radius. This separates gameplay setup problems from decoding and DSP issues.

## Choose the integration you need

[!card layout="compact" title="Projectile flybys" text="Build a near-miss path calculation and connect it to the stereo Flyby Wave Player."](flyby.md)

[!card layout="compact" title="Physical sound playback" text="Play sound at world positions, use hit results and register persistent audio components."](playback-helpers.md)

[!card layout="compact" title="Acoustic path queries" text="Understand clear, obstructed and around-obstacle routes before passing compact data into MetaSound."](acoustic-paths.md)

[!card layout="compact" title="Scene components" text="Set up emitters, barriers, portals and the bridge between scene state and sound."](components.md)

[!card layout="compact" title="Materials and performance" text="Understand Acoustic Physical Materials, thickness, transmission loss and world query budgets."](materials-and-settings.md)

The stereo conversion does not require a new Blueprint API: these helpers still supply **sound assets and control data**, while the internal MetaSound graph now connects Left and Right audio buffers. Refer to [stereo routing](../getting-started/stereo-routing.md) when authoring the Source itself.
