# AudioPhysx docs — in-depth stereo revision

This is a documentation update, not C++ source code. It was written from the uploaded `Source.zip` available in this conversation, not from an unverified engine build.

## Existing GitHub Pages site: which package?

Use `AudioPhysx_Docs_Deep_Stereo_ContentOnly.zip`. It includes `docs/` and `_includes/head.html`, but **does not replace your existing `retype.yml` or `.github/workflows`**. Preserve the working GitHub Pages URL and Action already in your repository. Merge this content over your existing docs, rather than deleting any previously uploaded screenshot images.

The optional `_includes/head.html` contains the new colour/typography stylesheet. It is a Retype-supported site-wide include and is not the `.github` workflow folder. If GitHub's web uploader refuses folders that begin with an underscore, use GitHub Desktop or create the file through Add file → Create new file with `_includes/head.html` as the path.

## Screenshot filenames

Place original editor captures in `docs/static/images/`. See `SCREENSHOT_PLAN.md`. Every page uses an invisible image slot until you insert its screenshot, so readers do not see broken images. If you use the included optional `scripts/activate_screenshots.py` in your working Actions workflow, it fills matching image slots only when the image is actually present.

## Notes about the new stereo code

- Every audio-producing playback and DSP operator in this source has Left and Right outputs.
- The four pre-existing control-only nodes output numbers/triggers, not audio.
- AP: Stereo to Mono deliberately produces `Out Mono` because that is its stated purpose.
- The stereo upgrade changes MetaSound graph pin layouts, so existing saved assets may need refreshing or rewiring. Test before saving migrated assets.
- Source inspection is not an Unreal compile or a Shipping build. Advertise only tested engine/platform combinations.

## Style

Pages use one H1, usually two or three H2 headings, and several real paragraphs rather than a paragraph fragment under every heading. Pin references are preserved in a folded section so the guide stays readable.
