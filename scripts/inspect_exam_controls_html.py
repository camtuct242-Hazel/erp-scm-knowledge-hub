with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="btn-prev-q"')
print(html[idx:idx+1200])
