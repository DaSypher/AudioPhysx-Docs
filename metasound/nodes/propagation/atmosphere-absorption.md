# AP: Atmosphere Absorption

**MetaSound category:** `AudioPhysx → Propagation`  
**Source contract:** Unreal Engine 5.8.4 development source

Change high-frequency absorption based on travel distance and air conditions.

## When to use it

Large outdoor scenes and long-range sound effects.

## Quick setup

Connect mono audio; provide `Distance (cm)`, temperature, humidity and pressure values.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio` | Audio (mono) | Mono input audio. |
| `Distance (cm)` | Float | Distance travelled by sound in centimetres. |
| `Temperature (C)` | Float | Air temperature in degrees Celsius; default 20. |
| `Humidity (%)` | Float | Relative humidity from 0 to 100; default 50. |
| `Pressure (kPa)` | Float | Atmospheric pressure in kilopascals; default 101.325. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio` | Audio (mono) | Audio after atmospheric absorption. |

## Behaviour and design notes

For realism, combine thoughtfully with Unreal attenuation; avoid unintentionally applying two similar air-absorption treatments.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Propagation overview](../../propagation.md) and [Troubleshooting](../../../support/troubleshooting.md).
