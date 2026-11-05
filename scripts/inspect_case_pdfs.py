import os
import glob
from pypdf import PdfReader

pdf_files = glob.glob(r"references/Case studies/*.pdf")
for pdf_path in pdf_files:
    reader = PdfReader(pdf_path)
    print(f"=== {os.path.basename(pdf_path)} ({len(reader.pages)} pages) ===")
    for idx, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"--- Page {idx+1} ({len(text)} chars) ---")
        print(text[:400].strip())
        print("...")
