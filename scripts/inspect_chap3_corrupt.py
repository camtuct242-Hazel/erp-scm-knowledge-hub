with open('outputs/content/chapters/CHAP_03.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Mặc dù Case 2.2')
if idx != -1:
    print("Found in CHAP_03.md:")
    print(text[max(0, idx-100):min(len(text), idx+600)])
else:
    print("Not found in CHAP_03.md")
