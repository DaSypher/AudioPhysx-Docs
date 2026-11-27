# AP: PhysMat Wave Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Select recordings by exact Physical Material asset path, with fallback recordings.

## When to use it

Footsteps, collision feedback and material-dependent interactions.

## Quick setup

Supply `Hit PhysMat Path`, configure material routes and assign `Default Waves` for unmatched materials.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Play` | Trigger | Choose and play one recording. |
| `Stop` | Trigger | Stop all active voices. |
| `Hit PhysMat Path` | String | Exact Physical Material asset path. |
| `Default Waves` | Wave Asset Array | Wave Asset array used when no route matches. |
| `Default Volume` | Float | Linear gain of fallback recordings. |
| `No Immediate Repeat` | Boolean | Avoid repeating the previous recording  when alternatives are available. |
| `Max Voices` | Integer | Maximum overlapping recordings. |
| `Waves` | Wave Asset Array | Wave Asset array for this material. |
| `Volume` | Float | Linear volume for this material. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mixed mono audio output. |
| `On Finished` | Trigger | Fires when the final voice ends naturally. |
| `On Rejected` | Trigger | Fires when a requested voice cannot start. |

## Behaviour and design notes

Material path matching is exact. It is not enough to supply only a surface-type integer.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
