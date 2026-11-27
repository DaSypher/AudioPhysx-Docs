# AP: Float Smoother

**MetaSound category:** `AudioPhysx → QoL`  
**Source contract:** Unreal Engine 5.8.4 development source

Apply independent rise and fall smoothing to a floating-point control value.

## When to use it

Volume and filter parameters driven by noisy or abrupt gameplay values.

## Quick setup

Connect `Target`, set `Rise (ms)` and `Fall (ms)`, and use the `Smoothed` output.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Target` | Float | Float value to smooth. Sampled once per audio block. |
| `Rise (ms)` | Float | Exponential time constant for increasing values. Zero snaps immediately. |
| `Fall (ms)` | Float | Exponential time constant for decreasing values. Zero snaps immediately. |
| `Snap` | Trigger | Immediately set the output to Target in this block (block-rate behaviour). |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Smoothed` | Float | Rise/fall smoothed Float control signal (block-rate). |

## Behaviour and design notes

This is a block-rate control smoother, not an audio-rate filter.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [QoL overview](../../qol.md) and [Troubleshooting](../../../support/troubleshooting.md).
