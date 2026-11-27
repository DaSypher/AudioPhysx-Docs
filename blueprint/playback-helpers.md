# Playback helpers from Blueprint

You don't need a dedicated audio Actor to use every AudioPhysx feature. The public Blueprint library provides convenient entry points for sounds at world locations and for registering existing audio components with the plugin's managed update system.

## Play a sound at a world position

**`AP: Play Physical Sound`** accepts a sound asset, world location and source rotation, with volume and optional acoustic/obstruction behaviour exposed by its Blueprint function. This is suitable when the game already knows where an event happened, such as a door slam or explosion.

**`AP: Play Physical Impact`** is the related convenience operation when you already have an `FHitResult`. It can use hit-location information rather than requiring you to reconstruct the position by hand.

Neither operation creates a sound recording. You still supply a `USoundBase`, usually a prepared MetaSound Source or other Unreal sound asset.

## Keep an existing Audio Component updated

**`AP: Register Audio Component`** associates an existing `UAudioComponent` with managed AudioPhysx parameter updates. The registration call allows obstruction tracing to be enabled or disabled. **`AP: Unregister Audio Component`** removes it from that management when it is no longer required.

This is useful for persistent emitters, where creating a new sound for every update would be inappropriate. Registration should follow the component's lifetime so the world subsystem does not keep attempting work on an irrelevant emitter.

## Set the world environment

**`AP: Set World Environment`** supplies temperature, humidity and pressure values for the AudioPhysx world context. These are used by relevant acoustic processing paths; they do not, on their own, change every sound in the game.

## A reasonable first test

Create a mono MetaSound Source with a simple Wave Player, call `AP: Play Physical Sound` at a known location, and verify that it is audible with expected spatialization. Once basic playback works, enable acoustic processing and compare with an unobstructed control sound.

!!!warning Availability matters
The helper requires a valid world/audio environment and a supported sound asset. If you're debugging a silent sound, test the MetaSound directly before assuming the Blueprint's acoustic query is at fault.
!!!
