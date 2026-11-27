# Optional: Automatically show screenshots as soon as you upload them

You can keep your **existing working Retype workflow**. This is a one-time improvement that avoids editing Markdown for every screenshot.

1. Upload `scripts/activate_screenshots.py` to your public documentation repository.
2. In GitHub, open `.github/workflows/retype-action.yml` on the `main` branch and click Edit.
3. Insert these lines immediately after the `actions/checkout` step and its `with` block, and **before** the `retypeapp/action-build@latest` step:

```yaml
      - name: Activate AudioPhysx screenshots
        run: python3 scripts/activate_screenshots.py
```

4. Commit. Now upload screenshots to `docs/static/images/...` using the filenames in `SCREENSHOT_PLAN.md`.
5. Every push triggers the workflow, which inserts Markdown image references only for files that exist. Missing screenshots stay invisible rather than showing broken images.

You do NOT need to upload your commercial source files to this documentation repository.
