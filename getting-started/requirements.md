# Requirements and terminology

AudioPhysx is a native C++ plugin for Unreal Engine. The code reviewed for this edition targets **UE 5.8.4** and includes the stereo conversion and RPM playback system. That establishes what the source is intended to build against; it does not prove that a final Fab distribution has passed testing in every target build configuration. For current support claims, consult the [compatibility page](../support/compatibility.md).

You need a compatible Unreal project with MetaSounds enabled, the complete AudioPhysx plugin installed and some legal Wave Assets for the tutorials. More advanced systems require meaningful game data: a projectile path, an impact location, source-listener separation, a hit Physical Material or an acoustic barrier and portal setup. The audio nodes cannot invent those values from a waveform alone.

## Understanding the pins

A **Wave Asset** is a reference to an imported recording. A **Wave Asset Array** stores several recordings for variation, selection or layering. The array itself is not an audio stream; a Wave Player decides what to do with its contents when an event arrives.

An **audio buffer** carries actual samples. With the current stereo AudioPhysx convention, you normally connect the Left audio channel to the Left input of the next processor, and Right to Right. The final MetaSound Source output format should match the signal you want to render. If you intentionally need one mono stream, [Stereo to Mono](stereo-routing.md) makes that conversion explicit.

A **Trigger** represents a point in time: play, stop, release, reset or announce completion. Triggers are not audio signals. A **Float**, **Boolean**, **Integer**, **String** or **Float Array** is a control value; it can describe distance, acoustic loss, random probability or surface identity without being either an event or an audio channel.

## Units are not optional

Most Unreal world coordinates and many AudioPhysx distances are expressed in **centimetres**. Other pins are explicitly labelled metres `(m)`, metres per second `(m/s)`, milliseconds `(ms)`, seconds `(s)`, decibels `(dB)`, hertz `(Hz)`, kilopascals `(kPa)` or semitones `(st)`. Use the unit printed on the pin, because there is no universal convention that all values in the plugin are metres.

For example, a projectile whose closest approach is 500 Unreal units away is usually **500 cm, or 5 m**. Feeding the number 500 to the flyby player's `Distance (m)` would tell it the projectile passed half a kilometre away. Likewise, a pitch ratio from Doppler Ratio is not interchangeable with a semitone pitch input.

If an effect sounds unexpectedly late, quiet or bright, verify the values and units before changing the DSP. Errors in source data can be far more dramatic than errors in a filter setting.
