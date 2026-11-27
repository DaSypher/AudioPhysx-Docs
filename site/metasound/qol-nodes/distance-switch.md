---
label: "AP: Distance Switch (Dynamic)"
icon: file
order: 78
---

# AP: Distance Switch (Dynamic)

**AudioPhysx / QoL** · Unreal Engine 5.8.4 development source

Choose which gameplay-audio branch should react to an event based on the current source-to-listener distance.

<!-- IMAGE SLOT: site/static/images/nodes/node-distance-switch.png -->

## Understanding the behaviour

Dynamic Distance Switch examines `Distance (cm)` when `Play` arrives and routes that trigger through one of several expandable distance ranges. It can also provide a gain value for the selected branch. Crucially, this node does **not** decode audio or mix stereo channels. The branches can point to any appropriate playback nodes, including the new stereo Wave Players, so the switch's output remains an event rather than a sound stream.

Dynamic groups let a graph designer add the needed ranges without having a fixed palette of near, medium and far pins in every project. The range boundaries and global maximum distance determine which route is selected or whether the request is out of range.

Imagine an explosion with three entirely different MetaSound chains: a close chain that includes mechanical debris, a midrange chain with more room reflections, and a distant chain with long air absorption. Distance Switch can trigger the correct chain at the moment of the explosion while leaving each chain free to use its own DSP and stereo mixing.

That is a different design choice from Distance Wave Player, which selects recordings and plays them within one integrated node. Use the switch when the entire graph branch, not just the Wave Asset, should change.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Make a stereo player for each range
In a Stereo MetaSound Source, add **AP: Distance Switch (Dynamic)** and two simple Wave Players, one representing a close sound and another a distant sound.

>>> 2. Create the distance bands
Expand the switch’s range entries and set the `Start Distance (cm)` values in ascending order. Provide `Max Distance (cm)` for the maximum evaluated range.

>>> 3. Supply the distance value
Connect a controllable Float to `Distance (cm)`. For a first test, choose values that clearly fall inside the close and far ranges.

>>> 4. Route dynamic triggers to players
Connect each range-specific `Play` output to its corresponding Wave Player `Play` input. Route the player Left/Right outputs through your chosen mix to the stereo Source output; the switch itself does not produce audio.

>>> 5. Check selection and range errors
Trigger the switch with `Play` at different distances. Observe `Selected Index` and optional `Out of Range` or `Invalid Ranges` outputs when troubleshooting; use the accompanying `Gain` control only if downstream playback/mixing is wired to consume it.
>>>

<!-- IMAGE SLOT: site/static/images/graphs/setup-distance-switch.png -->

**After the basic setup:** Configure the desired number of distance ranges and set their `Start Distance (cm)` values in ascending order. Supply the current source-listener distance, then connect the appropriate range `Play` output to each branch's starting trigger. If using the range `Gain` output, explicitly wire it into a compatible gain control; it does nothing acoustically unless the downstream signal chain consumes it.

Trigger at known distances and monitor `Selected Index`. The node provides `Out of Range` and `Invalid Ranges` diagnostic triggers, which help distinguish an intentionally unselected event from a malformed distance configuration.

`Max Distance (cm)` is the global outer cutoff. `Volume` specifies each range's gain multiplier; the corresponding output `Gain` exposes the selected branch's multiplier. The per-range `Play` outputs remain triggers. Since no audio buffers are processed here, there is no `Out Left` or `Out Right` pin to document or connect.

**Practical limitations.** Do not put incompatible or overlapping ranges into production without verifying the selection order. A wrong boundary can choose a surprising branch or raise `Invalid Ranges`. Keep large graphs maintainable by limiting the number of authored perspectives to real acoustic differences, rather than creating many arbitrary metre bands with almost identical processing.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Evaluate distance and trigger one range.
- **`Distance (cm)`** — *Float*. Source-to-listener distance in centimetres.
- **`Max Distance (cm)`** — *Float*. Maximum distance at which sound can start.
- **`Start Distance (cm)`** — *Float*. Distance at which this range becomes active.
- **`Volume`** — *Float*. Volume multiplier for this range.

**Outputs from the current C++ node definition**

- **`Play`** — *Trigger*. Triggers when this range is selected.
- **`Gain`** — *Float*. Volume multiplier for the selected branch.
- **`Out of Range`** — *Trigger*. Triggered when distance exceeds Max Distance.
- **`Invalid Ranges`** — *Trigger*. Triggered when range configuration is invalid.
- **`Selected Index`** — *Integer*. Selected range index, or -1 if rejected.

===

**Related:** [Distance Wave Player](../playback-nodes/distance-wave-player.md) if only the recording pool should change.
