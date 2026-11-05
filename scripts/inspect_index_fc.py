with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="view-flashcards"' in l:
        for j in range(i, min(len(lines), i + 70)):
            print(f"{j+1}: {lines[j]}", end="")
        break
