# QoL nodes

These utilities streamline graph control and channel routing. Most manipulate events or Float values rather than waveform data. Stereo to Mono is the exception: it deliberately converts left and right audio into one channel at the point where the sound designer asks for that conversion.

**[AP: Float Smoother](float-smoother.md)** — Turn abrupt control changes into more natural transitions without adding an audio filter to the signal.

**[AP: Trigger Cooldown](trigger-cooldown.md)** — Prevent bursts of nearly simultaneous gameplay events from becoming a wall of repeated sound.

**[AP: Trigger Probability](trigger-probability.md)** — Make optional sound details happen occasionally rather than on every gameplay event.

**[AP: Distance Switch (Dynamic)](distance-switch.md)** — Choose which gameplay-audio branch should react to an event based on the current source-to-listener distance.

**[AP: Stereo to Mono](stereo-to-mono.md)** — A deliberate exit from a stereo AudioPhysx graph when the next stage needs one mono audio stream.

For a broader explanation, return to the [QoL overview](../../qol.md).
