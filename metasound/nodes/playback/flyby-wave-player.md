# AP: Flyby Wave Player

**AudioPhysx / Playback** · Unreal Engine 5.8.4 development source

Turn a near-miss calculation into an audible projectile whizz, with an optional ballistic-crack layer.

## Understanding the behaviour

Flyby Wave Player handles **playback**, while a separate Blueprint/world subsystem evaluates the projectile path. The node chooses a whizz recording from `Whizz Waves`, and can additionally select a `Crack Waves` recording when the supplied shock condition requests it. `Distance (m)`, `Speed (m/s)`, `Intensity`, `Speed of Sound (m/s)` and `Shock` describe the result of the path calculation rather than controlling a generic random one-shot.

The chosen recordings render into independent Left and Right output channels. The final Source can still be spatialized by Unreal, and the game-side subsystem can schedule the sound near the closest approach. This division keeps world geometry and projectile event logic off MetaSound's real-time audio thread.

A fast projectile passing just beside the listener should sound noticeably different from one passing tens of metres away. A supersonic close pass may call for both a whizz and a sharp crack, while a slow object or a path whose shock cone does not reach the listener should not automatically create that same crack. The recordings supply the cinematic character; the gameplay calculation supplies the conditions under which they should play.

This is useful with hitscan weapons as well as moving projectiles submitting successive path segments. You do not have to build a custom Chaos rigid-body simulation merely to evaluate a near miss.

## Building and controlling the sound

Create a stereo Source with the Flyby player and supply several whizz variations, optionally adding crack variations. Connect `Out Left` and `Out Right` to the stereo Source and link `On Finished` appropriately. To use the managed Blueprint helper, expose the five Float inputs with the exact `AP.Flyby.*` names given in the Blueprint integration guide, and connect each to its corresponding player control.

First audition with manually supplied values, then call `AP: Play Projectile Flyby` from gameplay using a path start, path end, speed in metres per second and audible radius in metres. The Boolean acceptance result tells you whether the event was scheduled, not necessarily whether audio has reached the listener yet.

`Shock` is an explicit 0/1-style request for the crack layer; it is not a generic measure of volume. `Distance (m)` is measured in **metres** even though Unreal world locations are commonly centimetres. `Intensity` is a normalized strength control. The player exposes `On Rejected` for unavailable content and `On Finished` for natural completion; `Stop` cancels immediately without the normal finish event.

**Practical limitations.** The current system uses simplified constant-speed path and acoustic timing. It should not be marketed as an exact ballistic shock-wave simulation or as a continuous physically traced sound source. Always test duplicate suppression on moving projectiles, sensible near-miss thresholds and the audio Source's spatialization policy with the final packaged build.

==- Exact input and output pins

**Inputs from the current C++ node definition**

- **`Play`** — *Trigger*. Start one flyby, restarting this player if already active.
- **`Stop`** — *Trigger*. Stop immediately; does not emit On Finished.
- **`Whizz Waves`** — *Wave Asset Array*. Randomly chosen rush/whizz Wave Asset Array.
- **`Crack Waves`** — *Wave Asset Array*. Randomly chosen supersonic crack Wave Asset Array.
- **`Distance (m)`** — *Float*. Closest approach in metres. Optional: for custom graph controls.
- **`Speed (m/s)`** — *Float*. Projectile speed in metres/second.
- **`Intensity`** — *Float*. Normalized near-miss strength, 0 to 1.
- **`Speed of Sound (m/s)`** — *Float*. Local speed of sound; used to validate shock playback.
- **`Shock`** — *Float*. 1 = Mach cone reaches listener (0 = ordinary whizz).

**Outputs from the current C++ node definition**

- **`Out Left`** — *Audio buffer*. Left-channel whizz and crack mix. Spatialize in the MetaSound Source.
- **`Out Right`** — *Audio buffer*. Right channel of the stereo playback mix.
- **`On Finished`** — *Trigger*. All started variations have finished naturally.
- **`On Rejected`** — *Trigger*. No playable wave was selected.

===

**Related:** [Flyby Blueprint integration](../../../blueprint/flyby.md) for the exact external input names and path workflow.
