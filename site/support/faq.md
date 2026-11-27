---
label: "Frequently asked questions"
icon: question
order: 85
---


# Frequently asked questions

**Why make all the audio nodes stereo?** The previous mono-first design forced information out of a stereo recording before a sound designer had decided whether that information was useful. The updated Wave Players and DSP processors preserve Left and Right channels, making it possible to author wider layered effects and process stereo ambience without an early downmix. This is a signal-path capability, not a requirement that every positional world sound remain stereo. A small point-source effect may still be better downmixed before Unreal spatialization.

**Does Stereo to Mono destroy stereo information?** Yes, deliberately. It produces one mono signal by averaging the channels, `0.5 × (Left + Right)`. That avoids the simple level increase from adding two identical channels, but opposite-polarity content may cancel. It also cannot restore any original stereo image after the fold-down. Use it near the end of the graph when that format is appropriate, and listen to the result.

**Why do some AudioPhysx nodes still have no Left and Right outputs?** Trigger Cooldown, Trigger Probability, Float Smoother, Dynamic Distance Switch and Doppler Ratio are controls or event processors, not audio renderers. A trigger or single pitch ratio does not become a two-channel sound just because a nearby Wave Player is stereo. Their outputs remain correctly typed for the data they represent.

**Does AudioPhysx replace MetaSounds or Unreal spatialization?** No. It adds focused native tools to the existing Unreal audio pipeline. Source layouts, attenuation, concurrency and spatialization remain important. AudioPhysx helps decide which recording to play, what effect to apply and how game information reaches that processing.

**Do the acoustic nodes perform a fully accurate world simulation?** No. They combine physically inspired calculations with practical perceptual approximations. For example, Early Reflections creates synthetic taps rather than measuring every real surface, and the flyby solver uses a simplified constant-speed path. Reliable results depend on good recording content, geometry data, material values and informed mixing decisions.

**Do I need Chaos?** The flyby system can evaluate supplied projectile path segments without building a special Chaos rigid-body simulation. Acoustic queries rely on world geometry and collision information, but they are not themselves a requirement to run Chaos physics for every sound event.

**Can AudioPhysx be used with Sound Cues?** The native node set inspected for this edition is a MetaSound library, with Blueprint helpers available for sound assets. Dedicated custom Sound Cue QoL nodes are planned but **not** included in the reviewed source. Unreal's own Sound Cues remain available separately.

**Will this automatically work with Unreal Engine 6?** No UE6 support is verified or promised. The playback system still uses some Unreal-internal APIs behind a private adapter, and changes in future engine versions may require plugin updates. The [compatibility matrix](compatibility.md) should be updated only after testing the actual submitted package.
