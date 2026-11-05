with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Let's inspect where i18n dictionaries are defined
idx_vi = app_js.find('vi: {')
idx_en = app_js.find('en: {')
print("vi starts at:", idx_vi, "en starts at:", idx_en)
