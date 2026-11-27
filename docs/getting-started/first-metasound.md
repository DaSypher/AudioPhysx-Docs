---
label: Your first MetaSound
icon: play
order: 80
---
# Your first AudioPhysx MetaSound

We're going to create a sound that has **three distinct stages**: a click, a mechanical movement, and a final clunk. One `Play` trigger starts the action; AudioPhysx waits for each recording to finish before moving to the next. You won't need Blueprint timers or hand-authored delays.

## Make the graph

>>> 1. Create a mono Source
Create a **MetaSound Source** in the Content Browser, choose a mono output layout and open it. Import three short Wave Assets if you don't already have them.

>>> 2. Add the player
Search `AP: Sequence Wave Player` in the add-node menu. This is in **AudioPhysx → Playback**.

>>> 3. Fill the slots
Expand `Sequence Waves` to three inputs. Assign the click, movement and clunk in that order. These are **individual Wave Assets**, not arrays.

>>> 4. Connect the event and audio
Connect the Source's `On Play` to the node's `Play`, and connect `Out Mono` to the Source's mono audio output.

>>> 5. Handle the end of the source
If you want the Source to finish when the last recording ends, connect the player's `On Finished` to the Source's completion input. If you later add a tail-generating effect, move completion handling to the last effect.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/graph-first-sequence.png -->

## What you should hear

A single Play creates three sounds in order. If you lengthen the middle recording, the final clunk should occur later automatically. If you turn on `Loop Sequence`, the whole pattern starts again; without looping, the player finishes after the final valid slot.

!!!tip Try one change
Replace the final clunk with a different-length recording and audition again. You'll immediately see why this approach is easier than maintaining hand-calculated trigger delays.
!!!

## When this is the wrong node

If each stage needs to select a *different random take*, use [Random Sequence Wave Player](../metasound/nodes/playback/random-sequence-wave-player.md). If you need shots at fixed RPM while the trigger is held, use [Start Loop End Player](../metasound/nodes/playback/start-loop-end.md).

[Next: Learn triggers and completion](signals-and-completion.md)
