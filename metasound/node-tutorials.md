# How to use the node tutorials

Every AudioPhysx MetaSound node has its **own page in the left sidebar**. Expand Playback, Acoustics, Propagation or QoL and select the node you want to build. You no longer need to navigate through an extra generic “Nodes” folder or a second “node reference” directory.

On a node page, first read **Understanding the behaviour**, then follow its **Build the sound — step by step** instructions. The setup starts with a minimal, testable stereo graph where applicable. The detailed pin descriptions remain under an expandable technical reference, so the main page is written as an explanation rather than a long API table.

## Where the screenshots go

Each node has two different image slots:

- **Node close-up:** a readable crop of that node’s pins, saved as `docs/static/images/nodes/node-<node-name>.png`.
- **Basic setup graph:** a complete *working graph* showing inputs, connected nodes and Source outputs, saved as `docs/static/images/graphs/setup-<node-name>.png`.

For example, the Start Loop End page expects `docs/static/images/graphs/setup-start-loop-end.png` as its setup image. The page contains a hidden image marker until that file exists; the setup instructions remain readable without any image.

Do **not** upload screenshots to `.github/` or the `Source/` folder. Keep them in `docs/static/images/` in the public documentation repository. Use the filenames from the `NODE_SETUP_SCREENSHOT_CHECKLIST.csv` bundled with the documentation download.

To have screenshots appear automatically when uploaded, enable the optional `scripts/activate_screenshots.py` step **before** the Retype build in your GitHub Actions workflow. The script checks each filename and only inserts image links when that file exists. See the included `GITHUB_IMAGE_SETUP.md` for the one-time workflow change.

## Capturing a useful graph

Show the actual **MetaSound input trigger**, the AudioPhysx node, the relevant connected Wave Asset or control inputs, and the **Left/Right Source outputs**. For control-only nodes, show what the output controls (for example, Trigger Probability feeding a Wave Player). Use a real Unreal screenshot taken after verifying playback; never substitute a drawing that suggests an unsupported pin connection.

For **AP: Stereo to Mono**, show the stereo Left/Right inputs feeding the converter’s `Out Mono`, then a Mono MetaSound Source output. It is the explicit exception to the standard stereo-output workflow.
