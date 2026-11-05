import os
import glob

cases_md = glob.glob(r"outputs/content/case-studies/*.md")
for f in cases_md:
    size = os.path.getsize(f)
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    print(f"{os.path.basename(f)}: {size} bytes, {len(lines)} lines")
    headings = [l.strip() for l in lines if l.startswith('#')]
    print(f"  Headings count: {len(headings)}")
    for h in headings[:8]:
        print(f"    {h}")
