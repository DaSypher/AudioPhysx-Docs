---
label: "AP: Trigger Cooldown"
icon: file
order: 80
---

# AP: Trigger Cooldown

**AudioPhysx / QoL** · Unreal Engine 5.8.4 development source

Prevent bursts of nearly simultaneous gameplay events from becoming a wall of repeated sound.

<!-- IMAGE SLOT: site/static/images/nodes/node-trigger-cooldown.png -->

## Understanding the behaviour

A collision system, animation notify or gameplay event can generate more triggers than the player should hear. Trigger Cooldown accepts an incoming event, then blocks further events for a chosen amount of time. The ones that pass are emitted from `On Passed`; rejected events can be observed through `On Rejected`. Both outputs are triggers, and the underlying signal remains sample-addressed within the audio block.

The node does not render audio and therefore has no stereo or mono channels. Its purpose is to control which requests reach a Wave Player. The remaining cooldown is exposed as a Float so you can inspect or further condition the behaviour.

Imagine a rigid object scraping across a surface. The gameplay collision system may report several small contacts in rapid succession, but triggering a sharp hit sound for every one can sound like machine-gun chatter. A modest cooldown allows the first event to be heard while suppressing immediate duplicates. The same idea works for interface clicks, cloth impacts and repeated small environmental rattles.

This is not always appropriate for actual automatic gunfire: if every shot is meaningful, rejecting deliberately scheduled shots could damage weapon timing.

## Build the sound — step by step

The setup below is deliberately small so you can hear what this node contributes before adding more systems. Create the sound in a fresh test MetaSound first, then copy the working graph into your game.

>>> 1. Create a repeated-event sound
Build a Stereo MetaSound Source with **AP: Random Wave Player** and a few short collision or mechanical recordings. Add **AP: Trigger Cooldown** before the player.

>>> 2. Feed the cooldown node
Connect your repeated event trigger to cooldown `In`. For a single-shot preview, you can use the Source `On Play` trigger and then retrigger the Source during gameplay.

>>> 3. Choose a minimum interval
Set `Cooldown (ms)` to a modest value appropriate for the event. A short mechanical click may tolerate repeated starts faster than an ambience or heavy impact.

>>> 4. Connect accepted events to playback
Wire `On Passed` to the Wave Player `Play`. Connect the player `Out Left`/`Out Right` to the stereo Source audio outputs. Optionally monitor `On Rejected` and `Remaining (ms)` during debugging.

>>> 5. Test bursts and reset
Send several quick triggers and verify some are rejected during the cooldown. Trigger `Reset` to clear the cooldown, then test again. The cooldown filters events; it does not modify the waveform.
>>>

<!-- IMAGE SLOT: site/static/images/graphs/setup-trigger-cooldown.png -->

**After the basic setup:** Place the node between the original event and your playback node. Connect the event to `In`, set `Cooldown (ms)`, and connect `On Passed` to the target player's `Play`. To diagnose a missing sound, route `On Rejected` to a debug trigger or another temporary diagnostic graph. Use `Reset` when you intentionally want to abandon the current cooldown, for example when a new distinct interaction begins.

Compare a high-frequency burst with and without the cooldown. The accepted events should remain properly timed; they are not queued to play later after the cooldown has passed.

`Cooldown (ms)` sets the minimum interval between accepted triggers, with zero intended to pass all events. `Remaining (ms)` reports the remaining cooldown at the end of an audio block. `Reset` clears the cooldown state and affects subsequent admission decisions. None of these outputs should be wired to an audio buffer pin: they are control/event signals.

**Practical limitations.** Treat the cooldown as an intentional sound-design constraint, not a workaround for a fundamentally broken collision event producer. Too long a cooldown can make legitimate footsteps or rapid actions disappear. If the event producer is accidentally firing twice because of duplicated animation notifies, correct that first rather than hiding every symptom with a very long lockout.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`In`** — *Trigger*. Triggers to rate-limit.
- **`Reset`** — *Trigger*. Clear the cooldown; simultaneous In triggers may pass.
- **`Cooldown (ms)`** — *Float*. Minimum time between accepted triggers. Zero passes all triggers.

**Outputs from the current C++ node definition**

- **`On Passed`** — *Trigger*. Triggers allowed through at the original sample frame.
- **`On Rejected`** — *Trigger*. Triggers blocked by the cooldown at the original sample frame.
- **`Remaining (ms)`** — *Float*. Cooldown remaining at the end of this audio block. Block-rate Float.

===

**Related:** [Trigger Probability](trigger-probability.md) for occasional events rather than minimum time separation.
