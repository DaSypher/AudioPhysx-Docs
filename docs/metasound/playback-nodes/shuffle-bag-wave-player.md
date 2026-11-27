---
label: "AP: Shuffle-Bag Wave Player"
icon: file
order: 99
---

# AP: Shuffle-Bag Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

Variation selection that deliberately uses a bag of eligible recordings instead of always making an unrestricted random choice.

<!-- IMAGE SLOT: docs/static/images/nodes/node-shuffle-bag-wave-player.png -->

## Understanding the behaviour

A shuffle bag is useful when ordinary randomness still sounds repetitive. In a small sound library, the same take can be selected several times in a row by chance. Here, each eligible entry participates in the current bag, and `Play` draws from the remaining entries. When a cycle is exhausted, another bag can be constructed. Optional weights influence how the eligible entries participate in that selection process; they do not change the volume of the Wave Asset.

Playback remains fully stereo. Each accepted sound is mixed into `Out Left` and `Out Right`, so a recorded stereo rustle or environmental hit can retain its channel information. `Selected Index` and `Bag Remaining` provide useful feedback for diagnosing unexpected variation choices without listening for tiny differences between similar clips.

Imagine an NPC walking over a dry wooden floor. With a random player, it is possible to hear the same distinctive creak repeatedly. A bag approach distributes selection more deliberately across available takes. It can also work well for repeated mechanical clunks, short movement details and sets of similar destruction fragments.

Do not confuse this with timing or sequencing. A shuffle bag determines **which** recording to play next. Your animation, footsteps system or game event still determines **when** the next `Play` trigger arrives.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Build the playback Source
Create a Stereo MetaSound Source and add **AP: Shuffle-Bag Wave Player**. Use several distinct recordings of the same event so the changing choices are easy to hear.

>>> 2. Connect recordings and optional weights
Fill `Waves` with at least four takes. Leave `Weights` empty for the simplest test, or provide one non-negative weight per recording; a weight of zero excludes that entry.

>>> 3. Wire triggering and reset
Connect Source `On Play` to the player `Play`. Optionally expose a separate trigger for `Reset Bag` so you can deliberately restart its selection cycle.

>>> 4. Connect stereo and monitoring
Connect `Out Left` and `Out Right` to the corresponding outputs of the MetaSound. Watch `Selected Index` and `Bag Remaining` if you need to confirm the selection sequence.

>>> 5. Compare with free random selection
Trigger the graph repeatedly and listen for distributed choices. Try `Seed` with a known nonzero value to reproduce a sequence while debugging. Increase `Max Voices` only if simultaneous playback is actually required.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/setup-shuffle-bag-wave-player.png -->

**After the basic setup:** Create a Wave Asset Array with your variations, then connect it to `Waves`. `Weights` is optional; its entries correspond by index to the Wave Assets, so keep the arrays aligned when you add or remove a recording. Connect the trigger and both stereo outputs in the same way as any other player. Trigger through a complete cycle and observe the remaining count to understand the node's behaviour.

Use `Reset Bag` when you intentionally want to abandon the current selection history, such as after moving to a completely different interaction context. Resetting the bag does not automatically stop existing voices, so the sound that is already audible need not be cut off.

`Seed` controls reproducibility. A fixed, nonzero seed is useful when testing the same sequence repeatedly; the source defines zero as a request for a new random seed. `Pitch Shift (st)` and `Gain (dB)` affect newly started voices, not the weights. `Max Voices` controls simultaneous playback. Rejected selections are reported through `On Rejected` when there is no playable eligible choice or available voice.

**Practical limitations.** This node is not a content-quality substitute: obviously different loudness or inconsistent noise floors can reveal the individual recording choices. Very high weights may cause the distribution to feel less even than expected, and zero-weight entries are intentionally ineligible. Check selection in a realistic playback run rather than assuming a handful of preview clicks establishes the distribution.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Draw and play one unused eligible wave.
- **`Stop`** — *Trigger*. Stop all current voices without firing On Finished.
- **`Reset Bag`** — *Trigger*. Discard the remaining bag; keep playing voices.
- **`Waves`** — *Wave Asset Array*. Wave Asset Array. Maximum 128 entries.
- **`Weights`** — *FFloatArray*. Optional non-negative weights aligned with Waves. Missing entries use 1; zero excludes an entry.
- **`Pitch Shift (st)`** — *Float*. Playback-rate pitch in semitones, -24 to 24.
- **`Gain (dB)`** — *Float*. Gain for newly started voices, -96 to +12 dB.
- **`Max Voices`** — *Integer*. Maximum overlapping voices (1 to 16).
- **`Seed`** — *Integer*. Nonzero seed is deterministic. Zero selects a random seed.

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Mixed playback audio.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. Final active voice finished naturally.
- **`On Rejected`** — *Trigger*. No eligible wave, free voice or playable proxy.
- **`Selected Index`** — *Integer*. Most recent selected index; -1 on rejection/Stop.
- **`Bag Remaining`** — *Integer*. Number of unplayed entries left in the current bag.

===

**Related:** [Random Wave Player](random-wave-player.md) when you do not need bag history.
