with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('renderCaseStudy:')
if pos != -1:
    print(text[pos:pos+2500])
