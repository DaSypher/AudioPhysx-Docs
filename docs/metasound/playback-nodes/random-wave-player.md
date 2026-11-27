---
label: "AP: Random Wave Player"
icon: file
order: 100
---

# AP: Random Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

A reliable starting point for any event that should sound familiar without replaying precisely the same recording every time.

<!-- IMAGE SLOT: docs/static/images/nodes/node-random-wave-player.png -->

## Understanding the behaviour

The Random Wave Player takes a collection of Wave Assets and makes a selection whenever `Play` is triggered. Once the selection is accepted, that recording plays through the node's stereo output. Unlike a graph built from separate random-number, asset-switch and Wave Player elements, selection and concurrent playback are handled together. The node also exposes whether a requested start was rejected, which is useful when you are debugging empty arrays or reaching a voice limit.

Stereo matters particularly if the source recording contains actual left/right differences. The player now mixes its active voices into independent `Out Left` and `Out Right` buffers, rather than collapsing recordings to a single channel. If this is a tightly positioned 3D footstep, you may still choose to downmix at the end of the graph; the point is that no early stage forces you to discard stereo material.

Consider a character handling a set of loose metal objects. You might have six recordings of a similar small impact, each with slightly different rhythm and resonance. Randomly choosing between them prevents a short repeated animation from sounding machine-generated. For a weapon or collision system, the same node can respond to closely spaced triggers while older recordings are still ringing out, up to the configured voice limit.

A collection of recordings should sound like a family. Random selection does not automatically equalize their loudness or remove poorly trimmed silence. Prepare the Wave Assets so the listener notices physical variation rather than inconsistent editing.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Create a stereo MetaSound Source
In the Content Browser, create a MetaSound Source with **Stereo** as its output format. Add **AP: Random Wave Player** from AudioPhysx. This simple graph tests selection and playback before adding any environmental processing.

>>> 2. Prepare your variation array
Import at least three short recordings of the same event, such as mechanical clicks or impacts. Build a Wave Asset Array and connect it to `Waves`. Keep the takes at roughly comparable loudness so that random selection does not cause an unintended volume jump.

>>> 3. Connect the start trigger
Connect the Source `On Play` trigger to `Play`. Leave `Stop` disconnected for this first one-shot test. Enable `No Immediate Repeat` when you have more than one valid recording.

>>> 4. Route both audio channels
Connect `Out Left` to the Source left output and `Out Right` to its right output. Set `Max Voices` conservatively; it controls how many triggered recordings can overlap.

>>> 5. Audition and check the result
Play the Source several times and check `Selected Index` if you are debugging which take was chosen. Rapidly retrigger to confirm your chosen voice limit is appropriate. `On Rejected` is a useful signal when nothing can play.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/setup-random-wave-player.png -->

**After the basic setup:** Create a stereo MetaSound Source and add `AP: Random Wave Player`. Supply several recordings to `Waves`, connect `On Play` or your own event to `Play`, and connect `Out Left` and `Out Right` to the corresponding Source outputs. Begin with a modest `Max Voices` setting, trigger the node repeatedly, and listen for overlap. If the Source is intentionally mono, route the two outputs into `AP: Stereo to Mono` first.

When `No Immediate Repeat` is enabled, the node attempts to avoid selecting the previous recording when there is more than one valid option. `Selected Index` makes it easy to confirm that selection is working even when the recordings happen to sound similar.

`Pitch Shift (st)` alters playback pitch in semitones; positive values are higher, negative values lower. This is a playback-rate-style change, so consider how it affects perceived duration and naturalness. `Max Voices` limits how many recordings may exist simultaneously. `On Finished` indicates natural completion of the final active voice, whereas `On Rejected` identifies an unsuccessful start request rather than playing a replacement silence. These are event outputs, not audio buffers.

**Practical limitations.** For performance, avoid setting voice capacity arbitrarily high on effects triggered dozens of times per frame. More active voices mean more decoding and mixing work. Audition realistic bursts in a packaged Development build and verify that the sound still follows the gameplay event when the pool is busy. A single long ambient recording would generally be better served by a normal Unreal playback workflow than a constantly retriggered random one-shot player.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Select one random valid Wave Asset and play it.
- **`Stop`** — *Trigger*. Stop all active wave playback.
- **`Waves`** — *Wave Asset Array*. Array of Wave Assets to randomly select from.
- **`No Immediate Repeat`** — *Boolean*. Prevent consecutive selections of the same  wave when alternatives are available.
- **`Pitch Shift (st)`** — *Float*. Playback pitch adjustment in semitones.  Also changes playback duration.
- **`Max Voices`** — *Integer*. Maximum number of overlapping recordings,  from 1 to 16.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Left channel of the active-voice stereo mix.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Triggered when the final active voice  finishes naturally.
- **`On Rejected`** — *Trigger*. Triggered when playback cannot start.
- **`Selected Index`** — *Integer*. Index of the most recently accepted wave,  or -1 for a rejected selection.

===

**Related:** [Shuffle-Bag Wave Player](shuffle-bag-wave-player.md) if you want a selection history rather than an unrestricted random draw.
