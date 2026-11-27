# AP: Dynamic Propagation

**AudioPhysx / Propagation** · Unreal Engine 5.8.4 development source

Model changing sound travel time from a moving source, with bounded pitch-like effects and protection against sudden position jumps.

## Understanding the behaviour

A vehicle approaching and receding changes the distance sound must travel while the recording is playing. Dynamic Propagation accepts a changing `Distance (cm)` and updates a delay buffer in response. Adjusting playback travel time can create a Doppler-like change in perceived pitch, so the node includes smoothing, a maximum permitted Doppler change and handling for abrupt distance jumps.

This is not the same as merely reducing volume with distance. The node changes the timing of audio samples reaching the listener. The current stereo implementation maintains separate channel delay histories so both recorded channels move through the same propagation model without being summed together.

Imagine an engine recording attached to a fast-moving car. As it approaches, the sound path gets shorter; as it drives away, the path lengthens. The player may hear a controlled movement in pitch and arrival timing. Now teleport the car to a distant location: a naïve delay buffer could click or scrub wildly, which is why jump detection and crossfading are exposed as controls.

Use a fairly constant recording for the first test. If the source contains rapid, unrelated pitch modulation, it is harder to judge whether the propagation effect itself behaves sensibly.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Create a moving-sound stereo graph
Start with a sustained engine or moving-object recording and put **AP: Dynamic Propagation** between its stereo Wave Player and the Source outputs.

>>> 2. Wire stereo input and output
Connect Left/Right separately through the propagation processor. This node processes actual audio, unlike Doppler Ratio, which outputs only a control value.

>>> 3. Drive the current distance
Feed `Distance (cm)` from a changing source/listener measurement, or adjust a test Float manually. Supply `Speed of Sound (m/s)` and set `Max Delay (s)` capacity at initialization.

>>> 4. Smooth movement and discontinuities
Adjust `Smoothing (ms)` and `Max Doppler (%)` for ordinary motion. Set `Jump Threshold (cm)` and `Jump Crossfade (ms)` so teleport-like changes do not create harsh audio discontinuities.

>>> 5. Test approach, departure and teleport
Move the source toward and away from the listener, then jump it suddenly. Monitor `Doppler Ratio` only for diagnosis or separate use; do not apply the same pitch effect a second time without a deliberate design reason.
>>>

**After the basic setup:** Feed a stereo engine recording into `In Left` and `In Right`, and supply a continually updated source-listener distance. Begin with a realistic `Speed of Sound (m/s)`, a sufficiently large `Max Delay (s)` and moderate `Smoothing (ms)`. Move the listener steadily toward and away from the source, then deliberately test a large instantaneous distance change.

Monitor the `Doppler Ratio` diagnostic output when debugging unusual pitch movement. Because Dynamic Propagation already creates a Doppler-like result through its changing delay, that diagnostic ratio should not be applied again to the same sound as an additional pitch shift unless the exaggeration is deliberate.

`Max Doppler (%)` bounds the audible shift, `Jump Threshold (cm)` sets the displacement considered a discontinuity, and `Jump Crossfade (ms)` reduces abrupt changes around those discontinuities. `Smoothing (ms)` responds to ordinary small movements. `Max Delay (s)` is fixed when the operator is created; very large values or many active sources increase allocated memory.

**Practical limitations.** This is an approximation. It is not a complete geometrical propagation engine, does not add source directivity by itself and does not replace Unreal spatialization. Avoid feeding a position that flips unpredictably between unrelated reference points; the node cannot manufacture physically continuous motion from inconsistent game data. Check whether Unreal's own Doppler setting is active before layering effects.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Stereo signal to propagate.
- **`In Right`** — *Audio buffer*. Right audio channel to process.
- **`Distance (cm)`** — *Float*. Source-listener distance in centimetres.
- **`Speed of Sound (m/s)`** — *Float*. Sound speed in metres per second; default 343.
- **`Max Delay (s)`** — *Float*. Maximum travel time, fixed at voice creation.
- **`Smoothing (ms)`** — *Float*. Smooths small distance changes; default 25 ms.
- **`Max Doppler (%)`** — *Float*. Maximum pitch deviation; default 20 percent.
- **`Jump Threshold (cm)`** — *Float*. Large distance changes crossfade instead of scrubbing.
- **`Jump Crossfade (ms)`** — *Float*. Crossfade duration; default 40 ms.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Stereo audio after travel-time delay.
- **`Out Right`** — *Audio buffer*. Right audio channel after processing.
- **`Doppler Ratio`** — *Float*. Diagnostic pitch ratio. Do not apply again.

===

**Related:** [Doppler Ratio](doppler-ratio.md) if you only need a control value for another player.
