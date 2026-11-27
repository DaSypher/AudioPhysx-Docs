---
label: "FAQ"
icon: question
order: 85
---
# Frequently asked questions

## Is AudioPhysx a replacement for Unreal audio?

No. It extends MetaSounds and game-audio workflows. Unreal's own attenuation, concurrency, mixer, audio components and Sound Cues remain part of a typical project.

## Do I need Chaos physics?

No. The flyby path helpers use supplied positions and speed; the acoustic/material tools can use Blueprint or C++ data provided by your game. Some integrations use world traces or primitive components, but not a bespoke Chaos rigid-body simulation.

## Does every node create audio?

No. Playback nodes output recordings; DSP nodes modify existing audio; utility nodes shape triggers/controls; Blueprint helpers connect game-world information.

## Why is `Out Mono` used so often?

Many nodes deliberately produce mono audio to leave source spatialization and further processing to the MetaSound Source and Unreal audio pipeline.

## Is `On Finished` triggered when I stop a Wave Player?

Not necessarily. On several players, an explicit `Stop` cancels playback without the natural completion event. Consult that player's reference.

## Does changing Acoustic Physical Materials change existing recording assets?

No. Material parameters influence routing/evaluation or sound-selection logic. They don't destructively edit imported Wave Assets.

## Does AudioPhysx include Sound Cue nodes?

Not in the development source represented by this documentation. Sound Cue quality-of-life extensions are planned and should not be advertised as included until shipped.

## Will it work in Unreal Engine 6?

No future UE6 compatibility claim has been verified or promised. Check the supported engine matrix for the version you purchase.
