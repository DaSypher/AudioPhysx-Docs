---
label: Acoustic obstruction
icon: play
order: 84
---
# Make a sound believable behind a wall

**Goal:** Have a mono sound change its tone and apparent arrival when the path between source and listener becomes obstructed.

A hard on/off mute is rarely convincing. Even when an object blocks line of sight, some sound can transmit through the barrier or reach the listener by another route. AudioPhysx gives you two levels of control depending on whether the game already has acoustic path data.

## Choose an approach

+++ Simple authored transmission

Use [AP: Material Transmission](../metasound/nodes/acoustics/material-transmission.md) when you can provide an `Obstructed` Boolean plus designer-authored frequency losses. This is the easiest demonstration: toggle one state and hear a darker, quieter sound.

+++ World-selected route

Use [AP: Acoustic Paths](../metasound/nodes/acoustics/acoustic-paths.md) when the Blueprint/world solver supplies a four-value selected-route array. It can represent delay and three-band loss for the preferred direct or around-obstacle route.

+++

## Build a controlled listening test

>>> 1. Choose a clear source
A spoken phrase or a short repeated impact with some high-frequency content makes obstruction changes easy to hear.

>>> 2. Establish the unobstructed reference
Play it in an open path with no extra obstruction treatment. Adjust your game attenuation separately if necessary.

>>> 3. Apply one obstruction method
Wire the appropriate node and its controls. Compare clear and blocked values, keeping the recording itself unchanged.

>>> 4. Check completion
If the selected processor can delay the audio, use its completion output so the tail isn't cut off when the original Wave Player finishes.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/graph-acoustic-obstruction.png -->

## Listen critically

If the obstructed version sounds like someone turned the volume down but left all the sharp high frequencies untouched, it probably needs more spectral coloration. If it becomes completely dull, examine whether you're applying both Unreal occlusion and full-strength AudioPhysx transmission loss.

[Acoustic path queries](../blueprint/acoustic-paths.md)
