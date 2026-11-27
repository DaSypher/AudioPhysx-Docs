# Propagation: when sound takes time to reach us

Propagation concerns how a sound changes while travelling from its source to the listener. In the real world, an explosion heard at a great distance arrives after its flash, and a moving source can exhibit Doppler shift. In a game, these effects must be balanced against latency, memory and the fact that the level geometry and player motion may update suddenly rather than continuously.

[Distance Delay](nodes/propagation/distance-delay.md) captures a travel-time delay based on distance and sound speed. It works well for discrete events whose distance can be latched. [Dynamic Propagation](nodes/propagation/dynamic-propagation.md) changes the delay continuously for a moving source and includes smoothing and jump handling to keep the audible result controlled. Both are stereo DSP nodes and maintain separate channel delay histories.

[Doppler Ratio](nodes/propagation/doppler-ratio.md) computes a pitch multiplier from relative radial motion. It does not output audio—there is no reason to manufacture left and right audio channels for a single numeric ratio. Use it when another playback stage needs a pitch control, and avoid applying it again to a sound whose Dynamic Propagation has already introduced Doppler-like movement.

[Atmosphere Absorption](nodes/propagation/atmosphere-absorption.md) adjusts high-frequency content according to travelled distance and environmental conditions. It is separate from a wall-transmission filter and separate from ordinary source volume attenuation. In some projects Unreal's own air absorption may already be active, so compare the complete chain before using both systems together.

These are physically motivated **approximations**, not guaranteed measurements of the acoustic field in your level. A reliable design uses the right units and limits processing to what the listener can actually perceive. The individual references discuss centimetres, metres per second and buffer capacities in detail.
