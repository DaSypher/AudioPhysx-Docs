---
icon: download
---
# Installation

## Prerequisites

- An Unreal Engine installation compatible with the **specific AudioPhysx package** you downloaded.
- The AudioPhysx code plugin purchased through Fab, or its development build from the author.

## Install and enable

1. Install the plugin through Fab using its supported installation workflow, or place the distributed plugin in your Unreal project's `Plugins/AudioPhysx/` folder if using a source distribution.
2. Open Unreal Editor, go to **Edit → Plugins**, and check that AudioPhysx is enabled.
3. Restart the editor if requested.
4. Create or open a MetaSound asset and search the node palette for `AudioPhysx`.

If compiling a source distribution, match the supported engine/toolchain combination and use a full Editor build. Do not copy stale `Binaries` or `Intermediate` from a different machine.

## Next steps

Follow the [first MetaSound example](first-metasound.md).

> TODO: Before publishing, verify these installation steps against a **fresh Blueprint-only project** and an actual Fab-installed build. Add screenshots for Windows, and document other platforms only if tested.
