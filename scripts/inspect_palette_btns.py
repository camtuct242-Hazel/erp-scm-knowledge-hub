with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="exam-palette-grid"')
print(html[idx:idx+800])
