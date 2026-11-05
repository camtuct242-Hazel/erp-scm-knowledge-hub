with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos_vi = text.find('vi: {')
pos_en = text.find('en: {')
print("vi starts at:", pos_vi)
print("en starts at:", pos_en)
if pos_vi != -1:
    print(text[pos_vi:pos_vi+500])
