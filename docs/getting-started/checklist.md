---
label: Setup checklist
icon: checklist
order: 70
---
# Quick setup checklist

Use this before assuming a node is broken. It catches the most common installation, routing and completion mistakes.

## Can the sound start?

- [ ] The AudioPhysx plugin is enabled and the node appears in MetaSound search.
- [ ] Every required Wave Asset is imported and playable on its own.
- [ ] The correct trigger reaches the node (`Play` versus `Start Firing`, for example).
- [ ] `Out Mono` reaches the active MetaSound output, and the Source is actually being auditioned or played.

## Can the sound finish correctly?

- [ ] A repeating player has a valid stop/release trigger when appropriate.
- [ ] The `On Finished` connection doesn't cut off downstream effects such as early reflections.
- [ ] Voice limits and retriggering make sense under rapid gameplay events.

## Does the world data make sense?

- [ ] Distances are converted correctly between centimetres and metres.
- [ ] Material paths and surface types match the configured routes.
- [ ] Dynamic input group sizes still match the intended graph.
- [ ] World-based Blueprint helpers have a valid world/listener/audio environment.

## Before releasing a game

- [ ] Test standalone playback, then package a Development build.
- [ ] Verify cooked audio assets and Shipping behaviour.
- [ ] Repeat the test with missing/empty arrays and rapid triggers.

[Troubleshooting guide](../support/troubleshooting.md)
