---
label: "AP: Distance Wave Player"
icon: file
order: 94
---

# AP: Distance Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

Choose a different recorded perspective at different distances, rather than relying on volume attenuation alone.

<!-- IMAGE SLOT: docs/static/images/nodes/node-distance-wave-player.png -->

## Understanding the behaviour

A gunshot ten metres away often needs different recorded content from one heard several hundred metres away. Distance Wave Player evaluates `Distance (cm)` when `Play` arrives and uses the configured distance range to select a recording. Each expandable range has a start distance, a Wave Asset Array, and a volume setting. This lets the same gameplay event choose a near, medium or far recording without building a separate switch network for each sound.

The decision is made when playback starts. The player is not designed to continuously crossfade a recording that has already begun as the listener crosses a range boundary. Once accepted, the selected sound plays with its latched range gain and retains two audio output channels.

A useful application is a rifle report with separate close mechanical detail and distant tails. At short range, you may emphasize the muzzle report; farther away, you may want the environmental tail and less close-microphone detail. The node selects the appropriate authored material when the sound fires, while Unreal attenuation can continue to manage overall distance level and source spatialization.

For a repeatable test, move the listener between two fixed distances and trigger the sound at each location. You should hear a different recording pool, not just a quieter version of the same one.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Make a test Source with a distance input
Create a Stereo MetaSound Source and add **AP: Distance Wave Player**. Expose or set a Float for `Distance (cm)` so you can vary the distance while testing.

>>> 2. Configure at least two distance ranges
Expand the distance range groups and set `Start Distance (cm)` for your close and far bands in ascending order. Add distinguishable `Waves` arrays to each range, such as close mechanical detail and a distant report.

>>> 3. Set the allowed range
Supply an appropriate `Max Distance (cm)` and keep each authored band’s `Volume` under control. This player selects an appropriate **recording perspective**, not merely the gain of one recording.

>>> 4. Trigger and connect stereo
Connect `On Play` to `Play` and wire `Out Left`/`Out Right` to the Source outputs. If needed, set `Max Voices` and `No Immediate Repeat` to handle repeated events.

>>> 5. Audition range changes on retrigger
Set a close distance and trigger the sound, then try a far distance and trigger again. The selected sample should change according to the band. A change in distance does not automatically crossfade a recording already playing.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/setup-distance-wave-player.png -->

**After the basic setup:** Configure the dynamic distance ranges in ascending order of `Start Distance (cm)`, then assign one or more recordings to each `Waves` array. Supply the listener-source separation to `Distance (cm)` and connect `Play` and the two stereo outputs. Set `Max Distance (cm)` deliberately; it is a hard cutoff evaluated when a new sound is requested, not an automatic fade applied to all currently playing voices.

Use `No Immediate Repeat` when several takes exist in a range. Trigger the player in a test level with a known numerical distance before integrating any automatic listener-distance calculation.

`Volume` in a range is a **linear** playback multiplier, not a decibel value. This matters when you match the apparent loudness of near and far captures. `Max Voices` determines permitted overlap, and `On Finished` fires when the final naturally playing voice completes. There is no inherent acoustic air-absorption or Doppler calculation in the selection logic; those are separate responsibilities.

**Practical limitations.** Keep the boundaries meaningful and avoid excessive ranges with recordings that are nearly identical. A hard change between badly matched pools can be obvious during repeated action at a range boundary. Source location and built-in Unreal attenuation still need to be configured correctly. For simple trigger branching without an integrated Wave Player, [Distance Switch](../qol-nodes/distance-switch.md) is a lighter control-flow tool.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Select one sample from the current distance range.
- **`Stop`** — *Trigger*. Stop every active voice.
- **`Distance (cm)`** — *Float*. Source-to-listener distance in centimetres.
- **`Max Distance (cm)`** — *Float*. Hard playback cutoff evaluated only on Play.
- **`Max Voices`** — *Integer*. Maximum simultaneous samples (1 to 16).
- **`No Immediate Repeat`** — *Boolean*. Avoid selecting the same sample consecutively  within the selected distance range.
- **`Start Distance (cm)`** — *Float*. Distance at which this range becomes active.
- **`Waves`** — *Wave Asset Array*. Array of samples for this range.
- **`Volume`** — *Float*. Linear gain latched when a sample begins.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Stereo mix of all active voices.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Fires when the last playing voice ends naturally.  Stop or rejected Play events do not trigger it.

===

**Related:** [Dynamic Distance Switch](../qol-nodes/distance-switch.md) for routing other players by distance.
