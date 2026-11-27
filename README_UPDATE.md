# AudioPhysx documentation — editorial and visual update

This package is **only documentation**. It does not modify or redistribute the commercial C++ plugin.

## What changed

- Rewrote all 23 MetaSound node pages with clear descriptions of what happens to the sound, practical game examples, step-by-step setup and node-specific pitfalls.
- Preserved the 199 existing named pin references from the previous source-derived site; they now live in collapsible Input/Output sections instead of large tables.
- Rewrote the homepage, getting-started guides, Blueprint integrations, six examples and support pages.
- Added Retype cards, tabs, steps, useful callouts and a small number of conceptual Mermaid diagrams; no paid Retype theme options required.
- Removed dense tables from the editorial pages and maintained the existing Markdown paths and screenshot filename conventions.
- Hid three old redirect pages and the *planned, not shipped* Sound Cue page from the main navigation. They are still available by direct URL.
- Kept the published Fab/Shipping/UE6 compatibility claims cautious pending verification.

## Upload without changing your working GitHub Pages site

1. Back up or commit your current GitHub documentation repo first.
2. Extract the `AudioPhysx_Retype_Docs_Editorial_Revamp_ContentOnly.zip` archive.
3. Copy the archive's **`docs/` directory contents** into the matching `docs/` folder in your existing repository, replacing Markdown files when prompted.
4. If you have already added any PNG/JPEG/WebP screenshots under `docs/static/images/`, **keep those assets**. Do not delete the whole `docs/` directory just to apply this update.
5. Copy `scripts/activate_screenshots.py` if you use the optional screenshot-activation workflow.
6. Commit and push to `main`; your existing Retype Action will build and deploy the updated docs.

**Do not replace your existing `retype.yml` or `.github/workflows` from the content-only ZIP:** neither is included. Your custom site URL and working deployment stay intact.

## Image insertion

Screenshot slots remain HTML comments until the corresponding image exists, so visitors won't see broken images. See `SCREENSHOT_PLAN.md` for exact filenames. To automatically activate screenshots, add the `Activate AudioPhysx screenshots` step described in `GITHUB_ACTION_IMAGE_STEP.md` to your current workflow. You only need to do this once.

Image root: `docs/static/images/`. Example: `docs/static/images/nodes/node-start-loop-end.png`.

## Verification status

- 62 Markdown pages and 23 individual node references.
- 199 historical pin labels preserved and compared against the previous documentation archive.
- 213 Markdown/card links checked; no missing relative targets.
- All 62 page frontmatter blocks parsed successfully.
- Screenshot placeholders and existing filenames preserved.
- **A live Retype HTML build could not be completed in this runtime** (the npm registry request timed out). After publishing, check Retype Actions output and inspect the homepage, one node page and one Blueprint guide in the rendered site.

These pages are based on the AudioPhysx UE5.8.4 RPM-enabled source baseline and original reference content. They do not constitute an independent Unreal compilation, listening test or Shipping certification.
