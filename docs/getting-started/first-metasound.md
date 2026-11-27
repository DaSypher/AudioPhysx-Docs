---
icon: rocket
---
# Your first AudioPhysx MetaSound

This example uses **AP: Sequence Wave Player** to play multiple recordings one after another.

1. Create a MetaSound Source with a mono output.
2. Add `AP: Sequence Wave Player` from **AudioPhysx → Playback**.
3. Expand the **Sequence Waves** group and connect a Wave Asset to each `Wave` slot.
4. Connect the MetaSound `On Play` trigger to the node's `Play` input.
5. Connect `Out Mono` to the MetaSound audio output.
6. Connect `On Finished` to the MetaSound Source's completion trigger, if you want the source to finish automatically.
7. Preview playback with `Loop Sequence` disabled, then try enabling it.

## Expected behaviour

Each playable wave should finish before the next starts. `Stop` stops the sequence. The `On Finished` trigger indicates the completed sequence rather than the end of each individual wave.

> TODO: Add an editor screenshot and audition three waves with different lengths, including one compressed asset.
