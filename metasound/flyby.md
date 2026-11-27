# AP: Flyby Wave Player

**Category:** AudioPhysx → Playback

Plays flyby whizz variations and optional supersonic crack variations based on supplied flyby parameters.

## Inputs

| Pin | Description |
| --- | --- |
| `Play` | Start playback. |
| `Stop` | Stop playback. |
| `Whizz Waves` | Array of whizz/flyby recordings. |
| `Crack Waves` | Array of crack recordings. |
| `Distance (m)` | Closest-pass distance, in metres. |
| `Speed (m/s)` | Projectile speed, in metres per second. |
| `Intensity` | Flyby intensity control. |
| `Speed of Sound (m/s)` | Reference acoustic speed. |
| `Shock` | Shock-wave-related control. |

## Outputs

| Pin | Description |
| --- | --- |
| `Out Mono` | Audio output. |
| `On Finished` | Playback completion. |
| `On Rejected` | Player rejected the requested playback. |

This is an acoustically inspired *game effect*, not a full ballistic/shock-wave solver. The associated Blueprint path helper provides the near-miss data. See [Flyby integration](../blueprint/flyby.md).

> TODO: Verify parameter names in the final MetaSound graph and document exactly what `Shock` represents in the shipped node.
