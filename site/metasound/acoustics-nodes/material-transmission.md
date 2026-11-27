---
label: "AP: Material Transmission"
icon: file
order: 89
---

# AP: Material Transmission

**AudioPhysx / Acoustics** · Unreal Engine 5.8.4 development source

Give an obstructed sound a believable tonal change rather than making it merely quieter.

<!-- IMAGE SLOT: site/static/images/nodes/node-material-transmission.png -->

## Understanding the behaviour

Sound transmitted through a door, wall or panel often loses more high-frequency detail than low-frequency weight. Material Transmission takes stereo audio and an externally supplied `Obstructed` Boolean, then applies a frequency-shaped loss model whose low/high loss values describe the material. Thickness and reference thickness provide a way to scale that treatment with the geometry represented by your game data.

The node is a DSP processor, not a raycaster. It cannot know that a wall exists unless a Blueprint, component or world path calculation supplies the obstruction state. Left and Right inputs are processed with separate filter histories so differences in a stereo recording are not forcibly collapsed. The broad obstruction amount, however, is controlled by the same material inputs for both channels.

Try a metal door between the player and a nearby machine. The unobstructed version should contain clear clicks and bright mechanical texture. When the door closes, a filtered version might retain some low rumble but lose much of the sharp top end. A small amount of leakage can preserve an audible sense that the machine is still present, especially if you have deliberately designed a thin or imperfect barrier.

This sounds more convincing than a volume-only change because the tonal balance communicates the idea of an intervening object. It can also communicate the quality of the material: a lighter partition and a heavy sealed wall should not have identical transmitted spectra.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Build a clear stereo reference
Play a short speech or impact recording through a stereo Wave Player and add **AP: Material Transmission** between the player and the Source output.

>>> 2. Route audio into transmission
Wire the player `Out Left`/`Out Right` into `In Left`/`In Right` and the processor `Out Left`/`Out Right` into the Source outputs.

>>> 3. Create a simple obstruction control
Start with a manually controlled Boolean connected to `Obstructed`, so you can audition the same sound in open and blocked states before adding level traces.

>>> 4. Dial in material losses
Set `Low Loss (dB)` and `High Loss (dB)` so the blocked sound loses more high frequencies than low frequencies. Adjust `Thickness (cm)`, `Reference Thickness (cm)` and `Crossover (Hz)` to explore the model.

>>> 5. Refine the transition and avoid double filtering
Toggle `Obstructed` while changing `Leakage (%)` and `Smoothing (ms)`. Only after this works should you drive it from the acoustic world. Check you are not simultaneously applying a second full-strength occlusion filter.
>>>

<!-- IMAGE SLOT: site/static/images/graphs/setup-material-transmission.png -->

**After the basic setup:** Start with a simple stereo Wave Player and connect its two channels to `In Left` and `In Right`. Expose `Obstructed` as a Boolean or feed it from your gameplay trace. Set modest `Low Loss (dB)` and larger `High Loss (dB)` values, then switch the state while the source loops. Add thickness scaling and leakage only after you can hear the basic blocked/unblocked distinction.

If the result is too abrupt when a door opens or closes, increase `Smoothing (ms)` until the change is audible but not clicky. Keep the final Source output stereo when preserving the recording's width is important; downmix only as part of an intentional spatialization strategy.

`Thickness (cm)` describes the authored obstacle thickness. `Reference Thickness (cm)` tells the model what thickness corresponds to the supplied loss values. `Crossover (Hz)` is the approximate division between the lower- and higher-frequency treatment. `Leakage (%)` blends some unobstructed audio back into the filtered signal; large values can undermine the impression of a solid barrier. `Smoothing (ms)` controls how quickly the attenuation changes rather than how long a sound travels.

**Practical limitations.** This is not a substitute for a measured transmission-loss spectrum, and it does not independently simulate flanking paths or diffraction around corners. If Acoustic Paths already applies three-band route loss, decide whether an extra Material Transmission stage adds meaningful information or simply applies the same attenuation twice. Listen to a range of recordings before committing one loss preset to every sound category.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Left channel of the stereo source audio.
- **`In Right`** — *Audio buffer*. Right audio channel to process.
- **`Obstructed`** — *Boolean*. True when the sound path is obstructed.
- **`Thickness (cm)`** — *Float*. Assigned obstacle thickness in centimetres.
- **`Reference Thickness (cm)`** — *Float*. Thickness at which the specified losses apply.
- **`Low Loss (dB)`** — *Float*. Low-band transmission loss at reference thickness.
- **`High Loss (dB)`** — *Float*. High-band transmission loss at reference thickness.
- **`Crossover (Hz)`** — *Float*. Approximate low/high frequency division.
- **`Leakage (%)`** — *Float*. Fraction of unobstructed audio mixed back in.
- **`Smoothing (ms)`** — *Float*. Smoothing time for changing transmission gains.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Stereo audio after transmission filtering.
- **`Out Right`** — *Audio buffer*. Right audio channel after processing.

===

**Related:** [Acoustic Paths](acoustic-paths.md) when the route and delay should come from the world solver.
