#!/usr/bin/env python3
"""Make screenshot comments visible only when the corresponding image exists.
Run between checkout and Retype build in GitHub Actions.
"""
from pathlib import Path
import os, re
root=Path(__file__).resolve().parents[1]
site=root/"site"
pattern=re.compile(r'<!--\s*(?:IMAGE SLOT|HERO IMAGE SLOT):\s*((?:docs|site)/static/images/[A-Za-z0-9_./-]+)\s*-->')
activated=0
for page in site.rglob('*.md'):
    before=page.read_text(encoding='utf-8')
    def insert(match):
        global activated
        target=root/match.group(1)
        if not target.is_file():return match.group(0)
        activated+=1
        href=os.path.relpath(target,page.parent).replace(os.sep,'/')
        alt=target.stem.replace('-', ' ').title()+' — AudioPhysx'
        return f'![{alt}]({href})'
    after=pattern.sub(insert,before)
    if after!=before:page.write_text(after,encoding='utf-8')
print(f'Activated {activated} image references. Missing images remain invisible.')
