# Propagation — distance and motion

When we see an explosion far away, the light arrives almost immediately while the sound takes time. A moving vehicle can change the apparent pitch and travel time of its sound. These nodes provide controllable approximations of those behaviours.

**[Distance Delay](nodes/propagation/distance-delay.md)** is suited to events where a chosen distance can be latched into a travel-time delay. **[Dynamic Propagation](nodes/propagation/dynamic-propagation.md)** is designed for continuously updated distance and includes smoothing and jump handling.

**[Doppler Ratio](nodes/propagation/doppler-ratio.md)** outputs a control value based on radial motion; it does not render audio by itself. **[Atmosphere Absorption](nodes/propagation/atmosphere-absorption.md)** adjusts how frequencies are lost with travel through air.

## Use the right physical quantities

A **radial velocity** is movement *toward or away from* the listener; total movement speed is not sufficient on its own. A **distance** supplied in centimetres must be converted to metres where a model explicitly expects metres. A sound travelling through air cannot meaningfully exceed the delay buffer that its node allocated.

!!!tip A good first test
Use a clean, short impact and an explicit `Distance (cm)` input with Distance Delay. Once that sounds correct, move to Dynamic Propagation and a moving-source recording.
!!!

[Browse the Propagation reference](nodes/propagation/README.md) · [Units and terminology](../getting-started/requirements.md)
