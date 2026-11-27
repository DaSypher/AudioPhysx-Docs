# Querying sound routes through the level

A line from source to listener may be clear, obstructed by a wall or partly bypassed through an opening. AudioPhysx provides a game-thread acoustic path solver to estimate how these possibilities affect the sound. The result is deliberately separate from the MetaSound render thread: scene traces and geometry queries belong with the game world, while stereo DSP nodes process the returned control values.

The Blueprint library exposes **`AP: Query Acoustic Path`**, taking a world context, source location, listener location and optional source actor. Its result describes obstruction state, surface type, barrier count, acoustic-material use and measured thickness, plus direct-path delay and low/mid/high losses. It can additionally describe an around-obstacle candidate, including a possible emitter position and its estimated delay and frequency losses.

## Understand validity and selection

A particularly important distinction is **`bAroundPathValid` versus `bAroundPathSelected`**. Valid means the solver found a candidate. Selected means it considers that candidate preferable according to the available losses and configuration. The corresponding [Acoustic Paths MetaSound node](../metasound/nodes/acoustics/acoustic-paths.md) renders one selected route rather than automatically duplicating the signal into direct and around channels.

For testing, build a small scene with a sound source, listener and a single blocking surface. Query with a clear path first, then move the listener behind the barrier. Print the obstruction flag, barrier count, direct delay and band losses. Once those results are understandable, add an opening or Acoustic Portal and inspect whether a valid and selected alternate route appears. These experiments reveal much more than immediately trying to tune filter parameters by ear.

## Use the result in MetaSound

The selected route contract passed to the audio processor is a compact four-value Float Array: **delay milliseconds, low loss dB, mid loss dB, high loss dB**. The order is part of the interface. Connect the stereo source signal to Acoustic Paths, feed the selected array, and route completion through the processor when it still has delayed audio to release. When hearing something odd, first confirm the exact four values printed from the world-side calculation.

Because world queries cost CPU time, AudioPhysx has per-tick scheduling and ray budgets. Querying every emitter every rendered sample would be inappropriate. Use managed update intervals and realistic emitter counts, profile packaged-game performance, and avoid assigning the highest query detail to effects whose difference cannot be heard in the final mix.
