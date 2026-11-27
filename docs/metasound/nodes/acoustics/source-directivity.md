---
label: "AP: Source Directivity"
icon: broadcast
order: 80
---
# AP: Source Directivity

**MetaSound category:** `AudioPhysx → Acoustics`  
**Source contract:** Unreal Engine 5.8.4 development source

Apply direction-dependent spectral shaping and attenuation.

<!-- IMAGE SLOT: docs/static/images/nodes/node-source-directivity.png -->

## When to use it

Loudspeakers, exhausts, voices and directional machinery.

## Quick setup

Feed `Angle (deg)` and a mono audio signal, then adjust strength and rear attenuation.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio` | Audio (mono) | Mono input audio. |
| `Angle (deg)` | Float | Angle from the source forward direction  to the listener. 0 is front, 180 is rear. |
| `Directivity (%)` | Float | Directivity strength, 0 to 100 percent. |
| `Rear Attenuation (dB)` | Float | Maximum high-frequency attenuation at 180 degrees. |
| `Low Frequency Directivity (%)` | Float | Fraction of high-frequency attenuation  applied to the lower frequencies. |
| `Crossover (Hz)` | Float | Approximate low/high frequency division. |
| `Smoothing (ms)` | Float | Smooth changes in directional attenuation. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mono audio after directional filtering. |

## Behaviour and design notes

Requires a source-to-listener angle from your game or another AudioPhysx system. This is not 3D positional rendering by itself.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Acoustics overview](../../acoustics.md) and [Troubleshooting](../../../support/troubleshooting.md).
