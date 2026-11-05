with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('const state = {')
if pos != -1:
    print(text[pos:pos+1500])
