with open('outputs/content/chapters/CHAP_03.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Nhận xét của BA')
if idx != -1:
    print(text[idx-50:idx+400])
