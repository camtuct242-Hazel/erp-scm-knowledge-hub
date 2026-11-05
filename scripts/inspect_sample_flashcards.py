import json

with open('outputs/data/flashcards.json', 'r', encoding='utf-8') as f:
    fc = json.load(f)

print("Total cards in flashcards.json:", len(fc))
for i in range(min(3, len(fc))):
    print(f"\n--- Card {i+1} ---")
    print(json.dumps(fc[i], indent=2, ensure_ascii=False))
