---
label: "AP: Impact Dynamics"
icon: file
order: 87
---

# AP: Impact Dynamics

**AudioPhysx / Acoustics** · Unreal Engine 5.8.4 development source

Use one impact recording more expressively by changing its attack and colour according to how hard the impact was.

<!-- IMAGE SLOT: docs/static/images/nodes/node-impact-dynamics.png -->

## Understanding the behaviour

Impact Dynamics takes an existing stereo audio recording plus an `Impact` trigger and an `Impact Strength` control in the 0–1 range. It uses the strength to interpolate between soft and hard gain/filter settings, with an additional transient enhancement for stronger events. This can make a single usable asset feel gentler for a light contact and brighter or more aggressive for a forceful collision.

It does **not** detect a collision or compute collision impulse inside the audio thread. Your game, animation, trace or Blueprint helper decides that an impact occurred and provides a meaningful strength value. The node then shapes the audio. Both channels are processed independently, preserving the stereo source while applying the same intended impact strength.

Imagine a character dropping a small tool onto a wooden surface. A very light contact may need a soft, muted tap; a much stronger drop can need a brighter transient and greater level. Rather than importing dozens of almost identical strength variations, you can use a few recordings with dynamics that follow the gameplay's impact-strength signal.

This becomes particularly valuable for many small environmental interactions. It should still be driven by plausible events: setting the strength to 1 on every minor collision can make an otherwise natural scene sound exaggerated and exhausting.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Prepare an impact sound and stereo Source
Create a Stereo MetaSound Source, add a stereo AudioPhysx player for a short impact, and insert **AP: Impact Dynamics** after it.

>>> 2. Connect both audio inputs
Connect the Wave Player’s `Out Left` and `Out Right` to the impact node `In Left` and `In Right`. Route the processed Left/Right outputs to the Source.

>>> 3. Trigger the impact processor alongside playback
Connect the event used to begin the Wave Player to the processor’s `Impact` trigger as well. This tells the DSP when an impact occurs; the DSP does not generate collision events by itself.

>>> 4. Set the impact strength and shaping range
Supply an `Impact Strength` value in the intended normalized range. Start with moderate `Soft Gain`, `Hard Gain`, `Soft Cutoff (Hz)` and `Hard Cutoff (Hz)` settings.

>>> 5. Compare gentle and hard strikes
Trigger with a low strength and then a higher strength. Adjust `Transient Boost` and `Transient Time (ms)` carefully; compare `Applied Strength` to verify the control is reaching the processor.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/setup-impact-dynamics.png -->

**After the basic setup:** Connect your stereo impact recording to `In Left` and `In Right`, trigger its player and the Impact Dynamics `Impact` event together, and set `Impact Strength` appropriately. Begin with audible but moderate differences between `Soft Gain` / `Hard Gain` and between `Soft Cutoff (Hz)` / `Hard Cutoff (Hz)`. Audition at several strength values instead of testing only the extremes.

The output includes `Applied Strength`, which exposes the clamped value used by the processor. That makes it useful for checking whether gameplay is sending valid input and whether the strength normalization behaves as you expect.

`Soft Gain` and `Hard Gain` are **linear gain controls**, while the cutoff inputs are in hertz. `Transient Boost` adds attack emphasis, with `Transient Time (ms)` determining how long that emphasis lasts. Excessive transient gain can create sharp peaks and clipping, especially when multiple impacts overlap. A normalized strength represents an authored mapping from gameplay force, not a universal physical unit such as newtons.

**Practical limitations.** A strong impact can consist of several physical stages—first contact, material resonance and secondary movement—so dynamics processing cannot replace all variation in source recordings. Use a good base sound, and consider Layered Wave Player or material-based selection when a change in physical material is more important than a change in force. Profile simultaneous impacts in a dense scene before raising every node's transient enhancement.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In Left`** — *Audio buffer*. Stereo audio from the impact Wave Player.
- **`In Right`** — *Audio buffer*. Right audio channel to process.
- **`Impact`** — *Trigger*. Restart the transient when playback starts.
- **`Impact Strength`** — *Float*. Normalized impact strength, 0 to 1.
- **`Soft Gain`** — *Float*. Linear gain at impact strength 0.
- **`Hard Gain`** — *Float*. Linear gain at impact strength 1.
- **`Soft Cutoff (Hz)`** — *Float*. Low-pass cutoff for gentle impacts.
- **`Hard Cutoff (Hz)`** — *Float*. Low-pass cutoff for strong impacts.
- **`Transient Boost`** — *Float*. Extra attack gain applied to harder hits.
- **`Transient Time (ms)`** — *Float*. Duration of the attack enhancement.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Impact-shaped stereo audio.
- **`Out Right`** — *Audio buffer*. Right audio channel after processing.
- **`Applied Strength`** — *Float*. Clamped strength used by this operator.

===

**Related:** [Material-dependent footsteps](../../examples/material-footsteps.md) for a related event-driven workflow.
