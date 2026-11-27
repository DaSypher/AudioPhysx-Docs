---
label: "AP: Trigger Probability"
icon: shuffle
order: 60
---
# AP: Trigger Probability

**MetaSound category:** `AudioPhysx → QoL`  
**Source contract:** Unreal Engine 5.8.4 development source

Allow or reject incoming triggers according to a configurable probability.

<!-- IMAGE SLOT: docs/static/images/nodes/node-trigger-probability.png -->

## When to use it

Optional Foley layers, occasional ambient details and controlled variation.

## Quick setup

Feed `In`, set `Probability`, and connect `On Passed` to playback.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `In` | Trigger | Evaluate this trigger against the current probability. |
| `ReSeed` | Trigger | Restart the random sequence using Seed; same-frame In uses the restarted sequence. |
| `Probability` | Float | Probability from 0 (never) to 1 (always), sampled once per audio block. |
| `Seed` | Integer | Nonnegative: deterministic. -1: use a new random seed. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `On Passed` | Trigger | Passed trigger at its original sample frame. |
| `On Rejected` | Trigger | Rejected trigger at its original sample frame. |
| `Last Roll` | Float | Last random value in [0,1); -1 until first In. Block-rate Float. |

## Behaviour and design notes

`Seed` and `ReSeed` control random sequence reproducibility. A rejected event does not become a delayed event.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [QoL overview](../../qol.md) and [Troubleshooting](../../../support/troubleshooting.md).
