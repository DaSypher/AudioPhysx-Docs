# Projectile near-miss audio

**Primary AudioPhysx tools:** AP: Flyby Wave Player + Blueprint helper

A good example is a listening experiment, not just a screenshot of connected pins. This exercise explains what content to prepare, which signals the graph needs, and what result you should listen for before increasing complexity.

## Prepare the recording and context

A near miss should be driven by a projectile path rather than by the fact that a gun was fired. Start with a straight hitscan segment that passes deliberately beside the listener and a second segment that clearly misses the audible radius. Choose a couple of whizz recordings and optionally separate crack recordings. Their editing and apparent source distance will strongly influence the perceived quality of the result.

## Assemble the MetaSound and test it

Set up a stereo Source with Flyby Wave Player and the five exact `AP.Flyby.*` Float inputs described in the [Blueprint flyby guide](../blueprint/flyby.md). Call `AP: Calculate Flyby` first and print `bAudible`, closest distance and shock state. When those values match the geometry, use `AP: Play Projectile Flyby` to schedule the Source for an accepted path. Feed the actual shot start, end and metres-per-second speed to the helper.

## Judge the result in a game

Compare close, distant, slower and faster passes. The crack layer should follow the computed shock request rather than playing on every whizz. If a moving projectile produces duplicate flybys, review the `ProjectileInstance` you supply for duplicate suppression. Remember that the helper uses a simplified constant-speed acoustic model, not an exact physical shock-front simulation.

A repeatable test in a small scene is more valuable than adding several processors at once. Check the Source's channel layout and all completion events before moving the same graph into a large level. If the audio will ultimately be positioned as a mono point source, audition the [Stereo to Mono](../metasound/nodes/qol/stereo-to-mono.md) version as well as the full stereo path.

[Browse the full node reference](../metasound/README.md) for exact control types and limitations.
