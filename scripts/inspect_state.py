import json
import os

print("=== INSPECTING DATA FILES ===")
files = ['flashcards.json', 'case-studies.json', 'chapters.json', 'examinations.json', 'glossary.json', 'scenarios.json']
for f in files:
    path = os.path.join('outputs', 'data', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            print(f"{f}: {len(d)} items, type: {type(d)}")
            if len(d) > 0 and isinstance(d, list):
                print(f"  First item keys: {list(d[0].keys())}")
            elif isinstance(d, dict):
                print(f"  Dict keys: {list(d.keys())}")

with open('outputs/app/data.js', 'r', encoding='utf-8') as fp:
    line1 = fp.readline()
    line2 = fp.readline()
    print("data.js line 1:", line1.strip())
    print("data.js line 2 starts with:", line2[:100])
