with open('outputs/content/case-studies/CASE_01_TEXAGO.md', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Management now needs to make a decision')
if pos != -1:
    print(text[pos:pos+1500])
else:
    pos2 = text.find('Questions')
    if pos2 != -1:
        print(text[pos2:pos2+1500])
    else:
        print("Neither found, printing around line 100:")
        lines = text.split('\n')
        print('\n'.join(lines[80:120]))
