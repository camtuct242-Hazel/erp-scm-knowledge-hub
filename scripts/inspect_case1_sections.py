with open('outputs/content/case-studies/CASE_01_TEXAGO.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if l.startswith('## 2.') or l.startswith('## 3.'):
        print(f"Heading at line {i+1}: {l.strip()}")
        for j in range(i, min(len(lines), i + 25)):
            print(f"  {lines[j]}", end="")
