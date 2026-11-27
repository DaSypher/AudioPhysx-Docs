# A one-shot that doesn't sound identical every time

**Goal:** Make footsteps, impacts or small interactions feel less repetitive by varying the recording instead of triggering one identical file on every event.

## Prepare the sound

Import four or five takes of the **same type of event**. For example, several small metal knocks. Trim obvious leading silence, match the perceived loudness where practical and keep them in a single Wave Asset Array.

## Wire the MetaSound

>>> 1. Add the player
Create a mono MetaSound Source and add [AP: Random Wave Player](../metasound/nodes/playback/random-wave-player.md).

>>> 2. Give it alternatives
Connect your Wave Asset Array to `Waves`, then connect `Play` from the desired trigger event.

>>> 3. Listen to repeated events
Connect `Out Mono` to the Source output, enable `No Immediate Repeat` if desired and audition repeated starts.

>>> 4. Stress-test the event
Trigger faster than one recording can finish. Check `Max Voices` and decide how much overlapping sound the game needs.
>>>

## What to listen for

A convincing variation player should sound **natural**, not simply more random. If one take is much louder than the others, listeners may notice the level jump more than they appreciate the variety. If you need each variation to be heard within a cycle, try the [Shuffle-Bag Wave Player](../metasound/nodes/playback/shuffle-bag-wave-player.md).
