# AP: Distance Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

Choose a different recorded perspective at different distances, rather than relying on volume attenuation alone.

## Understanding the behaviour

A gunshot ten metres away often needs different recorded content from one heard several hundred metres away. Distance Wave Player evaluates `Distance (cm)` when `Play` arrives and uses the configured distance range to select a recording. Each expandable range has a start distance, a Wave Asset Array, and a volume setting. This lets the same gameplay event choose a near, medium or far recording without building a separate switch network for each sound.

The decision is made when playback starts. The player is not designed to continuously crossfade a recording that has already begun as the listener crosses a range boundary. Once accepted, the selected sound plays with its latched range gain and retains two audio output channels.

A useful application is a rifle report with separate close mechanical detail and distant tails. At short range, you may emphasize the muzzle report; farther away, you may want the environmental tail and less close-microphone detail. The node selects the appropriate authored material when the sound fires, while Unreal attenuation can continue to manage overall distance level and source spatialization.

For a repeatable test, move the listener between two fixed distances and trigger the sound at each location. You should hear a different recording pool, not just a quieter version of the same one.

## Building and controlling the sound

Configure the dynamic distance ranges in ascending order of `Start Distance (cm)`, then assign one or more recordings to each `Waves` array. Supply the listener-source separation to `Distance (cm)` and connect `Play` and the two stereo outputs. Set `Max Distance (cm)` deliberately; it is a hard cutoff evaluated when a new sound is requested, not an automatic fade applied to all currently playing voices.

Use `No Immediate Repeat` when several takes exist in a range. Trigger the player in a test level with a known numerical distance before integrating any automatic listener-distance calculation.

`Volume` in a range is a **linear** playback multiplier, not a decibel value. This matters when you match the apparent loudness of near and far captures. `Max Voices` determines permitted overlap, and `On Finished` fires when the final naturally playing voice completes. There is no inherent acoustic air-absorption or Doppler calculation in the selection logic; those are separate responsibilities.

**Practical limitations.** Keep the boundaries meaningful and avoid excessive ranges with recordings that are nearly identical. A hard change between badly matched pools can be obvious during repeated action at a range boundary. Source location and built-in Unreal attenuation still need to be configured correctly. For simple trigger branching without an integrated Wave Player, [Distance Switch](../qol/distance-switch.md) is a lighter control-flow tool.

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

**Related:** [Dynamic Distance Switch](../qol/distance-switch.md) for routing other players by distance.
