# Quick setup checklist

- [ ] AudioPhysx plugin enabled and visible in **Edit → Plugins**.
- [ ] Relevant Wave Assets import and audition correctly in Unreal.
- [ ] MetaSound source output channel layout matches the graph.
- [ ] `Play` or other start trigger is connected.
- [ ] `Out Mono` is connected to the intended graph output.
- [ ] Completion event is connected appropriately, including any downstream audio tails.
- [ ] Dynamic input groups contain the expected slots and connections.
- [ ] Project settings and physical-material routes are configured if the node needs them.
- [ ] Feature works in standalone play and in a packaged Development build before shipping.

If a sound is silent, use [Troubleshooting](../support/troubleshooting.md).
