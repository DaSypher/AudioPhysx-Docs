---
label: "AP: Trigger Probability"
icon: file
order: 79
---

# AP: Trigger Probability

**AudioPhysx / QoL** · Unreal Engine 5.8.4 development source

Make optional sound details happen occasionally rather than on every gameplay event.

<!-- IMAGE SLOT: docs/static/images/nodes/node-trigger-probability.png -->

## Understanding the behaviour

A probability gate makes one decision for each trigger presented to `In`. A `Probability` of 0 rejects everything; a value of 1 allows everything; values between represent a chance for each event. `On Passed` and `On Rejected` preserve the event as a trigger rather than converting it into audio. The `Last Roll` Float lets you see the most recent random value used by the decision process.

This control-only design is deliberate. It is independent of whether your eventual Wave Player produces stereo or mono output. You can place Trigger Probability before a complex stereo layered effect just as easily as before a simple one-shot player.

Consider adding occasional fabric rustling to a character's movement. A rustle on every single footstep may feel artificial, but a chance-based trigger creates texture without requiring a complicated animation state machine. Likewise, a working motor can produce an occasional metallic rattle rather than a rattle at every update.

Randomness is not the same as a guaranteed schedule. A 25% chance does not mean exactly one event every four triggers, and long runs without a pass are possible.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Create an optional stereo sound layer
Add a simple stereo Wave Player with a subtle recording, such as a small gear rattle. Insert **AP: Trigger Probability** in the trigger path.

>>> 2. Connect the candidate event
Connect an incoming event to `In`. This is the event *candidate* that may or may not start the optional sound.

>>> 3. Set a starting probability
Set `Probability` between 0 and 1; for example, 0.25 requests a 25% acceptance chance per event. Use `Seed` for repeatable debugging or trigger `ReSeed` when you want a fresh sequence.

>>> 4. Wire accepted events to the player
Connect `On Passed` to the Wave Player `Play`. Route its stereo outputs to the Source or to a properly configured stereo mix. The probability node itself has no audio outputs.

>>> 5. Listen over many events
Trigger repeatedly. Expect occasional playback, not an exact one-in-four schedule. `On Rejected` and `Last Roll` can help explain why an individual event did not play.
>>>

<!-- IMAGE SLOT: docs/static/images/graphs/setup-trigger-probability.png -->

**After the basic setup:** Insert the node between the gameplay trigger and the optional sound. Supply `Probability`, then route `On Passed` to the target player's Play input. Use `On Rejected` only if the graph needs to react or if you want to debug how often the optional detail is being suppressed. A fixed `Seed` is helpful for reproducible test sessions, while `ReSeed` restarts the random sequence.

Test the extremes first: zero probability should never pass a trigger, and one should always pass. Only then choose an intermediate value appropriate to the desired density.

`Probability` is sampled once per audio block and lies between 0 and 1. The source accepts a nonnegative deterministic `Seed`; `-1` requests a new random seed. `Last Roll` is a block-rate Float that reports the latest draw and begins at a sentinel value before any event arrives. That makes it useful for debugging selection without confusing a numeric value with an audio output.

**Practical limitations.** If a specific recording must be heard at least once during a finite gameplay cycle, a simple probability gate is the wrong tool. Use a deterministic schedule or a bag-style selection instead. Also avoid hiding a key gameplay cue behind an optional probability gate unless the player has another reliable way to understand the event.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In`** — *Trigger*. Evaluate this trigger against the current probability.
- **`ReSeed`** — *Trigger*. Restart the random sequence using Seed; same-frame In uses the restarted sequence.
- **`Probability`** — *Float*. Probability from 0 (never) to 1 (always), sampled once per audio block.
- **`Seed`** — *Integer*. Nonnegative: deterministic. -1: use a new random seed.

**Outputs from the current C++ node definition**

- **`On Passed`** — *Trigger*. Passed trigger at its original sample frame.
- **`On Rejected`** — *Trigger*. Rejected trigger at its original sample frame.
- **`Last Roll`** — *Float*. Last random value in [0,1); -1 until first In. Block-rate Float.

===

**Related:** [Shuffle-Bag Wave Player](../playback-nodes/shuffle-bag-wave-player.md) for distributing sound choices across an entire variation pool.
