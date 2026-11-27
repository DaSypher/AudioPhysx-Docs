# Troubleshooting AudioPhysx

When an effect does not behave as expected, debug from the outside in. First verify Unreal can play the chosen recording. Then verify the MetaSound receives its starting trigger. Next confirm the expected Left and Right audio buffers reach the Source output. Only after this works should you investigate acoustic path data, material configuration, voice limits or the extra DSP stages in the chain. That process may feel slower than changing settings randomly, but it usually identifies the real problem with fewer false fixes.

## Missing nodes, silence or incorrect audio layout

If the AudioPhysx nodes do not appear in the palette, check **Edit → Plugins** and confirm that the correct native module loaded. After replacing source files, close Unreal Editor, disable Live Coding and rebuild for the intended engine version. A duplicate `.cpp` file or a stale binary from an older plugin version can make registration confusing even if the project appears to launch normally.

If a node is present but silent, use one known-good Wave Asset and a simple Source. Make sure the requested array actually contains playable recordings, `Play` reaches the correct input and both `Out Left` and `Out Right` are connected as intended. The stereo upgrade may leave older saved graphs with missing or stale mono connections. A Source set to Stereo needs the correct output channel routing; a Source deliberately set to Mono needs an explicit Stereo to Mono path when using AudioPhysx's stereo outputs.

If a player offers `On Rejected`, observe it while testing. It can distinguish a failed start request from an audible voice that happens to be attenuated or spatialized out of hearing range. Check the Selected Index and active-voice diagnostics where those are provided.

## Playback timing and completion

Sequence Wave Player advances after one recording actually finishes. Random Sequence makes a new selection at each stage and follows the same completion-driven timing. Start Loop End is different: its positive RPM setting starts middle shots at scheduled intervals and waits for `Stop Firing` before entering its ending phase. If you never supply that release event, it is not expected to finish like an ordinary one-shot.

A downstream Acoustic Paths or Early Reflections node may continue to produce audio after the original Wave Player finishes. Pass the player's `On Finished` to `Source Finished` on the processor and use the processor's own completion output where appropriate. Otherwise a Source-level completion connection can kill the final delayed samples. Conversely, do not automatically assume explicit `Stop` emits a natural-completion trigger; the detailed node pages explain cancellation behaviour.

## Incorrect physics, material or environment behaviour

If PhysMat Wave Player always uses the fallback pool, print the **exact Physical Material asset path** coming from the hit result. If Surface Wave Player selects the wrong pool, check the `EPhysicalSurface` integer and the configured route list. Changes to surface-specific routes can alter dynamic pins, so back up and inspect affected MetaSound assets after changing those settings.

If flyby playback does not happen, call `AP: Calculate Flyby` and inspect `bAudible`, closest distance and shock state before scheduling audio. The path endpoints use Unreal world coordinates, while the audible radius and speed inputs use metres and metres per second. If Acoustic Paths sounds too dark or delayed, inspect the selected four-value route array and make sure its order is delay, low loss, mid loss, high loss. Do not assume a well-functioning filter can correct wrong world data.

## Editor works but packaged game does not

A successful Editor compile or MetaSound preview is not complete runtime verification. Test a clean installation in a new project and package Development and Shipping configurations for each platform you intend to claim. Verify cooked Wave Assets, module loading, engine API compatibility and audio-device behaviour with the exact commercial distribution rather than a development folder that may contain extra files.

When asking for help, share a minimal graph with the relevant pin connections and the first meaningful log error. Keep personal project paths, account details and client or private data out of public issue reports.
