---
label: "AP: Trigger Probability"
icon: shuffle
order: 60
---
# AP: Trigger Probability

**MetaSound · AudioPhysx / Qol**

Let an incoming trigger through only some of the time.

<!-- IMAGE SLOT: docs/static/images/nodes/node-trigger-probability.png -->

## What actually happens

Not every event needs an audible consequence. A subtle rattle might happen on some movements, a cloth rustle on occasional animation cycles, or a debris tick on only a fraction of impacts.

Trigger Probability evaluates a random decision for each incoming `In` event. Unlike an audio player’s variation picker, it decides **whether the event happens at all**.

## Hear it in a game

Add a faint gear-rattle layer to a running machine, but send its trigger through this node first. A probability of 0 should never pass; 1 should always pass; values between those extremes should create occasional events.

## Build a working graph

>>> 1. Connect the event
Send an event trigger to `In`.
>>>

>>> 2. Choose probability and seed
Set `Probability` from 0 to 1 and wire `On Passed` to the optional sound effect.
>>>

>>> 3. Route occasional sounds
Use `Seed` and `ReSeed` when a repeatable sequence is useful for debugging.
>>>

## The controls that matter

`Probability` is a fraction: 0.25 means an intended 25% chance per evaluated trigger, **not** one event every four triggers. `Seed` and `ReSeed` control the random stream; this node does not alter a sample’s gain or playback pitch.

## What the node outputs

- **`On Passed`** · Trigger — Passed trigger at its original sample frame.
- **`On Rejected`** · Trigger — Rejected trigger at its original sample frame.
- **`Last Roll`** · Float — Last random value in [0,1); -1 until first In. Block-rate Float.

## Things to watch for

- Chance is statistical, not a guaranteed distribution. Long runs of passes or rejections can happen.
- If a sound must play at least once during a finite cycle, prefer a selection strategy with explicit history.

==- Full input reference
- **`In`** · *Trigger* — Evaluate this trigger against the current probability.
- **`ReSeed`** · *Trigger* — Restart the random sequence using Seed; same-frame In uses the restarted sequence.
- **`Probability`** · *Float* — Probability from 0 (never) to 1 (always), sampled once per audio block.
- **`Seed`** · *Integer* — Nonnegative: deterministic. -1: use a new random seed.
===

==- Full output reference
- **`On Passed`** · Trigger — Passed trigger at its original sample frame.
- **`On Rejected`** · Trigger — Rejected trigger at its original sample frame.
- **`Last Roll`** · Float — Last random value in [0,1); -1 until first In. Block-rate Float.
===

## Continue learning

[Shuffle-Bag Wave Player](../playback/shuffle-bag-wave-player.md) distributes sound *choices* rather than rejecting whole events. Also see the [Qol overview](../../qol.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
