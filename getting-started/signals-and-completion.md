# Triggers, audio buffers and completion

A MetaSound graph contains different kinds of wires because it describes both **events** and **continuous sound**. `Play`, `Stop`, `Reset` and `On Finished` are triggers that represent moments. `Out Left`, `Out Right`, `In Left` and `In Right` carry the audio sample buffers. A Float such as `Distance (cm)` or `Impact Strength` describes a changing control value but does not itself produce sound.

Confusing these responsibilities is a common reason for nodes that appear to work individually but produce silence inside a larger graph. For example, a Wave Player can receive Play and load a valid sample without any audible result if its audio outputs are not connected to the Source. Conversely, an acoustic processor can have both audio channels connected but remain in the wrong state if the required material, route or obstruction input never updates.

## Stopping and finishing are different events

A sound may finish naturally after rendering its final sample, or it may be explicitly cancelled by gameplay. Many AudioPhysx players reserve `On Finished` for natural completion. For that reason, pressing `Stop` should not be assumed to fire the same trigger as the end of the recording. `Stop Firing` on Start Loop End has another meaning: it requests the **release phase** and allows the ending to play.

Downstream processors introduce another consideration. A Wave Player may finish its original recording while Acoustic Paths is still delivering delayed samples or Early Reflections still has audible taps. In such a graph, the processor's `Source Finished` input can receive the player's completion signal, and the processor's own `On Finished` can indicate when the extended audible tail is complete. Ending the MetaSound Source too early cuts off that processing.

## Keep the signal layout explicit

When routing the current stereo nodes, move each channel through the intended Left and Right path. The two channels carry separate audio buffer data; duplicating the Left buffer into both inputs is not equivalent to preserving a stereo recording. When you intentionally choose a mono Source, make the fold-down explicit with Stereo to Mono rather than relying on ambiguous routing or connecting a stereo pin into a mono-only input.

Some nodes have **expandable pin groups** for waves, steps or distance bands. These are part of the authored graph layout. Surface Wave Player can additionally generate pins from project settings. If an interface changes, check the actual pins and connections before saving migrated assets.
