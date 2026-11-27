---
label: Acoustic path queries
icon: broadcast
order: 80
---
# Querying acoustic paths

A direct ray between a speaker and listener may cross a barrier. In some scenes, sound could instead travel through an opening or around an obstacle. AudioPhysx's path solver provides a **game-thread approximation** of that situation, producing an acoustic route that the MetaSound can render.

## What the Blueprint actually receives

`AP: Query Acoustic Path` is exposed through `UAPAcousticPathLibrary`. Give it a world context, source position, listener position and optionally a source actor. The returned `FAPAcousticPathResult` describes direct-path obstruction, delay and low/mid/high frequency losses. It can also describe an alternative route, including its proposed emitter location and losses, when one is valid.

The flags are important:

- **`bAroundPathValid`** means the solver found a usable alternate candidate.
- **`bAroundPathSelected`** means the system considers that alternate preferable to the direct path.

A valid path is not automatically the path selected for playback. This distinction helps prevent two sound copies playing at once merely because a doorway route exists.

## Build a small repeatable test

>>> 1. Make a two-area map
Use a source on one side of a simple wall and a listener on the other. Leave a doorway or other controllable opening so there is a meaningful alternate route to compare.

>>> 2. Query the path
Call `AP: Query Acoustic Path` and print direct obstruction, selected-route state, delays and the loss values.

>>> 3. Change only one condition
Move the listener to a clear line of sight, then behind the wall, then near the doorway. Confirm the results change in a way that matches the geometry.

>>> 4. Connect a MetaSound
Use the compact selected-route Float Array with [AP: Acoustic Paths](../metasound/nodes/acoustics/acoustic-paths.md). Listen to the difference only after the geometric result makes sense.
>>>

<!-- IMAGE SLOT: docs/static/images/blueprint/bp-query-acoustic-path.png -->

## Why this runs outside MetaSound

World traces require access to scene geometry. They belong on the **game thread**, not inside a DSP function rendering thousands of audio samples. The managed AudioPhysx world subsystem provides limits and scheduling controls so a large level does not perform unconstrained acoustic queries for every source at every moment.

!!!tip Test data before audio
When a sound seems too muffled, print the selected route first. If the wrong barrier is being found, changing the MetaSound filter will only hide the real problem.
!!!

[Acoustic components](components.md) · [MetaSound route processor](../metasound/nodes/acoustics/acoustic-paths.md)
