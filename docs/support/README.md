---
label: "Support & release notes"
icon: help-circle
order: 50
---


# Support and compatibility

AudioPhysx adds native audio players, world-query integrations and DSP nodes to Unreal Engine, so troubleshooting is easiest when you separate **build and registration**, **event and asset playback**, and **world-derived control data**. An Editor plugin that is enabled but has missing nodes suggests a different problem from a Wave Player that starts but is not routed to any Source output.

The [troubleshooting guide](troubleshooting.md) starts from those distinctions. The [FAQ](faq.md) explains why audio nodes are now stereo, how to choose mono spatialization, how physics-related helpers use gameplay data, and which features are actually included in the current source. The [compatibility page](compatibility.md) deliberately distinguishes an intended engine target from a verified, packaged commercial build. [Changelog](changelog.md) records this documentation baseline without inventing a Fab release version.

When reporting a problem, include the exact Unreal Engine version, plugin version or source snapshot, the node or Blueprint function involved, and a minimal reproduction. For a build issue, the first meaningful compiler or linker error is normally more useful than the last line of the build log. For a playback issue, a small screenshot showing Play, both audio channels and completion wiring is often more useful than a full screenshot of a huge production graph.
