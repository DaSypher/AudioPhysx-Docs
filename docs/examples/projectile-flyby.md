---
label: "Projectile near-miss flyby"
icon: play
order: 85
---
# Projectile near-miss flyby

**Tools used:** AP: Flyby Wave Player + AP: Play Projectile Flyby

## Goal

Produce a useful, repeatable audio behaviour with a small MetaSound/Blueprint setup.

## Build the example

Set up the flyby MetaSound, then call the Blueprint helper with shot start/end positions and speed. Test one close pass, one far pass and one subsonic pass.

<!-- IMAGE SLOT: docs/static/images/graphs/graph-projectile-flyby.png -->

## Expected result

Check that close passes are more noticeable and that rejected paths do not play. Listen for any duplicated sounds on moving projectiles.

## Before shipping

- Test empty arrays and stop/retrigger behaviour.
- Test the final recording assets in a packaged Development build.
- Check voice budgets and spatialization in a scene with multiple sound sources.

[Find the node reference](../metasound/README.md).
