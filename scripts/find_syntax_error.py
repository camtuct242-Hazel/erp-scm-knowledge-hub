with open("outputs/app/app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines in app.js: {len(lines)}")
for idx, line in enumerate(lines):
    if "Số" in line:
        print(f"Line {idx+1}: {line.strip()[:100]}")
