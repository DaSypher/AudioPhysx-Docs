# Sound behind a wall

**Primary AudioPhysx tools:** AP: Material Transmission or Acoustic Paths

A good example is a listening experiment, not just a screenshot of connected pins. This exercise explains what content to prepare, which signals the graph needs, and what result you should listen for before increasing complexity.

## Prepare the recording and context

Use a short, bright source such as speech, a hand clap or a mechanical impact. A strong high-frequency component makes it easier to hear what the obstruction processor changes. Put the source behind a simple wall and establish a clear listening reference before adding effects. When the recording is already very dull, it may be difficult to hear the difference between correct transmission and an ineffective setup.

## Assemble the MetaSound and test it

For the simplest comparison, use Material Transmission with a controlled `Obstructed` Boolean and set the high-band loss larger than the low-band loss. Connect `In Left` and `In Right`, then the processed stereo outputs. For world-selected path processing, first print the route from the acoustic Blueprint query and feed its four-value Float Array into Acoustic Paths. Pass the upstream completion trigger into `Source Finished` so delayed audio is not cut off.

## Judge the result in a game

The blocked version should generally become quieter and less bright while still sounding like the same source. If it is overly muffled, check whether Unreal's native occlusion is also active. If the effect appears too late, check the path delay and the amount of delay buffering reserved by the node. A world-derived path model is only as reliable as its collision data and query settings.

A repeatable test in a small scene is more valuable than adding several processors at once. Check the Source's channel layout and all completion events before moving the same graph into a large level. If the audio will ultimately be positioned as a mono point source, audition the [Stereo to Mono](../metasound/nodes/qol/stereo-to-mono.md) version as well as the full stereo path.

[Browse the full node reference](../metasound/README.md) for exact control types and limitations.
