import os, pypdf

case_dir = "references/Case studies"
for fname in os.listdir(case_dir):
    if "Case 4" in fname:
        fpath = os.path.join(case_dir, fname)
        print("Opening:", fpath)
        reader = pypdf.PdfReader(fpath)
        for i, page in enumerate(reader.pages):
            print(f"\n=== PAGE {i+1} ===")
            print(page.extract_text())
