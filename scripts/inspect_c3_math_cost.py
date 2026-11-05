with open('outputs/content/chapters/CHAP_03.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('chi phí toán học')
while idx != -1:
    print(text[max(0, idx-40):min(len(text), idx+120)])
    idx = text.find('chi phí toán học', idx+1)
