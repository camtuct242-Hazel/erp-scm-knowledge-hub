with open('outputs/data/chapters.json', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Case 2.2')
while idx != -1:
    print("Match in chapters.json:")
    print(text[max(0, idx-50):min(len(text), idx+250)])
    idx = text.find('Case 2.2', idx+1)
