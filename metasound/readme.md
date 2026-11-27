# The AudioPhysx MetaSound library

The current native source contains **24 nodes**. They are divided by the job they perform rather than the feature that first inspired them: ten Wave Players for selecting recordings and scheduling playback, five acoustic processors for changing the character of audio, four propagation-related tools (one of which emits only a control value), and five QoL utilities including the new stereo-to-mono converter.

Understanding the difference between these groups is important. A playback node needs an event and usually some Wave Assets. A DSP processor needs an existing audio stream and physical or authored parameters. A control utility may have no audio pins at all because it decides which event passes or what number to use elsewhere. The pages are written to make those responsibilities clear before listing pin names.

## Find the nodes you need

The four categories expand directly in the **left sidebar**. Select a node to open its full explanation, five-step setup guide, stereo routing instructions, and expandable pin reference. There are no separate category-note pages to click through.

**Playback** handles Wave Asset playback, variation and timing. Start with [Random Wave Player](playback-nodes/random-wave-player.md) for one-shot variation, [Random Sequence](playback-nodes/random-sequence-wave-player.md) for multi-stage events, or [Start Loop End](playback-nodes/start-loop-end.md) for RPM-controlled firing and held actions.

**Acoustics** changes the character of an existing sound using world information or authored controls. Try [Material Transmission](acoustics-nodes/material-transmission.md) to create a blocked-sound effect, or [Acoustic Paths](acoustics-nodes/acoustic-paths.md) for a selected path's delay and frequency-band losses.

**Propagation** concerns travel time, source movement and absorption through air. [Distance Delay](propagation-nodes/distance-delay.md) works with latched travel-time delays; [Dynamic Propagation](propagation-nodes/dynamic-propagation.md) responds to moving sources.

**QoL** streamlines control logic and conversion. [Trigger Cooldown](qol-nodes/trigger-cooldown.md) limits rapid events, [Float Smoother](qol-nodes/float-smoother.md) softens parameter changes, and [Stereo to Mono](qol-nodes/stereo-to-mono.md) folds stereo down for a mono signal path.

## How to read the reference pages

Each node begins with a practical explanation of the problem it solves. You will then find a more detailed discussion of what the node does to the sound or to the event flow, a real game-audio example, setup guidance and the risks worth testing. The complete pin descriptions are still present in an expandable **Exact input and output pins** section. They are extracted from the current C++ declarations, so you do not have to trust an older screenshot for the correct pin names.

The stereo convention is consistent across the audio processors: the input is typically `In Left` and `In Right`, and the output is `Out Left` and `Out Right`. Wave Players generally supply `Out Left` and `Out Right`. Control-only nodes are not artificially given audio channels. `AP: Stereo to Mono` deliberately outputs `Out Mono` because that is the point of the converter. If you are migrating an older MetaSound, see [stereo routing and migration](../getting-started/stereo-routing.md) before saving the revised graph.

**Want a complete walkthrough?** [Build your first MetaSound](../getting-started/first-metasound.md), then expand any node category in the sidebar. Every node has a dedicated five-step guide.
