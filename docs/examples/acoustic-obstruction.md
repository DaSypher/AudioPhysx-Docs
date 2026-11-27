---
label: "Basic acoustic obstruction"
icon: play
order: 84
---
# Basic acoustic obstruction

**Tools used:** AP: Material Transmission or AP: Acoustic Paths

## Goal

Produce a useful, repeatable audio behaviour with a small MetaSound/Blueprint setup.

## Build the example

Start with mono audio. For an authored obstruction effect, feed a Boolean and material-loss controls to Material Transmission. For world-derived routing, use the Acoustic Path integration and connect the selected route array.

<!-- IMAGE SLOT: docs/static/images/graphs/graph-acoustic-obstruction.png -->

## Expected result

Compare an unobstructed recording with a filtered/delayed obstructed one. Avoid applying another full-strength obstruction filter downstream.

## Before shipping

- Test empty arrays and stop/retrigger behaviour.
- Test the final recording assets in a packaged Development build.
- Check voice budgets and spatialization in a scene with multiple sound sources.

[Find the node reference](../metasound/README.md).
