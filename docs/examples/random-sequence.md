---
label: Multi-stage sound variation
icon: play
order: 87
---
# One action, several random stages

**Goal:** Keep the order of a sound effect recognizable while allowing its individual details to change.

Imagine a mechanical device that opens, performs an action, then closes. A random single-sound player cannot enforce that three-stage structure; a fixed sequence can, but it sounds the same every time. [AP: Random Sequence Wave Player](../metasound/nodes/playback/random-sequence-wave-player.md) combines both ideas.

## Prepare three arrays

Create one array of opening clicks, one of mechanical middle actions and one of ending clunks. Each array can contain multiple takes, but keep each array specific to its stage.

## Build the sequence

>>> 1. Add and expand the node
Create a mono Source, add `AP: Random Sequence Wave Player` and expand the `Sequence Steps` group to three stages.

>>> 2. Assign an array to each stage
Connect the opening array to stage one, mechanism array to stage two, and ending array to stage three.

>>> 3. Start it with one event
Connect `Play` and `Out Mono`. Use `On Finished` if this effect should end the Source when the third recording finishes.

>>> 4. Audition several passes
The recordings within each stage should vary, but the opening, middle and ending should always follow one another in that order.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/graph-random-sequence.png -->

## Why there are no delay pins

This is a **completion-driven** sequencer. The next stage starts when the current recording ends. If you make the middle clip longer, the final stage happens later automatically. For simultaneous layers, choose a Layered Wave Player instead.
