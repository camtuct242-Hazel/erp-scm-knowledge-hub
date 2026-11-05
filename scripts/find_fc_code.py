with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'renderflashcard:' in line.lower() or 'filterflashcard' in line.lower():
        print(f"Match at line {i+1}")
        for j in range(i, min(len(lines), i + 100)):
            print(f"{j+1}: {lines[j]}", end="")
