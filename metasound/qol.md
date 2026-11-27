# QoL

These tools shape audio behaviour using physically inspired processing, author-controlled parameters or timing logic.

| Node | Purpose |
| --- | --- |
| [AP: Distance Switch (Dynamic)](nodes/qol/distance-switch.md) | Route a trigger to one of several expandable distance bands. |
| [AP: Float Smoother](nodes/qol/float-smoother.md) | Apply independent rise and fall smoothing to a floating-point control value. |
| [AP: Trigger Cooldown](nodes/qol/trigger-cooldown.md) | Let triggers through only when a configured cooldown has elapsed. |
| [AP: Trigger Probability](nodes/qol/trigger-probability.md) | Allow or reject incoming triggers according to a configurable probability. |

## How to choose

- **Route triggers by distance:** Distance Switch (Dynamic).
- **Avoid sharp parameter changes:** Float Smoother.
- **Limit trigger rates:** Trigger Cooldown.
- **Occasional/random events:** Trigger Probability.

For a reproducible demonstration, start with the [first MetaSound tutorial](../getting-started/first-metasound.md).
