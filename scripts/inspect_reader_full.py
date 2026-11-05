with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="view-chapter-reader"')
idx_end = html.find('id="view-exams"', idx)
print(html[idx:idx_end])
