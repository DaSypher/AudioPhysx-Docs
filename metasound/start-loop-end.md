# AP: Start Loop End Player

**Category:** AudioPhysx → Playback

Plays a selected introduction, followed by repeated middle sounds, followed by a selected ending when firing stops. The middle section supports either completion-based playback or an RPM-driven shot cadence.

## Inputs

| Pin | Purpose |
| --- | --- |
| `Start Firing` | Begin the sequence. |
| `Stop Firing` | Request transition into the ending section. |
| `Immediate Release` | Choose whether to move promptly into the ending or finish outstanding playback first. |
| `RPM` | At `0`, preserve sequential middle playback; positive values schedule overlapping middle-shot starts. |
| `Start Waves` | Intro Wave Asset Array. |
| `Loop Waves` | Repeated middle Wave Asset Array. |
| `End Waves` | Tail Wave Asset Array. |

## Outputs

| Pin | Purpose |
| --- | --- |
| `Out Mono` | Mixed mono audio. |
| `On Finished` | Sequence complete after release and remaining audio. |

## Example: automatic weapon

Supply one or more starting recordings, several short main-shot variations, and a set of release recordings. For a 600 RPM cadence, the scheduled interval is `60 / 600 = 0.1 s` (100 ms). This does **not** require each middle recording to last 100 ms; shots may overlap.

## Important

- `RPM = 0` uses the older completion-driven behaviour and also suits machinery.
- `Stop Firing` is a **release request**, not necessarily an immediate silence command.
- The number of simultaneously active shots is bounded by the player implementation.
- `On Finished` should not be treated as proof of an external gameplay action completing.

> TODO: Confirm voice-stealing/overflow handling and run restart, stop-during-intro, long-tail, 0/600/1200 RPM and Shipping-build tests before publishing.
