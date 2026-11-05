with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="flashcard-card-element"')
if pos != -1:
    print(text[pos+1000:pos+2000])
