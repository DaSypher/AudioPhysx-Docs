# AudioPhysx documentation style guide

## Editorial priorities

1. Lead with **the useful result** a developer can achieve. Readers should not need to understand C++ to choose a node.
2. Explain **what the audio actually does**, including the distinction between playback, DSP, control events and game-side path calculations.
3. Give a **concrete listening example** for every feature.
4. Use **steps** for installation and graph wiring, **tabs** for legitimate alternatives, **short callouts** for pitfalls, and **cards** for navigation.
5. Keep an exact technical reference, but fold long lists of pin types into collapsible sections instead of turning every page into a table.
6. Document limitations accurately; avoid claiming complete physical realism or guaranteed future Unreal versions.

## Retype Free conventions

Use native Markdown and free Retype components: `[!card]`, `!!!tip`, `!!!warning`, `>>> Step`, `+++ Tab`, and `==- Collapsible section` when they improve clarity. Do not rely on Retype Pro theme variables, custom fonts or extra hosting subscriptions.

Do not add three columns of tiny text to long node references; keep most explanation in straightforward paragraphs with comfortable whitespace.

## Images

Use genuine UE Editor screenshots, not rendered imitations of MetaSound pins. Preserve the image slots and filenames listed in `SCREENSHOT_PLAN.md`. A screenshot should demonstrate an actual graph connection, not only an isolated node title.

## Release language

Current documentation describes an AudioPhysx **UE5.8.4 development baseline**. Until the Fab plugin has passed fresh-project and packaged-game tests, do not claim that every feature is Shipping-verified, that all platforms are supported, or that future UE versions will run without maintenance.
