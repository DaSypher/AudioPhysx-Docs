---
label: "AP: Doppler Ratio"
icon: file
order: 83
---

# AP: Doppler Ratio

**AudioPhysx / Propagation** · Unreal Engine 5.8.4 development source

Calculate a pitch multiplier from source and listener motion without rendering audio in the node itself.

<!-- IMAGE SLOT: site/static/images/nodes/node-doppler-ratio.png -->

## Understanding the behaviour

The Doppler effect is a change in perceived frequency caused by relative movement along the line between source and listener. Doppler Ratio receives the source's velocity **toward** the listener and the listener's velocity **toward** the source, plus the speed of sound. From those controls it produces `Pitch Ratio`, a Float value suitable for a playback or modulation stage that accepts a linear pitch multiplier.

Unlike Dynamic Propagation, this node does not take `In Left` or `In Right`, and it does not output audio. It remains a control-only node despite the broader move to stereo, because a numerical ratio does not have independent audio channels. Changing a control-only node to emit stereo audio would add complexity without making its result more correct.

Picture a horn attached to a train moving toward a stationary listener. The relevant speed is how fast the horn's source is approaching *along the listener direction*, not merely how fast the train is travelling somewhere on the map. A vehicle driving sideways across the listener's line of sight can have a large total velocity but a much smaller radial velocity.

The same idea applies when the listener is moving. By supplying both toward-velocities you can model which party contributes to the perceived pitch change.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Start with a movement-driven source
Create a Stereo MetaSound Source containing a sustained playback sound such as a vehicle engine, then add **AP: Doppler Ratio** as a separate **control** node.

>>> 2. Supply radial motion rather than overall speed
Provide `Source Toward Listener (m/s)` and `Listener Toward Source (m/s)` in metres per second. The values should reflect motion directly toward/away from the other participant, not unsigned movement speed.

>>> 3. Supply a speed-of-sound reference
Set `Speed of Sound (m/s)` to your intended environment value. Check that the resulting `Pitch Ratio` changes as the source switches from approach to departure.

>>> 4. Apply the ratio using a compatible control
Use `Pitch Ratio` with a pitch-rate input designed for a **multiplier**. A pin in *semitones* is not equivalent; convert the ratio before connecting it to a semitone-based control.

>>> 5. Compare with built-in Doppler
Audition a smooth pass-by. If another node or Unreal attenuation already applies Doppler, avoid applying a second full-strength shift.
>>>

<!-- IMAGE SLOT: site/static/images/graphs/setup-doppler-ratio.png -->

**After the basic setup:** In Blueprint or your gameplay-side acoustic system, calculate signed radial velocity components in metres per second. Supply them to `Source Toward Listener (m/s)` and `Listener Toward Source (m/s)`. Positive values mean approaching, according to these pin labels. Use a sensible `Speed of Sound (m/s)` and connect the output ratio to a compatible playback-pitch control.

Check a stationary case first: the ratio should be near the neutral value. Then test approaching and receding motion and confirm the resulting multiplier changes in the expected direction. Some downstream pitch inputs use semitones rather than ratios, so check the receiving node's unit before making the connection.

`Pitch Ratio` is not an octave/semitone value and is not an audio buffer. The source's `Speed of Sound (m/s)` input defaults to an ordinary air value and sets the scale of the effect. No panning, attenuation, or travel delay is added in this node; it is a small mathematical part of a larger audio graph.

**Practical limitations.** Avoid calculating radial velocity from unsigned speed alone. That would not distinguish an approaching vehicle from one moving away. If you already use Dynamic Propagation for the same sound, applying the resulting ratio as a second pitch effect can exaggerate movement. Prefer one clear Doppler responsibility in the audio chain.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Source Toward Listener (m/s)`** — *Float*. Positive means source approaches listener.
- **`Listener Toward Source (m/s)`** — *Float*. Positive means listener approaches source.
- **`Speed of Sound (m/s)`** — *Float*. Default 343 m/s.

**Outputs from the current C++ node definition**

- **`Pitch Ratio`** — *Float*. Pitch multiplier for playback WITHOUT Dynamic Propagation.

===

**Related:** [Dynamic Propagation](dynamic-propagation.md) when you need a processed stereo stream.
