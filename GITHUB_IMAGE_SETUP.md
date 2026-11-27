# Optional automatic screenshot activation

The documentation pages include comments of the form `<!-- IMAGE SLOT: docs/static/images/... -->`. Visitors do not see these placeholders. When you upload a matching file, you can automatically replace the comment with a Markdown image reference during the Retype build, without manually editing every node page.

1. Copy `scripts/activate_screenshots.py` into the documentation repository.
2. Open your existing `.github/workflows/retype-action.yml` in GitHub's editor.
3. After the `actions/checkout` step and before `retypeapp/action-build@latest`, insert:

```yaml
      - name: Activate screenshot references
        run: python3 scripts/activate_screenshots.py
```

4. Commit that workflow edit once. Then upload screenshots using the filenames in `SCREENSHOT_PLAN.md`.

The script deliberately uses **relative image links**, which work with a GitHub Pages project URL such as `username.github.io/AudioPhysx-Docs/`. It does not modify your original Markdown in the remote repository; it modifies the GitHub Actions checkout during the build. You can also simply insert regular Markdown image links manually without using the script.
