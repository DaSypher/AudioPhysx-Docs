# Upload the redesigned docs

Use the **ContentOnly** archive for your existing working GitHub Pages site.

1. Open your local clone of `AudioPhysx-Docs` with GitHub Desktop (recommended for many files).
2. Extract and merge the `docs/` folder into the repository root.
3. **Do not delete any images you've already added** under `docs/static/images/`.
4. If using automatic screenshots, also copy `scripts/activate_screenshots.py`.
5. Review changed files, commit with a message such as `Rewrite AudioPhysx docs and navigation`, and push to `main`.
6. GitHub Actions should publish the new pages using your **existing** workflow.

Your `retype.yml`, GitHub Pages settings, and hidden `.github` workflow are **not** part of the content-only update, so they do not need reconfiguration.

All screenshot paths remain the same as the previous documentation release.
