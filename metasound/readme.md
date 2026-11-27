# The AudioPhysx MetaSound library

The current native source contains **24 nodes**. They are divided by the job they perform rather than the feature that first inspired them: ten Wave Players for selecting recordings and scheduling playback, five acoustic processors for changing the character of audio, four propagation-related tools (one of which emits only a control value), and five QoL utilities including the new stereo-to-mono converter.

Understanding the difference between these groups is important. A playback node needs an event and usually some Wave Assets. A DSP processor needs an existing audio stream and physical or authored parameters. A control utility may have no audio pins at all because it decides which event passes or what number to use elsewhere. The pages are written to make those responsibilities clear before listing pin names.

## Navigate by what you are building

[!card layout="compact" title="Playback" text="Random, shuffle-bag, layered, sequenced, distance- and material-based players, held RPM effects, and flybys."](playback-nodes/README.md)

[!card layout="compact" title="Acoustics" text="Selected acoustic routes, transmission through materials, directionality, impacts and early reflections."](acoustics-nodes/README.md)

[!card layout="compact" title="Propagation" text="Travel-time delay, dynamic motion, Doppler ratio and atmospheric absorption."](propagation-nodes/README.md)

[!card layout="compact" title="QoL" text="Smooth values, limit and randomize triggers, switch distance branches, and fold stereo to mono."](qol-nodes/README.md)

## How to read the reference pages

Each node begins with a practical explanation of the problem it solves. You will then find a more detailed discussion of what the node does to the sound or to the event flow, a real game-audio example, setup guidance and the risks worth testing. The complete pin descriptions are still present in an expandable **Exact input and output pins** section. They are extracted from the current C++ declarations, so you do not have to trust an older screenshot for the correct pin names.

The stereo convention is consistent across the audio processors: the input is typically `In Left` and `In Right`, and the output is `Out Left` and `Out Right`. Wave Players generally supply `Out Left` and `Out Right`. Control-only nodes are not artificially given audio channels. `AP: Stereo to Mono` deliberately outputs `Out Mono` because that is the point of the converter. If you are migrating an older MetaSound, see [stereo routing and migration](../getting-started/stereo-routing.md) before saving the revised graph.

**Prefer a worked example?** Open [Node tutorials and screenshots](node-tutorials.md), then expand a category in the sidebar. Each node has its own page and a five-step basic graph.
