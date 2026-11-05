with open("outputs/app/app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(1615, min(1630, len(lines))):
    print(f"--- Line {i+1} ---")
    print(lines[i])
