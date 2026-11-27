---
label: "AP: Sequence Wave Player"
icon: file
order: 98
---

# AP: Sequence Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

Play several recordings one after another, using the recordings themselves to determine when each step should advance.

<!-- IMAGE SLOT: docs/static/images/nodes/node-sequence-wave-player.png -->

## Understanding the behaviour

The Sequence Wave Player is a completion-driven sound arranger. It exposes an expandable set of individual `Wave` inputs, and the node works through them in their authored order. When one playable recording finishes, the next begins. This is fundamentally different from adding a trigger delay of a fixed number of milliseconds: changing a recording's duration does not require you to maintain a parallel list of manual delays.

The source now supplies two audio outputs. If your click, motor and release recordings were authored in stereo, their left/right differences remain available across the entire sequence. A fixed sequence is not a multi-layer mixer; the intention is that one ordered element follows another.

A useful example is a mechanical lock: a short button press, the mechanical motor opening the mechanism, then a final latch sound. The game only issues one start event. The player takes care of the boundaries between the elements, making it easier to replace a middle recording without breaking the timing of the last.

This is also a good beginner node because it demonstrates the distinction between a trigger and an audio buffer. `Play` begins the operation, while `Out Left` and `Out Right` carry continuous audio until the sequence ends.

## Building and controlling the sound

In a stereo MetaSound Source, add the node and expand the sequence group to reveal the number of Wave Asset slots you need. Assign each recording in the order you want it played, then connect the Source's `On Play` to `Play`. Connect the two stereo outputs to the respective Source channels. With `Loop Sequence` disabled, connect `On Finished` to the Source completion pin when no other processor needs to play a tail.

Audition with a deliberately longer recording in the middle and verify that the third sound begins after it, not at a fixed elapsed time. `Play` again restarts the sequence; `Stop` explicitly cancels playback without claiming natural completion.

`Loop Sequence` repeats the complete set after the last playable entry. That can make sense for a repetitive machine pattern, but it is not a held gun trigger or a release phase. `On Finished` is meaningful for a non-looping pass after the final recording has naturally ended. For sustained gunfire with a stop-triggered outro, prefer the specialized Start Loop End Player.

**Practical limitations.** This node does not randomly choose the contents of its steps: the selected Wave Asset for each slot is fixed in the graph. If you need an ordered action with a different take at each phase, use Random Sequence. If recordings must overlap rather than follow completion, use Layered Wave Player. These distinctions matter more for believable sound design than the number of pins on the nodes.


==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Play the wave sequence from the beginning. Retriggering restarts it.
- **`Stop`** — *Trigger*. Stop playback immediately, without firing On Finished.
- **`Loop Sequence`** — *Boolean*. Restart from the first valid wave after the last finishes.
- **`Wave`** — *Wave Asset*. Wave Asset to play in sequence. Add or remove Wave slots on the node.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Stereo audio output from the currently playing wave.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Fires once after the last wave finishes naturally (when not looping).

===

**Related:** [Random Sequence Wave Player](random-sequence-wave-player.md) for randomized variation within each step.
