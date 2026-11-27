---
label: "Propagation"
icon: pulse
order: 70
---
# Propagation

These tools shape audio behaviour using physically inspired processing, author-controlled parameters or timing logic.

| Node | Purpose |
| --- | --- |
| [AP: Atmosphere Absorption](nodes/propagation/atmosphere-absorption.md) | Change high-frequency absorption based on travel distance and air conditions. |
| [AP: Distance Delay](nodes/propagation/distance-delay.md) | Delay mono audio based on distance divided by speed of sound. |
| [AP: Dynamic Propagation](nodes/propagation/dynamic-propagation.md) | Continuously vary sound travel time with source-listener distance, including a bounded Doppler-style effect. |
| [AP: Doppler Ratio](nodes/propagation/doppler-ratio.md) | Compute a pitch ratio from radial source and listener velocities. |

## How to choose

- **Distance-driven air absorption:** Atmosphere Absorption.
- **Latch a travel-time delay:** Distance Delay.
- **Continuously moving source:** Dynamic Propagation.
- **Separate pitch ratio control:** Doppler Ratio.

For a reproducible demonstration, start with the [first MetaSound tutorial](../getting-started/first-metasound.md).
