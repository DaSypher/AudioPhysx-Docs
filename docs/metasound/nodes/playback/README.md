---
label: "Playback node reference"
icon: play
order: 70
---

# Playback nodes

This category is where AudioPhysx decides which recordings should play, how they are ordered, and whether several recordings should be heard simultaneously. The ten Wave Player nodes all expose stereo audio output, so you can keep an authored stereo recording intact until your Source needs to be downmixed for a particular spatialization policy.

**[AP: Random Wave Player](random-wave-player.md)** — A reliable starting point for any event that should sound familiar without replaying precisely the same recording every time.

**[AP: Shuffle-Bag Wave Player](shuffle-bag-wave-player.md)** — Variation selection that deliberately uses a bag of eligible recordings instead of always making an unrestricted random choice.

**[AP: Sequence Wave Player](sequence-wave-player.md)** — Play several recordings one after another, using the recordings themselves to determine when each step should advance.

**[AP: Random Sequence Wave Player](random-sequence-wave-player.md)** — A predictable beginning, middle and end—but with fresh recording choices inside every stage.

**[AP: Layered Wave Player](layered-wave-player.md)** — Combine several recordings into a single composite sound while controlling the level, pitch and onset of each layer.

**[AP: Start Loop End Player](start-loop-end.md)** — One sound can have a meaningful start, a repeating body, and a release that only plays when the action ends.

**[AP: Distance Wave Player](distance-wave-player.md)** — Choose a different recorded perspective at different distances, rather than relying on volume attenuation alone.

**[AP: PhysMat Wave Player](physmat-wave-player.md)** — Choose impact or interaction recordings using the exact Physical Material asset involved in the event.

**[AP: Surface Wave Player](surface-wave-player.md)** — Use Unreal physical surface types to select footstep, impact or interaction variations through one MetaSound player.

**[AP: Flyby Wave Player](flyby-wave-player.md)** — Turn a near-miss calculation into an audible projectile whizz, with an optional ballistic-crack layer.

For a broader explanation, return to the [Playback overview](../../playback.md).
