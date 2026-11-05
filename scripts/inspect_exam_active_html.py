with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="view-exam-active"')
print(html[idx:idx+2000])
