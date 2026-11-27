---
label: "Home"
icon: home
order: 100
---
# AudioPhysx

**Build more expressive game audio with less MetaSound wiring.**

AudioPhysx is an Unreal Engine C++ audio toolkit focused on **sample playback, procedural acoustic behaviour, physical-material routing and Blueprint audio integration**. It provides native MetaSound nodes intended to simplify common game-audio tasks while keeping the important sound-design controls exposed.

!!!info Development documentation
This site documents the current AudioPhysx **UE5.8.4 development source**, including the latest Start Loop End RPM change. The commercial release and supported-platform matrix are not yet finalized. Review [compatibility](support/compatibility.md) before using these pages as a release guarantee.
!!!

<!-- HERO IMAGE SLOT: docs/static/images/brand/hero-audiophysx.png -->

## Start here

1. [Install AudioPhysx](getting-started/installation.md) into your Unreal Engine project.
2. [Create your first AudioPhysx MetaSound](getting-started/first-metasound.md).
3. Explore the [MetaSound node catalogue](metasound/README.md) or [Blueprint integrations](blueprint/README.md).
4. Follow a [practical recipe](examples/README.md).

## What can AudioPhysx do?

| Playback and variation | Acoustic behaviour | Game integration |
| --- | --- | --- |
| Random, weighted and shuffle-bag selection | Acoustic paths and transmission | Blueprint playback helpers |
| Sequence and random-sequence players | Dynamic propagation and Doppler control | Projectile flyby path calculations |
| Layered one-shots and intro/loop/outro | Atmospheric absorption and reflections | Acoustic components and materials |
| RPM-driven overlapping middle shots | Source directivity and impact shaping | Material- and surface-aware sounds |

## Find your tool

- [Playback nodes](metasound/playback.md) — randomized sounds, sequences, layers and specialized players.
- [Acoustics nodes](metasound/acoustics.md) — material transmission, paths, impact shaping, reflections and directivity.
- [Propagation nodes](metasound/propagation.md) — delay, air absorption and Doppler-inspired processing.
- [QoL nodes](metasound/qol.md) — control smoothing, trigger probability, cooldowns and routing.
- [Blueprint integration](blueprint/README.md) — world-aware playback, flyby and acoustic querying.

## A note about realism

AudioPhysx combines physically motivated calculations with perceptual approximations. A believable game-audio result is the goal; not every node is a complete physical simulation. Each reference page explains the data or controls it expects.

---

[Compatibility](support/compatibility.md) · [Troubleshooting](support/troubleshooting.md) · [Changelog](support/changelog.md)
