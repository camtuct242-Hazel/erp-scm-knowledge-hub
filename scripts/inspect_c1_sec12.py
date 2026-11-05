with open('outputs/content/chapters/CHAP_01.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('## 12. Kiểm tra Đánh giá Kiến thức')
print(text[idx:])
