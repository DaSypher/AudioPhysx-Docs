---
label: "Randomized one-shots"
icon: play
order: 95
---

# Randomized one-shots

**Primary AudioPhysx tools:** AP: Random Wave Player

A good example is a listening experiment, not just a screenshot of connected pins. This exercise explains what content to prepare, which signals the graph needs, and what result you should listen for before increasing complexity.

## Prepare the recording and context

Use several recordings of one physical event, such as a handful of metal objects being moved or several punches on the same surface. Import the files as Wave Assets and trim them so their transients begin consistently. Aim for roughly similar perceived level; the player can choose a recording but cannot magically make radically different source edits sound like one cohesive event.

## Assemble the MetaSound and test it

Add a Random Wave Player to a stereo Source and connect the recording array to `Waves`. Connect the event trigger to `Play`, then route `Out Left` and `Out Right` to the stereo output. Enable `No Immediate Repeat` when you have multiple valid takes and want to reduce consecutive identical choices. Choose a `Max Voices` setting appropriate to the likely overlap and listen to a rapid burst of triggers, not just one click.

<!-- IMAGE SLOT: site/static/images/graphs/graph-randomized-one-shot.png -->

## Judge the result in a game

You should hear the same kind of event with subtle natural differences. If one take leaps out of the mix or contains a long tail that conflicts with the next event, correct the source asset or reduce overlap deliberately. For a strictly positioned sound, try converting the completed stereo result to mono before spatialization and compare the two presentations.

A repeatable test in a small scene is more valuable than adding several processors at once. Check the Source's channel layout and all completion events before moving the same graph into a large level. If the audio will ultimately be positioned as a mono point source, audition the [Stereo to Mono](../metasound/qol-nodes/stereo-to-mono.md) version as well as the full stereo path.

[Browse the full node reference](../metasound/README.md) for exact control types and limitations.
