# AP: Surface Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Select waves using Unreal physical surface types and a configured route table.

## When to use it

Footsteps and impacts that vary by the EPhysicalSurface of a hit.

## Quick setup

Set up the plugin’s Surface Audio settings, restart the editor when required, then assign recordings to the generated surface-specific pins.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Select one valid wave from the hit surface. |
| `Stop` | Trigger | Stop all playing samples. |
| `Hit Surface Type` | Integer | Unreal EPhysicalSurface integer value  of the impacted physical material. |
| `Max Voices` | Integer | Maximum overlapping samples (1 to 16). |
| `No Immediate Repeat` | Boolean | Avoid selecting the previous sample  when alternatives exist. |
| `Default Waves` | Wave Asset Array | Fallback array for unmatched surfaces  or empty surface arrays. |
| `Default Volume` | Float | Linear volume for fallback samples. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mixed mono audio from active samples. |
| `On Finished` | Trigger | Fires when the last playing voice ends naturally.  Stop or rejected Play events do not trigger it. |

## Behaviour and design notes

The node creates pins from project settings. Changing enabled routes can change the graph interface; back up and review affected MetaSounds after changing the configuration.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
