import json
import os
import sys

# Ensure current dir is in sys.path
sys.path.insert(0, os.path.abspath("."))

from scripts_generate_exams_data import exams_metadata
from scripts.exam_01 import get_questions as q01
from scripts.exam_02 import get_questions as q02
from scripts.exam_03 import get_questions as q03
from scripts.exam_04 import get_questions as q04
from scripts.exam_05 import get_questions as q05
from scripts.exam_06 import get_questions as q06
from scripts.exam_07 import get_questions as q07
from scripts.exam_08 import get_questions as q08
from scripts.exam_09 import get_questions as q09
from scripts.exam_10 import get_questions as q10

all_modules = [q01, q02, q03, q04, q05, q06, q07, q08, q09, q10]

all_questions = []
exam_dict = {exam["id"]: {**exam, "questions": []} for exam in exams_metadata}

seen_ids = set()

for idx, get_q in enumerate(all_modules, 1):
    qs = get_q()
    exam_id = f"EXAM-{idx:02d}"
    print(f"Exam {exam_id}: loaded {len(qs)} questions")
    
    assert len(qs) == 25, f"Exam {exam_id} must have exactly 25 questions, got {len(qs)}"
    
    basic_count = 0
    inter_count = 0
    adv_count = 0
    
    for q in qs:
        assert q["id"] not in seen_ids, f"Duplicate question ID: {q['id']}"
        seen_ids.add(q["id"])
        
        assert len(q["options_en"]) == 4, f"Question {q['id']} options_en != 4"
        assert len(q["options_vi"]) == 4, f"Question {q['id']} options_vi != 4"
        assert q["correct_answer"] in [0, 1, 2, 3], f"Question {q['id']} invalid correct_answer"
        assert len(q["question_en"].strip()) > 0, f"Question {q['id']} empty question_en"
        assert len(q["question_vi"].strip()) > 0, f"Question {q['id']} empty question_vi"
        assert len(q["explanation_en"].strip()) > 0, f"Question {q['id']} empty explanation_en"
        assert len(q["explanation_vi"].strip()) > 0, f"Question {q['id']} empty explanation_vi"
        
        if q["difficulty"] == "Basic":
            basic_count += 1
        elif q["difficulty"] == "Intermediate":
            inter_count += 1
        elif q["difficulty"] == "Advanced":
            adv_count += 1
            
        exam_dict[exam_id]["questions"].append(q)
        all_questions.append(q)
        
    print(f"  Difficulty distribution: Basic={basic_count} (40%), Intermediate={inter_count} (40%), Advanced={adv_count} (20%)")
    assert basic_count == 10, f"Exam {exam_id} has {basic_count} Basic, expected 10"
    assert inter_count == 10, f"Exam {exam_id} has {inter_count} Intermediate, expected 10"
    assert adv_count == 5, f"Exam {exam_id} has {adv_count} Advanced, expected 5"

print("=" * 60)
print(f"Total verified unique questions: {len(all_questions)}")
print(f"Total examinations: {len(exam_dict)}")

output_data = {
    "examinations": list(exam_dict.values()),
    "total_examinations": len(exam_dict),
    "total_questions": len(all_questions)
}

os.makedirs("outputs/data", exist_ok=True)
with open("outputs/data/examinations.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("Successfully written to outputs/data/examinations.json")
