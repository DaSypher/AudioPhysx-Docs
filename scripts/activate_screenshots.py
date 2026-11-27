#!/usr/bin/env python3
"""Optional Retype pre-build step. Only activates image links when the file is present.

  - name: Activate screenshot references
    run: python3 scripts/activate_screenshots.py

Run after actions/checkout and before retypeapp/action-build in your existing workflow.
"""
from pathlib import Path
import re,os

root=Path(__file__).resolve().parents[1]
image_pattern=re.compile(r'<!--\s*(?:IMAGE SLOT|HERO IMAGE SLOT):\s*(docs/static/images/[a-zA-Z0-9_./-]+)\s*-->')
activated=0
for page in (root/'docs').rglob('*.md'):
    before=page.read_text(encoding='utf-8')
    def replace(match):
        global activated
        f=root/match.group(1)
        if not f.is_file():return match.group(0)
        activated+=1
        # Relative paths keep working even when GitHub Pages is hosted under /repo-name/.
        href=os.path.relpath(f,page.parent).replace(os.sep,'/')
        alt=f.stem.replace('-',' ').title()+' — AudioPhysx'
        return f'![{alt}]({href})'
    after=image_pattern.sub(replace,before)
    if after!=before:page.write_text(after,encoding='utf-8')
print(f'Activated {activated} image references; missing assets remain hidden comments.')
