---
label: "AP: Atmosphere Absorption"
icon: file
order: 82
---

# AP: Atmosphere Absorption

**AudioPhysx / Propagation** · Unreal Engine 5.8.4 development source

Make distant audio gradually lose some of its high-frequency definition as it travels through air.

<!-- IMAGE SLOT: docs/static/images/nodes/node-atmosphere-absorption.png -->

## Understanding the behaviour

Air transmission can change the character of a sound even when no wall or other obstacle exists between source and listener. Atmosphere Absorption uses travelled distance together with temperature, humidity and pressure to estimate frequency-dependent losses. The audible goal is a controlled reduction in brightness as the path grows longer, rather than simply moving the volume slider down.

The stereo version accepts `In Left` and `In Right` and produces `Out Left` and `Out Right`. Each channel is processed using its own audio history while the environmental controls remain shared. That means stereo ambience or an authored wide sound can retain its left/right differences through the frequency shaping.

Try a short crisp impact or a mechanical sound with noticeable high-frequency content. Compare a near distance with a much larger one, leaving the Wave Asset unchanged. At a longer path, you should expect the very bright content to be less pronounced. You can then adjust the atmospheric conditions and hear how the approximate absorption model responds.

In a game, this effect can complement distance-recording choices. A distant weapon tail is not just a close gunshot made quieter, so use appropriate source material as well as DSP when the perspective change matters.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Create a bright stereo test signal
Use a crisp impact or noise-rich recording through an AudioPhysx stereo Wave Player. Add **AP: Atmosphere Absorption** after the player.

>>> 2. Connect the stereo signal path
Connect player `Out Left` and `Out Right` into `In Left`/`In Right`, then connect the processor `Out Left`/`Out Right` to the stereo Source outputs.

>>> 3. Begin with a short travel distance
Supply `Distance (cm)` using Unreal centimetres. Start close so the sound resembles the original recording before testing long-distance absorption.

>>> 4. Set environment conditions
Provide values for `Temperature (C)`, `Humidity (%)` and `Pressure (kPa)` that reflect your level’s intended atmosphere. Do not treat the controls as artistic volume knobs only.

>>> 5. Compare near and far playback
Audition the same audio at different distances. Listen mainly to the changing brightness. Check any existing Unreal air-absorption settings so you do not apply the same effect twice.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/setup-atmosphere-absorption.png -->

**After the basic setup:** Connect stereo audio to the two input buffers and provide `Distance (cm)` from gameplay or the AudioPhysx world system. Use the environment values you intend for the scene, beginning with standard conditions rather than extreme laboratory inputs. Feed the two outputs to a stereo Source or a later stereo processor. The node is an audio processor and does not produce a completion trigger on its own.

Audition the source first without absorption, then with a moderate distance and eventually a very long distance. If the result becomes unnaturally muffled early, inspect whether Unreal's own air-absorption attenuation is also enabled.

`Temperature (C)` uses degrees Celsius; `Humidity (%)` is relative humidity; `Pressure (kPa)` is kilopascals. `Distance (cm)` is the travelled path length in Unreal centimetres. These units are not interchangeable with the flyby system's metre-based closest approach, and a wrong distance conversion can make any physically inspired model appear dramatically incorrect.

**Practical limitations.** The model is an approximation for believable game-audio behaviour, not a laboratory-calibrated prediction for every atmospheric condition. It also does not simulate rain, terrain, wind scattering or barrier transmission. Tune it in context, using a real output device and a varied set of recordings, rather than choosing a very dark result solely because it sounds dramatic on one sharp test sample.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Left channel of the stereo audio input.
- **`In Right`** — *Audio buffer*. Right audio channel to process.
- **`Distance (cm)`** — *Float*. Distance travelled by sound in centimetres.
- **`Temperature (C)`** — *Float*. Air temperature in degrees Celsius; default 20.
- **`Humidity (%)`** — *Float*. Relative humidity from 0 to 100; default 50.
- **`Pressure (kPa)`** — *Float*. Atmospheric pressure in kilopascals; default 101.325.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Audio after atmospheric absorption.
- **`Out Right`** — *Audio buffer*. Right audio channel after processing.

===

**Related:** [Material Transmission](../acoustics-nodes/material-transmission.md) when a wall or barrier, rather than air, is the main source of spectral loss.
