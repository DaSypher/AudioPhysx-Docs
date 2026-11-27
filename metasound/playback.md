# Playback nodes

AudioPhysx includes several playback patterns. Select the simplest one that fits the sound design; do not use a complex multi-voice player when a single Wave Player is enough.

| Node | Intended use |
| --- | --- |
| AP: Distance Wave Player | Playback with distance-related control. |
| AP: PhysMat Wave Player | Select recording(s) from physical material context. |
| AP: Random Wave Player | Random variation selection. |
| AP: Surface Wave Player | Surface-based wave selection. |
| AP: Shuffle-Bag Wave Player | Non-repeating shuffled variation selection. |
| AP: Layered Wave Player | Trigger multiple audio layers. |
| AP: Sequence Wave Player | Play individual waves in order, automatically. |
| [AP: Random Sequence Wave Player](random-sequence.md) | Play one random wave from each ordered wave-array step. |
| [AP: Start Loop End Player](start-loop-end.md) | Play intro, repeating middle, and release/tail waves. |
| [AP: Flyby Wave Player](flyby.md) | Whizz/crack variations driven by flyby parameters. |

> TODO: Add exact pin tables and runtime examples for the first six nodes after comparing with the final shipping source and auditioning each node.
