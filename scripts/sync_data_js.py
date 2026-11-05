import json
import os

print("Syncing updated flashcards and case contents into outputs/app/data.js...")

# 1. Read flashcards.json
with open('outputs/data/flashcards.json', 'r', encoding='utf-8') as f:
    flashcards_list = json.load(f)

# 2. Read all 4 case study markdown files
case_contents = {}
for cid, filename in [('CASE-01', 'CASE_01_TEXAGO.md'),
                      ('CASE-02', 'CASE_02_BETTER_PRODUCTS.md'),
                      ('CASE-03', 'CASE_03_ACT_TIRE.md'),
                      ('CASE-04', 'CASE_04_SOCA.md')]:
    path = os.path.join('outputs', 'content', 'case-studies', filename)
    with open(path, 'r', encoding='utf-8') as f:
        case_contents[cid] = f.read()

# 3. Read data.js and parse
with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'window.APP_DATA = '
if text.startswith('//'):
    line1_end = text.find('\n')
    text_data = text[line1_end+1:].strip()
else:
    text_data = text.strip()

if text_data.startswith(prefix):
    text_data = text_data[len(prefix):].strip()
if text_data.endswith(';'):
    text_data = text_data[:-1].strip()

app_data = json.loads(text_data)

# 4. Update data in app_data
app_data['flashcards'] = flashcards_list
app_data['caseContents'] = case_contents

# 5. Write back to outputs/app/data.js
output_js = "// ERP SCM Knowledge Hub - Bundled Datasets for Offline & Standalone Execution\nwindow.APP_DATA = " + json.dumps(app_data, ensure_ascii=False) + ";"
with open('outputs/app/data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print("data.js successfully updated! Size:", os.path.getsize('outputs/app/data.js'))
print("Flashcards count in data.js:", len(app_data['flashcards']))
print("Case contents keys:", list(app_data['caseContents'].keys()))
