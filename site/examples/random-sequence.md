---
label: "Multi-stage variation"
icon: play
order: 93
---

# Multi-stage variation

**Primary AudioPhysx tools:** AP: Random Sequence Wave Player

A good example is a listening experiment, not just a screenshot of connected pins. This exercise explains what content to prepare, which signals the graph needs, and what result you should listen for before increasing complexity.

## Prepare the recording and context

Imagine a powered door that makes three recognizably ordered sounds: a button or access click, the motor moving, and a final latch. Record several alternatives for each distinct phase. Store all opening clicks in one array, all motor variations in a second, and all closing clunks in a third. Keeping the arrays semantically separate is more important than their exact size.

## Assemble the MetaSound and test it

Create a stereo Source with Random Sequence Wave Player and expand it to three array steps. Connect the arrays in the desired order, route `Play` from one interaction trigger, then connect both stereo audio outputs. With `Loop Sequence` disabled, `On Finished` can end the Source after the last phase. Trigger the action repeatedly and listen to how the selected recordings change without changing the overall structure.

<!-- IMAGE SLOT: site/static/images/graphs/graph-random-sequence.png -->

## Judge the result in a game

The player waits for the chosen recording in one phase to finish before beginning the next. That makes this much easier to maintain than a chain of hard-coded delays when you replace assets later. If you actually need multiple stages to sound at once, use Layered Wave Player instead; that is a mixing problem, not a sequencing problem.

A repeatable test in a small scene is more valuable than adding several processors at once. Check the Source's channel layout and all completion events before moving the same graph into a large level. If the audio will ultimately be positioned as a mono point source, audition the [Stereo to Mono](../metasound/qol-nodes/stereo-to-mono.md) version as well as the full stereo path.

[Browse the full node reference](../metasound/README.md) for exact control types and limitations.
