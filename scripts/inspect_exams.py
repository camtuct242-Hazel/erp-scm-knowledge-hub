import json

with open("outputs/data/examinations.json", "r", encoding="utf-8") as f:
    d = json.load(f)

first_exam = d["examinations"][0]
print("Exam keys:", first_exam.keys())
print("Exam title representation:", {k: first_exam[k] for k in first_exam if "title" in k or "name" in k or "topic" in k})
