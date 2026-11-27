# Sound Cue support is planned, not shipped

The source used for this edition implements MetaSound nodes and Blueprint integration helpers. It does not include a finished custom `USoundNode` library for Unreal Sound Cues, so the documentation must not market Sound Cue extensions as currently available.

Sound Cue work may still be valuable, particularly where a focused Smart Random or Random Sequence utility would remove repetitive authoring. It should be approached as a quality-of-life project rather than an attempt to rebuild every MetaSound DSP effect in the older Sound Cue format. New Sound Cue node pages should only be published after their source exists and the behaviour passes Editor and packaged-game testing.

Until then, continue using the verified native Sound Cue facilities that Unreal provides and AudioPhysx's existing [MetaSound playback nodes](../metasound/README.md) where those are appropriate to the game.
