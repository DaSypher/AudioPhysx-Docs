# AP: Trigger Cooldown

**MetaSound · AudioPhysx / Qol**

Reject rapid repeated trigger events until a chosen minimum interval has elapsed.

## What actually happens

Collision, interaction and animation systems often produce more triggers than a sound designer wants to hear. This node lets an input trigger through, then holds off additional events for a configurable period.

The purpose is practical: avoid six identical scrape clicks caused by one contact, or a machine noise retriggering faster than it can be perceived.

## Hear it in a game

Send repeated footstep events to `In` with a modest `Cooldown (ms)`. Observe which events reach `On Passed` and which are rejected. Then set `Cooldown (ms)` to zero to compare unrestricted behaviour.

## Build a working graph

>>> 1. Connect the trigger
Connect a source trigger to `In`.
>>>

>>> 2. Choose a minimum interval
Choose `Cooldown (ms)` for the event you want to limit.
>>>

>>> 3. Route the accepted events
Use `On Passed` to start playback; optionally inspect rejected events when debugging. `Reset` clears the cooldown state.
>>>

## The controls that matter

`Cooldown (ms)` is the minimum allowed interval between accepted events. `Reset` makes the next event eligible according to the implementation’s state. This does not modify audio; it only routes triggers.

## What the node outputs

- **`On Passed`** · Trigger — Triggers allowed through at the original sample frame.
- **`On Rejected`** · Trigger — Triggers blocked by the cooldown at the original sample frame.
- **`Remaining (ms)`** · Float — Cooldown remaining at the end of this audio block. Block-rate Float.

## Things to watch for

- A cooldown that is too long may hide valid rapid events, particularly for automatic weapons.
- When gameplay timing matters, test the actual trigger producer; adding a cooldown does not correct a broken animation/event schedule.

==- Full input reference
- **`In`** · *Trigger* — Triggers to rate-limit.
- **`Reset`** · *Trigger* — Clear the cooldown; simultaneous In triggers may pass.
- **`Cooldown (ms)`** · *Float* — Minimum time between accepted triggers. Zero passes all triggers.
===

==- Full output reference
- **`On Passed`** · Trigger — Triggers allowed through at the original sample frame.
- **`On Rejected`** · Trigger — Triggers blocked by the cooldown at the original sample frame.
- **`Remaining (ms)`** · Float — Cooldown remaining at the end of this audio block. Block-rate Float.
===

## Continue learning

[Trigger Probability](trigger-probability.md) is for random admission rather than minimum spacing. Also see the [Qol overview](../../qol.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
