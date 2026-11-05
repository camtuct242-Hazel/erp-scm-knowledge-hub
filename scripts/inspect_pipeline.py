import json, re

with open('outputs/content/chapters/CHAP_01.md', 'r', encoding='utf-8') as f:
    chap1_md = f.read()

idx = chap1_md.find('4.3')
if idx != -1:
    print('--- In CHAP_01.md around 4.3 ---')
    print(chap1_md[idx:idx+1500])

with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()

m = re.search(r'window\.APP_DATA\s*=\s*(\{.*\});', data_js, re.DOTALL)
if m:
    app_data = json.loads(m.group(1))
    chap1_data = app_data.get('chapterContents', {}).get('chap-01', '')
    idx2 = chap1_data.find('4.3')
    if idx2 != -1:
        print('--- In data.js chapterContents[chap-01] around 4.3 ---')
        print(chap1_data[idx2:idx2+1500])
