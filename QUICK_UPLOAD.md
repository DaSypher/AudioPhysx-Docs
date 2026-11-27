# AudioPhysx docs refresh — fastest upload method

Your working Retype workflow and site configuration do NOT need to be replaced.

## Easiest safe update (recommended)

1. Open the ZIP named `AudioPhysx_Retype_Docs_ContentOnly.zip`.
2. Extract and upload the **contents of its `docs/` folder** into the `docs/` folder of your existing GitHub documentation repository on `main`.
3. This package contains NO hidden `.github` folder and NO replacement `retype.yml`, so it will not interfere with your existing working GitHub Actions or site URL.
4. GitHub's browser uploader may be awkward when merging a tree of folders; use GitHub Desktop or a normal Git checkout for multi-folder updates. If you only use the browser, create folders using 'Add file → Create new file' or upload one folder at a time.
5. Wait for the existing GitHub Action to build, then open your existing GitHub Pages URL.

Alternative: use the full site ZIP, but **keep your existing working `retype.yml`** (your GitHub username/site URL) and `.github/workflows/retype-action.yml` unless deliberately updating them.

## Critical image path

Store actual screenshots under `docs/static/images/`, for example:

`docs/static/images/nodes/node-start-loop-end.png`

Then insert into the relevant Markdown page:

`![Start Loop End Player in MetaSound](/static/images/nodes/node-start-loop-end.png)`

Do not place screenshots in `.github/` or `docs/_assets/`. Retype excludes underscore-prefixed folders by default. Use JPG or PNG as appropriate. Keep screenshot filenames lowercase with hyphens and use the exact name in the Markdown link.

## No broken images while you capture

The pages currently contain **HTML comments** like this:

`<!-- IMAGE SLOT: docs/static/images/nodes/node-start-loop-end.png -->`

They don't create broken image icons on the live site. When the screenshot exists, replace the comment with the Markdown image link above.

## Screenshot order

See `SCREENSHOT_PLAN.md` for the high-priority captures. You do not need to take 23 screenshots on day one. Capture a few visually strong overview/step-by-step images first, then one for each node as time allows.

## Technical status

Content is based on source structure, node declarations and prior developer build reports. Not an Unreal runtime test. Don't convert 'not verified' into 'supported' until testing proves it.
