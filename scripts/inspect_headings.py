import re

for i in range(1, 7):
    fn = f'outputs/content/chapters/CHAP_0{i}.md'
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    h2s = re.findall(r'^##\s+(.+)$', text, re.MULTILINE)
    print(f"\n=== {fn} Headings ({len(h2s)}) ===")
    for h in h2s:
        print(" ", h)
