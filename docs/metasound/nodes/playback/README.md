---
label: "Playback node reference"
icon: play
order: 90
---
# Playback reference

These players turn Wave Assets into varied, sequenced, layered or world-sensitive audio.

### [AP: Distance Wave Player](distance-wave-player.md)

Choose a recording collection based on how far the sound source is from the listener.

### [AP: Flyby Wave Player](flyby-wave-player.md)

Turn a projectile near-miss result into an audible whizz and optional ballistic crack.

### [AP: Layered Wave Player](layered-wave-player.md)

Build one composite effect from several recordings that start together or at different offsets.

### [AP: PhysMat Wave Player](physmat-wave-player.md)

Route playback using an exact Unreal Physical Material asset path, with a fallback when nothing matches.

### [AP: Random Sequence Wave Player](random-sequence-wave-player.md)

Keep the stages of an action in order, but randomly vary the recording played at each stage.

### [AP: Random Wave Player](random-wave-player.md)

Play a random recording from an array whenever an event occurs, with optional variation and multiple simultaneous voices.

### [AP: Sequence Wave Player](sequence-wave-player.md)

Build a fixed sequence of recordings without timing it by hand. Each playable wave starts after the one before it finishes.

### [AP: Shuffle-Bag Wave Player](shuffle-bag-wave-player.md)

Choose variations without repeatedly favoring the same few recordings, with weights and an explicit bag reset.

### [AP: Start Loop End Player](start-loop-end.md)

Play an opening sound, sustain a repeatable middle section, and finish with a proper release when the action ends.

### [AP: Surface Wave Player](surface-wave-player.md)

Add the player to a MetaSound and connect the exposed surface-specific arrays as well as `Default Waves`.

[Back to Playback overview](../../playback.md)
