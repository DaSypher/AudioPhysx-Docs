---
label: "Material-dependent footsteps"
icon: play
order: 92
---

# Material-dependent footsteps

**Primary AudioPhysx tools:** AP: Surface or PhysMat Wave Player

A good example is a listening experiment, not just a screenshot of connected pins. This exercise explains what content to prepare, which signals the graph needs, and what result you should listen for before increasing complexity.

## Prepare the recording and context

Start with two clearly different ground types, such as stone and grass, and prepare several footstep recordings for each. The character's animation or gameplay system supplies the foot-contact timing; AudioPhysx is responsible for choosing an appropriate recording after the ground has been identified. Do not debug the Wave Player before verifying that your trace returns the expected surface identifier.

## Assemble the MetaSound and test it

For broad categories, configure Surface Audio routes and use Surface Wave Player with the `Hit Surface Type` integer. For specific Physical Material assets, use PhysMat Wave Player with the exact `Hit PhysMat Path`. In either case, assign a default recording pool for unmatched material information, then connect `Play`, `Out Left` and `Out Right`. Walk over both known materials and an intentionally unmapped surface while printing the gameplay result.

<!-- IMAGE SLOT: docs/static/images/graphs/graph-material-footsteps.png -->

## Judge the result in a game

Surface type and Physical Material path represent different levels of detail; pick the one your game actually uses. A stereo recording may be suitable as part of a designed close-up effect, but a character's footstep as a small point source is also a good candidate for a final Stereo to Mono downmix. Listen in the game's actual spatialization environment rather than assuming one format will always be better.

A repeatable test in a small scene is more valuable than adding several processors at once. Check the Source's channel layout and all completion events before moving the same graph into a large level. If the audio will ultimately be positioned as a mono point source, audition the [Stereo to Mono](../metasound/nodes/qol/stereo-to-mono.md) version as well as the full stereo path.

[Browse the full node reference](../metasound/README.md) for exact control types and limitations.
