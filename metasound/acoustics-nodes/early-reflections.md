# AP: Early Reflections

**AudioPhysx / Acoustics** · Unreal Engine 5.8.4 development source

Add short, synthetic reflection taps that suggest nearby boundaries without running a full room simulation.

## Understanding the behaviour

Early reflections are some of the first distinct returns you hear after a short sound strikes surfaces in a space. A hand clap in a small room has a different initial tail from the same clap outdoors. This node creates a compact group of synthetic delayed reflections from a room-size estimate, sound speed and damping settings, mixing them with the dry stereo signal.

The reflected channels have independent state. This matters because a stereo recording can contain meaningful differences that should survive an effect, even though the same approximate room settings are applied to both sides. The node is **not** tracing the precise room geometry or generating an impulse response from your level. It deliberately offers a fast, editable suggestion of near-field reflections.

Try a dry finger snap, short metal hit or rifle report. Increase the Wet Level gradually and listen for small delayed arrivals after the direct sound. A larger Room Size should suggest a broader spacing of early returns, while stronger HF Damping makes those returns less bright. The goal is to help locate a sound in an environment without creating a long, washed-out reverb tail.

If your game already uses a global late reverb, early reflections can complement it—provided the timing and balance are intentional. Two sets of strong reflections from separate systems can sound unnaturally busy.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Make a clean stereo signal
Create a Stereo MetaSound Source and add a stereo Wave Player with a short clap, click or impact. Insert **AP: Early Reflections** after it.

>>> 2. Connect source and reflection audio
Connect player Left/Right outputs to `In Left` and `In Right` on Early Reflections, then route the reflection node `Out Left`/`Out Right` to the Source.

>>> 3. Choose a small room as a starting point
Set `Room Size (m)` and `Speed of Sound (m/s)` to sensible values. Keep `Dry Level` prominent and raise `Wet Level` gradually rather than beginning with an overpowering reflection mix.

>>> 4. Preserve the delayed tail
Connect the player’s `On Finished` to `Source Finished` on Early Reflections. Use the reflections node `On Finished` to close the MetaSound Source when no later processor contributes audio.

>>> 5. Listen for timing and tone
Use the same impact while changing `Room Size (m)` and `HF Damping`. Listen for short room taps and a natural decay; the node does not trace the actual walls of your level.
>>>

**After the basic setup:** Connect stereo audio to `In Left` and `In Right`, and feed the upstream Wave Player's `On Finished` into `Source Finished`. Then connect the resulting stereo output to the Source and use this node's `On Finished` when it represents the last audible stage in the graph. The completion routing ensures the Source can remain alive long enough to render the reflection taps after the dry recording ends.

Begin with a short sample and a relatively low Wet Level. Move Room Size and HF Damping one control at a time. If you start with a complex ambient recording, it can be difficult to tell whether the node's taps are contributing anything meaningful.

`Room Size (m)` is an authored scale, and `Speed of Sound (m/s)` controls the conversion into travel time. `Dry Level` and `Wet Level` are level controls for the direct signal and reflection taps. `HF Damping` reduces the higher-frequency content of the reflections. `On Finished` follows the last reflection tail rather than simply echoing the dry player's completion at the same instant.

**Practical limitations.** Treat the output as a convincing approximation, not a source of exact reflection arrival times for every wall in a real space. Highly reflective settings can add clutter and strong peaks; test with mono fold-down and normal game mix levels. If your purpose is sound transmission *around an obstacle* rather than room echo, Acoustic Paths is the more relevant processing tool.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Stereo signal to reflect.
- **`In Right`** — *Audio buffer*. Right audio channel to process.
- **`Source Finished`** — *Trigger*. Connect the Wave Player's On Finished output.
- **`Room Size (m)`** — *Float*. Controls four synthetic extra reflection  path lengths. Does not trace geometry.
- **`Speed of Sound (m/s)`** — *Float*. Propagation speed for reflection delays.
- **`Dry Level`** — *Float*. Level of the original sound.
- **`Wet Level`** — *Float*. Level of the reflection taps.
- **`HF Damping`** — *Float*. Higher values remove more high frequencies  from reflections.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Original sound plus early reflections.
- **`Out Right`** — *Audio buffer*. Right audio channel after processing.
- **`On Finished`** — *Trigger*. Fires after the last reflection tail.

===

**Related:** [Acoustic Paths](acoustic-paths.md) for selected travel routes rather than artificial room taps.
