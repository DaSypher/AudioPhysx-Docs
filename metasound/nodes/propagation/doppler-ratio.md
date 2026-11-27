# AP: Doppler Ratio

**MetaSound category:** `AudioPhysx → Propagation`  
**Source contract:** Unreal Engine 5.8.4 development source

Compute a pitch ratio from radial source and listener velocities.

## When to use it

Manual Doppler control for players or modulation chains not using Dynamic Propagation.

## Quick setup

Supply source/listener velocities toward each other and use `Pitch Ratio` to control a compatible playback pitch input.

## Inputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Source Toward Listener (m/s)` | Float | Positive means source approaches listener. |
| `Listener Toward Source (m/s)` | Float | Positive means listener approaches source. |
| `Speed of Sound (m/s)` | Float | Default 343 m/s. |

## Outputs

| Pin | Type | Purpose |
| --- | --- | --- |
| `Pitch Ratio` | Float | Pitch multiplier for playback WITHOUT Dynamic Propagation. |

## Behaviour and design notes

Positive velocity values in the named pins mean moving toward the other party. Do not double-apply with Dynamic Propagation.

> **Units matter:** Pin names indicate metres (`m`), metres per second (`m/s`), centimetres (`cm`), milliseconds (`ms`), decibels (`dB`) and semitones (`st`). Don't convert centimetres to metres unless the target pin expects metres.

## Testing checklist

1. Test the intended input settings with a valid source recording or signal.
2. Test zero/empty/invalid inputs where applicable.
3. Test rapid parameter changes and retriggering where applicable.
4. Verify output and completion behaviour in a packaged build before relying on the node in shipping content.

See [Propagation overview](../../propagation.md) and [Troubleshooting](../../../support/troubleshooting.md).
