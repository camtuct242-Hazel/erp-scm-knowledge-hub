with open('outputs/content/chapters/CHAP_01.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('4.3')
print(text[idx:idx+1500])
