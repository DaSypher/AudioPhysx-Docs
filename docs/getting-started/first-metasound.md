---
label: "Your first MetaSound"
icon: play
order: 80
---
# Your first AudioPhysx MetaSound

In this walkthrough you'll make three recordings play **in order** using `AP: Sequence Wave Player`. Each sound starts once the previous sound has finished—no manual delay values.

## 1. Create a MetaSound Source

Create a new **MetaSound Source** with a mono output. Open it in the MetaSound editor.

<!-- IMAGE SLOT: docs/static/images/setup/create-metasound.png -->

## 2. Add the node

Search for **AP: Sequence Wave Player** in `AudioPhysx → Playback`. Add it to the graph.

<!-- IMAGE SLOT: docs/static/images/nodes/node-sequence-wave-player.png -->

## 3. Assign waves

Expand the `Sequence Waves` group to the number of recordings you want. Assign a Wave Asset to each `Wave` slot in the intended order.

## 4. Wire Play, audio and completion

| From | To |
| --- | --- |
| MetaSound `On Play` | Sequence player's `Play` |
| Sequence player's `Out Mono` | MetaSound mono audio output |
| Sequence player's `On Finished` | MetaSound Source `On Finished` (when appropriate) |

<!-- IMAGE SLOT: docs/static/images/graphs/graph-first-sequence.png -->

## 5. Audition and verify

Preview the MetaSound. You should hear each recording sequentially. With `Loop Sequence` enabled the list repeats; without looping it ends after the last valid sound.

!!!tip
If you're creating a long-running ambient or interactive source, don't wire `On Finished` in a way that stops the Source before you want it to end.
!!!

Next: [Random Sequence Wave Player](../metasound/nodes/playback/random-sequence-wave-player.md) or [Start Loop End Player](../metasound/nodes/playback/start-loop-end.md).
