# Acoustics

These tools shape audio behaviour using physically inspired processing, author-controlled parameters or timing logic.

| Node | Purpose |
| --- | --- |
| [AP: Acoustic Paths](nodes/acoustics/acoustic-paths.md) | Apply the selected acoustic route: propagation delay and three-band loss from the game-thread path solver. |
| [AP: Impact Dynamics](nodes/acoustics/impact-dynamics.md) | Shape the transient, level and filtering of an impact recording according to impact strength. |
| [AP: Early Reflections](nodes/acoustics/early-reflections.md) | Add a small set of simulated early reflections to a mono recording. |
| [AP: Material Transmission](nodes/acoustics/material-transmission.md) | Apply obstruction-dependent, frequency-shaped transmission loss to mono audio. |
| [AP: Source Directivity](nodes/acoustics/source-directivity.md) | Apply direction-dependent spectral shaping and attenuation. |

## How to choose

- **Wall transmission:** Material Transmission.
- **Selected path and delay:** Acoustic Paths.
- **Impact shaping:** Impact Dynamics.
- **Synthetic room taps:** Early Reflections.
- **Facing-dependent tone:** Source Directivity.

For a reproducible demonstration, start with the [first MetaSound tutorial](../getting-started/first-metasound.md).
