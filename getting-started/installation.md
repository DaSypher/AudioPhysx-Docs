# Installing the plugin

AudioPhysx can be installed either as a finished, compatible Fab code plugin or from a complete source distribution. This guide describes both approaches, but the current documentation package does not contain or redistribute the paid plugin source. In particular, a ZIP containing only `Source/` is not by itself a distributable Unreal plugin: the descriptor and any required build configuration still need to be present.

## Install and verify

**If you have the Fab package**, follow the supported Unreal/Fab installation flow for a verified engine version. Open your project, go to **Edit → Plugins** and confirm that AudioPhysx is enabled. Restart the Editor when prompted. The exact Launcher/Fab steps should be checked with the final released package, as the commercial installation has not been independently tested during this documentation task.

**If you have the source distribution**, close Unreal Editor and disable Live Coding. Place the complete plugin directory—including `AudioPhysx.uplugin` and the `Source` folder—under `YourProject/Plugins/AudioPhysx/`. Regenerate project files if necessary, compile the Editor target with the appropriate toolchain, and reopen the project. Do not mix old and new implementations of a node: duplicate registration functions and stale generated headers can cause misleading linker or startup errors.

**Check the result in a MetaSound Source.** Create a stereo MetaSound Source and search for `AP: Random Wave Player` or `AudioPhysx` in the node palette. Confirm the Wave Player has `Out Left` and `Out Right` pins, and confirm that `AP: Stereo to Mono` is available in QoL. This is a useful sanity check that the current stereo build, rather than an older mono DLL, has loaded.

If the plugin appears in the Plugins window but nodes are unavailable, inspect the Editor startup log and the first meaningful build or MetaSound registration message. A successful checkbox state does not prove the module has loaded its native nodes correctly. If you need to clear old build outputs, close the Editor before removing generated `Binaries` and `Intermediate` for a clean source rebuild.

## Avoid damaging existing MetaSounds

A major part of this update changes audio pins from mono to stereo. Back up existing MetaSound assets before refreshing or replacing their AudioPhysx nodes. When you first open an older asset, check every input and output connection rather than assuming Unreal automatically transforms a single mono connection into two independent stereo connections.

New graphs are simplest to author as stereo from the beginning. For world emitters that should remain mono, connect the player or final DSP stage to [AP: Stereo to Mono](stereo-routing.md) immediately before the Source's mono output. Test the finished graph in the Editor, then in a packaged Development build before relying on it in shipping content.
