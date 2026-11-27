# AP: Stereo to Mono

**AudioPhysx / QoL** · Unreal Engine 5.8.4 development source

A deliberate exit from a stereo AudioPhysx graph when the next stage needs one mono audio stream.

## Understanding the behaviour

AudioPhysx's updated playback and DSP nodes preserve two channels by default. That is useful for stereo recordings and creative effects, but some Source layouts and downstream processors expect a single audio buffer. **AP: Stereo to Mono** exists so you can decide exactly where that conversion happens instead of losing channel information early in the graph.

The converter reads `In Left` and `In Right` and writes one `Out Mono` buffer. Its math is intentionally simple: for each frame, the output is **0.5 × (Left + Right)**. If both input channels contain the same signal, the resulting mono level remains the same instead of doubling. There is no intentional delay or extra sample-buffer history introduced by the node.

Suppose your layered weapon effect combines stereo mechanical recordings, a left-biased recoil texture and a broad tail. You can build and evaluate that mix in stereo, then convert it to mono before a precisely positioned 3D source if that fits the game's spatialization design. This avoids forcing every upstream player and effect to operate in mono just because the final emitter has a point-source role.

It is also useful for compatibility with a mono-only signal processor. However, converting to mono always sacrifices some stereo spatial information, so it should be a conscious decision.

## Building and controlling the sound

Add `AP: Stereo to Mono` from **AudioPhysx → QoL** after the last stereo stage that needs both channels. Connect the source or processor's `Out Left` to `In Left` and `Out Right` to `In Right`. Then connect the converter's `Out Mono` to a mono MetaSound output or mono-only downstream node.

Start by testing a dual-mono signal, then a recording with different left/right content. Compare the folded-down result with the original stereo mix. If a strong instrument or effect disappears in mono, inspect phase relationships in the recording or layered chain before treating the converter as the cause.

There are only three audio pins: two inputs and one output. The node does not generate a trigger, does not select recordings and does not normalize loudness dynamically. Averaging is a conventional, conservative fold-down but not a universal perceptual mix algorithm. Material that is opposite in polarity between channels can cancel substantially or completely when summed.

**Practical limitations.** This converter is the **intentional exception** to AudioPhysx's stereo-output convention. Control-only QoL nodes still produce controls and triggers rather than stereo audio, while other audio-bearing playback and DSP nodes expose independent channel outputs. If you only have one channel from upstream, do not assume that connecting it twice recreates the missing stereo information.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Left channel of the stereo source.
- **`In Right`** — *Audio buffer*. Right channel of the stereo source.

**Outputs from the current C++ node definition**

- **`Out Mono`** — *Audio buffer*. Mono result: 0.5 * (Left + Right). Opposite-polarity content may cancel.

===

**Related:** [Stereo signal flow guide](../../../getting-started/stereo-routing.md) for when to retain or fold down stereo in Unreal.
