import json
import os
import re

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

raw_glossary = load_json("outputs/data/glossary.json")
glossary = []
for g in raw_glossary:
    ng = dict(g)
    # Map domain to category
    ng["category"] = g.get("category") or g.get("domain", "General")
    # Extract abbreviation if present in parentheses e.g. "Enterprise Resource Planning (ERP)"
    if "abbreviation" not in ng or not ng["abbreviation"]:
        m = re.search(r'\(([A-Z0-9\-\/]+)\)', g.get("term_en", ""))
        ng["abbreviation"] = m.group(1) if m else ""
    # Ensure bilingual practical example
    if "practical_example_vi" not in ng:
        ng["practical_example_vi"] = g.get("practical_example", "")
    if "practical_example_en" not in ng:
        ng["practical_example_en"] = g.get("practical_example", "")
    # Ensure erp_mapping
    if "erp_mapping" not in ng or not ng["erp_mapping"]:
        p_ex = g.get("practical_example", "")
        if "SAP" in p_ex or "Oracle" in p_ex:
            ng["erp_mapping"] = p_ex[:80] + "..."
        else:
            ng["erp_mapping"] = f"Core SCM Master Data / {ng['category']}"
    glossary.append(ng)

flashcards = load_json("outputs/data/flashcards.json")
exam_data = load_json("outputs/data/examinations.json")
raw_exams = exam_data["examinations"] if isinstance(exam_data, dict) and "examinations" in exam_data else exam_data

opt_keys = ["A", "B", "C", "D"]

# Normalize exam objects and questions
examinations = []
for ex in raw_exams:
    norm_ex = dict(ex)
    if "title" not in norm_ex:
        norm_ex["title"] = {
            "vi": ex.get("title_vi", ""),
            "en": ex.get("title_en", "")
        }
    if "description" not in norm_ex:
        norm_ex["description"] = {
            "vi": ex.get("description_vi", ""),
            "en": ex.get("description_en", "")
        }
    if "exam_number" not in norm_ex:
        match = re.search(r'\d+', ex.get("id", "1"))
        norm_ex["exam_number"] = int(match.group()) if match else 1

    norm_questions = []
    for q in ex.get("questions", []):
        nq = dict(q)
        # Normalize question text
        if "question" not in nq:
            nq["question"] = {
                "vi": q.get("question_vi", ""),
                "en": q.get("question_en", "")
            }
        # Normalize options
        if "options" not in nq:
            opts_en = q.get("options_en", [])
            opts_vi = q.get("options_vi", [])
            nq["options"] = {}
            for idx, k in enumerate(opt_keys):
                nq["options"][k] = {
                    "vi": opts_vi[idx] if idx < len(opts_vi) else "",
                    "en": opts_en[idx] if idx < len(opts_en) else ""
                }
        # Normalize correct_option
        if "correct_option" not in nq:
            c_ans = q.get("correct_answer", 0)
            if isinstance(c_ans, int) and 0 <= c_ans < 4:
                nq["correct_option"] = opt_keys[c_ans]
            elif isinstance(c_ans, str) and c_ans in opt_keys:
                nq["correct_option"] = c_ans
            else:
                nq["correct_option"] = "A"
        # Normalize explanation
        if "explanation" not in nq:
            nq["explanation"] = {
                "vi": q.get("explanation_vi", ""),
                "en": q.get("explanation_en", "")
            }
        norm_questions.append(nq)

    norm_ex["questions"] = norm_questions
    examinations.append(norm_ex)

case_studies = load_json("outputs/data/case-studies.json")
scenarios = load_json("outputs/data/scenarios.json")
chapters = load_json("outputs/data/chapters.json")

chapter_contents = {}
for i in range(1, 7):
    chap_id = f"chap-{i:02d}"
    fpath = f"outputs/content/chapters/CHAP_{i:02d}.md"
    if os.path.exists(fpath):
        chapter_contents[chap_id] = load_text(fpath)

case_contents = {}
case_files = {
    "CASE-01": "outputs/content/case-studies/CASE_01_TEXAGO.md",
    "CASE-02": "outputs/content/case-studies/CASE_02_BETTER_PRODUCTS.md",
    "CASE-03": "outputs/content/case-studies/CASE_03_ACT_TIRE.md",
    "CASE-04": "outputs/content/case-studies/CASE_04_SOCA.md"
}
for cid, fpath in case_files.items():
    if os.path.exists(fpath):
        case_contents[cid] = load_text(fpath)

app_data = {
    "glossary": glossary,
    "flashcards": flashcards,
    "examinations": examinations,
    "caseStudies": case_studies,
    "scenarios": scenarios,
    "chapters": chapters,
    "chapterContents": chapter_contents,
    "caseContents": case_contents
}

with open("outputs/app/data.js", "w", encoding="utf-8") as f:
    f.write("// ERP SCM Knowledge Hub - Bundled Datasets for Offline & Standalone Execution\n")
    f.write("window.APP_DATA = ")
    json.dump(app_data, f, ensure_ascii=False)
    f.write(";\n")

print(f"Rebuilt outputs/app/data.js with {len(glossary)} normalized glossary terms, {len(examinations)} examinations. Size: {os.path.getsize('outputs/app/data.js')} bytes.")
