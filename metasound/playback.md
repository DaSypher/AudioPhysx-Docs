# Playback — choose the right player

Playback nodes select, schedule and combine recordings. Use them when a sound needs a behaviour more involved than simply playing one Wave Asset when it receives a trigger.

## One event, several possible takes

**[Random Wave Player](nodes/playback/random-wave-player.md)** chooses a recording when an event occurs, with optional no-immediate-repeat and overlap settings. **[Shuffle-Bag Wave Player](nodes/playback/shuffle-bag-wave-player.md)** is preferable when repeated events should gradually cover the available takes rather than picking freely every time.

A footstep or repeated impact often starts here.

## An action made of stages

**[Sequence Wave Player](nodes/playback/sequence-wave-player.md)** plays fixed recordings consecutively. **[Random Sequence Wave Player](nodes/playback/random-sequence-wave-player.md)** does the same but chooses a variation from an array at each step.

**[Layered Wave Player](nodes/playback/layered-wave-player.md)** is different: it combines several layers within one event, optionally with small offsets. Choose sequence for *one after another* and layers for *sounds together*.

## An action that stays active

**[Start Loop End Player](nodes/playback/start-loop-end.md)** handles attack, held middle and release. At `RPM = 0`, middle recordings follow one another; with a positive RPM, overlapping shots start at a designed rate. See the [automatic weapon walkthrough](../examples/automatic-weapon.md).

## The world selects the sound

Use **[Distance Wave Player](nodes/playback/distance-wave-player.md)** when near and far recordings differ, **[Surface Wave Player](nodes/playback/surface-wave-player.md)** when Unreal surface types determine the material sound, and **[PhysMat Wave Player](nodes/playback/physmat-wave-player.md)** when exact Physical Material paths matter.

For near-miss projectiles, **[Flyby Wave Player](nodes/playback/flyby-wave-player.md)** is driven by a separate game-side calculation; it is not a generic Wave Player for every distant shot.

!!!tip Choosing by intent
If the sound needs to be *selected*, choose a variation player. If it needs to *happen in stages*, choose a sequence. If it needs to *continue while held*, choose Start Loop End. If it needs to *change with the game world*, choose a distance or material-aware player.
!!!

[Browse the complete Playback node index](nodes/playback/README.md)
