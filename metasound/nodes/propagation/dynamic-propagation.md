# AP: Dynamic Propagation

**MetaSound category:** `AudioPhysx → Propagation`  
**Source contract:** Unreal Engine 5.8.4 development source

Continuously vary sound travel time with source-listener distance, including a bounded Doppler-style effect.

## When to use it

Moving sound sources where travel-time changes should affect perceived pitch.

## Quick setup

Feed mono audio, distance and propagation settings. Use the single audio output for the processed signal.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio` | Audio (mono) | Mono signal to propagate. |
| `Distance (cm)` | Float | Source-listener distance in centimetres. |
| `Speed of Sound (m/s)` | Float | Sound speed in metres per second; default 343. |
| `Max Delay (s)` | Float | Maximum travel time, fixed at voice creation. |
| `Smoothing (ms)` | Float | Smooths small distance changes; default 25 ms. |
| `Max Doppler (%)` | Float | Maximum pitch deviation; default 20 percent. |
| `Jump Threshold (cm)` | Float | Large distance changes crossfade instead of scrubbing. |
| `Jump Crossfade (ms)` | Float | Crossfade duration; default 40 ms. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio` | Audio (mono) | Mono audio after travel-time delay. |
| `Doppler Ratio` | Float | Diagnostic pitch ratio. Do not apply again. |

## Behaviour and design notes

The `Doppler Ratio` output is diagnostic. Avoid applying that ratio again to the same processed signal.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Propagation overview](../../propagation.md) and [Troubleshooting](../../../support/troubleshooting.md).
