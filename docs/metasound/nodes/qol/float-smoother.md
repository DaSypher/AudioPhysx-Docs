---
label: "AP: Float Smoother"
icon: file
order: 81
---

# AP: Float Smoother

**AudioPhysx / QoL** · Unreal Engine 5.8.4 development source

Turn abrupt control changes into more natural transitions without adding an audio filter to the signal.

<!-- IMAGE SLOT: docs/static/images/nodes/node-float-smoother.png -->

## Understanding the behaviour

Gameplay often updates a value less frequently than MetaSound renders samples. If a value jumps suddenly from low to high and feeds a gain or cutoff control, the audible effect can step harshly. Float Smoother responds to the current `Target` over time, with separate **rise** and **fall** time constants. This makes it possible to react quickly to increasing values but more gently to decreasing values, or vice versa.

The node operates on Float controls once per audio block. It is intentionally not an audio-bearing stereo node: `Smoothed` represents one number, not a left/right waveform. There is no benefit in manufacturing two channels for a shared control value.

An engine-load parameter is a useful example. Throttle input may jump suddenly when a key is pressed, but the perceived engine response should rise over a short period and fall more gradually on release. A smoother can prevent the filter cutoff or gain from snapping between unrelated sonic states. You can make the same choice for obstruction amount, room wetness, mechanical tension and other slowly changing controls.

Smoothing can improve believability, but too much smoothing makes sound feel disconnected from gameplay. The right times depend on the event.

## Building and controlling the sound

Connect the changing parameter to `Target` and route `Smoothed` to the downstream gain, cutoff, modulation or other Float input. Start with a short rise and a longer fall, then audition a sharp target change. Use `Snap` when you need the output to move immediately to the current target, such as after a teleport or an intentional reset.

Keep your graph simple by using one Smoother before several consumers when they should all respond to the same conditioned value. Avoid creating independent smoothers for the same source unless they genuinely need different time responses.

`Rise (ms)` applies when the target is above the current output; `Fall (ms)` applies when it is below. A zero time in a direction snaps immediately. `Snap` overrides the smoothing state for that block. Because `Smoothed` is block-rate, it should not be used as though it were a full audio-rate oscillating signal.

**Practical limitations.** When a sound crackles after parameter updates, identify whether the discontinuity is in a numeric control or in audio samples. This node helps the former; it cannot repair a damaged recording or replace a de-clicking DSP stage. Test rapidly moving values and scene resets to ensure the response does not lag behind meaningful gameplay state changes.


==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Target`** — *Float*. Float value to smooth. Sampled once per audio block.
- **`Rise (ms)`** — *Float*. Exponential time constant for increasing values. Zero snaps immediately.
- **`Fall (ms)`** — *Float*. Exponential time constant for decreasing values. Zero snaps immediately.
- **`Snap`** — *Trigger*. Immediately set the output to Target in this block (block-rate behaviour).

**Outputs from the current C++ node definition**

- **`Smoothed`** — *Float*. Rise/fall smoothed Float control signal (block-rate).

===

**Related:** [Trigger Cooldown](trigger-cooldown.md) for limiting event frequency instead of numeric changes.
