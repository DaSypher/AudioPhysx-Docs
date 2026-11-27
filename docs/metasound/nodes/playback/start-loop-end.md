---
label: "AP: Start Loop End Player"
icon: repeat
order: 90
---
# AP: Start Loop End Player

**MetaSound category:** `AudioPhysx → Playback`  
**Source contract:** Unreal Engine 5.8.4 development source

Play a randomized introduction, repeat middle recordings, then play a randomized ending on release.

<!-- IMAGE SLOT: docs/static/images/nodes/node-start-loop-end.png -->

## When to use it

Automatic-fire weapons, powered tools, engines, energy beams and other held actions.

## Quick setup

Fill the three Wave Asset Arrays. Trigger `Start Firing`, then `Stop Firing` to request release. Connect `Out Mono` and use `On Finished` for natural completion.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Start Firing` | Trigger | Play a random intro, then begin firing middle waves. |
| `Stop Firing` | Trigger | Stop scheduling shots and enter the ending. |
| `Immediate Release` | Boolean | True: fade active waves and play ending immediately. False: let all active waves finish before ending. |
| `RPM` | Float | 0 = legacy sequential middle waves. 60-2400 = middle shots per minute, with overlap. Updated at shot boundaries. |
| `Start Waves` | Wave Asset Array | Random intro wave array. If empty, start middle sounds immediately. |
| `Loop Waves` | Wave Asset Array | Random middle wave array; RPM sets the interval between starts, not between completions. |
| `End Waves` | Wave Asset Array | Random ending wave array. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Mixed mono audio output. |
| `On Finished` | Trigger | Fires when ending audio and any remaining shots have finished. |

## Behaviour and design notes

`RPM = 0` waits for each middle recording to finish. Positive RPM values schedule overlapping middle shots. `Immediate Release` changes whether active audio finishes or fades into release.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Playback overview](../../playback.md) and [Troubleshooting](../../../support/troubleshooting.md).
