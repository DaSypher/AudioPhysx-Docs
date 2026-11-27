# Requirements

The documentation currently targets the **AudioPhysx UE5.8.4 development source**. The final Fab package may have a different verified version matrix; that will be published on [Compatibility](../support/compatibility.md).

## What you'll need

- An Unreal Engine project with the compatible AudioPhysx plugin installed and enabled.
- MetaSound support enabled in the engine and a MetaSound Source to edit.
- Your own licensed Wave Assets for playback demonstrations.
- For the optional acoustic or projectile integrations: a project Blueprint/C++ system that supplies locations, materials, traces or relevant movement data.

## Audio terms used throughout

| Term | Meaning |
| --- | --- |
| Wave Asset | A MetaSound reference to an audio recording selected by a player node. |
| Wave Asset Array | A collection of recordings for variation or layering. |
| Trigger | A sample-addressed MetaSound event such as Play, Stop or On Finished. |
| Out Mono | One mono audio stream; the MetaSound Source can spatialize it downstream. |
| Physical Material | Unreal asset describing a physical surface or material, which AudioPhysx can use for sound choices. |
| Acoustic route | A compact signal containing estimated propagation delay and spectral loss for one selected path. |

## Units

Unreal location/distance values in these inputs are usually **centimetres** unless explicitly marked `(m)`; speed inputs may be **metres per second**; RPM means events per minute. The node labels specify units.
