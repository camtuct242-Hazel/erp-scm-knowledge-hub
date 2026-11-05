import json, re

# Read all 6 chapters
contents = {}
for i in range(1, 7):
    cid = f'chap-0{i}'
    fn = f'outputs/content/chapters/CHAP_0{i}.md'
    with open(fn, 'r', encoding='utf-8') as f:
        contents[cid] = f.read()

# Load data.js
with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.APP_DATA\s*=\s*(\{.*\});', text, re.DOTALL)
assert m, "APP_DATA not found in data.js"

app_data = json.loads(m.group(1))
app_data['chapterContents'] = contents

new_data_js = f"window.APP_DATA = {json.dumps(app_data, ensure_ascii=False)};\n"

with open('outputs/app/data.js', 'w', encoding='utf-8') as f:
    f.write(new_data_js)

print("data.js synchronized with updated chapterContents!")
for k, v in contents.items():
    print(f"  {k}: {len(v):,} chars, tabs={v.count('\t')}")
