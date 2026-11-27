# Material-dependent footsteps

**Tools used:** AP: PhysMat Wave Player or AP: Surface Wave Player

## Goal

Produce a useful, repeatable audio behaviour with a small MetaSound/Blueprint setup.

## Build the example

Use your game’s footstep trace or animation event to obtain a Physical Material/path or surface type, and feed the corresponding AudioPhysx player. Configure matching material-specific recordings and fallback waves.

## Expected result

Confirm the trace returns the expected material and unmatched materials use the default rather than silence.

## Before shipping

- Test empty arrays and stop/retrigger behaviour.
- Test the final recording assets in a packaged Development build.
- Check voice budgets and spatialization in a scene with multiple sound sources.

[Find the node reference](../metasound/README.md).
