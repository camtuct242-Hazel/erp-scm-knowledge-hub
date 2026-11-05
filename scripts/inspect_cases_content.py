import os

for f in ['CASE_01_TEXAGO.md', 'CASE_02_BETTER_PRODUCTS.md', 'CASE_03_ACT_TIRE.md', 'CASE_04_SOCA.md']:
    path = os.path.join('outputs', 'content', 'case-studies', f)
    with open(path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    print(f"=== {f} ({len(lines)} lines) ===")
    for i in range(min(40, len(lines))):
        print(f"{i+1}: {lines[i]}", end="")
    print("\n...\n")
