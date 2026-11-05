with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

idx_vi = app_js.find('vi: {')
print("VI entries snippet:")
print(app_js[idx_vi:idx_vi+600])
