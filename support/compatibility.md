# Engine and platform compatibility

A plugin is only supported where its **exact distributable build** has been compiled, loaded and tested. The current docs reflect the UE 5.8.4 development source reviewed on **27 November 2026**; the final Fab release package has not yet passed a complete independently verified matrix.

## What is known today

**Developer-reported:** The AudioPhysx UE 5.8.4 Editor baseline has compiled and the existing node set has undergone iterative in-project testing. This is not evidence that every Wave Player, every asset type or every platform has been verified.

**Still to verify:** A clean install in a new Blueprint-only project; packaged Development and Shipping builds; all playback edge cases; and any platform outside the project's tested local environment.

**Not claimed:** Compatibility with Unreal Engine 6 or untested desktop, mobile or console targets.

!!!warning Before you release
Do not replace this section with a generic “works with all versions” claim. Maintain a list of tested **engine versions, operating systems and packaged configurations** derived from the exact Fab distribution.
!!!

## Technical constraints to understand

AudioPhysx currently isolates Unreal's internal `FSoundWaveProxyPlayer` in a shared adapter, but that API remains an engine-version risk. Some dynamic MetaSound sub-interfaces are experimental. Surface Wave Player's pin layout can depend on project settings, and flyby/acoustic models include deliberate approximations.

The purpose of listing these constraints is to explain real boundaries, not to imply the whole plugin is unstable. They tell users where engine updates and saved-graph changes deserve additional testing.

## A release verification routine

>>> 1. Test the exact ZIP or Fab package
Create a fresh project and install only what buyers will receive. A source tree with extra development files may hide missing runtime dependencies.

>>> 2. Verify basic playback
Test an ordinary one-shot, a random sequence, an RPM-controlled held sequence, and a flyby in a clean level.

>>> 3. Package and run
Build Development and Shipping packages for each platform you intend to claim. Listen to real runtime output, not just the editor's preview.

>>> 4. Record the result
Add the tested platform, engine version, plugin version and date to the supported-product release notes.
>>>
