import os, json, re

print("==================================================")
print("AUDITING CHAPTERS IN outputs/content/chapters/")
print("==================================================")

chapters_dir = 'outputs/content/chapters'
chap_files = sorted([f for f in os.listdir(chapters_dir) if f.endswith('.md')])

for f in chap_files:
    path = os.path.join(chapters_dir, f)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Check for corruptions
    tabs = content.count('\t')
    backspaces = content.count('\x08')
    formfeeds = content.count('\x0c')
    
    # Check LaTeX corruption patterns
    corrupt_ext = re.findall(r'(\d+ext[^\s$]*|[^\s$\\]ext\{)', content)
    corrupt_imes = re.findall(r'(\d+imes[^\s$]*|[^\s$\\]imes)', content)
    raw_aligned = re.findall(r'(\\begin\{aligned\}|\begin\{aligned\})', content)
    
    # Check section headings
    h1s = re.findall(r'^#\s+(.+)$', content, re.MULTILINE)
    h2s = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    
    # Check review questions
    questions = re.findall(r'(\d+\.\s+\*\*Câu hỏi[^\*]*\*\*)', content)
    
    print(f"\n--- {f} (Size: {len(content):,} bytes) ---")
    print(f"  H1: {h1s[:1]}")
    print(f"  H2 sections count: {len(h2s)}")
    print(f"  Review questions found: {len(questions)}")
    print(f"  Control characters: tabs={tabs}, backspaces={backspaces}, formfeeds={formfeeds}")
    if corrupt_ext:
        print(f"  Corrupt 'ext': {corrupt_ext[:5]}")
    if corrupt_imes:
        print(f"  Corrupt 'imes': {corrupt_imes[:5]}")
    if raw_aligned:
        print(f"  'aligned' blocks count: {len(raw_aligned)}")

print("\n==================================================")
print("AUDITING outputs/data/chapters.json")
print("==================================================")
with open('outputs/data/chapters.json', 'r', encoding='utf-8') as fp:
    cj = json.load(fp)
print(f"Type: {type(cj)}, Length: {len(cj)}")
if isinstance(cj, list):
    for item in cj:
        print(f"  ID: {item.get('id')}, Title: {item.get('title')}, Sections: {len(item.get('sections', []))}")

print("\n==================================================")
print("AUDITING outputs/app/data.js (chapterContents)")
print("==================================================")
with open('outputs/app/data.js', 'r', encoding='utf-8') as fp:
    djs = fp.read()
m = re.search(r'window\.APP_DATA\s*=\s*(\{.*\});', djs, re.DOTALL)
if m:
    app_data = json.loads(m.group(1))
    c_contents = app_data.get('chapterContents', {})
    print(f"chapterContents keys: {list(c_contents.keys())}")
    for k, v in c_contents.items():
        tabs = v.count('\t')
        q_count = len(re.findall(r'(\d+\.\s+\*\*Câu hỏi[^\*]*\*\*)', v))
        print(f"  {k}: {len(v):,} chars, tabs={tabs}, review questions={q_count}")
