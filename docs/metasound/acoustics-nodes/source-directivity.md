---
label: "AP: Source Directivity"
icon: file
order: 88
---

# AP: Source Directivity

**AudioPhysx / Acoustics** · Unreal Engine 5.8.4 development source

Make the source sound different when the listener stands in front of it, beside it, or behind it.

<!-- IMAGE SLOT: docs/static/images/nodes/node-source-directivity.png -->

## Understanding the behaviour

Many sound sources radiate unevenly. A voice tends to carry more clarity in front of the speaker, while the rear of a device may attenuate sharp detail without fully eliminating its low-frequency body. Source Directivity receives stereo audio and a listener-relative `Angle (deg)`, then shapes the output according to the authored directivity strength, rear attenuation and frequency division.

The input angle must come from the game or another world-audio parameter system. The DSP node is not a position tracker, and it cannot deduce a source Actor's forward vector from the waveform. By retaining separate filter histories for Left and Right, the processing stage preserves stereo differences while applying a common source-orientation response.

Place a portable radio or loud mechanical generator in a test room. Walk around it in a circle with a steady recording playing. The front should have more presence while the rear sounds comparatively subdued. If you rotate the emitter itself, the apparent bright/dark pattern should rotate with it rather than being permanently aligned to the level.

This provides a useful layer of realism for sources with a meaningful forward-facing axis. It is less useful for a small spherical point source that should radiate almost equally in all directions.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Choose a directional sound
Use a voice, loudspeaker or machinery sound in a Stereo MetaSound Source. Add **AP: Source Directivity** after its stereo Wave Player.

>>> 2. Connect stereo audio correctly
Wire the Wave Player Left/Right into directivity `In Left`/`In Right`, and the processor Left/Right to the Source output.

>>> 3. Supply the facing angle
Control `Angle (deg)` manually at first: compare front-facing and rear-facing values. Later calculate the source-to-listener angle using gameplay/world orientation.

>>> 4. Tune the directional response
Increase `Directivity (%)` gradually and adjust `Rear Attenuation (dB)`. Use `Low Frequency Directivity (%)` and `Crossover (Hz)` to avoid removing too much bass behind the source.

>>> 5. Walk around the source and listen
When the manual test is convincing, connect a changing angle from your game and use `Smoothing (ms)` to prevent stepped changes. Compare with Unreal attenuation to avoid excessive double directivity.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/setup-source-directivity.png -->

**After the basic setup:** Connect a stereo Source or Wave Player to `In Left` and `In Right`, then supply the angle between the emitter's facing direction and the listener direction to `Angle (deg)`. Begin with a low `Directivity (%)` value and compare 0, 90 and 180 degree situations. Increase `Rear Attenuation (dB)` gradually rather than trying an extreme value first.

Tune `Low Frequency Directivity (%)` separately from the overall directional strength. If bass seems to disappear when the listener walks behind the source, make the low-frequency treatment less aggressive. Use `Smoothing (ms)` to reduce stepping when the input angle is updated at game-thread intervals.

`Angle (deg)` controls the facing relationship, `Directivity (%)` controls how pronounced the effect is, and `Rear Attenuation (dB)` sets a maximum rear loss. `Crossover (Hz)` separates the low and high frequency approximations. The node does not implement 3D panning by itself; Unreal's spatializer and attenuation system are still responsible for placing the sound in the world.

**Practical limitations.** Carefully check the source-forward convention and whether your game returns a signed or unsigned angle. A value that always describes absolute separation can be correct for a symmetric forward/back model, but a miscomputed vector can reverse the effect. Also avoid stacking this with another strong directivity configuration in the same Source without comparing the combined result.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Left channel of the stereo audio input.
- **`In Right`** — *Audio buffer*. Right audio channel to process.
- **`Angle (deg)`** — *Float*. Angle from the source forward direction  to the listener. 0 is front, 180 is rear.
- **`Directivity (%)`** — *Float*. Directivity strength, 0 to 100 percent.
- **`Rear Attenuation (dB)`** — *Float*. Maximum high-frequency attenuation at 180 degrees.
- **`Low Frequency Directivity (%)`** — *Float*. Fraction of high-frequency attenuation  applied to the lower frequencies.
- **`Crossover (Hz)`** — *Float*. Approximate low/high frequency division.
- **`Smoothing (ms)`** — *Float*. Smooth changes in directional attenuation.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Stereo audio after directional filtering.
- **`Out Right`** — *Audio buffer*. Right audio channel after processing.

===

**Related:** [Doppler Ratio](../propagation-nodes/doppler-ratio.md) for motion-induced pitch controls rather than facing direction.
