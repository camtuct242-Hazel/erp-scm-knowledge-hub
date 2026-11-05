with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('state.flashcardList')
if pos != -1:
    print(text[pos-100:pos+300])
