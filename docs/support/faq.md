---
label: Frequently asked questions
icon: question
order: 85
---
# Frequently asked questions

## Is AudioPhysx a replacement for MetaSounds or Unreal Audio?

No. It provides additional C++ nodes and Blueprint integration for the existing Unreal audio pipeline. You still use MetaSound Sources, the mixer, spatialization, Sound Attenuation and concurrency features as appropriate for your game.

## Why are so many outputs mono?

Mono is a practical source format for many spatial game sounds. It lets Unreal handle the source's 3D positioning and means an acoustic processor can work on one clearly defined signal. It does not mean every sound in your game must be mono.

## Does it generate all realistic audio procedurally?

No. Many nodes play or transform your own recordings. The physically inspired processors model particular behaviours such as attenuation, delay, directionality or early reflections; they are not a complete acoustic simulation of the game world.

## Do I need Chaos physics?

No. The flyby functions operate on supplied projectile path segments and speed. Acoustic path helpers can use ordinary world queries and level components. You may integrate them with a Chaos-driven game, but Chaos is not required for the core workflows described here.

## What's the difference between Surface and PhysMat playback?

Surface Wave Player chooses from a category such as a physical-surface type. PhysMat Wave Player can distinguish specific Physical Material asset paths. Use the broader category when the sound should be shared across several surfaces, and the exact path when you need a more detailed selection.

## Why doesn't `Stop` always fire `On Finished`?

`Stop` can mean an explicit cancellation. Natural completion means the recording has actually ended. Some nodes distinguish those two behaviours so gameplay can tell the difference. Read the particular player's reference before wiring Source completion.

## Can I use a Sound Cue instead of MetaSound?

Unreal's native Sound Cues can still be used wherever your workflow calls for them. AudioPhysx's **custom Sound Cue QoL nodes are planned**, not included in the reviewed development source. Current native node references are MetaSound-focused.

## Will the plugin work in UE6 without updates?

No UE6 compatibility has been verified or promised. Native code plugins depend on engine APIs, and some current AudioPhysx player and dynamic-interface implementations use APIs with compatibility risks. Follow the [published support matrix](compatibility.md) for the specific product version you intend to use.

## Are acoustic material numbers scientifically measured?

Not by default. AudioPhysx offers authored and simplified modelling choices. Material values must be selected meaningfully for the game, and a convincing result is not the same thing as a validated laboratory measurement.
