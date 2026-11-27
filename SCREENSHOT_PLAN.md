# Screenshot plan

**You do not need all screenshots now.** The P0 captures will create most of the perceived quality of the site; P1 adds confidence for technical users; P2 completes individual node references.

| Priority | Filename (under `docs/static/images/`) | What to show |
| --- | --- | --- |
| **P0** | `blueprint/bp-flyby-hitscan.png` | Blueprint node AP: Play Projectile Flyby wired to trace start/end and MetaSound asset. |
| **P0** | `brand/hero-audiophysx.png` | Unreal scene or polished composite: one side a MetaSound graph, other side in-game audio scene. No generic stock photos. |
| **P0** | `graphs/graph-automatic-weapon.png` | Working weapon graph with RPM showing start/stop and output. |
| **P0** | `graphs/graph-first-sequence.png` | Complete working Sequence Wave Player graph with three waves and On Finished wiring. |
| **P0** | `graphs/graph-flyby-metasound.png` | Flyby Wave Player inputs, outputs and runtime parameters. |
| **P0** | `nodes/node-start-loop-end.png` | Crop Start Loop End node with RPM, three arrays and both outputs visible. |
| **P0** | `setup/node-search.png` | MetaSound add-node search for AudioPhysx showing categories. |
| **P0** | `setup/plugin-enabled.png` | Edit → Plugins with AudioPhysx enabled; hide personal project paths. |
| **P1** | `acoustics/acoustic-test-room.png` | Simple two-room map, wall barrier, emitter and portal, preferably with annotations. |
| **P1** | `blueprint/bp-play-physical-sound.png` | Blueprint node AP: Play Physical Sound with basic inputs wired. |
| **P1** | `blueprint/bp-query-acoustic-path.png` | Blueprint AP: Query Acoustic Path and useful return fields. |
| **P1** | `brand/hero-demos.png` | Two or three verified demo moments or a screenshot of example map. |
| **P1** | `graphs/graph-acoustic-interface.png` | AP.AcousticRoute.Selected array connected to Acoustic Paths. |
| **P1** | `settings/acoustic-material-inspector.png` | Details panel for UAPAcousticPhysicalMaterial, readable section names. |
| **P1** | `settings/project-settings-audiophysx.png` | AudioPhysx Developer Settings with path/ray budgets; hide unrelated settings. |
| **P1** | `setup/create-metasound.png` | Content browser and MetaSound Source asset creation. |
| **P2** | `graphs/graph-acoustic-obstruction.png` | Capture complete working graph for this recipe; zoom for legibility. |
| **P2** | `graphs/graph-material-footsteps.png` | Capture complete working graph for this recipe; zoom for legibility. |
| **P2** | `graphs/graph-projectile-flyby.png` | Capture complete working graph for this recipe; zoom for legibility. |
| **P2** | `graphs/graph-random-sequence.png` | Capture complete working graph for this recipe; zoom for legibility. |
| **P2** | `graphs/graph-randomized-one-shot.png` | Capture complete working graph for this recipe; zoom for legibility. |
| **P2** | `nodes/node-acoustic-paths.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-atmosphere-absorption.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-distance-delay.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-distance-switch.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-distance-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-doppler-ratio.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-dynamic-propagation.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-early-reflections.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-float-smoother.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-flyby-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-impact-dynamics.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-layered-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-material-transmission.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-physmat-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-random-sequence-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-random-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-sequence-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-shuffle-bag-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-source-directivity.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-surface-wave-player.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-trigger-cooldown.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |
| **P2** | `nodes/node-trigger-probability.png` | Capture full native node with key inputs/outputs and representative non-sensitive values. |

## Capture standards

- Prefer **real UE5.8.4 Editor screenshots**, not generated imitations of a node UI.
- Use a consistent editor theme and a practical zoom level. Node pins/text should remain readable at 1280px website width.
- PNG for diagrams/Editor screens; JPEG or WebP for heavy gameplay scenes if desired.
- Crop blank canvas; keep relevant context when showing a workflow.
- Hide personal paths, emails, license data and debugging overlays.
- Filenames are lowercase hyphenated and should match the exact Markdown reference.
- Capture your source graph **after** testing the final shipping plugin.
