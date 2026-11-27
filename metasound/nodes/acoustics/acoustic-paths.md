# AP: Acoustic Paths

**MetaSound category:** `AudioPhysx → Acoustics`  
**Source contract:** Unreal Engine 5.8.4 development source

Apply the selected acoustic route: propagation delay and three-band loss from the game-thread path solver.

## When to use it

Wall and portal acoustics where direct or around-obstacle routing changes audibility.

## Quick setup

Connect your mono audio, the compact four-value route array and `Source Finished` from the upstream player.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Audio In` | Audio (mono) | Mono input to propagate. |
| `Source Finished` | Trigger | Wave Player On Finished; passed through after the path tails. |
| `Selected Route` | Float Array | Float Array from AP.AcousticRoute.Selected: delay ms, low/mid/high loss dB. Route selection occurs on the game thread. |
| `Smoothing (ms)` | Float | Smooth path loss and delay changes. |
| `Delay Capacity (ms)` | Float | Delay buffer capacity allocated ONCE at graph creation. Default 128 ms; raise to 1500 ms only if long cinematic propagation is required. Changes during playback cannot grow the buffer. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Out Mono` | Audio (mono) | Only the selected, delayed and filtered acoustic path. |
| `On Finished` | Trigger | Triggered after the longest queued acoustic path tail. |

## Behaviour and design notes

The `Selected Route` array is `[delay ms, low loss dB, mid loss dB, high loss dB]`. This node renders one selected path, not separate simultaneous direct/around voices.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Acoustics overview](../../acoustics.md) and [Troubleshooting](../../../support/troubleshooting.md).
