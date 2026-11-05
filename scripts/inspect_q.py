import json

with open("outputs/data/examinations.json", "r", encoding="utf-8") as f:
    d = json.load(f)

first_q = d["examinations"][0]["questions"][0]
print("Question keys:", first_q.keys())
for k, v in first_q.items():
    print(f"  {k}: {type(v)} -> {repr(v)[:80]}")
