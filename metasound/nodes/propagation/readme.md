# Propagation nodes

Propagation tools describe how travel time, relative motion and atmosphere change the sound. Some process stereo audio directly; Doppler Ratio produces a single Float because it is a mathematical control. Knowing which type you are using helps avoid doubling the same physical effect in the signal chain.

**[AP: Distance Delay](distance-delay.md)** — Delay a sound by its estimated travel time across an authored source-to-listener distance.

**[AP: Dynamic Propagation](dynamic-propagation.md)** — Model changing sound travel time from a moving source, with bounded pitch-like effects and protection against sudden position jumps.

**[AP: Doppler Ratio](doppler-ratio.md)** — Calculate a pitch multiplier from source and listener motion without rendering audio in the node itself.

**[AP: Atmosphere Absorption](atmosphere-absorption.md)** — Make distant audio gradually lose some of its high-frequency definition as it travels through air.

For a broader explanation, return to the [Propagation overview](../../propagation.md).
