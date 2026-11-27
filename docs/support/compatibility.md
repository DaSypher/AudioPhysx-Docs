---
label: "Compatibility"
icon: shield-check
order: 80
---


# Compatibility and technical boundaries

These pages are based on the **AudioPhysx UE 5.8.4 source package uploaded for this documentation revision**. They describe what is present in the code and how it is intended to be used. They do not constitute independent evidence that the plugin compiles, auditions or packages successfully in every target configuration. Before marketing a Fab release, run a clean-project installation and verify the exact shipping archive rather than a development source tree with additional local dependencies.

**Source target:** Unreal Engine 5.8.4. **New audio convention:** stereo playback/DSP output, with the explicit Stereo to Mono converter. **Pending verification:** compilation and audio tests on the exact release archive, clean Blueprint-only project installation, packaged Development and Shipping builds, and any operating system or Unreal Engine version intended to be listed as supported. **Not claimed:** automatic compatibility with future UE6 releases or untested target platforms.

## What to test before listing a supported version

Create a fresh project with the intended supported engine, install only the plugin files customers will receive and confirm that all native node registrations appear. Test stereo separation using a Wave Asset with different Left and Right content. Test the Stereo to Mono average, including the effect of phase cancellation. Exercise Random Wave Player with overlapping voices, Sequence and Random Sequence with varying recording lengths, and Start Loop End at zero and positive RPM with both release settings.

Then test one representative acoustic processor with a stereo input, a managed acoustic path with an actual barrier and a flyby triggered by a real path segment. Use a Development package to diagnose unexpected behaviour, then verify a Shipping package. Performance should be tested with a realistic count of emitters and voices, not just one preview graph.

The code includes some engine-internal playback dependencies, dynamic configurable pin layouts and simplified acoustic models. A private playback adapter reduces the number of future engine-specific call sites but does not guarantee cross-version compatibility. These are practical engineering boundaries to document, not excuses to claim functionality without listening tests.

For the final commercial documentation, replace this provisional statement with a dated matrix of **engine version, operating system, build configuration and verified result**. Add only combinations you have actually tested. If a future engine requires source changes, describe the new compatible release instead of implying that a binary built for an older engine must work unchanged.
