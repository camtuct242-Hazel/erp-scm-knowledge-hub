with open('outputs/content/chapters/CHAP_02.md', 'r', encoding='utf-8') as f:
    c2 = f.read()

idx = c2.find('4.2')
if idx != -1:
    print(c2[idx:idx+1500])
