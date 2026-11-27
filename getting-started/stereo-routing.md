# Stereo routing and deliberate mono conversion

AudioPhysx's current design is **stereo throughout audio-bearing playback and processing**, with a dedicated node for conversion to mono. This is useful because it avoids discarding information before the sound designer has decided whether that information matters. It is not a statement that stereo is always acoustically preferable for every source in a 3D game.

Most Wave Players expose `Out Left` and `Out Right`. Acoustic processors commonly expect `In Left` and `In Right` and expose `Out Left` and `Out Right` again. Their delay and filter histories are separate, so a stereo recording can travel through the chain without being summed into mono at the first stage. The world controls—distance, obstruction, material or speed—are often shared across both channels because they describe one source-to-listener relationship.

## How to connect stereo nodes

A basic full-stereo path might begin with `AP: Random Wave Player`, continue through `AP: Material Transmission`, and then feed a stereo MetaSound Source. Connect the player's Left output to the processor's Left input and Right to Right. The processor's Left and Right outputs then connect to the corresponding Source channels. If you accidentally connect the same channel to both inputs, you may hear duplicated mono rather than the original stereo recording.

This also means you can combine source design and processing more freely. A Layered Wave Player can mix a stereo mechanical texture with other recordings; Early Reflections can preserve independent channel history; Dynamic Propagation can delay each stereo channel without first summing them. The effects still have limits and shared physical controls, but stereo content is no longer discarded merely because the plugin's internal renderer has a mono output.

## When mono is still the better result

A small object making a footstep, a gun muzzle report or a collision at a known world position often behaves conceptually as a **point source**. Unreal's spatializer may be better suited to positioning one mono signal in 3D than a wide stereo recording whose left/right cues were captured or designed for a different listening position. The correct choice depends on the type of sound, the project's spatialization settings and the listening test.

To downmix, place **AP: Stereo to Mono** after the last stereo processor. Connect `Out Left` to `In Left` and `Out Right` to `In Right`; then feed its `Out Mono` into a mono MetaSound output. The node uses a simple sample-by-sample average:

```text
Mono = 0.5 × (Left + Right)
```

This keeps dual-mono content at the same level rather than summing it 6 dB hotter. It cannot preserve the original stereo field, and opposite-polarity material may cancel during the fold-down. Always audition an important effect in mono before shipping it—especially if you have layered stereo bass or strongly phase-shifted recordings.

## Migrating existing graphs

If your MetaSound was authored with an older AudioPhysx version, back it up before opening it in the stereo build. Verify the installed module is actually the stereo version, inspect saved node pins, reconnect Left and Right audio paths, and change the MetaSound Source output format only when the finished sound design needs it. Mono-only graphs can use the converter rather than forcing the entire pipeline back to mono.

Do not treat trigger and Float nodes as part of this migration. `AP: Doppler Ratio`, `AP: Float Smoother`, `AP: Trigger Probability`, `AP: Trigger Cooldown` and `AP: Distance Switch` do not render audio samples, so their existing event/number pin contracts remain appropriate. **AP: Stereo to Mono** is the deliberate mono-output exception. Recompile the graph and check real stereo separation using a test recording with noticeably different Left and Right content.

Read the [Stereo to Mono node reference](../metasound/qol-nodes/stereo-to-mono.md) for the exact pin names and limitations.
