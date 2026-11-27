# Acoustics — change the character of sound

These nodes are for effects that can make the **same recording** behave differently in different spaces, behind different materials or at different listener positions. They are useful where another random recording is not enough.

## Sound passing through a barrier

[Material Transmission](nodes/acoustics/material-transmission.md) uses an obstruction state and frequency-dependent losses to produce a muffled, transmitted sound. Use it for a simple, authored blocked/unblocked effect. [Acoustic Paths](nodes/acoustics/acoustic-paths.md) instead consumes the selected route from the world solver, including route delay and three-band loss.

## Sound arriving in a space

[Early Reflections](nodes/acoustics/early-reflections.md) suggests the first short echoes from nearby surfaces. It uses a lightweight model controlled by room size and damping, not real-time geometric reconstruction.

## Where the source faces

[Source Directivity](nodes/acoustics/source-directivity.md) shapes loudness and brightness as the listener moves from a source's front to its rear. It needs source-listener orientation information from the game.

## How strongly something is hit

[Impact Dynamics](nodes/acoustics/impact-dynamics.md) turns an impact event plus a strength value into filtered and transient-shaped playback. It is an audio processor, not an impact detector.

!!!warning Avoid accidental double-processing
Unreal attenuation and other environmental effects can also apply occlusion, air absorption and directivity. Compare the complete signal path before stacking several strong filters.
!!!

[Browse the Acoustics reference](nodes/acoustics/README.md) · [Try the obstruction recipe](../examples/acoustic-obstruction.md)
