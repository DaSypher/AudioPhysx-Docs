---
label: "AP: Start Loop End Player"
icon: file
order: 95
---

# AP: Start Loop End Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

One sound can have a meaningful start, a repeating body, and a release that only plays when the action ends.

<!-- IMAGE SLOT: docs/static/images/nodes/node-start-loop-end.png -->

## Understanding the behaviour

Start Loop End is built around the lifecycle of a sustained action. Its three Wave Asset Arrays provide possible *start*, *middle*, and *end* recordings. A start trigger first plays an introductory variation when one is available, then enters the middle phase. When `Stop Firing` arrives, the node stops scheduling new middle events and transitions into a final recording. This separation is essential for weapons, continuous tools and machines that should not abruptly stop when a button is released.

The **RPM** input changes how the middle phase behaves. With `RPM = 0`, the next middle recording starts after the last one has finished—the older sequential mode. With positive RPM, new middle recordings are scheduled according to rounds per minute, even if older middle recordings are still audible. The current code uses a bounded pool of twelve middle voices for overlap. Both channels of each chosen recording are mixed to `Out Left` and `Out Right`.

For automatic gunfire, try a brief attack recording, several main shot variations, and one or more release recordings. At 600 RPM, the intended interval between middle-shot starts is 100 milliseconds. A recording that lasts 250 milliseconds can therefore overlap subsequent shots. That is fundamentally different from cutting each clip to 100 milliseconds or speeding it up to fit the firing cadence.

The same system can also describe a held industrial tool. Set RPM to zero for a completion-based repeating middle, and use an authentic winding-down recording when the player releases the control.

## Building and controlling the sound

Add the node to a stereo Source, provide `Start Waves`, `Loop Waves` and `End Waves`, and connect the weapon's pressed event to `Start Firing`. Connect the release event to `Stop Firing`; sending only the start event leaves the player in its sustained state. Connect the left and right outputs to the stereo Source, or downmix deliberately for a mono spatialized Source. Begin with 600 RPM and test how recorded clip duration changes the overlap.

Toggle `Immediate Release` while holding and releasing the action. With it enabled, currently active waves fade quickly and the end begins promptly. With it disabled, active recordings finish before the ending starts. `On Finished` is intended to signal completion of the released sequence, not to fire after each middle shot.

`RPM = 0` preserves sequential middle playback. A positive value is bounded by the implementation's supported range of 60–2400 RPM. This controls the start intervals, **not** the source playback speed. The code maintains a maximum of twelve middle voices; when every voice is occupied, a new scheduled shot is skipped instead of abruptly cutting another. `Immediate Release` changes release semantics but does not make existing recordings disappear retroactively unless the fade path is selected.

**Practical limitations.** Test starting and stopping in the middle of the introduction, releasing while several middle shots overlap, and retriggering while the ending is audible. Also test empty arrays and a long middle recording at high RPM to expose voice saturation. This is a playback scheduler, not a ballistic or weapons-logic system: gameplay still decides exactly when shots happen and when to send the release trigger.


==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Start Firing`** — *Trigger*. Play a random intro, then begin firing middle waves.
- **`Stop Firing`** — *Trigger*. Stop scheduling shots and enter the ending.
- **`Immediate Release`** — *Boolean*. True: fade active waves and play ending immediately. False: let all active waves finish before ending.
- **`RPM`** — *Float*. 0 = legacy sequential middle waves. 60-2400 = middle shots per minute, with overlap. Updated at shot boundaries.
- **`Start Waves`** — *Wave Asset Array*. Random intro wave array. If empty, start middle sounds immediately.
- **`Loop Waves`** — *Wave Asset Array*. Random middle wave array; RPM sets the interval between starts, not between completions.
- **`End Waves`** — *Wave Asset Array*. Random ending wave array.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Stereo mix output.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Fires when ending audio and any remaining shots have finished.

===

**Related:** [Automatic weapon walkthrough](../../../examples/automatic-weapon.md) for a practical setup.
