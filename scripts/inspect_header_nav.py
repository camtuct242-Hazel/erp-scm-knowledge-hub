with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
header_idx = html.find('<header')
header_end = html.find('</header>')
print(html[header_idx:header_end+9])
