import os, re

root_dirs = ['outputs', 'scripts']
patterns = ['imes', '30ext', 'extđơn', 'begin{aligned}']

for r in root_dirs:
    for root, dirs, files in os.walk(r):
        for f in files:
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                for p in patterns:
                    matches = list(re.finditer(re.escape(p), content))
                    if matches:
                        print(f"Found '{p}' in {path}: {len(matches)} occurrences")
                        for m in matches[:3]:
                            start = max(0, m.start() - 40)
                            end = min(len(content), m.end() + 40)
                            print(f"   Context: {repr(content[start:end])}")
            except Exception as e:
                pass
