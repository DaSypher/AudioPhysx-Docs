# AudioPhysx documentation — setup and publication

This is a **public documentation repository**, NOT the commercial AudioPhysx source project.
It contains Markdown documentation and a Retype GitHub Pages build workflow.
The pages are initial drafts and should be checked against the final shipping plugin.

## Local preview

Install Node.js, then run:

```bash
npm install retypeapp --global
retype start
```

Retype will start a local preview and watch edits to the Markdown pages.

## Free hosting with GitHub Pages

1. Create a **public** GitHub repository named `AudioPhysx-Docs` (or your preferred name). Keep your paid plugin source in a different, **private** repository.
2. Edit `retype.yml`: replace `YOUR-GITHUB-USERNAME` with your actual GitHub username. If you choose a different repository name, also replace `AudioPhysx-Docs` in the `url`.
3. Upload all the files/folders in this starter directory to the repository's `main` branch, including `.github/workflows/retype-action.yml` (hidden folders matter).
4. Open the repository's **Actions** tab, enable workflows if prompted, and inspect the `Publish AudioPhysx Docs` run. The workflow builds Retype and creates/updates a `retype` branch.
5. Go to **Settings → Pages**. Choose **Deploy from a branch**, branch **retype**, folder **/(root)**, then save. Select **Enforce HTTPS** once available.
6. The resulting site uses `https://YOUR-GITHUB-USERNAME.github.io/AudioPhysx-Docs/`. Allow for GitHub Pages publication propagation.
7. Every later commit to `main` updates the documentation automatically after the workflow completes.

Official docs:
- https://retype.com/guides/github-actions/
- https://retype.com/hosting/github-pages/
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Publishing checklist
- Replace every `TODO` before promoting draft pages as a public reference.
- Add screenshots taken from the **final shipping plugin**; don't show out-of-date nodes.
- Confirm supported engine versions, platforms, shipping-build status, and technical limitations.
- Record the `.uplugin` plugin version and match it to the changelog.
- Link the documentation URL on the Fab listing.
- Never upload the paid C++ plugin source, customer data, or private assets to the public docs repository.

## Note on the Retype free plan
Retype says its free edition may be used for commercial documentation. Free GitHub Pages requires a public repository on GitHub Free. The generated website is public.
