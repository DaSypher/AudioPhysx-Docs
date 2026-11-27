---
label: "Multi-stage sound variation"
icon: play
order: 87
---
# Multi-stage sound variation

**Tools used:** AP: Random Sequence Wave Player

## Goal

Produce a useful, repeatable audio behaviour with a small MetaSound/Blueprint setup.

## Build the example

Create one `Waves` array for each stage: e.g., opening mechanism, main action, closure. Each stage randomly selects one recording and starts the next once playback ends.

<!-- IMAGE SLOT: docs/static/images/graphs/graph-random-sequence.png -->

## Expected result

The ordered structure stays the same; the individual recordings vary.

## Before shipping

- Test empty arrays and stop/retrigger behaviour.
- Test the final recording assets in a packaged Development build.
- Check voice budgets and spatialization in a scene with multiple sound sources.

[Find the node reference](../metasound/README.md).
