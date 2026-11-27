# AP: Material Transmission

**MetaSound category:** `AudioPhysx → Acoustics`  
**Source contract:** Unreal Engine 5.8.4 development source

Apply obstruction-dependent, frequency-shaped transmission loss to mono audio.

## When to use it

Sound heard behind doors, walls or other acoustic obstacles.

## Quick setup

Feed `Audio`, `Obstructed`, thickness and low/high loss controls; output the filtered mono signal.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio` | Audio (mono) | Mono source audio. |
| `Obstructed` | Boolean | True when the sound path is obstructed. |
| `Thickness (cm)` | Float | Assigned obstacle thickness in centimetres. |
| `Reference Thickness (cm)` | Float | Thickness at which the specified losses apply. |
| `Low Loss (dB)` | Float | Low-band transmission loss at reference thickness. |
| `High Loss (dB)` | Float | High-band transmission loss at reference thickness. |
| `Crossover (Hz)` | Float | Approximate low/high frequency division. |
| `Leakage (%)` | Float | Fraction of unobstructed audio mixed back in. |
| `Smoothing (ms)` | Float | Smoothing time for changing transmission gains. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mono audio after transmission filtering. |

## Behaviour and design notes

Loss values are authored controls or obtained from higher-level acoustic calculations; the node itself does not raycast the world.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Acoustics overview](../../acoustics.md) and [Troubleshooting](../../../support/troubleshooting.md).
