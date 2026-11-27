---
label: "Examples and recipes"
icon: beaker
order: 80
---


# Learn by building something audible

Node reference pages explain individual tools; the examples show how several parts fit together in an actual listening task. They deliberately begin with ordinary Wave Assets and small MetaSound graphs rather than a large demonstration project that needs dozens of dependencies. Once you understand the basic routing, you can replace the test sounds with your game's own authored content.

**For playback**, try [randomized one-shots](randomized-one-shot.md) or an [automatic weapon with RPM](automatic-weapon.md). These show the distinction between selecting a recording and scheduling it in time. A [random multi-stage action](random-sequence.md) demonstrates how each stage can vary while retaining the order of the action. The [material footstep recipe](material-footsteps.md) connects gameplay surface data to sound selection.

**For world-reactive audio**, the [flyby exercise](projectile-flyby.md) separates projectile geometry from audio playback, while the [acoustic obstruction example](acoustic-obstruction.md) compares a simple authored barrier filter with a selected world route. Both are designed to be understood by printing the gameplay result before adjusting the sound.

These recipes use the new stereo conventions. Unless a specific example intentionally downmixes, audio-bearing connections should run Left to Left and Right to Right. If you are building a precisely localized point emitter, the [stereo routing guide](../getting-started/stereo-routing.md) explains when and how to introduce Stereo to Mono at the end of the chain.

<!-- IMAGE SLOT: site/static/images/brand/hero-demos.png -->

Use your own or appropriately licensed recordings for these exercises. A test that sounds poor because the assets contain leading silence, mismatched loudness or phase problems is not a reliable evaluation of the node's actual timing and processing behaviour.
