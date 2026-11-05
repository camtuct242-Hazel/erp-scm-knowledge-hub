with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

fc_lines = []
for i, line in enumerate(lines):
    if 'flashcard' in line.lower() or 'card' in line.lower():
        fc_lines.append((i+1, line.strip()))

print(f"Total lines in app.js: {len(lines)}")
print("Sample flashcard occurrences in app.js:")
for line_num, content in fc_lines[:30]:
    print(f"L{line_num}: {content[:80]}")
