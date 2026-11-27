# Acoustic path queries

`AP: Query Acoustic Path` is exposed by `UAPAcousticPathLibrary`. It evaluates an acoustic path for supplied **source and listener world positions**, with an optional source actor.

## Return data

`FAPAcousticPathResult` includes direct-path delay and frequency-band loss; whether obstruction was found; information about encountered barriers; and, where valid, an around-obstacle route with delay, loss and a proposed emitter position.

## Recommended workflow

1. Place an acoustic source and listener in a test map.
2. Add an obstruction with a suitable collision setup.
3. Run `AP: Query Acoustic Path` from Blueprint and print the result fields.
4. Compare a clear line of sight, a blocked direct path and a route near a configured portal.
5. Use results to drive acoustic audio parameters as appropriate.

## Performance

These are world-geometry queries and should be performed on the **game thread**. Avoid doing them for every emitter on every rendered audio sample. The AudioPhysx world subsystem has budgets and scheduling controls for managed emitters.

## Don't confuse route validity with route selection

`bAroundPathValid` means an alternate route exists; `bAroundPathSelected` means AudioPhysx currently prefers that route. The audio-path node operates on one selected route rather than mixing two independent voices.
