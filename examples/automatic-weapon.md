# Automatic weapon with RPM

**Primary AudioPhysx tools:** AP: Start Loop End Player

A good example is a listening experiment, not just a screenshot of connected pins. This exercise explains what content to prepare, which signals the graph needs, and what result you should listen for before increasing complexity.

## Prepare the recording and context

Collect a short introductory attack or weapon mechanism, several main gunshot variations and one or more release/tail recordings. Keep the main recordings in a consistent tonal family. A gunshot that rings for 250 ms does **not** need to be cut to 100 ms just because the weapon fires at 600 rounds per minute; the scheduler is designed to let the recordings overlap.

## Assemble the MetaSound and test it

Create a stereo Source and add Start Loop End Player. Fill `Start Waves`, `Loop Waves` and `End Waves`. Route gameplay press to `Start Firing` and release to `Stop Firing`, then connect Left/Right audio and final completion. Set `RPM` to 600 and audition a sustained hold: once the introductory recording finishes, middle shots should be scheduled roughly every 100 ms. Test `Immediate Release` both on and off to hear whether active shots fade quickly or finish before the ending begins.

## Judge the result in a game

A convincing automatic weapon should communicate a stable firing rhythm while allowing individual shot bodies and tails to overlap. The source has a bounded twelve-voice middle pool, so extremely high RPM plus long clips can saturate it and cause new scheduled shots to be skipped. If the event never finishes, check that `Stop Firing` actually arrives; a missing release event is not an audio-decoder problem.

A repeatable test in a small scene is more valuable than adding several processors at once. Check the Source's channel layout and all completion events before moving the same graph into a large level. If the audio will ultimately be positioned as a mono point source, audition the [Stereo to Mono](../metasound/nodes/qol/stereo-to-mono.md) version as well as the full stereo path.

[Browse the full node reference](../metasound/README.md) for exact control types and limitations.
