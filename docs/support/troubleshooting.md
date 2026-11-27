---
label: "Troubleshooting"
icon: tools
order: 90
---
# Troubleshooting

## No AudioPhysx nodes appear

1. Check **Edit → Plugins** and verify the plugin is enabled.
2. Confirm that the installed plugin contains a `.uplugin` descriptor and supported compiled module.
3. Restart Unreal Editor after enabling/rebuilding.
4. Search the MetaSound add-node menu for `AP:` and check the `AudioPhysx` categories.

## Node exists but produces silence

- Confirm a playable Wave Asset is assigned and not an empty array.
- Check trigger wiring and connect `Out Mono` to an active audio output.
- Verify attenuation, distance controls and any required material/route inputs.
- Check whether `On Rejected` is being emitted (where available).

## Sequencer doesn't finish

- `Loop Sequence` may be enabled.
- `Start Loop End Player` requires `Stop Firing` to request release.
- A downstream delay or reflection node may have an additional audible tail.

## Dynamic pins changed or broke a graph

- Back up the MetaSound asset before changing global route configurations.
- For `Surface Wave Player`, review Surface Audio settings, restart and reconnect affected pins.
- For expandable input/output groups, confirm the current instance counts.

## C++ build errors

1. Disable Live Coding and close the Editor.
2. Read the **first actual compiler error**, not the last cascade error.
3. Verify supported engine/toolchain and source package version.
4. If reflected headers changed or compiler output is stale, clean plugin `Binaries/` and `Intermediate/` before regenerating/rebuilding.
5. Don't merge two versions of the same implementation file into `Source`.

## Packaged game differs from Editor

Check cooked Wave Assets, AudioPhysx module loading, asset references, concurrency and audio device initialization in a **Development package**, followed by Shipping verification. Editor preview alone is insufficient.

## Report a reproducible problem

Include UE version, plugin version, operating system, exact input settings, expected result, actual result, log and a minimal graph screenshot.
