---
label: "AP: Distance Delay"
icon: file
order: 85
---

# AP: Distance Delay

**AudioPhysx / Propagation** · Unreal Engine 5.8.4 development source

Delay a sound by its estimated travel time across an authored source-to-listener distance.

<!-- IMAGE SLOT: site/static/images/nodes/node-distance-delay.png -->

## Understanding the behaviour

Sound travels through air at a finite speed. The Distance Delay node converts `Distance (cm)` and `Speed of Sound (m/s)` into a delay and passes the stereo input through buffered output. Unlike a free-running moving-source simulation, it supports an explicit `Relatch` trigger: you can capture a new travel time for an event rather than continuously scrubbing the buffer as the source moves.

Both audio channels have their own delay history. This preserves a stereo recording's internal differences instead of applying an early mono sum. The delay length is common to Left and Right, because the node models one general source-listener separation rather than calculating a different physical path for each ear.

A distant explosion is a classic example. The visual flash is visible almost immediately, but the sound arrives noticeably later. If the game already knows the distance at the moment of the event, you can latch that value and allow the recording to travel through the buffer. A larger distance should produce a longer wait, without requiring you to write a Blueprint Delay node whose duration you maintain separately.

This is an audio-propagation control, not an attenuation or room model. A real distant explosion may also need appropriate recording perspective, air absorption and environmental effects.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Prepare a stereo sound and delay processor
Create a stereo Source with a short impact Wave Player, and insert **AP: Distance Delay** after the player.

>>> 2. Wire both audio channels
Connect the player Left/Right outputs to `In Left`/`In Right`, and route the delay processor `Out Left`/`Out Right` to the Source.

>>> 3. Set distance and physical speed
Set `Distance (cm)` in Unreal centimetres and `Speed of Sound (m/s)` in metres per second. The intended travel time is distance in metres divided by the speed of sound.

>>> 4. Set capacity and request a latch
Choose `Max Delay (s)` large enough for your scenario before the graph starts. Trigger `Relatch` when you want to capture the current distance-derived delay.

>>> 5. Compare delayed and direct events
Audition the original impact and the delayed one from a greater distance. Avoid adding a second manual delay elsewhere without accounting for the combined result.
>>>

<!-- IMAGE SLOT: site/static/images/graphs/setup-distance-delay.png -->

**After the basic setup:** Create a stereo MetaSound Source, feed a Wave Player's Left and Right outputs into the Distance Delay inputs, and supply a distance in Unreal centimetres and sound speed in metres per second. Choose `Max Delay (s)` large enough for the most distant audible source you intend to represent. When the event's location is known, trigger `Relatch` to calculate the delay and discard any older pending tail according to the documented behaviour.

Compare a short sample at a near distance with the same sample at a much greater distance. Listen for increased arrival time, not pitch change. Keep the Source alive until delayed audio has finished; the node itself does not supply a separate `On Finished` trigger.

`Max Delay (s)` is a **capacity allocation** made when the operator is constructed; increasing it consumes additional memory for each instance. `Relatch` recalculates the current propagation delay and clears a previous pending tail rather than mixing two unrelated event histories. The node is intended for a captured distance, so use Dynamic Propagation when the sound path should evolve continuously during playback.

**Practical limitations.** Unreal distances are normally in centimetres; sound speed here is explicitly metres per second. Incorrect conversion can create a delay off by a factor of 100. Be mindful of total time when a Wave Player, an acoustic path processor and a manually delayed gameplay event are all present; applying the same travel delay several times can make the result unrealistically late.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Stereo audio input.
- **`In Right`** — *Audio buffer*. Right audio channel to process.
- **`Distance (cm)`** — *Float*. Distance travelled by sound in Unreal centimetres. Sampled only when latched.
- **`Speed of Sound (m/s)`** — *Float*. Propagation speed in metres per second.  Default 343 m/s. Converted internally to cm/s.  Sampled only when latched.
- **`Max Delay (s)`** — *Float*. Maximum delay capacity in seconds (0.01-10). Allocated when the operator is constructed.
- **`Relatch`** — *Trigger*. Recalculate propagation delay and discard the previous pending audio tail.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Delayed stereo audio.
- **`Out Right`** — *Audio buffer*. Right audio channel after processing.

===

**Related:** [Dynamic Propagation](dynamic-propagation.md) for a moving source with continuously changing distance.
