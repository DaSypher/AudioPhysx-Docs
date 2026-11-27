# Understanding inputs, outputs and completion

## Three kinds of pins

- **Trigger pins** describe moments: start playback, stop playback, release a held effect or announce completion.
- **Audio pins** carry sample buffers. `Out Mono` produces a single audio channel.
- **Control pins** carry values such as gain, pitch, distance, speed or material selection.

## `On Finished` is not the same as `Stop`

In AudioPhysx Wave Players, natural completion usually produces `On Finished`; an explicit `Stop` often cancels without issuing that natural-completion event. Check each node page for precise behaviour.

An effect such as Early Reflections or Acoustic Paths can extend the audio tail after the source Wave Player finishes. Connect the source's completion event to the processing node's `Source Finished` input and use the processor's output completion where appropriate.

## Dynamic pin groups

Some nodes allow the graph author to add more ranges, steps or waves. Change the group counts in the MetaSound editor and inspect the generated pins. For `AP: Surface Wave Player`, pins may additionally depend on project settings, so route edits deserve extra care.

## Common wiring mistake

Don't connect a Wave Player's `On Finished` directly to the MetaSound Source's finished trigger if other downstream effects still have audible tails.
