# Automatic weapon with RPM

**Tools used:** AP: Start Loop End Player

## Goal

Produce a useful, repeatable audio behaviour with a small MetaSound/Blueprint setup.

## Build the example

Provide `Start Waves` (optional), several short `Loop Waves`, and `End Waves`. Connect a trigger to `Start Firing`, and release to `Stop Firing`. Set `RPM = 600` for a nominal 100 ms shot interval.

## Expected result

Verify that middle shots overlap when recordings last longer than the shot interval. Test both `Immediate Release` modes.

## Before shipping

- Test empty arrays and stop/retrigger behaviour.
- Test the final recording assets in a packaged Development build.
- Check voice budgets and spatialization in a scene with multiple sound sources.

[Find the node reference](../metasound/README.md).
