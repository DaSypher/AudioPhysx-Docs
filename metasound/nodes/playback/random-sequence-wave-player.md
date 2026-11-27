# AP: Random Sequence Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

A predictable beginning, middle and end—but with fresh recording choices inside every stage.

## Understanding the behaviour

Random Sequence combines two ideas: ordered playback and random variation. Each expandable step receives a **Wave Asset Array**, not one Wave Asset. When the player reaches a step, it selects a playable member of that array, plays it to completion, and then advances to the next step. The number of stages and the recordings inside each stage are two separate design decisions.

This lets you build recognizably structured events without every repetition sounding identical. Because the outputs are now `Out Left` and `Out Right`, both the chosen recording and the change from one stage to another can retain genuine stereo content. The selection is made when a stage begins; it is not a continuous shuffle of a playing recording.

Consider opening a sci-fi container. You always want an authorization beep, a motor action and a seal release, but you recorded several different beeps, motor passes and sealing noises. Three ordered arrays give you the same functional sequence every time while avoiding the exact same combination of sounds on every interaction.

This works particularly well for repeated gameplay interactions where the timing depends on the actual recordings. You do not need to enter the motor duration anywhere in the graph: the next phase follows playback completion.

## Building and controlling the sound

Add the player to a stereo MetaSound Source. Expand the sequence-step group to three steps and give each `Waves` input an array appropriate to that stage. Connect the starting trigger to `Play` and the stereo channels to the Source output. Keep `Loop Sequence` disabled for a one-shot action, then check that `On Finished` occurs after the last chosen clip completes.

For a useful test, create arrays with distinct recordings of different lengths. Trigger the action several times and check that it always visits all available stages in the intended order. Empty or unplayable step entries are handled by the player's fallback/skip logic, so missing content can shorten the audible result.

`Loop Sequence` repeats the whole collection of stages, not just the last recording. `Stop` immediately stops the action without emitting the natural-completion trigger. The node's previous-selection tracking can reduce obvious immediate repetition when there are multiple valid members; it is not intended as a guaranteed shuffle-bag cycle.

**Practical limitations.** Make sure each array contains recordings belonging to the same functional stage. A long release sample accidentally placed in the middle-stage array will delay the final stage by its full length. Likewise, the node cannot automatically synchronize a mechanically meaningful animation; it schedules **audio** by audio completion, so gameplay effects that must coincide with particular subevents may still require event markers or explicit triggers.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Start the sequence. Play again to restart.
- **`Stop`** — *Trigger*. Stop immediately without On Finished.
- **`Loop Sequence`** — *Boolean*. Restart after the final recording.
- **`Waves`** — *Wave Asset Array*. A Wave Asset Array for this expandable step.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Audio from the current step.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Fires after all playable steps finish.

===

**Related:** [Sequence Wave Player](sequence-wave-player.md) for a fixed sequence without per-stage randomness.
