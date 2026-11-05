with open('outputs/content/chapters/CHAP_03.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('## 9.')
if idx != -1:
    print("Section 9 in CHAP_03.md:")
    print(text[idx:idx+1500])
