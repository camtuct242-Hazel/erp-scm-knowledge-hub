with open('outputs/content/case-studies/CASE_01_TEXAGO.md', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of CASE_01_TEXAGO.md:", len(text))
# Check if any raw code block has tables
if '```text' in text:
    print("Found ```text code blocks in CASE_01_TEXAGO.md!")
