# AP: Random Sequence Wave Player

**Category:** AudioPhysx → Playback

Each expandable step takes a **Wave Asset Array**, selects one playable entry, plays it, and then advances to the next step after playback completes.

## Inputs

| Pin | Description |
| --- | --- |
| `Play` | Begin/restart playback. |
| `Stop` | Stop playback. |
| `Loop Sequence` | Repeat the series of steps. |
| `Waves` | Expandable Wave Asset Array per step. |

## Outputs

| Pin | Description |
| --- | --- |
| `Out Mono` | Audio stream of the selected step. |
| `On Finished` | The final step has finished (when not looping). |

## Example

Step 1 contains three weapon-ready sounds; Step 2 contains four mechanical sounds; Step 3 contains two finishing sounds. The sequencer plays **one item from each array**, in that order.

> TODO: Add a MetaSound graph screenshot and verify behaviour for empty arrays, invalid wave proxies, retriggering and random no-repeat selection.
