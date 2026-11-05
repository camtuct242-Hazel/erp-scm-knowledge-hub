with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

idx = code.find('renderChapterReader:')
idx2 = code.find('toggleChapterCompleted:', idx)
print(code[idx:idx2])
