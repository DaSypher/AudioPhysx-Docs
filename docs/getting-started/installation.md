---
label: "Installation"
icon: download
order: 85
---
# Installing AudioPhysx

The exact installation method depends on whether you received the finished Fab code plugin or a private development source build.

## For a Fab plugin installation

1. Obtain the AudioPhysx plugin for a **supported engine version** through Fab/Epic's plugin installation flow.
2. Open your project and go to **Edit → Plugins**.
3. Search for **AudioPhysx**, enable it if needed and restart the editor when requested.
4. Open a MetaSound Source and search for `AP:` or `AudioPhysx` in the add-node menu.

!!!warning Current status
These steps describe the intended customer workflow. The Fab distribution has not been verified here. Do not claim an engine or platform is supported until you have tested the final packaged plugin.
!!!

## For a source distribution

1. Close Unreal Editor and disable Live Coding.
2. Put the **complete plugin directory** (including its `.uplugin` descriptor) in `YourProject/Plugins/AudioPhysx/`.
3. Regenerate project files if required, and build the Editor target with the supported toolchain.
4. Reopen Unreal Editor and confirm the nodes appear.

Do **not** copy a `Source` ZIP by itself and expect a working plugin: a distributable code plugin also needs its descriptor and appropriate packaging metadata.

<!-- IMAGE SLOT: docs/static/images/setup/plugin-enabled.png -->

## Check the installation

Create a new MetaSound Source and confirm you can add **AP: Random Wave Player**, connect a wave array and play a sample. See [Your first MetaSound](first-metasound.md).

## Typical installation problems

| Symptom | First check |
| --- | --- |
| AudioPhysx doesn't appear in Plugins | Plugin directory structure and `.uplugin` presence |
| Node missing in MetaSound | Plugin enabled, editor restarted, rebuild completed |
| C++ source fails to compile | Match engine version and platform/toolchain, check first compiler error |
| Old node pins or registration errors | Close editor, perform clean rebuild without stale plugin intermediates |

[More troubleshooting](../support/troubleshooting.md)
