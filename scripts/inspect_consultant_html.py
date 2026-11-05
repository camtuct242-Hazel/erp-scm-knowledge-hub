with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="view-consultant"')
if pos != -1:
    print(text[pos:pos+1500])
