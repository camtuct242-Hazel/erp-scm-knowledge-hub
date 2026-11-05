import os
import glob

search_paths = [
    r"C:\Users\asus\.gemini",
    r"C:\Users\asus\AppData\Roaming",
    r"C:\Users\asus\AppData\Local",
    r"C:\Program Files",
    r"C:\Kiến thức cần học",
]

found = []
for base in search_paths:
    print(f"Searching in {base}...")
    for root, dirs, files in os.walk(base):
        # limit depth to prevent long scans
        depth = root[len(base):].count(os.sep)
        if depth > 5:
            continue
        for f in files:
            if 'katex.min.js' in f.lower() or 'mathjax' in f.lower():
                found.append(os.path.join(root, f))
                if len(found) >= 20:
                    break
        if len(found) >= 20:
            break
    if len(found) >= 20:
        break

print(f"Found {len(found)} candidate math libraries:")
for p in found:
    print(" ", p)
