# AP: Acoustic Paths

**AudioPhysx / Acoustics** · Unreal Engine 5.8.4 development source

Render the single acoustic route selected by the world solver, including travel delay and frequency-dependent loss, without creating duplicate sound copies.

## Understanding the behaviour

The Acoustic Paths node receives stereo audio and a compact `Selected Route` Float Array. That array contains four values in a strict order: **delay in milliseconds, low-band loss in decibels, mid-band loss, and high-band loss**. It is normally supplied by the AudioPhysx game-thread path system through `AP.AcousticRoute.Selected`. The solver decides which route is appropriate; this MetaSound node turns that selected route into audible delay and spectral reduction.

The distinction between **direct** and **around-obstacle** sound matters. When an opening provides a better path, the system can prefer that route over heavily transmitted sound through a barrier. The current audio node applies one selected route rather than playing two simultaneous copies of the source. Separate channel histories preserve differences between Left and Right while the same route data controls their acoustic treatment.

Imagine a radio playing behind a heavy wall with an open doorway nearby. A direct line to the listener might intersect the wall and require substantial high-frequency loss, while the route through the doorway might travel farther but preserve more clarity. Rather than choosing based solely on the shortest distance, an acoustic routing system can compare available route losses and select the preferred listening result.

This approach is particularly effective when the sound designer wants perceptual plausibility without asking the audio renderer to perform geometry queries. The world solver works on a scheduled game-thread budget; the MetaSound processor simply receives already calculated values.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Start with a known-good stereo recording
Create a Stereo MetaSound Source and play a simple sound from an AudioPhysx Wave Player. Add **AP: Acoustic Paths** after the player, not instead of it.

>>> 2. Wire the two audio channels independently
Connect the player’s `Out Left` to `In Left` and `Out Right` to `In Right` on Acoustic Paths. Route the processor’s `Out Left`/`Out Right` to the Source outputs.

>>> 3. Provide a test route manually
Before adding level geometry, build a Float Array for `Selected Route` with exactly four values: `[delay in ms, low loss dB, mid loss dB, high loss dB]`. Start with `[0, 0, 0, 0]` and then change high-band loss or delay to hear the difference.

>>> 4. Connect finishing through the effect
Wire the Wave Player `On Finished` to Acoustic Paths `Source Finished`. If this processor is last, connect the Acoustic Paths `On Finished` to the Source completion so the delayed tail can finish.

>>> 5. Test world-driven routing second
After the authored route works, supply `AP.AcousticRoute.Selected` from the Acoustic Path Blueprint/world helper. Compare open and obstructed positions; check the actual route array first if the sound is unexpectedly muffled.
>>>

**After the basic setup:** Connect your stereo player outputs to `In Left` and `In Right`. Supply the compact `Selected Route` array from the relevant acoustic interface or Blueprint-managed source. Pass the player's `On Finished` into `Source Finished` rather than ending the MetaSound Source immediately, and use the Acoustic Paths node's `On Finished` output for final completion when its delayed tail is the last thing audible.

Begin by testing a clear route with near-zero loss and delay, then feed deliberately larger high-band loss and a controlled delay. Listen on headphones to confirm both stereo channels remain independent. Only after the hand-authored test works should you connect the world solver and start debugging barriers or portals.

`Smoothing (ms)` limits sudden audible changes when the selected route updates. `Delay Capacity (ms)` reserves the processor's delay memory **when the operator is created**. The source documents a compact 128 ms default and recommends a larger 1500 ms capacity only where long cinematic travel time is required. Changing the capacity pin while the graph is running does not resize already allocated storage. The route itself uses positive loss values in decibels, and its array order must never be guessed.

**Practical limitations.** A selected route is only as good as the geometry and acoustic material data supplied to the solver. If the sound is far too muffled, print the path result before trying random filter values. If there is a separate Unreal occlusion or transmission effect downstream, check that you are not double-attenuating the same bands. With a delayed signal, careless completion wiring can cut off the final samples even though the original Wave Player has already finished.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Left channel of the stereo audio to propagate.
- **`In Right`** — *Audio buffer*. Right audio channel to process.
- **`Source Finished`** — *Trigger*. Wave Player On Finished; passed through after the path tails.
- **`Selected Route`** — *Float Array*. Float Array from AP.AcousticRoute.Selected: delay ms, low/mid/high loss dB. Route selection occurs on the game thread.
- **`Smoothing (ms)`** — *Float*. Smooth path loss and delay changes.
- **`Delay Capacity (ms)`** — *Float*. Delay buffer capacity allocated ONCE at graph creation. Default 128 ms; raise to 1500 ms only if long cinematic propagation is required. Changes during playback cannot grow the buffer.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Only the selected, delayed and filtered acoustic path.
- **`Out Right`** — *Audio buffer*. Right audio channel after processing.
- **`On Finished`** — *Trigger*. Triggered after the longest queued acoustic path tail.

===

**Related:** [Acoustic path queries](../../blueprint/acoustic-paths.md) for the world-side calculation.
