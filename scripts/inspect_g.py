import json

with open("outputs/data/glossary.json", "r", encoding="utf-8") as f:
    d = json.load(f)

first_g = d[0]
print("Glossary keys:", first_g.keys())
print("First item:", first_g)
