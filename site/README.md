---
label: "Home"
icon: home
order: 100
---


# AudioPhysx — audio that reacts to the world

**A MetaSound and Blueprint toolkit for responsive, carefully designed Unreal Engine audio.** AudioPhysx brings together flexible sample players, physically inspired processing, propagation tools and control utilities so you can make sounds respond to distance, material, movement and gameplay events without duplicating the same large node graph everywhere.

The plugin is designed around an important distinction: the game provides **what happened and where**, while the audio graph decides **which recording is appropriate and how it should sound**. Sometimes the best solution is a believable physical approximation; sometimes it is a deliberate, well-authored variation of a recording. The two approaches can work together.

<!-- HERO IMAGE SLOT: site/static/images/brand/hero-audiophysx.png -->

!!!info Development documentation
The pages describe the newly uploaded **UE 5.8.4 stereo source**, including the RPM-enabled Start Loop End Player and the new Stereo to Mono converter. These are source-verified interfaces, not proof that every node has been compiled and tested in a packaged Shipping build. See [compatibility](support/compatibility.md) before making release claims.
!!!

## Choose where to begin

[!card layout="compact" title="Get started" text="Install AudioPhysx, understand the signals and build your first MetaSound."](getting-started/README.md)

[!card layout="compact" title="Find a MetaSound node" text="Explore the playback, acoustics, propagation and QoL tools, with full source-derived pin references."](metasound/README.md)

[!card layout="compact" title="Connect a game system" text="Learn the Blueprint side: projectile paths, acoustic queries, emitters and materials."](blueprint/README.md)

[!card layout="compact" title="Build a practical example" text="Follow real sound-design recipes for gunfire, layered sound, flybys and obstruction."](examples/README.md)

## What makes the workflow different?

**Playback tools** handle the details that become repetitive in ordinary graphs: non-identical one-shots, shuffle-bag history, fixed and random sequences, synchronized layers, physical-material routing and held actions with proper endings. For example, the Start Loop End Player can schedule overlapping gunshot variations from a real RPM value while preserving a release tail when the player stops firing.

**Acoustic tools** take meaningful data from the world and transform the sound rather than guessing geometry from audio samples. Material Transmission filters sound that passes through barriers; Acoustic Paths renders one world-selected route; Early Reflections adds a lightweight sense of local space; Source Directivity can make the front of a speaker sound different from its rear. Each tool has its own purpose and limitations, explained in its reference page.

**Stereo is now a first-class signal path.** The playback and stereo DSP nodes provide `Out Left` and `Out Right`, preserving genuine channel differences. If the final sound should become a mono point-source emitter, `AP: Stereo to Mono` performs an explicit fold-down. The format decision belongs to the sound designer rather than being forced by every intermediate node. [Read the stereo guide](getting-started/stereo-routing.md).

<!-- IMAGE SLOT: site/static/images/graphs/graph-stereo-overview.png -->

## How to get a convincing result

Start with good source recordings and one clear goal. Choose a player that solves the required event timing, then add only processing that supplies a distinct audible benefit. A distance-based selection, a Doppler effect and a wall-transmission filter are three different tools; none automatically fixes an inaccurate listener position or a poorly edited Wave Asset. AudioPhysx aims to make these decisions approachable without pretending that every source must use every processor.

For a first exercise, follow [your first MetaSound](getting-started/first-metasound.md). If you already know MetaSounds, go straight to the [node library](metasound/README.md). You can also browse [examples](examples/README.md) or check [troubleshooting](support/troubleshooting.md) when an installed graph does not behave as expected.
