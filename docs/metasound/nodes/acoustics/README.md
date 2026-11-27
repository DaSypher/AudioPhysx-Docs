---
label: "Acoustics node reference"
icon: broadcast
order: 70
---

# Acoustics nodes

These nodes transform an existing stereo signal using values from a physical or perceptual model. They do not automatically know which wall is between the source and listener or how hard a collision occurred; that information comes from the game or the appropriate AudioPhysx world-side system. The left and right processing histories remain separate.

**[AP: Acoustic Paths](acoustic-paths.md)** — Render the single acoustic route selected by the world solver, including travel delay and frequency-dependent loss, without creating duplicate sound copies.

**[AP: Material Transmission](material-transmission.md)** — Give an obstructed sound a believable tonal change rather than making it merely quieter.

**[AP: Source Directivity](source-directivity.md)** — Make the source sound different when the listener stands in front of it, beside it, or behind it.

**[AP: Impact Dynamics](impact-dynamics.md)** — Use one impact recording more expressively by changing its attack and colour according to how hard the impact was.

**[AP: Early Reflections](early-reflections.md)** — Add short, synthetic reflection taps that suggest nearby boundaries without running a full room simulation.

For a broader explanation, return to the [Acoustics overview](../../acoustics.md).
