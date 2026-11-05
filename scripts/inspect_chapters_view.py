with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
idx = html.find('id="view-chapters"')
if idx != -1:
    print(html[idx:idx+2500])
