# Engine and platform compatibility

## Current documentation basis

These pages were generated against the **AudioPhysx UE5.8.4 development source** available on 27 November 2026. They do not establish that a final Fab package has passed packaged-game verification.

| Environment | Status |
| --- | --- |
| UE5.8.4 development Editor build | Developer-reported working baseline; not independently compiled in this documentation task |
| Clean Blueprint-only project | **Not yet verified** |
| Packaged Development build | **Not yet verified** |
| Packaged Shipping build | **Not yet verified** |
| Windows target | Toolchain/package support **to be verified** |
| Linux/macOS/mobile/consoles | **No verified support claim** |
| Unreal Engine 6 | **No verified support claim** |

Only update this table after building and testing the exact product package. A successful Editor build does not prove packaged-game compatibility.

## Known design constraints

- Several native players use an adapter around Unreal's internal `FSoundWaveProxyPlayer` API. Compatibility with new engine versions may require source updates.
- Some dynamic MetaSound sub-interfaces use experimental engine APIs.
- Surface-specific pin layouts can depend on AudioPhysx settings.
- Flyby/early-reflection models are acoustic approximations rather than full physical solvers.

## How to report compatibility

Include exact Unreal version, platform, development/shipping configuration, full plugin version and an actionable reproduction.
