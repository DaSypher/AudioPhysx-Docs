---
label: "AP: Impact Dynamics"
icon: zap
order: 80
---
# AP: Impact Dynamics

**MetaSound · AudioPhysx / Acoustics**

Make one impact recording react to whether the hit was gentle or forceful.

<!-- IMAGE SLOT: docs/static/images/nodes/node-impact-dynamics.png -->

## What actually happens

An impact is more than a volume change. Soft contacts tend to have gentler transients, while harder contacts can sound brighter and more aggressive. This node uses an `Impact` trigger and a normalized strength value to drive impact-time gain, filtering and transient emphasis around the input recording.

It is a **sound-shaping** node, not a collision detector. Supply the actual impact event and, if desired, calculate its strength through an existing AudioPhysx Blueprint helper.

## Hear it in a game

Use one moderately strong metal knock recording. Audition it with an impact strength near the soft end and then near the hard end. Adjust the soft/hard gain and cutoff controls until one source asset provides useful expressive variation.

## Build a working graph

>>> 1. Provide the impact sound
Connect the existing impact audio to `Audio In`.
>>>

>>> 2. Drive strength and impact event
Trigger `Impact` at the event and supply a normalized `Impact Strength` control.
>>>

>>> 3. Shape the transient
Tune `Soft Gain`, `Hard Gain`, `Soft Cutoff (Hz)` and `Hard Cutoff (Hz)`, adding transient boost only where the recording benefits.
>>>

## The controls that matter

`Soft Gain` and `Hard Gain` describe level shaping at the two strength extremes. `Soft Cutoff (Hz)` and `Hard Cutoff (Hz)` control the filter range. `Transient Boost` and `Transient Time (ms)` affect attack emphasis over a short window.

## What the node outputs

- **`Out Mono`** · Audio (mono) — Impact-shaped mono audio.
- **`Applied Strength`** · Float — Clamped strength used by this operator.

## Things to watch for

- A noisy or inaccurate strength value can make the same asset change character unpredictably; smooth or normalize the driving gameplay value if needed.
- Too much transient boost can sound clicky or harsh. Audition at realistic game levels.

==- Full input reference
- **`Audio In`** · *Audio (mono)* — Mono audio from the impact Wave Player.
- **`Impact`** · *Trigger* — Restart the transient when playback starts.
- **`Impact Strength`** · *Float* — Normalized impact strength, 0 to 1.
- **`Soft Gain`** · *Float* — Linear gain at impact strength 0.
- **`Hard Gain`** · *Float* — Linear gain at impact strength 1.
- **`Soft Cutoff (Hz)`** · *Float* — Low-pass cutoff for gentle impacts.
- **`Hard Cutoff (Hz)`** · *Float* — Low-pass cutoff for strong impacts.
- **`Transient Boost`** · *Float* — Extra attack gain applied to harder hits.
- **`Transient Time (ms)`** · *Float* — Duration of the attack enhancement.
===

==- Full output reference
- **`Out Mono`** · Audio (mono) — Impact-shaped mono audio.
- **`Applied Strength`** · Float — Clamped strength used by this operator.
===

## Continue learning

[Blueprint playback helpers](../../../blueprint/playback-helpers.md) describes available game-side audio and impact utilities. Also see the [Acoustics overview](../../acoustics.md) and [signal & completion concepts](../../../getting-started/signals-and-completion.md).
