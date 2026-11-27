# Frequently asked questions

## Does AudioPhysx require Chaos?

The flyby path helpers are designed to work from path and speed data supplied by the game, without requiring Chaos rigid-body simulation. Other physics-related features may use engine queries depending on the setup.

## Can Sound Cues use these MetaSound nodes?

No. The MetaSound nodes live inside MetaSound graphs. Dedicated Sound Cue QoL nodes are planned separately and are not yet part of this source version.

## Are future Unreal Engine versions guaranteed?

No. Native code plugins must be tested and submitted for the specific engine versions advertised.
