---
label: Automatic weapon with RPM
icon: play
order: 88
---
# Automatic weapon sound with RPM

**Goal:** Start a weapon with an attack recording, repeat variable shot bodies at an actual firing rate, and play a proper release tail when the player lets go of the trigger.

The important improvement over a simple sequential player is that a shot recording might last longer than the interval between rounds. **RPM controls when the next shot begins**, not how quickly the current recording must finish.

## Prepare three kinds of recording

**Start Waves** should contain the distinctive attack or mechanism sound when the weapon first fires. **Loop Waves** holds your repeatable middle gunshot variations. **End Waves** contains the release, stopping mechanism or tail used after firing stops.

## Connect it

>>> 1. Add Start Loop End Player
Create a mono MetaSound Source and add [AP: Start Loop End Player](../metasound/nodes/playback/start-loop-end.md).

>>> 2. Assign the wave arrays
Fill `Start Waves`, `Loop Waves` and `End Waves`. Use multiple middle takes to prevent the same shot being selected endlessly.

>>> 3. Set a firing rate
Set `RPM` to 600 for a nominal **100 ms interval** between middle-shot starts. Positive RPM values are distinct from the `RPM = 0` completion-driven mode.

>>> 4. Wire the controls
Send the weapon pressed event to `Start Firing` and the released event to `Stop Firing`. Connect `Out Mono` to the graph output and completion as appropriate.

>>> 5. Test both release options
With `Immediate Release` enabled, active shots fade and the end begins promptly. With it disabled, active audio gets time to complete first.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/graph-automatic-weapon.png -->

## What to listen for

At 600 RPM, a new middle recording should start approximately every tenth of a second once the intro has finished, even when an individual recording is longer. Releasing the weapon should prevent new middle shots and lead into an ending. Because the node has a **twelve-voice middle pool**, very long samples at high RPM can exhaust the available voices; new shot starts may then be skipped rather than cutting earlier recordings off.

!!!warning Held audio needs a release event
If your gameplay only sends `Start Firing` and never sends `Stop Firing`, the source may remain in the active middle state. This is a gameplay trigger contract, not a playback bug.
!!!

[Detailed player reference](../metasound/nodes/playback/start-loop-end.md)
