with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

idx = code.find('renderConsultantView:')
print(code[idx:idx+400])
