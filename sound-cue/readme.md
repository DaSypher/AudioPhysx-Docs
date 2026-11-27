# Sound Cue support — planned

AudioPhysx currently focuses its native node library on **MetaSounds**. Sound Cue QoL additions are part of the proposed commercial roadmap, but **no custom `USoundNode` implementation is included in the reviewed development baseline**.

## Why consider Sound Cue extensions?

Sound Cues already contain useful random, modulation, switching and concatenation facilities. A new AudioPhysx node should only be added when it removes substantial graph complexity or improves everyday authoring. Building a second copy of every MetaSound DSP node would add maintenance cost without offering Sound Cue users much benefit.

The first possible additions are a **Smart Random** control with cohesive selection and repeat behaviour, and a **Random Sequence** that keeps stages in order but chooses variations at each stage. These are concepts, not shipped features.

!!!info Feature availability
Do not assume the Sound Cue examples described here are available in the current plugin. The navigation and documentation will be updated when an implementation has passed runtime and packaged-build testing.
!!!

In the meantime, use the [MetaSound Playback tools](../metasound/playback.md) for the equivalent audio workflows, or Unreal's built-in Sound Cue nodes where appropriate.
