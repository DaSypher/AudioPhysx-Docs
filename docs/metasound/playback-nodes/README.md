---
label: "Playback"
icon: play
order: 95
---


# Playback: what should play, and when?

A convincing sound library needs more than a folder of recordings. It needs a clear decision about when an event begins, whether recordings overlap, how a variation is chosen, and when the audible result should actually end. AudioPhysx provides several players because these are genuinely different problems: an explosion can use a single variation, a machine may have a fixed mechanical sequence, and an automatic rifle needs a repeatable event cadence independent of individual recording duration.

**For one-shot variation**, start with [Random Wave Player](random-wave-player.md). It can choose a take whenever the game sends an event and allow limited overlap. If repeated events reveal the same recordings too often, [Shuffle-Bag Wave Player](shuffle-bag-wave-player.md) adds selection history. Both produce stereo audio but do not decide the gameplay timing of the input trigger.

**For structured actions**, use [Sequence Wave Player](sequence-wave-player.md) when every stage should play one specific recording, or [Random Sequence Wave Player](random-sequence-wave-player.md) when each stage can select one of several variations. These wait for the current recording to finish. [Layered Wave Player](layered-wave-player.md) instead combines several recordings at once, with optional per-layer delays, gain and pitch. That difference between sequential and simultaneous audio is fundamental to how the sound will feel.

**For held or context-dependent actions**, [Start Loop End Player](start-loop-end.md) manages an introduction, repeated middle and released ending. It now supports RPM-timed overlapping middle shots. [Distance Wave Player](distance-wave-player.md) chooses a recorded perspective using distance. [PhysMat Wave Player](physmat-wave-player.md) and [Surface Wave Player](surface-wave-player.md) choose content from material identity, while [Flyby Wave Player](flyby-wave-player.md) plays near-miss whizzes and optional cracks using data supplied by the flyby subsystem.

All ten Wave Players now expose **`Out Left` and `Out Right`**. That is a capability, not an instruction to make every source a wide stereo emitter. A localized footstep or weapon report may be better downmixed before 3D positioning, whereas a designed ambience or layered interface effect might benefit from keeping stereo intact. The [stereo routing guide](../../getting-started/stereo-routing.md) covers both cases.

[Explore the individual Playback references](README.md)


Every node in this category has its own sidebar entry and a **Build the sound — step by step** walkthrough with a named basic-setup screenshot location.
