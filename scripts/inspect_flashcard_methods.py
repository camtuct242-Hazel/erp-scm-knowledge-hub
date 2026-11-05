with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'renderflashcard' in line.lower() or 'filterflashcards' in line.lower() or 'flipflashcard' in line.lower():
        start = max(0, i - 5)
        end = min(len(lines), i + 70)
        print(f"--- MATCH AT LINE {i+1} ---")
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}", end="")
        break
