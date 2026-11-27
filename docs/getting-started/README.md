---
label: Getting started
icon: rocket
order: 95
---
# Start creating with AudioPhysx

You do not need to understand sound propagation or C++ before getting value from AudioPhysx. Begin with a simple Wave Player and add complexity only when the sound actually calls for it.

## Your first 15 minutes

>>> 1. Understand the basics
Read [Requirements and terminology](requirements.md). Learn the difference between a Wave Asset, trigger and audio output, and why Unreal distances are often in centimetres.

>>> 2. Install and confirm the plugin
Follow [Installation](installation.md), then check that the `AudioPhysx` categories appear in the MetaSound node search.

>>> 3. Build one complete sound
Use [Your first MetaSound](first-metasound.md) to connect three recordings to **AP: Sequence Wave Player**.

>>> 4. Understand completion
Read [Signals and completion](signals-and-completion.md). It explains why an audio source can finish before a delayed reflection or propagation tail has ended.

>>> 5. Troubleshoot with a checklist
Keep the [Setup checklist](checklist.md) open when testing your own MetaSounds.
>>>

<!-- IMAGE SLOT: docs/static/images/setup/node-search.png -->

Once that works, try a [randomized one-shot](../examples/randomized-one-shot.md) or [RPM-controlled weapon](../examples/automatic-weapon.md). Both reuse the same fundamentals.
