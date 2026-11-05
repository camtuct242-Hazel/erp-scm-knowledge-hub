with open('outputs/content/case-studies/CASE_03_ACT_TIRE.md', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Question')
while pos != -1:
    print(text[pos:pos+400])
    print("---")
    pos = text.find('Question', pos+400)
