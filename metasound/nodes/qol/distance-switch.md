# AP: Distance Switch (Dynamic)

**MetaSound category:** `AudioPhysx → QoL`  
**Source contract:** Unreal Engine 5.8.4 development source

Route a trigger to one of several expandable distance bands.

## When to use it

Different MetaSound branches for close, medium and far perspectives.

## Quick setup

Expand distance range groups and configure start distances, volumes and outputs; trigger `Play`.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Evaluate distance and trigger one range. |
| `Distance (cm)` | Float | Source-to-listener distance in centimetres. |
| `Max Distance (cm)` | Float | Maximum distance at which sound can start. |
| `Start Distance (cm)` | Float | Distance at which this range becomes active. |
| `Volume` | Float | Volume multiplier for this range. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Triggers when this range is selected. |
| `Gain` | Float | Volume multiplier for the selected branch. |
| `Out of Range` | Trigger | Triggered when distance exceeds Max Distance. |
| `Invalid Ranges` | Trigger | Triggered when range configuration is invalid. |
| `Selected Index` | Integer | Selected range index, or -1 if rejected. |

## Behaviour and design notes

This routes triggers and gain controls; it is not an audio player. Set input/output group counts consistently.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [QoL overview](../../qol.md) and [Troubleshooting](../../../support/troubleshooting.md).
