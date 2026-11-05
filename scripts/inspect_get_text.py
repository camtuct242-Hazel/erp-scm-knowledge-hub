with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('getText:')
if pos != -1:
    print(text[pos:pos+300])

fc_pos = text.find('renderFlashcard:')
if fc_pos != -1:
    print(text[fc_pos:fc_pos+1000])
