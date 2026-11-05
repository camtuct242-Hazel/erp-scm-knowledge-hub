with open('outputs/app/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.[a-zA-Z0-9_-]*(?:callout|insight|alert|note|box)[^{]*\{[^}]*\})', css)
for m in matches[:10]:
    print(m)
