# Installing AudioPhysx

The exact steps depend on whether you're using a **Fab-distributed plugin** or a **source checkout**. Choose the relevant path below. In either case, the first goal is to see the AudioPhysx node categories in the MetaSound editor.

+++ Fab / launcher installation

When the commercial package is available for your verified engine version, install it through the Fab/Epic workflow, open your project and enable **AudioPhysx** under **Edit → Plugins** if it is not enabled already. Restart Unreal when prompted.

The final Fab delivery workflow has **not been validated** for this development documentation. Use the supported-engine list published with the actual product package.

+++ Source checkout

>>> 1. Close Unreal and disable Live Coding
A running editor can hold previously compiled module DLLs and generated build state.

>>> 2. Install the complete plugin
Copy the full `AudioPhysx` plugin directory—**including its `.uplugin` descriptor**—into `YourProject/Plugins/AudioPhysx/`.

>>> 3. Build the Editor target
Regenerate project files if required, then build the project Editor target with the Unreal-compatible toolchain.

>>> 4. Reopen the project
Enable the plugin if prompted, restart if necessary, and open a MetaSound Source to search for `AP:`.
>>>

+++

## Confirm it works

Create a mono MetaSound Source and search the add-node menu for **AP: Sequence Wave Player** under `AudioPhysx → Playback`. If it appears, continue with [Your first MetaSound](first-metasound.md). A successful plugin listing in the Plugins browser alone does not prove every audio node can play correctly.

## If the nodes are missing

A missing node may mean the plugin was not enabled, the compiled module failed to load, or an old editor session is still open. For a source build, pay attention to the **first** compiler error rather than secondary failures. If reflected headers or generated build outputs are stale, close Unreal and clean the plugin's `Binaries` and `Intermediate` directories before regenerating and rebuilding.

Do not merge two source versions that contain the same node under different filenames; duplicate MetaSound registration can produce linker or runtime registration problems.

[Read build troubleshooting](../support/troubleshooting.md)
