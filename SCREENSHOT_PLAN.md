# AudioPhysx screenshot checklist

The new documentation is complete without images: missing screenshots remain hidden placeholders. Add actual UE 5.8.4 screenshots under `docs/static/images/`; do not replace source-sensitive node screenshots with mockups. **Start with P0**, especially the two stereo routing examples and the new converter.

## P0 — Essential visual proof

- [ ] `brand/hero-audiophysx.png` — Home hero: real Unreal editor and game audio environment
- [ ] `graphs/graph-first-sequence.png` — Your first stereo Sequence Wave Player graph, complete wiring
- [ ] `graphs/graph-stereo-overview.png` — Stereo player into stereo DSP, Left and Right channels correctly routed
- [ ] `graphs/graph-stereo-to-mono.png` — Stereo chain converted to a mono MetaSound Source
- [ ] `setup/node-search.png` — MetaSound node palette showing AudioPhysx categories
- [ ] `setup/plugin-enabled.png` — AudioPhysx enabled in Edit > Plugins

## P1 — Integration demonstrations

- [ ] `acoustics/acoustic-test-room.png` — Two-room acoustic test with barrier, emitter and portal
- [ ] `blueprint/bp-flyby-hitscan.png` — Blueprint path trace into Play Projectile Flyby helper
- [ ] `blueprint/bp-play-physical-sound.png` — Play Physical Sound Blueprint function connected
- [ ] `blueprint/bp-query-acoustic-path.png` — Blueprint Acoustic Path result with direct/around values
- [ ] `brand/hero-demos.png` — Game or demonstration map overview
- [ ] `graphs/graph-acoustic-interface.png` — Compact AP.AcousticRoute.Selected into Acoustic Paths
- [ ] `graphs/graph-flyby-metasound.png` — Stereo Flyby player with five exposed AP.Flyby parameters
- [ ] `settings/acoustic-material-inspector.png` — Acoustic Physical Material inspector with transmission settings
- [ ] `settings/project-settings-audiophysx.png` — AudioPhysx project settings and performance limits

## P2 — Full node-by-node coverage

- [ ] `graphs/graph-acoustic-obstruction.png` — Complete working Sound behind a wall example graph
- [ ] `graphs/graph-automatic-weapon.png` — Complete working Automatic weapon with RPM example graph
- [ ] `graphs/graph-material-footsteps.png` — Complete working Material-dependent footsteps example graph
- [ ] `graphs/graph-projectile-flyby.png` — Complete working Projectile near-miss audio example graph
- [ ] `graphs/graph-random-sequence.png` — Complete working Multi-stage variation example graph
- [ ] `graphs/graph-randomized-one-shot.png` — Complete working Randomized one-shots example graph
- [ ] `nodes/node-acoustic-paths.png` — AP: Acoustic Paths: all pins, representative input values, readable zoom
- [ ] `nodes/node-atmosphere-absorption.png` — AP: Atmosphere Absorption: all pins, representative input values, readable zoom
- [ ] `nodes/node-distance-delay.png` — AP: Distance Delay: all pins, representative input values, readable zoom
- [ ] `nodes/node-distance-switch.png` — AP: Distance Switch (Dynamic): all pins, representative input values, readable zoom
- [ ] `nodes/node-distance-wave-player.png` — AP: Distance Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-doppler-ratio.png` — AP: Doppler Ratio: all pins, representative input values, readable zoom
- [ ] `nodes/node-dynamic-propagation.png` — AP: Dynamic Propagation: all pins, representative input values, readable zoom
- [ ] `nodes/node-early-reflections.png` — AP: Early Reflections: all pins, representative input values, readable zoom
- [ ] `nodes/node-float-smoother.png` — AP: Float Smoother: all pins, representative input values, readable zoom
- [ ] `nodes/node-flyby-wave-player.png` — AP: Flyby Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-impact-dynamics.png` — AP: Impact Dynamics: all pins, representative input values, readable zoom
- [ ] `nodes/node-layered-wave-player.png` — AP: Layered Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-material-transmission.png` — AP: Material Transmission: all pins, representative input values, readable zoom
- [ ] `nodes/node-physmat-wave-player.png` — AP: PhysMat Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-random-sequence-wave-player.png` — AP: Random Sequence Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-random-wave-player.png` — AP: Random Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-sequence-wave-player.png` — AP: Sequence Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-shuffle-bag-wave-player.png` — AP: Shuffle-Bag Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-source-directivity.png` — AP: Source Directivity: all pins, representative input values, readable zoom
- [ ] `nodes/node-start-loop-end.png` — AP: Start Loop End Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-stereo-to-mono.png` — AP: Stereo to Mono: all pins, representative input values, readable zoom
- [ ] `nodes/node-surface-wave-player.png` — AP: Surface Wave Player: all pins, representative input values, readable zoom
- [ ] `nodes/node-trigger-cooldown.png` — AP: Trigger Cooldown: all pins, representative input values, readable zoom
- [ ] `nodes/node-trigger-probability.png` — AP: Trigger Probability: all pins, representative input values, readable zoom

Keep recordings and user account details private when capturing screenshots. Use PNG for node graphs, readable zoom, and use widescreen crops for complex Blueprint workflows. Avoid changing filenames after inserting links.
