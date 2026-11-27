---
label: "Setup checklist"
icon: checklist
order: 70
---


# A practical setup checklist

Most silent or incorrect AudioPhysx graphs can be diagnosed by working from the simplest part of the chain outward. First make sure a known-good Wave Asset plays through a basic stereo Source with the correct `Out Left` and `Out Right` wiring. Only then connect random selection, material routing, time delay or a world acoustic parameter. This separates an asset/import problem from a source-graph problem and from an acoustic-world problem.

**When audio is silent**, check that the correct start trigger actually reaches the node, that the relevant recording arrays contain playable assets, and that you have connected the outputs to an active MetaSound Source. For players that can reject a request, inspect `On Rejected` or an index output before assuming Unreal audio itself is failing.

**When timing is wrong**, distinguish a completion-driven sequence from RPM scheduling. Sequence Wave Player advances only when the current recording finishes. Start Loop End with positive RPM starts middle shots by a fixed interval and needs `Stop Firing` to enter the release phase. An extra Distance Delay or Acoustic Paths stage can delay the audible output even after the original playback has begun.

**When world-driven sound is wrong**, print the source-listener distance, physical material, obstruction result or selected acoustic route. Check units carefully: centimetres, metres and metres per second are used for different controls. A perfectly functioning filter cannot make an incorrect material path or invalid world trace meaningful.

**Before shipping**, test the exact plugin package in a clean project and compare Editor preview with packaged Development and Shipping audio. Include stereo and mono recordings, empty arrays, rapid retriggering and more than one simultaneously active sound. A clean Editor build is important, but it does not prove all runtime platform behaviour.
