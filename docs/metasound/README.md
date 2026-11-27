---
label: MetaSound nodes
icon: pulse
order: 90
---
# MetaSound node library

AudioPhysx extends MetaSounds with native C++ nodes for **playing**, **processing** and **controlling** sound. Choosing the right category is easier when you begin with the question you want your audio to answer.

## I want to play recordings more intelligently

Do you need a random variation? A guaranteed order? Multiple simultaneous layers? A start/hold/end action? Explore [Playback](playback.md), which contains the integrated Wave Players.

[!card layout="compact" title="Playback" text="Variations, sequences, layers, distance bands, physical materials, gunfire and flybys."](playback.md)

## I want the room or material to change the sound

You may need a filter, transmission model, directivity effect or reflection taps rather than another recording. Those tools are under [Acoustics](acoustics.md).

[!card layout="compact" title="Acoustics" text="Obstruction, selected routes, impact shaping, reflections and orientation."](acoustics.md)

## I want motion and travel time to matter

When a source moves or becomes more distant, sound arrival and spectral balance can change. [Propagation](propagation.md) contains distance delay, Doppler-style control and atmospheric absorption.

[!card layout="compact" title="Propagation" text="Timing, Doppler ratios, moving-source delay and air absorption."](propagation.md)

## I want simpler trigger and control logic

Use [QoL](qol.md) for routing triggers, smoothing values and managing trigger repetition. These nodes generally do not decode Wave Assets.

[!card layout="compact" title="QoL" text="Distance branching, float smoothing, probability and cooldowns."](qol.md)

!!!tip How to read a node page
Every reference starts with **what happens**, then shows a **game-audio use case** and **wiring steps**. The exact pin list is folded away under **Full input reference** / **Full output reference** so you can still look up types without interrupting the explanation.
!!!

[Understanding completion](../getting-started/signals-and-completion.md) · [Blueprint integration](../blueprint/README.md)
