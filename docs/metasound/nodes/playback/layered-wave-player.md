---
label: "AP: Layered Wave Player"
icon: file
order: 96
---

# AP: Layered Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

Combine several recordings into a single composite sound while controlling the level, pitch and onset of each layer.

<!-- IMAGE SLOT: docs/static/images/nodes/node-layered-wave-player.png -->

## Understanding the behaviour

Many complex game sounds are deliberately built from layers: a sharp transient that establishes the attack, a low-frequency body that provides weight, and a mechanical or environmental texture that identifies the object. Layered Wave Player starts those recordings as one stack and mixes them into stereo output. Each layer has its own recording, optional gain, optional pitch offset and optional start delay.

The controls use aligned arrays: the value at index 2 in `Layer Gains (dB)` belongs to the Wave Asset at index 2 in `Layer Waves`. Missing optional array values default to the documented neutral values. Separate left/right audio buffers mean layered stereo recordings remain stereo rather than being mixed into a single common channel.

Think of an energy weapon: a short bright crack, a low synthesized pulse and a delayed resonance tail. Rather than pre-rendering every possible combination, you can author three independent recordings and control their balance in the MetaSound. The third layer may begin a few milliseconds later to make the source feel heavier without pretending that every recorded element started at the exact same instant.

The same approach is useful for mechanical impacts, doors, or cinematic effects, although it should not be applied to every tiny event simply because layering is available.

## Building and controlling the sound

Populate `Layer Waves` in a clear order and, if needed, add matching entries to `Layer Gains (dB)`, `Layer Pitch (st)` and `Layer Delays (ms)`. The current implementation allows up to eight configured layers. Trigger `Play` once and connect `Out Left` / `Out Right` to the Source. Start with zero gain offsets and zero delays so you can hear the natural edit points, then adjust one layer at a time.

The node treats one stack as a coordinated event. If it cannot reserve sufficient voices for an eligible stack, it can reject the request rather than partially starting only some layers. `Active Layers` helps diagnose how much of the voice budget is currently occupied.

`Layer Gains (dB)` are per-layer trims, not master volume. `Layer Pitch (st)` uses semitone offsets, and `Layer Delays (ms)` shifts the start time of each layer by up to the configured supported range. `Max Voices` is the total voice budget across currently playing stacks, not the number of possible layer slots. `On Rejected` reports a stack that could not start; `On Finished` indicates natural completion after the final active layer.

**Practical limitations.** Stereo layering creates more opportunities for phase and loudness problems. Two low-frequency recordings with different timing may reinforce or cancel each other unpredictably. Use realistic game volumes, inspect peaks, and try the final output both in stereo and downmixed to mono, particularly if the effect will be spatialized as a single point in the world.


==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Start the valid layers as one atomic stack.
- **`Stop`** — *Trigger*. Stop all stacks. Does not fire On Finished.
- **`Layer Waves`** — *Wave Asset Array*. Wave Asset array: indices 0 to 7, one sound per layer.
- **`Layer Gains (dB)`** — *FFloatArray*. Optional per-layer gains, aligned with Layer Waves. Missing values = 0 dB.
- **`Layer Pitch (st)`** — *FFloatArray*. Optional per-layer playback-rate pitch offsets in semitones. Missing = 0.
- **`Layer Delays (ms)`** — *FFloatArray*. Optional per-layer onset delay, 0 to 2000 ms. Missing = 0.
- **`Max Voices`** — *Integer*. Maximum simultaneous individual layers across all stacks, 1 to 32.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Left-channel mix of all active layers.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Last layer of all active stacks finished naturally.
- **`On Rejected`** — *Trigger*. No playable layers or insufficient free voices for the entire stack.
- **`Active Layers`** — *Integer*. Number of active or pending layers.

===

**Related:** [Stereo to Mono](../qol/stereo-to-mono.md) when the finished effect must feed a mono Source.
