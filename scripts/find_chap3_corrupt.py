import os, re

patterns = ["chi phí toán học", "30/nga", "Mặc dù Case 2.2", "vượt xa con số", "vượt xa"]

found = []
for root, dirs, files in os.walk('outputs'):
    for f in files:
        if f.endswith(('.md', '.json', '.js', '.html')):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                for p in patterns:
                    if p in content:
                        found.append((path, p))
            except Exception:
                pass

print("Search results:")
for path, p in set(found):
    print(f"  {path} contains '{p}'")
