with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'init\w*:\s*function', text)]
for idx in matches:
    print(text[idx-20:idx+60])
