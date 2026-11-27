# QoL: fewer repeated control graphs

Not everything in AudioPhysx needs to process audio samples. Many MetaSounds become difficult to maintain because the same housekeeping logic is rebuilt repeatedly: a trigger should only pass every few hundred milliseconds, an occasional detail should only fire sometimes, or a filter parameter should move smoothly instead of jumping between values. The QoL nodes solve those narrow problems and can be connected to any suitable playback or processing chain.

[Trigger Cooldown](trigger-cooldown.md) limits how often an event can pass. [Trigger Probability](trigger-probability.md) accepts some events at a specified chance. [Float Smoother](float-smoother.md) conditions a block-rate numeric value using rise and fall response. [Distance Switch](distance-switch.md) routes a trigger into the appropriate distance band instead of embedding several nested branch nodes in every MetaSound. All four are intentionally control-only; they do not need stereo outputs.

The new [Stereo to Mono](stereo-to-mono.md) is the exception. It accepts `In Left` and `In Right` and emits `Out Mono` using a conservative average. This is useful because the other AudioPhysx audio nodes are stereo by default. If the end of a graph needs a mono audio buffer, you can explicitly place the converter there rather than giving up stereo content in the first Wave Player.

A good QoL graph should remain easy to read. For example, a gameplay event might pass through a short cooldown and then a probability gate before triggering an optional mechanical rattle. Each control has one job. Overusing them can conceal a gameplay bug just as easily as it can clean up an audio graph, so test the underlying events before adding complicated gating logic.

Every node in this category has its own sidebar entry and a **Build the sound — step by step** walkthrough with a named basic-setup screenshot location.
