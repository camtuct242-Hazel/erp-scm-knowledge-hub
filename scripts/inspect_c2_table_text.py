with open('outputs/content/chapters/CHAP_02.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('table-responsive')
print(text[idx:idx+800])
