with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
idx = code.find('renderChapterReader:')
print(code[idx:idx+600])

idx2 = code.find('chapterContents')
print("chapterContents references in app.js:")
while idx2 != -1:
    print("  ", code[max(0, idx2-40):min(len(code), idx2+80)])
    idx2 = code.find('chapterContents', idx2+1)
