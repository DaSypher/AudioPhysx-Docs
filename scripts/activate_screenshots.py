#!/usr/bin/env python3
"""Replace IMAGE SLOT HTML comments with Markdown links, but only for existing assets.

Safe to run in GitHub Actions before Retype builds. It only changes Markdown files
in the Actions checkout; you do not need to commit generated changes.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r'<!--\s*(?:IMAGE SLOT|HERO IMAGE SLOT):\s*(docs/static/images/[a-zA-Z0-9_./-]+)\s*-->')
count = 0
for page in (root / 'docs').rglob('*.md'):
    before = page.read_text(encoding='utf-8')
    def replace(match):
        global count
        target = root / match.group(1)
        if not target.is_file():
            return match.group(0)
        count += 1
        alt = target.stem.replace('-', ' ').title() + ' — AudioPhysx'
        return f'![{alt}](/static/images/{target.relative_to(root / "docs" / "static" / "images").as_posix()})'
    after = pattern.sub(replace, before)
    if after != before:
        page.write_text(after, encoding='utf-8')
print(f'Activated {count} screenshot links; missing images remain invisible comments.')
