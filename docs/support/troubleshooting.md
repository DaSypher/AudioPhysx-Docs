---
icon: alert
---
# Troubleshooting

## Plugin fails to compile after replacing source

- Verify the editor was closed and Live Coding is disabled.
- Make sure the old source folder was **replaced**, not merged; stale `.cpp` files can cause duplicate registrations or symbols.
- If generated-header errors appear following reflection declaration changes, delete generated plugin/project `Intermediate` outputs and rebuild cleanly.
- Check the exact first compiler error, not only the final UnrealBuildTool failure message.

## Node not visible in MetaSound

- Check AudioPhysx is enabled and the correct editor target built successfully.
- Search using the full name, such as `AP: Start Loop End Player`.
- Restart the editor when dynamic-interface configuration changes.

## Sequence plays silence or ends unexpectedly

- Verify the Wave Asset inputs are assigned, cooked and playable in the target project.
- Test simple mono PCM assets first, then compressed/streamed formats.
- Check the player `Stop`/`Stop Firing` control flow and that the MetaSound itself is not stopped prematurely.

## Need help?

> TODO: Add a verified support contact method and expected response policy. Do not promise future engine-version updates unless they can be delivered.
