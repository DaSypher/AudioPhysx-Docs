---
label: "Randomized one-shot sounds"
icon: play
order: 89
---
# Randomized one-shot sounds

**Tools used:** AP: Random Wave Player

## Goal

Produce a useful, repeatable audio behaviour with a small MetaSound/Blueprint setup.

## Build the example

Supply multiple recordings of the same event to `Waves`, connect `On Play` or a gameplay trigger to `Play`, and route `Out Mono` to the graph output. Enable `No Immediate Repeat` if desired.

<!-- IMAGE SLOT: docs/static/images/graphs/graph-randomized-one-shot.png -->

## Expected result

Listen for variation without obvious level jumps; use consistently prepared recordings.

## Before shipping

- Test empty arrays and stop/retrigger behaviour.
- Test the final recording assets in a packaged Development build.
- Check voice budgets and spatialization in a scene with multiple sound sources.

[Find the node reference](../metasound/README.md).
