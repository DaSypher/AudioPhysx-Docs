# Before you begin

AudioPhysx is a native Unreal Engine **C++ plugin**. This documentation currently reflects a development build for **UE 5.8.4**; confirm the final supported engine versions on [Compatibility](../support/compatibility.md) before installing a commercial package.

You'll need an Unreal project with MetaSounds available, a working AudioPhysx installation, and appropriately licensed audio recordings for the playback tutorials. The more advanced acoustic and flyby workflows also need game-provided positions, traces or material data.

## The four things you connect most often

**Wave Asset** is a reference to an imported sound recording. A **Wave Asset Array** holds several such references; it does not itself play multiple recordings simultaneously unless the chosen player is designed to do that.

**Trigger** means *something happens at this moment*. `Play`, `Stop Firing` and `On Finished` are events, not audio streams. A trigger might be issued by another MetaSound node or by a gameplay parameter/event.

**Audio** pins carry actual sample buffers. `Out Mono` is a one-channel audio stream. That mono output can be routed through additional processing and then spatialized by Unreal's broader audio system.

**Control** pins carry numbers, Booleans, arrays or material identifiers. For example, a player may use a `Distance (cm)` control to select an appropriate recording before playback begins.

## Units are part of the contract

- **cm** — centimetres. Unreal world positions are generally expressed in centimetres.
- **m** — metres. Some AudioPhysx physical models and flyby inputs use metres instead.
- **m/s** — metres per second; do not confuse this with Unreal's centimetres-per-second velocity values.
- **ms** — milliseconds, one thousandth of a second.
- **dB** — decibels, used for level or frequency-band loss. A dB number is not a linear gain multiplier.
- **st** — semitones, a unit of musical pitch interval.
- **RPM** — events or rounds per minute, used for the middle of Start Loop End playback.

!!!warning Watch your conversions
A projectile 500 Unreal units away is typically **500 cm = 5 m**. Feeding `500` directly to a pin labelled `Distance (m)` would be a hundredfold distance error.
!!!

## What this plugin does not replace

AudioPhysx extends, rather than replaces, Unreal's core audio features. You still use MetaSound Sources, audio components, Sound Attenuation, concurrency settings and the Audio Mixer where relevant. Acoustic modelling nodes also need meaningful world data; they do not automatically know your level geometry from the audio samples alone.

[Next: Install AudioPhysx](installation.md)
